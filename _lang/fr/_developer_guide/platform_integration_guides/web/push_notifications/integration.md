---
nav_title: Intégration
article_title: Intégration de notifications push pour le Web
platform: Web
channel: notification push
page_order: 0
page_type: reference
description: "Cet article décrit comment intégrer les notifications push Braze pour le Web via le SDK Braze."

local_redirect: #soft-push-prompts
  soft-push-prompts: '/docs/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/'

---

# Intégration de notifications push

Une notification push est une alerte qui apparaît sur l’écran de l’utilisateur lorsqu’une mise à jour importante se produit. Vous pouvez recevoir des notifications push même lorsque votre page Web n’est pas actuellement ouverte dans le navigateur de l’utilisateur. Les notifications push constituent un moyen précieux de fournir à vos utilisateurs un contenu urgent et pertinent, ou de les ré-engager avec votre site.

![][27]

Consultez nos [meilleures pratiques concernant les notifications push][7] pour plus de ressources.

Les notifications push Web sont implémentées à l’aide des [normes de notification push W3C][1], pour lesquelles les navigateurs développent leur support. Actuellement, les navigateurs qui prennent en charge les notifications push Web comprennent la plupart des versions de Chrome, Firefox et Opera. La notification push pour le Web n’est pas prise en charge à ce jour sur les navigateurs iOS. Il est prévu qu’avec l’adoption plus large de la norme, plus de navigateurs continueront à implémenter un support. De plus, la version Safari pour ordinateur de bureau (sur macOS X) dispose d’une solution de notification push Web personnalisée basée sur les services de notification push Apple. Braze prend en charge ces notifications Safari.

{% multi_lang_include archive/web-v4-rename.md %}

## Intégration

### Étape 1 : Configurer le service de traitement de votre site

- Si vous n’avez pas déjà un service de traitement, créez un nouveau fichier nommé `service-worker.js` avec l’extrait de code suivant et placez-le dans le répertoire racine de votre site Internet.
- Sinon, si votre site enregistre déjà un service de traitement, ajoutez l’extrait de code suivant au fichier du service de traitement et définissez l’option d’initialisation [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) sur `true` lors de l’initialisation du SDK Web.

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

Si le nom du fichier de votre service de traitement n’est pas `service-worker.js`, vous devez utiliser l’`serviceWorkerLocation`option d’initialisation [ ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions).

{% alert important %}
Votre serveur Web doit renvoyer un `Content-Type: application/javascript` lorsqu’il notifie votre fichier de service de traitement. 
{% endalert %}

#### Que se passe-t-il si je ne peux pas enregistrer un service de traitement dans le répertoire racine ?

Par défaut, un service de traitement ne peut être utilisé que dans le même répertoire que celui dans lequel il est enregistré. Par exemple, si votre fichier de service de traitement existe dans `/assets/service-worker.js`, vous ne pouvez l’enregistrer que dans `example.com/assets/*` ou un sous-répertoire du dossier `assets` mais pas sur votre page d’accueil (`example.com/`). Pour cette raison, il est recommandé d’héberger et d’enregistrer le service de traitement dans le répertoire racine (c.-à-d., `https://example.com/service-worker.js`).

Si vous ne pouvez pas enregistrer un service de traitement dans votre domaine racine, une autre approche consiste à utiliser l’en-tête HTTP [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) lorsque vous notifiez votre fichier de service de traitement. En configurant votre serveur pour renvoyer `Service-Worker-Allowed: /` en réponse au service de traitement, le navigateur recevra l’instruction d’élargir la portée et d’autoriser l’utilisation dans un répertoire différent.

### Étape 2 : Enregistrer le navigateur

Pour qu’un navigateur reçoive des notifications push, vous devez l’enregistrer pour que vous puissiez réaliser une notification push en appelant `braze.requestPushPermission()`. Cela demandera immédiatement l’autorisation de notification push à l’utilisateur. 

Si vous souhaitez afficher votre propre IU liée à la notification push avant de demander une autorisation (appelée demande de notification push douce), vous pouvez tester pour voir si la notification push est prise en charge dans le navigateur de l’utilisateur avec `braze.isPushSupported()`. Reportez-vous à l’[exemple de demande de notification push douce]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/) utilisant des messages in-app.

Si vous souhaitez désinscrire un utilisateur, vous pouvez le faire en appelant `braze.unregisterPush()`.

{% alert important %}
Les versions récentes de Safari et de Firefox exigent que vous appeliez cette méthode depuis un gestionnaire d’événements à courte durée d’action (par exemple, à partir d’un gestionnaire de bouton d’action ou d’une demande de notification push douce). Ceci est cohérent avec [les meilleures pratiques de Chrome en matière d’expérience utilisateur](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE) pour l’enregistrement de notifications push.
{% endalert %}

### Étape 3 : Configurer la notification push Safari

Si vous souhaitez prendre en charge les notifications push pour Safari sur macOS X, suivez les instructions supplémentaires suivantes :

- Générez un certificat de notification push Safari en suivant les instructions [S’enregistrer auprès d’Apple][3].
- Dans le tableau de bord de Braze, sur la page **Settings (Paramètres)** (où se trouvent vos clés API), sélectionnez votre application Web. Cliquez sur **Configure Safari Push (Configurer la notification push Safari)** et suivez les instructions en téléchargeant le certificat de notification push que vous venez de générer.
- Lorsque vous appelez `braze.initialize`, fournissez l’option de configuration facultative `safariWebsitePushId` avec l’ID de notification push du site Internet que vous avez utilisé lors de la génération de votre certificat de notification push Safari. Par exemple, `braze.initialize('YOUR-API-KEY', {safariWebsitePushId: 'web.com.example.domain'})`

