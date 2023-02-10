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

> C’est souvent une bonne idée pour les sites d’implémenter une invite de notification push « douce » pour laquelle vous avez « préparé » l’utilisateur et présenté vos arguments pour justifier l’envoi des notifications push avant de demander l’autorisation de le faire. C’est utile parce que le navigateur limite la fréquence à laquelle vous pouvez inviter l’utilisateur directement, et si l’utilisateur refuse l’autorisation, vous ne pouvez plus la demander à nouveau. Cet article couvre l’intégration de votre intégration SDK Web pour créer une campagne d’amorce de notification push pour votre application Web.

{% alert tip %}
Ceci peut être effectué sans personnalisation SDK à l’aide de notre nouvelle [fonction de base de notification push « sans code »]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/). 
{% endalert %} 

Sinon, si vous souhaitez inclure une gestion spéciale de la personnalisation au lieu d’appeler `requestPushPermission()` directement, tel que décrit dans la norme[Web push integration (intégration des notifications push)]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration), utilisez les [messages in-app déclenchés]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/) de Braze :

{% multi_lang_include archive/web-v4-rename.md %}

## Étape 1 : Créer une campagne d’amorce de notification push

Tout d’abord, vous devez créer une campagne de messagerie in-app « Préparer pour la notification push » dans le tableau de bord de Braze :

1. Créer un message in-app **Modal** et donnez-lui le texte et le style que vous souhaitez. 
2. Ensuite, définissez le comportement lors du clic sur **Fermer le message**. Ce comportement sera personnalisé plus tard.
3. Ajoutez une paire clé-valeur au message où la clé est `msg-id` et la valeur est `push-primer`.
4. Attribuez une action de déclenchement d’événement personnalisé (c’est-à-dire, « préparer-à-la-notification-push ») au message. Vous pouvez créer l’événement personnalisé manuellement depuis le tableau de bord si nécessaire.

## Étape 2 : Supprimer les appels

Dans votre intégration SDK Braze, trouvez et supprimez tout appel à `automaticallyShowInAppMessages()` à partir de votre extrait de code de chargement.

## Étape 3 : Mettre à jour l’intégration

Enfin, remplacez l’appel supprimé par l’extrait de code suivant :

```javascript
import * as braze from "@braze/web-sdk";
// Assurez-vous de bien supprimer les appels à braze.automaticallyShowInAppMessages()
braze.subscribeToInAppMessage(function(inAppMessage) {
  // Vérifiez que le message n’est pas une variante de contrôle
  if (inAppMessage instanceof braze.inAppMessage) {
    // l’accès aux paires-clé valeur, défini comme `extras`
    const keyValuePairs = inAppMessage.extras || {};
    // vérifiez la valeur de notre clé `msg-id` définie dans le Tableau de bord de Braze
    if (keyValuePairs["msg-id"] === "push-primer") {
      // Nous ne souhaitons pas afficher l’invite de notification push douce sur les navigateurs des utilisateurs
      //qui ne sont pas compatibles avec les notifications push, ou si l’utilisateur a déjà accordé/bloqué son autorisation
      si (
        braze.isPushSupported() === false ||
        braze.isPushPermissionGranted() ||
        braze.isPushBlocked()
      ) {
        // ne pas appeler `showInAppMessage`
        return;
      }

      // l’utilisateur est éligible à la réception de l’invite native
      // inscrire un gestionnaire de clic sur l’un des deux boutons
      if (inAppMessage.buttons[0]) {
        // Invite l’utilisateur lorsque l’on clique sur le premier bouton
        inAppMessage.buttons[0].subscribeToClickedEvent(function() {
          braze.requestPushPermission(
            function() {
              // réussite
            },
            function() {
              // refus de l’utilisateur
            }
          );
        });
      }
    }
  }

  // afficher le message in-app maintenant
  braze.showInAppMessage(inAppMessage);
});
```


Lorsque vous souhaitez afficher l’invite de notification push douce, appelez `braze.logCustomEvent` - tout nom d’événement déclenche ce message in-app.
