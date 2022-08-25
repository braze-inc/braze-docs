---
nav_title: Demande de notification push douce
article_title: Demande de notification push douce pour Web
platform: Web
page_order: 19
page_type: reference
description: "Cet article explique comment créer une demande de notification push douce pour votre application Web"
channel: notification push

---

# Invite de notification push douce

{% alert tip %}
Braze prend désormais en charge des messages in-app d’enregistrement de notifications push prêts à l’emploi sans codage requis ! Pour en savoir plus, consultez notre [Guide d’amorce de notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/).
{% endalert %}

C’est souvent une bonne idée pour les sites d’implémenter une invite de notification push « douce » pour laquelle vous avez « préparé » l’utilisateur et présenté vos arguments pour justifier l’envoi des notifications push avant de demander l’autorisation de le faire. C’est utile parce que le navigateur limite la fréquence à laquelle vous pouvez inviter l’utilisateur directement, et si l’utilisateur refuse l’autorisation, vous ne pouvez plus la demander à nouveau. 

Cela peut être fait simplement par le biais des [messages in-app déclenchés]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#trigger-types) de Braze pour une expérience utilisateur transparente. Plutôt que d’appeler directement `requestPushPermission()` comme décrit dans l’[intégration de notification push pour le Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration) habituelle.

{% include archive/web-v4-rename.md %}

## Étape 1 : Créer une campagne d’amorce de notification push

Tout d’abord, vous devez créer une campagne de messagerie in-app « Préparer pour la notification push » dans le tableau de bord de Braze :

1. Créer un message in-app **Modal** et donnez-lui le texte et le style que vous souhaitez. 
2. Ensuite, définissez le comportement lors du clic sur **Fermer le message**. Ce comportement sera personnalisé plus tard.
3. Ajoutez une paire clé-valeur au message où la clé est `msg-id` et la valeur est `push-primer`.
4. Affectez une action de déclenchement d’événement personnalisé « préparer-à-la-notification-push » au message. Vous pouvez créer l’événement personnalisé manuellement depuis le tableau de bord si nécessaire.

## Étape 2 : Supprimer les appels

Dans votre intégration SDK Braze, trouvez et supprimez tout appel à `automaticallyShowInAppMessages()` à partir de votre extrait de code de chargement.

## Étape 3 : Mettre à jour l’intégration

Enfin, remplacez l’appel supprimé par l’extrait de code suivant :

```javascript

// Be sure to remove calls to automaticallyShowInAppMessages() 
// from your code as noted in the steps above

braze.subscribeToInAppMessage(function(inAppMessage) {
  if (inAppMessage instanceof braze.InAppMessage) {
    // checks the key-value pair for a "msg-id" key
    const keyValuePairs = inAppMessage.extras || {};

    // If this is our push primer message
    if (keyValuePairs["msg-id"] === "push-primer") {
      if (!braze.isPushSupported() || braze.isPushPermissionGranted() || braze.isPushBlocked()) {
        // do not show the message because user/browser is not eligible
        return;
      }

      // the browser is eligible to request push permission
      // register a callback when the left-button is clicked
      if (inAppMessage.buttons[0] != null) {
        // Prompt the user when the first button is clicked
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          braze.requestPushPermission(function(){
            // success!
          }, function(){
            // user declined
          });
        });
      }

      // show the in-app message now
      braze.showInAppMessage(inAppMessage);
    }
  }
});
```

Lorsque vous souhaitez afficher l’invite de notification push douce à l’utilisateur, appelez `braze.logCustomEvent("prime-for-push")`. Par exemple, pour inviter l’utilisateur lors de chaque chargement de page juste après le début de la session Braze :

```
braze.openSession();
braze.logCustomEvent("prime-for-push");
```
