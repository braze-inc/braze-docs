---
nav_title: Video
article_title: Video in In-App-Nachrichten
page_order: 4
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie Videos in Ihre HTML-In-App-Nachrichten einbetten können."
channel:
  - in-app messages
---

# Video {#video}

> Um ein Video in einer HTML-In-App-Nachricht abzuspielen, fügen Sie das folgende `<video>`-Element in Ihr HTML ein und ersetzen die Videonamen durch den Namen Ihrer Datei (oder die URL des Remote-Assets). Weitere mögliche Optionen finden Sie unter `<video>` auf [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video).

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

Wenn Sie ein lokales Video-Asset verwenden möchten, müssen Sie diese Datei beim Hochladen von Assets in Ihre Kampagne angeben.

{% alert note %}
Video-Content ist nur verfügbar, wenn das Gerät über eine angemessene Netzwerkgeschwindigkeit verfügt, es sei denn, das Video wird lokal vom Gerät abgerufen.
{% endalert %}

## Überlegungen zu Android

Um Videos und anderen HTML5-Content in HTML-In-App-Nachrichten auf Android einzubetten, muss die Hardwarebeschleunigung in der Aktivität aktiviert werden, in der die In-App-Nachricht angezeigt wird. Weitere Informationen finden Sie im [Android-Entwicklerhandbuch]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/#android_embedding-youtube-content).

## Überlegungen zu iOS

Zur Unterstützung von iOS-Geräten:

- Sie müssen das Attribut `playsinline` einfügen, da die Wiedergabe im Vollbildmodus derzeit noch nicht unterstützt wird.
- iOS unterstützt standardmäßig keine automatische Wiedergabe. Um diese Standardoption zu aktualisieren, können Sie die Option [`ABKInAppMessageHTMLViewController`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ViewControllers/ABKInAppMessageHTMLViewController.m) ändern.


