{% multi_lang_include developer_guide/prerequisites/web.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web).

## À propos des invites à pression douce

C’est souvent une bonne idée pour les sites d’implémenter une invite de notification push « douce » pour laquelle vous avez « préparé » l’utilisateur et présenté vos arguments pour justifier l’envoi des notifications push avant de demander l’autorisation de le faire. C’est utile parce que le navigateur limite la fréquence à laquelle vous pouvez inviter l’utilisateur directement, et si l’utilisateur refuse l’autorisation, vous ne pouvez plus la demander à nouveau.

Par ailleurs, si vous souhaitez inclure un traitement personnalisé spécial, au lieu d'appeler directement `requestPushPermission()` comme décrit dans l'[intégration Web push]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration) standard, utilisez nos [messages in-app déclenchés]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web).

{% alert tip %}
Ceci peut être fait sans personnalisation du SDK en utilisant notre nouvelle [fonctionnalité d’amorçage de notifications push sans code]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
{% endalert %}

## Configuration des invites à pression douce

{% multi_lang_include archive/web-v4-rename.md %}

### Étape 1 : Créer une campagne d’amorce de notification push

Tout d’abord, vous devez créer une campagne de messagerie in-app « Préparer pour la notification push » dans le tableau de bord de Braze :

1. Créez un message in-app **modal** avec le texte et le style que vous souhaitez. 
2. Ensuite, définissez le comportement au clic sur **Fermer le message.** Ce comportement sera personnalisé plus tard.
3. Ajoutez une paire clé-valeur au message où la clé est `msg-id` et la valeur est `push-primer`.
4. Attribuez au message une action de déclenchement d'événement personnalisé (telle que « amorçage de notification push »). Vous pouvez créer l’événement personnalisé manuellement depuis le tableau de bord si nécessaire.

### Étape 2 : Supprimer les appels

Dans votre intégration SDK Braze, trouvez et supprimez tout appel à `automaticallyShowInAppMessages()` à partir de votre extrait de code de chargement.

### Étape 3 : Mettre à jour l’intégration

Enfin, remplacez l’appel supprimé par l’extrait de code suivant :

```javascript
import * as braze from "@braze/web-sdk";
// Be sure to remove any calls to braze.automaticallyShowInAppMessages()
braze.subscribeToInAppMessage(function(inAppMessage) {
  // check if message is not a control variant
  if (inAppMessage instanceof braze.inAppMessage) {
    // access the key-value pairs, defined as `extras`
    const keyValuePairs = inAppMessage.extras || {};
    // check the value of our key `msg-id` defined in the Braze dashboard
    if (keyValuePairs["msg-id"] === "push-primer") {
      // We don't want to display the soft push prompt to users on browsers
      // that don't support push, or if the user has already granted/blocked permission
      if (
        braze.isPushSupported() === false ||
        braze.isPushPermissionGranted() ||
        braze.isPushBlocked()
      ) {
        // do not call `showInAppMessage`
        return;
      }

      // user is eligible to receive the native prompt
      // register a click handler on one of the two buttons
      if (inAppMessage.buttons[0]) {
        // Prompt the user when the first button is clicked
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          braze.requestPushPermission(
            function() {
              // success!
            },
            function() {
              // user declined
            }
          );
        });
      }
    }
  }

  // show the in-app message now
  braze.showInAppMessage(inAppMessage);
});
```

Lorsque vous souhaitez afficher l’invite de notification push douce, appelez `braze.logCustomEvent` - tout nom d’événement déclenche ce message in-app.
