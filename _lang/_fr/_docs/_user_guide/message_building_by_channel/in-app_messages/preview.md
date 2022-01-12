---
nav_title: Aperçu HTML
article_title: Aperçu du message dans l'application HTML
page_order: 9
description: "Cet article de référence couvre la nouvelle fonctionnalité d'aperçu HTML de la messagerie dans l'application."
channel:
  - messages intégrés à l'application
---

# Aperçu HTML des messages dans l'application

En savoir plus sur les nouvelles fonctionnalités d'aperçu pour les messages personnalisés HTML In-App.

{% sdk_min_versions web:2.5.0 android:8.0.0 ios:3.23.0 %}

{% alert important %}
Il s'agit d'une fonction d'opt-in. Demandez à votre équipe de compte Braze de vous donner accès dès aujourd'hui!
{% endalert %}

## Nouvelles fonctionnalités

### Aperçu interactif

L'écran d'aperçu du message montre maintenant un aperçu plus réaliste qui rend le JavaScript inclus dans votre message.

Cela signifie que vous pouvez maintenant prévisualiser _et interagir_ avec vos messages personnalisés (ex: pagination de clic, soumission de formulaires ou d'enquêtes, regarder des animations JavaScript, etc.)

![Nouveau HTML dans l'aperçu de l'application]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Nous nous assurerons que toutes les méthodes javascript [`appboyBridge`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge) que vous utilisez dans votre HTML ne mettront pas à jour les profils d'utilisateur _lors de la prévisualisation dans le tableau de bord_.
{% endalert %}


### Messages HTML transversaux

Ce nouveau type de message HTML vous permet maintenant de créer un message qui peut être envoyé à la fois sur mobile et sur le web !

![Nouveau message HTML dans l'application Cross Channel]({% image_buster /assets/img/iam-beta-html-cross-channel.png %})

### Nouveau chargeur d'actifs

Téléchargez les ressources de campagne dans la bibliothèque médiatique de Braze à l'aide d'une simple interface de glisser-déposer.

Ce nouveau flux de travail facilite le téléchargement de fichiers et copier/coller leurs URL directement dans votre HTML.

Nous avons également ajouté la possibilité de télécharger les nouveaux types de fichiers, y compris :

| Type de fichier     | Extension de fichier              |
|:------------------- |:--------------------------------- |
| Fichiers de police  | `.ttf`, `.woff`, `.otf`, `.woff2` |
| SVG Images          | `.svg`                            |
| Fichiers Javascript | `.js`                             |
| CSS Files           | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
L'utilisation du CDN de la médiathèque de Braze pour héberger les ressources vous assurera que vos messages sont affichés sur les appareils mobiles, même si un utilisateur a une mauvaise connexion Internet ou hors ligne.
{% endalert %}

### Coloration syntaxique

L'éditeur de code inclut maintenant la coloration syntaxique avec un certain nombre de thèmes de couleurs différents.

Cela aide à repérer facilement les éventuelles erreurs de code directement dans le compositeur de message, et mieux organiser votre code (en utilisant des espaces ou des tabulations - quel que soit le côté de cet argument).

![Nouveau message syntaxique HTML dans l'application]({% image_buster /assets/img/iam-beta-html-syntax-highlighting.png %})

### Améliorations du suivi des boutons

Vous pouvez maintenant suivre les performances dans votre message en utilisant la nouvelle méthode JavaScript [`appboyBridge.logClick(button_id)`][1]. Cela vous permet de suivre par programmation le "Bouton 1", le "Bouton 2" et les "Clics corporels" en utilisant `appboyBridge. ogClick("0")`, `appboyBridge.logClick("1")`, ou `appboyBridge.logClick()`, respectivement.

Cette méthode remplace les méthodes de suivi automatique des clics (c'est-à-dire `?abButtonId=0`) qui ont été supprimées. De plus, les messages HTML In-App ne se limitent plus à l'enregistrement d'un événement de clic par impression.

Par exemple, pour fermer un message et enregistrer le bouton 2 cliqué, vous pouvez utiliser :

```
<a href="#" onclick="appboyBridge.logClick('1');appboyBridge.closeMessage()">✖</a>
```

Vous pouvez également suivre les nouveaux noms de boutons personnalisés - jusqu'à 100 noms uniques par campagne, par exemple `appboyBridge. ogClick("bouton bleu")` ou `appboyBridge.logClick("vu carrousel page 3")`.

#### Exigences

* jusqu'à 100 identifiants de boutons uniques sont autorisés par campagne
* Chaque ID de bouton ne peut pas contenir plus de 255 caractères
* Seuls les caractères alphanumériques, espaces, tirets et tirets bas sont autorisés.

**Remarque**: Cette méthode remplace les méthodes de suivi automatique des clics précédentes (i.e. `?abButtonId=0`) qui ont été supprimées.

## Changements incompatibles vers le bas {#backward-incompatible-changes}

1. Le changement le plus notable incompatible avec ce nouveau type de message est la configuration SDK. Les utilisateurs dont l'App SDK ne répond pas aux exigences minimales de version [SDK](#supported-sdk-versions) ne seront pas affichés le message. <br>

2. The `appboy://close` deeplink which was previously supported on mobile apps has been removed in favor of the Javascript, `appboyBridge.closeMessage()`. Cela permet le cross-platform HTML car le web ne supporte pas les liens profonds.

3. Le suivi automatique des clics, qui a utilisé `?abButtonId=0` pour les identifiants des boutons, et le suivi "body click" sur les boutons de fermeture ont été supprimés. Les exemples de code ci-dessous montrent comment changer votre HTML pour utiliser nos nouvelles méthodes javascript de suivi des clics :

| Avant                     | Après                     |
|:------------------------- |:------------------------- |
| <code>&lt;a href="appboy://close"&gt;Bouton de fermeture&lt;/a&gt;</code> | <code>&lt;a href="#" onclick="appboyBridge.logClick();appboyBridge.closeMessage()"&gt;Bouton de fermeture&lt;/a&gt;</code> |
| <code>&lt;a href="appboy://close?abButtonId=0"&gt;Bouton de fermeture&lt;/a&gt;</code> | <code>&lt;a href="#" onclick="appboyBridge.logClick('0');appboyBridge.closeMessage()"&gt;Bouton de fermeture&lt;/a&gt;</code> |
| <code>&lt;a href="app://deeplink?abButtonId=0">Track button 1&lt;/a&gt;</code> | <code>&lt;a href="app://deeplink" onclick="appboyBridge.logClick('0')"&gt;Piste bouton 1&lt;/a&gt;</code> |
| <code>&lt;script&gt;<br>location.href = "appboy://close?abButtonId=1"<br>&lt;/script&gt;</code> | <code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;appboyBridge.logClick("1");<br>&nbsp;&nbsp;appboyBridge.closeMessage();<br>});<br>&lt;/script&gt;</code> |

## Création d'une nouvelle campagne {#instructions}

### Exigences du SDK {#supported-sdk-versions}

Ces nouvelles fonctionnalités nécessitent la mise à jour vers la version Braze SDK suivante :

{% sdk_min_versions web:2.5.0 android:8.0.0 ios:3.23.0 %}

{% alert warning %}
Parce que ce type de message ne peut être reçu que par certaines versions plus récentes du SDK, les utilisateurs qui sont sur des versions SDK non supportées ne recevront pas le message.

Envisagez d'adopter ce nouveau type de message une fois qu'une portion importante de votre base d'utilisateurs est joignable, ou cibler uniquement les utilisateurs dont la version de l'application est _au-dessus de_ les exigences. [En savoir plus]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)
{% endalert %}

### Nouveau type de message {#new-message-type}

Lors de la création d'un message "Code Personnalisé", choisissez la nouvelle option "Téléchargement HTML avec Aperçu" comme indiqué ci-dessous:

![Nouveau message d'accès anticipé dans l'application HTML]({% image_buster /assets/img/iam-beta-html-dropdown.gif %})

Gardez à l'esprit que les utilisateurs de votre application mobile ont besoin de mettre à niveau vers les versions SDK supportées pour recevoir ce message.

Nous vous recommandons [de pousser les utilisateurs à mettre à jour]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/) leurs applications mobiles avant de lancer des campagnes qui dépendent des nouvelles versions de Braze SDK.

