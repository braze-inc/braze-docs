{% multi_lang_include developer_guide/prerequisites/web.md %}

## Nachrichten triggern

## Auslöser-Typen

In-App-Nachrichten werden automatisch getriggert, wenn das SDK einen der folgenden angepassten Event-Typen protokolliert: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` und `Push Click`. Beachten Sie, dass die Trigger `Specific Purchase` und `Custom Event` auch robuste Filter für Eigenschaften enthalten.

{% alert note %}
In-App-Nachrichten können nicht über die API oder durch API-Ereignisse ausgelöst werden, sondern nur durch angepasste Events, die vom SDK protokolliert werden. Wenn Sie mehr über die Protokollierung erfahren möchten, lesen Sie den Abschnitt [Protokollierung angepasster Events]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Semantik der Zustellung

Alle in Frage kommenden In-App-Nachrichten werden dem Gerät eines Nutzers:innen zu Beginn seiner Sitzung zugestellt. Wenn es zugestellt wird, holt das SDK die Assets im Voraus, so dass sie zum Zeitpunkt des Triggerns verfügbar sind und die Anzeige-Latenzzeit minimiert wird. Wenn das triggernde Ereignis mehr als eine in Frage kommende In-App-Nachricht hat, wird nur die Nachricht mit der höchsten Priorität zugestellt.

Weitere Informationen über die Semantik des SDK für den Sitzungsstart finden Sie unter [Sitzungslebenszyklus]({{site.baseurl}}/developer_guide/platform_integration_guides/analytics/tracking_sessions/).

### Rate-Limits

Standardmäßig können Sie einmal alle 30 Sekunden eine In-App-Nachricht senden.

Um dies zu überschreiben, fügen Sie bitte die folgende Eigenschaft zu Ihrer Braze-Konfiguration hinzu – bevor die Braze-Instanz initialisiert wird. Sie können jede beliebige positive ganze Zahl einstellen, die das minimale Zeitintervall in Sekunden angibt. Zum Beispiel:

```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

## Schlüssel-Wert-Paare

Wenn Sie eine Kampagne in Braze erstellen, können Sie Schlüssel-Wert-Paare festlegen, die das `extras`In-App-Messaging-Objekt verwenden kann, um Daten an Ihre App zu senden. Zum Beispiel:

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```

## Deaktivieren von automatischen Triggern

So verhindern Sie, dass In-App-Nachrichten automatisch ausgelöst werden:

Entfernen Sie den Aufruf von`braze.automaticallyShowInAppMessages()`innerhalb Ihres Ladungs-Snippets und erstellen Sie anschließend eine angepasste Logik, um die Anzeige oder Nichtanzeige von In-App-Nachrichten zu verwalten.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the Braze built-in display capabilities, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Wenn Sie die Website nicht entfernen, rufen Sie `braze.automaticallyShowInAppMessages()`bitte an`braze.showInAppMessage`, da die Nachricht möglicherweise mehrfach angezeigt wird.
{% endalert %}

Der Parameter `inAppMessage` ist eine [`braze.InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)-Unterklasse oder ein [`braze.ControlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.controlmessage.html)-Objekt, von denen jedes über verschiedene Methoden zum Abo von Lebenszyklus-Events verfügt. Die vollständige Dokumentation finden Sie in den [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html).

Es kann jeweils nur eine Nachricht[`Modal`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=modal&sdktab=web)oder[`Full`]({{site.baseurl}}/developer_guide/in_app_messages/?tab=full&sdktab=web)In-App-Nachricht angezeigt werden. Wenn Sie versuchen, eine zweite Nachricht des Typs "modal" oder "full" anzuzeigen, während bereits eine angezeigt wird, gibt `braze.showInAppMessage` den Wert "false" zurück, und die zweite Nachricht wird nicht angezeigt.

## Manuelles Auslösen von Nachrichten

### Anzeige einer Nachricht in Realtime

In-App-Nachrichten können auch innerhalb Ihrer Website erstellt und lokal in Realtime angezeigt werden. Alle auf dem Dashboard verfügbaren Lokalisierungsoptionen sind auch lokal verfügbar. Dies ist besonders nützlich für die Anzeige von Nachrichten, die Sie in Echtzeit in der App auslösen möchten. Analytics zu diesen lokal erstellten Nachrichten sind jedoch im Braze-Dashboard nicht verfügbar.

```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```

## Triggern von Exit-Intent-Nachrichten

Exit-Intent-Nachrichten sind unaufdringliche In-App-Nachrichten, die dazu dienen, Besuchern wichtige Informationen zu übermitteln, bevor sie Ihre Website verlassen.

Um Trigger für diese Nachrichtentypen einzurichten, implementieren Sie bitte eine Exit-Intent-Bibliothek in Ihrer Website (z. B. [die Open-Source-Bibliothek von ouibounce](https://github.com/carlsednaoui/ouibounce)) und verwenden Sie anschließend den folgenden Code, um dies als angepasstes Event in`'exit intent'` Braze zu protokollieren. Jetzt können Ihre zukünftigen In-App-Nachricht-Kampagnen diesen Nachrichtentyp als angepassten Event-Trigger verwenden.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
