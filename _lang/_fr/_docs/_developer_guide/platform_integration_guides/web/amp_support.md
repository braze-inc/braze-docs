---
nav_title: Support AMP
article_title: Support AMP pour le Web
platform: Web
page_order: 5
page_type: Référence
description: "Cet article de référence décrit comment intégrer Braze sur une page AMP."
---

# Support AMP

**Cette section n'est PAS une étape d'intégration nécessaire sauf si vous essayez d'intégrer Braze sur une page AMP.**

Les pages mobiles accélérées (AMP) est un projet soutenu par Google conçu pour améliorer le temps de chargement des pages sur les appareils mobiles en appliquant certaines normes, y compris restreindre l'utilisation de JavaScript.

En conséquence, le Braze SDK ne peut pas être chargé sur une page AMP. Cependant, le projet AMP fournit un composant qui supporte le Web push. Les instructions suivantes détaillent comment configurer ce composant et référencer la documentation suivante sur le composant `amp-web-push` : https://www.ampproject.org/docs/reference/components/amp-web-push

## Étape 1 : Inclure le script AMP web push

Ajoute la balise de script async suivante à votre tête :

```
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

## Étape 2 : Ajouter un widget d'abonnement / de désabonnement

Vous devrez ajouter un widget qui permet aux utilisateurs de s'abonner et de se désabonner de push. Cela devrait vivre dans le corps de votre HTML et peut être stylisé comme bon vous semble.

```
<! - Un widget d'abonnement -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Abonnez-vous aux Notifications</button>
</amp-web-push-widget>

<! - Un widget de désabonnement -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Se désabonner des Notifications</button>
</amp-web-push-widget>
```

## Étape 3 : Télécharger le dialogue IFrame & Permission

Le composant AMP Web Push fonctionne en créant une popup qui gère l'abonnement push. Par conséquent, vous devrez inclure quelques fichiers d'aide dans votre projet. Téléchargez le fichier [helper-iframe.html](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html) et le fichier [permission-dialog.html](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html) et stockez-les sur votre site.

## Étape 4 : Créer un fichier de travail de service

Créez un fichier `service-worker.js` avec le contenu ci-dessous, et placez-le à la racine de votre site Web.

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2FAppboy%2Fappboy-web-sdk%2Fblob%2Fmaster%2Fsample-build%2Fservice-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Étape 5 : Configurer l'élément HTML de push web AMP

Vous devrez maintenant ajouter l'élément html amp-web-push à votre page. Déposez le code HTML suivant dans le corps de votre document :

```
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey=YOUR_API_KEY&baseUrl=YOUR_BASE_URL"
>
```

En particulier, le service-worker-URL nécessite d'ajouter votre apiKey et baseUrl (https://dev.appboy.com/api/v3) en tant que paramètres de requête, comme indiqué ci-dessus.

Vous devriez maintenant être configuré pour l'abonnement push et la désinscription sur votre page AMP. 
