---
nav_title: Tealium
article_title: Tealium
page_order: 1
alias: /partners/tealium/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Tealium, einer universellen Datendrehscheibe, die es Ihnen ermöglicht, mobile, Internet- und alternative Daten mit anderen Drittanbieter-Datenquellen zu verbinden."
page_type: partner
search_tag: Partner

---

# Tealium

> [Tealium](https://tealium.com/) ist eine universelle Datendrehscheibe und Kundendaten-Plattform, bestehend aus EventStream, AudienceStream und iQ Tag Management, die es Ihnen ermöglicht, Mobil-, Web- und alternative Daten aus Drittanbieter-Quellen zu verbinden. Die Verbindung von Tealium mit Braze ermöglicht einen Datenfluss von angepassten Events, Nutzer-Attributen und Käufen, die Sie in die Lage versetzen, Ihre Daten in Realtime zu nutzen.

![Eine Übersichtsgrafik von Tealium, die zeigt, wie die verschiedenen Produkte von Tealium und die Braze-Plattform zusammenpassen, um kanalübergreifende Kampagnen in Realtime zu aktivieren.]({% image_buster /assets/img/tealium/tealium_overview.png %}){: style="border:0;"}

Die Integration von Braze und Tealium erlaubt es Ihnen, Ihre Nutzer:innen zu tracken und Daten an verschiedene Anbieter von Analytics weiterzuleiten. Tealium lässt Sie zu:
- Synchronisieren Sie Zielgruppen von Tealium mit [AudienceStream]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream/) mit Braze, um Kampagnen und Canvase von Braze zu personalisieren oder Segmente zu erstellen.
- [Importieren Sie Daten plattformübergreifend](#choose-your-integration-type). Braze bietet sowohl eine [Side-by-side-SDK-Integration](#side-by-side-sdk-integration) für Ihre Android-, iOS- und Internet-Anwendungen als auch eine [Server-zu-Server-Integration](#server-to-server-integration), die innerhalb jeder Plattform verwendet werden kann, die Ereignisdaten melden kann.<br><br>

{% tabs %}
{% tab EventStream %}
Tealium EventStream ist eine Datenerfassung und API-Drehscheibe, die im Zentrum Ihrer Daten steht. EventStream wickelt die gesamte Datenlieferkette ab, von der Einrichtung und Installation bis hin zur Identifizierung, Validierung und Verbesserung der eingehenden Nutzer:innen-Daten. EventStream arbeitet in Realtime mit Ereignis-Feeds und Konnektoren. Im Folgenden finden Sie die Features, aus denen der [EventStream](https://docs.tealium.com/server-side/getting-started/eventstream-api-hub/introduction/) besteht.
- Datenquellen (Installation und Datenerfassung)
- Live-Ereignisse (Prüfung von Echtzeitdaten)
- Ereignisspezifikationen und Attribute (Anforderungen an die Datenebene und Validierung)
- Ereignis-Feeds (gefilterte Ereignistypen)
- Konnektoren für Ereignisse (API-Hub-Aktionen)

{% endtab %}
{% tab AudienceStream %}

Tealium AudienceStream ist eine Omnichannel-Kund:in-Segmentierung und Realtime Action Engine. AudienceStream nimmt die Daten, die in EventStream einfließen, und erstellt Besucherprofile, die die wichtigsten Attribute des Engagements Ihrer Kund:innen mit Ihrer Marke darstellen. Weitere Informationen zur Einrichtung finden Sie in unserem [AudienceStream-Artikel]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_audience_stream/).

{% endtab %}
{% tab iQ Tag Management %}
Tealium iQ erlaubt es Ihnen, Code in Ihren Apps über ein Tag in der Tealium iQ Tag Management UI zu triggern. Dieser Tag sammelt, kontrolliert und liefert Ereignisdaten von Mobil- und Internetplattformen und erlaubt es Ihnen, eine native Braze-Implementierung zu konfigurieren, ohne Braze-spezifischen Code zu Ihren Apps hinzuzufügen. Nutzer:innen können Mobile Remote Commands über iQ Tag Management oder JSON-Konfigurationsdateien integrieren (empfohlener Ansatz von Tealium). Nutzer:innen, die das Braze Web SDK verwenden, müssen die Integration über den web iQ Tag vornehmen.

Wenn Sie mehr über die Vor- und Nachteile der einzelnen Methoden erfahren möchten, lesen Sie den folgenden Abschnitt [Tealium iQ Tag Manager:in](#mobile-remote-commands).
{% endtab %}
{% endtabs %}

{% alert important %}
Tealium bietet sowohl Batch- als auch Non-Batch-Konnektor-Aktionen an. Der Konnektor ohne Stapelverarbeitung sollte verwendet werden, wenn Anfragen in Realtime für den Anwendungsfall wichtig sind und keine Bedenken bestehen, dass die Spezifikationen für die Rate-Limits der Braze APIs überschritten werden. Kontaktieren Sie den Braze Support oder Ihren Customer-Success-Manager:in, wenn Sie Fragen haben.<br><br>

Bei Konnektoren mit Stapelverarbeitung werden Anfragen in eine Warteschlange gestellt, bis einer der folgenden Schwellenwerte erreicht ist:<br><br>
- Maximale Anzahl von Anfragen: 75
- Maximale Zeit seit der ältesten Anfrage: 10 Minuten
- Maximale Größe der Anfragen: 1 MB

Tealium bündelt standardmäßig keine Zustimmungsereignisse (Abo-Einstellungen) oder Nutzer:innen-Löschungsereignisse.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Tealium Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Tealium-Konto](https://my.tealiumiq.com/) mit Server- und/oder Client-seitigem Zugriff. | 
| Installierter Quellcode und Tealium Quellcode [Bibliotheken](https://docs.tealium.com/platforms/) | Die Herkunft der Daten, die an Tealium gesendet werden, z.B. von mobilen Apps, Websites oder Backend-Servern.<br><br>Sie müssen die Bibliotheken in Ihrer App, Ihrer Website oder Ihrem Server installieren, bevor Sie einen erfolgreichen Tealium Konnektor einrichten können. |
| Braze REST und SDK-Endpunkt | Ihre REST- oder SDK-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
| Bezeichner der Braze App (nur bei Side-by-Side) | Ihr Bezeichner für die App. <br><br>Diese finden Sie im **Braze Dashboard > Einstellungen verwalten > API-Schlüssel**. |
| Code-Version (nur Seite an Seite) | Entspricht der SDK-Version und sollte im Format major.minor angegeben werden (zum Beispiel 3.2 und nicht 3.0.1). Die Code-Version sollte 3.0 oder höher sein. |
| REST API-Schlüssel (nur von Server zu Server) | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track` und `users.delete`. <br><br>Dieser kann über **Braze-Dashboard > Entwicklungskonsole > REST-API-Schlüssel > Neuen API-Schlüssel erstellen** erstellt werden.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Wählen Sie Ihren Integrationstyp

| Integration | Details |
| ----------- | ------- |
| [Seite an Seite](#side-by-side-sdk-integration) | Verwendet das SDK von Tealium, um Ereignisse in die nativen Aufrufe von Braze zu übersetzen, was den Zugriff auf tiefere Features und eine umfassendere Nutzung von Braze zulässt als die Server-zu-Server Integration.<br><br>Wenn Sie Braze-Fernbefehle verwenden möchten, beachten Sie, dass Tealium nicht alle Braze-Methoden (z.B. Content-Cards) unterstützt. Um eine Braze-Methode zu verwenden, die nicht durch einen entsprechenden Remote-Befehl abgebildet wird, müssen Sie die Methode durch Hinzufügen von nativem Braze-Code zu Ihrer Codebasis aufrufen.|
| [Server-zu-Server](#server-to-server-integration) | Leitet Daten von Tealium an die REST API Endpunkte von Braze weiter.<br><br>Unterstützt keine Braze UI Features wie In-App-Nachrichten, Content-Cards oder Push-Benachrichtigungen. Es gibt auch automatisch erfasste Daten, wie z.B. Felder auf Geräteebene, die mit dieser Methode nicht verfügbar sind.<br><br>Ziehen Sie eine Side-by-side-Integration in Betracht, wenn Sie diese Features nutzen möchten.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Side-by-side-Integration von SDKs

### Ferngesteuerte Befehle

Remote-Befehle sind ein Feature der Tealium iOS- und Android-Bibliotheken, das es Ihnen erlaubt, vom Tealium SDK - über die Braze Server - Braze aufzurufen. Das Braze-Fernbedienungsmodul installiert und erstellt automatisch die erforderlichen Bibliotheken von Braze und kümmert sich um die Darstellung von Nachrichten und das Analytics Tracking. Um Braze mobile remote command zu verwenden, müssen Sie Tealium Bibliotheken in Ihren Apps installieren.

Tealium bietet zwei Möglichkeiten zur Integration von Mobile Remote Command. Es gibt keinen Funktionsverlust zwischen den Integrationstypen, und der zugrunde liegende native Code ist identisch.

| Mobile Fernsteuerungsmethode | Profis | Nachteile |
| --- | --- | --- |
| **Tag der Fernsteuerung** | Ändern Sie die Abbildungen und Daten, die an den Fernbefehl gesendet werden, ganz einfach über die Tealium iQ UI.<br><br>Dies erlaubt es uns, zusätzliche Daten oder Ereignisse an ein SDK eines Drittanbieters zu senden, nachdem die App bereits im App Shop ist, ohne dass der Client die App aktualisieren muss. | Das Tag Management Modul in der App stützt sich auf eine ausgeblendete Webansicht, um JavaScript zu verarbeiten. |
| **JSON-Konfigurationsdatei**<br>[(Empfohlen](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#how-it-works)) | Die Verwendung der JSON-Methode macht eine ausgeblendete Webansicht in der App überflüssig und reduziert den Speicherverbrauch erheblich.<br><br>Die JSON-Datei kann per Fernzugriff oder lokal in der App der Kund:in gehostet werden. | Im Moment gibt es keine UI, um dies zu verwalten, so dass es ein wenig zusätzlichen Aufwand erfordert.<br><br>Hinweis: Tealium arbeitet an einem UI für die Verwaltung, das dieses Problem lösen und den JSON-Fernbefehlen das gleiche Maß an Flexibilität verleihen wird, das sie mit der iQ Tag-Verwaltungsversion haben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Verwenden Sie die Datenabbildungen von Braze mobile remote command, um Standard-Benutzerattribute und angepasste Attribute festzulegen und Käufe und angepasste Events zu verfolgen. Die entsprechenden Braze-Methoden finden Sie in dem folgenden Chart.

| Fernsteuerung | Braze Methode |
| -------------- | ------------ |
| appendcustomarrayattribute | addToCustomAttributeArrayWithKey()|
| E-Mail-Benachrichtigung | setEmailNotificationSubscriptionType() |
| incrementcustomattribute | incrementCustomAttribute() |
| Aktivieren Sie | startWithApiKey() |
| logcustomevent | logCustomEvent() |
| logpurchase | logKauf() |
| Pushnotifikation | setPushNotificationSubscriptionType() |
| removecustomattribute | setCustomAttributeWithKey() |
| setcustomattribute | setCustomAttributeArrayWithKey() |
| setcustomarrayattribute | setCustomAttributeArrayWithKey() |
| setlastknownlocation | setLastKnownLocationWithLatitude() |
| unsetcustomattribute | unsetCustomAttributeWithKey() |
| useralias | addAlias() |
| Benutzerattribut | ABKUser() |
| Benutzerkennung | changeUser() |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Einzelheiten zur Einrichtung der mobilen Fernsteuerung von Braze und eine Übersicht über die unterstützten Methoden finden Sie in der Dokumentation für Entwickler:in von Tealium:
- [Fernsteuerung](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#json-template)
- [Tag der Fernsteuerung](https://docs.tealium.com/client-side-tags/braze-mobile-remote-command-tag/)

{% alert important %}
Die mobilen Fernbefehle von Braze unterstützen nicht alle Braze-Methoden und Messaging-Kanäle (z.B. Content-Cards). Um eine Braze-Methode zu verwenden, die nicht durch einen entsprechenden Remote-Befehl abgebildet wird, müssen Sie die Methode direkt aufrufen, indem Sie Ihrer Codebasis nativen Braze-Code hinzufügen.
{% endalert%}

### Braze Web SDK Tag

Verwenden Sie den Braze Web SDK Tag, um das Braze Web SDK auf Ihrer Website einzusetzen. [Tealium iQ Tag Management](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) erlaubt es Kunden:in, Braze als Tag innerhalb des Tealium-Dashboards hinzuzufügen, um die Besucheraktivitäten zu verfolgen. Tags werden in der Regel von Marketern verwendet, um die Wirksamkeit von Online-Werbung, E-Mail-Marketing und Website-Personalisierung zu verstehen.

1. Navigieren Sie in Tealium zu **iQ > Tags > + Tag hinzufügen > Braze Web SDK**.
2. Geben Sie im Dialogfeld Tag-Konfiguration den API-Schlüssel (Ihren Bezeichner-Schlüssel für die Braze App), die Basis-URL (den Braze SDK-Endpunkt) und die [Code-Version des Braze Web SDK](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) ein. Sie können auch die Protokollierung aktivieren, um Informationen zu Debugging-Zwecken in der Internet-Konsole zu protokollieren.
3. Wählen Sie im Dialogfeld [Lastregeln](https://docs.tealium.com/iq-tag-management/load-rules/about/) die Option "Auf allen Seiten laden" oder wählen Sie **Regel erstellen**, um festzulegen, wann und wo eine Instanz dieses Tags auf Ihrer Website geladen werden soll.
4. In den **[Daten-Abbildungen](https://docs.tealium.com/iq-tag-management/data-mappings/about/)** wählen Sie **Zuordnungen erstellen**, um Tealium Daten auf Braze abzubilden. Die Zielvariablen für den Braze Web SDK-Tag sind in den Tab **Datenabbildung** für den Tag integriert. In den [folgenden Tabellen](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) sind die verfügbaren Zielkategorien aufgeführt und die einzelnen Zielnamen beschrieben.
5. Wählen Sie **Finish**.

### Side-by-side-Integrationen Ressourcen

- iOS-Fernbedienung: [Tealium Dokumentation](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Tealium GitHub Repository](https://github.com/Tealium/tealium-ios-braze-remote-command)
- Android Fernsteuerung: [Tealium Dokumentation](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Tealium GitHub Repository](https://github.com/Tealium/tealium-android-braze-remote-command)
- Internet SDK Tag: [Tealium Dokumentation](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)

## Server-zu-Server-Integration

Diese Integration leitet Daten von Tealium an die REST API von Braze weiter.

Die Server-zu-Server Integration unterstützt keine UI Features von Braze wie In-App-Nachrichten, Content-Cards oder Push-Benachrichtigungen. Es gibt auch automatisch erfasste Daten (z.B. Felder auf Geräteebene), die mit dieser Methode nicht verfügbar sind.

Wenn Sie diese Daten und Features nutzen möchten, sollten Sie unsere [Side-by-side]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium/#side-by-side-sdk-integration) SDK-Integration in Betracht ziehen.

### Schritt 1: Eine Quelle einrichten

Tealium setzt voraus, dass Sie zunächst eine gültige Datenquelle für Ihren Konnektor einrichten, aus der er schöpfen kann.
1. Navigieren Sie in der Seitenleiste von Tealium unter **Server-Side** zu **Quellen > Datenquellen > + Datenquelle hinzufügen**.
2. Suchen Sie die gewünschte Plattform in den verfügbaren Kategorien, und geben Sie Ihre Quelle an.<br>![]({% image_buster /assets/img/tealium/data_source.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. Wählen Sie aus den Optionen für **die Ereignisspezifikationen** die [Spezifikationen](https://docs.tealium.com/server-side/event-specifications/about/) aus, die Sie hinzufügen möchten. Ereignisspezifikationen helfen Ihnen, die Ereignisnamen und die erforderlichen Attribute für das Tracking in Ihrer Installation zu identifizieren. Diese Angaben werden auf eingehende Ereignisse angewendet.<br>![]({% image_buster /assets/img/tealium/event_specs.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>Nehmen Sie sich etwas Zeit, um darüber nachzudenken, welche Daten für Sie am wertvollsten sind und welche Spezifikationen für Ihren Anwendungsfall am geeignetsten erscheinen. [Angepasste Event-Spezifikationen](https://docs.tealium.com/iq-tag-management/events/about/) sind ebenfalls verfügbar. <br>
4. Der nächste Dialog bringt Sie zum Schritt **Code holen** voran. Der hier zur Verfügung gestellte Basiscode und der Code für das Tracking von Ereignissen dienen Ihnen als Installationsanleitung. Laden Sie die PDF-Datei herunter, wenn Sie diese Anweisungen an Ihr Team weitergeben möchten. Wählen Sie **Speichern & Weiter**, wenn Sie fertig sind.<br>
5. Sie können nun Ihre gespeicherte Quelle einsehen und Ereignisspezifikationen hinzufügen oder entfernen. <br>![]({% image_buster /assets/img/tealium/braze_connection.png %}){: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>In der Detailansicht der Datenquelle können Sie die folgenden Aktionen durchführen:
- Anzeigen und Kopieren des Schlüssels der Datenquelle
- Installationsanleitung ansehen
- Zurück zur Seite **Code holen** 
- Hinzufügen oder Entfernen von Ereignisspezifikationen
- Navigieren Sie, um Live-Ereignisse in Bezug auf eine Ereignisspezifikation anzuzeigen
- Und mehr...<br>
6. Zum Schluss wählen Sie oben auf der Seite **Speichern / Veröffentlichen** aus. Wenn Sie Ihren Quellcode nicht veröffentlichen, können Sie ihn bei der Konfiguration Ihres Braze Konnektors nicht finden.

Unter [Datenquellen](https://docs.tealium.com/server-side/data-sources/about-data-sources/) finden Sie weitere Anweisungen zum Einrichten und Bearbeiten Ihrer Datenquelle.

### Schritt 2: Einen Konnektor für Ereignisse erstellen

Ein Konnektor ist eine Integration zwischen Tealium und einem anderen Anbieter, die zur Übertragung von Daten verwendet wird. Diese Konnektoren enthalten Aktionen, die die unterstützten APIs des Partners repräsentieren. 

1. Navigieren Sie in der Seitenleiste von Tealium unter **Server-Side** zu **EventStream > Event Connectors.**
2. Wählen Sie den blauen Button **\+ Konnektor hinzufügen**, um den Marktplatz der Konnektoren zu durchsuchen. In dem neu erscheinenden Dialogfeld verwenden Sie die Spotlight-Suche, um den Konnektor **Braze** zu finden.
3. Um diesen Konnektor hinzuzufügen, klicken Sie auf die Kachel für den Konnektor **Braze**. Wenn Sie darauf klicken, können Sie die Verbindungsübersicht und eine Liste der erforderlichen Informationen, der unterstützten Aktionen und der Konfigurationsanweisungen anzeigen. Die Konfiguration umfasst drei Schritte: Quelle, Konfiguration und Aktion.

#### Quelle

Nachdem Sie die Quelle konfiguriert haben, gehen Sie zurück zur Seite mit dem Konnektor Braze unter **EventStream** > **Event Connectors** > **\+ Add Connector** > **Braze**. 

Wählen Sie dann die Datenquelle aus, die Sie gerade erstellt haben, und wählen Sie unter **Ereignis-Feed** die Option **Alle Ereignisse** oder eine bestimmte Ereignisspezifikation, den empfohlenen Pfad, um nur geänderte Werte an Braze zu senden. Wählen Sie **Weiter**.

#### Konfiguration

Wählen Sie dann unten auf der Seite **Konnektor hinzufügen** aus. Benennen Sie Ihren Konnektor und geben Sie hier den Endpunkt der Braze API und den REST-API-Schlüssel von Braze an.

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Wenn Sie bereits einen Konnektor erstellt haben, können Sie optional einen vorhandenen Konnektor aus der Liste der verfügbaren Konnektoren verwenden und ihn mit dem Bleistiftsymbol an Ihre Bedürfnisse anpassen oder mit dem Papierkorbsymbol löschen. 

#### Aktion

Benennen Sie als nächstes Ihre Konnektor-Aktion und wählen Sie einen Aktionstyp aus, der Daten gemäß der von Ihnen konfigurierten Abbildung sendet. Hier werden Sie Braze-Attribute, Ereignisse und Käufe auf Tealium-Attribut-, Ereignis- und Kaufnamen abbilden.

{% alert important %}
Nicht alle angebotenen Felder sind erforderlich.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Nutzer:innen verfolgen - Batch und Non-Batch %}

Mit dieser Aktion können Sie die Attribute von Nutzer:innen, Ereignissen und Käufen in einer einzigen Aktion tracken.

| Parameter | Beschreibung |
| ---------- | ----------- |
| Nutzer-ID | Verwenden Sie dieses Feld, um das Feld Nutzer:in von Tealium auf das entsprechende Feld von Braze abzubilden. Abbildung von einem oder mehreren Attributen der Nutzer:in. Wenn mehrere IDs angegeben werden, wird der erste Wert, der nicht leer ist, in der folgenden Reihenfolge ausgewählt: Externe ID, Braze ID, Alias-Name und Alias-Label.<br><br>\- Externe ID und Braze ID sollten beim Import von Push-Tokens nicht angegeben werden.<br>\- Wenn Sie einen Nutzer-Alias angeben, sollten der Alias-Name und das Alias-Label festgelegt werden. <br><br>Weitere Informationen finden Sie unter dem Braze-[Endpunkt `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). |
| Nutzerattribute | Verwenden Sie die vorhandenen Feldnamen der Braze-Benutzerprofile, um die Werte der Nutzerprofile im Braze-Dashboard zu aktualisieren, oder fügen Sie den Nutzerprofilen Ihre eigenen angepassten Daten für die [Attribute der Nutzer]({{site.baseurl}}/api/objects_filters/user_attributes_object/) hinzu.<br><br>\- Standardmäßig werden neue Nutzer:innen angelegt, wenn noch keine vorhanden sind.<br>\- Wenn Sie **Nur vorhandene Nutzer:innen aktualisieren** auf `true` setzen, werden nur vorhandene Nutzer:innen aktualisiert und keine neuen Nutzer:innen angelegt.<br>\- Wenn ein Tealium Attribut leer ist, wird es in Null umgewandelt und aus dem Nutzerprofil von Braze:innen entfernt. Anreicherungen sollten verwendet werden, wenn keine Nullwerte an Braze gesendet werden sollen, um ein Nutzer:in-Attribut zu entfernen. |
| Attribute der Nutzer:innen ändern | Verwenden Sie dieses Feld, um bestimmte Nutzer:innen-Attribute zu erhöhen oder zu verringern.<br><br>\- Integer-Attribute können um positive oder negative ganze Zahlen inkrementiert werden.<br>\- Attribute in Arrays können durch Hinzufügen oder Entfernen von Werten in bestehenden Arrays geändert werden. |
| Event | Ein Event stellt ein einzelnes Vorkommen eines angepassten Events durch einen bestimmten Nutzer:innen zu einem bestimmten Zeitpunkt dar. Verwenden Sie dieses Feld zum Tracking und zur Abbildung von Ereignisattributen, wie sie im [Braze-Ereignisobjekt]({{site.baseurl}}/api/objects_filters/event_object/) enthalten sind. <br><br>\- Das Attribut "Ereignis" `Name` ist für jedes zugeordnete Ereignis erforderlich.<br>\- Das Attribut `Time` wird automatisch auf jetzt gesetzt, wenn es nicht explizit abgebildet wird. <br>\- Standardmäßig werden neue Ereignisse erstellt, wenn noch keines vorhanden ist. Wenn Sie `Update Existing Only` auf `true` setzen, werden nur bestehende Ereignisse aktualisiert und es wird kein neues Ereignis erstellt.<br>\- Bilden Sie Attribute vom Typ Array ab, um mehrere Ereignisse hinzuzufügen. Attribute vom Typ Array müssen gleich lang sein.<br>\- Sie können Attribute mit einem einzigen Wert verwenden und auf jedes Ereignis anwenden. |
| Template für Veranstaltungen | Stellen Sie Ereignis-Templates zur Verfügung, auf die in den Daten referenziert werden kann. Templates können verwendet werden, um Daten zu transformieren, bevor sie an Braze gesendet werden. Weitere Informationen finden Sie in der [Anleitung für Templates](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) von Tealium. |
| Ereignis Template-Variable | Stellen Sie Template-Variablen für Ereignisse als Dateneingabe bereit. Lesen Sie den [Leitfaden für Template-Variablen](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) von Tealium, um mehr zu erfahren. |
| Kauf | Verwenden Sie dieses Feld, um die Attribute der Nutzer:innen zu verfolgen und abzubilden, wie sie im [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/) Braze enthalten sind.<br><br>\- Die Attribute `Product ID`, `Currency`, und `Price` sind für jeden zugeordneten Kauf erforderlich.<br>\- Das Attribut "Kauf" `Time` wird automatisch auf "jetzt" gesetzt, wenn es nicht explizit abgebildet wird.<br>\- Standardmäßig werden neue Einkäufe angelegt, wenn noch keine vorhanden sind. Wenn Sie `Update Existing Only` auf `true` setzen, werden nur bestehende Käufe aktualisiert und es wird kein neuer Kauf angelegt.<br>\- Bilden Sie Attribute vom Typ Array ab, um mehrere Artikel zum Kauf hinzuzufügen. Attribute vom Typ Array müssen gleich lang sein.<br>\- Sie können Attribute mit einem einzigen Wert verwenden, die dann für jeden Artikel gelten.|
| Template kaufen | Templates können verwendet werden, um Daten zu transformieren, bevor sie an Braze gesendet werden.<br>\- Definieren Sie ein Purchase Template, wenn Sie Unterstützung für verschachtelte Objekte benötigen.<br>\- Wenn eine Einkaufsvorlage definiert wird, wird die Konfiguration, die im Abschnitt Einkäufe Ihrer Aktion eingerichtet wurde, ignoriert.<br>\- Weitere Informationen finden Sie in der [Anleitung für Templates](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) von Tealium.|
| Template kaufen variabel | Stellen Sie Produkt-Template-Variablen als Dateneingabe bereit. Lesen Sie den [Leitfaden für Template-Variablen](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) von Tealium, um mehr zu erfahren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example.png %})

