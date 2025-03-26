---
nav_title: Hightouch Personalization API
article_title: Hightouch Personalization API
description: "Dieser Referenzartikel beschreibt die Integration zwischen Braze und der Personalization API von Hightouch, einem verwalteten Service zum Hosten einer Daten-API mit niedriger Latenz, die auf einem beliebigen Datensatz innerhalb Ihres Cloud Data Warehouse basiert. Dieser Referenzartikel beschreibt die Anwendungsfälle, für die die Hightouch Personalization API geeignet ist, die Daten, mit denen sie arbeitet, wie sie konfiguriert wird und wie sie in Braze integriert werden kann."
page_type: partner
search_tag: Partner
---

# Hightouch Personalization API

> Die [Personalization API](https://hightouch.com/docs/destinations/personalization-api) von Hightouch ist ein verwalteter Service, mit dem Sie eine Daten-API mit niedriger Latenz hosten können, die auf einem beliebigen Datensatz in Ihrem Cloud Data Warehouse basiert.

![][3]

Die Integration von Braze und Hightouch ermöglicht es Ihnen, die API mit [Braze Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) zu nutzen, um aktuelle Kunden- oder Objektdaten zum Zeitpunkt des Versands in Ihre Kampagnen oder Canvases zu ziehen.

Die Personalisierungs-API von Hightouch bietet einen REST-Endpunkt zur Verwendung in Ihrer Braze-Konfiguration. Konkret können Sie das Connected Content-Angebot von Braze nutzen, um eine GET-Anfrage an die Personalisierungs-API zu stellen, um alle Informationen zu einer bestimmten Kennung abzurufen. Die von dieser API bereitgestellten Daten können Kunden-, Produkt- oder andere Objektdaten darstellen. 

![][2]

## Voraussetzungen

| Anforderung| Beschreibung|
| ---| ---| 
| [Hightouch-Konto](https://app.hightouch.com/login) mit aktivierter Personalisierungs-API | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Hightouch [Business Tier-Konto](https://hightouch.com/pricing).|
| Definierte Anwendungsfälle | Bevor Sie die API einrichten, müssen Sie Ihren Anwendungsfall für diese Integration festlegen. In der folgenden Liste finden Sie häufige Anwendungsfälle. |
| In einem Cloud Data Warehouse oder einer anderen Quelle gespeicherte Daten | Hightouch lässt sich mit [mehr als 25 Datenquellen](https://hightouch.com/integrations) integrieren |
| Hightouch API-Schlüssel | Dieser kann unter **Hightouch > Einstellungen > API-Schlüssel > API-Schlüssel hinzufügen** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs %}
{% tab Anwendungsfälle %}

### Anwendungsfälle

Bevor Sie beginnen, sollten Sie genau planen, wie Sie die Personalisierungs-API verwenden möchten.

Häufige Anwendungsfälle sind:
- **Produktempfehlungen**, um die Einbettung von personalisierten Produktempfehlungen in E-Mail-Vorlagen, Kampagnen oder In-App-Erlebnisse zu optimieren
- **Personalisierte Marketingkampagnen** durch Anreicherung von Marketing-Touchpoints mit dynamischen Produktempfehlungen
- **Personalisierung in der App oder im Web**, z. B. angepasste Suchergebnisse, kohortenbasierte Preisgestaltung und Nachrichten, Artikelempfehlungen oder Standorte der nächstgelegenen Filiale
- **Empfehlungen auf der Grundlage finanzieller oder medizinischer Daten - für Finanzdaten**gelten strenge Anforderungen, die Hightouch durch seine [strengen Datensicherheitsrichtlinien](https://hightouch.com/docs/security/overview#compliance) erfüllt. Mit Hightouch können Sie Kundensegmente auf der Grundlage finanzieller oder medizinischer Daten erstellen, ohne die zugrundeliegenden Attribute, die Sie für Ihre Segmentierungskriterien verwenden, preiszugeben.

{% endtab %}
{% tab Datensätze %}

### Datensätze

Die Personalisierungs-API fungiert als Cache für ausgewählte Daten in Ihrem Warehouse, so dass Sie die Empfehlungsdaten dort bereits gespeichert haben sollten. Sie können Hightouch verwenden, um es bei Bedarf nach einer Vorlage umzuwandeln. Diese Art von Daten umfasst:
- Benutzer-Metadaten wie geografische Region, Alter oder andere demografische Informationen
- Benutzeraktionen oder Ereignisse, einschließlich früherer Käufe, Seitenaufrufe, Klicks usw.

{% endtab %}
{% endtabs %}

## Integration

### Schritt 1: Datenquelle mit Hightouch verbinden

[Hightouch-Quellen](https://hightouch.com/docs/getting-started/concepts#sources) sind der Ort, an dem die Geschäftsdaten Ihres Unternehmens gespeichert sind. In diesem Fall ist es der Ort, an dem Ihre Benutzerdaten gespeichert sind.
1. Gehen Sie in Hightouch zu **Quellenübersicht > Quelle hinzufügen**. Wählen Sie Ihr Data Warehouse als Quelle.<br><br>
2. Geben Sie die entsprechenden Anmeldedaten ein; diese sind je nach Quelle unterschiedlich. 

Weitere Einzelheiten finden Sie in der entsprechenden [Quelldokumentation](https://hightouch.com/docs).

### Schritt 2: Modelldaten

Hightouch-Modelle definieren, welche Daten aus Ihrer Quelle gezogen werden sollen. Um ein neues Modell einzurichten, gehen Sie folgendermaßen vor:

1. In Hightouch gehen Sie zu [**Übersicht Modelle**](https://app.hightouch.com/models) > **Modell hinzufügen** und wählen Sie die Quelle, die Sie gerade verbunden haben. <br><br>
2. Wählen Sie als nächstes eine [Modellierungsmethode](https://hightouch.com/docs/models/creating-models). Da alle Ihre Informationen in einer Tabelle zusammengefasst werden sollen, können Sie den visuellen Tabellenselektor verwenden, um diese zu definieren. Alternativ können Sie SQL schreiben, um nur die gewünschten Spalten einzubeziehen, oder sich auf Ihre vorhandenen dbt-Modelle, Looker Looks oder Sigma-Arbeitsmappen verlassen.<br><br>
3. Bevor Sie fortfahren, sollten Sie eine Vorschau Ihres Modells anzeigen, um sicherzustellen, dass es die Daten abfragt, an denen Sie interessiert sind. Braze beschränkt die Vorschau standardmäßig auf die ersten 100 Datensätze. Nachdem Sie Ihre Daten überprüft haben, klicken Sie auf **Weiter**.<br><br>
4. Benennen Sie Ihr Modell, zum Beispiel "Benutzerempfehlungen".<br><br>
5. Wählen Sie abschließend einen Primärschlüssel aus und klicken Sie auf **Fertig stellen**. Ein Primärschlüssel sollte eine Spalte mit eindeutigen Bezeichnern sein. Dies ist auch das Feld, das Sie verwenden werden, um die Personalisierungs-API aufzurufen, um die Empfehlungen eines bestimmten Benutzers abzurufen.

### Schritt 3: Konfigurieren Sie die Personalisierungs-API

Das Vorbereiten der API für den Empfang von Anfragen umfasst zwei Schritte:
- Aktivieren Sie die Personalisierungs-API in den Regionen, die Ihrer Infrastruktur am nächsten liegen.
- Erstellen von Synchronisierungen, um festzulegen, welche Modelle im von Hightouch verwalteten Cache materialisiert werden sollen

Folgen Sie diesen Anweisungen, um beides auszufüllen:

1. In Hightouch, gehen Sie zu [**Ziele**](https://app.hightouch.com/destinations) und wählen Sie die für Sie erstellte Hightouch-Personalisierungs-API. Wenn Sie dieses Ziel nicht aktiviert haben, wenden Sie sich an den [Hightouch-Support](mailto:friends@hightouch.com).<br><br>
2. Wählen Sie dann die entsprechende Region aus. Wenn Sie die Region auswählen, die Ihrer Infrastruktur am nächsten liegt, verkürzen sich Ihre Reaktionszeiten. Wenn Sie keine Region in der Nähe Ihrer Infrastruktur sehen, wenden Sie sich an den [Hightouch-Support](mailto:friends@hightouch.com).<br><br>
3. Gehen Sie zur [Übersichtsseite**Syncs**](https://app.hightouch.com/syncs) und klicken Sie auf die Schaltfläche **Sync hinzufügen**. Wählen Sie dann das entsprechende Modell und das Ziel, das Sie zuvor eingerichtet haben.<br><br> 
4. Geben Sie einen alphanumerischen Namen für die Sammlung ein. Sammlungen sind konzeptionell ähnlich wie Datenbanktabellen. Jede sollte einen bestimmten Datentyp repräsentieren, z. B. Kunden oder Rechnungen. Sammlungsnamen müssen alphanumerisch sein und werden Teil Ihres Personalisierungs-API-Endpunkts.<br><br>
5. Als nächstes geben Sie an, welche Spalte aus Ihrem Modell als Primärindex für die Datensatzsuche dienen soll. Dieses Feld muss jeden Datensatz in der Sammlung eindeutig identifizieren und ist oft derselbe wie der Primärschlüssel Ihres Modells. Die Personalisierungs-API unterstützt Abfragen auf mehreren Indizes. Sie könnten zum Beispiel Kundenprofile über `user_id`, `anonymous_id` oder `email_address` abrufen wollen. Um mehrere Indizes zu aktivieren, wenden Sie sich an den [Hightouch-Support](mailto:friends@hightouch.com).<br><br>
6. Verwenden Sie den Feld-Mapper, um festzulegen, welche Spalten aus Ihrem Modell in die API-Antwort-Nutzdaten aufgenommen werden sollen. Sie können diese Felder umbenennen und den erweiterten Mapper verwenden, um Transformationen mithilfe der Liquid-Vorlagensprache anzuwenden.<br><br>
7. Wählen Sie das passende [Löschverhalten](https://www.hightouch.com/docs/destinations/personalization-api#delete-behavior) für Ihren Anwendungsfall.<br><br>
8. Klicken Sie abschließend auf **Weiter** und wählen Sie einen [Synchronisierungszeitplan](https://hightouch.com/docs/syncs/schedule-sync-ui) aus.

Hightouch synchronisiert nun die Daten in Ihrem Warehouse mit einer verwalteten Datenbank und stellt sie über die Personalization API zur Verfügung.

### Schritt 4: Aufruf der Personalisierungs-API über Braze Connected Content

Sobald Sie Ihre Personalisierungs-API-Instanz eingerichtet haben, können Sie sie als Endpunkt für Braze Connected Content verwenden. 

Die API ist unter `https://personalization.{region}.hightouch.com` zugänglich, zum Beispiel unter `https://personalization.us-west-2.hightouch.com`. 

Die Informationen sind über diesen Endpunkt `/v1/collections/:collection_name/records/:index_key/:index_value` verfügbar.

Sie könnten zum Beispiel diesen Ausschnitt in eine Kampagne oder ein Canvas einfügen:

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

Sie können Liquid Templating verwenden, um auf die in der JSON-Nutzlast zurückgegebenen Eigenschaften zu verweisen und sie in Ihren Nachrichten zu verwenden.

Für die Beispiel-Nutzdaten unten:

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

| Flüssige Vorlage | Zurückgegebenes Beispiel |
| --- | --- |
| {% raw %}`{{artists.recommendations.concerts[0].artist}}`{% endraw %}| Aphex Twin |
| {% raw %}`{{artists.recommendations.concerts[0].location}}`{% endraw %}| San Francisco, CA |
| {% raw %}`{{artists.recommendations.upcoming_album_release.title}}`{% endraw %}| Universelle Sprache |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Fehlersuche

Wenn Sie Fragen haben, wenden Sie sich an den [Hightouch-Support](mailto:friends@hightouch.com), um Hilfe zu erhalten.

[1]: {% image_buster /assets/img/hightouch/cohort5.png %}
[2]: {% image_buster /assets/img/hightouch/cohort6.png %}  
[3]: {% image_buster /assets/img/hightouch/cohort7.png %}  
