---
nav_title: Dixa
article_title: Dixa
description: "Dieser Artikel stellt die Partnerschaft zwischen Braze und Dixa vor."
alias: /partners/dixa/
page_type: partner
search_tag: Partner

---

# Dixa

> [Dixa](https://www.dixa.com/) ist eine Plattform für den Dienst am Kunden, mit der Sie Ihre Kundenerlebnisse verbessern können, indem Sie Kommunikationskanäle wie Chat, E-Mail, Telefon und Social Media in einer einzigen Schnittstelle zusammenfassen. Es hilft Unternehmen, die Kundenzufriedenheit und Effizienz durch intelligentes Routing, Automatisierung und Insights zur Realtime Performance zu verbessern.

Die Integration von Braze und Dixa bietet einen besseren Überblick über alle Ihre Nutzer:innen, indem sie den Agenten im Kundendienst Realtime-Daten von Braze zur Verfügung stellt.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung          | Beschreibung                                                                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ein Dixa-Konto        | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Dixa-Administratorkonto.                                                                                           |
| Ein Braze REST API-Schlüssel  | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.export.ids` und `email.status`.<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Ein Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Fügen Sie Braze-Daten in die Ansicht des Kundendienstmitarbeiters ein, während Sie mit Ihren Nutzern:innen über verschiedene Kommunikationskanäle wie E-Mail, Messenger oder Chat kommunizieren.

## Integration

Sie müssen ein Dixa-Administrator sein, um Integrationen innerhalb von Dixa zu konfigurieren. Für die Integration von Braze gehen Sie in Dixa zu **Einstellungen** > **Integrationen** > **Braze**.

![]({% image_buster /assets/img/dixa/dixa-create-integration.png %}){: style="width:450px;"}

### Schritt 1: Erstellen Sie die Integration in Dixa

Auf der Seite **Braze-Widget erstellen** füllen Sie die folgenden erforderlichen Felder aus, um die Integration zu erstellen:

- **Name des Widgets:** Dies ist der Name der Integration, der später in der Konversations-Seitenleiste als Titel verwendet wird.
- **API URL:** Dies ist die URL des REST API-Endpunkts von Braze für Ihre Instanz.
- **API-Schlüssel:** Dies ist der API-Schlüssel von Braze, den Sie in den Voraussetzungen erstellt haben.

### Schritt 2: Konfigurieren Sie die Integration

Als nächstes konfigurieren Sie die Integration von Braze und Dixa. Wählen Sie eine der folgenden Optionen, um die Ansicht des Braze-Widgets in der Konversations-Seitenleiste anzupassen.

#### Zeigen Sie das Widget in der Konversations-Seitenleiste an

Diese Einstellung blendet die gesamte Integration in der Konversations-Seitenleiste in Dixa ein oder aus. 

Wenn Sie die Integration aktiv konfigurieren, empfehlen wir Ihnen, diese Funktion zu deaktivieren, während Sie die erforderlichen Felder ausfüllen. Wenn Sie mit der Konfiguration fertig sind, können Sie sie wieder einschalten und die Dixa-Agenten können die Integration nutzen.

#### Details zu Kund:in anzeigen

Wählen Sie, ob Sie die Nutzer:innen anzeigen oder ausblenden möchten. Die Details enthalten Daten über Standort, E-Mail, Telefonnummer, Status des E-Mail-Abos, Status des Push-Benachrichtigungs-Abos und die Dauer der Mitgliedschaft in Braze. 

#### Anzeige des Buttons zum Ändern des Status des E-Mail-Abos

Die Buttons basieren auf einem der drei Abo-Status von Braze: `subscribed`, `opted-in` und `unsubscribed`. Wenn ein Nutzer:innen `subscribed` ist, kann der Agent zwischen `opt-in` und `unsubscribe` wählen. Wenn ein Nutzer:in `opted-in` oder `unsubscribed` ist, ist es nur möglich, zwischen diesen beiden zu wechseln.

#### Liste der angepassten Attribute anzeigen

Wählen Sie, ob Sie die angepassten Attribute des Nutzers:innen in Braze anzeigen oder ausblenden möchten.

#### Anzeigen einer Liste angepasster Events

Wählen Sie, ob Sie die angepassten Braze Events des Nutzers:innen anzeigen oder ausblenden möchten.

#### Eine Liste der Einkäufe anzeigen

Wählen Sie, ob Sie eine Liste der vom Nutzer:innen gekauften Produkte anzeigen oder ausblenden möchten. Hier können Sie sehen, wie oft es gekauft wurde. Um das Datum des ersten und letzten Kaufs anzuzeigen, bewegen Sie den Mauszeiger über den Artikel. 

### Beispiel Integration

Im Folgenden sehen Sie ein Beispiel für die Integration:

![Die Integration von Braze und Dixa in Dixa, die den Status des E-Mail-Abos eines Nutzers:in, angepasste Attribute, angepasste Events und Käufe anzeigt.]({% image_buster /assets/img/dixa/dixa-braze-integration.png %}){: style="width:350px;"}

