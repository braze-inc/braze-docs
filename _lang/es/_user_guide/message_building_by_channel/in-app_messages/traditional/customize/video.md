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

## Consideraciones sobre iOS

Para ser compatible con dispositivos iOS:

- Debe incluir el atributo `playsinline` porque la reproducción a pantalla completa no es compatible por el momento.
- iOS no admite la reproducción automática por defecto. Para actualizar esta opción por defecto, puede modificar la opción [`ABKInAppMessageHTMLViewController`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ViewControllers/ABKInAppMessageHTMLViewController.m)


