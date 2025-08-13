---
nav_title: Ausblenden von Nachrichten
article_title: Beenden von In-App-Nachrichten für Android und FireOS
platform: 
  - Android
  - FireOS
page_order: 5
description: "Dieser Referenzartikel behandelt die Kündigung von In-App-Nachrichten für Ihre Android- oder FireOS-Anwendung."
channel:
  - in-app messages

---

# Entlassung von Nachrichten

> Dieser Referenzartikel behandelt die Kündigung von In-App-Nachrichten für Ihre Android- oder FireOS-Anwendung.

## Deaktivieren von Ausblendungen über die Zurück-Taste

Standardmäßig werden In-App-Nachrichten von Braze mit der Zurück-Taste ausgeblendet. Dieses Verhalten kann für jede einzelne Nachricht deaktiviert werden über [`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html). 

Im folgenden Beispiel ist `disable_back_button` ein angepasstes Schlüssel-Wert-Paar, das in der In-App-Nachricht festgelegt ist und angibt, ob die Nachricht über die Zurück-Taste ausgeblendet werden kann:

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
Hinweis: Wenn diese Funktion deaktiviert ist, wird stattdessen das Standardverhalten der Zurück-Taste der Host-Aktivität verwendet. Dies kann dazu führen, dass durch die Zurück-Taste die Anwendung statt der angezeigten In-App-Nachricht geschlossen wird.
{% endalert %}

## Modal durch Tippen außerhalb des Fensters ausblenden

Der Standardwert und historische Wert ist `false`, d.h. Klicks außerhalb des Modals werden das Modal nicht schließen. Wenn Sie diesen Wert auf `true` setzen, wird die modale In-App-Nachricht ausgeblendet, wenn der Nutzer auf eine Stelle außerhalb der In-App-Nachricht tippt. Dieses Verhalten kann durch folgenden Aufruf umgeschaltet werden:

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