### Téléchargement des fichiers de ressources {#upload-assets}

Utilisez la médiathèque de Braze pour télécharger et héberger des ressources pour vos messages HTML personnalisés.

Nous vous recommandons de télécharger des ressources dans la médiathèque de Braze pour deux raisons :

1. Les actifs ajoutés à une campagne via la médiathèque permettent d'afficher vos messages même lorsque l'utilisateur est hors ligne
2. Les actifs téléchargés sur Braze peuvent être plus facilement réutilisés à travers les campagnes.

Pour ajouter _nouveaux actifs_ à votre campagne, utilisez la section Glisser-déposer pour télécharger un fichier _et_ ajouter associer le fichier à cette campagne.

Vous pouvez également ajouter _ressources_ existantes à votre campagne que vous avez déjà téléchargée dans la médiathèque de Braze en sélectionnant __Ajouter de la médiathèque__.

Une fois vos ressources ajoutées à une campagne, vous pouvez utiliser le bouton _Copier le lien_ pour stocker l'URL du fichier dans votre presse-papiers.

Ensuite, collez l'URL de la ressource copiée dans votre code HTML comme vous le feriez normalement lorsque vous référencez une ressource distante.

{% alert tip %}
Vous pouvez appuyer sur `CTRL+F` ou `CMD+F` dans l'éditeur HTML pour rechercher dans votre code !
{% endalert %}


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#javascript-bridge
