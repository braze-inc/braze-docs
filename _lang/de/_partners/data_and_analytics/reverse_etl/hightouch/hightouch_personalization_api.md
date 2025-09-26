---
nav_title: Hightouch Personalisierung API
article_title: Hightouch Personalisierung API
description: "Dieser referenzierte Artikel beschreibt die Integration zwischen der Personalisierungs-API von Braze und Hightouch, einem verwalteten Dienst für das Hosting einer Daten-API mit niedriger Latenz, die auf einem beliebigen Datensatz innerhalb Ihres Data Warehouse in der Cloud basiert. Dieser referenzierte Artikel beschreibt die Anwendungsfälle, für die die Hightouch Personalization API geeignet ist, die Daten, mit denen sie arbeitet, die Konfiguration und die Integration mit Braze."
page_type: partner
search_tag: Partner
---

# Hightouch Personalisierung API

> Die [Personalisierung API](https://hightouch.com/docs/destinations/personalization-api) von Hightouch ist ein verwalteter Dienst, mit dem Sie eine Daten-API mit niedriger Latenz hosten können, die auf jedem Datensatz in Ihrem Data Warehouse in der Cloud basiert.

![]({% image_buster /assets/img/hightouch/cohort7.png %})

Die Integration von Braze und Hightouch ermöglicht es Ihnen, die API mit [Braze Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) zu nutzen, um aktuelle Kundendaten oder Objektdaten zum Zeitpunkt des Versands in Ihre Kampagnen oder Canvase zu ziehen.

Die Personalisierung API von Hightouch bietet einen REST-Endpunkt zur Verwendung innerhalb Ihrer Braze-Konfiguration. Konkret können Sie das Braze Connected-Content-Angebot nutzen, um eine GET-Anfrage an die Personalisierungs-API zu stellen, um alle Informationen zu einem bestimmten Bezeichner abzurufen. Die von dieser API bereitgestellten Daten können Kunden-, Produkt- oder andere Objektdaten darstellen. 

![]({% image_buster /assets/img/hightouch/cohort6.png %})

## Voraussetzungen

| Anforderung| Beschreibung|
| ---| ---| 
| [Hightouch-Konto](https://app.hightouch.com/login) mit Enablement der Personalisierung API | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Hightouch [Business Tier-Konto](https://hightouch.com/pricing).|
| Definierte Anwendungsfälle | Bevor Sie die API einrichten, müssen Sie Ihren Anwendungsfall für diese Integration festlegen. Referenzieren Sie die folgende Liste für gängige Anwendungsfälle. |
| In einem Cloud Data Warehouse oder einer anderen Datenquelle gespeicherte Daten | Hightouch integriert sich in [mehr als 25 Datenquellen](https://hightouch.com/integrations) |
| Hightouch API-Schlüssel | Dieser kann unter **Hightouch > Einstellungen > API-Schlüssel > API-Schlüssel hinzufügen** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs %}
{% tab Anwendungsfälle %}

### Anwendungsfälle

Bevor Sie beginnen, sollten Sie genau planen, wie Sie die Personalisierung API verwenden möchten.

Zu den üblichen Anwendungsfällen gehören:
- **Produktempfehlungen** zur Optimierung der Einbettung personalisierter Produktempfehlungen in E-Mail-Templates, Kampagnen oder App-Erlebnisse
- **Personalisierte Marketing Kampagnen** durch Anreicherung von Marketing Touchpoints mit dynamischen Produktempfehlungen
- **Personalisierung in der App oder im Internet**, z. B. angepasste Suchergebnisse, kohortenbasierte Preisgestaltung und Messaging, Artikelempfehlungen oder Standorte in der Nähe des Shops
- **Empfehlungen, die auf finanziellen oder medizinischen Daten basieren - finanzielle**Daten unterliegen strengen Anforderungen, die Hightouch durch seine [strengen Richtlinien zur Datensicherheit](https://hightouch.com/docs/security/overview#compliance) erfüllt. Mit Hightouch können Sie Kundensegmente auf der Grundlage finanzieller oder medizinischer Daten erstellen, ohne die zugrundeliegenden Attribute offenzulegen, die in Ihren Segmentierungskriterien verwendet werden.

{% endtab %}
{% tab Datensätze %}

### Datensätze

Die Personalisierung API fungiert als Cache für ausgewählte Daten in Ihrem Shop, so dass Sie die Empfehlungsdaten bereits dort gespeichert haben sollten. Sie können Hightouch verwenden, um sie bei Bedarf nach einem Template zu transformieren. Zu dieser Art von Daten gehören:
- Nutzer:innen-Metadaten wie geografische Region, Alter oder andere demografische Informationen
- Nutzer:innen-Aktionen oder -Ereignisse, einschließlich früherer Käufe, Seitenaufrufe, Klicks, usw.

{% endtab %}
{% endtabs %}

## Integration

### Schritt 1: Datenquelle mit Hightouch verbinden

[Hightouch-Quellen](https://hightouch.com/docs/getting-started/concepts#sources) sind der Ort, an dem die Geschäftsdaten Ihres Unternehmens gespeichert sind. In diesem Fall ist es der Ort, an dem Ihre Nutzer:innen-Daten gespeichert sind.
1. Gehen Sie in Hightouch zu **Übersicht der Quellen > Quelle hinzufügen**. Wählen Sie Ihr Data Warehouse als Quelle aus.<br><br>
2. Geben Sie die entsprechenden Zugangsdaten ein; diese sind je nach Quelle unterschiedlich. 

Weitere Einzelheiten entnehmen Sie bitte der entsprechenden [Dokumentation](https://hightouch.com/docs).

### Schritt 2: Daten zum Modell

Hightouch-Modelle definieren, welche Daten aus Ihrer Quelle gezogen werden sollen. Um ein neues Modell einzurichten, gehen Sie folgendermaßen vor:

1. Gehen Sie in Hightouch zu [**Übersicht der Modelle**](https://app.hightouch.com/models) > **Modell hinzufügen**, und wählen Sie die Quelle aus, die Sie gerade verbunden haben. <br><br>
2. Wählen Sie als nächstes eine [Modellierungsmethode](https://hightouch.com/docs/models/creating-models). Da alle Ihre Informationen in einer Tabelle zusammengefasst werden sollen, können Sie den visuellen Tabellenselektor verwenden, um diese zu definieren. Alternativ können Sie auch SQL schreiben, um nur die gewünschten Spalten einzubeziehen, oder sich auf Ihre vorhandenen dbt-Modelle, Looker Looks oder Sigma-Arbeitsmappen verlassen.<br><br>
3. Bevor Sie fortfahren, sollten Sie eine Vorschau Ihres Modells anzeigen, um sicherzustellen, dass es die Daten abfragt, an denen Sie interessiert sind. Standardmäßig beschränkt Braze die Vorschau auf die ersten 100 Datensätze. Nachdem Sie Ihre Daten validiert haben, klicken Sie auf **Weiter**.<br><br>
4. Benennen Sie Ihr Modell, zum Beispiel "Nutzer:innen".<br><br>
5. Wählen Sie abschließend einen Primärschlüssel aus und klicken Sie auf **Fertig stellen**. Ein Primärschlüssel sollte eine Spalte mit eindeutigen Bezeichnern sein. Dies ist auch das Feld, über das Sie die Personalisierung API aufrufen, um die Empfehlungen eines bestimmten Nutzer:innen abzurufen.

### Schritt 3: API zur Personalisierung konfigurieren

Das Vorbereiten der API für den Empfang von Anfragen besteht aus zwei Schritten:
- Enablement der Personalisierung API in den Regionen, die Ihrer Infrastruktur am nächsten liegen
- Erstellen von Synchronisierungen, um festzulegen, welche Modelle im von Hightouch verwalteten Cache materialisiert werden sollen

Folgen Sie diesen Anweisungen, um beides auszufüllen:

1. In Hightouch, gehen Sie zu [**Ziele**](https://app.hightouch.com/destinations) und wählen Sie die für Sie erstellte Hightouch Personalisierung API aus. Wenn Sie dieses Ziel nicht aktiviert haben, wenden Sie sich an den [Hightouch Support](mailto:friends@hightouch.com).<br><br>
2. Wählen Sie dann die entsprechende Region aus. Wenn Sie die Region auswählen, die Ihrer Infrastruktur am nächsten liegt, verkürzen sich Ihre Reaktionszeiten. Wenn Sie keine Region in der Nähe Ihrer Infrastruktur sehen, wenden Sie sich an den [Hightouch Support](mailto:friends@hightouch.com).<br><br>
3. Rufen Sie die [Übersichtsseite**Syncs**](https://app.hightouch.com/syncs) auf und klicken Sie auf den Button **Sync hinzufügen**. Wählen Sie dann das entsprechende Modell und das Ziel aus, das Sie zuvor eingerichtet haben.<br><br> 
4. Geben Sie einen alphanumerischen Namen für die Sammlung ein. Sammlungen sind konzeptionell ähnlich wie Datenbanktabellen. Jede sollte einen bestimmten Datentyp repräsentieren, z.B. Kunden oder Rechnungen. Die Sammlungsnamen müssen alphanumerisch sein und werden Teil Ihres Endpunkts der Personalisierung APIs.<br><br>
5. Als nächstes geben Sie an, welche Spalte aus Ihrem Modell als Primärindex für die Datensatzsuche dienen soll. Dieses Feld muss jeden Datensatz in der Sammlung eindeutig identifizieren und ist oft derselbe wie der Primärschlüssel Ihres Modells. Die Personalisierung API unterstützt Abfragen auf mehreren Indizes. Sie könnten zum Beispiel Kundenprofile mit `user_id`, `anonymous_id` oder `email_address` abrufen wollen. Um mehrere Indizes zu aktivieren, wenden Sie sich an den [Hightouch Support](mailto:friends@hightouch.com).<br><br>
6. Verwenden Sie den Feld-Mapper, um festzulegen, welche Spalten aus Ihrem Modell in die API-Antwort-Nutzlast aufgenommen werden sollen. Sie können diese Felder umbenennen und den vorgebrachten Mapper verwenden, um Transformationen mit Hilfe der Liquid Template-Sprache anzuwenden.<br><br>
7. Wählen Sie das passende [Löschverhalten](https://www.hightouch.com/docs/destinations/personalization-api#delete-behavior) für Ihren Anwendungsfall aus.<br><br>
8. Klicken Sie abschließend auf **Weiter** und wählen Sie einen [Zeitplan für die Synchronisierung](https://hightouch.com/docs/syncs/schedule-sync-ui) aus.

Hightouch synchronisiert jetzt die Daten in Ihrem Data Warehouse mit einer verwalteten Datenbank und stellt sie über die Personalisierung API zur Verfügung.

### Schritt 4: Aufruf der Personalisierung API über Braze Connected-Content

Sobald Sie Ihre API-Instanz für die Personalisierung eingerichtet haben, können Sie sie als Endpunkt für Braze Connected-Content verwenden. 

Die API ist unter `https://personalization.{region}.hightouch.com` zugänglich, zum Beispiel unter `https://personalization.us-west-2.hightouch.com`. 

Die Informationen sind über diesen Endpunkt `/v1/collections/:collection_name/records/:index_key/:index_value` verfügbar.

Sie können dieses Snippet zum Beispiel in eine Kampagne oder ein Canvas einfügen:

{% raw %}

```liquid
{% connected_content
     https://personalization.us-west-2.hightouch.com/v1/collections/customer/records/id/12345
     :method get
     :headers {
       "Authorization": "Bearer {{YOUR-API-KEY}}"
  }
     :content_type application/json
     :save customer
%}
```
{% endraw %}

Sie können Liquid Templating verwenden, um die in der JSON-Nutzlast zurückgegebenen Eigenschaften zu referenzieren und sie in Ihrem Messaging zu verwenden.

Für die Beispiel-Nutzlast unten:

```json
{
    "user_id": 12345,
    "full_name": "Jane Doe",
    "lifetime_value": 1492.18,
    "churn_risk": 0.04,
    "90_day_summary": {
        "num_songs_listened": 813,
        "top_genres": [
            "house",
            "techno",
            "ambient"
        ],
        "top_artists": [
            "deadmau5",
            "Marsh",
            "Enamour"
        ],
    },
    "recommendations": {
        "concerts": [
            {
                "artist": "Aphex Twin",
                "location": "San Francisco, CA",
                "event_date": "2023-01-31"
            },
            {
                "artist": "Sultan + Shepard",
                "location": "San Francisco, CA",
                "event_date": "2023-02-25"
            }
        ],
        "upcoming_album_release": {
            "title": "Universal Language",
            "artist": "Simon Doty",
            "label": "Anjunadeep",
            "release_date": "2023-04-28"
        }
    },
}
```

Die folgenden Liquid-Referenzen würden diese Beispieldaten zurückgeben:

| Liquid Template | Zurückgegebenes Beispiel |
| --- | --- |
| {% raw %}`{{artists.recommendations.concerts[0].artist}}`{% endraw %}| Aphex Twin |
| {% raw %}`{{artists.recommendations.concerts[0].location}}`{% endraw %}| San Francisco, CA |
| {% raw %}`{{artists.recommendations.upcoming_album_release.title}}`{% endraw %}| Universelle Sprache |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Fehlersuche

Wenn Sie Fragen haben, wenden Sie sich an den [Hightouch-Support](mailto:friends@hightouch.com), um Hilfe zu erhalten.

