---
nav_title: Bluedot
article_title: Bluedot
alias: /partners/bluedot/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Bluedot, einer Standort-Plattform, die eine genaue und unkomplizierte Geoofencing-Plattform für Ihre Apps bietet."
page_type: partner
search_tag: Partner

---

# Bluedot

> [Bluedot](https://bluedot.io/) ist eine Standort-Plattform, die eine genaue und unkomplizierte Geofencing-Plattform für Ihre Apps bietet. Nutzen Sie das SDK von Bluedot, um Nachrichten intelligenter zu gestalten, mobile Bestellvorgänge zu automatisieren, Arbeitsabläufe zu optimieren und reibungslose Erlebnisse zu schaffen. 

_Diese Integration wird von Bluedot gepflegt._

## Über die Integration

Die Integration von Braze und Bluedot erlaubt es Ihnen, die Geofence Dienste von Bluedot zu nutzen, um Benutzer-Events zu erstellen, die zum Aufbau von Customer Journeys, Kampagnen und zur Analyse des Kundenverhaltens und der Interessen verwendet werden können. Ereignisse (Eingang/Austritt), die der Nutzer:innen auf seinem Gerät erzeugt, werden sofort mit allen relevanten Informationen an Braze gesendet. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Bluedot Konto | Um die Vorteile dieser Integration zu nutzen, benötigen Sie ein Bluedot-Konto. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Die von Bluedot zur Verfügung gestellten Informationen über angepasste Standorte von Events können in Ihren Kampagnen verwendet werden, um gängige Anwendungsfälle zu erfüllen:
- [`QSR`](https://bluedot.io/solutions/quick-service-restaurants/) (Quick Service Restaurant)
- [`Click and Collect`](https://bluedot.io/solutions/click-and-collect/)
- [`Drive-Thru`](https://bluedot.io/solutions/qsr-drive-thru/) 

## Integration

### Schritt 1: Erstellen Sie ein Bluedot Projekt
Richten Sie Ihr Bluedot-Konto ein und melden Sie sich bei Ihrem [Bluedot Canvas Dashboard](https://docs.bluedot.io/canvas/) an. Besuchen Sie die [Bluedot Dokumentation](https://docs.bluedot.io/canvas/creating-a-new-project/), um zu erfahren, wie Sie ein neues Projekt erstellen können.

### Schritt 2: Integration der SDKs
Integrieren Sie das Bluedot Point SDK und das Braze SDK in Ihre App anhand der Schritte, die in der Dokumentation zur [Integration von Bluedot und Braze](https://docs.bluedot.io/integrations/braze-integration/) beschrieben sind.

### Schritt 3: Authentifizierung des Bluedot SDK
Verwenden Sie zur Authentifizierung des Bluedot Point SDK die in Schritt 1 erstellte `projectId`.

### Schritt 4: Verwenden Sie Bluedot Ereignisse in Braze

#### Triggern von Nachrichten

Sie können eine Push-Kampagne oder ein Canvas einrichten, das auf Standort-Ereignisse reagiert, die vom Bluedot SDK generiert werden. Diese Integration ist ideal für Realtime Messaging, wenn Nutzer:innen einen Veranstaltungsort oder einen Standort von Interesse betreten, oder für eine verzögerte Folgekommunikation, nachdem sie ihn verlassen haben.

Richten Sie in Braze eine aktionsbasierte Kampagne ein, die Nachrichten auf der Grundlage eines bestimmten Standorts versendet. Verwenden Sie für Ihren Trigger ein angepasstes Event von `bluedot_entry` oder `bluedot_exit`, wie im folgenden Screenshot gezeigt:

![Eine aktionsbasierte Kampagne in der Phase der Zustellung. Hier haben Sie zwei Zeitplan-Optionen, die die Kampagne senden, wenn ein Nutzer:innen ein angepasstes `bluedot_entry` oder `bluedot_exit` Event ausführt.]({%image_buster /assets/img_archive/Campaign-Delivery-BD.png %}){: style="max-width:80%"}

#### Targeting von Nutzer:innen

Stellen Sie sicher, dass Sie **Alle Nutzer**:innen für Ihren Workspace als Targeting auswählen.
![Eine aktionsbasierte Kampagne mit dem Schritt der Zielgruppe Nutzer:innen fordert Sie auf, "Alle Nutzer:innen" als gewünschtes Segment auszuwählen.]({%image_buster /assets/img_archive/Campaign-Target_users-BD.png %}){: style="max-width:80%"}

