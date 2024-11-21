---
nav_title: Notification push Web Safari Mobile
article_title: Notification push Web Safari Mobile
platform: Web
channel: push
page_order: 5
page_type: reference
description: "Cet article de référence indique comment intégrer les notifications push Web sur vos navigateurs Safari iOS et iPad."
search_rank: 3
---

# Notification push Web Safari Mobile (iOS et iPadOS)

> [Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) prend en charge les notifications push Web mobiles, ce qui signifie que vous pouvez désormais réengager les utilisateurs mobiles avec des notifications push sur iOS et iPadOS.<br><br>Cet article vous guidera à travers les étapes requises pour configurer les notifications push mobiles pour Safari.

## Étapes d’intégration

Tout d’abord, veuillez lire et suivre notre [guide d’intégration des notifications push Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/) standard. Les étapes suivantes ne sont nécessaires que pour prendre en charge les notifications push Web sur Safari pour la prise en charge d’iOS et d’iPadOS.

### Étape 1 : Créer un fichier de manifeste {#manifest}

Un [manifeste d'application web](https://developer.mozilla.org/en-US/docs/Web/Manifest) est un fichier JSON qui contrôle la manière dont votre site web est présenté lorsqu'il est installé sur l'écran d'accueil d'un utilisateur.

Par exemple, vous pouvez définir la couleur du thème d'arrière-plan et l'icône que l'[App Switcher](https://support.apple.com/en-us/HT202070) utilise, si le rendu est en plein écran pour ressembler à une application native, ou si l'application doit s'ouvrir en mode paysage ou portrait.

Créez un nouveau fichier `manifest.json` dans le répertoire racine de votre site Web, avec les champs obligatoires suivants. 

```json
{
  "name": "your app name",
  "short_name": "your app name",
  "display": "fullscreen",
  "icons": [{
    "src": "favicon.ico",
    "sizes": "128x128",
  }]
}
```

La liste complète des champs pris en charge est disponible [ici.](https://developer.mozilla.org/en-US/docs/Web/Manifest)

### Étape 2 : Lier le fichier de manifeste {#manifest-link}

Ajouter la balise suivante `<link>` à l’élément `<head>` de votre site Web pointant vers l’endroit où votre fichier de manifeste est hébergé.

```html
<link rel="manifest" href="/manifest.json" />
```

### Étape 3 : Ajouter un service de traitement {#service-worker}

Votre site Web doit disposer d’un fichier de service de traitement qui importe la bibliothèque de services de traitement de Braze, comme décrit dans notre [guide d’intégration des notifications push Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-1-configure-your-sites-service-worker).

### Étape 4 : Ajouter à l’écran d’accueil {#add-to-homescreen}

Contrairement aux principaux navigateurs comme Chrome et Firefox, vous n’êtes pas autorisé à demander une autorisation de notification push sur Safari iOS/iPadOS, sauf si votre site Web a été ajouté à l’écran d’accueil de l’utilisateur. 

La fonctionnalité [Ajouter à l’écran d’accueil](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) permet aux utilisateurs de mettre en favori votre site Web, en ajoutant votre icône à leur précieux espace d’écran d’accueil.

![Un iPhone montrant les options permettant de mettre un site web en signet et de l'enregistrer sur l'écran d'accueil]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### Étape 5 : Afficher l’invite de notification push native {#push-prompt}
Une fois que l’application a été ajoutée à votre écran d’accueil, vous pouvez maintenant demander une autorisation des notifications push lorsque l’utilisateur effectue une action (comme cliquer sur un bouton). Ceci peut être effectué à l’aide de la méthode [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission) ou à l'aide d'un [message in-app d'amorce de notification push sans code]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/).

{% alert note %}
Une fois que vous avez accepté ou refusé l’invite, vous devrez supprimer et réinstaller le site Web sur votre écran d’accueil pour pouvoir l’afficher à nouveau.
{% endalert %}

![Une notification push demandant d'"autoriser" ou de "ne pas autoriser" les notifications]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

Par exemple :

```typescript
import { requestPushPermission } from "@braze/web-sdk";

button.onclick = function(){
    requestPushPermission(() => {
        console.log(`User accepted push prompt`);
    }, (temporary) => {
        console.log(`User ${temporary ? "temporarily dismissed" : "permanently denied"} push prompt`);
    });
};
```


## Étapes suivantes

Ensuite, envoyez-vous un [message de test]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) pour valider l'intégration. Une fois votre intégration terminée, vous pouvez utiliser nos [messages d'amorce de notification push sans code]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/) pour optimiser vos taux d'abonnement aux notifications push.

