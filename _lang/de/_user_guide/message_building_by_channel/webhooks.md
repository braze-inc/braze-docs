---
nav_title: Webhooks
article_title: Webhooks
page_order: 4
layout: dev_guide
alias: /about_webhooks/
guide_top_header: "Webhooks"
guide_top_text: "Webhooks sind ein gängiger Weg für Anwendungen, um Daten in Echtzeit auszutauschen. Heutzutage haben wir selten eine einzige Anwendung, die alles kann. Meistens arbeiten Sie mit vielen verschiedenen Anwendungen oder Systemen, die auf bestimmte Aufgaben spezialisiert sind, und diese Anwendungen müssen alle miteinander kommunizieren können. Hier kommen die Webhooks ins Spiel. <br><br> Ein Webhook ist eine automatische Nachricht von einem System an ein anderes, nachdem ein bestimmtes Kriterium erfüllt wurde. In Braze ist dieses Kriterium normalerweise das Triggern eines angepassten Events. <br><br>Im Kern ist ein Webhook eine Event-basierte Methode für zwei getrennte Systeme, um auf der Grundlage von in Echtzeit übermittelten Daten effektive Maßnahmen zu ergreifen. Diese Nachricht enthält Anweisungen, die dem empfangenden System mitteilen, wann und wie es eine bestimmte Aufgabe ausführen soll. Aus diesem Grund können Sie mit Webhooks dynamischer und flexibler auf Daten und programmatische Funktionen zugreifen und Customer Journeys einrichten, die Ihre Prozesse rationalisieren. <br><br>**Die Verfügbarkeit von Webhooks hängt von Ihrem Braze-Paket ab. Wenden Sie sich an Ihren oder Ihre Account Manager:in oder Customer-Success-Manager:in, um loszulegen.**"
description: "Diese Startseite ist der Ausgangspunkt für Webhooks. Hier finden Sie Artikel zur Erstellung von Webhooks, zur Erstellung von Webhook-Vorlagen und zu Braze-to-Braze-Webhooks."
channel:
  - webhooks
search_rank: 3
guide_featured_title: "Abschnittsartikel"
guide_featured_list:
- name: Einen Webhook erstellen
  link: /docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Erstellen einer Webhook-Vorlage
  link: /docs/user_guide/message_building_by_channel/webhooks/webhook_template/
  image: /assets/img/braze_icons/table.svg
- name: Braze-to-Braze Webhooks
  link: /docs/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/
  image: /assets/img/braze_icons/switch-horizontal-01.svg
- name: Berichterstattung
  link: /docs/user_guide/message_building_by_channel/webhooks/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Fehlerbehebung bei Webhook-Anfragen 
  link: /docs/help/help_articles/api/webhook_connected_content_errors/
  image: /assets/img/braze_icons/check-square-broken.svg
---

## [![Braze Lernkurse]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"} Anwendungsfälle

Webhooks sind eine hervorragende Möglichkeit, Ihre Systeme miteinander zu verbinden – schließlich kommunizieren Apps über Webhooks. Hier sind einige allgemeine Szenarien, in denen Webhooks besonders nützlich sein können:

- Senden von Daten an und von Braze
- Senden von Nachrichten an Ihre Kund:innen über Kanäle, die nicht direkt von Braze unterstützt werden
- Posten in Braze-APIs

Einige spezifischere Anwendungsfälle sind die folgenden:

