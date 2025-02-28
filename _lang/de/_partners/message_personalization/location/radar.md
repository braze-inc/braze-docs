---
nav_title: Radar
article_title: Radar
alias: /partners/radar/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Radar, einer Geofencing-Plattform, mit der Sie Ihren iOS- und Android-Apps Standortkontext und Tracking hinzufügen können."
page_type: partner
search_tag: Partner

---

# Radar

> [Radar](https://www.onradar.com/) ist die führende Plattform für Geofencing und Standortverfolgung. Die Radar-Plattform besteht aus drei Kernprodukten: [Geofences](https://radar.io/product/geofencing), [Trip Tracking](https://radar.io/product/trip-tracking) und [Geo-APIs](https://radar.io/product/api). Durch die Kombination der branchenführenden Engagement-Plattform von Braze mit den branchenführenden Geofencing-Funktionen von Radar können Sie Ihren Umsatz und Ihre Loyalität durch eine Vielzahl von standortbasierten Produkt- und Serviceerlebnissen steigern. Dazu gehören Abhol- und Lieferverfolgung, standortabhängige Benachrichtigungen, kontextbezogene Personalisierung, Standortüberprüfung, Filialfinder, automatische Adressvervollständigung und mehr.

Die Integration von Braze und Radar ermöglicht Ihnen den Zugriff auf ausgefeilte standortbasierte Kampagnenauslöser und die Anreicherung von Benutzerprofilen mit umfangreichen Standortdaten von Erstanbietern. Wenn Radar Geofence- oder Trip-Tracking-Ereignisse erzeugt, werden benutzerdefinierte Ereignisse und Benutzerattribute in Echtzeit an Braze gesendet. Diese Ereignisse und Attribute können dann verwendet werden, um standortbezogene Kampagnen auszulösen, Abhol- und Liefervorgänge auf der letzten Meile zu unterstützen, die Flotten- und Versandlogistik zu überwachen oder Benutzersegmente auf der Grundlage von Standortmustern zu erstellen. 

Darüber hinaus können die Radar Geo APIs genutzt werden, um Ihre Marketingkampagnen durch [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/) zu bereichern oder zu personalisieren. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Radar-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Radar-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| App Kennung | Ihre [App-Kennung]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) können Sie im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** finden. |
| iOS API-Schlüssel<br>Android API-Schlüssel | Diese API-Schlüssel finden Sie auf dem Braze-Dashboard unter **Einstellungen** > **App-Einstellungen**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

Um Daten zwischen den SDKs von Braze und Radar abzubilden, müssen Sie in beiden Systemen die gleichen Benutzer-IDs oder Benutzer-Aliase festlegen. Dies kann mit der Methode `changeUser()` im Braze SDK und mit der Methode `setUserId()` im Radar SDK geschehen.

Um die Integration zu aktivieren:

