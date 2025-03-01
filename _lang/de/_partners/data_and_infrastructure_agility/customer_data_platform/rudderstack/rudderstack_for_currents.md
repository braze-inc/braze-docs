---
nav_title: RudderStack für Strömungen
article_title: RudderStack für Strömungen
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze Currents und RudderStack, einer Open-Source-Kundendateninfrastruktur, die eine nahtlose Braze-Integration für Ihre Android-, iOS- und Webanwendungen bietet."
page_type: partner
tool: Currents
search_tag: Partner

---

# RudderStack für Strömungen

> Mit [RudderStack](https://www.rudderstack.com/) können Sie Ihre Kundendaten sammeln, umwandeln und aktivieren, indem Sie Ihr Cloud Data Warehouse als zentrale Quelle der Wahrheit nutzen. Dieser Artikel gibt einen Überblick darüber, wie Sie eine Verbindung zwischen Braze Currents und RudderStack einrichten.

Die Integration von Braze und RudderStack ermöglicht es Ihnen, Braze Currents zu nutzen, um Ihre Braze-Ereignisse nach RudderStack zu exportieren und so tiefere Analysen durchzuführen.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| RuderStack-Konto | Ein [RudderStack-Konto](https://app.rudderstack.com/login) ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen. |
| Ziel löten | Wir empfehlen Ihnen, [Braze als Ziel]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration) in RudderStack [einzurichten]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration). |
| Currents | Um Daten zurück in RudderStack zu exportieren, müssen Sie [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie eine Datenquelle für Braze in RudderStack

Zunächst müssen Sie eine Braze-Quelle in der RudderStack-Web-App erstellen. Eine Anleitung zum Erstellen einer Datenquelle finden Sie auf der [RudderStack-Website](https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/braze-currents/).

Sobald dies geschehen ist, stellt RudderStack eine Webhook-URL zur Verfügung, einschließlich des Schreibschlüssels, den Sie im nächsten Schritt verwenden müssen. Sie finden die Webhook-URL auf der Registerkarte **Einstellungen** Ihrer Braze-Quelle.

### Schritt 2: Aktuell erstellen

Navigieren Sie in Braze zu **Strömungen > + Strömung erstellen > RudderStack Export**. Geben Sie einen Integrationsnamen, eine Kontakt-E-Mail, die RudderStack Webhook-URL (die in das Schlüsselfeld gehört) und die RudderStack-Region an. 

### Schritt 3: Ereignisse exportieren

Wählen Sie dann die Ereignisse aus, die Sie exportieren möchten. Klicken Sie abschließend auf **Aktuelles starten**

Alle Ereignisse, die an RudderStack gesendet werden, enthalten die Adresse des Benutzers `external_user_id`. Zur Zeit sendet Braze keine Ereignisdaten an RudderStack für Benutzer, die ihre `external_user_id` nicht eingestellt haben.

## Details zur Integration

Braze unterstützt den Export aller Daten, die in den [Currents-Ereignisglossaren]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) aufgeführt sind, nach RudderStack.

Die Payload-Struktur für exportierte Daten ist die gleiche wie die Payload-Struktur für benutzerdefinierte HTTP-Konnektoren, die Sie im [Repository für Beispiele für benutzerdefinierte HTTP-Konnektoren](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors) einsehen können.