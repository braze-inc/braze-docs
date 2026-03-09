### Voraussetzungen

Bevor Sie diese Integration verwenden können, müssen Sie [ein Konto und einen Container für Google Tag Manager erstellen](https://support.google.com/tagmanager/answer/14842164).

### Schritt 1: Öffnen Sie die Tag-Template-Galerie.

Wählen Sie im [Google Tag Manager](https://tagmanager.google.com/) Ihren Workspace aus und wählen Sie anschließend **„Templates“** aus. Wählen Sie im Bereich **„Tag-Template“** **die Option „Galerie durchsuchen“** aus.

![Die Template-Seite für einen Beispiel-Workspace in Google Tag Manager.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### Schritt 2: Fügen Sie das Initialisierungs-Tag-Template hinzu.

Bitte suchen Sie in der Template-Galerie nach **„Braze Initialization Tag**“ und`braze-inc` wählen Sie diese Option aus.

![Die Vorlagengalerie, die die verschiedenen „braze-inc”-Templates präsentiert.]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

Auswählen **„Zum Workspace hinzufügen“** > **„Hinzufügen**“.

![Die Seite „Braze-Initialisierungstag“ im Google Tag Manager.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### Schritt 3: Das Tag konfigurieren

Wählen Sie im Abschnitt **„Vorlagen“** das neu hinzugefügte Template aus.

![Die Seite „Vorlagen“ im Google Tag Manager, auf der das Template „Braze Initialization Tag“ angezeigt wird.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

Bitte wählen Sie das Bleistift-Symbol, um das Dropdown-Menü **„Tag-Konfiguration“** zu öffnen.

![Die Kachel „Tag-Konfiguration“ mit dem „Bleistift“-Symbol wird angezeigt.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

Bitte geben Sie die erforderlichen Mindestinformationen ein:

| Feld         | Beschreibung |
| ------------- | ----------- |
| **API-Schlüssel**   | Ihr [Braze-API-Schlüssel]({{site.baseurl}}/api/basics/#about-rest-api-keys), den Sie im Braze-Dashboard unter **„Einstellungen“** > **„App-Einstellungen“** finden. |
| **API-Endpunkt** | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der Braze-URL für [Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
| **SDK Version**  | Die aktuellste`MAJOR.MINOR`Version des Web Braze SDK, die im [Changelog]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web) aufgeführt ist. Wenn die neueste Version beispielsweise `4.1.2` ist, geben Sie `4.1` ein. Weitere Informationen finden Sie unter [„Über die SDK-Versionsverwaltung]({{site.baseurl}}/developer_guide/sdk_integration/version_management/)“. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Für zusätzliche Initialisierungseinstellungen wählen Sie bitte **„Braze-Initialisierungsoptionen**“ und wählen Sie die gewünschten Optionen aus.

![Die Liste der Braze-Initialisierungsoptionen finden Sie unter „Tag-Konfiguration”.]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### Schritt 4: Wählen Sie Initialisierungsoptionen

Das Braze-Initialisierungstag bietet die folgenden Optionen. Die meisten davon lassen sich direkt dem [Internet SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) zuordnen[`InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions), und einige entsprechen Internet SDK-Methoden, die das Tag während der Initialisierung aufruft. Bitte wählen Sie die Optionen aus, die Ihren Anforderungen an die Integration entsprechen:

| GTM-Option | Internet-SDK-Konfiguration oder -Methode | Beschreibung |
| --- | --- | --- |
| **HTML-In-App-Nachrichten zulassen** | `allowUserSuppliedJavascript` | Aktiviert HTML-In-App-Nachrichten, Banner und von den Nutzern:innen bereitgestellte JavaScript-Klickaktionen. Erforderlich für [HTML-In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/) und [Banner,]({{site.baseurl}}/developer_guide/banners/placements/?sdktab=web) die angepasstes HTML verwenden. Bitte aktivieren Sie diese Option nur, wenn Sie dem HTML- und JavaScript-Inhalt vertrauen, da dadurch die Ausführung von benutzerdefiniertem JavaScript zulässig ist. |
| **App-Versionsnummer** | `appVersion`, `appVersionNumber` | App-Version für die Segmentierung (zum Beispiel`1.2.3.4`). |
| **Neue Sitzung automatisch öffnen** | `braze.openSession()` | Öffnet eine neue Sitzung, nachdem das SDK durch Aufruf dieser Methode initialisiert wurde. |
| **Neue In-App-Nachrichten automatisch anzeigen** | `braze.automaticallyShowInAppMessages()` | Zeigt automatisch neue In-App-Nachrichten an, wenn diese vom Server eintreffen, indem diese Methode nach der Initialisierung aufgerufen wird. |
| **Automatische Wartung des Push-Tokens deaktivieren** | `disablePushTokenMaintenance` | Verhindert, dass das SDK Push-Token bei neuen Sitzungen mit dem Braze-Backend synchronisiert. |
| **Automatische Registrierung von Service-Teammitgliedern deaktivieren** | `manageServiceWorkerExternally` | Bitte verwenden Sie diese Option, wenn Sie den Service Worker selbst registrieren und verwalten. |
| **Cookies deaktivieren** | `noCookies` | Verwendet localStorage anstelle von Cookies für Nutzerdaten und Sitzungsdaten. Verhindert die domänenübergreifende Erkennung. |
| **Font Awesome deaktivieren** | `doNotLoadFontAwesome` | Verhindert, dass das SDK Font Awesome aus dem CDN lädt. Bitte verwenden Sie diese Option, wenn Ihre Website über eine eigene Font Awesome-Datei verfügt. |
| **SDK-Authentifizierung aktivieren** | `enableSdkAuthentication` | Aktiviert [die SDK-Authentifizierung]({{site.baseurl}}/developer_guide/sdk_integration/authentication/). |
| **Web-SDK-Protokollierung aktivieren** | `enableLogging` | Aktiviert die Konsolenprotokollierung für die Fehlersuche. Bitte vor dem Produkt entfernen. |
| **Mindestintervall zwischen getriggerten Nachrichten** | `minimumIntervalBetweenTriggerActionsInSeconds` | Mindestzeit in Sekunden zwischen Aktionen, die getriggert werden (Standard: 30). |
| **Karten in einem neuen Tab öffnen** | `openCardsInNewTab` | Öffnet Content-Card-Links in einem neuen Tab, wenn die Standard-Feed-UI verwendet wird. |
| **Standort des Service-Teammitglieds** | `serviceWorkerLocation` | Benutzerdefinierter Pfad für die Service-Worker-Datei (Standard: `/service-worker.js`). |
| **Sitzungszeitlimit (Sekunden)** | `sessionTimeoutInSeconds` | Zeitlimit für die Sitzung in Sekunden (Standard: 1800). |

{% alert note %}
Um [benutzerdefinierte HTML-In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/) bei Verwendung des Google Tag Manager Braze Initialization Tag zu aktivieren, wählen Sie **bitte „HTML-In-App-Nachrichten zulassen“** in **den Braze-Initialisierungsoptionen** aus. Die Abbildung dieses Kontrollkästchens entspricht der`allowUserSuppliedJavascript`Initialisierungsoption in`braze.initialize()`und setzt diese auf `true`. Das Google Tag Manager Braze Initialisierungstag verwendet dieses Label anstelle des Optionsnamens.
{% endalert %}

Für Optionen, die nicht im GTM-Template verfügbar sind (wie `contentSecurityNonce`, `localization`, oder `devicePropertyAllowlist`), verwenden Sie bitte stattdessen [die Laufzeitinitialisierung]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web).

### Schritt 5: Auf *allen Seiten* triggern

Das Initialisierungs-Tag sollte auf allen Seiten Ihrer Website ausgeführt werden. Dies ist zulässig für die Nutzung der Braze SDK-Methoden und die Erfassung von Web-Push-Analytics.

### Schritt 6: Bitte überprüfen Sie Ihre Integration.

Sie können Ihre Integration mit einer der folgenden Optionen überprüfen:

- **Option 1:** Mit [dem Debugging-Tool](https://support.google.com/tagmanager/answer/6107056?hl=en) von Google Tag Manager können Sie überprüfen, ob das Braze-Initialisierungstag auf Ihren konfigurierten Seiten oder Ereignissen korrekt ausgelöst wird.
- **Option 2:** Bitte überprüfen Sie, ob von Ihrer Webseite aus Netzwerk-Anfragen an Braze gestellt werden. Darüber hinaus sollte nun die globale`window.braze`Bibliothek definiert werden.
