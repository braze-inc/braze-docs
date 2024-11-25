---
nav_title: Support AMP
article_title: Support AMP pour le Web
platform: Web
page_order: 5
page_type: reference
description: "Cet article de référence décrit le support AM pour le Web et comment intégrer Braze sur une page AMP."

---

# Support AMP

{% alert note %}
Cette section n’est pas nécessaire à l’intégration, sauf si vous essayez d’intégrer Braze sur une page AMP.
{% endalert %}

> Cet article de référence décrit le support AM pour le Web et comment intégrer Braze sur une page AMP. Les pages mobiles accélérées (AMP) sont un projet soutenu par Google conçu pour améliorer le temps de chargement des pages sur les appareils mobiles en appliquant certaines normes, notamment en limitant l’utilisation de JavaScript.

Par conséquent, le SDK Braze ne peut pas être chargé sur une page AMP. Cependant, le projet AMP fournit un composant prenant en charge les notifications push pour le Web. Les [instructions suivantes](https://www.ampproject.org/docs/reference/components/amp-web-push) expliquent comment configurer ce composant et faire référence à la documentation suivante sur le composant `amp-web-push`.

## Étape 1 : Inclure le script de notification push pour le Web en AMP

Ajoutez la balise de script asynchrone suivante à votre en-tête :

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

## Étape 2 : Ajouter un widget d’abonnement et de désabonnement

Vous devez ajouter un widget qui permet aux utilisateurs de s’abonner et de se désabonner des notifications push. On doit trouver ceci au sein de votre corps HTML et le code peut être stylisé comme vous le désirez.

```js
<!-- A subscription widget -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Subscribe to Notifications</button>
</amp-web-push-widget>

<!-- An unsubscription widget -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Unsubscribe from Notifications</button>
</amp-web-push-widget>
```

## Étape 3 : Télécharger le facilitateur iFrame et la boîte de dialogue d’autorisation

Le composant de notification push pour le Web en AMP fonctionne en créant une fenêtre contextuelle qui gère l’abonnement aux notifications push. Par conséquent, vous devrez inclure quelques fichiers facilitateurs dans votre projet. Téléchargez le fichier [helper-iframe.html](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html) et le fichier [permission-dialog.html](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html) et enregistrez-les sur votre site.

## Étape 4 : Créer un fichier de service de traitement

Créez un fichier `service-worker.js` avec le contenu suivant et placez-le dans le répertoire racine de votre site Internet :

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Étape 5 : Configurer l’élément HTML des notifications push pour le Web en AMP

Vous devez maintenant ajouter l’élément HTML `amp-web-push` à votre page. Déposez le code HTML suivant dans le corps de votre document :

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey={YOUR_API_KEY}&baseUrl={YOUR_BASE_URL}"
>
```

En particulier, l’`service-worker-URL` nécessite d'ajouter votre `apiKey` et `baseUrl` (https://dev.appboy.com/api/v3) en tant que paramètres de requête.

L’abonnement et le désabonnement aux notifications push sur votre page AMP devraient être configurés.
