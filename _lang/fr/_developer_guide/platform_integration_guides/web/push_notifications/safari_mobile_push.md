---
nav_title: Notification push Web Safari Mobile
article_title: Notification push Web Safari Mobile
platform: Web
channel: push
page_order: 5
page_type: reference
description: "Découvrez comment intégrer les notifications push Web sur vos navigateurs Safari iOS et iPad."
search_rank: 3
---

# Notification push Web Safari Mobile (iOS et iPadOS)

[Safari v16.4][safari-release-notes] prend en charge les notifications push Web mobiles, ce qui signifie que vous pouvez désormais réengager les utilisateurs mobiles avec des notifications push sur iOS et iPadOS.

Cet article vous guidera à travers les étapes requises pour configurer les notifications push mobiles pour Safari.

## Étapes d’intégration

Tout d’abord, veuillez lire et suivre notre [guide d’intégration des notifications push Web][web-push-integration] standard. Les étapes suivantes ne sont nécessaires que pour prendre en charge les notifications push Web sur Safari pour la prise en charge d’iOS et d’iPadOS.

### Étape 1 : Créer un fichier de manifeste {#manifest}

Un [manifeste d’application Web][manifest-file] est un fichier JSON qui contrôle la façon dont votre site Web est présenté lorsqu’il est installé sur l’écran d’accueil d’un utilisateur.

Par exemple, vous pouvez définir la couleur et l’icône du thème d’arrière-plan que l’[App Switcher][app-switcher] utilise, qu’il se présente en plein écran pour ressembler à une application native, ou que l’application s’ouvre en mode paysage ou portrait.

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

La liste complète des champs pris en charge est disponible [ici][manifest-file].

### Étape 2 : Lier le fichier de manifeste {#manifest-link}

Ajouter les balises suivantes `<link>` à l’élément `<head>` de votre site Web pointant vers l’endroit où votre fichier de manifeste est hébergé.

```html
<link rel="manifest" href="/manifest.json" />
```

### Étape 3 : Ajouter un service de traitement {#service-worker}

Votre site Web doit disposer d’un fichier de service de traitement qui importe la bibliothèque de services de traitement de Braze, comme décrit dans notre [guide d’intégration des notifications push Web][service-worker].

### Étape 4 : Ajouter à l’écran d’accueil {#add-to-homescreen}

Contrairement aux principaux navigateurs comme Chrome et Firefox, vous n’êtes pas autorisé à demander une autorisation de notification push sur Safari iOS/iPadOS, sauf si votre site Web a été ajouté à l’écran d’accueil de l’utilisateur. 

La fonctionnalité [Ajouter à l’écran d’accueil][add-to-homescreen] permet aux utilisateurs de mettre en favori votre site web, en ajoutant votre icône à leur précieux espace d’écran d’accueil.

![Un iPhone affichant les options permettant de mettre en favori un site Web et de l’enregistrer sur l’écran d’accueil][add-to-homescreen-img]{: style="max-width:40%"}

### Étape 5 : Afficher l’invite de notification push native {#push-prompt}
Une fois que l’application a été ajoutée à votre écran d’accueil, vous pouvez maintenant demander une autorisation des notifications push lorsque l’utilisateur effectue une action (comme cliquer sur un bouton). Cela peut être fait à l’aide de la méthode [`requestPushPermission`][requestPushPermission], ou avec un [message in-app d’amorce de notification push sans code][push-primer].

{% alert note %}
Une fois que vous avez accepté ou refusé l’invite, vous devrez supprimer et réinstaller le site Web sur votre écran d’accueil pour pouvoir l’afficher à nouveau.
{% endalert %}

![Une invite de notification push demandant d’« autoriser » ou de « ne pas autoriser » les notifications][2]{: style="max-width:40%"}

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

Ensuite, envoyez-vous un [message de test][test-message] pour valider l’intégration. Une fois votre intégration terminée, vous pouvez utiliser nos [message d’amorce de notification push sans code][push-primer] pour optimiser votre taux d’abonnement aux notifications push.

[webkit-release-notes]: https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/
[safari-release-notes]: https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes
[manifest-file]: https://developer.mozilla.org/en-US/docs/Web/Manifest
[app-switcher]: https://support.apple.com/en-us/HT202070
[add-to-homescreen]: https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc
[web-push-integration]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/
[service-worker]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-1-configure-your-sites-service-worker
[test-message]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/
[push-primer]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/
[requestPushPermission]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission
[1]: {% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}
[2]: {% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}
