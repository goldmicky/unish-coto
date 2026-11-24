"""Render static HTML. All contact values come from site.config.json. No network."""
from pathlib import Path
import json,html,re
ROOT=Path(__file__).resolve().parents[1]
def main():
    config=json.loads((ROOT/'site.config.json').read_text(encoding='utf-8'))
    if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+",config['email']):raise ValueError('Invalid support email')
    for source in (ROOT/'templates').glob('*.html'):
        text=source.read_text(encoding='utf-8')
        for key,value in config.items():text=text.replace('{{'+key+'}}',html.escape(str(value),quote=True))
        if '{{' in text:raise ValueError('Unresolved template value')
        (ROOT/source.name).write_text(text,encoding='utf-8')
    print('Static pages built. Privacy and contact remain readable without JavaScript.')
if __name__=='__main__':main()
