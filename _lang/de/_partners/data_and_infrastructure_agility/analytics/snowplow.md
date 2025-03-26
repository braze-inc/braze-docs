---
nav_title: Schneepflug
article_title: Schneepflug
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Snowplow, einer Open-Source-Datenerfassungsplattform, die es Ihnen ermöglicht, Snowplow-Ereignisse über das serverseitige Google Tag Manager-Tagging an Braze weiterzuleiten."
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Schneepflug

> [Snowplow][1] ist eine skalierbare Open-Source-Plattform für eine umfangreiche, qualitativ hochwertige Datenerfassung mit niedriger Latenz. Es wurde entwickelt, um hochwertige, vollständige Verhaltensdaten für Unternehmen zu sammeln.

Die Integration von Braze und Snowplow ermöglicht es Benutzern, Snowplow-Ereignisse über das serverseitige Tagging von Google Tag Manager an Braze weiterzuleiten. Das Snowplow Braze-Tag ermöglicht es Ihnen, Ereignisse an Braze zu senden und bietet gleichzeitig zusätzliche Flexibilität und Kontrolle:
- Vollständiger Einblick in alle Datentransformationen
- Die Fähigkeit, sich im Laufe der Zeit weiterzuentwickeln
- Alle Daten bleiben in Ihrer privaten Cloud, bis Sie sie weiterleiten möchten.
- Einfache Einrichtung durch umfangreiche Tag-Bibliotheken und die vertraute Google Tag Manager-Benutzeroberfläche

Nutzen Sie die umfangreichen Verhaltensdaten von Snowplow, um leistungsstarke kundenorientierte Interaktionen in Braze voranzutreiben und personalisierte Nachrichten in Echtzeit zu versenden.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Schneepflug-Pipeline | Eine Schneepflug-Pipeline muss eingerichtet und in Betrieb sein. |
| Google Tag Manager auf der Server-Seite | GTM-SS muss bereitgestellt und der [Snowplow-Client für GTM-SS][2] eingerichtet werden. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][3]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

### Personalisierte, handlungsorientierte Bereitstellung
Verwenden Sie eines der zahlreichen Ereignisse, die Snowplow standardmäßig sammelt, oder definieren Sie Ihre eigenen Ereignisse, um noch detailliertere Customer Journeys zu gestalten, die für Ihr Unternehmen sinnvoll sind. Nutzen Sie die reichhaltigen Verhaltensdaten von Snowplow, um Kundentrichter zu entwerfen und einen Mehrwert für Ihre Marketing- und Produktteams zu schaffen, damit diese die Konversion und Produktnutzung durch Braze maximieren können.

### Dynamische Segmentierung
Erstellen Sie in Braze dynamische Zielgruppen auf der Grundlage der hochwertigen Verhaltensdaten von Snowplow: Wenn Benutzer in Ihrem Produkt, Ihrer App oder Ihrer Website Aktionen ausführen, können Sie die Echtzeit-Verhaltensdaten, die Snowplow sammelt, nutzen, um Benutzer automatisch zu den relevanten Segmenten in Braze hinzuzufügen oder zu entfernen.

## Integration

### Schritt 1: Installation der Vorlage

#### Manuelle Installation

1. Laden Sie die [`template.tpl`][7] Vorlage-Datei.
2. Erstellen Sie ein neues Tag im Bereich **Vorlagen** eines Google Tag Manager Server-Containers.
3. Klicken Sie auf das Menü **Weitere Aktionen** in der oberen rechten Ecke und wählen Sie **Importieren**.
4. Importieren Sie Ihre heruntergeladene Vorlagendatei und speichern Sie sie.

#### Tag Manager Galerie

Demnächst verfügbar! Dieser Tag muss noch genehmigt werden, um in die GTM-Galerie aufgenommen zu werden.

### Schritt 2: Einrichtung der Lötfahne

Wenn die Vorlage installiert ist, fügen Sie das Braze-Tag zu Ihrem GTM-SS-Container hinzu.

1. Wählen Sie auf der Registerkarte **Tag** die Option **Neu** und wählen Sie dann das **Braze Tag** als Ihre Tag-Konfiguration.
2. Wählen Sie den gewünschten Auslöser für die Ereignisse, die Sie an Braze weiterleiten möchten.
3. Geben Sie die erforderlichen Parameter ein und konfigurieren Sie Ihr Tag (weitere Einzelheiten finden Sie im folgenden Abschnitt Anpassung).
4. Klicken Sie auf **Speichern**.

## Anpassung

### Erforderliche Tag-Parameter

In der folgenden Tabelle finden Sie die erforderlichen Tag-Parameter, die Sie bei der Einrichtung Ihres Braze-Tags angeben müssen.

| Parameter | Beschreibung |
| --------- | ----------- |
| Braze REST API Endpunkt | Setzen Sie dies auf die URL Ihres Braze [REST-Endpunkts][3]. |
| Braze API-Schlüssel | Setzen Sie hier Ihren [Braze-API-Schlüssel][4] ein, der in jeder Anfrage enthalten sein wird. |
| Löten `external_id` | Setzen Sie diesen Schlüssel auf die Client-Event-Eigenschaft, die der `external_id` Ihrer Benutzer entspricht und als [Braze-Benutzerkennung][5] verwendet wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Ereignis-Mapping

In der folgenden Tabelle sind die Optionen für die Zuordnung von Ereignissen zum Ereignis Snowplow aufgeführt, die vom [Snowplow-Client][2] beansprucht werden.

