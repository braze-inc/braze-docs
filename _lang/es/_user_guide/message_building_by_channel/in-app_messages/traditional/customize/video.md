---
nav_title: Video
article_title: Vídeo en los mensajes de la aplicación
page_order: 4
page_type: reference
description: "Este artículo describe cómo incrustar vídeos en tus mensajes HTML in-app."
channel:
  - in-app messages
---

# Video {#video}

> Para reproducir un video en un mensaje HTML dentro de la aplicación, incluye el siguiente elemento `<video>` en tu HTML, y sustituye los nombres de los videos por el nombre de tu archivo (o la URL del activo remoto). Puedes encontrar otras opciones posibles de `<video>` en [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video).

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

Para utilizar un activo de vídeo local, asegúrese de incluir este archivo al cargar activos en su campaña.

{% alert note %}
El contenido de video solo está disponible cuando el dispositivo tiene una velocidad de red razonable, a menos que el video proceda del dispositivo localmente.
{% endalert %}

## Consideraciones sobre Android

Para incrustar vídeo y otros contenidos HTML5 en mensajes HTML in-app en Android, es necesario activar la aceleración por hardware en la Actividad en la que se muestra el mensaje in-app. Para más información, consulta la [guía del desarrollador de Android]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/#android_embedding-youtube-content).

**reproducción automática**: Incluso con la habilitación de la aceleración por hardware, es posible que Android WebViews requiera un gesto del usuario para iniciar la reproducción multimedia. Si necesitas la reproducción automática, configura WebView, que se utiliza para renderizar mensajes dentro de la aplicación, para desactivar el requisito de gestos del usuario estableciendo [`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean)). Esto requiere una personalización a nivel de SDK de cómo se muestran los mensajes HTML dentro de la aplicación. Para obtener orientación sobre la configuración, consulta [Personalizar mensajes dentro de la aplicación para el SDK de Braze]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).

## Consideraciones sobre iOS

Para ser compatible con dispositivos iOS:

- Debes incluir el`playsinline`atributo porque no se admite la reproducción a pantalla completa.
- **La reproducción automática no está garantizada en iOS**. El comportamiento de reproducción en iOS depende de las políticas multimedia`WKWebView` a nivel del sistema operativo y puede requerir una acción por parte del usuario incluso cuando se hayan realizado`autoplay` las `muted`configuraciones de y . Prueba tu mensaje HTML dentro de la aplicación en las versiones y dispositivos iOS de destino.

Si se requiere la reproducción automática y tus pruebas muestran que no funciona de forma predeterminada, puedes personalizar el mensaje`WKWebViewConfiguration` utilizado por HTML dentro de la aplicación para ajustar el requisito de acción del usuario para la reproducción multimedia, por ejemplo, configurando la`mediaTypesRequiringUserActionForPlayback`propiedad . Esto requiere una personalización a nivel de SDK. Para obtener recursos de SWIFT, consulta [Personalizar mensajes dentro de la aplicación para el SDK de Braze]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift) y [Añadir la interfaz JavaScript de Braze a WebViews para SWIFT]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/?sdktab=swift).

## Consideraciones sobre la Web

La mayoría de los navegadores modernos solo permiten la reproducción automática en determinadas condiciones (normalmente, cuando el video está silenciado). Si utilizas`autoplay`  en un mensaje dentro de la aplicación, incluye`muted`  y realiza pruebas en todos los navegadores y dispositivos compatibles, ya que las políticas de los navegadores varían y, en algunos casos, pueden seguir requiriendo una acción por parte del usuario.