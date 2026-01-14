---
nav_title: Video
article_title: Video en mensajes dentro de la aplicación
page_order: 4
page_type: reference
description: "Este artículo describe cómo incrustar videos en tus mensajes HTML dentro de la aplicación."
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

Para utilizar un activo de video local, asegúrate de incluir este archivo cuando subas activos a tu campaña.

{% alert note %}
El contenido de video sólo está disponible cuando el dispositivo tiene una velocidad de red razonable, a menos que el video proceda del dispositivo localmente.
{% endalert %}

## Consideraciones sobre Android

Para incrustar video y otros contenidos HTML5 en mensajes HTML dentro de la aplicación en Android, es necesario habilitar la aceleración por hardware en la Actividad donde se muestra el mensaje dentro de la aplicación. Para más información, consulta la [guía del desarrollador de Android]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/#android_embedding-youtube-content).

## Consideraciones sobre iOS

Para admitir dispositivos iOS:

- Debes incluir el atributo `playsinline` porque la reproducción a pantalla completa no es compatible por el momento.
- iOS no admite la reproducción automática predeterminada. Para actualizar esta opción predeterminada, puedes modificar la opción [`ABKInAppMessageHTMLViewController`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ViewControllers/ABKInAppMessageHTMLViewController.m)


