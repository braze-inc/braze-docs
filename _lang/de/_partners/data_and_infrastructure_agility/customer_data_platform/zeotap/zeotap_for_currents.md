---
nav_title: Zeotap für Ströme
article_title: Zeotap für Ströme
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze Currents und Zeotap, einer Kundendatenplattform der nächsten Generation, die Ihnen hilft, Ihr mobiles Publikum zu entdecken und zu verstehen, indem sie Identitätsauflösung, Einblicke und Datenanreicherung bietet."
page_type: partner
tool: Currents
search_tag: Partner
---

# Zeotap für Ströme

> [Zeotap](https://zeotap.com/) ist eine Kundendatenplattform der nächsten Generation, die Ihnen hilft, Ihr mobiles Publikum zu entdecken und zu verstehen, indem sie Identitätsauflösung, Einblicke und Datenanreicherung bietet.

Die Integration von Braze und Zeotap ermöglicht es Ihnen, den Umfang und die Reichweite Ihrer Kampagnen zu vergrößern, indem Sie die Kundensegmente von Zeotap mit den Benutzerprofilen von Braze synchronisieren. Mit [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) können Sie die Daten auch mit Zeotap verbinden, um sie über den gesamten Wachstumsbereich hinweg nutzbar zu machen.

{% alert important %}
Der benutzerdefinierte HTTP-Connector befindet sich derzeit in der Beta-Phase. Wenn Sie daran interessiert sind, diese Integration einzurichten, wenden Sie sich an Ihren Customer Success Manager.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
|Zeotap-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Zeotap-Konto](https://zeotap.com/). |
| Currents | Um Daten zurück in Zeotap zu exportieren, müssen Sie [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Implementierung

### Schritt 1: Eine Currents-Quelle erstellen

1. Gehen Sie in Zeotap zu **Quellen** unter **Integrieren**.
2. Wählen Sie **Quelle erstellen**.
3. Wählen Sie als Kategorie **Kundenbindungskanäle**.<br><br>![Ein Fenster "Quelle erstellen", das verschiedene Kategorien auflistet, darunter "Customer Engagement Channels".][1]{: style="max-width:70%;"}<br><br>
4. Wählen Sie **Braze** als Datenquelle.
5. Geben Sie einen Quellennamen ein.
6. Wählen Sie Ihre Region.<br><br>![Fenster mit Optionen zur Auswahl Ihrer Region und Dateneinheit.][6]{: style="max-width:70%;"}<br><br>
7. Wählen Sie **Quelle erstellen**.
8. Gehen Sie auf die Registerkarte **Implementierungsdetails** und notieren Sie sich die **API URL** und den **Schreibschlüssel**.<br><br>![Implementierungsdetails für Braze Currents, die die API-URL und den Schreibschlüssel enthalten.][2]

### Schritt 2: Konfigurieren Sie das Daten-Streaming in Currents

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Datenexport**.
2. Wählen Sie **Neuen Strom erstellen** und **Benutzerdefinierte Ströme exportieren**.<br><br>![Die Schaltfläche "Neuen Strom erstellen" mit einem Dropdown-Menü, das "Export von benutzerdefinierten Strömen" enthält.][3]{: style="max-width:60%;"}<br><br>
3. Geben Sie einen Integrationsnamen und eine E-Mail ein, um bei Fehlern mit der Integration kontaktiert zu werden.
4. Geben Sie unter **Credentials** die folgenden Informationen ein, die Sie in [Schritt 1](#step-1-create-a-currents-source) notiert haben:
- Die API-URL als **Endpunkt**
- Der Schreibschlüssel als **Überbringer** des **Tokens**<br><br>![Abschnitte zur Eingabe von Integrationsdetails und Anmeldeinformationen.][4]<br><br>
5. Wählen Sie die Nachrichtenereignisse, die Sie an Zeotap senden möchten.<br><br>![Die Registerkarte "Allgemeine Einstellungen" mit einem Abschnitt zur Auswahl von Ereignissen für die Einbindung von Nachrichten.][5]
6. Wählen Sie **Aktuelles starten**, um die Änderungen zu speichern und Ereignisse an Zeotap zu senden.

{% alert important %}
Der Currents Connector unterstützt keine anonymen Benutzer (Benutzer ohne `external_id`).
{% endalert %}

[1]: {% image_buster /assets/img/zeotap/cec.png %}
[2]: {% image_buster /assets/img/zeotap/implementation_details.png %}
[3]: {% image_buster /assets/img/zeotap/custom_currents_export.png %}
[4]: {% image_buster /assets/img/zeotap/credentials.png %}
[5]: {% image_buster /assets/img/zeotap/message_engagement_events.png %}
[6]: {% image_buster /assets/img/zeotap/select_region.png %}