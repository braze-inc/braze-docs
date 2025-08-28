---
nav_title: Zeotap für Currents
article_title: Zeotap für Currents
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze-Currents und Zeotap, einer Kundendaten-Plattform der nächsten Generation, die Ihnen hilft, Ihre mobile Zielgruppe zu entdecken und zu verstehen, indem sie Identitätsauflösung, Insights und Datenanreicherung bietet."
page_type: partner
tool: Currents
search_tag: Partner
---

# Zeotap für Currents

> [Zeotap](https://zeotap.com/) ist eine Customer Data Platform (CDP) der nächsten Generation, die Ihnen hilft, Ihre mobile Zielgruppe zu entdecken und zu verstehen, indem sie Identitätsauflösung, Insights und Datenanreicherung bietet.

Mit der Integration von Braze und Zeotap können Sie den Umfang und die Reichweite Ihrer Kampagnen erweitern, indem Sie die Segmente von Zeotap-Kunden mit den Nutzerprofilen von Braze synchronisieren. Mit [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) können Sie Daten auch mit Zeotap verbinden, um sie über den gesamten Growth Stack hinweg nutzbar zu machen.

{% alert important %}
Der angepasste HTTP-Konnektor befindet sich derzeit in der Betaphase. Wenn Sie daran interessiert sind, diese Integration einzurichten, wenden Sie sich an Ihren Customer-Success-Manager:in.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
|Zeotap-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein [Zeotap-Konto](https://zeotap.com/). |
| Currents | Um Daten zurück in Zeotap zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data/braze_currents/) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Implementierung

### Schritt 1: Erstellen Sie eine Currents-Quelle

1. Gehen Sie in Zeotap unter **Integrieren** auf **Quellen**.
2. Wählen Sie **Quelle erstellen**.
3. Wählen Sie **Customer-Engagement-Kanäle** als Kategorie aus.<br><br>![Ein Fenster "Quelle erstellen", das verschiedene Kategorien auflistet, darunter "Customer-Engagement-Kanäle".]({% image_buster /assets/img/zeotap/cec.png %}){: style="max-width:70%;"}<br><br>
4. Wählen Sie **Braze** als Datenquelle aus.
5. Geben Sie einen Quellennamen ein.
6. Wählen Sie Ihre Region aus.<br><br>![Fenster mit Optionen zum Auswählen Ihrer Region und der Dateneinheit.]({% image_buster /assets/img/zeotap/select_region.png %}){: style="max-width:70%;"}<br><br>
7. Wählen Sie **Quelle erstellen**.
8. Gehen Sie zum Tab **Implementierungsdetails** und notieren Sie sich die **API-URL** und den **API-Schlüssel**.<br><br>![Implementierungsdetails für Braze-Currents, die die API-URL und den API-Schlüssel enthalten.]({% image_buster /assets/img/zeotap/implementation_details.png %})

### Schritt 2: Konfigurieren Sie das Daten streamen von in Currents

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Datenexport**.
2. Wählen Sie **Neue Currents erstellen** und **Angepasste Currents exportieren**.<br><br>![Der Button "Neue Currents erstellen" mit einem Dropdown-Menü, das "Custom Currents Export" enthält.]({% image_buster /assets/img/zeotap/custom_currents_export.png %}){: style="max-width:60%;"}<br><br>
3. Geben Sie einen Namen für die Integration und eine E-Mail ein, um bei Fehlern mit der Integration kontaktiert zu werden.
4. Geben Sie unter **Zugangsdaten** die folgenden Informationen ein, die Sie in [Schritt 1](#step-1-create-a-currents-source) notiert haben:
- Die API URL als **Endpunkt**
- Der Schreibschlüssel als **Bearer Token**<br><br>![Abschnitte zur Eingabe von Integrationsdetails und Zugangsdaten.]({% image_buster /assets/img/zeotap/credentials.png %})<br><br>
5. Wählen Sie die Messaging-Ereignisse aus, die Sie an Zeotap senden möchten.<br><br>![Der Tab "Allgemeine Einstellungen" mit einem Abschnitt zum Auswählen von Ereignissen für das Engagement von Nachrichten.]({% image_buster /assets/img/zeotap/message_engagement_events.png %})
6. Wählen Sie **Launch Current**, um die Änderungen zu speichern und Ereignisse an Zeotap zu senden.

{% alert important %}
Der Currents Konnektor unterstützt keine anonymen Nutzer:innen (Nutzer:innen ohne `external_id`).
{% endalert %}

