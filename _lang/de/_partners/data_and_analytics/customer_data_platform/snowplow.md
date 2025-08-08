---
nav_title: Snowplow
article_title: Snowplow
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Snowplow, einer Plattform für die Datenerfassung mit offenem Quellcode, die es Ihnen erlaubt, Snowplow-Ereignisse über das Server-seitige Tagging des Google Tag Managers an Braze weiterzuleiten."
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> [Snowplow](https://snowplowanalytics.com) ist eine skalierbare Open-Source-Plattform für eine umfangreiche, qualitativ hochwertige Datenerfassung mit geringer Latenz. Es wurde entwickelt, um hochwertige, vollständige Verhaltensdaten für Unternehmen zu sammeln.

_Diese Integration wird von Snowplow gepflegt._

## Über die Integration

Die Integration von Braze und Snowplow ermöglicht es Nutzern:innen, Snowplow-Ereignisse über Google Tag Manager Server-seitiges Tagging an Braze weiterzuleiten. Der Snowplow Braze Tag erlaubt es Ihnen, Ereignisse an Braze zu senden und bietet gleichzeitig zusätzliche Flexibilität und Kontrolle:
- Vollständiger Einblick in alle Transformationen der Daten
- Die Fähigkeit, sich im Laufe der Zeit weiterzuentwickeln
- Alle Daten verbleiben in Ihrer privaten Cloud, bis Sie sie weiterleiten möchten.
- Einfache Einrichtung dank umfangreicher Bibliotheken mit Tags und vertrauter Google Tag Manager:in UI

Nutzen Sie die umfangreichen Verhaltensdaten von Snowplow, um leistungsstarke kundenorientierte Interaktionen in Braze voranzutreiben und personalisierte Nachrichten in Realtime zugestellt zu bekommen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Schneepflug-Pipeline | Eine Schneepflug-Pipeline muss eingerichtet und in Betrieb sein. |
| Google Tag Manager:in auf der Server-Seite | GTM-SS muss bereitgestellt und der [Snowplow Client für GTM-SS](https://docs.snowplowanalytics.com/docs/forwarding-events-to-destinations/forwarding-events/google-tag-manager-server-side/snowplow-client-for-gtm-ss/) muss eingerichtet werden. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

### Personalisierte, aktionsbasierte Zustellung
Verwenden Sie eines der zahlreichen Ereignisse, die Snowplow standardmäßig sammelt, oder definieren Sie angepasste Events, um noch detailliertere Customer Journeys zu gestalten, die für Ihr Unternehmen sinnvoll sind. Nutzen Sie die reichhaltigen Verhaltensdaten von Snowplow, um Funnels für Kunden zu entwerfen und Ihren Marketing- und Produkt-Teams dabei zu helfen, Konversion und Produktnutzung durch Braze zu maximieren.

### Dynamische Segmentierung
Erstellen Sie dynamische Zielgruppen in Braze auf der Grundlage der hochwertigen Verhaltensdaten von Snowplow: Wenn Nutzer:innen in Ihrem Produkt, Ihrer App oder Ihrer Website Aktionen durchführen, können Sie die von Snowplow in Echtzeit erfassten Verhaltensdaten nutzen, um Nutzer:innen automatisch zu relevanten Segmenten in Braze hinzuzufügen oder zu entfernen.

## Integration

### Schritt 1: Template-Installation

#### Manuelle Installation

1. Laden Sie die [`template.tpl`](https://github.com/snowplow/snowplow-gtm-server-side-braze-tag/blob/main/template.tpl) Template-Datei herunter.
2. Erstellen Sie einen neuen Tag im Bereich **Templates** eines Google Tag Manager Server Containers.
3. Klicken Sie auf das Menü **Weitere Aktionen** in der oberen rechten Ecke und wählen Sie **Importieren**.
4. Importieren Sie Ihre heruntergeladene Template-Datei und speichern Sie sie.

#### Tag Manager:in der Galerie

Demnächst verfügbar! Dieser Tag muss noch genehmigt werden, um in die GTM-Galerie aufgenommen zu werden.

### Schritt 2: Braze Tag einrichten

Wenn Sie das Template installiert haben, fügen Sie den Braze Tag zu Ihrem GTM-SS Container hinzu.

1. Wählen Sie auf dem Tab **Tag** die Option **Neu** und wählen Sie dann den **Braze Tag** als Ihre Tag-Konfiguration aus.
2. Wählen Sie den gewünschten Auslöser für die Ereignisse aus, die Sie an Braze weiterleiten möchten.
3. Geben Sie die erforderlichen Parameter ein und konfigurieren Sie Ihren Tag (weitere Einzelheiten finden Sie im folgenden Abschnitt Anpassung).
4. Klicken Sie auf **Speichern**.

## Anpassung

### Erforderliche Tag-Parameter

In der folgenden Tabelle finden Sie die erforderlichen Tag-Parameter, die Sie in die Einrichtung Ihrer Braze Tags aufnehmen müssen.

| Parameter | Beschreibung |
| --------- | ----------- |
| Braze REST API Endpunkt | Setzen Sie dies auf die URL Ihres Braze REST [Endpunktes]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
| Braze API-Schlüssel | Setzen Sie hier Ihren Braze [API-Schlüssel]({{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys) ein, der in jeder Anfrage enthalten sein wird. |
| Braze `external_id` | Setzen Sie diesen Schlüssel auf die Eigenschaft des Client-Ereignisses, das der `external_id` Ihrer Nutzer:innen entspricht und als [Bezeichner der Braze-Benutzer]({{site.baseurl}}/developer_guide/rest_api/basics/#external-user-id-explanation):innen verwendet wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Abbildung von Ereignissen

In der folgenden Tabelle sind die Optionen für die Abbildung von Ereignissen in Bezug auf das Ereignis Snowplow aufgeführt, das vom [Snowplow Client](https://docs.snowplowanalytics.com/docs/forwarding-events-to-destinations/forwarding-events/google-tag-manager-server-side/snowplow-client-for-gtm-ss/) beansprucht wird.

| Option Abbildung | Beschreibung |
| --------- | ----------- |
| Selbstbeschreibendes Ereignis einbeziehen | Standardmäßig aktiviert. Gibt an, ob die selbstbeschreibenden Daten von Snowplow in die an Braze gesendeten Eigenschaften des Ereignisses aufgenommen werden sollen. |
| Kontextregeln für Schneepflug-Ereignisse | Beschreibt, wie das Braze Tag die mit einem Snowplow-Ereignis verbundenen Kontext-Entitäten verwendet. |
| Entität aus Array extrahieren, wenn einzelnes Element | Schneepflug-Entitäten befinden sich immer in Arrays, da mehrere der gleichen Entität an ein Ereignis angehängt werden können. Diese Option wählt das einzelne Element aus dem Array aus, wenn das Array nur ein einziges Element enthält. |
| Alle Entitäten in das Ereignisobjekt einbeziehen | Standardmäßig aktiviert. Schließt alle Entitäten eines Ereignisses in das Objekt Eigenschaften des Braze-Ereignisses ein. Deaktivieren Sie diese Option, um einzelne Entitäten für die Aufnahme auszuwählen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Fortgeschrittene Abbildung von Ereignissen

#### Regeln für Event-Eigenschaften

Wenn Sie andere Eigenschaften aus dem Client-Ereignis aufnehmen und auf das Braze-Ereignis abbilden möchten, referenzieren Sie die Regeln in der folgenden Tabelle: 

| Regeln für Event-Eigenschaften | Beschreibung |
| --------- | ----------- |
| Gemeinsame Event-Eigenschaften einbeziehen | Standardmäßig aktiviert, legt diese Option fest, ob die Event-Eigenschaften aus der [gemeinsamen Event-Definition](https://developers.google.com/tag-platform/tag-manager/server-side/common-event-data) automatisch in die Eigenschaften des Braze-Events aufgenommen werden sollen. |
| Zusätzliche Regeln für die Abbildung von Nutzer:innen- und Event-Eigenschaften | Geben Sie den Schlüssel der Eigenschaft aus dem Client-Ereignis und den Objektschlüssel der Eigenschaften an, auf den Sie ihn abbilden möchten (oder lassen Sie den abgebildeten Schlüssel leer, um denselben Namen zu behalten). Sie können hier eine Schlüsselpfad-Notation verwenden (z.B. `x-sp-tp2.p` für eine Snowplow Event-Plattform oder `x-sp-contexts.com_snowplowanalytics_snowplow_web_page_1.0.id` für eine Snowplow Event-Seitenansicht-ID (in Array-Index 0) oder Eigenschaften wählen, die nicht von Snowplow stammen, wenn Sie einen anderen Client verwenden.<br><br>Regeln für die Abbildung von Event-Eigenschaften füllen das Braze Event-Eigenschaften Objekt.|
| Gemeinsame Nutzer:in-Eigenschaften einbeziehen| Diese Option ist standardmäßig aktiviert und legt fest, ob die Eigenschaften von `user_data` aus der gemeinsamen Event-Definition in das Objekt Nutzer:in aufgenommen werden sollen.|
| Eigenschaft "Ereigniszeit | Mit dieser Option können Sie die Eigenschaft des Client-Ereignisses angeben, um die Ereigniszeit (im ISO-8601-Format) zu füllen, oder sie leer lassen, um die aktuelle Zeit zu verwenden (Standardverhalten). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Abbildung der Entität

Mithilfe der Abbildungstabelle für Snowplow-Entitäten können die Entitäten in Braze umbenannt und in Event-Eigenschaften oder Nutzer:innen-Attribute aufgenommen werden. 

Die Entität kann in zwei verschiedenen Formaten angegeben werden:
- Hauptversionsübereinstimmung: `x-sp-contexts_com_snowplowanalytics_snowplow_web_page_1` wobei `com_snowplowanalytics_snowplow` für den Ereignisanbieter, `web_page` für den Schemanamen und `1` für die Hauptversionsnummer steht. `x-sp-` kann auch weggelassen werden, falls gewünscht.
- Vollständige Schemaübereinstimmung: `iglu:com.snowplowanalytics.snowplow/webPage/jsonschema/1-0-0`
<br><br>

| Option für die Abbildung von Entitäten | Beschreibung |
| --------- | ----------- |
| Nicht zugeordnete Objekte in Ereignis einbeziehen | Bei der Neuzuordnung oder dem Verschieben einiger Entitäten zu Nutzer:in-Attributen mit der vorangegangenen Anpassung können Sie mit dieser Option sicherstellen, dass alle nicht zugeordneten Entitäten (z.B. alle Entitäten, die nicht in den [Regeln für die Event-Eigenschaften](#event-property-rules) gefunden wurden) in das Objekt Eigenschaften des Braze-Events aufgenommen werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


