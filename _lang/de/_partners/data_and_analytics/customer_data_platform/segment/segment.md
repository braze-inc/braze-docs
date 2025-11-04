---
nav_title: Segment
article_title: Segment
page_order: 1
alias: /partners/segment/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Segment, einer Customer Data Platform, die Informationen sammelt und zwischen den Quellen in Ihrem Marketing Stack weiterleitet."
page_type: partner
search_tag: Partner

---

# Segment

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> [Segmente](https://segment.com) ist eine Customer Data Platform (CDP), mit der Sie Ihre Kundendaten sammeln, bereinigen und aktivieren können. 

Die Integration von Braze und Segmente erlaubt es Ihnen, Ihre Nutzer:innen zu tracken und Daten an verschiedene Anbieter von Analytics weiterzuleiten. Segmente erlaubt Ihnen das:

- Synchronisieren Sie [Segment Engage]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_engage/) mit Braze zur Verwendung in Kampagnen und zur Segmentierung in Braze-Canvas.
- [Importieren Sie Daten zwischen den beiden Plattformen](#integration-options). Wir bieten eine Side-by-side SDK-Integration für Ihre Android-, iOS- und Internet-Anwendungen sowie eine Server-zu-Server-Integration zur Synchronisierung Ihrer Daten mit den Braze REST APIs.
- [Verbinden Sie Daten über Currents mit Segmenten]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/). 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Segmente Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein [Segment-Konto](https://app.segment.com/login) erforderlich. |
| Installierte [Bibliotheken](https://segment.com/docs/sources/) für Quellcode und Segmente | Die Herkunft der Daten, die an Segmente gesendet werden, wie z.B. mobile Apps, Websites oder Backend-Server.<br><br>Sie müssen die Bibliotheken in Ihrer App, Ihrer Website oder Ihrem Server installieren, bevor Sie einen erfolgreichen `Source > Destination` Ablauf einrichten können. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Um Braze und Segmente zu integrieren, müssen Sie [Braze als Ziel](#connection-settings) entsprechend dem [von Ihnen gewählten Integrationstyp](#integration-options) (Verbindungsmodus) festlegen. Wenn Sie ein neuer Kunde von Braze sind, können Sie historische Daten mithilfe von [Segmentierungen](#segment-replays) an Braze weitergeben. Als nächstes müssen Sie [Abbildungen](#methods) einrichten und [Ihre Integration testen](#step-4-test-your-integration), um einen reibungslosen Datenfluss zwischen Braze und Segmente zu gewährleisten.

### Schritt 1: Ein Braze-Ziel erstellen {#connection-settings}

Nachdem Sie Ihre Quellen erfolgreich eingerichtet haben, müssen Sie Braze als [Ziel](https://segment.com/docs/destinations/) für jede Quelle (iOS, Android, Internet usw.) konfigurieren. Sie haben viele Möglichkeiten, den Datenfluss zwischen Braze und Segmente über die Verbindungseinstellungen anzupassen.

### Schritt 2: Wählen Sie den Zielrahmen und die Verbindungsart {#integration-options}

Navigieren Sie in Segmente zu **Ziele** > **Braze** > **Braze konfigurieren** > **Wählen Sie Ihre Quelle aus** > **Einrichtung**.

![Die Seite zur Einrichtung der Quelle. Diese Seite enthält Einstellungen, um das Ziel-Framework als "Aktionen" oder "klassisch" und den Verbindungsmodus als "Cloud-Modus" oder "Geräte-Modus" festzulegen.]({% image_buster /assets/img/segment/setup.png %})

Sie können die Web-Source von Segmente (Analytics.js) und die nativen Client-seitigen Bibliotheken mit Braze integrieren, indem Sie entweder eine Side-by-side-Integration (im Geräte-Modus) oder eine Server-zu-Server-Integration (im Cloud-Modus) verwenden.

Die Wahl des Verbindungsmodus hängt von der Art der Quelle ab, für die das Ziel konfiguriert ist.

| Integration | Details |
| ----------- | ------- |
| [Seite an Seite<br>(Gerätemodus)](#side-by-side-sdk-integration) |Verwendet das SDK von Segment, um Ereignisse in native Braze-Aufrufe zu übersetzen, was den Zugriff auf tiefere Features und eine umfassendere Nutzung von Braze als bei der Server-zu-Server-Integration zulässt.<br><br>Beachten Sie, dass Segmente nicht alle Braze-Methoden unterstützen (z.B. Content-Cards). Um eine Braze-Methode zu verwenden, die nicht durch eine entsprechende Abbildung abgebildet ist, müssen Sie die Methode aufrufen, indem Sie Ihrer Codebasis nativen Braze-Code hinzufügen. |
| [Server-zu-Server<br>(cloud-mode)](#server-to-server-integration) | Leitet Daten von Segmenten an Braze REST API Endpunkte weiter.<br><br>Unterstützt keine Braze UI Features wie In-App-Nachrichten, Content-Cards oder Push-Benachrichtigungen. Es gibt auch automatisch erfasste Daten, wie z.B. Felder auf Geräteebene, die mit dieser Methode nicht verfügbar sind.<br><br>Ziehen Sie eine Side-by-side-Integration in Betracht, wenn Sie diese Features nutzen möchten.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Besuchen Sie [Segmente](https://segment.com/docs/destinations/#connection-modes), um mehr über die beiden Integrationsmöglichkeiten (Verbindungsmodi) zu erfahren, einschließlich der jeweiligen Vorteile.
{% endalert %}

#### Side-by-side-Integration von SDKs

Diese Integration, die auch als Gerätemodus bezeichnet wird, bildet das SDK und die [Methoden](#methods) von Segmente auf das SDK von Braze ab und erlaubt so den Zugriff auf alle Features, die unser SDK bietet, wie Push, In-App-Nachricht und andere Methoden, die von Braze stammen. 

{% alert note %}
Wenn Sie den Gerätemodus von Segmente verwenden, müssen Sie das Braze SDK nicht direkt integrieren. Wenn Sie Braze als Ziel für Segmente im Gerätemodus hinzufügen, wird das Segment SDK das Braze SDK initialisieren und die entsprechenden abgebildeten Braze-Methoden aufrufen.
{% endalert %}

Bei der Verwendung einer Verbindung im Gerätemodus weist das Braze SDK, ähnlich wie bei der nativen Integration des Braze SDK, jedem Nutzer:innen einen `device_id` und einen Backend-Bezeichner, `braze_id`, zu. Dies erlaubt es Braze, anonyme Aktivitäten des Geräts zu erfassen, indem diese Bezeichner anstelle von `userId` abgeglichen werden. 

{% tabs local %}
{% tab Android %}

{% alert important %}
Der Code für die Integration in den Android-Gerätemodus wird von Braze gepflegt und regelmäßig aktualisiert, um neue Braze SDK-Versionen zu berücksichtigen.

<br>
Welches Braze SDK Sie verwenden, hängt davon ab, welches Segment SDK Sie verwenden:

| Segmente | Segment SDK | Braze SDK | Segmentierung
| - | ----------- | --------- |
| Bevorzugt | [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| Legacy | [Analytics-Android](https://github.com/segmentio/analytics-android) | [Braze Segment Android](https://github.com/braze-inc/braze-segment-android) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endalert %}

Um Braze als Ziel im Gerätemodus für Ihre Android-Quelle einzurichten, wählen Sie **Aktionen** als **Ziel-Framework** und dann **Speichern**. 

Um die Side-by-side-Integration zu vervollständigen, lesen Sie die ausführliche Anleitung von Segmente zum Hinzufügen der Braze Zielabhängigkeit zu Ihrer [Android](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/) App.

Der Code für die Integration in [den Android-Gerätemodus](https://github.com/braze-inc/braze-segment-kotlin) wird von Braze gepflegt und regelmäßig aktualisiert, um neue Braze SDK-Versionen zu berücksichtigen.

{% endtab %}
{% tab iOS %}

{% alert important %}
Der Code für die Integration des iOS-Gerätemodus wird von Braze gepflegt und regelmäßig aktualisiert, um neue SDK-Versionen von Braze zu berücksichtigen.

<br>
Welches Braze SDK Sie verwenden, hängt davon ab, welches Segment SDK Sie verwenden:

| Segmente | Segment SDK | Braze SDK | Segmentierung
| - | ----------- | --------- |
| Bevorzugt | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze Segment Swift](https://github.com/braze-inc/braze-segment-swift) |
| Legacy | [Analytics-iOS](https://github.com/segmentio/analytics-ios) | [Braze Segment iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endalert %}

Um Braze als Ziel im Gerätemodus für Ihre iOS-Quelle einzurichten, wählen Sie **Aktionen** als **Ziel-Framework** und dann **Speichern**. 

Um die Side-by-side-Integration zu vervollständigen, lesen Sie die ausführliche Anleitung von Segmente zum Hinzufügen des Braze Segment Pods zu Ihrer [iOS](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/) App.

Der Code für die Integration [des iOS-Gerätemodus](https://github.com/braze-inc/braze-segment-swift) wird von Braze gepflegt und regelmäßig aktualisiert, um neue SDK-Versionen von Braze zu berücksichtigen.

{% endtab %}
{% tab Internet oder JavaScript %}

Das Braze Web Mode (Actions) Framework von Segmente wird empfohlen, um Braze als Ziel für den Internet-Gerätemodus einzurichten. 

Wählen Sie in Segmente **Aktionen** als Zielrahmen und **Gerätemodus** als Verbindungsmodus aus.

![]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
Der Code für das [React Native Braze Plugin](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze) wird von Segment gepflegt und regelmäßig aktualisiert, um neue Braze SDK-Versionen zu berücksichtigen.

Wenn Sie eine React Native Segmente-Quelle mit Braze verbinden, müssen Sie eine Quelle und ein Ziel pro Betriebssystem einrichten. Zum Beispiel die Einrichtung eines iOS-Ziels und eines Android-Ziels. 

Innerhalb Ihrer App-Codebasis initialisieren Sie das Segment SDK bedingt nach Gerätetyp, indem Sie den jeweiligen, mit jeder App verbundenen Quellcode-Schreibschlüssel verwenden.

Wenn ein Push-Token von einem Gerät registriert und an Braze gesendet wird, wird er mit dem Bezeichner der App verknüpft, der bei der Initialisierung des SDK verwendet wurde. Die gerätetypabhängige Initialisierung stellt sicher, dass alle an Braze gesendeten Push-Token mit der entsprechenden App verknüpft sind.

{% alert important %}
Wenn die React Native App Braze mit demselben Braze App-Bezeichner für alle Geräte initialisiert, dann werden alle React Native Nutzer:innen in Braze als Android- oder iOS-Nutzer:innen betrachtet und alle Push-Token werden mit diesem Betriebssystem assoziiert.
{% endalert %}

Um Braze als Ziel im Gerätemodus für jede Quelle einzurichten, wählen Sie **Aktionen** als **Zielrahmen** und dann **Speichern**.

{% endtab %}
{% endtabs %}

#### Server-zu-Server-Integration

Diese auch als Cloud-Modus bezeichnete Integration leitet Daten von Segmenten an die REST APIs von Braze weiter. Verwenden Sie das [Braze Cloud Mode (Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) Framework von Segmente, um ein Cloud-Modus-Ziel für jede Ihrer Quellen einzurichten. 

Im Gegensatz zur Side-by-side-Integration unterstützt die Server-zu-Server-Integration keine Features der Braze UI, wie z.B. In-App-Nachrichten, Content-Cards oder die automatische Registrierung von Push-Token. Es gibt auch [automatisch erfasste]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection) Daten (wie anonyme Nutzer:innen und Felder auf Geräteebene), die nicht über den Cloud-Modus verfügbar sind.

Wenn Sie diese Daten und Features nutzen möchten, sollten Sie die Side-by-side-Integration (Gerätemodus) des SDK verwenden.

Der Quellcode für das [Ziel Braze Cloud Mode (Actions)](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze) wird von Segmente verwaltet.

### Schritt 3: Einstellungen

Definieren Sie die Einstellungen für Ihr Ziel. Nicht alle Einstellungen gelten für alle Zieltypen.

{% tabs local %}
{% tab Mobiler Geräte-Modus %}

| Einstellung | Beschreibung |
| ------- | ----------- |
| Bezeichner der App | Der Bezeichner der App, der verwendet wird, um die spezifische App zu referenzieren. Diese finden Sie im Braze-Dashboard unter **Einstellungen verwalten** | 
| Angepasster API Endpunkt<br>(SDK-Endpunkt) | Ihr Braze SDK-Endpunkt, der Ihrer Instanz entspricht (z.B. `sdk.iad-01.braze.com`) | 
| Endpunkt Region | Ihre Braze-Instanz (z.B. US 01, US 02, EU 01, etc.) | 
| Enablement der automatischen Registrierung von In-App-Nachrichten | Deaktivieren Sie dies, wenn Sie In-App-Nachrichten manuell registrieren möchten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Internet-Geräte-Modus %}

| Einstellung | Beschreibung |
| ------- | ----------- |
| Bezeichner der App | Der Bezeichner der App, der verwendet wird, um die spezifische App zu referenzieren. Diese finden Sie im Braze-Dashboard unter **Einstellungen verwalten** | 
| Angepasster API Endpunkt<br>(SDK-Endpunkt) | Ihr Braze SDK-Endpunkt, der Ihrer Instanz entspricht (z.B. `sdk.iad-01.braze.com`) | 
| Safari Website Push ID | Wenn Sie Safari Push unterstützen, müssen Sie diese Option mit der Website Push ID angeben, die Sie Apple bei der Erstellung Ihres Safari Push-Zertifikats mitgeteilt haben (beginnt mit `web`, zum Beispiel `web.com.example.domain`). |
| Braze Web SDK Version | Die Version des Braze Web SDK, die Sie verwenden möchten |
| Automatisches Senden von In-App-Nachrichten | Standardmäßig werden alle In-App-Nachrichten, für die ein Nutzer:innen berechtigt ist, automatisch dem Nutzer zugestellt. Deaktivieren Sie dies, wenn Sie In-App-Nachrichten manuell anzeigen möchten. |
| Laden Sie nicht die Schriftart awesome | Braze verwendet Font Awesome für In-App-Nachrichten-Symbole. Standardmäßig lädt Braze FontAwesome automatisch aus dem FontAwesome CDN. Um dieses Verhalten zu deaktivieren (z. B. weil Ihre Website eine angepasste Version von FontAwesome verwendet), setzen Sie diese Option auf `TRUE`. Beachten Sie, dass Sie in diesem Fall dafür verantwortlich sind, dass FontAwesome auf Ihrer Website geladen ist - andernfalls werden In-App-Nachrichten möglicherweise nicht korrekt dargestellt. |
| Enablement von In-App-Nachrichten im HTML-Format | Wenn Sie diese Option aktivieren, ist es Nutzern:innen des Braze-Dashboards erlaubt, In-App-Nachrichten im HTML-Format zu verwenden. | 
| In-App-Nachrichten in einem neuen Tab öffnen | Standardmäßig werden Links von In-App-Nachricht-Klicks im aktuellen Tab oder in einem neuen Tab geladen, wie im Dashboard für jede Nachricht angegeben. Setzen Sie diese Option auf `TRUE`, um zu erzwingen, dass alle Links von Klicks auf In-App-Nachrichten in einem neuen Tab oder Fenster geöffnet werden. |
| In-App-Nachricht z index | Geben Sie einen Wert für diese Option an, um die Standard-Z-Indizes von Braze außer Kraft zu setzen. | 
| Explizite Ablehnung von In-App-Nachrichten verlangen | Standardmäßig wird eine In-App-Nachricht durch Drücken des Escape-Buttons oder durch einen Klick auf den ausgegrauten Hintergrund der Seite verworfen, wenn sie angezeigt wird. Setzen Sie diese Option auf true, um dieses Verhalten zu verhindern und einen expliziten Klick auf einen Button zu verlangen, um Nachrichten zu schließen. |
| Mindestabstand zwischen triggernden Aktionen in Sekunden | Der Standardwert ist 30.<br>Standardmäßig wird eine triggernde Aktion nur ausgelöst, wenn seit der letzten triggernden Aktion mindestens 30 Sekunden vergangen sind. Geben Sie einen Wert für diese Konfigurationsoption an, um diesen Standard mit einem eigenen Wert zu überschreiben. Wir empfehlen, diesen Wert nicht kleiner als 10 zu wählen, um den Nutzer:innen nicht mit Benachrichtigungen zu überhäufen.|
| Standort der Service-Teammitglieder | Standardmäßig sucht Braze bei der Registrierung von Nutzern:innen für Web-Push-Benachrichtigungen nach der erforderlichen Service-Teammitglied-Datei im Stammverzeichnis Ihres Servers unter `/service-worker.js`. Wenn Sie Ihr Service-Teammitglied unter einem anderen Pfad auf diesem Server hosten möchten, geben Sie für diese Option einen Wert an, der dem absoluten Pfad zu der Datei entspricht. (zum Beispiel: `/mycustompath/my-worker.js`). Beachten Sie, dass die Festlegung eines Wertes hier den Umfang der Push-Benachrichtigungen auf Ihrer Website einschränkt. In der obigen Instanz zum Beispiel kann `requestPushPermission`, da sich die Datei des Service-Teammitglieds im Verzeichnis `/mycustompath/` befindet, nur von Webseiten aufgerufen werden, die mit `http://yoursite.com/mycustompath/` beginnen. |
| Push-Token Wartung deaktivieren | Standardmäßig werden Nutzer:innen, die bereits eine Web-Push-Erlaubnis erteilt haben, ihr Push-Token bei neuen Sitzungen automatisch mit dem Braze Backend synchronisieren, um die Zustellbarkeit zu gewährleisten. Um dieses Verhalten zu deaktivieren, setzen Sie diese Option auf `FALSE`. |
| Externes Service-Teammitglied verwalten | Wenn Sie Ihr eigenes Service-Teammitglied haben, das Sie registrieren und dessen Lebenszyklus Sie kontrollieren, setzen Sie diese Option auf `TRUE`, und das Braze SDK wird kein Service-Teammitglied registrieren oder deregistrieren. Wenn Sie diese Option auf `TRUE` setzen, müssen Sie das Service-Teammitglied selbst registrieren, bevor Sie `requestPushPermission` aufrufen, und sicherstellen, dass es den Code des Braze Service-Teammitglieds enthält, entweder mit `self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');` oder indem Sie den Inhalt dieser Datei direkt einfügen. Wenn diese Option `TRUE` lautet, ist die Option `serviceWorkerLocation` irrelevant und wird ignoriert. |
| Content-Sicherheits-Nonce | Wenn Sie einen Wert für diese Option angeben, fügt das Braze SDK die Nonce zu allen vom SDK erstellten `<script>` und `<style>` Elementen hinzu. Dies ermöglicht es dem Braze SDK, mit der Richtlinie für die Sicherheit von Inhalten Ihrer Website zu arbeiten. Zusätzlich zur Einstellung dieser Nonce müssen Sie eventuell auch das Laden von FontAwesome zulassen. Dies können Sie tun, indem Sie `use.fontawesome.com` zur Zulässigkeitsliste Ihrer Richtlinie für die Inhaltssicherheit hinzufügen oder indem Sie die Option `doNotLoadFontAwesome` verwenden und FontAwesome manuell laden. |
| Crawler-Aktivität zulassen | Standardmäßig ignoriert das Braze Web SDK Aktivitäten von bekannten Spidern oder Web-Crawlern, wie z.B. Google, basierend auf dem Nutzer:in-String. Dies speichert Datenpunkte, macht Analytics genauer und kann das Page Rank verbessern. Wenn Sie jedoch möchten, dass Braze stattdessen die Aktivitäten dieser Crawler protokolliert, können Sie diese Option auf `TRUE` setzen. |
| Enablement der Protokollierung | Setzen Sie diese Option auf `TRUE`, um die Protokollierung standardmäßig zu aktivieren. Beachten Sie, dass Braze dadurch ein Protokoll in der JavaScript-Konsole erstellt, das für alle Nutzer:innen sichtbar ist. Bevor Sie Ihre Seite für die Produktion freigeben, sollten Sie diese entfernen oder einen alternativen Logger mit `setLogger` bereitstellen. |
| Nutzer:innen JavaScript zulassen | Standardmäßig lässt das Braze Web SDK keine vom Benutzer bereitgestellten JavaScript-Klick-Aktionen zu, da es Nutzern:innen des Braze-Dashboards erlaubt, JavaScript auf Ihrer Website auszuführen. Um anzugeben, dass Sie den Nutzer:innen des Braze-Dashboards zutrauen, nicht bösartige JavaScript-Klick-Aktionen zu schreiben, setzen Sie diese Eigenschaft auf `TRUE`. Wenn `enableHtmlInAppMessages` auf `TRUE` steht, wird diese Option auch auf `TRUE` gesetzt. |
| Version der App| Wenn Sie einen Wert für diese Option angeben, werden an Braze gesendete Nutzer:innen-Ereignisse mit der angegebenen Version assoziiert, die für die Segmentierung von Nutzern verwendet werden kann. |
| Zeitüberschreitung der Sitzung in Sekunden | Der Standardwert ist 30.<br>Standardmäßig werden Sitzungen nach 30 Minuten Inaktivität beendet. Geben Sie einen Wert für diese Konfigurationsoption an, um diesen Standard mit einem eigenen Wert zu überschreiben. | 
| Eigenschaft des Geräts allowlist | Standardmäßig erkennt und sammelt das Braze SDK automatisch alle Eigenschaften des Geräts in `DeviceProperties`. Um dieses Verhalten außer Kraft zu setzen, geben Sie ein Array von `DeviceProperties` an. Beachten Sie, dass ohne einige Eigenschaften nicht alle Features ordnungsgemäß funktionieren werden. Zum Beispiel funktioniert die Zustellung zur Ortszeit nicht ohne die Zeitzone. |
| Lokalisierung | Standardmäßig werden alle vom SDK erzeugten, für den Benutzer sichtbaren Nachrichten in der Browser-Sprache des Nutzers:in angezeigt. Geben Sie einen Wert für diese Option an, um dieses Verhalten außer Kraft zu setzen und eine bestimmte Sprache zu erzwingen. Der Wert für diese Option sollte ein ISO 639-1 Sprachcode sein. |
| Keine Cookies | Standardmäßig speichert das Braze SDK kleine Datenmengen (Nutzer:innen, Sitzungskennungen) in Cookies. Dies ist zulässig, damit Braze Nutzer:innen und Sitzungen über verschiedene Subdomänen Ihrer Website hinweg erkennen kann. Wenn dies für Sie ein Problem darstellt, geben Sie `TRUE` für diese Option ein, um die Speicherung von Cookies zu deaktivieren und sich vollständig auf HTML 5 localStorage zu verlassen, um Nutzer:innen und Sitzungen zu identifizieren. |
| Alle Seiten tracken | **Klassisches Ziel Internet Nur Geräte-Modus (Wartung)**<br><br>Segmente empfiehlt die Migration zum Ziel Internet Actions Framework, wo diese Einstellung [durch Abbildungen aktiviert](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping) werden kann.<br><br>Dadurch werden alle [Seitenaufrufe](https://segment.com/docs/spec/page/) an Braze als Ereignis "Seite geladen/angesehen" gesendet. |
| Nur benannte Seiten tracken | **Klassisches Ziel Internet Nur Geräte-Modus (Wartung)**<br><br>Segmente empfiehlt die Migration zum Ziel Internet Actions Framework, wo diese Einstellung [durch Abbildungen aktiviert](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping) werden kann.<br><br>Dadurch werden nur Seitenaufrufe an Braze gesendet, die mit einem Namen verknüpft sind. |
| Kauf protokollieren, wenn Einnahmen vorhanden sind | **Klassisches Ziel Internet Nur Geräte-Modus (Wartung)**<br><br>Segmente empfiehlt die Migration zum Ziel Internet Actions Framework, wo diese Einstellung [durch Abbildungen aktiviert](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping) werden kann.<br><br>Wenn diese Option aktiviert ist, triggern alle Tracking-Aufrufe mit der Eigenschaft Umsatz ein Kauf-Event. | 
| Nur bekannte Nutzer:innen tracken | **Klassisches Ziel Internet Nur Geräte-Modus (Wartung)**<br><br>Segmente empfiehlt die Migration auf das Ziel Internet Actions Framework, wo diese Einstellung durch Abbildungen aktiviert werden kann.<br><br>Falls aktiviert, verzögert diese neue Einstellung den Aufruf von `window.appboy.initialize`, bis eine gültige `userId` vorliegt. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Cloud-Modus %}

| Einstellung | Beschreibung |
| ------- | ----------- |
| Bezeichner der App | Der Bezeichner der App, der verwendet wird, um die spezifische App zu referenzieren. Diese finden Sie im Braze-Dashboard unter **Einstellungen verwalten** | 
| REST-API-Schlüssel | Diese finden Sie in Ihrem Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. | 
| Angepasster REST API Endpunkt | Ihr Braze REST Endpunkt, der Ihrer Instanz entspricht (z.B. rest.iad-01.braze.com). | 
| Nur vorhandene Nutzer:innen aktualisieren | **Nur klassische Ziele im Cloud-Modus (Wartung)**<br><br>Segmente empfiehlt die Migration auf das Ziel Cloud Actions Framework, wo diese Einstellung [durch Abbildungen aktiviert](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping) werden kann.<br><br>Legt fest, ob nur bestehende Nutzer:innen aktualisiert werden sollen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Schritt 4: Methoden zur Abbildung {#methods}

Braze unterstützt die Methoden [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page), [Identify](https://segment.com/docs/spec/identify/) und [Tracking](https://segment.com/docs/spec/track/) Segmente. Welche Arten von Bezeichnern bei diesen Methoden verwendet werden, hängt davon ab, ob die Daten über eine Server-zu-Server-Integration (Cloud-Modus) oder eine Side-by-side-Integration (Geräte-Modus) gesendet werden. In den Zielen Braze Web Mode Actions und Cloud Mode Actions können Sie auch eine Abbildung für einen [Segment-Alias-Anruf](https://segment.com/docs/connections/spec/alias/) einrichten. 

{% alert note %}
Obwohl Nutzer-Alias als Bezeichner im Ziel Braze Cloud Mode (Actions) unterstützt werden, ist zu beachten, dass der Alias-Aufruf von Segmente nicht direkt mit Nutzer-Alias von Braze zusammenhängt.
{% endalert %}

| Bezeichner Typ | Unterstütztes Ziel |
| --------------- | --------------------- |
| `userId` (`external_id`) | Alle |
| Anonyme Nutzer:innen | Ziele im Gerätemodus |
| Nutzer:in alias | Ziele im Cloud-Modus |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Das Ziel Cloud-Modus (Aktionen) bietet eine [Aktion Alias erstellen](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias), mit der Sie einen reinen Alias-Nutzer:in erstellen oder einen Alias zu einem bestehenden Profil `external_id` hinzufügen können. Die [Aktion Nutzer:innen identifizieren](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user) kann zusammen mit der Aktion Bezeichner erstellen verwendet werden, um einen Nutzer:innen, der nur einen Bezeichner hat, mit einer `external_id` zusammenzuführen, nachdem ein Bezeichner für den Nutzer:innen verfügbar geworden ist. 

Es ist auch möglich, eine Umgehung zu entwickeln und `braze_id` zu verwenden, um anonyme Nutzer:in-Daten im Cloud-Modus zu senden. Dies erfordert die manuelle Aufnahme der Nutzer:innen `braze_id` in alle Ihre Segment API-Aufrufe. In der [Dokumentation von Segmente](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users) erfahren Sie mehr darüber, wie Sie diese Umgehung einrichten können.

An Braze gesendete Ziele Daten können im Rahmen von Cloud-Modus-Aktionen gebündelt werden. Die Chargengröße ist auf 75 Ereignisse begrenzt, und diese Chargen sammeln sich über einen Zeitraum von 30 Sekunden an, bevor sie gespült werden. Das Stapeln von Anfragen erfolgt pro Aktion. Zum Beispiel werden Identify Calls (Attribute) in einer Anfrage und Tracking Calls (angepasste Events) in einer zweiten Anfrage zusammengefasst. Braze empfiehlt, dieses Feature zu aktivieren, da es die Anzahl der Anfragen reduziert, die von Segmenten an Braze gesendet werden. Dadurch verringert sich das Risiko, dass das Ziel auf die Rate-Limits von Braze stößt und Anfragen wiederholt werden müssen. 

Sie können die Stapelverarbeitung für eine Aktion aktivieren, indem Sie zu Ihrem Braze Ziel > **Abbildungen** navigieren. Klicken Sie dort auf das 3-Punkte-Symbol rechts neben der Abbildung und wählen Sie **Abbildung bearbeiten**. Blättern Sie zum Ende des Abschnitts **Abbildungen auswählen** und vergewissern Sie sich, dass die Option **Daten zu Braze stapeln** auf **Ja** gesetzt ist.


{% tabs local %}
{% tab Identifizieren %}
#### Identifizieren

Mit dem Aufruf [Identify](https://segment.com/docs/spec/identify/) können Sie einen Nutzer:innen mit seinen Aktionen verknüpfen und Attribute über ihn aufzeichnen. 

Bestimmte Segmente haben spezielle Eigenschaften, die den Standard-Attribut-Profilen in Braze zugeordnet sind:

| Besondere Merkmale der Segmente | Braze Standard Attribute |
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

Andere reservierte Braze Profilfelder wie `email_subscribe` und `push_subscribe` können gesendet werden, indem Sie die Braze-Namenskonvention für diese Felder verwenden und sie als Eigenschaften innerhalb eines Identify-Aufrufs übergeben.

##### Hinzufügen eines Nutzers:innen zu einer Abo-Gruppe

Sie können einen Nutzer:in einer bestimmten Abo-Gruppe auch mit Hilfe der folgenden Felder in den Traits-Parametern abonnieren oder abmelden.

Verwenden Sie das reservierte Braze-Profilfeld namens `braze_subscription_groups`, das mit einem Array von Objekten verknüpft werden kann. Jedes Objekt im Array sollte zwei reservierte Schlüssel haben:

1. `subscription_group_state`: Zeigt an, ob der Nutzer:in `"subscribed"` oder `"unsubscribed"` zu einer bestimmten Abo-Gruppe gehört.
2. `subscription_group_id`: Stellt die eindeutige ID der Abo-Gruppe dar. Sie finden diese ID im Braze-Dashboard unter **Abo-Gruppen-Management**.

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

Alle anderen Eigenschaften werden als [angepasste Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) aufgezeichnet.

| Segmente Methode | Braze Methode | Beispiel |
|---|---|---|
| Identifizieren Sie sich mit der Nutzer:in ID | Externe ID einstellen | Segmente:  `analytics.identify("dawei");`<br>Braze: `Braze.changeUser("dawei")` |
| Identifizieren Sie mit reservierten Merkmalen | Nutzer:in-Attribute festlegen | Segment: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `Braze.getUser().setEmail("dawei@braze.com");`
| Mit angepassten Bezeichnern identifizieren | Angepasste Attribute festlegen | Segment: `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze: `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| Identifizieren Sie sich mit Nutzer:innen ID und Merkmalen | Segmente: Externe ID und Attribut festlegen | Kombinieren Sie die vorangegangenen Methoden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

In den Zielen [Internet-Modus-Aktionen](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) und [Cloud-Modus-Aktionen](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile) können die oben genannten Abbildungen mit der Aktion Nutzerprofil aktualisieren eingestellt werden.

{% alert important %}
Stellen Sie bei der Übergabe von Nutzer:innen-Attributen sicher, dass Sie nur Werte für Attribute übergeben, die sich seit dem letzten Update geändert haben. So stellen Sie sicher, dass Sie nicht unnötigerweise Datenpunkte für Ihr Kontingent verbrauchen. Für Client-seitige Quellen verwenden Sie das [Open-Source-Middleware-Tool](https://github.com/segmentio/segment-braze-mobile-middleware) von Segment, um Ihre Integration zu optimieren und die Datenpunkt-Nutzung zu begrenzen, indem Sie doppelte `identify()` Aufrufe von Segment entprellen. 

{% endalert %}
{% endtab %}

{% tab Tracking %}
#### Tracking

Wenn Sie ein Ereignis tracken, erfassen wir dieses Ereignis als [angepasstes Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) unter dem angegebenen Namen. 

Metadaten, die innerhalb des Eigenschaften-Objekts des Tracking-Aufrufs gesendet werden, werden in Braze als angepasste Event-Eigenschaften für das zugehörige Event protokolliert. Es werden alle [Datentypen für angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) unterstützt.

In den Zielen [Internet Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) und [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event) können die oben genannten Abbildungen mit der Aktion Tracking Event eingestellt werden.

| Segmente Methode | Braze Methode | Beispiel |
|---|---|---|
| [Tracking](https://segment.com/docs/spec/track/) | Als [angepasstes Event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) protokolliert. | Segment: `analytics.track("played_game");` <br>Braze: `Braze.logCustomEvent("played_game");`|
| [Tracking mit Eigenschaften](https://segment.com/docs/spec/track/) | Als [Event-Eigenschaft]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) protokolliert. | Segment: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze: `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Tracking mit Produkt](https://segment.com/docs/spec/track/) | Als [Kauf-Event]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web) protokolliert. | Segment: `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Braze: `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

##### Bestellung abgeschlossen {#order-completed}

Wenn Sie ein Tracking-Ereignis mit dem Namen `Order Completed` unter Verwendung des in der [E-Commerce API](https://segment.com/docs/spec/ecommerce/v2/) von Segmente beschriebenen Formats durchführen, erfassen wir die Produkte, die Sie als [Käufe]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) aufgeführt haben.

Bei den Zielen [Internet Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) und [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase) kann die Standard Abbildung über die Tracking Purchase Action angepasst werden.

{% endtab %}

{% tab Seite %}
#### Seite {#page}

Mit dem [Seitenaufruf](https://segment.com/docs/spec/page/) können Sie aufzeichnen, wann immer ein Nutzer:innen eine Seite Ihrer Website sieht, zusammen mit allen optionalen Eigenschaften der Seite.

Dieser Ereignistyp kann als Trigger in den Zielen Internet Mode Actions und Cloud Actions verwendet werden, um ein angepasstes Event in Braze zu protokollieren.
{% endtab %}

{% endtabs %}

### Schritt 5: Testen Sie Ihre Integration

Wenn Sie die Side-by-Side-Integration (im Gerätemodus) verwenden, können Ihre [Übersichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/) (Lifetime-Sitzungen, MAU, DAU, Stickiness, tägliche Sitzungen und tägliche Sitzungen pro MAU) verwendet werden, um sicherzustellen, dass Braze Daten von Segmente erhält.

Sie können Ihre Daten auf den Seiten für [angepasste Events]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data/#custom-event-data) oder [Einnahmen]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) einsehen oder [ein Segment erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment). Auf der Seite **Angepasste Events** des Dashboards können Sie die Anzahl der angepassten Events im Zeitverlauf anzeigen. Beachten Sie, dass Sie keine [Formeln]({{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula/#creating-a-formula) verwenden können, die MAU- und DAU-Statistiken enthalten, wenn Sie eine Server-zu-Server-Integration (Cloud-Modus) verwenden.

Wenn Sie Kaufdaten an Braze senden (siehe Bestellung abgeschlossen auf dem Tab **Tracking** in [Schritt 3](#methods)), können Sie auf der Seite mit den [Einnahmen]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) Daten zu den Einnahmen oder Käufen in bestimmten Zeiträumen oder die Gesamteinnahmen Ihrer App einsehen.

[Wenn Sie ein Segment erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment), können Sie Ihre Nutzer:in auf der Grundlage der angepassten Event- und Attribut-Daten filtern.

{% alert important %}
Wenn Sie eine Server-zu-Server-Integration (Cloud-Modus) verwenden, funktionieren Filter, die sich auf automatisch gesammelte Sitzungsdaten beziehen (z. B. "zuerst verwendete App" und "zuletzt verwendete App"), nicht. Verwenden Sie eine Side-by-side-Integration (Geräte-Modus), wenn Sie diese in Ihrer Segmentierung und Braze-Integration verwenden möchten.
{% endalert %}

## Nutzer:in löschen und unterdrücken 

Wenn Sie Nutzer:innen löschen oder unterdrücken müssen, beachten Sie bitte Folgendes: Das [Feature zum Löschen von Nutzern:innen](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) von Segmente **wird** auf den Braze[`/users/delete` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) abgebildet. Beachten Sie, dass die Überprüfung dieser Löschungen bis zu 30 Tage dauern kann.

Sie müssen sicherstellen, dass Sie einen gemeinsamen Bezeichner für Nutzer:innen von Braze und Segmenten auswählen (wie in `external_id`). Nachdem Sie eine Anfrage zur Löschung mit Segment initiiert haben, können Sie den Status auf dem Tab Löschanfragen in Ihrem Segment Dashboard einsehen.

## Segmente wiedergeben

Segmente bietet einen Dienst für Clients an, um alle historischen Daten an einen neuen Partner weiterzugeben. Neue Braze-Kunden, die alle relevanten historischen Daten importieren möchten, können dies über Segmente tun. Sprechen Sie mit Ihrem Segment-Vertreter, wenn Sie daran interessiert sind.

Segment stellt eine Verbindung zu unserem [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) her, um Nutzerdaten in Ihrem Namen in Braze zu importieren.

{% alert important %}
Alle Bezeichner, die im Ziel Cloud Mode Actions unterstützt werden, werden als Teil von Segmentierungen unterstützt.
{% endalert %}

## Bewährte Praktiken

{% details Überprüfen Sie Anwendungsfälle, um Mehrkosten bei den Daten zu vermeiden. %}

Segmente schränken die Anzahl der Daten, die Clients an sie senden, **nicht** ein. Segmente ermöglichen es Ihnen, alle Ereignisse zu senden oder zu entscheiden, welche Ereignisse Sie an Braze senden. Anstatt alle Ihre Ereignisse über Segmente zu senden, empfehlen wir Ihnen, mit Ihren Marketing- und Redaktionsteams Anwendungsfälle zu besprechen, um festzulegen, welche Ereignisse Sie an Braze senden, um Mehrkosten bei den Daten zu vermeiden.

{% enddetails %}

{% details Verstehen Sie den Unterschied zwischen dem angepassten API-Endpunkt und dem angepassten REST API-Endpunkt in den Zieleinstellungen des Mobilgerätemodus. %}

| Braze Terminologie | Segmente äquivalent |
| ----------------- | ------------------ |
| Braze SDK-Endpunkt | Angepasster API Endpunkt |
| Braze REST Endpunkt | Angepasster REST API Endpunkt |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ihr Braze API-Endpunkt (in Segmente als "Custom API Endpoint" bezeichnet) ist der SDK-Endpunkt, den Braze für Ihr SDK einrichtet (zum Beispiel `sdk.iad-03.braze.com`). Ihr Braze REST API Endpunkt (in Segmente als "Custom REST API Endpoint" bezeichnet) ist der REST API Endpunkt (zum Beispiel `https://rest.iad-03.braze.com`)
{% enddetails %}

{% details Stellen Sie sicher, dass Ihr angepasster API Endpunkt korrekt in die Zieleinstellungen für den Modus des mobilen Geräts eingegeben wird. %}

| Braze Terminologie | Segmente äquivalent |
| ----------------- | ------------------ |
| Braze SDK-Endpunkt | Angepasster API Endpunkt |
| Braze REST Endpunkt | Angepasster REST API Endpunkt |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Um sicherzustellen, dass Sie Ihren Braze SDK-Endpunkt korrekt eingeben, müssen Sie das richtige Format einhalten. Ihr SDK-Endpunkt von Braze darf nicht `https://` (z.B. `sdk.iad-03.braze.com`) enthalten, da sonst die Integration von Braze fehlschlägt. Dies ist erforderlich, da Segmente Ihrem Endpunkt automatisch `https://` voranstellt, was dazu führt, dass Braze mit einem ungültigen Endpunkt `https://https://sdk.iad-03.braze.com` initialisiert wird.

{% enddetails %}

{% details Nuancen bei der Abbildung von Daten. %}

Szenarien, in denen die Daten nicht wie erwartet weitergeleitet werden:

1. Verschachtelte angepasste Attribute
  - Obwohl [verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/) technisch über Segmente an Braze gesendet werden können, wird jedes Mal die **gesamte Nutzlast** gesendet. Dadurch entstehen jedes Mal, wenn die Nutzdaten gesendet werden, [Datenpunkte]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#data-points) pro im verschachtelten Objekt übergebenen Schlüssel.<br><br> Um nur eine Teilmenge der Datenpunkte beim Senden der Nutzlast auszugeben, können Sie das Feature der angepassten [Zielfunktionen](https://segment.com/docs/connections/functions/destination-functions/) von Segment verwenden. Dieses Feature in der Segmente-Plattform erlaubt es Ihnen, die Art und Weise, wie Daten an nachgelagerte Ziele gesendet werden, anzupassen.

  {% alert note %}
  Die Funktionen für angepasste Ziele werden innerhalb von Segmenten gesteuert, und Braze hat nur begrenzten Insight in Funktionen, die extern konfiguriert wurden.
  {% endalert %}

{: start="2"}
2\. Weitergabe anonymer Daten von Server zu Server.
  - Kunden können die Server-zu-Server Bibliotheken von Segmente nutzen, um anonyme Daten in andere Systeme zu funken. Lesen Sie den Abschnitt Abbildungsmethoden, um mehr darüber zu erfahren, wie Sie Nutzer:innen ohne `external_id` über eine Server-zu-Server-Integration (Cloud-Modus) an Braze senden können.

{% enddetails %}

{% details Anpassung der Initialisierung von Braze. %}

Es gibt verschiedene Möglichkeiten, Braze anzupassen: Push, In-App-Nachrichten, Content-Cards und Initialisierung. Bei einer Side-by-side-Integration können Sie Push, In-App-Nachrichten und Content-Cards wie bei einer direkten Braze-Integration anpassen.

Die Anpassung der Integration des Braze SDK oder die Festlegung von Initialisierungskonfigurationen kann jedoch schwierig und manchmal nicht möglich sein. Das liegt daran, dass Segment das Braze SDK für Sie initialisiert, wenn die Segmentierung erfolgt.

{% enddetails %}

{% details Deltas an Braze senden. %}

Stellen Sie bei der Übergabe von Nutzer:innen-Attributen sicher, dass Sie nur Werte für Attribute übergeben, die sich seit dem letzten Update geändert haben. So stellen Sie sicher, dass Sie nicht unnötigerweise Datenpunkte für Ihr Kontingent verbrauchen. Für Client-seitige Quellen verwenden Sie das [Open-Source-Middleware-Tool](https://github.com/segmentio/segment-braze-mobile-middleware) von Segment, um Ihre Integration zu optimieren und die Datenpunkt-Nutzung einzuschränken, indem Sie doppelte `identify()` Aufrufe von Segment entprellen. 

{% enddetails %}


