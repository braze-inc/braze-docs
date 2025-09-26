---
nav_title: Hightouch
article_title: Hightouch
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Hightouch, einer Plattform, mit der Sie Ihre Kundendaten aus Ihrem Data Warehouse mit Business-Tools synchronisieren können."
page_type: partner
search_tag: Partner

---

# Hightouch

> [Hightouch](https://hightouch.io) ist eine moderne Plattform für die Datenintegration, mit der Sie Kunden-, Produkt- oder proprietäre Daten aus Ihrem Data Warehouse oder Data Lake mit jeder App Ihrer Wahl synchronisieren können, und zwar ohne die Hilfe Ihrer IT- oder Entwicklerteams.

Die Integration von Braze und Hightouch erlaubt es Ihnen, bessere Kampagnen auf Braze mit aktuellen Kundendaten aus Ihrem Data Warehouse zu erstellen. Durch die automatische Synchronisierung von Kundendaten mit Braze müssen Sie sich nicht mehr um die Konsistenz der Daten kümmern und können sich auf den Aufbau erstklassiger Kundenerlebnisse konzentrieren. 

Mit dieser Integration können Sie auch [Nutzer:innen-Kohorten in Braze importieren]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch_cohort_import/) und gezielte Kampagnen auf der Grundlage von Daten versenden, die möglicherweise nur in Ihrem Warehouse vorhanden sind.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Hightouch Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Hightouch-Konto.
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track` und `users.export.ids`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) ab.<br><br>Hightouch benötigt den Namen des Clusters, in dem sich Ihre Braze-Instanz befindet. Wenn Ihr Braze Endpunkt zum Beispiel `https://rest.iad-01.braze.com` ist, benötigen Sie nur `iad-01`.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

* Synchronisieren Sie Daten über Nutzer:innen und Konten mit Braze, um hyper-personalisierte Kampagnen zu erstellen.
* Aktualisieren Sie Ihre Segmente in Braze automatisch mit frischen Daten aus Ihrem Data Warehouse.
* Liefern Sie bessere Erlebnisse, indem Sie Daten von anderen Kund:in Touchpoints in Braze einbringen.
* Importieren Sie Kohorten von Nutzern:innen in Braze, was das Versenden von Targeting-Kampagnen und Canvase zulässig macht. 

## Integration

### Schritt 1: Erstellen Sie Ihr Hightouch Braze Ziel

1. Auf der Hightouch-Plattform klicken Sie im Bereich **Ziele** auf **Ziel hinzufügen**.
2. Wählen Sie **Braze** aus der Liste der verfügbaren Ziele aus.
3. Geben Sie Ihren Braze REST-Endpunkt (außer "https://rest.") und Ihren Braze REST API-Schlüssel an.<br><br>![]({% image_buster /assets/img/hightouch/hightouch_braze_setup.png %})

### Schritt 2: Synchronisierung von Objekten und Ereignissen

Hightouch unterstützt die Synchronisierung sowohl mit Nutzer:innen als auch mit Ereignissen.

| Ziel | Beschreibung | Unterstützte Modi |
|---|---|---|
| Objekt | Synchronisiert Datensätze mit Objekten wie Nutzer:innen oder Organisationen in Ihrem Ziel.| Upsert oder Update |
| Events | Synchronisiert Aufzeichnungen als Ereignisse mit Ihrem Ziel; dies geschieht oft in Form eines Tracking-Aufrufs. | Tracking von Ereignissen oder Käufen |

{% alert note %}
Weitere Informationen darüber, wie sich Synchronisierungen auf den Verbrauch Ihrer Datenpunkte bei Braze auswirken, finden Sie bei [Hightouch](https://hightouch.com/docs/destinations/braze#syncing-and-data-point-consumption).
{% endalert %}

#### Synchronisieren von Braze Objekten

Sie können Hightouch-Objekte (Nutzer:innen) mit den entsprechenden Braze Standard- oder angepassten Feldern synchronisieren. Sie können auch einen Datensatzabgleich durchführen, um die Daten zwischen den beiden Plattformen zu vereinheitlichen.

#### Synchronisierung von Braze-Ereignissen

Hightouch erlaubt Ihnen das Tracking von Ereignis- und Kauf-Daten und deren Synchronisierung mit Braze. In Hightouch können mehrere Optionen eingestellt werden, die sich auf das Synchronisationsverhalten auswirken, z.B. die Einrichtung von Tracking-Daten und die Definition von nicht vorhandenem Nutzer:in.

{% alert important %}
Weitere Anweisungen zur Synchronisierung von Objekten und Ereignissen finden Sie in der [Hightouch Dokumentation](https://hightouch.io/docs/destinations/braze/).
{% endalert %}



## Demo zur Integration

<div class="video-container">
    <iframe width="560" height="315" src="https://drive.google.com/file/d/1KQdCwZzV88hXMx7AMWgh8izqkldtNv5p/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


