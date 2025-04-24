---
nav_title: Über Webhooks
article_title: Über Webhooks
page_order: 0
channel:
  - webhooks
description: "Dieser Referenzartikel behandelt die Grundlagen von Webhooks, einschließlich gängiger Anwendungsfälle, der Webhook-Anatomie und ihrer Verwendung in Braze."

---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"}Über Webhooks

> Dieser Referenzartikel behandelt die Grundlagen von Webhooks, um Ihnen die Bausteine an die Hand zu geben, die Sie zum Erstellen Ihrer eigenen Webhooks benötigen. Suchen Sie nach Schritten, wie Sie einen Webhook in Braze erstellen können? Siehe [Erstellen eines Webhooks][1].

Webhooks sind ein gängiger Weg für Anwendungen, um Daten in Echtzeit auszutauschen. Heutzutage haben wir selten eine einzige Anwendung, die alles kann. Meistens arbeiten Sie mit vielen verschiedenen Anwendungen oder Systemen, die auf bestimmte Aufgaben spezialisiert sind, und diese Anwendungen müssen alle miteinander kommunizieren können. Hier kommen die Webhooks ins Spiel.

Ein Webhook ist eine automatische Nachricht von einem System an ein anderes, nachdem ein bestimmtes Kriterium erfüllt wurde. In Braze ist dieses Kriterium normalerweise das Triggern eines angepassten Events.

Im Kern ist ein Webhook eine Event-basierte Methode für zwei getrennte Systeme, um auf der Grundlage von in Echtzeit übermittelten Daten effektive Maßnahmen zu ergreifen. Diese Nachricht enthält Anweisungen, die dem empfangenden System mitteilen, wann und wie es eine bestimmte Aufgabe ausführen soll. Aus diesem Grund können Sie mit Webhooks dynamischer und flexibler auf Daten und programmatische Funktionen zugreifen und Customer Journeys einrichten, die Ihre Prozesse rationalisieren.

## Anwendungsfälle

Webhooks sind eine hervorragende Möglichkeit, Ihre Systeme miteinander zu verbinden – schließlich kommunizieren Apps über Webhooks. Hier sind einige allgemeine Szenarien, in denen Webhooks besonders nützlich sein können:

- Senden von Daten an und von Braze
- Senden von Nachrichten an Ihre Kund:innen über Kanäle, die nicht direkt von Braze unterstützt werden
- Posten in Braze-APIs

Einige spezifischere Anwendungsfälle sind die folgenden:

