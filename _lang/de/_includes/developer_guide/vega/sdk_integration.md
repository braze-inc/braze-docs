## Über das Braze Vega SDK

Mit dem Braze Vega SDK können Sie Analytics sammeln und Ihren Nutzer:innen umfangreiche In-App-Nachrichten anzeigen. Die meisten Methoden im Braze Vega SDK sind asynchron und geben Versprechen zurück, die abgewartet oder aufgelöst werden sollten.

## Integration des Braze Vega SDK

### Schritt 1: Installieren Sie die Braze-Bibliothek

Installieren Sie das Braze Vega SDK mit Ihrem bevorzugten Paket Manager:in.

{% tabs local %}
{% tab npm %}
Wenn Ihr Projekt NPM verwendet, können Sie das Braze Vega SDK als Abhängigkeit hinzufügen.

```bash
npm install @braze/vega-sdk --save
```

Nach der Installation können Sie die von Ihnen benötigten Methoden importieren:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}

{% tab yarn %}
Wenn Ihr Projekt Yarn verwendet, können Sie das Braze Vega SDK als Abhängigkeit hinzufügen.

```bash
yarn add @braze/vega-sdk
```

Nach der Installation können Sie die von Ihnen benötigten Methoden importieren:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}
{% endtabs %}

### Schritt 2: Initialisieren Sie das SDK

Nachdem das Braze Vega SDK zu Ihrem Projekt hinzugefügt wurde, initialisieren Sie die Bibliothek mit dem API-Schlüssel und der [SDK-Endpunkt-URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints), die Sie unter **Einstellungen** > **App-Einstellungen** in Ihrem Braze-Dashboard finden.

{% alert important %}
Sie müssen das `changeUser` Versprechen abwarten oder auflösen, bevor Sie andere Braze-Methoden aufrufen, da sonst Ereignisse und Attribute auf den falschen Nutzer:in gesetzt werden können.
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
Anonyme Nutzer:innen können für Ihre [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users) gezählt werden. Vielleicht möchten Sie das SDK deshalb lieber bedingt laden oder initialisieren, um diese Nutzer von der MAU-Zählung auszuschließen.
{% endalert %}

## Optionale Konfigurationen

### Protokollieren

Sie können die SDK-Protokollierung aktivieren, um bei der Fehlersuche und -behebung zu helfen. Es gibt mehrere Möglichkeiten, die Protokollierung zu aktivieren.

#### Enablement der Protokollierung während der Initialisierung

Übergeben Sie `enableLogging: true` an `initialize()`, um Debugging-Nachrichten auf der Konsole zu protokollieren:

```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```

{% alert important %}
Grundlegende Protokolle sind für alle Nutzer:innen sichtbar, daher sollten Sie die Protokollierung deaktivieren, bevor Sie Ihren Code für die Produktion freigeben.
{% endalert %}

#### Enablement der Protokollierung nach der Initialisierung

Verwenden Sie `toggleLogging()`, um die SDK-Protokollierung nach der Initialisierung zu aktivieren oder zu deaktivieren:

```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### Benutzerdefinierte Protokollierung

Verwenden Sie `setLogger()`, um eine angepasste Logger-Funktion bereitzustellen, mit der Sie den Umgang mit SDK-Protokollen besser kontrollieren können:

```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### Optionen zur Konfiguration

Sie können zusätzliche Konfigurationsoptionen an `initialize()` übergeben, um das SDK-Verhalten anzupassen:

```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 30 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## Upgraden des SDK

Wenn Sie das Braze Vega SDK von NPM oder Yarn referenzieren, können Sie auf die neueste Version upgraden, indem Sie Ihre Paketabhängigkeit aktualisieren:

```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## Testen Ihrer Integration

So überprüfen Sie, ob Ihre SDK-Integration korrekt funktioniert:

1. Initialisieren Sie das SDK mit `enableLogging: true`, um Debug-Nachrichten in der Konsole zu sehen
2. Stellen Sie sicher, dass Sie `await changeUser()` vor dem Aufruf anderer SDK-Methoden
3. Rufen Sie `await openSession()` an, um eine Sitzung zu beginnen.
4. Überprüfen Sie auf Ihrem Braze-Dashboard unter **Übersicht**, ob die Daten der Sitzung aufgezeichnet werden.
5. Testen Sie die Protokollierung eines angepassten Events und überprüfen Sie, ob es in Ihrem Dashboard erscheint.


