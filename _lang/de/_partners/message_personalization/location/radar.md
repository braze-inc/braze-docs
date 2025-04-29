---
nav_title: Radar
article_title: Radar
alias: /partners/radar/
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Radar, einer Geofencing-Plattform, um Ihre iOS- und Android-Apps um Standort-Kontext und Tracking zu erweitern."
page_type: partner
search_tag: Partner

---

# Radar

> [Radar](https://www.onradar.com/) ist die führende Plattform für Geoofencing und Standort-Tracking. Die Radar-Plattform besteht aus drei Kernprodukten: [Geofences](https://radar.io/product/geofencing), [Trip Tracking](https://radar.io/product/trip-tracking) und [Geo APIs](https://radar.io/product/api). Die Kombination der branchenführenden Engagement-Plattform von Braze mit den branchenführenden Geofencing-Funktionen von Radar erlaubt es Ihnen, durch eine breite Palette von standortbasierten Produkten und Diensten Ihren Umsatz zu steigern und Ihre Kunden zu binden. Dazu gehören das Tracking von Abholungen und Zustellungen, durch den Standort getriggerte Benachrichtigungen, kontextuelle Personalisierung, Standortüberprüfung, Shop-Locators, automatische Adressvervollständigung und mehr.

_Diese Integration wird von Radar gepflegt._

## Über die Integration

Die Integration von Braze und Radar erlaubt Ihnen den Zugriff auf ausgefeilte standortbasierte Kampagnen-Trigger und die Anreicherung von Nutzerprofilen mit umfangreichen First-Party-Standortdaten. Wenn Radar Geofence- oder Trip Tracking-Ereignisse generiert werden, werden angepasste Events und Attribute der Nutzer:innen in Echtzeit an Braze gesendet. Diese Ereignisse und Attribute können dann verwendet werden, um standortbezogene Kampagnen zu triggern, Abhol- und Zustellvorgänge auf der letzten Meile zu unterstützen, die Flotten- und Versandlogistik zu überwachen oder Nutzer:innen auf der Grundlage von Standortmustern zu segmentieren. 

Darüber hinaus können Sie die Radar Geo APIs nutzen, um Ihre Kampagnen durch [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) zu bereichern oder zu personalisieren. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Radar-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Radar-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Bezeichner der App | Ihren [Bezeichner für die App]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) finden Sie auf dem Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. |
| iOS API-Schlüssel<br>Android API-Schlüssel | Diese API-Schlüssel finden Sie auf dem Braze-Dashboard unter **Einstellungen** > **App-Einstellungen**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

Um Daten zwischen den SDKs von Braze und Radar abzubilden, müssen Sie in beiden Systemen dieselben Nutzer:in oder Nutzer-Aliasing festlegen. Dies kann mit der Methode `changeUser()` im Braze SDK und mit der Methode `setUserId()` im Radar SDK geschehen.

So aktivieren Sie die Integration:

