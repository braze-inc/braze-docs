---
nav_title: Segment
article_title: Segment
page_order: 1
alias: /partners/segment/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Segment, einer Plattform für Kundendaten, die Informationen sammelt und zwischen den Quellen in Ihrem Marketing-Stack weiterleitet."
page_type: partner
search_tag: Partner

---

# Segment

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment][5] ist eine Plattform für Kundendaten, mit der Sie Ihre Kundendaten sammeln, bereinigen und aktivieren können. 

Die Integration von Braze und Segment ermöglicht es Ihnen, Ihre Benutzer zu verfolgen und Daten an verschiedene Anbieter von Benutzeranalysen weiterzuleiten. Mit Segment können Sie:
- Synchronisieren Sie [Segment Engage]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_engage/) mit Braze zur Verwendung in Braze-Kampagnen und Canvas-Segmentierung.
- [Importieren Sie Daten zwischen den beiden Plattformen](#integration-options). Wir bieten eine Side-by-Side-SDK-Integration für Ihre Android-, iOS- und Webanwendungen sowie eine Server-zu-Server-Integration für die Synchronisierung Ihrer Daten mit den REST-APIs von Braze
- [Verbinden Sie Daten mit Segment über Currents]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/). 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Segment-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein [Segment-Konto](https://app.segment.com/login) erforderlich. |
| Installierte Quellcode- und [Segment-Source-Bibliotheken](https://segment.com/docs/sources/) | Der Ursprung aller Daten, die an Segment gesendet werden, wie z.B. mobile Apps, Websites oder Backend-Server.<br><br>Sie müssen die Bibliotheken in Ihrer Anwendung, Website oder auf Ihrem Server installieren, bevor Sie einen erfolgreichen `Source > Destination` Ablauf einrichten können. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Um Braze und Segment zu integrieren, müssen Sie [Braze als Ziel](#connection-settings) in Übereinstimmung mit dem [von Ihnen gewählten Integrationstyp](#integration-options) (Verbindungsmodus) festlegen. Wenn Sie ein neuer Braze-Kunde sind, können Sie historische Daten mit Hilfe von [Segmentwiedergaben](#segment-replays) an Braze weitergeben. Als nächstes müssen Sie [Mappings](#methods) einrichten und [Ihre Integration testen](#step-4-test-your-integration), um einen reibungslosen Datenfluss zwischen Braze und Segment sicherzustellen.

### Schritt 1: Ein Lötziel erstellen {#connection-settings}

Nachdem Sie Ihre Quellen erfolgreich eingerichtet haben, müssen Sie Braze als [Ziel](https://segment.com/docs/destinations/) für jede Quelle konfigurieren (iOS, Android, Web, etc.). In den Verbindungseinstellungen haben Sie viele Möglichkeiten, den Datenfluss zwischen Braze und Segment anzupassen.

### Schritt 2: Wählen Sie das Ziel-Framework und den Verbindungstyp {#integration-options}

Navigieren Sie in Segment zu **Ziele > Braze > Braze konfigurieren > Wählen Sie Ihre Quelle > Einrichtung**.

![Die Seite zur Einrichtung der Quelle. Diese Seite enthält Einstellungen, mit denen Sie das Ziel-Framework entweder als "Aktionen" oder "klassisch" und den Verbindungsmodus entweder als "Cloud-Modus" oder "Gerätemodus" festlegen können.][42]

Sie können die Web-Source-Bibliotheken von Segment (Analytics.js) und die nativen clientseitigen Bibliotheken mit Braze integrieren, indem Sie entweder eine Side-by-Side-Integration (Device-Mode) oder eine Server-to-Server-Integration (Cloud-Mode) verwenden.

Die Wahl des Verbindungsmodus hängt von der Art der Quelle ab, für die das Ziel konfiguriert ist.

| Integration | Details |
| ----------- | ------- |
| [Seite an Seite<br>(device-mode)](#side-by-side-sdk-integration) |Verwendet das SDK von Segment, um Ereignisse in die nativen Aufrufe von Braze zu übersetzen. Dies ermöglicht den Zugriff auf tiefere Funktionen und eine umfassendere Nutzung von Braze als bei der Server-zu-Server-Integration.<br><br>Beachten Sie, dass Segment nicht alle Braze-Methoden (z.B. Content Cards) unterstützt. Um eine Braze-Methode zu verwenden, die nicht durch ein entsprechendes Mapping abgebildet wird, müssen Sie die Methode durch Hinzufügen von nativem Braze-Code zu Ihrer Codebasis aufrufen. |
| [Server-zu-Server<br>(cloud-mode)](#server-to-server-integration) | Leitet Daten von Segment an die REST-API-Endpunkte von Braze weiter.<br><br>Unterstützt keine Braze UI-Funktionen wie In-App-Nachrichten, Content Cards oder Push-Benachrichtigungen. Es gibt auch automatisch erfasste Daten, wie z.B. Felder auf Geräteebene, die mit dieser Methode nicht verfügbar sind.<br><br>Ziehen Sie eine Side-by-Side-Integration in Betracht, wenn Sie diese Funktionen nutzen möchten.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Besuchen Sie [Segment](https://segment.com/docs/destinations/#connection-modes), um mehr über die beiden Integrationsoptionen (Verbindungsmodi) und die jeweiligen Vorteile zu erfahren.
{% endalert %}

#### Nebeneinander liegende SDK-Integration

Diese auch als Device-Mode bezeichnete Integration ordnet das SDK und die [Methoden](#methods) von Segment dem Braze-SDK zu und ermöglicht den Zugriff auf alle Funktionen, die unser SDK bietet, wie Push, In-App-Messaging und andere Braze-eigene Methoden. 

{% alert note %}
Wenn Sie den Gerätemodus von Segment verwenden, müssen Sie das Braze SDK nicht direkt integrieren. Wenn Sie Braze als Ziel im Gerätemodus für Segment hinzufügen, wird das Segment SDK das Braze SDK initialisieren und die entsprechenden zugeordneten Braze-Methoden aufrufen.
{% endalert %}

Wenn Sie eine Verbindung im Gerätemodus verwenden, ähnlich wie bei der nativen Integration des Braze SDK, weist das Braze SDK jedem Benutzer eine `device_id` und eine Backend-Kennung, `braze_id`, zu. Dadurch kann Braze die anonyme Aktivität des Geräts erfassen, indem es diese Identifikatoren anstelle von `userId` abgleicht. 

{% tabs local %}
{% tab Android %}

{% alert important %}
Der Quellcode für die Integration des Android-Gerätemodus wird von Braze gepflegt und regelmäßig aktualisiert, um neue Braze SDK-Versionen zu berücksichtigen.

<br>
Welches Braze SDK Sie verwenden, hängt davon ab, welches Segment SDK Sie verwenden:

| Segment SDK | Braze SDK |
| - | ----------- | --------- |
| Bevorzugt | [Analytik-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| Legacy | [Analytics-Android](https://github.com/segmentio/analytics-android) | [Braze Segment Android](https://github.com/braze-inc/braze-segment-android) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endalert %}

Um Braze als Ziel im Gerätemodus für Ihre Android-Quelle einzurichten, wählen Sie **Classic** als Ziel-Framework und klicken auf **Speichern**. 

![]({% image_buster /assets/img/segment/android.png %})

Um die Side-by-Side-Integration zu vervollständigen, lesen Sie bitte die detaillierte Anleitung von Segment zum Hinzufügen der Braze-Zielabhängigkeit zu Ihrer [Android-App](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/).

Der Quellcode für die Integration [des Android-Gerätemodus](https://github.com/braze-inc/braze-segment-kotlin) wird von Braze gepflegt und regelmäßig aktualisiert, um neue Braze SDK-Versionen zu berücksichtigen.

{% endtab %}
{% tab iOS %}

{% alert important %}
Der Quellcode für die Integration des iOS-Gerätemodus wird von Braze gepflegt und regelmäßig aktualisiert, um neue Braze SDK-Versionen zu berücksichtigen.

<br>
Welches Braze SDK Sie verwenden, hängt davon ab, welches Segment SDK Sie verwenden:

| Segment SDK | Braze SDK |
| - | ----------- | --------- |
| Bevorzugt | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze Segment Swift](https://github.com/braze-inc/braze-segment-swift) |
| Legacy | [Analytics-iOS](https://github.com/segmentio/analytics-ios) | [Braze Segment iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endalert %}

Um Braze als Ziel im Gerätemodus für Ihre iOS-Quelle einzurichten, wählen Sie **Classic** als Ziel-Framework und klicken auf **Speichern**. 

![]({% image_buster /assets/img/segment/ios.png %})

Um die Side-by-Side-Integration zu vervollständigen, lesen Sie die ausführliche Anleitung von Segment zum Hinzufügen des Braze Segment Pods zu Ihrer [iOS-App](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/).

Der Quellcode für die Integration des [iOS-Gerätemodus](https://github.com/braze-inc/braze-segment-swift) wird von Braze gepflegt und regelmäßig aktualisiert, um neue Braze SDK-Versionen zu berücksichtigen.

{% endtab %}
{% tab Web oder JavaScript %}

Das neue Braze Web Mode (Actions) Framework von Segment wird für die Einrichtung von Braze als Device-Mode-Ziel für Ihre Webquelle empfohlen. 

Wählen Sie in der Setup-Benutzeroberfläche **Aktionen** als Ziel-Framework und **Gerätemodus** als Verbindungsmodus.

![]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
Der Quellcode für das [React Native Braze Plugin](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze) wird von Segment gepflegt und regelmäßig aktualisiert, um neue Braze SDK-Versionen zu berücksichtigen.

Wenn Sie eine React Native Segment Source mit Braze verbinden, müssen Sie eine Quelle und ein Ziel pro Betriebssystem einrichten. Zum Beispiel, indem Sie ein iOS-Ziel und ein Android-Ziel einrichten. 

Innerhalb Ihrer App-Codebasis initialisieren Sie das Segment SDK bedingt nach Gerätetyp, indem Sie den jeweiligen Quellcode-Schreibschlüssel verwenden, der mit jeder App verbunden ist.

Wenn ein Push-Token von einem Gerät registriert und an Braze gesendet wird, wird es mit der App-Kennung verknüpft, die bei der Initialisierung des SDK verwendet wurde. Die gerätetypabhängige Initialisierung stellt sicher, dass alle an Braze gesendeten Push-Token mit der entsprechenden App verknüpft sind.

{% alert important %}
Wenn die React Native-App Braze mit demselben Braze-App-Identifikator für alle Geräte initialisiert, werden alle React Native-Benutzer in Braze als Android- oder iOS-Benutzer betrachtet und alle Push-Tokens werden mit diesem Betriebssystem verknüpft.
{% endalert %}

Um Braze als Ziel im Gerätemodus für jede Quelle einzurichten, wählen Sie **Classic** als Ziel-Framework und klicken Sie auf **Speichern**.

{% endtab %}
{% endtabs %}

#### Server-zu-Server-Integration

Diese Integration wird auch als Cloud-Modus bezeichnet und leitet Daten von Segment an die REST-APIs von Braze weiter. Verwenden Sie das neue [Braze Cloud Mode (Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) Framework von Segment, um ein Cloud-Modus-Ziel für jede Ihrer Quellen einzurichten. 

Im Gegensatz zur Side-by-Side-Integration unterstützt die Server-zu-Server-Integration nicht die UI-Funktionen von Braze, wie z. B. In-App-Messaging, Content Cards oder die automatische Registrierung von Push-Token. Es gibt auch [automatisch erfasste]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection) Daten (z. B. anonyme Benutzer und Felder auf Geräteebene), die im Cloud-Modus nicht verfügbar sind.

Wenn Sie diese Daten und diese Funktionen nutzen möchten, sollten Sie die SDK-Integration im Side-by-Side-Modus (Gerätemodus) verwenden.

Der Quellcode für das [Ziel Braze Cloud Mode (Actions)](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze) wird von Segment verwaltet.

### Schritt 3: Einstellungen

Legen Sie die Einstellungen für Ihr Ziel fest. Nicht alle Einstellungen werden auf alle Zieltypen angewendet.

{% tabs local %}
{% tab Modus für mobile Geräte %}

| Einstellung | Beschreibung |
| ------- | ----------- |
| App Kennung | Der App-Identifikator, der verwendet wird, um die spezifische App zu referenzieren. Diese finden Sie im Braze-Dashboard unter **Einstellungen verwalten** | 
| Benutzerdefinierter API-Endpunkt<br>(SDK-Endpunkt) | Ihr Braze SDK-Endpunkt, der Ihrer Instanz entspricht (z. B. `sdk.iad-01.braze.com`) | 
| Endpunkt Region | Ihre Braze-Instanz (z.B. US 01, US 02, EU 01, usw.) | 
| Aktivieren Sie die automatische Registrierung von Nachrichten in der App | Deaktivieren Sie dies, wenn Sie In-App-Nachrichten manuell registrieren möchten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Web Device-Modus %}

| Einstellung | Beschreibung |
| ------- | ----------- |
| App Kennung | Der App-Identifikator, der verwendet wird, um die spezifische App zu referenzieren. Diese finden Sie im Braze-Dashboard unter **Einstellungen verwalten** | 
| Benutzerdefinierter API-Endpunkt<br>(SDK-Endpunkt) | Ihr Braze SDK-Endpunkt, der Ihrer Instanz entspricht (z. B. `sdk.iad-01.braze.com`) | 
| Safari Website Push-ID | Wenn Sie Safari-Push unterstützen, müssen Sie diese Option mit der Website-Push-ID angeben, die Sie Apple bei der Erstellung Ihres Safari-Push-Zertifikats mitgeteilt haben (beginnt mit `web`, zum Beispiel `web.com.example.domain`). |
| Braze Web SDK Version | Die Version des Braze Web SDK, die Sie verwenden möchten |
| Automatisch In-App-Nachrichten senden | Standardmäßig werden alle In-App-Nachrichten, für die ein Nutzer berechtigt ist, automatisch an den Nutzer zugestellt. Deaktivieren Sie dies, wenn Sie In-App-Nachrichten manuell anzeigen möchten. |
| Schriftart awesome nicht laden | Braze verwendet Font Awesome für In-App-Nachrichten-Symbole. Standardmäßig lädt Braze FontAwesome automatisch aus dem FontAwesome CDN. Um dieses Verhalten zu deaktivieren (zum Beispiel, weil Ihre Website eine angepasste Version von FontAwesome verwendet), setzen Sie diese Option auf `TRUE`. Beachten Sie, dass Sie in diesem Fall dafür verantwortlich sind, dass FontAwesome auf Ihrer Website geladen ist - andernfalls werden die In-App-Meldungen möglicherweise nicht korrekt dargestellt. |
| Aktivieren Sie HTML-In-App-Nachrichten | Wenn Sie diese Option aktivieren, können Benutzer von Braze Dashboard HTML-In-App-Nachrichten verwenden. | 
| In-App-Nachrichten in einer neuen Registerkarte öffnen | Standardmäßig werden Links aus In-App-Nachrichten in der aktuellen Registerkarte oder in einer neuen Registerkarte geladen, wie im Dashboard für jede einzelne Nachricht festgelegt. Setzen Sie diese Option auf `TRUE`, um zu erzwingen, dass alle Links von In-App-Nachrichten in einem neuen Tab oder Fenster geöffnet werden. |
| In-App Nachricht z Index | Geben Sie einen Wert für diese Option an, um die Standard-Z-Indizes von Braze außer Kraft zu setzen. | 
| Explizite Ablehnung von In-App-Nachrichten verlangen | Wenn eine In-App-Nachricht angezeigt wird, wird diese standardmäßig durch Drücken der Escape-Taste oder einen Klick auf den ausgegrauten Hintergrund der Seite geschlossen. Setzen Sie diese Option auf true, um dieses Verhalten zu verhindern und einen expliziten Klick auf eine Schaltfläche zu verlangen, um Nachrichten zu schließen. |
| Mindestintervall zwischen Auslöseaktionen in Sekunden | Der Standardwert ist 30.<br>Standardmäßig wird eine Trigger-Aktion nur dann ausgelöst, wenn seit der letzten Trigger-Aktion mindestens 30 Sekunden verstrichen sind. Geben Sie einen Wert für diese Konfigurationsoption an, um diesen Standardwert mit einem eigenen Wert zu überschreiben. Wir empfehlen, diesen Wert nicht kleiner als 10 zu wählen, um den Benutzer nicht mit Benachrichtigungen zu überhäufen.|
| Standort des Servicemitarbeiters | Bei der Registrierung von Benutzern für Web-Push-Benachrichtigungen sucht Braze standardmäßig im Stammverzeichnis Ihres Webservers unter `/service-worker.js` nach der erforderlichen Service Worker-Datei. Wenn Sie Ihren Service Worker unter einem anderen Pfad auf dem Server hosten möchten, geben Sie für diese Option einen Wert an, der dem absoluten Pfad zu der Datei entspricht. (zum Beispiel: `/mycustompath/my-worker.js`). Beachten Sie, dass die Festlegung eines Wertes hier den Umfang der Push-Benachrichtigungen auf Ihrer Website einschränkt. Da sich im obigen Beispiel die Service Worker-Datei im Verzeichnis `/mycustompath/` befindet, kann `requestPushPermission` nur von Webseiten aufgerufen werden, die mit `http://yoursite.com/mycustompath/` beginnen. |
| Push-Token-Wartung deaktivieren | Standardmäßig werden Benutzer, die bereits eine Web-Push-Erlaubnis erteilt haben, ihr Push-Token bei neuen Sitzungen automatisch mit dem Braze-Backend synchronisieren, um die Zustellbarkeit sicherzustellen. Um dieses Verhalten zu deaktivieren, setzen Sie diese Option auf `FALSE`. |
| Externes Management von Servicekräften | Wenn Sie einen eigenen Service Worker haben, den Sie registrieren und dessen Lebenszyklus Sie kontrollieren, setzen Sie diese Option auf `TRUE`, und das Braze SDK wird keinen Service Worker registrieren oder deregistrieren. Wenn Sie diese Option auf `TRUE` setzen, müssen Sie den Service-Worker vor dem Aufruf von `requestPushPermission` selbst registrieren und sicherstellen, dass er den Code des Braze-Service-Workers enthält, entweder mit `self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');` oder indem Sie den Inhalt dieser Datei direkt einbinden, damit Push korrekt funktioniert. Wenn diese Option `TRUE` lautet, ist die Option `serviceWorkerLocation` irrelevant und wird ignoriert. |
| Inhaltliche Sicherheit nonce | Wenn Sie einen Wert für diese Option angeben, fügt das Braze SDK die Nonce zu allen vom SDK erstellten `<script>` und `<style>` Elementen hinzu. Dadurch kann das Braze SDK mit den Sicherheitsrichtlinien für Inhalte Ihrer Website arbeiten. Zusätzlich zur Einstellung dieser Nonce müssen Sie eventuell auch das Laden von FontAwesome zulassen. Dies können Sie tun, indem Sie `use.fontawesome.com` in die Zulässigkeitsliste Ihrer Content Security Policy aufnehmen oder die Option `doNotLoadFontAwesome` verwenden und das Programm manuell laden. |
| Crawler-Aktivität zulassen | Standardmäßig ignoriert das Braze Web SDK Aktivitäten von bekannten Spidern oder Web-Crawlern, wie z.B. Google, basierend auf dem User Agent String. Das spart Datenpunkte, macht die Analysen genauer und kann das Page Rank verbessern. Wenn Sie jedoch möchten, dass Braze stattdessen die Aktivitäten dieser Crawler protokolliert, können Sie diese Option auf `TRUE` setzen. |
| Protokollierung einschalten | Setzen Sie diese Option auf `TRUE`, um die Protokollierung standardmäßig zu aktivieren. Beachten Sie, dass Braze dadurch ein Protokoll in der JavaScript-Konsole erstellt, das für alle Benutzer sichtbar ist. Bevor Sie Ihre Seite für die Produktion freigeben, sollten Sie dies entfernen oder einen alternativen Logger mit `setLogger` bereitstellen. |
| News Feed Karten in einer neuen Registerkarte öffnen (Karten in neuer Registerkarte öffnen) | Standardmäßig werden Links von Kartenobjekten in der aktuellen Registerkarte oder im aktuellen Fenster geladen. Setzen Sie diese Option auf `TRUE`, damit Links von Karten in einem neuen Tab oder Fenster geöffnet werden. <br><br>**Hinweis:** Der News Feed ist veraltet. Braze empfiehlt Kunden, die unser News Feed-Tool verwenden, auf unseren Nachrichtenkanal Content Cards umzusteigen - er ist flexibler, anpassbarer und zuverlässiger. Lesen Sie den [Migrationsleitfaden]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) für mehr. |
| Erlauben Sie vom Benutzer geliefertes JavaScript | Standardmäßig lässt das Braze Web SDK keine benutzerdefinierten JavaScript-Klickaktionen zu, da es den Benutzern des Braze Dashboards erlaubt, JavaScript auf Ihrer Website auszuführen. Um anzugeben, dass Sie den Braze Dashboard-Benutzern zutrauen, nicht bösartige JavaScript-Klickaktionen zu schreiben, setzen Sie diese Eigenschaft auf `TRUE`. Wenn `enableHtmlInAppMessages` auf `TRUE` steht, wird diese Option auch auf `TRUE` gesetzt. |
| App Version| Wenn Sie einen Wert für diese Option angeben, werden die an Braze gesendeten Benutzerereignisse mit der angegebenen Version assoziiert, die zur Benutzersegmentierung verwendet werden kann. |
| Zeitüberschreitung der Sitzung in Sekunden | Der Standardwert ist 30.<br>Standardmäßig werden Sitzungen nach 30 Minuten Inaktivität beendet. Geben Sie einen Wert für diese Konfigurationsoption an, um diesen Standardwert mit einem eigenen Wert zu überschreiben. | 
| Geräteeigenschaft allowlist | Standardmäßig erkennt und sammelt das Braze SDK automatisch alle Geräteeigenschaften in `DeviceProperties`. Um dieses Verhalten außer Kraft zu setzen, geben Sie ein Array von `DeviceProperties` an. Beachten Sie, dass ohne einige Eigenschaften nicht alle Funktionen ordnungsgemäß funktionieren werden. Zum Beispiel funktioniert die Zustellung in der lokalen Zeitzone nicht ohne die Zeitzone. |
| Lokalisierung | Standardmäßig werden alle vom SDK generierten, für den Benutzer sichtbaren Meldungen in der Browsersprache des Benutzers angezeigt. Geben Sie einen Wert für diese Option an, um dieses Verhalten außer Kraft zu setzen und eine bestimmte Sprache zu erzwingen. Der Wert für diese Option sollte ein ISO 639-1 Sprachcode sein. |
| Keine Cookies | Standardmäßig speichert das Braze SDK kleine Datenmengen (Benutzer-IDs, Sitzungs-IDs) in Cookies. Dies geschieht, damit Braze Benutzer und Sitzungen über verschiedene Subdomänen Ihrer Website hinweg erkennen kann. Wenn dies für Sie ein Problem darstellt, geben Sie `TRUE` für diese Option ein, um die Cookie-Speicherung zu deaktivieren und sich vollständig auf HTML 5 localStorage zu verlassen, um Benutzer und Sitzungen zu identifizieren. |
| Alle Seiten verfolgen | **Nur klassisches Ziel Web Device-Mode (Wartung)**<br><br>Segment empfiehlt die Migration zum Web Actions-Framework, wo diese Einstellung [über Zuordnungen aktiviert](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping) werden kann.<br><br>Dadurch werden alle [Seitenaufrufe](https://segment.com/docs/spec/page/) als Ereignis "Seite geladen/angesehen" an Braze gesendet. |
| Nur benannte Seiten verfolgen | **Nur klassisches Ziel Web Device-Mode (Wartung)**<br><br>Segment empfiehlt die Migration zum Web Actions-Framework, wo diese Einstellung [über Zuordnungen aktiviert](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping) werden kann.<br><br>Dadurch werden nur Seitenaufrufe an Braze gesendet, die mit einem Namen verknüpft sind. |
| Kauf protokollieren, wenn Einnahmen vorhanden sind | **Nur klassisches Ziel Web Device-Mode (Wartung)**<br><br>Segment empfiehlt die Migration zum Web Actions-Framework, wo diese Einstellung [über Zuordnungen aktiviert](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping) werden kann.<br><br>Wenn diese Option aktiviert ist, lösen alle Track-Aufrufe mit der Eigenschaft Umsatz ein Kaufereignis aus. | 
| Nur bekannte Benutzer verfolgen | **Nur klassisches Ziel Web Device-Mode (Wartung)**<br><br>Segment empfiehlt die Migration auf das Ziel Web Actions Framework, wo diese Einstellung über Mappings aktiviert werden kann.<br><br>Wenn diese neue Einstellung aktiviert ist, wird der Aufruf von `window.appboy.initialize` so lange verzögert, bis eine gültige `userId` vorhanden ist. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Cloud-Modus %}

| Einstellung | Beschreibung |
| ------- | ----------- |
| App Kennung | Der App-Identifikator, der verwendet wird, um die spezifische App zu referenzieren. Diese finden Sie im Braze-Dashboard unter **Einstellungen verwalten** | 
| REST-API-Schlüssel | Diese finden Sie in Ihrem Braze Dashboard unter **Einstellungen** > **API-Schlüssel**. | 
| Benutzerdefinierter REST-API-Endpunkt | Ihr Braze REST-Endpunkt, der Ihrer Instanz entspricht (z. B. rest.iad-01.braze.com). | 
| Nur vorhandene Nutzer:innen aktualisieren | **Klassisches Ziel Nur Cloud-Modus (Wartung)**<br><br>Segment empfiehlt die Migration auf das Ziel Cloud Actions Framework, wo diese Einstellung [über Zuordnungen aktiviert](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping) werden kann.<br><br>Legt fest, ob nur bestehende Benutzer aktualisiert werden sollen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Schritt 4: Karten-Methoden {#methods}

Braze unterstützt die Methoden [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page), [Identify](https://segment.com/docs/spec/identify/) und [Track](https://segment.com/docs/spec/track/) Segment. Welche Arten von Identifikatoren bei diesen Methoden verwendet werden, hängt davon ab, ob die Daten über eine Server-zu-Server- (Cloud-Modus) oder eine Side-by-Side-Integration (Geräte-Modus) gesendet werden. In den Zielen Braze Web Mode Actions und Cloud Mode Actions können Sie auch ein Mapping für einen [Segment-Alias-Anruf](https://segment.com/docs/connections/spec/alias/) einrichten. 

{% alert note %}
Obwohl Benutzer-Aliase als Bezeichner im Ziel Braze Cloud Mode (Actions) unterstützt werden, ist zu beachten, dass der Alias-Aufruf von Segment nicht direkt mit Braze-Benutzer-Aliasen zusammenhängt.
{% endalert %}

| Identifikator Typ | Unterstütztes Ziel |
| --------------- | --------------------- |
| `userId` (`external_id`) | Alle |
| Anonymer Benutzer | Ziele im Gerätemodus |
| Benutzer-Alias | Ziele im Cloud-Modus |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Das Ziel Cloud-Modus (Aktionen) bietet eine [Aktion Alias erstellen](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias), mit der Sie einen reinen Alias-Benutzer erstellen oder einen Alias zu einem bestehenden `external_id` Profil hinzufügen können. Die [Aktion Benutzer identifizieren](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user) kann zusammen mit der Aktion Alias erstellen verwendet werden, um einen reinen Alias-Benutzer mit einem `external_id` zusammenzuführen, nachdem ein Alias für den Benutzer verfügbar wird. 

Es ist auch möglich, einen Workaround zu entwickeln und `braze_id` zu verwenden, um anonyme Benutzerdaten im Cloud-Modus zu senden. Dazu müssen Sie die `braze_id` des Benutzers manuell in alle Ihre Segment-API-Aufrufe aufnehmen. In der [Dokumentation von Segment](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users) erfahren Sie mehr darüber, wie Sie diese Abhilfe einrichten können.

An Braze gesendete Zieldaten können im Rahmen von Cloud-Modus-Aktionen gebündelt werden. Die Chargengröße ist auf 75 Ereignisse begrenzt, und diese Chargen sammeln sich über einen Zeitraum von 30 Sekunden an, bevor sie gespült werden. Das Stapeln von Anfragen wird pro Aktion durchgeführt. Zum Beispiel werden Identify Calls (Attribute) in einer Anfrage und Track Calls (benutzerdefinierte Ereignisse) in einer zweiten Anfrage zusammengefasst. Braze empfiehlt, diese Funktion zu aktivieren, da dadurch die Anzahl der Anfragen, die von Segment an Braze gesendet werden, reduziert wird. Dadurch verringert sich das Risiko, dass das Ziel auf die Ratenbeschränkungen von Braze stößt und Anfragen wiederholt werden müssen. 

Sie können die Stapelverarbeitung für eine Aktion aktivieren, indem Sie zu Ihrem Braze-Ziel > **Zuordnungen** navigieren. Klicken Sie dort auf das 3-Punkte-Symbol rechts neben der Zuordnung und wählen Sie **Zuordnung bearbeiten**. Scrollen Sie zum Ende des Abschnitts **Zuordnungen auswählen** und vergewissern Sie sich, dass **Stapeldaten zum Löten** auf **Ja** eingestellt ist.


{% tabs local %}
{% tab Identifizieren Sie %}
#### Identifizieren Sie

Mit dem Aufruf [Identifizieren](https://segment.com/docs/spec/identify/) können Sie einen Benutzer mit seinen Aktionen verknüpfen und Attribute über ihn aufzeichnen. 

Bestimmte Segment-Spezialeigenschaften entsprechen den Standard-Attributprofilfeldern in Braze:

| Besondere Segmenteigenschaften | Standard-Attribute zum Löten |
| ------------- | ----------- |
| `userId` | `external_id` |
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `email` | `email` |
| `birthday` | `dob` |
| `address.country` | `country` |
| `address.city` | `home_city` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Andere reservierte Braze-Profilfelder wie `email_subscribe` und `push_subscribe` können gesendet werden, indem Sie die Braze-Namenskonvention für diese Felder verwenden und sie als Traits innerhalb eines Identify-Aufrufs übergeben.

##### Hinzufügen eines Benutzers zu einer Abonnementgruppe

Sie können einen Benutzer auch bei einer bestimmten Abonnementgruppe anmelden oder abmelden, indem Sie die folgenden Felder im Parameter traits verwenden.

Verwenden Sie das reservierte Braze-Profilfeld namens `braze_subscription_groups`, das mit einem Array von Objekten verknüpft werden kann. Jedes Objekt im Array sollte zwei reservierte Schlüssel haben:

1. `subscription_group_state`: Zeigt an, ob der Benutzer `"subscribed"` oder `"unsubscribed"` zu einer bestimmten Abonnementgruppe gehört.
2. `subscription_group_id`: Stellt die eindeutige ID der Abonnementgruppe dar. Sie finden diese ID im Braze Dashboard unter **Abonnementgruppenverwaltung**.

{% subtabs %}
{% subtab Swift %}
```swift
analytics.identify(
  userId: "{your-user}",
  traits: [
    "braze_subscription_groups": [
      [
        "subscription_group_id": "{your-group-id}",
        "subscription_group_state": "subscribed"
      ],
      [
        "subscription_group_id", "{your-group-id}",
        "subscription_group_state": "unsubscribed"
      ]
    ]
  ]
)
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
analytics.identify(
  "{your-user}",
  buildJsonObject {
    put("braze_subscription_groups", buildJsonArray {
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "subscribed")
          }
        )
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "unsubscribed")
          }
        )
      }
    )
  }
)
```
{% endsubtab %}
{% subtab TypeScript %}
```typescript
analytics.identify(
  "{your-user}",
  {
    braze_subscription_groups: [
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "subscribed"
      },
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "unsubscribed"
      }
    ]
  }
)
```
{% endsubtab %}
{% endsubtabs %}

##### Angepasste Attribute

Alle anderen Eigenschaften werden als [benutzerdefinierte Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) aufgezeichnet.

| Segment-Methode | Hartlötverfahren | Beispiel |
|---|---|---|
| Identifizieren Sie sich mit der Benutzer-ID | Externe ID einstellen | Segment:  `analytics.identify("dawei");`<br>Hartlöten: `Braze.changeUser("dawei")` |
| Identifizieren Sie sich mit reservierten Zügen | Benutzerattribute festlegen | Segment: `analytics.identify({email: "dawei@braze.com"});`<br> Hartlöten: `Braze.getUser().setEmail("dawei@braze.com");`
| Identifizieren Sie sich mit benutzerdefinierten Merkmalen | Benutzerdefinierte Attribute festlegen | Segment: `analytics.identify({fav_cartoon: "Naruto"});`<br>Löten: `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| Identifizieren Sie sich mit Benutzer-ID und Merkmalen | Segment: Externe ID und Attribut festlegen | Kombinieren Sie die vorangegangenen Methoden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

In den Zielen [Web-Modus-Aktionen](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) und [Cloud-Modus-Aktionen](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile) können die oben genannten Zuordnungen mit der Aktion Benutzerprofil aktualisieren festgelegt werden.

{% alert important %}
Stellen Sie bei der Übergabe von Benutzerattributdaten sicher, dass Sie nur Werte für Attribute übergeben, die sich seit der letzten Aktualisierung geändert haben. So stellen Sie sicher, dass Sie nicht unnötig Datenpunkte für Ihr Kontingent verbrauchen. Für clientseitige Quellen verwenden Sie das [Open-Source-Middleware-Tool](https://github.com/segmentio/segment-braze-mobile-middleware) von Segment, um Ihre Integration zu optimieren und die Nutzung von Datenpunkten zu begrenzen, indem Sie doppelte `identify()` Aufrufe von Segment entprellen. 

{% endalert %}
{% endtab %}

{% tab Spur %}
#### Spur

Wenn Sie ein Ereignis verfolgen, zeichnen wir dieses Ereignis als [benutzerdefiniertes Ereignis]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) unter dem angegebenen Namen auf. 

Metadaten, die innerhalb des Eigenschaftenobjekts des Track-Aufrufs gesendet werden, werden in Braze als benutzerdefinierte Ereigniseigenschaften für das zugehörige Ereignis protokolliert. Alle [Datentypen für benutzerdefinierte Ereigniseigenschaften]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) werden unterstützt.

In den Zielen [Web-Modus-Aktionen](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) und [Cloud-Modus-Aktionen](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event) können die oben genannten Zuordnungen über die Aktion Ereignis verfolgen festgelegt werden.

| Segment-Methode | Hartlötverfahren | Beispiel |
|---|---|---|
| [Spur](https://segment.com/docs/spec/track/) | Als [benutzerdefiniertes Ereignis]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) protokolliert. | Segment: `analytics.track("played_game");` <br>Hartlöten: `Braze.logCustomEvent("played_game");`|
| [Mit Eigenschaften verfolgen](https://segment.com/docs/spec/track/) | Als [Ereigniseigenschaft]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) protokolliert. | Segment: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Hartlöten: `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Mit Produkt verfolgen](https://segment.com/docs/spec/track/) | Wird als [Kaufereignis]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/) protokolliert. | Segment: `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Hartlöten: `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

##### Bestellung abgeschlossen {#order-completed}

Wenn Sie ein Ereignis mit dem Namen `Order Completed` unter Verwendung des in der [Ecommerce API](https://segment.com/docs/spec/ecommerce/v2/) von Segment beschriebenen Formats verfolgen, zeichnen wir die Produkte auf, die Sie als [Käufe]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) aufgeführt haben.

In den Zielen [Web-Modus-Aktionen](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) und [Cloud-Modus-Aktionen](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase) kann die Standardzuordnung über die Aktion Kauf verfolgen angepasst werden.

{% endtab %}

{% tab Seite %}
#### Seite {#page}

Mit dem [Seitenaufruf](https://segment.com/docs/spec/page/) können Sie aufzeichnen, wann immer ein Benutzer eine Seite Ihrer Website sieht, zusammen mit allen optionalen Eigenschaften der Seite.

Dieser Ereignistyp kann als Auslöser in den Zielen Web Mode Actions und Cloud Actions verwendet werden, um ein benutzerdefiniertes Ereignis in Braze zu protokollieren.
{% endtab %}

{% endtabs %}

### Schritt 5: Testen Sie Ihre Integration

Wenn Sie die Side-by-Side-Integration (im Gerätemodus) verwenden, können Sie Ihre [Übersichtsmetriken][27] (Lifetime-Sitzungen, MAU, DAU, Stickiness, tägliche Sitzungen und tägliche Sitzungen pro MAU) verwenden, um sicherzustellen, dass Braze Daten von Segment erhält.

Sie können Ihre Daten auf den Seiten für [benutzerdefinierte Ereignisse][22] oder [Einnahmen][28] einsehen oder [ein Segment erstellen][23]. Auf der Seite **Benutzerdefinierte Ereignisse** des Dashboards können Sie die Anzahl der benutzerdefinierten Ereignisse im Laufe der Zeit anzeigen. Beachten Sie, dass Sie keine [Formeln][24] verwenden können, die MAU- und DAU-Statistiken enthalten, wenn Sie eine Server-zu-Server-Integration (Cloud-Modus) verwenden.

Wenn Sie Kaufdaten an Braze senden (siehe Bestellung abgeschlossen auf der Registerkarte **Verfolgen** in [Schritt 3](#methods)), können Sie auf der [Umsatzseite][28] Daten zu den Einnahmen oder Käufen in bestimmten Zeiträumen oder die Gesamteinnahmen Ihrer App einsehen.

[Wenn Sie ein Segment erstellen][26], können Sie Ihre Benutzer anhand der benutzerdefinierten Ereignis- und Attributdaten filtern.

{% alert important %}
Wenn Sie eine Server-zu-Server-Integration (Cloud-Modus) verwenden, funktionieren Filter, die sich auf automatisch erfasste Sitzungsdaten beziehen (z. B. "zuerst verwendete App" und "zuletzt verwendete App"), nicht. Verwenden Sie eine Side-by-Side-Integration (Gerätemodus), wenn Sie diese in Ihrer Segment- und Braze-Integration verwenden möchten.
{% endalert %}

## Benutzerlöschung und -unterdrückung 

Wenn Sie Benutzer löschen oder unterdrücken müssen, beachten Sie, dass [die Benutzerlöschfunktion von Segment](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) dem [Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) Braze [`/users/delete` zugeordnet]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) **ist**. Beachten Sie, dass die Überprüfung dieser Löschungen bis zu 30 Tage dauern kann.

Sie müssen sicherstellen, dass Sie eine gemeinsame Benutzerkennung für Braze und Segment wählen (wie in `external_id`). Nachdem Sie mit Segment einen Löschantrag gestellt haben, können Sie den Status auf der Registerkarte Löschanträge in Ihrem Segment-Dashboard einsehen.

## Segment-Wiederholungen

Segment bietet seinen Kunden den Service, alle historischen Daten an einen neuen Technologiepartner zu übermitteln. Neue Braze-Kunden, die alle relevanten historischen Daten importieren möchten, können dies über Segment tun. Sprechen Sie mit Ihrem Segmentvertreter, wenn Sie daran interessiert sind.

Segment stellt eine Verbindung zu unserem [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) her, um in Ihrem Namen Benutzerdaten in Braze zu importieren.

{% alert important %}
Alle Identifikatoren, die im Ziel Cloud Mode Actions unterstützt werden, werden als Teil von Segment Replays unterstützt.
{% endalert %}

## Bewährte Praktiken

{% details Prüfen Sie Anwendungsfälle, um Datenüberlastungen zu vermeiden. %}

Segment schränkt die Anzahl der Datenelemente, die die Kunden an sie senden, **nicht** ein. Mit Segmenten können Sie alle oder nur bestimmte Ereignisse an Braze senden. Anstatt alle Ihre Ereignisse über Segment zu senden, empfehlen wir Ihnen, gemeinsam mit Ihren Marketing- und Redaktionsteams zu prüfen, welche Ereignisse Sie an Braze senden möchten, um Datenüberlastungen zu vermeiden.

{% enddetails %}

{% details Verstehen Sie den Unterschied zwischen dem benutzerdefinierten API-Endpunkt und dem benutzerdefinierten REST-API-Endpunkt in den Mobile Device Mode-Zieleinstellungen. %}

| Hartlöten Terminologie | Segment-Äquivalent |
| ----------------- | ------------------ |
| Braze SDK Endpunkt | Benutzerdefinierter API-Endpunkt |
| Braze REST Endpunkt | Benutzerdefinierter REST-API-Endpunkt |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ihr Braze-API-Endpunkt (in Segment "Custom API Endpoint" genannt) ist der SDK-Endpunkt, den Braze für Ihr SDK einrichtet (z.B. `sdk.iad-03.braze.com`). Ihr Braze REST API Endpunkt (in Segment "Custom REST API Endpoint" genannt) ist der REST API Endpunkt (zum Beispiel `https://rest.iad-03.braze.com`)
{% enddetails %}

{% details Vergewissern Sie sich, dass Ihr benutzerdefinierter API-Endpunkt korrekt in die Zieleinstellungen des Mobilgerätemodus eingegeben wurde. %}

| Hartlöten Terminologie | Segment-Äquivalent |
| ----------------- | ------------------ |
| Braze SDK Endpunkt | Benutzerdefinierter API-Endpunkt |
| Braze REST Endpunkt | Benutzerdefinierter REST-API-Endpunkt |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Sie müssen das richtige Format einhalten, um sicherzustellen, dass Sie Ihren Braze SDK-Endpunkt korrekt eingeben. Ihr Braze SDK-Endpunkt darf nicht `https://` (z.B. `sdk.iad-03.braze.com`) enthalten, da sonst die Braze-Integration nicht funktioniert. Dies ist erforderlich, da Segment Ihrem Endpunkt automatisch `https://` voranstellt, was dazu führt, dass Braze mit einem ungültigen Endpunkt `https://https://sdk.iad-03.braze.com` initialisiert wird.

{% enddetails %}

{% details Nuancen der Datenzuordnung. %}

Szenarien, in denen die Daten nicht wie erwartet weitergegeben werden:

1. Verschachtelte benutzerdefinierte Attribute
  - Obwohl [verschachtelte benutzerdefinierte Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/) technisch über Segment an Braze gesendet werden können, wird jedes Mal die **gesamte Nutzlast** gesendet. Dadurch entstehen jedes Mal, wenn die Nutzlast gesendet wird, [Datenpunkte]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#data-points) pro im verschachtelten Objekt übergebenen Schlüssel.<br><br> Um nur eine Teilmenge von Datenpunkten auszugeben, wenn die Nutzlast gesendet wird, können Sie die benutzerdefinierten [Zielfunktionen](https://segment.com/docs/connections/functions/destination-functions/) von Segment verwenden. Mit dieser Funktion der Segment-Plattform können Sie festlegen, wie die Daten an nachgelagerte Ziele gesendet werden.

  {% alert note %}
  Benutzerdefinierte Zielfunktionen werden innerhalb von Segment gesteuert, und Braze hat nur begrenzten Einblick in Funktionen, die extern konfiguriert wurden.
  {% endalert %}

{: start="2"}
2\. Übermittlung anonymer Daten von Server zu Server.
  - Kunden können die Server-to-Server-Bibliotheken von Segment nutzen, um anonyme Daten an andere Systeme weiterzuleiten. Im Abschnitt Kartenmethoden erfahren Sie mehr darüber, wie Sie Benutzer ohne `external_id` über eine Server-zu-Server-Integration (Cloud-Modus) an Braze senden können.

{% enddetails %}

{% details Anpassung der Initialisierung von Braze. %}

Es gibt verschiedene Möglichkeiten, Braze anzupassen: Push, In-App-Nachrichten, Content Cards und Initialisierung. Mit einer Side-by-Side-Integration können Sie Push, In-App-Nachrichten und Content Cards wie bei einer direkten Braze-Integration anpassen.

Es kann jedoch schwierig und manchmal nicht möglich sein, eine Anpassung vorzunehmen, wenn das Braze SDK integriert ist, oder Initialisierungskonfigurationen festzulegen. Das liegt daran, dass Segment das Braze SDK für Sie initialisiert, wenn die Segment-Initialisierung erfolgt.

{% enddetails %}

{% details Senden Sie Deltas an Braze. %}

Stellen Sie bei der Übergabe von Benutzerattributdaten sicher, dass Sie nur Werte für Attribute übergeben, die sich seit der letzten Aktualisierung geändert haben. So stellen Sie sicher, dass Sie nicht unnötig Datenpunkte für Ihr Kontingent verbrauchen. Für clientseitige Quellen verwenden Sie das [Open-Source-Middleware-Tool](https://github.com/segmentio/segment-braze-mobile-middleware) von Segment, um Ihre Integration zu optimieren und die Verwendung von Datenpunkten zu begrenzen, indem Sie doppelte `identify()` Aufrufe von Segment entprellen. 

{% enddetails %}


[5]: https://segment.com
[13]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events
[14]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[18]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[19]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[22]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data/#custom-event-data
[23]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[24]: {{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula/#creating-a-formula
[25]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection
[26]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[27]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/
[28]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[36]: https://segment.com/docs/sources/#server
[38]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[39]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[40]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[41]: https://segment.com/docs/spec/identify/#user-id
[42]: {% image_buster /assets/img/segment/setup.png %}
[43]: {% image_buster /assets/img/segment/website.png %}
[44]: {% image_buster /assets/img/segment/ios.png %}
[45]: {% image_buster /assets/img/segment/android.png %}
