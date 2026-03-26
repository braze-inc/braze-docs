## Über das Braze Vega SDK

Mit dem Braze Vega SDK können Sie Analytics-Daten erfassen und Ihren Nutzer:innen umfangreiche In-App-Nachrichten anzeigen. Die meisten Methoden im Braze Vega SDK sind asynchron und geben Promises zurück, die abgewartet oder aufgelöst werden sollten.

## Integration des Braze Vega SDK

### Schritt 1: Installieren Sie die Braze-Bibliothek

Installieren Sie das Braze Vega SDK mit Ihrem bevorzugten Paketmanager.

{% tabs local %}
{% tab npm %}
Falls Ihr Projekt NPM verwendet, können Sie das Braze Vega SDK als Abhängigkeit hinzufügen.

```bash
npm install @braze/vega-sdk --save
```

Nach der Installation können Sie die benötigten Methoden importieren:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}

{% tab yarn %}
Falls Ihr Projekt Yarn verwendet, können Sie das Braze Vega SDK als Abhängigkeit hinzufügen.

```bash
yarn add @braze/vega-sdk
```

Nach der Installation können Sie die benötigten Methoden importieren:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}
{% endtabs %}

### Schritt 2: Initialisieren Sie das SDK

Nachdem Sie das Braze Vega SDK zu Ihrem Projekt hinzugefügt haben, initialisieren Sie die Bibliothek mit dem SDK-API-Schlüssel und [der SDK-Endpunkt-URL,]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) die Sie in Ihrem Braze-Dashboard unter **„Einstellungen“** > **„App-Einstellungen“** finden.

{% alert important %}
Sie müssen das`changeUser`Versprechen abwarten oder auflösen, bevor Sie andere Braze-Methoden aufrufen, da sonst Ereignisse und Attribute möglicherweise für die falsche Nutzer:in festgelegt werden.
{% endalert %}

```javascript
import { useEffect } from "react-native";
import {
  initialize,
  changeUser,
  logCustomEvent,
  openSession,
  setCustomUserAttribute,
  setUserCountry
} from "@braze/vega-sdk";

const App = () => {
  useEffect(() => {
    const initBraze = async () => {
      // Initialize the SDK
      await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
        sessionTimeoutInSeconds: 60,
        appVersionNumber: "1.2.3.4",
        enableLogging: true, // set to `true` for debugging
      });

      // Change user
      await changeUser("user-id-123");
      
      // Start a session
      await openSession();
      
      // Log custom events and set user attributes
      logCustomEvent("visited-page", { pageName: "home" });
      setCustomUserAttribute("my-attribute", "my-attribute-value");
      setUserCountry("USA");
    };
    
    initBraze();
  }, []);
  
  return (
    // Your app components
  );
};
```

{% alert important %}
Anonyme Nutzer:innen können zu Ihrer [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users) hinzugerechnet werden. Vielleicht möchten Sie das SDK deshalb lieber bedingt laden oder initialisieren, um diese Nutzer von der MAU-Zählung auszuschließen.
{% endalert %}

## Optionale Konfigurationen

### Protokollieren

Sie können die SDK-Protokollierung aktivieren, um die Fehlersuche und Fehlerbehebung zu unterstützen. Es gibt mehrere Möglichkeiten für Enablement der Protokollierung.

#### Protokollierung während der Initialisierung aktivieren

Bitte übergeben Sie`enableLogging: true`an, `initialize()`um Debugging-Nachrichten in der Konsole zu protokollieren:

```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```

{% alert important %}
Grundlegende Protokolle sind für alle Nutzer:innen sichtbar. Bitte erwägen Sie daher, die Protokollierung zu deaktivieren, bevor Sie Ihren Code für die Produktion freigeben.
{% endalert %}

#### Protokollierung nach Initialisierung aktivieren

Verwenden Sie die Option`toggleLogging()` für Enablement, um die SDK-Protokollierung nach der Initialisierung zu aktivieren oder zu deaktivieren:

```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### Benutzerdefinierte Protokollierung

Verwenden Sie diese`setLogger()` Option, um eine angepasste Logger-Funktion bereitzustellen und so mehr Kontrolle über die Verarbeitung von SDK-Protokollen zu erhalten:

```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### Konfigurationsoptionen

Sie können zusätzliche Konfigurationsoptionen an `initialize()`übergeben, um das Verhalten des SDK anzupassen:

```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 30 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## Upgraden des SDK

Wenn Sie das Braze Vega SDK von NPM oder Yarn referenzieren, können Sie auf die neueste Version upgraden, indem Sie ein Update für Ihre Paketabhängigkeit durchführen:

```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## Testen Sie Ihre Integration

Um zu überprüfen, ob Ihre SDK-Integration ordnungsgemäß funktioniert:

1. Initialisieren Sie das SDK mit, `enableLogging: true`um Debug-Nachrichten in der Konsole anzuzeigen.
2. Bitte stellen Sie sicher, dass Sie`await changeUser()`  bevor Sie andere SDK-Methoden aufrufen.
3. Bitte rufen Sie `await openSession()`an, um eine Sitzung zu beginnen.
4. Bitte überprüfen Sie in Ihrem Braze-Dashboard unter **„Übersicht“**, ob die Sitzungsdaten erfasst werden.
5. Bitte testen Sie die Protokollierung eines angepassten Events und überprüfen Sie, ob es in Ihrem Dashboard angezeigt wird.