1. Suchen Sie in Radar auf der Seite [Integrationen](https://radar.com/documentation/integrations) nach Braze.
1. Setzen Sie **Aktiviert** auf **Ja**.
3. Fügen Sie Ihre App-Kennung und Ihre API-Schlüssel ein.

{% alert note %}
Sie können separate API-Schlüssel für Test- und Live-Umgebungen festlegen.
{% endalert %}

{:start="4"}
4\. Wählen Sie Ihren Braze-Endpunkt.
5\. Geben Sie eine beliebige Filterung von Ereignissen oder Ereignisattributen ein, um sicherzustellen, dass nur relevante Daten für das Engagement Marketing an Braze gesendet werden. Wann immer Radar-Ereignisse erzeugt werden, sendet Radar benutzerdefinierte Ereignisse und Benutzerattribute an Braze. Ereignisse von iOS-Geräten werden mit Ihren iOS-API-Schlüsseln gesendet; Ereignisse und Benutzerattribute von Android-Geräten werden mit Ihren Android-API-Schlüsseln gesendet.

{% alert note %}
Standardmäßig wird Radar `userId` für eingeloggte Benutzer auf Braze `external_id` abgebildet. Sie können jedoch abgemeldete Benutzer verfolgen oder benutzerdefinierte Zuordnungen festlegen, indem Sie Radar `metadata.brazeAlias` oder `metadata.brazeExternalId` einstellen. Wenn Sie `metadata.brazeAlias` einstellen, müssen Sie auch in Braze einen passenden Alias mit der Bezeichnung `radarAlias` hinzufügen.
{% endalert %}

## Ereignis- und attributbasierte Anwendungsfälle

Sie können benutzerdefinierte Ereignisse und Benutzerattribute verwenden, um standortbezogene Segmente zu erstellen oder standortbezogene Kampagnen auszulösen.

### Lösen Sie eine Benachrichtigung über die Ankunft im Geschäft für die Abholung an der Bordsteinkante aus. 

Senden Sie dem Benutzer eine Push-Benachrichtigung mit Ankunftsanweisungen, wenn er in Ihrem Geschäft für eine Abholung an der Bordsteinkante ankommt.

![Eine aktionsbasierte Zustellungskampagne, die zeigt, dass die Kampagne zugestellt wird, wenn das benutzerdefinierte Ereignis "arrived_at_trip_destination" eintritt und die "trip_metadata" gleich "curbside" ist.]({% image_buster /assets/img_archive/radar-campaign.png %})

### Erstellen Sie ein Zielgruppensegment von Besuchern, die kürzlich im Geschäft waren.

Sie können zum Beispiel alle Benutzer ansprechen, die Ihr Geschäft innerhalb der letzten 7 Tage besucht haben, unabhängig davon, ob sie einen Kauf getätigt haben oder nicht.

![Ein Segment, in dem "radar_geofence_tags" den Wert my_store enthält und "radar_updated_at" vor weniger als 7 Tagen war.]({% image_buster /assets/img_archive/radar-segment.png %})

## Connected-Content

Das folgende Beispiel zeigt, wie Sie eine Werbeaktion durchführen, um Nutzer in der Nähe mit einem digitalen Angebot in ein Geschäft zu locken. 

![Ein Android-Bild einer Connected Content-Push-Nachricht, die "New In Store Deals, Walmart and target near you" anzeigt.][1]{: style="float:right;max-width:30%;border:0;"}

Um loszulegen, benötigen Sie Ihren Radar-API-Schlüssel, den Sie in Ihren Anfrage-URLs verwenden können.

Als nächstes stellen Sie innerhalb eines `connected_content` Tags eine GET-Anfrage an die [Search Places API](https://radar.io/documentation/api#search-places). Die API für die Suche nach Orten gibt Orte in der Nähe zurück, die auf [Radar Places](https://radar.io/documentation/places) basieren: eine Datenbank mit Orten, Ketten und Kategorien, die einen umfassenden Überblick über die Welt bietet.

Der folgende Codeschnipsel ist ein Beispiel dafür, was Radar als JSON-Objekt vom API-Aufruf zurückgeben wird:

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

Um die gezielte und personalisierte Nachricht von Connected Content zu erstellen, können Sie das Attribut `most_recent_location` von Braze als Eingabe für den Parameter `near` in der URL der API-Anfrage verwenden. Das Attribut `most_recent_location` wird über die Radar-Ereignisintegration oder direkt über das Braze SDK erfasst.

Im folgenden Beispiel wird die Radarkettenfilterung für Target- und Walmart-Standorte angewendet und der Suchradius für nahe gelegene Standorte auf 2 km festgelegt.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

Wie Sie aus dem Tag `connect_content` ersehen können, wird das JSON-Objekt in der lokalen Variablen `nearbyplaces` gespeichert, indem Sie `:save nearbyplaces` nach der URL hinzufügen.
Sie können testen, wie die Ausgabe aussehen sollte, indem Sie auf {% raw %}`{{nearbyplaces.places}}`{% endraw%} verweisen.

Wenn wir unseren Anwendungsfall zusammenfassen, würde die Syntax der Kampagne folgendermaßen aussehen. Der folgende Code durchläuft das Objekt `nearbyplaces.places`, extrahiert eindeutige Werte und verknüpft sie mit den richtigen, für den Menschen lesbaren Trennzeichen für die Nachricht.

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
In der [Radar-Dokumentation](https://radar.io/documentation/api) finden Sie alle Radar-APIs, die in Connected Content genutzt werden können.
{% endalert %}

[1]: {% image_buster /assets/img/radar_example.png %}