---
nav_title: Standort-Targeting
article_title: Standort-Targeting
page_order: 10
page_type: tutorial
tool: 
- Segments
- Location
description: "In diesem Artikel erfahren Sie, wie Sie das Location Targeting einrichten, mit dem Sie Nutzer nach ihrem Standort segmentieren können."

---

# Standort-Targeting

> In diesem Artikel erfahren Sie, wie Sie Location Targeting einrichten, mit dem Sie Nutzer nach ihrem letzten Aufenthaltsort segmentieren können. Dies ist ideal, wenn Sie sich mit standortbezogenen Kampagnen und Strategien befassen.

## Schritt 1: Segment erstellen

Navigieren Sie zur Seite **Segmente** unter **Zielgruppe**, um alle Ihre aktuellen Benutzersegmente anzuzeigen. Auf dieser Seite können Sie neue Segmente erstellen und benennen. Um zu beginnen, wählen Sie **Segment erstellen** und geben Sie Ihrem Segment einen Namen.

![Modal zum Erstellen eines Segments.]({% image_buster /assets/img_archive/createsegment2.png %}){: style="max-width:70%;"}

## Schritt 2: Standort anpassen

Nachdem Sie Ihr Segment erstellt haben, fügen Sie einen Filter für **den letzten Standort** hinzu, um Nutzer:innen nach dem letzten Ort zu targetieren, an dem sie Ihre App verwendet haben. Sie haben die Möglichkeit, Nutzer:innen innerhalb oder außerhalb eines kreisförmigen Standardbereichs oder eines anpassbaren polygonalen Bereichs zu markieren.

![Filter für den letzten Standort innerhalb eines Kreises.]({% image_buster /assets/img_archive/filter_recent_location.png %})

{% tabs %}
{% tab Circular %}

### Kreisförmige Regionen

Bei kreisförmigen Regionen können Sie den Ursprung verschieben und den Positionsradius für Ihre Segmentierung anpassen.

![Ein kreisförmiger Umriss der Städte zwischen New Jersey und New York.]({% image_buster /assets/img_archive/location_circle.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Polygonal %}

### Polygonale Regionen

Bei polygonalen Regionen können Sie genauer festlegen, welche Bereiche in Ihrem Segment enthalten sein sollen.

![Ein Umriss des Staates New York als ausgewählte polygonale Region.]({% image_buster /assets/img_archive/create_polygon.png %}){: style="max-width:70%;"}

{% endtab %}
{% endtabs %}

## Partnerschaftsunterstützung für Beacon und Geofence

Wenn Sie bestehende Beacon- oder Geofence-Unterstützung mit unseren Targeting- und Nachrichtenfunktionen kombinieren, erhalten Sie mehr Informationen über die physischen Aktionen Ihrer Nutzer, so dass Sie ihnen entsprechende Nachrichten senden können. Sie können das Standort-Tracking mit einigen unserer Partner nutzen: 

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