| Mapping-Option | Beschreibung |
| --------- | ----------- |
| Selbstbeschreibendes Ereignis einbeziehen | Ist standardmäßig aktiviert. Gibt an, ob die selbstbeschreibenden Ereignisdaten von Snowplow in die an Braze gesendeten Eigenschaftsobjekte des Ereignisses aufgenommen werden sollen. |
| Kontextregeln für Schneepflug-Ereignisse | Beschreibt, wie das Braze-Tag die mit einem Snowplow-Ereignis verbundenen Kontextentitäten verwendet. |
| Entität aus Array extrahieren, wenn einzelnes Element | Schneepflug-Entitäten befinden sich immer in Arrays, da mehrere der gleichen Entität an ein Ereignis angehängt werden können. Diese Option wählt das einzelne Element aus dem Array aus, wenn das Array nur ein einziges Element enthält. |
| Alle Entitäten in das Ereignisobjekt einbeziehen | Ist standardmäßig aktiviert. Schließt alle Entitäten eines Ereignisses in das Objekt Eigenschaften des Braze-Ereignisses ein. Deaktivieren Sie diese Option, um einzelne Entitäten für die Aufnahme auszuwählen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erweiterte Ereigniszuordnung

#### Regeln für Ereigniseigenschaften

Wenn Sie andere Eigenschaften aus dem Client-Ereignis einbeziehen und sie dem Braze-Ereignis zuordnen möchten, beziehen Sie sich auf die Regeln in der folgenden Tabelle: 

| Regeln für Ereigniseigenschaften | Beschreibung |
| --------- | ----------- |
| Gemeinsame Ereigniseigenschaften einbeziehen | Diese Option ist standardmäßig aktiviert und legt fest, ob die Ereigniseigenschaften aus der [allgemeinen Ereignisdefinition][6] automatisch in die Eigenschaften des Braze-Ereignisses aufgenommen werden sollen. |
| Zusätzliche Zuordnungsregeln für Benutzereigenschaften und Ereigniseigenschaften | Geben Sie den Eigenschaftsschlüssel aus dem Client-Ereignis und den Objektschlüssel der Eigenschaften an, die Sie zuordnen möchten (oder lassen Sie den zugeordneten Schlüssel leer, um denselben Namen beizubehalten). Sie können hier eine Schlüsselpfad-Notation verwenden (z.B. `x-sp-tp2.p` für eine Snowplow-Ereignisplattform oder `x-sp-contexts.com_snowplowanalytics_snowplow_web_page_1.0.id` für eine Snowplow-Ereignis-Seitenansicht-ID (in Array-Index 0) oder Sie wählen Eigenschaften, die nicht von Snowplow stammen, wenn Sie einen alternativen Client verwenden.<br><br>Regeln für die Zuordnung von Ereigniseigenschaften füllen das Objekt Braze-Ereigniseigenschaften.|
| Gemeinsame Benutzereigenschaften einbeziehen| Diese Option ist standardmäßig aktiviert und legt fest, ob die Eigenschaften `user_data` aus der allgemeinen Ereignisdefinition in das Objekt Braze Benutzerattribute aufgenommen werden sollen.|
| Eigenschaft Ereigniszeit | Mit dieser Option können Sie die Client-Ereignis-Eigenschaft angeben, um die Ereigniszeit (im ISO-8601-Format) zu füllen, oder sie leer lassen, um die aktuelle Zeit zu verwenden (Standardverhalten). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Entitätszuordnung

Mithilfe der Snowplow-Entitätentabelle können die Entitäten in Braze auf andere Namen umgeschrieben und in Ereigniseigenschaften oder Benutzerattribute aufgenommen werden. 

Die Entität kann in zwei verschiedenen Formaten angegeben werden:
- Hauptversionsübereinstimmung: `x-sp-contexts_com_snowplowanalytics_snowplow_web_page_1` wobei `com_snowplowanalytics_snowplow` für den Ereignisanbieter, `web_page` für den Schemanamen und `1` für die Hauptversionsnummer steht. `x-sp-` kann auch weggelassen werden, falls gewünscht.
- Vollständige Schemaübereinstimmung: `iglu:com.snowplowanalytics.snowplow/webPage/jsonschema/1-0-0`
<br><br>

| Option Entitätszuordnung | Beschreibung |
| --------- | ----------- |
| Nicht zugeordnete Objekte in Ereignis einbeziehen | Wenn Sie mit der vorangegangenen Anpassung einige Entitäten neu zuordnen oder in Benutzerattribute verschieben, können Sie mit dieser Option sicherstellen, dass alle nicht zugeordneten Entitäten (z.B. alle Entitäten, die nicht in den [Eigenschaftsregeln des Ereignisses](#event-property-rules) gefunden werden) in das Eigenschaftsobjekt des Braze-Ereignisses aufgenommen werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[1]: https://snowplowanalytics.com
[2]: https://docs.snowplowanalytics.com/docs/forwarding-events-to-destinations/forwarding-events/google-tag-manager-server-side/snowplow-client-for-gtm-ss/
[3]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[4]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[5]: {{site.baseurl}}/developer_guide/rest_api/basics/#external-user-id-explanation
[6]: https://developers.google.com/tag-platform/tag-manager/server-side/common-event-data
[7]: https://github.com/snowplow/snowplow-gtm-server-side-braze-tag/blob/main/template.tpl
