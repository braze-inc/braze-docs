---
nav_title: Rudderstack für Currents
article_title: Rudderstack für Currents
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze-Currents und Rudderstack, einer Open-Source-Infrastruktur für Kundendaten, die eine nahtlose Integration von Braze für Ihre Android-, iOS- und Internet-Anwendungen bietet."
page_type: partner
tool: Currents
search_tag: Partner

---

# Rudderstack für Currents

> Mit [Rudderstack](https://www.rudderstack.com/) können Sie Ihre Kundendaten über Ihren Stack hinweg sammeln, transformieren und aktivieren, indem Sie Ihr Data Warehouse in der Cloud als zentrale Wahrheitsquelle nutzen. Dieser Artikel gibt eine Übersicht darüber, wie Sie eine Verbindung zwischen Braze-Currents und Rudderstack einrichten.

Die Integration von Braze und Rudderstack erlaubt es Ihnen, Braze-Currents zu nutzen, um Ihre Braze-Ereignisse nach Rudderstack zu exportieren und so tiefere Analytics zu ermöglichen.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| Rudderstack Konto | Sie benötigen ein [Rudderstack-Konto](https://app.rudderstack.com/login), um die Vorteile dieser Partnerschaft zu nutzen. |
| Braze Ziel | Wir empfehlen,  in Rudderstack [Braze als Ziel einzurichten]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration). |
| Currents | Um Daten zurück in Rudderstack zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto einrichten lassen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie eine Datenquelle für Braze in Rudderstack

Zunächst müssen Sie eine Braze-Quelle in der Rudderstack Web App erstellen. Eine Anleitung zum Erstellen einer Datenquelle finden Sie auf der [Rudderstack-Website](https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/braze-currents/).

Sobald dies geschehen ist, stellt Rudderstack eine Webhook-URL zur Verfügung, einschließlich des Schreibschlüssels, den Sie im nächsten Schritt verwenden müssen. Sie finden die Webhook-URL auf dem Tab **Einstellungen** Ihrer Braze-Quelle.

### Schritt 2: Currents erzeugen

Navigieren Sie in Braze zu **Currents > + Create Current > Rudderstack Export**. Geben Sie den Namen der Integration, die E-Mail des Kontakts, die Webhook-URL von Rudderstack (die in das Schlüsselfeld gehört) und die Region von Rudderstack an. 

### Schritt 3: Ereignisse exportieren

Wählen Sie dann die Ereignisse aus, die Sie exportieren möchten. Klicken Sie abschließend auf **Launch Current**

Alle Ereignisse, die an Rudderstack gesendet werden, enthalten die `external_user_id` des Nutzers:innen. Zur Zeit sendet Braze keine Ereignisdaten an Rudderstack für Nutzer:innen, die ihre `external_user_id` nicht eingestellt haben.

## Details zur Integration

Braze unterstützt den Export aller Daten, die in den [Currents-Ereignisglossaren]({{site.baseurl}}/user_guide/data/braze_currents/) aufgeführt sind, nach Rudderstack.

Die Payload-Struktur für exportierte Daten entspricht der Payload-Struktur für angepasste HTTP-Konnektoren, die Sie im [Beispiel-Repository für angepasste HTTP-Konnektoren](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors) einsehen können.