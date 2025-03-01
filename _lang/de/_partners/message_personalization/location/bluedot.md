---
nav_title: Bluedot
article_title: Bluedot
alias: /partners/bluedot/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Bluedot, einer Ortungsplattform, die eine genaue und unkomplizierte Geofencing-Plattform für Ihre Apps bietet."
page_type: partner
search_tag: Partner

---

# Bluedot

> [Bluedot](https://bluedot.io/) ist eine Ortungsplattform, die eine genaue und unkomplizierte Geofencing-Plattform für Ihre Apps bietet. Nutzen Sie das SDK von Bluedot, um intelligentere Nachrichten zu übermitteln, mobile Bestellvorgänge zu automatisieren, Arbeitsabläufe zu optimieren und reibungslose Erfahrungen zu schaffen. 

Die Integration von Braze und Bluedot ermöglicht es Ihnen, die Geofence-Standortdienste von Bluedot zu nutzen, um Benutzerereignisse zu erstellen, die zum Aufbau von Journeys und Kampagnen sowie zur Analyse des Verhaltens und der Interessen von Kunden verwendet werden können. Ereignisse (Eintritt/Austritt), die der Benutzer auf seinem Gerät erzeugt, werden sofort mit allen relevanten Informationen an Braze gesendet. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Bluedot Konto | Um die Vorteile dieser Integration zu nutzen, benötigen Sie ein Bluedot-Konto. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Die von Bluedot bereitgestellten benutzerdefinierten Informationen zum Veranstaltungsort können in Ihren Kampagnen verwendet werden, um gängige Anwendungsfälle zu erfüllen:
- [`QSR`](https://bluedot.io/solutions/quick-service-restaurants/) (Schnellrestaurant)
- [`Click and Collect`](https://bluedot.io/solutions/click-and-collect/)
- [`Drive-Thru`](https://bluedot.io/solutions/qsr-drive-thru/) 

## Integration

### Schritt 1: Ein Bluedot-Projekt erstellen
Richten Sie Ihr Bluedot-Konto ein und melden Sie sich bei Ihrem [Bluedot Canvas Dashboard](https://docs.bluedot.io/canvas/) an. Besuchen Sie die [Bluedot-Dokumentation](https://docs.bluedot.io/canvas/creating-a-new-project/), um zu erfahren, wie Sie ein neues Projekt erstellen können.

### Schritt 2: Integrieren Sie die SDKs
Integrieren Sie das Bluedot Point SDK und das Braze SDK in Ihre App, indem Sie die in der Dokumentation zur [Bluedot-Braze-Integration](https://docs.bluedot.io/integrations/braze-integration/) beschriebenen Schritte ausführen.

### Schritt 3: Authentifizierung des Bluedot SDK
Verwenden Sie die in Schritt 1 erstellte `projectId` zur Authentifizierung des Bluedot Point SDK.

### Schritt 4: Verwenden Sie Bluedot-Ereignisse in Braze

#### Nachrichten auslösen

Sie können eine Push-Kampagne oder ein Canvas einrichten, das auf die vom Bluedot SDK generierten Standortereignisse reagiert. Diese Integrationsroute ist ideal für Echtzeit-Nachrichten, sobald Nutzer einen Veranstaltungsort oder einen Ort von Interesse betreten, oder für eine verzögerte Folgekommunikation, nachdem sie ihn verlassen haben.

Richten Sie in Braze eine aktionsbasierte Kampagne ein, die Nachrichten auf der Grundlage eines bestimmten Standorts versendet. Verwenden Sie für Ihren Auslöser ein benutzerdefiniertes Ereignis von `bluedot_entry` oder `bluedot_exit`, wie im folgenden Screenshot gezeigt:

![Eine aktionsbasierte Kampagne in der Lieferstufe. Hier haben Sie zwei Planungsoptionen, die die Kampagne senden, wenn ein Benutzer ein benutzerdefiniertes `bluedot_entry` oder `bluedot_exit` Ereignis ausführt.]({%image_buster /assets/img_archive/Campaign-Delivery-BD.png %}){: style="max-width:80%"}

#### Benutzer anvisieren

Stellen Sie sicher, dass Sie **Alle Benutzer** für Ihren Arbeitsbereich auswählen.
![Eine aktionsbasierte Kampagne mit dem Schritt "Zielbenutzer" ermutigt Sie, "Alle Benutzer" als gewünschtes Segment auszuwählen.]({%image_buster /assets/img_archive/Campaign-Target_users-BD.png %}){: style="max-width:80%"}