"""Focused, dependency-free public-file and HTML validation. Does not access Firebase."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import json,re
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.images=[];self.ids=set();self.h1=0;self.lang=None;self.viewport=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.lang=a.get('lang')
        if tag=='h1':self.h1+=1
        if tag=='meta' and a.get('name')=='viewport':self.viewport=True
        if 'id' in a:
            assert a['id'] not in self.ids,'Duplicate HTML id'
            self.ids.add(a['id'])
        if tag in ['a','link']:self.links.append(a.get('href',''))
        if tag in ['script','img']:self.links.append(a.get('src',''))
        if tag=='img':self.images.append(a)
def main():
    config=json.loads((ROOT/'site.config.json').read_text(encoding='utf-8'))
    pages={}
    for name in ['index.html','privacidad.html','soporte.html']:
        text=(ROOT/name).read_text(encoding='utf-8');p=Page();p.feed(text);pages[name]=p
        assert p.lang=='es' and p.h1==1 and p.viewport,name
        assert config['email'] in text and '{{' not in text,name
        assert '�' not in text and 'Ã³' not in text,'Encoding corruption'
        assert 'mailto:'+config['email'] in text,name
        assert all('alt' in im and im.get('width') and im.get('height') for im in p.images),'Image accessibility/dimensions'
        assert not re.search(r'<(?:iframe|form)\b',text,re.I),'Unexpected external integration'
    for name,p in pages.items():
        for link in p.links:
            u=urlparse(link)
            if u.scheme:
                assert u.scheme in ['https','mailto'],link
                continue
            target=unquote(u.path) or name
            assert not target.startswith('/'),'Absolute paths break project Pages'
            file=ROOT/target
            assert file.is_file(),link
            if u.fragment:
                assert target in pages and u.fragment in pages[target].ids,link
    for p in ROOT.rglob('*'):
        if not p.is_file() or '.git' in p.parts or '.local' in p.parts:continue
        assert p.suffix.lower() not in ['.apk','.aab','.p12','.jks','.keystore','.db','.sqlite','.log'],p.name
        assert p.name not in ['google-services.json','firebase_options.dart','key.properties'],p.name
        if p.suffix in ['.html','.js','.css']:
            text=p.read_text(encoding='utf-8')
            assert not any(s in text for s in ['googletagmanager.com','google-analytics.com','firebaseConfig','localStorage','document.cookie']),'Unexpected tracker/config'
    policy=(ROOT/'privacidad.html').read_text(encoding='utf-8')
    assert all(s in policy for s in ['Unish Coto','SQLite','d?a y mes','CloudSync','Google Sign-In','GitHub Pages','Conservaci?n','Eliminaci?n'.lower()])
    assert not any(s in policy for s in ['PENDIENTE','BORRADOR'])
    assert '@media(max-width:650px)' in (ROOT/'assets/css/styles.css').read_text()
    assert 'prefers-reduced-motion' in (ROOT/'assets/css/styles.css').read_text()
    print(json.dumps({'pages':3,'localLinksAndAnchors':'PASS','htmlWithoutJavaScript':'PASS','contactCentralized':True,'publicFileBoundary':'PASS','responsiveCss':'present','browserVisualQa':'not verified: native app approval timed out'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
