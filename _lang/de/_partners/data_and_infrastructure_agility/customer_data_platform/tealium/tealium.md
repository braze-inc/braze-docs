---
nav_title: Tealium
article_title: Tealium
page_order: 1
alias: /partners/tealium/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Tealium, einer universellen Datendrehscheibe, die es Ihnen ermöglicht, mobile, Web- und alternative Daten mit anderen Drittquellen zu verbinden."
page_type: partner
search_tag: Partner

---

# Tealium

> [Tealium](https://tealium.com/) ist eine universelle Datendrehscheibe und Kundendatenplattform, die sich aus EventStream, AudienceStream und iQ Tag Management zusammensetzt und es Ihnen ermöglicht, Mobil-, Web- und alternative Daten aus Drittquellen zu verbinden. Die Verbindung von Tealium mit Braze ermöglicht einen Datenfluss von benutzerdefinierten Ereignissen, Benutzerattributen und Käufen, die es Ihnen ermöglichen, auf Ihre Daten in Echtzeit zu reagieren.

![Eine Tealium-Übersichtsgrafik, die zeigt, wie die verschiedenen Tealium-Produkte und die Braze-Plattform zusammenpassen, um kanalübergreifende Kampagnen in Echtzeit zu aktivieren.][22]{: style="border:0;"}

Mit der Integration von Braze und Tealium können Sie Ihre Benutzer verfolgen und Daten an verschiedene Anbieter von Benutzeranalysen weiterleiten. Mit Tealium können Sie:
- Synchronisieren Sie Tealium Audiences mit [AudienceStream]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/) mit Braze, um Braze-Kampagnen und Canvases zu personalisieren oder Segmente zu erstellen.
- [Importieren Sie Daten plattformübergreifend](#choose-your-integration-type). Braze bietet sowohl eine [Side-by-Side-SDK-Integration](#side-by-side-sdk-integration) für Ihre Android-, iOS- und Webanwendungen als auch eine [Server-zu-Server-Integration](#server-to-server-integration), die innerhalb jeder Plattform verwendet werden kann, die Ereignisdaten melden kann.<br><br>

{% tabs %}
{% tab EventStream %}
Tealium EventStream ist ein Datenerfassungs- und API-Hub, der im Zentrum Ihrer Daten steht. EventStream wickelt die gesamte Datenlieferkette ab, von der Einrichtung und Installation bis hin zur Identifizierung, Validierung und Verbesserung der eingehenden Benutzerdaten. EventStream arbeitet in Echtzeit mit Ereignis-Feeds und Konnektoren. Im Folgenden finden Sie die Funktionen, aus denen der [EventStream](https://docs.tealium.com/server-side/getting-started/eventstream-api-hub/introduction/) besteht.
- Datenquellen (Installation und Datenerfassung)
- Live-Ereignisse (Echtzeit-Datenprüfung)
- Ereignisspezifikationen und Attribute (Anforderungen an die Datenebene und Validierung)
- Ereignis-Feeds (gefilterte Ereignistypen)
- Ereignis-Konnektoren (API-Hub-Aktionen)

{% endtab %}
{% tab AudienceStream %}

Tealium AudienceStream ist eine Omnichannel-Kundensegmentierungs- und Echtzeit-Aktionsmaschine. AudienceStream verwendet die Daten, die in EventStream einfließen, und erstellt Besucherprofile, die die wichtigsten Attribute des Engagements Ihrer Kunden mit Ihrer Marke darstellen. Weitere Informationen zur Einrichtung finden Sie in unserem Artikel über [AudienceStream]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/).

{% endtab %}
{% tab iQ Tag Management %}
Mit Tealium iQ können Sie Code in Ihren Anwendungen auslösen, indem Sie ein Tag in der Tealium iQ Tag Management UI verwenden. Dieses Tag sammelt, steuert und liefert Ereignisdaten von mobilen und Web-Plattformen. So können Sie eine native Braze-Implementierung konfigurieren, ohne Braze-spezifischen Code zu Ihren Anwendungen hinzuzufügen. Benutzer können Mobile Remote Commands über iQ Tag Management oder JSON-Konfigurationsdateien (empfohlener Ansatz von Tealium) integrieren. Benutzer, die das Braze Web SDK verwenden, müssen die Integration über das Web iQ Tag vornehmen.

Wenn Sie mehr über die Vor- und Nachteile der einzelnen Methoden erfahren möchten, lesen Sie den folgenden Abschnitt zum [Tealium iQ Tag Manager](#mobile-remote-commands).
{% endtab %}
{% endtabs %}

{% alert important %}
Tealium bietet sowohl Batch- als auch Non-Batch-Connector-Aktionen. Der Non-Batch-Connector sollte verwendet werden, wenn Echtzeitanfragen für den Anwendungsfall wichtig sind und keine Bedenken bestehen, dass die API-Ratenbeschränkungen von Braze überschritten werden. Wenden Sie sich an den Braze-Support oder Ihren Kundenbetreuer, wenn Sie irgendwelche Fragen haben.<br><br>

Bei Batch-Verbindungen werden die Anfragen in eine Warteschlange gestellt, bis einer der folgenden Schwellenwerte erreicht ist:<br><br>
- Maximale Anzahl von Anfragen: 75
- Maximale Zeit seit der ältesten Anfrage: 10 Minuten
- Maximale Größe der Anfragen: 1 MB

Tealium stapelt standardmäßig keine Zustimmungsereignisse (Abonnementeinstellungen) oder Benutzerlöschungsereignisse.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Tealium-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Tealium-Konto](https://my.tealiumiq.com/) mit server- und/oder clientseitigem Zugriff. | 
| Installierter Quellcode und [Tealium-Quellbibliotheken](https://docs.tealium.com/platforms/) | Der Ursprung aller Daten, die an Tealium gesendet werden, wie z.B. mobile Apps, Websites oder Backend-Server.<br><br>Sie müssen die Bibliotheken in Ihrer Anwendung, Ihrer Website oder Ihrem Server installieren, bevor Sie einen erfolgreichen Tealium-Connector einrichten können. |
| Braze REST und SDK Endpunkt | Ihre REST- oder SDK-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
| Braze App-Identifikationsschlüssel (nur Side-by-Side) | Der Schlüssel zu Ihrer App-Kennung. <br><br>Diesen finden Sie im **Braze Dashboard > Einstellungen verwalten > API-Schlüssel**. |
| Code-Version (nur Seite an Seite) | Entspricht der SDK-Version und sollte im Format major.minor angegeben werden (zum Beispiel 3.2 und nicht 3.0.1). Die Code-Version sollte 3.0 oder höher sein. |
| REST-API-Schlüssel (nur von Server zu Server) | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track` und `users.delete`. <br><br>Dieser kann über **Braze Dashboard > Developer Console > REST API Key > Create New API Key** erstellt werden.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Wählen Sie Ihren Integrationstyp

| Integration | Details |
| ----------- | ------- |
| [Seite an Seite](#side-by-side-sdk-integration) | Verwendet das SDK von Tealium, um Ereignisse in die nativen Aufrufe von Braze zu übersetzen. Dies ermöglicht den Zugriff auf tiefere Funktionen und eine umfassendere Nutzung von Braze als bei der Server-zu-Server-Integration.<br><br>Wenn Sie Braze-Fernbefehle verwenden möchten, beachten Sie, dass Tealium nicht alle Braze-Methoden (z.B. Content Cards) unterstützt. Um eine Braze-Methode zu verwenden, die nicht durch einen entsprechenden Remote-Befehl abgebildet wird, müssen Sie die Methode durch Hinzufügen von nativem Braze-Code zu Ihrer Codebasis aufrufen.|
| [Server-zu-Server](#server-to-server-integration) | Leitet Daten von Tealium an die REST-API-Endpunkte von Braze weiter.<br><br>Unterstützt keine Braze UI-Funktionen wie In-App-Nachrichten, Content Cards oder Push-Benachrichtigungen. Es gibt auch automatisch erfasste Daten, wie z.B. Felder auf Geräteebene, die mit dieser Methode nicht verfügbar sind.<br><br>Ziehen Sie eine Side-by-Side-Integration in Betracht, wenn Sie diese Funktionen nutzen möchten.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Nebeneinander liegende SDK-Integration

### Ferngesteuerte Befehle

Remote-Befehle sind eine Funktion der Tealium iOS- und Android-Bibliotheken, die es Ihnen ermöglichen, vom Tealium SDK - über die Braze-Server - Anrufe an Braze zu tätigen. Das Braze-Fernbedienungsmodul installiert und erstellt automatisch die erforderlichen Braze-Bibliotheken und kümmert sich um das Rendering von Nachrichten und die Verfolgung von Analysen. Um Braze mobile remote command zu verwenden, müssen Sie die Tealium-Bibliotheken in Ihren Anwendungen installieren.

Tealium bietet zwei Möglichkeiten zur Integration von Mobile Remote Command. Es gibt keinen Funktionsverlust zwischen den Integrationstypen, und der zugrunde liegende native Code ist identisch.

| Mobile Fernsteuerungsmethode | Profis | Nachteile |
| --- | --- | --- |
| **Fernbedienungs-Tag** | Ändern Sie die Zuordnungen und Daten, die an den Fernbefehl gesendet werden, ganz einfach über die Tealium iQ UI.<br><br>Dies ermöglicht es uns, zusätzliche Daten oder Ereignisse an ein SDK eines Drittanbieters zu senden, nachdem die App bereits im App Store ist, ohne dass der Kunde die App aktualisieren muss. | Das Tag Management Modul in der App verlässt sich auf eine versteckte Webansicht, um JavaScript zu verarbeiten. |
| **JSON-Konfigurationsdatei**<br>[(Empfohlen](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#how-it-works)) | Durch die Verwendung der JSON-Methode entfällt die Notwendigkeit einer versteckten Webansicht in der Anwendung und der Speicherverbrauch wird erheblich reduziert.<br><br>Die JSON-Datei kann per Fernzugriff oder lokal in der Anwendung des Kunden gehostet werden. | Im Moment gibt es keine Benutzeroberfläche, um dies zu verwalten, so dass es ein wenig zusätzlichen Aufwand erfordert.<br><br>Hinweis: Tealium arbeitet an einer Verwaltungsoberfläche, die dieses Problem lösen und den JSON-Fernbedienungsbefehlen das gleiche Maß an Flexibilität verleihen wird, wie es bei der iQ Tag-Verwaltungsversion der Fall ist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Verwenden Sie die Datenmappings von Braze Mobile Remote Command, um Standard-Benutzerattribute und benutzerdefinierte Attribute festzulegen und Käufe und benutzerdefinierte Ereignisse zu verfolgen. In der folgenden Tabelle finden Sie die entsprechenden Lötmethoden.

| Fernsteuerung | Hartlötverfahren |
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

Weitere Einzelheiten zur Einrichtung von Braze mobile remote command und eine Übersicht der unterstützten Methoden finden Sie in der Tealium-Entwicklerdokumentation:
- [Fernsteuerung](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#json-template)
- [Fernbedienungs-Tag](https://docs.tealium.com/client-side-tags/braze-mobile-remote-command-tag/)

{% alert important %}
Die mobilen Fernbedienungsbefehle von Braze unterstützen nicht alle Braze-Methoden und Nachrichtenkanäle (z.B. Content Cards). Um eine Braze-Methode zu verwenden, die nicht durch einen entsprechenden Remote-Befehl abgebildet wird, müssen Sie die Methode direkt aufrufen, indem Sie Ihrer Codebasis nativen Braze-Code hinzufügen.
{% endalert%}

### Braze Web SDK-Tag

Verwenden Sie das Braze Web SDK Tag, um das Web SDK von Braze auf Ihrer Website einzusetzen. [Tealium iQ Tag Management](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) ermöglicht es Kunden, Braze als Tag innerhalb des Tealium-Dashboards hinzuzufügen, um Besucheraktivitäten zu verfolgen. Tags werden in der Regel von Marketingfachleuten verwendet, um die Wirksamkeit von Online-Werbung, E-Mail-Marketing und Website-Personalisierung zu verstehen.

1. Navigieren Sie in Tealium zu **iQ > Tags > + Tag hinzufügen > Braze Web SDK**.
2. Geben Sie im Dialogfeld Tag-Konfiguration den API-Schlüssel (Ihren Braze-App-Identifizierungsschlüssel), die Basis-URL (Braze-SDK-Endpunkt) und die [Braze Web SDK-Codeversion](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) ein. Sie können auch die Protokollierung aktivieren, um Informationen zu Debugging-Zwecken in der Webkonsole zu protokollieren.
3. Wählen Sie im Dialogfeld [Lastregeln](https://docs.tealium.com/iq-tag-management/load-rules/about/) die Option "Auf allen Seiten laden" oder wählen Sie die Option **Regel erstellen**, um festzulegen, wann und wo eine Instanz dieses Tags auf Ihrer Website geladen werden soll.
4. In den **[Daten-Zuordnungen](https://docs.tealium.com/iq-tag-management/data-mappings/about/)** wählen Sie **Zuordnungen erstellen**, um Tealium-Daten auf Braze abzubilden. Die Zielvariablen für das Braze Web SDK-Tag sind in der Registerkarte **Datenzuordnung** für das Tag integriert. In den [folgenden Tabellen](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) sind die verfügbaren Zielkategorien aufgeführt und die einzelnen Zielnamen beschrieben.
5. Wählen Sie **Finish**.

### Ressourcen für die Seite-an-Seite-Integration

- iOS-Fernbedienung: [Tealium Dokumentation](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Tealium GitHub Repository](https://github.com/Tealium/tealium-ios-braze-remote-command)
- Android-Fernbedienung: [Tealium Dokumentation](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Tealium GitHub Repository](https://github.com/Tealium/tealium-android-braze-remote-command)
- Web SDK-Tag: [Tealium Dokumentation](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)

## Server-zu-Server-Integration

Diese Integration leitet Daten von Tealium an die REST-API von Braze weiter.

Die Server-zu-Server-Integration unterstützt keine Braze UI-Funktionen wie In-App-Nachrichten, Content Cards oder Push-Benachrichtigungen. Es gibt auch automatisch erfasste Daten (z. B. Felder auf Geräteebene), die mit dieser Methode nicht verfügbar sind.

Wenn Sie diese Daten und diese Funktionen nutzen möchten, sollten Sie unsere [Side-by-Side]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium/#side-by-side-sdk-integration) SDK-Integration in Betracht ziehen.

### Schritt 1: Eine Quelle einrichten

Tealium erfordert, dass Sie zunächst eine gültige Datenquelle einrichten, aus der Ihr Connector schöpfen kann.
1. Navigieren Sie in der Seitenleiste von Tealium unter **Server-Side** zu **Quellen > Datenquellen > + Datenquelle hinzufügen**.
2. Suchen Sie die gewünschte Plattform in den verfügbaren Kategorien und geben Sie den Namen Ihrer Quelle an. Dies ist ein Pflichtfeld.<br>![][6]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. Wählen Sie aus den Optionen für **die Ereignisspezifikationen** die [Spezifikationen](https://docs.tealium.com/server-side/event-specifications/about/) aus, die Sie hinzufügen möchten. Ereignisspezifikationen helfen Ihnen, die Namen der Ereignisse und die erforderlichen Attribute zu ermitteln, die Sie in Ihrer Installation verfolgen müssen. Diese Angaben werden auf eingehende Ereignisse angewendet.<br>![][7]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>Nehmen Sie sich etwas Zeit, um darüber nachzudenken, welche Daten für Sie am wertvollsten sind und welche Spezifikationen für Ihren Anwendungsfall am geeignetsten erscheinen. [Benutzerdefinierte Ereignisspezifikationen][19] sind ebenfalls verfügbar. <br>
4. Der nächste Dialog führt Sie zum Schritt **Code holen**. Der hier bereitgestellte Basiscode und der Code für die Ereignisverfolgung dienen als Installationsanleitung. Laden Sie die mitgelieferte PDF-Datei herunter, wenn Sie diese Anweisungen an Ihr Team weitergeben möchten. Wählen Sie **Speichern & Weiter**, wenn Sie fertig sind.<br>
5. Sie können nun Ihre gespeicherte Quelle einsehen und Ereignisspezifikationen hinzufügen oder entfernen. <br>![][18]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>In der Detailansicht der Datenquelle können Sie die folgenden Aktionen durchführen:
- Anzeigen und Kopieren des Schlüssels der Datenquelle
- Installationsanleitung ansehen
- Zurück zur Seite **Code holen** 
- Hinzufügen oder Entfernen von Ereignisspezifikationen
- Navigieren Sie, um Live-Ereignisse in Bezug auf eine Ereignisspezifikation anzuzeigen
- Und mehr...<br>
6. Wählen Sie schließlich die Option **Speichern / Veröffentlichen**, die Sie oben auf der Seite finden. Wenn Sie Ihren Quellcode nicht veröffentlichen, können Sie ihn bei der Konfiguration Ihres Braze Connectors nicht finden.

Unter [Datenquellen](https://docs.tealium.com/server-side/data-sources/about-data-sources/) finden Sie weitere Anweisungen zum Einrichten und Bearbeiten Ihrer Datenquelle.

### Schritt 2: Erstellen Sie einen Ereignis-Connector

Ein Konnektor ist eine Integration zwischen Tealium und einem anderen Anbieter, die der Datenübertragung dient. Diese Konnektoren enthalten Aktionen, die die unterstützten APIs des Partners darstellen. 

1. Navigieren Sie in der Seitenleiste von Tealium unter **Server-Side** zu **EventStream > Event Connectors**.
2. Klicken Sie auf die blaue Schaltfläche **\+ Konnektor hinzufügen**, um den Marktplatz für Konnektoren zu durchsuchen. In dem neu erscheinenden Dialogfeld verwenden Sie die Spotlight-Suche, um den **Braze-Anschluss** zu finden.
3. Um diesen Anschluss hinzuzufügen, klicken Sie auf die Kachel **Braze-Anschluss**. Wenn Sie darauf klicken, können Sie die Verbindungsübersicht und eine Liste der erforderlichen Informationen, unterstützten Aktionen und Konfigurationsanweisungen anzeigen. Die Konfiguration umfasst drei Schritte: Quelle, Konfiguration und Aktion.

#### Quelle

Nachdem Sie die Quelle konfiguriert haben, gehen Sie zurück zur Braze-Connector-Seite unter **EventStream** > **Event Connectors** > **\+ Add Connector** > **Braze**. 

Wählen Sie dann die Datenquelle aus, die Sie gerade erstellt haben, und wählen Sie unter **Ereignis-Feed** die Option **Alle Ereignisse** oder eine bestimmte Ereignisspezifikation, den empfohlenen Pfad, um nur geänderte Werte an Braze zu senden. Wählen Sie **Weiter**.

#### Konfiguration

Wählen Sie dann unten auf der Seite die Option **Connector hinzufügen**. Benennen Sie Ihren Connector und geben Sie hier Ihren Braze-API-Endpunkt und Ihren Braze-REST-API-Schlüssel an.

![][15]{: style="max-width:70%;"}

Wenn Sie bereits eine Verbindung erstellt haben, können Sie optional eine bestehende Verbindung aus der Liste der verfügbaren Verbindungen verwenden und sie mit dem Bleistiftsymbol an Ihre Bedürfnisse anpassen oder mit dem Papierkorbsymbol löschen. 

#### Aktion

Benennen Sie als nächstes Ihre Konnektoraktion und wählen Sie einen Aktionstyp, der Daten entsprechend der von Ihnen konfigurierten Zuordnung sendet. Hier werden Sie Braze-Attribute, -Ereignisse und -Käufe den Tealium-Attribut-, -Ereignis- und -Kaufnamen zuordnen.

{% alert important %}
Nicht alle angebotenen Felder sind erforderlich.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Benutzer verfolgen - Batch und Non-Batch %}

Mit dieser Aktion können Sie Benutzer-, Ereignis- und Kaufattribute in einer einzigen Aktion verfolgen.

| Parameter | Beschreibung |
| ---------- | ----------- |
| Nutzer-ID | Verwenden Sie dieses Feld, um das Tealium-Benutzer-ID-Feld seinem Braze-Äquivalent zuzuordnen. Ordnen Sie ein oder mehrere Benutzer-ID-Attribute zu. Wenn mehrere IDs angegeben werden, wird der erste Wert, der nicht leer ist, anhand der folgenden Prioritätsreihenfolge ausgewählt: Externe ID, Braze ID, Alias-Name und Alias-Etikett.<br><br>\- Externe ID und Braze ID sollten beim Importieren von Push-Tokens nicht angegeben werden.<br>\- Wenn Sie einen Benutzer-Alias angeben, sollten der Alias-Name und das Alias-Label festgelegt werden. <br><br>Weitere Informationen finden Sie auf dem Braze [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). |
| Nutzerattribute | Verwenden Sie die vorhandenen Feldnamen der Benutzerprofile von Braze, um die Werte der Benutzerprofile im Braze-Dashboard zu aktualisieren, oder fügen Sie den Benutzerprofilen Ihre eigenen [benutzerdefinierten Attributdaten]({{site.baseurl}}/api/objects_filters/user_attributes_object/) hinzu.<br><br>\- Standardmäßig werden neue Benutzer angelegt, wenn keine vorhanden sind.<br>\- Wenn Sie **Nur vorhandene Benutzer aktualisieren** auf `true` setzen, werden nur vorhandene Benutzer aktualisiert und keine neuen Benutzer erstellt.<br>\- Wenn ein Tealium-Attribut leer ist, wird es in Null umgewandelt und aus dem Braze-Benutzerprofil entfernt. Anreicherungen sollten verwendet werden, wenn zum Entfernen eines Benutzerattributs keine Nullwerte an Braze gesendet werden sollen. |
| Benutzerattribute ändern | Verwenden Sie dieses Feld, um bestimmte Benutzerattribute zu erhöhen oder zu verringern<br><br>\- Ganzzahlige Attribute können um positive oder negative ganze Zahlen erhöht werden.<br>\- Array-Attribute können durch Hinzufügen oder Entfernen von Werten in bestehenden Arrays geändert werden. |
| Event | Ein Ereignis stellt ein einzelnes Auftreten eines benutzerdefinierten Ereignisses durch einen bestimmten Benutzer zu einem bestimmten Zeitpunkt dar. Verwenden Sie dieses Feld, um Ereignisattribute wie die im [Braze-Ereignisobjekt]({{site.baseurl}}/api/objects_filters/event_object/) zu verfolgen und zuzuordnen. <br><br>\- Das Ereignisattribut `Name` ist für jedes zugeordnete Ereignis erforderlich.<br>\- Das Ereignisattribut `Time` wird automatisch auf jetzt gesetzt, wenn es nicht explizit zugewiesen wird. <br>\- Standardmäßig werden neue Ereignisse erstellt, wenn noch keines vorhanden ist. Wenn Sie `Update Existing Only` auf `true` setzen, werden nur bestehende Ereignisse aktualisiert und es wird kein neues Ereignis erstellt.<br>\- Ordnen Sie Attribute vom Typ Array zu, um mehrere Ereignisse hinzuzufügen. Attribute vom Typ Array müssen gleich lang sein.<br>\- Einzelwertattribute können verwendet und auf jedes Ereignis angewendet werden. |
| Ereignis-Vorlage | Stellen Sie Ereignisvorlagen bereit, auf die in den Körperdaten verwiesen werden kann. Vorlagen können verwendet werden, um Daten umzuwandeln, bevor sie an Braze gesendet werden. Weitere Informationen finden Sie im [Vorlagen-Leitfaden](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) von Tealium. |
| Variable Ereignis-Vorlage | Geben Sie Variablen der Ereignisvorlage als Dateneingabe ein. Weitere Informationen finden Sie im [Leitfaden für Vorlagenvariablen](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) von Tealium. |
| Kauf | Verwenden Sie dieses Feld, um die Kaufattribute des Benutzers zu verfolgen und zuzuordnen, wie sie im [Braze-Kaufobjekt]({{site.baseurl}}/api/objects_filters/purchase_object/) enthalten sind.<br><br>\- Die Kaufattribute `Product ID`, `Currency` und `Price` sind für jeden zugeordneten Kauf erforderlich.<br>\- Das Kaufattribut `Time` wird automatisch auf jetzt gesetzt, wenn es nicht explizit zugewiesen wird.<br>\- Standardmäßig werden neue Einkäufe angelegt, wenn noch keine vorhanden sind. Wenn Sie `Update Existing Only` auf `true` setzen, werden nur bestehende Käufe aktualisiert und es wird kein neuer Kauf angelegt.<br>\- Ordnen Sie Attribute vom Typ Array zu, um mehrere Kaufartikel hinzuzufügen. Attribute vom Typ Array müssen gleich lang sein.<br>\- Einzelwertattribute können verwendet werden und gelten für jeden Artikel.|
| Vorlage kaufen | Vorlagen können verwendet werden, um Daten umzuwandeln, bevor sie an Braze gesendet werden.<br>\- Definieren Sie eine Kaufvorlage, wenn Sie Unterstützung für verschachtelte Objekte benötigen.<br>\- Wenn eine Kaufvorlage definiert wird, wird die Konfiguration, die im Abschnitt Käufe Ihrer Aktion eingerichtet wurde, ignoriert.<br>\- Weitere Informationen finden Sie im [Vorlagen-Leitfaden](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) von Tealium.|
| Kaufvorlage variabel | Stellen Sie Produktvorlagenvariablen als Dateneingabe bereit. Weitere Informationen finden Sie im [Leitfaden für Vorlagenvariablen](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) von Tealium. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example.png %})

{% endtab %}
{% tab Benutzer löschen - Nicht-Batch %}

Mit dieser Aktion können Sie Benutzer aus dem Braze Dashboard löschen.

| Parameter | Beschreibung |
| ---------- | ----------- |
| Nutzer-ID | Verwenden Sie dieses Feld, um die Tealium-Benutzer-ID dem entsprechenden Feld in Braze zuzuordnen. <br><br>\- Ordnen Sie ein oder mehrere Benutzer-ID-Attribute zu. Wenn mehrere IDs angegeben werden, wird der erste Wert, der nicht leer ist, anhand der folgenden Prioritätsreihenfolge ausgewählt: Externe ID, Braze ID, Alias-Name und Alias-Etikett.<br>\- Wenn Sie einen Benutzer-Alias angeben, sollten sowohl Alias-Name als auch Alias-Bezeichnung festgelegt werden.<br><br>Weitere Informationen finden Sie unter dem [Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) Braze [`/users/delete`.]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete.png %})

Wenn Sie die von Ihnen gewählten Optionen ändern möchten, wählen Sie **Zurück** zum Bearbeiten oder **Beenden** zum Abschließen.

{% endtab %}
{% endtabs %}

Wählen Sie **Weiter**.

Ihr Connector wird nun in der Liste der Connectoren auf Ihrer Tealium-Startseite angezeigt. <br>![][13]{: style="max-width:80%;"}

Stellen Sie sicher, dass Sie **Speichern / Veröffentlichen** für Ihren Connector wählen, wenn Sie fertig sind. Die von Ihnen konfigurierten Aktionen werden nun ausgelöst, wenn die Auslöserverbindungen erfüllt sind. 

### Schritt 3: Testen Sie Ihren Tealium-Anschluss

Nachdem Ihr Connector eingerichtet ist, sollten Sie ihn testen, um sicherzustellen, dass er ordnungsgemäß funktioniert. Der einfachste Weg, dies zu testen, ist die Verwendung des Tealium **Trace Tools**. Um Trace nutzen zu können, müssen Sie die Browser-Erweiterung Tealium Tools hinzufügen.

1. Um einen neuen Trace zu starten, wählen Sie **Trace** in der Seitenleiste unter **Serverseitige** Optionen. Wählen Sie **Start** und erfassen Sie die Trace-ID.
2. Öffnen Sie die Browsererweiterung und geben Sie die Trace-ID in AudienceStream Trace ein.
3. Prüfen Sie das Echtzeit-Protokoll.
4. Suchen Sie nach der Aktion, die Sie validieren möchten, indem Sie den Eintrag **Ausgelöste Aktionen** zum Erweitern auswählen.
5. Suchen Sie nach der Aktion, die Sie validieren möchten, und sehen Sie sich den Protokollstatus an. 

Ausführlichere Anweisungen zur Implementierung des Trace-Tools von Tealium finden Sie in der [Trace-Dokumentation][21] ] von Tealium.

## Demo zur Integration

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Mögliche Überschreitungen der Datenpunkte

Es gibt drei Möglichkeiten, wie Sie bei der Integration von Braze über Tealium versehentlich auf Datenüberlastungen stoßen können:

#### Doppelte Daten senden - senden Sie nur Braze-Deltas von Attributen

Tealium sendet keine Braze-Deltas von Benutzerattributen. Wenn Sie zum Beispiel eine EventStream-Aktion haben, die den Vornamen, die E-Mail-Adresse und die Handynummer eines Benutzers erfasst, sendet Tealium alle drei Attribute an Braze, sobald die Aktion ausgelöst wird. Tealium wird nicht danach suchen, was sich geändert hat oder aktualisiert wurde und nur diese Informationen senden.

**Lösung**: <br>Sie können Ihr Backend überprüfen, um festzustellen, ob sich ein Attribut geändert hat oder nicht, und wenn ja, die entsprechenden Methoden von Tealium aufrufen, um das Benutzerprofil zu aktualisieren. **Das ist es, was Benutzer, die Braze direkt integrieren, normalerweise tun.** <br>**ODER**<br> Wenn Sie keine eigene Version eines Benutzerprofils in Ihrem Backend speichern und nicht feststellen können, ob sich Attribute ändern oder nicht, können Sie AudienceStream und
[Anreicherungen erstellen](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/), um Benutzerattribute nur zu senden, wenn sich Werte geändert haben. Siehe die Dokumentation von Tealium über [Anreicherungsregeln](https://docs.tealium.com/server-side-connectors/braze-connector/).

#### Senden von irrelevanten Daten oder unnötiges Überschreiben von Daten

Wenn Sie mehrere EventStreams haben, die auf denselben Event-Feed abzielen, werden **alle für diesen Connector aktivierten Aktionen** automatisch ausgelöst, sobald eine einzelne Aktion ausgelöst wird. \*\*Dies könnte auch dazu führen, dass Daten in Braze überschrieben werden und unnötige Datenpunkte verbraucht werden.

**Lösung**: <br>Richten Sie eine separate Ereignisspezifikation oder einen Feed ein, um jede Aktion zu verfolgen. <br>**ODER**<br> Deaktivieren Sie Aktionen (oder Verbindungen), die Sie nicht auslösen möchten, indem Sie die Kippschalter im Tealium-Dashboard verwenden.

#### Braze zu früh initialisieren

Benutzer, die Tealium mit dem Braze Web SDK-Tag integrieren, können einen dramatischen Anstieg ihrer MAU verzeichnen. **Wenn Braze beim Laden der Seite initialisiert wird, erstellt Braze jedes Mal ein anonymes Profil, wenn ein Webbenutzer zum ersten Mal auf die Website zugreift.** Manche möchten das Nutzerverhalten nur dann verfolgen, wenn die Nutzer eine Aktion abgeschlossen haben, wie z. B. "Angemeldet" oder "Video angesehen", um ihre MAU-Zahl zu senken.

**Lösung**: <br>Legen Sie [Lastregeln](https://docs.tealium.com/iq-tag-management/load-rules/about/) fest, um genau zu bestimmen, wann und wo ein Tag auf Ihrer Website geladen wird. 

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[5]: {% image_buster /assets/img/tealium/braze_connector_marketplace.png %}
[6]: {% image_buster /assets/img/tealium/data_source.png %}
[7]: {% image_buster /assets/img/tealium/event_specs.png %}
[8]: {% image_buster /assets/img/tealium/get_code.png %}
[9]: {% image_buster /assets/img/tealium/summary.png %}
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[13]: {% image_buster /assets/img/tealium/summary_list.png %}
[15]: {% image_buster /assets/img/tealium/create_configuration.png %}
[16]: {% image_buster /assets/img/tealium/connector_summary.png %}
[17]: {% image_buster /assets/img/tealium/save_publish.png %}
[18]: {% image_buster /assets/img/tealium/braze_connection.png %}
[19]: https://docs.tealium.com/iq-tag-management/events/about/
[21]: https://docs.tealium.com/server-side/connectors/trace/about/
[22]: {% image_buster /assets/img/tealium/tealium_overview.png %}
[23]: {% image_buster /assets/img/tealium/remote_mappings.png %}