{% endtab %}
{% tab Nutzer:in löschen - Nicht-Batch %}

Diese Aktion erlaubt es Ihnen, Nutzer:innen aus dem Braze-Dashboard zu löschen.

| Parameter | Beschreibung |
| ---------- | ----------- |
| Nutzer-ID | Verwenden Sie dieses Feld, um das Feld Nutzer:in von Tealium auf seine Braze-Entsprechung abzubilden. <br><br>\- Abbildung von einem oder mehreren Attributen der Nutzer:in. Wenn mehrere IDs angegeben werden, wird der erste Wert, der nicht leer ist, in der folgenden Reihenfolge ausgewählt: Externe ID, Braze ID, Alias-Name und Alias-Label.<br>\- Wenn Sie einen Nutzer:innen-Alias angeben, sollten sowohl Alias-Name als auch Alias-Label festgelegt werden.<br><br>Weitere Informationen finden Sie unter dem Braze-[Endpunkt `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete.png %})

Wenn Sie die von Ihnen gewählten Optionen ändern möchten, wählen Sie **Zurück** zum Bearbeiten oder **Beenden** zum Abschließen.

{% endtab %}
{% endtabs %}

Wählen Sie **Weiter**.

Ihr Konnektor wird nun in der Liste der Konnektoren auf Ihrer Tealium-Startseite angezeigt. <br>![]({% image_buster /assets/img/tealium/summary_list.png %}){: style="max-width:80%;"}

Stellen Sie sicher, dass Sie **Speichern / Veröffentlichen** für Ihren Konnektor auswählen, wenn Sie fertig sind. Die von Ihnen konfigurierten Aktionen werden nun ausgelöst, wenn die triggernden Verbindungen erfüllt sind. 

### Schritt 3: Testen Sie Ihren Tealium Konnektor

Nachdem Ihr Konnektor betriebsbereit ist, sollten Sie ihn testen, um sicherzustellen, dass er ordnungsgemäß funktioniert. Der einfachste Weg, dies zu testen, ist die Verwendung des Tealium **Trace Tools**. Um Trace nutzen zu können, müssen Sie die Tealium Tools Browser-Erweiterung hinzufügen.

1. Um einen neuen Trace zu starten, wählen Sie **Trace** in der Seitenleiste unter **Serverseitige** Optionen. Wählen Sie **Start** und erfassen Sie die Trace ID.
2. Öffnen Sie die Browsererweiterung und geben Sie die Trace ID in AudienceStream Trace ein.
3. Prüfen Sie das Realtime-Protokoll.
4. Suchen Sie nach der Aktion, die Sie validieren möchten, indem Sie den Eintrag **Ausgelöste Aktionen** auswählen und erweitern.
5. Suchen Sie nach der Aktion, die Sie validieren möchten, und sehen Sie sich den Protokollstatus an. 

Ausführlichere Anweisungen zur Implementierung des Trace-Tools von Tealium finden Sie in der [Trace-Dokumentation](https://docs.tealium.com/server-side/connectors/trace/about/) von Tealium.

## Demo zur Integration

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Mögliche Mehrkosten für Datenpunkte

Es gibt drei Möglichkeiten, wie Sie bei der Integration von Braze über Tealium versehentlich auf Mehrkosten bei den Daten stoßen können:

#### Doppelte Daten senden - nur Braze-Deltas von Attributen senden

Tealium sendet keine Braze-Deltas von Nutzer:innen-Attributen. Wenn Sie zum Beispiel eine EventStream-Aktion haben, die den Vornamen, die E-Mail und die Handynummer eines Nutzers trackt, sendet Tealium alle drei Attribute an Braze, sobald die Aktion getriggert wird. Tealium wird nicht danach suchen, was sich geändert hat oder aktualisiert wurde und nur diese Informationen senden.

**Lösung**: <br>Sie können in Ihrem Backend überprüfen, ob sich ein Attribut geändert hat oder nicht, und wenn ja, die entsprechenden Methoden von Tealium aufrufen, um das Nutzerprofil zu aktualisieren. **Das tun Nutzer:innen, die Braze direkt integrieren, normalerweise auch.** <br>**ODER**<br> Wenn Sie keine eigene Version eines Nutzerprofils in Ihrem Backend speichern und nicht feststellen können, ob sich Attribute ändern oder nicht, können Sie AudienceStream und
[Anreicherungen erstellen](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/), um Nutzer:innen nur Attribute zu senden, wenn sich die Werte geändert haben. Siehe die Dokumentation von Tealium zu den [Anreicherungsregeln](https://docs.tealium.com/server-side-connectors/braze-connector/).

#### Senden von irrelevanten Daten oder unnötiges Überschreiben von Daten

Wenn Sie mehrere EventStreams haben, die auf denselben Event-Feed abzielen, werden **alle für diesen Konnektor aktivierten Aktionen** automatisch ausgelöst, sobald eine einzelne Aktion getriggert wird. \*\*Dies könnte auch dazu führen, dass Daten in Braze überschrieben werden und unnötige Datenpunkte verbrauchen.\\

**Lösung**: <br>Richten Sie eine separate Ereignisspezifikation oder einen Feed ein, um jede Aktion zu tracken. <br>**ODER**<br> Deaktivieren Sie Aktionen (oder Konnektoren), die Sie nicht auslösen möchten, mit den Umschaltern im Dashboard von Tealium.

#### Braze zu früh initialisieren

Nutzer:innen, die Tealium mit dem Braze Web SDK Tag integrieren, können einen dramatischen Anstieg ihrer MAU verzeichnen. **Wenn Braze beim Laden der Seite initialisiert wird, erstellt Braze jedes Mal ein anonymes Profil, wenn ein Internet Nutzer:in zum ersten Mal auf die Website navigiert.** Manche möchten das Nutzer:innen-Verhalten nur dann tracken, wenn die Nutzer:innen eine Aktion abgeschlossen haben, wie z.B. "Angemeldet" oder "Video angesehen", um ihre MAU-Zahl zu senken.

**Lösung**: <br>Richten Sie [Lastregeln](https://docs.tealium.com/iq-tag-management/load-rules/about/) ein, um genau zu bestimmen, wann und wo ein Tag auf Ihrer Website geladen wird. 

