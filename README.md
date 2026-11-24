# Unish Coto · sitio oficial

Sitio estático en español para la marca Unish Coto y Calendario Minero. HTML5, CSS y JavaScript nativo, sin dependencias de ejecución, publicidad, analítica ni formularios.

## Direcciones de GitHub Pages

- Inicio: https://goldmicky.github.io/unish-coto/
- Privacidad: https://goldmicky.github.io/unish-coto/privacidad.html
- Soporte: https://goldmicky.github.io/unish-coto/soporte.html

El despliegue se configura en **Settings → Pages → Deploy from a branch → main → /(root)**. No usa dominios ni servicios de pago. El estado efectivo del despliegue y la comprobación HTTPS se registran por separado; una URL prevista no demuestra publicación.

## Edición y contacto centralizado

Editar `site.config.json` para cambiar el correo público, la marca o la URL base. Después ejecutar:

```sh
python tools/build_site.py
python tools/check_site.py
```

Los archivos de `templates/` son las fuentes de las tres páginas. El generador produce HTML completo en la raíz. El correo y la política son legibles sin JavaScript: no dependen de una petición JSON ni de un renderizado en el navegador. Confirmar el diff antes de hacer commit.

Vista previa local:

```sh
python -m http.server 8876 --bind 127.0.0.1
```

Abrir http://127.0.0.1:8876/. Comprobar móvil y escritorio, teclado y reducción de movimiento. El menú se adapta y la navegación permanece disponible sin JavaScript.

## Recursos y seguridad

Solo se reutilizan el icono, dos poses WebP originales de Minerito y cuatro capturas aprobadas con datos sintéticos. Los recursos se conservaron sin sustituir personajes. El monograma UC es tipográfico. No se incluye código Flutter, APK/AAB, SQLite, configuración Firebase, diagnósticos Android, claves o credenciales.

La carpeta `.local/` está ignorada y nunca debe publicarse. La revisión de archivos y la lista pública se registran allí, fuera del commit. Las credenciales Git deben permanecer en Git Credential Manager; nunca en archivos, remotos ni comandos con tokens.

La política describe la compilación offline de Calendario Minero 1.0.0: perfil y SQLite locales, servicios Firebase incluidos pero inactivos, sin publicidad ni rastreo propio. Distingue el correo de soporte y los registros técnicos del alojamiento GitHub Pages. La presencia de un permiso de Internet no se presenta como prueba de transmisión de calendarios.

## Referencias revisadas

- [Google Play · Datos de usuario y política de privacidad](https://support.google.com/googleplay/android-developer/answer/10144311?hl=es)
- [GitHub · Fuente de publicación Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [GitHub · Privacidad del alojamiento](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)

Revisadas el 24/11/2026. Este sitio no publica la aplicación en Google Play ni garantiza su aprobación por Google.
