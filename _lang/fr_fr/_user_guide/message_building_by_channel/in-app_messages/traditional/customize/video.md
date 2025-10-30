---
nav_title: Vidéo
article_title: Vidéo dans les messages in-app
page_order: 4
page_type: reference
description: "Cet article explique comment intégrer des vidéos dans vos messages HTML in-app."
channel:
  - in-app messages
---

# Vidéo {#video}

> Pour lire une vidéo dans un message in-app HTML, incluez l'élément `<video>` suivant dans votre HTML, et remplacez les noms des vidéos par le nom de votre fichier (ou l'URL de la ressource distante). Vous pouvez trouver d'autres options possibles pour `<video>` sur [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video).

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

Pour utiliser une ressource vidéo locale, veillez à inclure ce fichier lorsque vous téléchargez des ressources dans votre campagne.

{% alert note %}
Le contenu vidéo n'est disponible que lorsque l'appareil dispose d'une vitesse de réseau raisonnable, à moins que la vidéo ne provienne de l'appareil localement.
{% endalert %}

## Considérations sur Android

Pour intégrer des vidéos et d'autres contenus HTML5 dans les messages in-app sur Android, l'accélération matérielle doit être activée dans l'activité où le message in-app est affiché. Pour plus d'informations, consultez le [guide du développeur Android]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/#android_embedding-youtube-content).

## Considérations relatives à l'iOS

Pour prendre en charge les appareils iOS :

- Vous devez inclure l'attribut `playsinline` car la lecture en plein écran n'est pas prise en charge pour le moment.
- iOS ne prend pas en charge la lecture automatique par défaut. Pour mettre à jour cette option par défaut, vous pouvez modifier l'option [`ABKInAppMessageHTMLViewController`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ViewControllers/ABKInAppMessageHTMLViewController.m)


