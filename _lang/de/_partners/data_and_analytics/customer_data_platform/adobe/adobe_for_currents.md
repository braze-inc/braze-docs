---
nav_title: Adobe für Currents
article_title: Adobe für Currents
alias: /partners/adobe_for_currents/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze-Currents und Adobe, einer Kundendaten-Plattform, die es Marken erlaubt, ihre Daten von Adobe (angepasste Attribute und Segmente) mit Braze zu verbinden und in Realtime abzubilden."
page_type: partner
tool: Currents
search_tag: Partner
---

# Adobe für Currents

> [Adobe](https://www.adobe.com/) ist eine Customer Data Platform (CDP), die es Marken erlaubt, ihre Daten von Adobe (angepasste Attribute und Segmente) mit Braze zu verbinden und in Echtzeit abzubilden.

Die Integration von Braze und Adobe erlaubt es Ihnen, den Informationsfluss zwischen den beiden Systemen nahtlos zu steuern. Mit [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) können Sie auch Daten mit Adobe verbinden, um sie über den gesamten Growth Stack hinweg nutzbar zu machen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Currents | Um Daten zurück in Adobe zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
| Adobe Experience Platform-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Adobe Experience Platform-Konto](https://experience.adobe.com/#/platform/home). |
| Erlaubnis zum Erstellen eines Konnektors | Sie benötigen die Berechtigung, eine Verbindung zu einer Streaming-Quelle herzustellen, um diese Integration nutzen zu können. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erstellen eines XDM-Schemas in Adobe

1. Gehen Sie in Adobe Experience Platform zu **Schemas** > wählen Sie **Schema erstellen** > wählen Sie **Experience Event** > wählen Sie **Weiter**.<br><br>![Adobe Schemas Seite für das Schema mit dem Namen "Braze-Currents Walk-Through".]({% image_buster /assets/img/adobe/currents_sources.png %})<br><br>
2. Geben Sie einen Namen und eine Beschreibung für Ihr Schema an. 
3. Im Panel **Komposition** konfigurieren Sie Ihre Schema Attribute:
- Wählen Sie unter **Feldgruppen** die Option **Hinzufügen** und fügen Sie dann die Feldgruppe **Braze-Currents Nutzer:in** hinzu.
- Wählen Sie **Speichern**.

Weitere Informationen zu Schemas finden Sie in der Dokumentation von Adobe zur [Erstellung von Schemas](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui).

### Schritt 2: Verbinden Sie Braze mit der Adobe Experience Platform

1. Gehen Sie in Adobe Experience Platform zu **Quellen** > **Katalog** > **Marketing-Automatisierung**.
2. Wählen Sie **Daten hinzufügen** für Braze-Currents.
3. Laden Sie die [Braze-Currents Beispieldatei](https://github.com/Appboy/currents-examples/blob/master/sample-data/Adobe/adobe_examples.json) hoch.<br><br>![Adobe "Seite mit Daten hinzufügen".]({% image_buster /assets/img/adobe/currents_add_data.png %})<br><br>
4. Nachdem Sie Ihre Datei hochgeladen haben, geben Sie Ihre Datenflussdetails an, einschließlich Informationen über Ihren Datensatz und das Schema, auf das Sie abbilden wollen. 
    - Wenn Sie zum ersten Mal eine Braze-Currents-Quelle anschließen, erstellen Sie einen neuen Datensatz und stellen Sie sicher, dass Sie das in [Schritt 1](#step-1-create-an-xdm-schema-in-adobe) erstellte Schema verwenden. 
    - Wenn Sie dies nicht zum ersten Mal tun, verwenden Sie einen vorhandenen Datensatz, der auf das Braze-Schema referenziert.
5. Konfigurieren Sie die Abbildung für Ihre Daten und lösen Sie die Probleme.
    - Ändern Sie die Abbildung für `id` von `to _braze.appID` auf `_id` auf der Stammebene des Schemas.
    - Stellen Sie sicher, dass `properties.is_amp` auf `_braze.messaging.email.isAMP` abgebildet ist.
    - Löschen Sie die Abbildung `time` und `timestamp`, wählen Sie dann das Symbol Hinzufügen > **Berechnetes Feld hinzufügen** und geben Sie **Zeit * 1000** ein. Wählen Sie **Speichern**.
    - Wählen Sie **Zielfeld** neben dem neuen Quellfeld auswählen und ordnen Sie es dem **Zeitstempel** auf der Stammebene des Schemas zu. <br><br>![Adobe Seite "Daten hinzufügen" mit Abbildungen.]({% image_buster /assets/img/adobe/currents_mapping.png %})<br><br>
6. Wählen Sie **Validieren**, um zu bestätigen, dass Sie die Probleme gelöst haben.

{% alert important %}
Die Zeitstempel von Braze werden in Sekunden angegeben. Um Zeitstempel in Adobe Experience Platform genau wiederzugeben, müssen Ihre berechneten Felder in Millisekunden angegeben werden. Um Sekunden in Millisekunden umzurechnen, verwenden Sie die Berechnung **time * 1000**.
{% endalert %}

{: start="7"}
7\. Wählen Sie **Weiter**, überprüfen Sie Ihre Datenflussdetails und wählen Sie dann **Fertig stellen**.<br><br>![Adobe Seite "Daten hinzufügen" ohne Fehler bei der Abbildung.]({% image_buster /assets/img/adobe/currents_no_errors.png %})

### Schritt 3: Erfassen von Zugangsdaten

Sammeln Sie die folgenden Daten, um sie in Braze einzugeben, damit Braze Daten an die Adobe Experience Platform senden kann.

| Feld         |Beschreibung                          |
|---------------|-------------------------------------|
| Client-ID     | Die Client-ID, die mit Ihrer Adobe Experience Platform-Quelle verknüpft ist. |
| Client-Geheimnis | Das Client-Geheimnis, das mit Ihrer Adobe Experience Platform-Quelle verknüpft ist. |
| Mandanten-ID     | Die mit Ihrer Adobe Experience Platform-Quelle verbundene Tenant ID. |
| Sandbox-Name  | Die Sandbox, die mit Ihrer Adobe Experience Platform-Quelle verbunden ist.   |
| Datenfluss-ID   | Die Dataflow ID, die mit Ihrer Adobe Experience Platform-Quelle verknüpft ist.   |
| Streaming-Endpunkt  | Der Endpunkt für das Streamen, der mit Ihrer Adobe Experience Platform-Quelle verbunden ist. Braze konvertiert dies automatisch in den Endpunkt für das Batch-Streaming. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Schritt 4: Konfigurieren Sie Currents zum Streamen von Daten zu Ihrer Datenquelle

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Datenexport**, und wählen Sie dann **Neue Currents erstellen**. 
2. Geben Sie Folgendes an:
    - Ein Name für den Konnektor
    - Kontaktinformationen für Benachrichtigungen über den Konnektor
    - Die Zugangsdaten aus [Schritt 3](#step-3-gather-credentials)
3. Wählen Sie die Ereignisse aus, die Sie empfangen möchten.
4. Konfigurieren Sie optional alle gewünschten Feldausschlüsse oder Transformationen.
5. Wählen Sie **Launch Current**.

