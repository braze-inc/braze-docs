---
nav_title: Adobe für Currents
article_title: Adobe für Currents
alias: /partners/adobe_for_currents/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze Currents und Adobe, einer Plattform für Kundendaten, die es Marken ermöglicht, ihre Adobe-Daten (benutzerdefinierte Attribute und Segmente) mit Braze in Echtzeit zu verbinden und abzubilden."
page_type: partner
tool: Currents
search_tag: Partner
---

# Adobe für Currents

> [Adobe](https://www.adobe.com/) ist eine Plattform für Kundendaten, die es Marken ermöglicht, ihre Adobe-Daten (benutzerdefinierte Attribute und Segmente) mit Braze in Echtzeit zu verbinden und abzubilden.

Die Integration von Braze und Adobe ermöglicht es Ihnen, den Informationsfluss zwischen den beiden Systemen nahtlos zu steuern. Mit [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) können Sie auch Daten mit Adobe verknüpfen, um sie für das gesamte Wachstumsprogramm nutzbar zu machen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Currents | Um Daten zurück in Adobe zu exportieren, müssen Sie [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
| Adobe Experience Platform-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Adobe Experience Platform-Konto](https://experience.adobe.com/#/platform/home). |
| Erlaubnis zum Erstellen eines Connectors | Sie benötigen die Berechtigung zum Erstellen einer Streaming-Quellenverbindung, um diese Integration nutzen zu können. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erstellen eines XDM-Schemas in Adobe

1. Gehen Sie in Adobe Experience Platform zu **Schemas** > wählen Sie **Schema erstellen** > wählen Sie **Experience Event** > wählen Sie **Weiter**.<br><br>![Adobe Schemas Seite für das Schema mit dem Namen "Braze Currents Walk-Through".][1]<br><br>
2. Geben Sie einen Namen und eine Beschreibung für Ihr Schema an. 
3. Konfigurieren Sie im **Kompositionsbereich** Ihre Schemaattribute:
- Wählen Sie unter **Feldgruppen** die Option **Hinzufügen** und fügen Sie dann die Feldgruppe **Braze Currents Benutzerereignis** hinzu.
- Wählen Sie **Speichern**.

Weitere Informationen zu Schemas finden Sie in der Dokumentation von Adobe zur [Erstellung von Schemas](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui).

### Schritt 2: Verbinden Sie Braze mit der Adobe Experience Platform

1. Gehen Sie in Adobe Experience Platform zu **Quellen** > **Katalog** > **Marketingautomatisierung**.
2. Wählen Sie **Daten** für Braze Currents **hinzufügen**.
3. Laden Sie die [Braze Currents Beispieldatei](https://github.com/Appboy/currents-examples/blob/master/sample-data/Adobe/adobe_examples.json) hoch.<br><br>![Adobe "Datenseite hinzufügen".][2]<br><br>
4. Nachdem Sie Ihre Datei hochgeladen haben, geben Sie die Details zu Ihrem Datenfluss an, einschließlich der Informationen zu Ihrem Datensatz und dem Schema, das Sie zuordnen möchten. 
    - Wenn Sie zum ersten Mal eine Braze Currents-Quelle anschließen, erstellen Sie einen neuen Datensatz und stellen Sie sicher, dass Sie das in [Schritt 1](#step-1-create-an-xdm-schema-in-adobe) erstellte Schema verwenden. 
    - Wenn Sie dies nicht zum ersten Mal tun, verwenden Sie einen vorhandenen Datensatz, der auf das Braze-Schema verweist.
5. Konfigurieren Sie das Mapping für Ihre Daten und lösen Sie die Probleme.
    - Ändern Sie die Zuordnung für `id` von `to _braze.appID` in `_id` auf der Stammebene des Schemas.
    - Stellen Sie sicher, dass `properties.is_amp` auf `_braze.messaging.email.isAMP` abgebildet ist.
    - Löschen Sie die Zuordnungen `time` und `timestamp`, wählen Sie dann das Symbol Hinzufügen > **Berechnetes Feld hinzufügen** und geben Sie **Zeit * 1000** ein. Wählen Sie **Speichern**.
    - Wählen Sie **Zielfeld zuordnen** neben dem neuen Quellfeld und ordnen Sie es dem **Zeitstempel** auf der Stammebene des Schemas zu. <br><br>![Adobe Seite "Daten hinzufügen" mit Mappings.][3]<br><br>
6. Wählen Sie **Validieren**, um zu bestätigen, dass Sie die Probleme behoben haben.

{% alert important %}
Die Zeitstempel von Braze werden in Sekunden angegeben. Um Zeitstempel in Adobe Experience Platform genau wiederzugeben, müssen Ihre berechneten Felder in Millisekunden angegeben werden. Um Sekunden in Millisekunden umzurechnen, verwenden Sie die Berechnung **time * 1000**.
{% endalert %}

{: start="7"}
7\. Wählen Sie **Weiter**, überprüfen Sie Ihre Datenflussdetails und wählen Sie dann **Fertig stellen**.<br><br>![Adobe Seite "Daten hinzufügen" ohne Zuordnungsfehler.][4]

### Schritt 3: Berechtigungsnachweise sammeln

Sammeln Sie die folgenden Angaben, um sie in Braze einzugeben, damit Braze Daten an die Adobe Experience Platform senden kann.

| Feld         |Beschreibung                          |
|---------------|-------------------------------------|
| Client-ID     | Die Client-ID, die mit Ihrer Adobe Experience Platform-Quelle verknüpft ist. |
| Client-Geheimnis | Das Client-Geheimnis, das mit Ihrer Adobe Experience Platform-Quelle verknüpft ist. |
| Mandanten-ID     | Die Mieter-ID, die mit Ihrer Adobe Experience Platform-Quelle verknüpft ist. |
| Sandbox-Name  | Die Sandbox, die mit Ihrer Adobe Experience Platform-Quelle verbunden ist.   |
| Datenfluss-ID   | Die Datenfluss-ID, die mit Ihrer Adobe Experience Platform-Quelle verknüpft ist.   |
| Streaming-Endpunkt  | Der Streaming-Endpunkt, der mit Ihrer Adobe Experience Platform-Quelle verbunden ist. Braze konvertiert dies automatisch in den Batch-Streaming-Endpunkt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Schritt 4: Konfigurieren Sie Currents für das Streaming von Daten zu Ihrer Datenquelle

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Datenexport** und wählen Sie dann **Neuen Strom erstellen**. 
2. Geben Sie Folgendes an:
    - Ein Name für den Anschluss
    - Kontaktinformationen für Benachrichtigungen über den Connector
    - Die Anmeldeinformationen aus [Schritt 3](#step-3-gather-credentials)
3. Wählen Sie die Ereignisse aus, die Sie erhalten möchten.
4. Konfigurieren Sie optional alle gewünschten Feldausschlüsse oder Transformationen.
5. Wählen Sie **Aktuelles starten**.

[1]: {% image_buster /assets/img/adobe/currents_sources.png %}
[2]: {% image_buster /assets/img/adobe/currents_add_data.png %}
[3]: {% image_buster /assets/img/adobe/currents_mapping.png %}
[4]: {% image_buster /assets/img/adobe/currents_no_errors.png %}