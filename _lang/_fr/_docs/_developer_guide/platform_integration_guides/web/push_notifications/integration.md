---
nav_title: Intégration
article_title: Intégration Push pour le Web
platform: Web
channel: Pousser
page_order: 0
page_type: Référence
description: "Cet article décrit comment intégrer Braze Web Push via le Braze SDK."
---

# Intégration Push

Une notification push est une alerte qui apparaît à l'écran de l'utilisateur lorsqu'une mise à jour importante se produit. Les notifications push peuvent être reçues même lorsque votre page Web n'est pas actuellement ouverte dans le navigateur de l'utilisateur. Les notifications push sont un moyen précieux de fournir à vos utilisateurs un contenu sensible au temps et pertinent ou de les réengager avec votre site.

![Échantillon Push][1]

Pour plus de ressources, reportez-vous à [Meilleures pratiques][7].

Les notifications push Web sont implémentées en utilisant la [norme Push du W3C][1], que les navigateurs sont en train de supporter. Actuellement, les navigateurs qui prennent en charge les push web incluent la plupart des versions de Chrome, Firefox et Opera. Les Push Web ne sont pas pris en charge à ce jour sur aucun navigateur iOS. On s'attend à ce que, au fur et à mesure que la norme sera plus largement adoptée, plus de navigateurs continueront à implémenter le support. De plus, Safari (sur Mac OS X) possède une solution de push web personnalisée basée sur les services de notification Push d'Apple ; Braze prend également en charge ces notifications Safari.

## Exigence HTTPS

Les standards Web exigent que le domaine requérant l'autorisation de notification push soit sécurisé.

### Qu'est-ce qui définit un site sécurisé ?

Un site est considéré comme sécurisé s'il correspond à l'un des modèles d'origine sécurisée suivants :

- (https, , , *)
- (wss, *, *)
- (, localhost, )
- (, .localhost, *)
- (, 127/8, )
- (, ::1/128, *)
- (fichier, *, —)
- (extension chrome, *, —)

Il s'agit d'une exigence de sécurité dans la spécification des standards ouverts sur laquelle Braze Web Push est construit, et empêche les attaques de l'homme au milieu.

### Que se passe-t-il si un site sécurisé n'est pas disponible?

Alors que les meilleures pratiques de l'industrie sont de sécuriser l'ensemble de votre site, les clients qui ne peuvent pas sécuriser leur domaine de site peuvent contourner les exigences en utilisant un modal sécurisé. En savoir plus dans notre guide pour utiliser \[Domaine Push Alternatif\]\[28\] ou voir une démo fonctionnelle [ici][4].

## Étape 1 : Configurer le service de votre site

- Si vous n'avez pas encore de Service Worker, créez un nouveau fichier nommé `service-worker. s` avec le contenu ci-dessous, et le placer dans le répertoire racine de votre site web.

- Sinon, si votre site enregistre déjà un Service Worker, ajoutez le contenu ci-dessous **au fichier Service Worker**, et définissez l'option d'initialisation [`manageServiceWorkerExternally` à `true`](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize) lors de l'initialisation du Web SDK.

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2FAppboy%2Fappboy-web-sdk%2Fblob%2Fmaster%2Fsample-build%2Fservice-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
Votre serveur web doit retourner un `Content-Type: application/javascript` lors du service de votre fichier Service Worker .
{% endalert %}

### Que se passe-t-il si je ne peux pas enregistrer un travailleur de service dans le répertoire racine ?