## Invite de notification push douce

C’est souvent une bonne idée pour les sites d’implémenter une invite de notification push « douce » pour laquelle vous avez « préparé » l’utilisateur et présenté vos arguments pour justifier l’envoi des notifications push avant de demander l’autorisation de le faire. C’est utile parce que le navigateur limite la fréquence à laquelle vous pouvez inviter l’utilisateur directement, et si l’utilisateur refuse l’autorisation, vous ne pouvez plus la demander à nouveau. Cela peut être fait simplement par le biais des [messages in-app déclenchés]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/) de Braze pour une expérience utilisateur transparente. Plutôt que d’appeler `braze.requestPushPermission()` directement comme décrit ci-dessus, à la place :

1. Créez une campagne de messagerie in-app « Préparer pour la notification push » dans le tableau de bord de Braze.
  - Faites-en un message in-app **Modal**. Donnez-lui le texte et le style que vous souhaitez présenter à l’utilisateur (« Pouvons-nous rester en contact ? »).
  - Donnez au message in-app une valeur de texte de bouton 1 « OK » (ou tout texte positif que vous souhaitez) et définissez le comportement de clic sur « Fermer le message ». Vous personnaliserez ce comportement plus tard.
  - Dans la section de composition d’engrenage, ajoutez une paire clé-valeur. Donnez-lui une clé de `msg-id` et une valeur de `push-primer`.
  - Donnez au message une action de déclenchement de l’événement personnalisé « préparer-pour-la-notification-push » (vous pouvez créer cet événement personnalisé manuellement depuis le tableau de bord si nécessaire).<br>
<br>

2. Dans votre intégration SDK Braze, trouvez et supprimez tout appel à `braze.automaticallyShowInAppMessages()` à partir de votre extrait de code de chargement.<br>
<br>

3. Remplacez l’appel supprimé par l’extrait de code suivant :

```javascript

// Be sure to remove calls to braze.automaticallyShowInAppMessages() 
// from your code as noted in the steps above

braze.subscribeToInAppMessage(function(inAppMessage) {
  var shouldDisplay = true;

  if (inAppMessage instanceof braze.InAppMessage) {
    // Read the key-value pair for msg-id
    var msgId = inAppMessage.extras["msg-id"];

    // If this is our push primer message
    if (msgId == "push-primer") {
      // We don't want to display the soft push prompt to users on browsers that don't support push, or if the user
      // has already granted/blocked permission
      if (!braze.isPushSupported() || braze.isPushPermissionGranted() || braze.isPushBlocked()) {
        shouldDisplay = false;
      }
      if (inAppMessage.buttons[0] != null) {
        // Prompt the user when the first button is clicked
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          braze.requestPushPermission();
        });
      }
    }
  }

  // Display the message
  if (shouldDisplay) {
    braze.showInAppMessage(inAppMessage);
  }
});
```

Lorsque vous souhaitez afficher l’invite de notification push douce à l’utilisateur, appelez `braze.logCustomEvent("prime-for-push")`. Par exemple, pour inviter l’utilisateur lors de chaque chargement de page juste après le début de la session Braze, votre code devrait ressembler à :

```javascript
braze.openSession();
braze.logCustomEvent("prime-for-push");
```

## Exigence HTTPS

Les normes Web exigent que le domaine demandant l’autorisation de notification push soit sécurisé.

### Qu’est-ce qui définit un site sécurisé ?

Un site est considéré comme sécurisé s’il correspond à l’un des modèles d’origine sécurisée suivants :

- (https, , *)
- (wss, *, *)
- (, localhost, )
- (, .localhost, *)
- (, 127/8, )
- (, ::1/128, *)
- (fichier, *, —)
- (extension chrome, *, —)

Cette exigence de sécurité dans la spécification des normes ouvertes sur laquelle la notification push Braze pour le Web est construite empêche les attaques de l'homme du milieu.

### Que se passe-t-il si un site sécurisé n’est pas disponible ?

Bien que les meilleures pratiques du secteur soient de rendre votre site sûr, les clients qui ne peuvent pas sécuriser leur domaine de site peuvent contourner l’exigence en utilisant un modal sécurisé. Vous pouvez en apprendre plus dans notre guide d’utilisation [Notification push sur un domaine alternatif][28] ou consulter une [démonstration de travail][4].

## Paramètres avancés du service de traitement

Le fichier du service de traitement de Braze appellera automatiquement `skipWaiting` lors de l’installation. Si vous souhaitez l’éviter, ajoutez le code suivant à votre fichier de service de traitement, avant l’importation de Braze :

```javascript
self.addEventListener('install', (event) => {
  event.stopImmediatePropagation();
}); 
self.importScripts('https://js.appboycdn.com/web-sdk/4.0/service-worker.js');
```

## Résolution des problèmes

**J’ai suivi les instructions d’intégration, mais je ne reçois toujours aucune notification push.**
- Les notifications push Web exigent que votre site soit en HTTPS.
- Tous les navigateurs ne peuvent pas recevoir de messages de notification push. Assurez-vous que `braze.isPushSupported()` retourne `true` dans le navigateur.
- Si un utilisateur a refusé au site l’accès aux notifications push, il ne recevra plus de demande d’autorisation à moins qu’il ne supprime l’état refusé de ses préférences de navigateur.

[1]: http://www.w3.org/TR/push-api/
[3]: https://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html#//apple_ref/doc/uid/TP40013225-CH3-SW33
[4]: http://appboyj.com/modal-test.html
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[27]: {{site.baseurl}}/assets/img_archive/web_push2.png
[28]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain
