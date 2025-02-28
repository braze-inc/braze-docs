---
nav_title: Zustellung von In-App-Nachrichten
article_title: In-App-Zustellung von Nachrichten für das Internet
platform: Web
channel: in-app messages
page_order: 4
page_type: reference
description: "Dieser Artikel beschreibt die Zustellung von In-App-Nachrichten über das Braze SDK, z. B. die manuelle Anzeige von In-App-Nachrichten oder das Senden von lokalen In-App-Nachrichten und Exit-Intent-Nachrichten."

---

# Zustellung von In-App-Nachrichten

> Dieser Artikel beschreibt die Zustellung von In-App-Nachrichten über das Braze SDK, z. B. die manuelle Anzeige von In-App-Nachrichten oder das Senden von lokalen In-App-Nachrichten und Exit-Intent-Nachrichten.

## Auslöser-Typen

Unser Produkt In-App-Nachricht erlaubt es Ihnen, die Anzeige einer In-App-Nachricht als Folge verschiedener Ereignistypen zu triggern: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, und `Push Click`. Außerdem enthalten die Trigger `Specific Purchase` und `Custom Event` robuste Eigenschaftsfilter.

{% alert note %}
Ausgelöste In-App-Nachrichten funktionieren nur bei angepassten Events, die über das Braze SDK protokolliert werden. In-App-Nachrichten können nicht über die API oder durch API-Event (wie Kauf-Events) getriggert werden. Wenn Sie mit einer Web App arbeiten, lesen Sie, wie Sie [angepasste Events protokollieren]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/#tracking-custom-events).
{% endalert %}

## Semantik der Zustellung

Alle In-App-Nachrichten, für die ein Nutzer:innen berechtigt ist, werden automatisch auf das Gerät oder den Browser des Nutzers heruntergeladen, sobald die Sitzung beginnt, und gemäß den Regeln für die Zustellung der Nachrichten getriggert. In unserer [Dokumentation zum Sitzungslebenszyklus]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#session-lifecycle) finden Sie weitere Informationen zur Semantik des Sitzungsstarts im SDK.

## Mindestzeitintervall zwischen Auslösern

Standardmäßig begrenzen wir die Rate für In-App-Nachrichten auf einmal alle 30 Sekunden, um ein hochwertiges Nutzererlebnis zu gewährleisten. Um diesen Wert außer Kraft zu setzen, können Sie die Konfigurationsoption `minimumIntervalBetweenTriggerActionsInSeconds` an Ihre [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)-Funktion übergeben:

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## Manuelle Anzeige von In-App-Nachrichten

Wenn Sie nicht möchten, dass Ihre Website neue In-App-Nachrichten sofort anzeigt, wenn sie getriggert werden, können Sie die automatische Anzeige deaktivieren und Ihre eigenen Abonnenten für die Anzeige registrieren. 

Finden Sie zunächst den Aufruf von `braze.automaticallyShowInAppMessages()` in Ihrem ladenden Snippet und entfernen Sie ihn. Dann erstellen Sie Ihre eigene Logik zur angepassten Handhabung einer getriggerten In-App-Nachricht, bei der Sie die Nachricht anzeigen oder nicht anzeigen. 

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use Braze's built-in display capabilities, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Wenn Sie `braze.automaticallyShowInAppMessages()` nicht von Ihrer Website entfernen, wenn Sie auch `braze.showInAppMessage` aufrufen, wird die Nachricht möglicherweise doppelt angezeigt.
{% endalert %}

Der Parameter `inAppMessage` ist eine [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)-Unterklasse oder ein [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html)-Objekt, von denen jedes über verschiedene Methoden zum Abo von Lebenszyklus-Events verfügt. In den [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) finden Sie eine vollständige Dokumentation.

Nur eine [`Modal`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#modal-in-app-messages) oder [`Full`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#full-in-app-messages) In-App-Nachricht kann zu einem bestimmten Zeitpunkt angezeigt werden. Wenn Sie versuchen, eine zweite Nachricht des Typs "modal" oder "full" anzuzeigen, während bereits eine angezeigt wird, gibt `braze.showInAppMessage` den Wert "false" zurück, und die zweite Nachricht wird nicht angezeigt.

## Lokale In-App-Nachrichten

In-App-Nachrichten können auch innerhalb Ihrer Website erstellt und lokal in Realtime angezeigt werden. Alle auf dem Dashboard verfügbaren Lokalisierungsoptionen sind auch lokal verfügbar. Dies ist besonders nützlich für die Anzeige von Nachrichten, die Sie in Echtzeit in der App auslösen möchten. Die Analytics für diese lokal erstellten Nachrichten werden jedoch nicht im Braze-Dashboard verfügbar sein.

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## Nachrichten mit Exit-Absicht

In-App-Nachrichten mit der Absicht, die App zu verlassen, erscheinen, wenn Besucher im Begriff sind, Ihre Website zu verlassen. Sie bieten eine weitere Opportunity, um Nutzern:innen wichtige Informationen mitzuteilen, ohne sie beim Besuch Ihrer Website zu unterbrechen. 

Um diese Nachrichten zu versenden, fügen Sie Ihrer Website zunächst eine Bibliothek mit Ausstiegsabsichten hinzu, z. B. diese [Open-Source-Bibliothek](https://github.com/carlsednaoui/ouibounce). Verwenden Sie dann den folgenden Code-Snippet, um die Exit-Absicht als angepasstes Event zu protokollieren. In-App-Nachricht-Kampagnen können dann im Dashboard erstellt werden, indem Sie die Absicht, die App zu verlassen, als angepasstes Event triggern.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```