- Wenn sich ein Benutzer von einer E-Mail abmeldet, können Sie über einen Webhook Ihre Analysedatenbank oder Ihr CRM mit denselben Informationen aktualisieren und so einen ganzheitlichen Überblick über das Verhalten dieses Benutzers erhalten.
- Senden Sie [Transaktionsnachrichten]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) an Benutzer über Facebook Messenger oder Line.
- Senden Sie Direkt-Mailing an Kund:innen als Reaktion auf ihre In-App- und Internet-Aktivitäten, indem Sie Webhooks zur Kommunikation mit Diensten von Drittanbietern wie [Lob.com]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/lob/) verwenden.
- Wenn ein Spieler ein bestimmtes Level erreicht oder eine bestimmte Anzahl von Punkten sammelt, verwenden Sie Webhooks und Ihre bestehende API-Einrichtung, um ihm ein Charakter-Upgrade oder Münzen direkt auf sein Konto zu schicken. Wenn Sie den Webhook als Teil einer Multichannel-Messaging-Kampagne versenden, können Sie gleichzeitig eine Push- oder andere Nachricht senden, um den Gamer über die Belohnung zu informieren.
- Wenn Sie eine Fluggesellschaft sind, können Sie Webhooks und Ihre bestehende API-Einrichtung nutzen, um dem Konto eines Kunden einen Rabatt gutzuschreiben, nachdem dieser eine bestimmte Anzahl von Flügen gebucht hat.
- Unzählige „If This Then That“ ([IFTTT](https://ifttt.com/about))-Vorgehensweisen – wenn sich ein:e Kund:in beispielsweise per E-Mail bei der App anmeldet, kann diese Adresse automatisch in Salesforce konfiguriert werden.

## Anatomie eines Webhooks

Ein Webhook besteht aus den folgenden drei Teilen:

![Beispiel-Webhook, aufgeteilt in HTTP-Methode, HTTP-URL und Anfragetext. Siehe die folgende Tabelle für weitere Einzelheiten.][2]

| Teil von Webhook | Beschreibung |
| --- | --- |
| [HTTP-Methode](#methods) | Wie APIs benötigen auch Webhooks Anfragemethoden. Diese werden an die URL weitergegeben, auf die der Webhook zugreift, und teilen dem Endpunkt mit, was er mit den gegebenen Informationen tun soll. Es gibt vier HTTP-Methoden, die Sie angeben können: POST, GET, PUT und DELETE. |
| HTTP-URL | Die URL-Adresse Ihres Webhook-Endpunkts. Der Endpunkt ist der Ort, an den Sie die Informationen senden, die Sie im Webhook erfassen. |
| Anfragetext | Dieser Teil des Webhooks enthält die Informationen, die Sie an den Endpunkt übermitteln. Der Anfragetext kann aus JSON Schlüssel-Wert-Paaren oder Rohtext bestehen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### HTTP-Methoden {#methods}

Die folgende Tabelle beschreibt die vier verschiedenen HTTP-Methoden, die Sie in Ihrem Webhook angeben können.

| HTTP-Methode | Beschreibung |
| ----------- | ----------- |
| POST | Diese Methode schreibt neue Informationen auf den Empfangsserver. Ein gängiges Beispiel für die POST-Methode in einer realen Anwendung ist ein [Kontaktformular](https://www.braze.com/company/contact) auf einer Website. Alle Informationen, die Sie in das Formular eingeben, werden Teil einer Anfrage und werden an eine:n Empfänger:in gesendet. Dies ist die gängigste Methode, um Daten zu versenden.
| GET | Diese Methode ruft vorhandene Informationen ab, anstatt neue Informationen zu schreiben. Per Definition unterstützt eine GET-Anfrage keinen Anfragetext. Dies ist die gebräuchlichste Methode, um Daten von einem Server abzufragen. Nehmen wir zum Beispiel den [Endpunkt`/segments/list` ]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). Wenn Sie eine GET-Anfrage stellen, wird eine Liste Ihrer Segmente zurückgegeben.
| PUT | Diese Methode aktualisiert die Informationen des Endpunkts und ersetzt alle vorhandenen Informationen durch die Angaben im Anfragetext. 
| LÖSCHEN | Diese Methode löscht die Ressource in der HTTP-URL. 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Webhaken in Braze

In Braze können Sie einen Webhook als Webhook-Kampagne, API-Kampagne oder Canvas-Komponente erstellen.

{% tabs %}
{% tab Webhook-Kampagne %}

1. Gehen Sie im Dashboard von Braze zu **Kampagnen**.
2. Klicken Sie auf **Kampagne erstellen** und wählen Sie **Webhook**.

Weitere Informationen finden Sie unter [Erstellen eines Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).

{% endtab %}
{% tab API-Kampagne %}

1. Gehen Sie im Dashboard von Braze zu **Kampagnen**.
2. Klicken Sie auf **Kampagne erstellen** und wählen Sie **API-Kampagne**.
3. Klicken Sie auf **Nachrichten hinzufügen** und wählen Sie **Webhook**.
4. Formatieren Sie Ihren API-Aufruf so, dass er ein [Webhook-Objekt]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/) enthält.

Weitere Informationen finden Sie unter [Erstellen eines Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).

{% endtab %}
{% tab Canvas-Komponente %}

1. Erstellen Sie in Ihrem Canvas eine neue Komponente.
2. Wählen Sie im Abschnitt **Nachricht** Ihrer Komponente die Option **Webhook**.

Weitere Informationen finden Sie unter [Erstellen eines Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).

{% endtab %}
{% endtabs %}


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[2]: {% image_buster /assets/img_archive/webhook_anatomy.png %}
