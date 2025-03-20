---
nav_title: "Über SMS"
article_title: Über SMS
page_order: 1
description: "Dieser Referenzartikel behandelt allgemeine Anwendungsfälle des SMS-Kanals und die Voraussetzungen für die Einrichtung von SMS."
page_type: reference
channel:
  - SMS
search_rank: 2
---

# [![Braze-Lernkurs]](https://learning.braze.com/messaging-channels-sms)([{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}Über SMS

> In diesem Artikel finden Sie einige häufig vorkommende Anwendungsfälle, Anforderungen und Begriffe, die Ihnen bei der SMS-Integration helfen und es Ihnen ermöglichen, effektiv und strategisch mit Ihren Kunden zu kommunizieren.![SMS-Nachricht mit dem Text "Willkommen bei Braze! Wir freuen uns, Sie an Bord zu haben. Schauen Sie sich unsere Dokumentation an, um loszulegen. https://www.braze.com/docs/ Text HELP for help and STOP to stop."][picture]{: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

<br>
SMS, auch bekannt als Short Message Service, wird verwendet, um Textnachrichten an Mobiltelefone zu senden. Derzeit werden weltweit täglich über 23 Milliarden Textnachrichten verschickt, wobei die SMS der direkteste Weg ist, Nutzer und Kunden zu erreichen. Diese weit verbreitete Nutzung und der bewährte Nutzen haben SMS zu einem effektiven Marketinginstrument für Unternehmen jeder Größe gemacht. 
<br><br>
## Potenzielle Anwendungsfälle

| Anwendungsfall | Erklärung |
|---|---|
| Allgemeines Marketing | SMS-Nachrichten sind ein direkter, flexibler und effizienter Weg, um Ihre Kunden über bevorstehende Angebote, günstige Verkäufe und aktuelle oder erwartete Produkte zu informieren. |
| Hinweise | Mit SMS-Nachrichten können Sie Nutzer:innen, die einen Termin für einen Dienst vereinbart haben, effektiv benachrichtigen. Wenn Sie beispielsweise eine SMS-Nachricht senden, die einen Kunden oder eine Kundin am Tag vor einem Arzttermin daran erinnert, dass er oder sie einen Termin verpasst hat, sparen Sie und Ihre Kund:innen Zeit und Geld. |
| Transaktionsnachrichten | SMS-Nachrichten sind ein effizienter Weg, um Transaktionsbenachrichtigungen wie Auftragsbestätigungen und Versandinformationen zu versenden und ihnen alle benötigten Informationen an einem Ort zur Verfügung zu stellen. Beachten Sie, dass es gesetzliche Richtlinien gibt, die beim Versenden von Nachrichten über Transaktionen beachtet werden müssen. Wenn Sie sich bezüglich dieser Richtlinien unsicher sind, wenden Sie sich an Ihr internes Rechtsteam.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anforderungen

Bevor Sie mit dem Versand von SMS beginnen, benötigen Sie einige Dinge. In der folgenden Tabelle finden Sie weitere Informationen.

|Anforderung | Beschreibung | Erwerbung |
|---|---|---|
| Eine spezielle Telefonnummer (entweder ein Short Code oder ein Long Code) | Eine spezielle Telefonnummer, die ausschließlich für eine bestimmte Marke oder einen bestimmten Anbieter zur Verfügung steht. | Braze übernimmt die Beschaffung dieser Nummern für Sie. Erfahren Sie mehr über [kurze und lange Codes]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/).|
| Liste der Benutzer mit Telefonnummern | Bevor Sie mit dem Versenden von Nachrichten beginnen können, müssen Sie Benutzer zu Ihrem Konto hinzufügen. Außerdem müssen Sie die ungefähre Größe Ihrer Zielgruppe kennen.  | Benutzer werden zunächst über unser Backend zu Braze hinzugefügt. Sie müssen diese Liste an uns weitergeben, damit wir sie für Sie hochladen können. Telefonnummern müssen als 10-stellige Nummer formatiert sein und eine Landesvorwahl enthalten. Erfahren Sie mehr über [Benutzertelefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/). |
| [SMS-Keywords und Antworten]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) | Allen grundlegenden Keywords müssen Antworten zugewiesen werden, bevor Sie mit dem Messaging beginnen können. | Sie sollten diese auflisten und sie während Ihres Onboarding-Prozesses an Ihre Braze-Vertretung oder Onboarding-Manager senden. [SMS-Schlüsselwortvorlagen]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application) anzeigen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Begriffe, die Sie kennen sollten

- **Shortcode:** Ein 5- bis 6-stelliger Code, der kürzer ist als eine vollständige Telefonnummer. Dieser Code wird zum Adressieren und Versenden von SMS-Nachrichten verwendet.<br><br>
- **Langcodes:** Ein 10-stelliger Code, der zur Adressierung von SMS-Nachrichten verwendet wird. Die meisten durchschnittlichen Telefonnummern gelten als Langcodes (e.g 123-456-7891). Diese Codes werden zum Adressieren und Versenden von SMS-Nachrichten verwendet.<br><br>
- **Abo-Gruppe:** Eine Sammlung von Telefonnummern (wie Shortcodes, Langcodes und/oder alphanumerische Sender-IDs), die für eine bestimmte Art von Messaging verwendet werden. Wenn eine Marke beispielsweise plant, sowohl Transaktions- als auch Werbe-SMS zu versenden, müssen Sie in Ihrem Braze-Dashboard zwei Abonnementgruppen mit separaten Pools sendender Telefonnummern einrichten.<br><br>
- **Segmente und Zeichenbeschränkungen für Nachrichtensegmente:** Ein Nachrichtensegment gibt an, in wie viele Segmente Ihre ursprüngliche SMS-Nachricht aufgeteilt wird. Jede Nachricht hat ein Zeichenlimit, das bei Überschreitung dazu führt, dass die Nachricht in Segmente unterteilt wird. Je nachdem, welchen Kodierungsstandard Sie verwenden (UTF-2 oder GSM-7), gibt es unterschiedliche Zeichengrenzen. Weitere Informationen über die Segmentierung von Nachrichten und die Begrenzung von Zeichen in Nachrichten finden Sie in unserem [message copy limits][2] ].<br><br>
- **Allgemeine Metriken für SMS-Kampagnen:** <br>*Gesendet*, *Sendet an den Zusteller*, *Zustellungsfehler*, *Bestätigte Zustellung*, *Ablehnungen*, *Opt-Out* und *Hilfe*. <br>Informationen zu diesen und anderen SMS-Metriken finden Sie unter [SMS-Berichterstattung][1]]. Beachten Sie, dass die Funktion *Sendungen an Netzbetreiber* veraltet ist, aber weiterhin für Nutzer:innen unterstützt wird, die bereits darüber verfügen.

<br><br>

Eine vollständige Liste der Begriffe finden Sie in unseren SMS [Terms to Know]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/terms/).

[Bild]: {% image_buster /assets/img/sms/sms_about.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy
