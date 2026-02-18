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

**reproducción automática**: Incluso con la aceleración por hardware habilitada, las WebViews de Android pueden requerir un gesto del usuario para iniciar la reproducción multimedia. Si necesitas la reproducción automática, configura el WebView utilizado para mostrar mensajes HTML dentro de la aplicación para desactivar el requisito de gesto del usuario configurando [`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean)). Esto requiere una personalización a nivel de SDK de cómo se muestran los mensajes HTML dentro de la aplicación. Para obtener instrucciones de configuración, consulta [Personalizar mensajes dentro de la aplicación para el SDK de Braze]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).

## Consideraciones sobre iOS

Para ser compatible con dispositivos iOS:

- Debes incluir el atributo `playsinline` porque no se admite la reproducción a pantalla completa.
- La **reproducción automática no está garantizada en** iOS. El comportamiento de la reproducción en iOS depende de las políticas multimedia de `WKWebView` y del sistema operativo, y puede requerir un gesto del usuario incluso cuando `autoplay` y `muted` están configurados. Prueba tu mensaje HTML dentro de la aplicación en las versiones y dispositivos iOS de destino.

Si la reproducción automática es necesaria y tus pruebas muestran que no funciona de forma predeterminada, puedes personalizar el `WKWebViewConfiguration` utilizado por los mensajes HTML dentro de la aplicación para ajustar el requisito de acción del usuario de reproducción multimedia, por ejemplo, configurando la propiedad `mediaTypesRequiringUserActionForPlayback`. Esto requiere una personalización a nivel del SDK. Para obtener recursos de Swift, consulta [Personalizar mensajes dentro de la aplicación para el SDK de Braze]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift) y [Añadir la interfaz JavaScript de Braze a WebViews para Swift]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/?sdktab=swift).

## Consideraciones sobre la Web

La mayoría de los navegadores modernos sólo permiten la reproducción automática en determinadas condiciones (normalmente cuando el video está silenciado). Si utilizas `autoplay` en un mensaje dentro de la aplicación Web, incluye `muted` y pruébalo en los navegadores y dispositivos compatibles, ya que las políticas de los navegadores varían y, en algunos casos, pueden requerir un gesto del usuario.