Par défaut, un Service Worker ne peut être utilisé que dans le même répertoire dans lequel il est enregistré. Par exemple, si votre fichier Service Worker existe dans `/assets/service-worker. s`, alors il ne serait possible que de l'enregistrer dans `exemple. om/assets/*` ou un sous-répertoire du dossier `assets` , mais pas sur votre page d'accueil (`example.com/`). Pour cette raison, il est recommandé d'héberger et d'enregistrer le Service Worker dans le répertoire racine (c'est-à-dire `https://example.com/service-worker.js`).

Si vous ne pouvez pas enregistrer un Service Worker dans votre domaine racine, une approche alternative est d'utiliser l'en-tête HTTP [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) lorsque vous desserviez votre fichier de Service Worker . En configurant votre serveur pour retourner `Service-Worker-Autorisé : /` dans la réponse pour le Service Worker, cela demandera au navigateur d'élargir le champ d'application et de l'autoriser à être utilisé dans un répertoire différent, comme la page d'accueil, même lorsque le fichier existe dans un répertoire plus profond.


## Étape 2 : Enregistrement du navigateur

In order for a browser to receive push notifications, you must register it for push by calling `appboy.registerAppboyPushMessages()`. Cela demandera immédiatement l'autorisation push de l'utilisateur.

Si vous souhaitez montrer votre propre interface utilisateur à l'utilisateur _avant_ de demander l'autorisation push (connue sous le nom d'invite soft push), vous pouvez tester pour voir si le push est pris en charge dans le navigateur de l'utilisateur avec `appboy. sPushSupported()`. Voir [ci-dessous pour un exemple de soft push prompt](#soft-push-prompts) en utilisant Braze In-App Messages.

Si vous souhaitez vous désabonner d'un utilisateur, vous pouvez le faire en appelant `appboy.unregisterAppboyPushMessages()`.

{% alert important %}
Les versions récentes de Safari et Firefox nécessitent que vous appeliez cette méthode à partir d'un gestionnaire d'événements de courte durée (e. . à partir d'un bouton cliquez sur handler ou sur soft push prompt). Ceci est également compatible avec [l'expérience utilisateur de Chrome des meilleures pratiques](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE) pour l'enregistrement push.
{% endalert %}

## Étape 3 : Configurer la poussée de Safari

Si vous souhaitez prendre en charge les notifications push pour Safari sur Mac OS X, suivez ces instructions supplémentaires :

* [Générer un certificat de poussée de Safari en suivant les instructions "S'enregistrer avec Apple"][3]
* Dans le tableau de bord de Braze, sur la page **Paramètres** (où se trouvent vos clés API), sélectionnez votre application Web. Cliquez sur **Configurer Safari Push** et suivez les instructions, en téléchargeant le certificat push que vous venez de générer.
* Lorsque vous appelez `appboy. nitialize` fournit l'option de configuration optionnelle `safariWebsitePushId` avec l'identifiant Push du site Web que vous avez utilisé lors de la génération de votre certificat Push de Safari. Par exemple `appboy.initialize('VOTRE API-KEY', {safariWebsitePushId: 'web.com.example.domain'})`

## Problèmes courants

__J'ai suivi les instructions d'intégration, mais je ne reçois toujours aucune notification push.__

- Tous les navigateurs ne peuvent pas recevoir de messages push. Veuillez vous assurer que `appboy.isPushSupported()` retourne vrai dans le navigateur.
- Notez que si un utilisateur a refusé un accès push du site, Ils ne seront plus invités à obtenir l'autorisation à moins qu'ils n'enlèvent le statut refusé des préférences de leur navigateur.
- Notez que les notifications de push Web nécessitent que votre site soit https.

## Demandes de poussée souple

C'est souvent une bonne idée pour les sites d'implémenter une invite push "soft" où vous "primez" l'utilisateur et faire valoir vos arguments pour leur envoyer des notifications push avant de demander l'autorisation push. Ceci est utile parce que le navigateur limite la fréquence à laquelle vous pouvez demander directement à l'utilisateur, et si l'utilisateur refuse l'autorisation, vous ne pourrez plus jamais lui demander. Cela peut se faire simplement par le biais des messages In-App [de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#in-app-messaging) déclenchés pour une expérience utilisateur transparente. Au lieu d'appeler `appboy.registerAppboyPushMessages()` directement comme décrit ci-dessus, à la place :

1. Créez une campagne de messagerie "Prime for Push" dans l'application sur le tableau de bord Braze.
  - Faites-en un message **Modal** dans l'application. Donnez-lui le texte et le style que vous souhaitez présenter à l'utilisateur ("Pouvons-nous rester en contact ?")
  - Donnez au message intégré une valeur de texte du bouton 1 « OK » (ou tout texte positif que vous souhaitez), et définissez le comportement au clic sur « Fermer le message ». Vous allez personnaliser ce comportement plus tard.
  - Dans la section composer d'engrenages, ajoutez une paire clé-valeur.  Donnez-lui une clé de `msg-id` et une valeur de `push-primer`.
  - Donnez au message une action de déclenchement de l'événement personnalisé 'prime-for-push' (vous pouvez créer cet événement personnalisé manuellement à partir du tableau de bord) si vous en avez besoin)

2. Dans votre intégration Braze SDK, trouvez et supprimez tous les appels à `appboy.display.automaticallyShowNewInAppMessages()` dans votre snippet.

3. Remplacer l'appel supprimé par le snippet suivant :

```javascript

// Assurez-vous de supprimer les appels à appboy.display.automaticallyShowNewInAppMessages() 
// de votre code comme indiqué dans les étapes ci-dessus

appboy. ubscribeToInAppMessage(function(inAppMessage) {
  var shouldDisplay = true;

  if (inAppMessage instanceof appboy. nAppMessage) {
    // Lit la paire key-value pour msg-id
    var msgId = inAppMessage. xtras["msg-id"];

    // S'il s'agit de notre message "push-primer"
    if (msgId == "push-primer") {
      // Nous ne voulons pas afficher l'invite "push" aux utilisateurs sur les navigateurs qui ne prennent pas en charge push, ou si l'utilisateur
      // a déjà accordé/bloqué la permission
      if (! chiot sPushSupported() || appboy.isPushPermissionGranted() || appboy. sPushBlocked()) {
        shouldDisplay = false;
      }
      if (inAppMessage. uttons[0] ! null) {
        // Invite l'utilisateur lorsque le premier bouton est cliqué
        inAppMessage. uttons[0]. ubscribeToClickedEvent(function() {
          appboy. egisterAppboyPushMessages();
        });
      }
    }
  }

  // Affiche le message
  if (shouldDisplay) {
    appboy. isplay.showInAppMessage(inAppMessage);
  }
});
```

Lorsque vous souhaitez afficher l'invite de push soft à l'utilisateur, appelez `appboy. ogCustomEvent("prime-for-push")` - par exemple, pour demander à l'utilisateur de chaque chargement de page juste après le début de la session de Braze, votre code ressemblerait à :

```
appboy.openSession();
appboy.logCustomEvent("prime-for-push");
```
[28]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain

[1]: {{site.baseurl}}/assets/img_archive/web_push2.png

[1]: http://www.w3.org/TR/push-api/
[3]: https://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html#//apple_ref/doc/uid/TP40013225-CH3-SW33
[4]: http://appboyj.com/modal-test.html
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