- Wenn sich ein Benutzer von einer E-Mail abmeldet, können Sie über einen Webhook Ihre Analysedatenbank oder Ihr CRM mit denselben Informationen aktualisieren und so einen ganzheitlichen Überblick über das Verhalten dieses Benutzers erhalten.
- Senden Sie [Transaktionsnachrichten]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) an Benutzer über Facebook Messenger oder Line.
- Senden Sie Direkt-Mailing an Kund:innen als Reaktion auf ihre In-App- und Internet-Aktivitäten, indem Sie Webhooks zur Kommunikation mit Diensten von Drittanbietern wie [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/) verwenden.
- Wenn ein Spieler ein bestimmtes Level erreicht oder eine bestimmte Anzahl von Punkten sammelt, verwenden Sie Webhooks und Ihre bestehende API-Einrichtung, um ihm ein Charakter-Upgrade oder Münzen direkt auf sein Konto zu schicken. Wenn Sie den Webhook als Teil einer Multichannel-Messaging-Kampagne versenden, können Sie gleichzeitig eine Push- oder andere Nachricht senden, um den Gamer über die Belohnung zu informieren.
- Wenn Sie eine Fluggesellschaft sind, können Sie Webhooks und Ihre bestehende API-Einrichtung nutzen, um dem Konto eines Kunden einen Rabatt gutzuschreiben, nachdem dieser eine bestimmte Anzahl von Flügen gebucht hat.
- Unzählige „If This Then That“ ([IFTTT](https://ifttt.com/about))-Vorgehensweisen – wenn sich ein:e Kund:in beispielsweise per E-Mail bei der App anmeldet, kann diese Adresse automatisch in Salesforce konfiguriert werden.

## Anatomie eines Webhooks

Ein Webhook besteht aus den folgenden Teilen.

| Teil von Webhook | Beschreibung |
| --- | --- |
| [HTTP-Methode](#methods) | Wie APIs benötigen auch Webhooks Anfragemethoden. Diese werden an die URL weitergegeben, auf die der Webhook zugreift, und teilen dem Endpunkt mit, was er mit den gegebenen Informationen tun soll. Es gibt vier HTTP-Methoden, die Sie angeben können: POST, GET, PUT und DELETE. |
| HTTP-URL | Die URL-Adresse Ihres Webhook-Endpunkts. Der Endpunkt ist der Ort, an den Sie die Informationen senden, die Sie im Webhook erfassen. |
| Anfragetext | Dieser Teil des Webhooks enthält die Informationen, die Sie an den Endpunkt übermitteln. Der Anfragetext kann aus JSON Schlüssel-Wert-Paaren oder Rohtext bestehen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Beispiel-Webhook mit einer HTTP-Methode, einer HTTP-URL und einem Body der Anfrage.]({% image_buster /assets/img_archive/webhook_anatomy.png %})

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
{% tab Webhook Campaign %}

1. Gehen Sie im Dashboard von Braze zu **Kampagnen**.
2. Klicken Sie auf **Kampagne erstellen** und wählen Sie **Webhook**.

Weitere Informationen finden Sie unter [Erstellen eines Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).

{% endtab %}
{% tab API Campaign %}

1. Gehen Sie im Dashboard von Braze zu **Kampagnen**.
2. Klicken Sie auf **Kampagne erstellen** und wählen Sie **API-Kampagne**.
3. Klicken Sie auf **Nachrichten hinzufügen** und wählen Sie **Webhook**.
4. Formatieren Sie Ihren API-Aufruf so, dass er ein [Webhook-Objekt]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/) enthält.

Weitere Informationen finden Sie unter [Erstellen eines Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).

{% endtab %}
{% tab Canvas Component %}

1. Erstellen Sie in Ihrem Canvas eine neue Komponente.
2. Wählen Sie im Abschnitt **Nachricht** Ihrer Komponente die Option **Webhook**.

Weitere Informationen finden Sie unter [Erstellen eines Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).

{% endtab %}
{% endtabs %}

## Webhook-Fehlerbehandlung und Rate-Limiting

Wenn Braze eine Fehlerantwort von einem Webhook-Aufruf erhält, passen wir das Sendeverhalten dieses Webhooks automatisch auf der Grundlage dieser Antwort-Header an:

- `Retry-After`
- `X-Rate-Limit-Limit`
- `X-Rate-Limit-Remaining`
- `X-Rate-Limit-Reset`

Diese Header helfen uns, Rate-Limits zu interpretieren und die Sendegeschwindigkeit entsprechend anzupassen, um weitere Fehler zu vermeiden. Wir setzen außerdem eine exponentielle Backoff Strategie für Wiederholungsversuche ein, die das Risiko einer Überlastung Ihrer Server durch zeitlich gestaffelte Wiederholungsversuche verringert.

Wenn wir feststellen, dass die Mehrheit der Webhook-Anfragen an einen bestimmten Host fehlschlägt, werden wir alle Sendeversuche an diesen Host vorübergehend zurückstellen. Nach einer bestimmten Abkühlungszeit setzen wir den Sendevorgang fort, damit sich Ihr System erholen kann.


