---
nav_title: Rejet de message
article_title: Rejet de messages in-app pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 5
description: "Cet article de référence explique le rejet des messages in-app dans votre application Android ou FireOS."
channel:
  - in-app messages

---

# Rejet de message

> Cet article de référence explique le rejet des messages in-app dans votre application Android ou FireOS.

## Désactiver le rejet par bouton de retour arrière

Par défaut, le bouton de retour arrière du matériel rejette les messages in-app de Braze. Ce comportement peut être désactivé au niveau de chaque message via l'option [`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html). 

Dans l’exemple suivant, `disable_back_button` est une paire clé-valeur personnalisée définie pour le message in-app qui indique si le message doit autoriser le bouton de retour arrière à rejeter le message :

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(new DefaultInAppMessageManagerListener() {
  @Override
  public void beforeInAppMessageViewOpened(View inAppMessageView, IInAppMessage inAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage);
    final Map<String, String> extras = inAppMessage.getExtras();
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false);
    }
  }

  @Override
  public void afterInAppMessageViewClosed(IInAppMessage inAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage);
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true);
  }
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : DefaultInAppMessageManagerListener() {
  override fun beforeInAppMessageViewOpened(inAppMessageView: View, inAppMessage: IInAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage)
    val extras = inAppMessage.extras
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false)
    }
  }

  override fun afterInAppMessageViewClosed(inAppMessage: IInAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage)
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true)
  }
})
```
{% endtab %}
{% endtabs %}

{% alert note %}
Notez que si cette fonctionnalité est désactivée, le comportement par défaut du bouton de retour arrière du matériel de l’activité hôte sera utilisé. Cela peut entraîner la fermeture de l’application par le bouton de retour arrière plutôt celle du message in-app.
{% endalert %}

## Rejet modal par touché extérieur

La valeur par défaut et historique est `false`, ce qui signifie que les clics à l’extérieur du modal ne le ferment pas. Définir cette valeur sur `true` entraînera le rejet du message in-app modal lorsque l’utilisateur touche en dehors du message in-app. Ce comportement peut être activé en appelant :

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

