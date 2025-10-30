---
nav_title: Kampagnen und Canvase
article_title: "Erste Schritte: Kampagnen und Canvase"
page_order: 3
page_type: reference
description: "Dieser Artikel bietet einen Überblick über die verschiedenen Möglichkeiten, wie Sie mit Braze Nachrichten versenden können."

---

# Erste Schritte: Kampagnen und Canvase

In Braze können Sie Nachrichten entweder über eine [Kampagne](#campaigns) oder ein [Canvas](#canvas) versenden.

- Wählen Sie eine Kampagne aus, um eine bestimmte Nachricht an eine Nutzergruppe zu senden. Eine Kampagne ist ein einzelner Schritt, um mit Ihren Nutzern über verschiedene Nachrichtenkanäle in Kontakt zu treten.
- Wenn Sie eine Reihe fortlaufender Nachrichten im Rahmen einer übergreifenden Customer Journey versenden möchten, wählen Sie Canvas, unser Tool zur Orchestrierung der Customer Journey. Während Kampagnen gut geeignet sind, um einfache, zielgerichtete Nachrichten zu versenden, können Sie mit Canvases Ihre Beziehungen zu Kunden auf die nächste Stufe heben.

## Kampagnen

Obwohl Kampagnen je nach Kanal unterschiedlich gestaltet werden können, gibt es in Braze vier Haupttypen von Kampagnen, die Sie kennen sollten:

| Art der Kampagne        | Beschreibung                                                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Regulär              | Dies ist die häufigste Art von Kampagnen. Sie können je nach Kommunikationszielen einen oder mehrere Kanäle ansprechen und Ihre Inhalte mit visuellen Editoren direkt in Braze gestalten, anpassen und testen. Erfahren Sie, wie Sie [eine Kampagne erstellen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) können. |
| A/B-Tests          | Bei Kampagnen, die auf einen einzigen Kanal abzielen, können Sie mehr als eine Version derselben Kampagne versenden und sehen, welche davon am besten abschneidet. Mit [multivariaten Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) können Sie Texte, Personalisierungen usw. in bis zu acht verschiedenen Varianten testen. |
| API                  | Mit [API-Kampagnen]({{site.baseurl}}/api/api_campaigns/) können Sie im Handumdrehen termingerechte Nachrichten versenden. Im Gegensatz zu anderen Kampagnentypen legen Sie im Braze-Dashboard weder die Nachricht noch die Empfänger oder den Zeitplan fest. Stattdessen übergeben Sie diese Bezeichner in Ihren API-Aufrufen. Diese werden in der Regel für Echtzeit-Transaktionsnachrichten oder aktuelle Nachrichten verwendet.  |
| Transaktions-E-Mails | Braze [Transaktions-E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/) sind speziell für den Versand automatisierter, nicht werblicher E-Mail-Nachrichten konzipiert, um eine vereinbarte Transaktion zwischen Ihnen und Ihren Kunden zu erleichtern. Sie senden geschäftskritische Benachrichtigungen an einen einzelnen Benutzer, bei denen Geschwindigkeit von größter Bedeutung ist. *Verfügbar für ausgewählte Pakete.* |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Regelmäßige Kampagnen und A/B-Testkampagnen können geplant werden (z. B. um eine Liste von Nutzern über eine bevorstehende Veranstaltung zu informieren) oder automatisch als Reaktion auf eine Nutzeraktion versendet werden (z. B. um eine E-Mail zu senden, wenn jemand Ihren Newsletter abonniert hat). Erfahren Sie mehr über die [Planung von Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types).
{% endalert %}

Unabhängig von der Art der Kampagne, die Sie erstellen, können Ihre Kampagnen auf die Bedürfnisse Ihrer Nutzer eingehen und eine durchdachte, personalisierte Antwort liefern. Nachdem Sie Ihre Kampagne verschickt haben, können Sie mit unseren [integrierten Analysetools]({{site.baseurl}}/user_guide/analytics/reporting/) sehen, wie sie abgeschnitten hat und wie viele Nutzer auf der Grundlage Ihrer [Conversion Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) konvertiert haben.

Hier erfahren Sie mehr über Braze-Kampagnen:

- Braze Learning: [Kampagnen einrichten](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [Kampagnen erstellen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign)
- [Ideen und Strategien]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies)

## Canvas

Anstatt sporadische Nachrichten über mehrere Kampagnen hinweg zu versenden, schaffen Canvases eine kontinuierliche, fließende Konversation mit den Nutzern. Das liegt daran, dass sich die Reise eines Nutzers durch ein Canvas in verschiedene Pfade aufteilen kann, je nachdem, was er mit Ihrer Marke macht (oder nicht macht). So können Sie die Nutzer automatisch und in Echtzeit durch einen bestimmten Fluss führen.

\![]({% image_buster /assets/img/getting_started/canvas_flow.png %})

So können Sie mit Canvasen Nutzer:innen erfassen, die den Konversionspfad verlassen haben, und sie in die am besten geeignete Outreach-Initiative einbinden.

Wenn Sie ein Canvas erstellen, folgen Sie vielen der gleichen Schritte wie bei der Einrichtung einer Kampagne: Sie legen eine allgemeine Zielgruppe, Teilnahmebedingungen und Sendeeinstellungen fest. Ihr Canvas startet, wenn jemand Ihre Auslösebedingung erfüllt. Dann wird ein Pfad im Canvas durchlaufen, bis Ihre Exit-Bedingungen erfüllt sind.

Ihr Canvas kann eine beliebige Kombination von [Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), [Verzögerungen]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), [Experimenten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) und mehr enthalten. Sie können Nachrichten auf allen unterstützten Kommunikationskanälen versenden und sie sogar [in soziale Netzwerke und Werbeplattformen wie Facebook, Google oder TikTok einbinden]({{site.baseurl}}/partners/canvas_audience_sync/overview/).

