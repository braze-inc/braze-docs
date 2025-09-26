---
nav_title: Vidéo
article_title: Vidéo dans les messages in-app
page_order: 4
page_type: reference
description: "Le présent article décrit comment intégrer des vidéos dans vos messages in-app HTML."
channel:
  - in-app messages
---

# Vidéo {#video}

> Pour lire une vidéo dans un message in-app HTML, incluez les éléments suivants `<video>` dans votre HTML, et remplacez le nom de la vidéo par celui de votre fichier (ou l’URL de la ressource distante). Pour connaître d'autres options `<video>` possibles, consultez la [documentation Web MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video).

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

Pour utiliser une ressource vidéo locale, assurez-vous d’inclure ce fichier lors du téléchargement de ressources dans votre campagne.

{% alert note %}
Le contenu vidéo n’est disponible que si l’appareil dispose d’une vitesse réseau suffisante, sauf si la vidéo provient localement de cet appareil.
{% endalert %}

## Considérations relatives à Android

Pour intégrer des vidéos et autres contenus HTML5 dans des messages in-app HTML sur Android, l’accélération matérielle est requise dans l’activité où le message in-app s’affiche. Pour plus d'informations, consultez le [guide du développeur Android]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/#android_embedding-youtube-content).

## Considérations relatives à iOS

Pour prendre en charge les appareils iOS :

- Vous devez inclure l'attribut `playsinline` car la lecture en plein écran n'est pas prise en charge pour le moment.
- iOS ne prend pas en charge la lecture automatique par défaut. Pour mettre à jour cette option par défaut, vous pouvez modifier le [`ABKInAppMessageHTMLViewController`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ViewControllers/ABKInAppMessageHTMLViewController.m)


