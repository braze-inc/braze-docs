---
nav_title: Soft Push Prompt
article_title: Soft Push Aufforderung für das Internet
platform: Web
page_order: 19
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie eine Soft-Push-Eingabeaufforderung für Ihre Web-Anwendung erstellen."
channel: push

---

# Soft Push Prompt

> Es ist oft eine gute Idee, eine "sanfte" Push-Aufforderung zu implementieren, mit der Sie den Nutzer:innen vor der Anfrage nach einer Push-Benachrichtigung "vorwarnen" ("prime") und sie für die Zusendung von Push-Benachrichtigungen gewinnen. Dies ist nützlich, da der Browser die Anzahl der direkten Anfragen an die Nutzer:innen drosselt, und wenn ein:e Nutzer:in die Erlaubnis verweigert, können Sie sie/ihn nie wieder fragen. Dieser Artikel behandelt die Modifizierung der Web SDK-Integration, um eine Push-Primer-Kampagne für Ihre Webanwendung zu erstellen.

{% alert tip %}
Dies kann ohne SDK-Anpassung mit unserem neuen [No Code Push Primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/) geschehen.
{% endalert %} 

Wenn Sie eine spezielle, angepasste Handhabung einbauen möchten, können Sie auch unsere [getriggerten In-App-Nachrichten]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/) verwenden, anstatt `requestPushPermission()` direkt aufzurufen, wie in der Standard [Web-Push Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-2-browser-registration) beschrieben:

{% multi_lang_include archive/web-v4-rename.md %}

## Schritt 1: Push-Primer-Kampagne erstellen

Zunächst müssen Sie im Braze-Dashboard eine In-App Messaging-"Prime for Push"-Kampagne erstellen:

1. Erstellen Sie eine **Modal** In-App-Nachricht mit dem von Ihnen gewünschten Text und Styling. 
2. Als nächstes stellen Sie das Verhalten bei Klick auf **Nachricht schließen** ein. Dieses Verhalten wird später angepasst.
3. Fügen Sie der Nachricht ein Schlüssel-Wert-Paar hinzu, wobei der Schlüssel `msg-id` und der Wert `push-primer` lautet.
4. Weisen Sie der Nachricht eine angepasste Event-triggernde Aktion zu (z. B. "prime-for-push"). Sie können das angepasste Event bei Bedarf manuell über das Dashboard erstellen.

## Schritt 2: Anrufe entfernen

Suchen Sie in Ihrer Braze SDK-Integration nach Aufrufen von `automaticallyShowInAppMessages()` und entfernen Sie diese aus Ihrem ladenden Snippet.

## Schritt 3: Update-Integration

Schließlich ersetzen Sie den entfernten Aufruf durch das folgende Snippet:

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


Wenn Sie dem Nutzer die Soft-Push-Aufforderung anzeigen möchten, rufen Sie `braze.logCustomEvent` auf – mit dem Namen des Ereignisses, das diese In-App-Nachricht triggert.