1. Suchen Sie in Radar auf der Seite [Integrationen](https://radar.com/documentation/integrations) nach Braze.
1. Setzen Sie **Enablement** auf **Ja**.
3. Geben Sie Ihren App-Bezeichner und Ihre API-Schlüssel ein.

{% alert note %}
Sie können separate API-Schlüssel für Test- und Live-Umgebungen festlegen.
{% endalert %}

{:start="4"}
4\. Wählen Sie Ihren Braze Endpunkt aus.
5\. Geben Sie beliebige Filter für Ereignisse oder Attribute ein, um sicherzustellen, dass nur relevante Daten an Braze für das Engagement Marketing gesendet werden. Wann immer Radar-Events generiert werden, sendet Radar angepasste Events und Nutzer:innen-Attribute an Braze. Ereignisse von iOS-Geräten werden mit Ihren iOS API-Schlüsseln gesendet; Ereignisse und Nutzer:innen-Attribute von Android-Geräten werden mit Ihren Android API-Schlüsseln gesendet.

{% alert note %}
Standardmäßig wird Radar `userId` auf Braze `external_id` für angemeldete Nutzer:innen abgebildet. Sie können jedoch abgemeldete Nutzer:innen tracken oder angepasste Abbildungen festlegen, indem Sie Radar `metadata.brazeAlias` oder `metadata.brazeExternalId` einstellen. Wenn Sie `metadata.brazeAlias` einstellen, müssen Sie auch einen passenden Alias in Braze mit dem Label `radarAlias` hinzufügen.
{% endalert %}

## Ereignis- und attributbasierte Anwendungsfälle

Sie können angepasste Events und Nutzer-Attribute verwenden, um standortbezogene Segmente zu erstellen oder standortbezogene Kampagnen zu triggern.

### Triggern Sie eine Benachrichtigung über die Ankunft im Shop für die Abholung an der Bordsteinkante 

Senden Sie eine Push-Benachrichtigung an die Nutzer:innen, wenn sie in Ihrem Shop eintreffen, um eine Abholung am Straßenrand vorzunehmen.

![Eine aktionsbasierte Zustellung der Kampagne, die zeigt, dass die Kampagne zugestellt wird, wenn das angepasste Event "arrived_at_trip_destination" eintritt und die "trip_metadata" gleich "curbside" ist.]({% image_buster /assets/img_archive/radar-campaign.png %})

### Erstellen Sie ein Segment der Zielgruppe der letzten Besucher des Shops

Stellen Sie zum Beispiel alle Nutzer:innen zusammen, die Ihren Shop innerhalb der letzten 7 Tage besucht haben, unabhängig davon, ob sie einen Kauf getätigt haben oder nicht.

![Ein Segment, in dem "radar_geofence_tags" den Wert my_store enthält und "radar_updated_at" vor weniger als 7 Tagen war.]({% image_buster /assets/img_archive/radar-segment.png %})

## Connected-Content

Das folgende Beispiel zeigt, wie Sie eine Aktion durchführen, um Nutzer:innen in der Nähe mit einem digitalen Angebot in den Shop zu locken. 

![Ein Android-Bild einer Connected-Content-Push-Nachricht, die "Neue In Store Deals, Walmart und Targeting in Ihrer Nähe" anzeigt.][1]{: style="float:right;max-width:30%;border:0;"}

Um loszulegen, benötigen Sie Ihren Radar API-Schlüssel, den Sie in Ihren Anfrage-URLs verwenden können.

Als nächstes stellen Sie innerhalb eines `connected_content` Tags eine GET-Anfrage an die [Search Places API](https://radar.io/documentation/api#search-places). Die Search Places API liefert Standorte in der Nähe, die auf [Radar Places](https://radar.io/documentation/places) basieren: eine Datenbank mit Standorten für Orte, Ketten und Kategorien, die einen umfassenden Überblick über die Welt bietet.

Der folgende Code-Snippet ist ein Beispiel dafür, was Radar als JSON-Objekt vom API-Aufruf zurückgibt:

```json
{
  "meta": {
    "code": 200
  },
  "places": [
    {
      "_id": "5dc9b0fd2004860034bf2b06",
      "name": "Target",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.42653983613333,
          40.548302893822985
        ]
      },
      "categories": [
        "shopping-retail",
        "department-store"
      ],
      "chain": {
        "slug": "target",
        "name": "Target",
        "domain": "target.com"
      }
    },
    {
      "_id": "5dc9b3d82004860034bfec54",
      "name": "Walmart",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.44121885326864,
          40.554603296187224
        ]
      },
      "categories": [
        "shopping-retail"
      ],
      "chain": {
        "slug": "walmart",
        "name": "Walmart",
        "domain": "walmart.com"
      }
    }
  ]
}
```

Um die gezielte und personalisierte Connected-Content Nachricht von Braze zu erstellen, können Sie das Attribut Braze `most_recent_location` als Eingabe für den Parameter `near` in der URL der API-Anfrage nutzen. Das Attribut `most_recent_location` wird über die Radar-Ereignisintegration oder direkt über das Braze SDK erfasst.

Im folgenden Beispiel wird der Radar-Kettenfilter für Target- und Walmart-Standorte angewendet, und der Suchradius für nahe gelegene Standorte wird auf 2 km festgelegt.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

Wie Sie aus dem Tag `connect_content` ersehen können, wird das JSON-Objekt in der lokalen Variable `nearbyplaces` gespeichert, indem `:save nearbyplaces` nach der URL hinzugefügt wird.
Sie können testen, wie die Ausgabe aussehen sollte, indem Sie auf {% raw %}`{{nearbyplaces.places}}`{% endraw%} verweisen.

Wenn wir unseren Anwendungsfall zusammenfassen, sieht die Syntax der Kampagne wie folgt aus. Der folgende Code iteriert durch das Objekt `nearbyplaces.places`, extrahiert eindeutige Werte und verkettet sie mit den richtigen, für den Menschen lesbaren Begrenzungszeichen für die Nachricht.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
{% if nearbyplaces.**http_status_code** != 200 %}
{% abort_message('Connected Content returned a non-200 http status code') %}
{% endif %}
{% if nearbyplaces.meta.code != 200 %}
{% abort_message('Connected Content returned a non-200 meta code') %}
{% endif %}
{% if nearbyplaces.places.size == 0 %}
{% abort_message('Connected Content returned no nearby places') %}
{% else %}
{% assign delimiter = ", " %}
{% assign names = nearbyplaces.places | map: 'name' | uniq %}
{% if names.size == 2 %}
{{ names | join: ' and ' }} 
{% elsif names.size > 2 %}
{% assign names_final_str = "" %}
{% for name in names %}
{% if forloop.first == true %}
{% assign names_final_str = names_final_str  | append: name %}
{% elsif forloop.last == true %}
{% assign names_final_str = names_final_str | append: ", and "  | append: name %}
{% else %}
{% assign names_final_str = names_final_str | append: delimiter  | append: name %}
{% endif %}
{% endfor %}
{{ names_final_str }}
{% else %}
{{ names }} 
{% endif %}
near you!
```
{% endraw %}

{% alert tip %}
In der [Dokumentation von Radar](https://radar.io/documentation/api) finden Sie alle Radar APIs, die Sie in Connected-Content nutzen können.
{% endalert %}


[1]: {% image_buster /assets/img/radar_example.png %}