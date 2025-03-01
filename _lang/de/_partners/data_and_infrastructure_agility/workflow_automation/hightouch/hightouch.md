---
nav_title: Hightouch
article_title: Hightouch
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Hightouch, einer Plattform zur Synchronisierung Ihrer Kundendaten aus Ihrem Warenlager mit Business-Tools."
page_type: partner
search_tag: Partner

---

# Hightouch

> [Hightouch][1] ist eine moderne Datenintegrationsplattform, die es Ihnen ermöglicht, Kunden-, Produkt- oder firmeneigene Daten aus Ihrem Warehouse oder Data Lake mit jeder beliebigen Anwendung Ihrer Wahl zu synchronisieren - und das alles ohne Unterstützung durch Ihre IT- oder Technik-Teams.

Die Integration von Braze und Hightouch ermöglicht es Ihnen, bessere Kampagnen auf Braze mit aktuellen Kundendaten aus Ihrem Data Warehouse zu erstellen. Durch die automatische Synchronisierung von Kundendaten mit Braze müssen Sie sich nicht mehr um die Datenkonsistenz kümmern und können sich auf den Aufbau erstklassiger Kundenerlebnisse konzentrieren. 

Diese Integration ermöglicht es Ihnen auch, [Benutzerkohorten in Braze zu importieren]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/hightouch/) und gezielte Kampagnen auf der Grundlage von Daten zu versenden, die möglicherweise nur in Ihrem Warehouse vorhanden sind.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Hightouch-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Hightouch-Konto.
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track` und `users.export.ids`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz][2] ab.<br><br>Hightouch benötigt den Namen des Clusters, in dem sich Ihre Braze-Instanz befindet. Wenn Ihr Braze-Endpunkt zum Beispiel `https://rest.iad-01.braze.com` ist, benötigen Sie nur `iad-01`.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

* Synchronisieren Sie Daten über Benutzer und Konten mit Braze, um hyper-personalisierte Kampagnen zu erstellen.
* Aktualisieren Sie Ihre Braze-Segmente automatisch mit frischen Daten aus Ihrem Lager.
* Bieten Sie bessere Erlebnisse, indem Sie Daten von anderen Kundenkontaktpunkten in Braze integrieren.
* Importieren Sie Nutzerkohorten in Braze, damit Sie gezielte Kampagnen und Canvases versenden können. 

## Integration

### Schritt 1: Erstellen Sie Ihr Hightouch Braze Ziel

1. Auf der Hightouch-Plattform klicken Sie im Bereich **Ziele** auf **Ziel hinzufügen**.
2. Wählen Sie **Braze** aus der Liste der verfügbaren Ziele aus.
3. Geben Sie Ihren Braze REST-Endpunkt (außer "https://rest.") und Ihren Braze REST API Key an.<br><br>![][3]

### Schritt 2: Synchronisierung von Objekten und Ereignissen

Hightouch unterstützt die Synchronisierung sowohl mit Benutzerobjekten als auch mit Ereignissen.

| Ziel | Beschreibung | Unterstützte Modi |
|---|---|---|
| Objekt | Synchronisiert Datensätze mit Objekten wie Benutzern oder Organisationen in Ihrem Ziel.| Upsert oder Update |
| Events | Synchronisiert Aufzeichnungen als Ereignisse mit Ihrem Ziel; dies geschieht oft in Form eines Track-Calls. | Veranstaltung oder Kauf auf der Rennstrecke |

{% alert note %}
Weitere Informationen darüber, wie sich Synchronisierungen auf den Verbrauch von Braze-Datenpunkten auswirken, finden Sie bei [Hightouch](https://hightouch.com/docs/destinations/braze#syncing-and-data-point-consumption).
{% endalert %}

#### Synchronisieren von Braze-Objekten

Sie können Hightouch-Objekte (Benutzerfelder) mit den entsprechenden Standard- oder benutzerdefinierten Feldern von Braze synchronisieren. Sie können auch einen Datensatzabgleich durchführen, um die Daten zwischen den beiden Plattformen zu vereinheitlichen.

#### Synchronisierung von Braze-Ereignissen

Mit Hightouch können Sie Ereignis- und Kaufdaten verfolgen und mit Braze synchronisieren. In Hightouch können mehrere Optionen eingestellt werden, die sich auf das Synchronisierungsverhalten auswirken, z. B. die Einrichtung von Tracking-Daten und die Definition von nicht vorhandenem Benutzerverhalten.

{% alert important %}
Weitere Anweisungen zur Synchronisierung von Objekten und Ereignissen finden Sie in der [Hightouch-Dokumentation](https://hightouch.io/docs/destinations/braze/).
{% endalert %}



## Demo zur Integration

<div class="video-container">
    <iframe width="560" height="315" src="https://drive.google.com/file/d/1KQdCwZzV88hXMx7AMWgh8izqkldtNv5p/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

[1]: https://hightouch.io
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: {% image_buster /assets/img/hightouch/hightouch_braze_setup.png %}
[4]: https://hightouch.io/docs/destinations/braze/

