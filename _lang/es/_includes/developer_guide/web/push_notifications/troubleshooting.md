## Solución de problemas

Si tienes problemas después de configurar las notificaciones push, ten en cuenta lo siguiente:

- Las notificaciones push web requieren que tu sitio sea HTTPS.
- No todos los exploradores pueden recibir mensajes push. Asegúrate de que `braze.isPushSupported()` devuelve `true` en el navegador.
- Algunos navegadores, como Firefox, no muestran imágenes en las notificaciones push. Para más detalles sobre la compatibilidad con navegadores, consulta la [documentación MDN de Imágenes de notificación](https://developer.mozilla.org/en-US/docs/Web/API/Notification/image).
- Si un usuario ha denegado el acceso push a un sitio, no se le volverá a pedir permiso a menos que elimine el estado denegado de las preferencias de su navegador.
