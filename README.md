# Unish Coto ? sitio oficial

Sitio est?tico en espa?ol para la marca Unish Coto y Calendario Minero. HTML5, CSS y JavaScript nativo, sin dependencias de ejecuci?n, publicidad, anal?tica ni formularios.

## Direcciones de GitHub Pages

- Inicio: https://goldmicky.github.io/unish-coto/
- Privacidad: https://goldmicky.github.io/unish-coto/privacidad.html
- Soporte: https://goldmicky.github.io/unish-coto/soporte.html

El despliegue se configura en **Settings ? Pages ? Deploy from a branch ? main ? /(root)**. No usa dominios ni servicios de pago. El estado efectivo del despliegue y la comprobaci?n HTTPS se registran por separado; una URL prevista no demuestra publicaci?n.

## Edici?n y contacto centralizado

Editar `site.config.json` para cambiar el correo p?blico, la marca o la URL base. Despu?s ejecutar:

```sh
python tools/build_site.py
python tools/check_site.py
```

Los archivos de `templates/` son las fuentes de las tres p?ginas. El generador produce HTML completo en la ra?z. El correo y la pol?tica son legibles sin JavaScript: no dependen de una petici?n JSON ni de un renderizado en el navegador. Confirmar el diff antes de hacer commit.

Vista previa local:

```sh
python -m http.server 8876 --bind 127.0.0.1
```

Abrir http://127.0.0.1:8876/. Comprobar m?vil y escritorio, teclado y reducci?n de movimiento. El men? se adapta y la navegaci?n permanece disponible sin JavaScript.

## Recursos y seguridad

Solo se reutilizan el icono, dos poses WebP originales de Minerito y cuatro capturas aprobadas con datos sint?ticos. Los recursos se conservaron sin sustituir personajes. El monograma UC es tipogr?fico. No se incluye c?digo Flutter, APK/AAB, SQLite, configuraci?n Firebase, diagn?sticos Android, claves o credenciales.

La carpeta `.local/` est? ignorada y nunca debe publicarse. La revisi?n de archivos y la lista p?blica se registran all?, fuera del commit. Las credenciales Git deben permanecer en Git Credential Manager; nunca en archivos, remotos ni comandos con tokens.

La pol?tica describe la compilaci?n offline de Calendario Minero 1.0.0: perfil y SQLite locales, servicios Firebase incluidos pero inactivos, sin publicidad ni rastreo propio. Distingue el correo de soporte y los registros t?cnicos del alojamiento GitHub Pages. La presencia de un permiso de Internet no se presenta como prueba de transmisi?n de calendarios.

## Referencias revisadas

- [Google Play ? Datos de usuario y pol?tica de privacidad](https://support.google.com/googleplay/android-developer/answer/10144311?hl=es)
- [GitHub ? Fuente de publicaci?n Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [GitHub ? Privacidad del alojamiento](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)

Revisadas el 24/11/2026. Este sitio no publica la aplicaci?n en Google Play ni garantiza su aprobaci?n por Google.
