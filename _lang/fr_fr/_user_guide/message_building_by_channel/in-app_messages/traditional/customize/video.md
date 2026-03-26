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

**lecture automatique** : Même lorsque l'accélération matérielle est activée, les WebViews Android peuvent nécessiter une action de l'utilisateur pour démarrer la lecture multimédia. Si vous avez besoin de la lecture automatique, veuillez configurer le WebView utilisé pour afficher les messages in-app HTML afin de désactiver l'exigence de geste de l'utilisateur en définissant [`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean)). Cela nécessite une personnalisation au niveau du SDK de la manière dont les messages in-app HTML sont affichés. Pour obtenir des conseils de configuration, veuillez consulter [la section Personnaliser les messages in-app pour le SDK Braze]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).

## Considérations relatives à iOS

Pour prendre en charge les appareils iOS :

- Il est nécessaire d'inclure `playsinline`l'attribut car la lecture en plein écran n'est pas prise en charge.
- **La lecture automatique n'est pas garantie sur iOS**. Le comportement de lecture iOS dépend des paramètres`WKWebView`et des politiques multimédias au niveau du système d'exploitation, et peut nécessiter une action de l'utilisateur même lorsque`autoplay`et`muted`sont activés. Veuillez tester votre message in-app sur les versions iOS et les appareils cibles.

Si la lecture automatique est requise et que vos tests indiquent qu'elle ne fonctionne pas par défaut, vous pouvez personnaliser l'élément`WKWebViewConfiguration`utilisé par les messages in-app afin d'ajuster l'exigence d'action de l'utilisateur pour la lecture multimédia, par exemple en définissant la`mediaTypesRequiringUserActionForPlayback`propriété. Cela nécessite une personnalisation au niveau du SDK. Pour les ressources Swift, veuillez consulter [Personnaliser les messages in-app pour le SDK Braze]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift) et [Ajouter l'interface JavaScript Braze aux WebViews pour Swift]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/?sdktab=swift).

## Considérations relatives au Web

La plupart des navigateurs modernes n'autorisent la lecture automatique que sous certaines conditions (généralement lorsque le son de la vidéo est désactivé). Si vous utilisez`autoplay`  dans un message in-app, veuillez inclure`muted`  et effectuer des tests sur tous les navigateurs et appareils pris en charge, car les politiques des navigateurs varient et peuvent encore nécessiter une action de la part de l'utilisateur dans certains cas.