Schauen Sie sich diese zusätzlichen Ressourcen an, um mehr über Canvas zu erfahren:

- Braze Learning: [User Journeys mit Canvas Flow](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [Canvase erstellen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
- [Canvas-Rahmen]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_outlines/)

## Messaging-Kanäle

Messaging-Kanäle sind die verschiedenen Kommunikationskanäle, über die Sie mit Ihren Kunden in Kontakt treten und gezielte Nachrichten übermitteln können. 

\![]({% image_buster /assets/img/getting_started/channels.png %})

Die folgende Tabelle gibt einen Überblick über die von uns unterstützten Kanäle.

| Kanal                                                                                              | Beschreibung                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [E-Mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)                        | Senden Sie personalisierte E-Mails an die Posteingänge Ihrer Benutzer.                                                                                                       |
| [Mobile Push-Benachrichtigung]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)                   | Liefern Sie Nachrichten als Benachrichtigungen direkt an die mobilen Geräte der Benutzer.                                                                                   |
| [Web-Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/web)                         | Schicken Sie Benachrichtigungen an Webbrowser, auch wenn Ihre Website dort gar nicht geöffnet ist.                                                         |
| [In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)    | Zeigen Sie Nachrichten in Ihrer mobilen App an, wenn diese aktiv genutzt wird.                                                                             |
| [SMS, MMS und RCS*]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/)                   | Senden Sie Textnachrichten an die Mobiltelefone der Benutzer.                                                                                                            |
| [WhatsApp*]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)              | Senden Sie Nachrichten über die beliebte Messaging-Plattform WhatsApp, um Ihre Nutzer zu erreichen und mit ihnen in Kontakt zu treten.                                                   |
| [Banner*]({{site.baseurl}}/user_guide/message_building_by_channel/banners/)       | Betten Sie Nachrichten direkt in Ihre App oder Website ein. |
| [Content-Cards*]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)       | Bieten Sie einen Posteingang in Ihrer App oder Website an, in dem Benutzer Nachrichten empfangen und mit ihnen interagieren können, oder zeigen Sie Nachrichten in einem Karussell, als Banner und mehr an. |
| [TV]({{site.baseurl}}/developer_guide/platforms/tv_and_ott/)                           | Interagieren Sie mit Nutzern auf vernetzten Fernsehplattformen.                                                                                                   |
| [Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | Ermöglichen Sie Echtzeitkommunikation und Integration mit externen Systemen durch benutzerdefinierte HTTP-Callbacks.                                                    |
| [LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/) | Engagieren Sie sich mit Nutzer:innen von LINE, der beliebtesten Messaging App in Japan.                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>\*\*Als Add-on-Feature erhältlich\*\*.</sup>

{% alert tip %}
Für kurze und dringende Nachrichten, die über die meisten Kanäle (E-Mail, SMS, Push) übermittelt werden können, nutzen Sie den [intelligenten Kanalfilter]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/), um die Nachricht automatisch über den besten Kanal für jeden Benutzer zu senden.
{% endalert %}

