---
nav_title: Opt-ins &amp; Opt-outs
article_title: WhatsApp Opt-Ins und Opt-Outs
description: "Dieser Referenzartikel behandelt die verschiedenen WhatsApp-Opt-in und Opt-out Methoden."
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
alias: /user_guide/message_building_by_channel/whatsapp/opt-ins_and_opt-outs/
---

# Opt-in und Opt-out

> Die Handhabung von WhatsApp Opt-Ins und Opt-Outs ist von entscheidender Bedeutung, da WhatsApp die [Qualitätsbewertung](https://www.facebook.com/business/help/896873687365001) Ihrer [Telefonnummer](https://www.facebook.com/business/help/896873687365001) überwacht und niedrige Bewertungen dazu führen können, dass Ihre Nachrichtenlimits reduziert werden. <br><br>Eine Möglichkeit, eine hochwertige Bewertung aufzubauen, besteht darin, Nutzer daran zu hindern, Ihr Unternehmen zu blockieren oder zu melden. Dies ist möglich, indem Sie [qualitativ hochwertige Nachrichten](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits) bereitstellen (z. B. einen Mehrwert für Ihre Nutzer), die Häufigkeit der Nachrichten kontrollieren und Ihren Kunden die Möglichkeit geben, den Erhalt künftiger Mitteilungen abzulehnen. <br><br>Auf dieser Seite erfahren Sie, wie Sie Opt-Ins und Opt-Outs einrichten und welche Unterschiede zwischen den Modifikatoren "regex" und "is" bestehen.

Opt-ins können aus externen Quellen oder von Braze stammen und SMS sowie In-App- und In-Browser-Nachrichten umfassen. Opt-outs können mithilfe von Schlüsselwörtern in Braze und WhatsApp-Marketingbuttons gehandhabt werden. Die folgenden Methoden helfen Ihnen bei der Einrichtung von Opt-Ins und Opt-Outs.

#### Opt-in-Methoden
- [Externe Opt-in-Verfahren](#external-to-braze-opt-in-methods)
  - [Externes Opt-in-Verzeichnis](#externally-built-opt-in-list)
  - [Ausgehende Nachricht im WhatsApp-Kanal des Kundensupports](#outbound-message-in-customer-support-whatsapp-channel)
  - [Eingehende WhatsApp-Nachricht](#inbound-whatsapp-message)
- [Braze-gestützte Opt-in-Methoden](#braze-powered-opt-in-methods)

#### Opt-out-Methoden
- [Allgemeine Opt-in-Schlüsselbegriffe](#general-opt-out-keywords)
- [Opt-out aus Werbemitteilungen](#marketing-opt-out-selection)

## Richten Sie Opt-Ins für Ihren Braze WhatsApp-Kanal ein

Für WhatsApp Opt-Ins müssen Sie die [Anforderungen von WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) erfüllen. Außerdem müssen Sie Braze die folgenden Informationen zur Verfügung stellen:
- Ein `external_id`, eine [Telefonnummer]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) und ein Update des Abo-Status für jeden Nutzer:innen. Telefonnummer und Abo-Status können über das [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) oder den [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) aktualisiert werden.

{% alert note %}
Braze hat eine Verbesserung des Endpunkts `/users/track` veröffentlicht, die Aktualisierungen des Abonnementstatus ermöglicht, über die Sie sich in [Abonnementgruppen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status) informieren können. Wenn Sie jedoch bereits Opt-in-Protokolle über den [Endpunkt`/v2/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/) erstellt haben, können Sie dies auch weiterhin dort tun.
{% endalert %}

### Externe Opt-in-Methoden für Braze

Ihre App oder Website (Kontoanmeldung, Kassenseite, Kontoeinstellungen, Kreditkartenterminal) an Braze.

Wenn bereits eine Einwilligung für Werbesendungen per E-Mail oder SMS vorliegt, ergänzen Sie einen Abschnitt zu WhatsApp. Nachdem sich ein Benutzer angemeldet hat, benötigt er eine `external_id`, eine [Telefonnummer]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) und einen aktuellen Abonnementstatus. Je nachdem, wie Ihre Braze-Installation eingerichtet ist, können Sie entweder den [`/subscription/status/set` Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) nutzen oder das [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/) verwenden.

#### Externes Opt-in-Verzeichnis

Wenn Sie WhatsApp bereits früher verwendet haben, haben Sie möglicherweise bereits eine Benutzerliste mit Opt-Ins gemäß den WhatsApp-Anforderungen erstellt. In diesem Fall laden Sie eine CSV-Datei hoch oder verwenden die API mit den [folgenden Informationen]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv) in Braze.

#### Ausgehende Nachricht im WhatsApp-Kanal des Kundensupports

In Ihrem Kundensupport-Kanal können Sie bei gelösten Problemen eine automatische Nachricht einfügen, in der Sie den Kunden fragen, ob er sich für Marketingnachrichten anmelden möchte. Die Funktionalität hängt von den Features ab, die in dem Kundensupport-Tool Ihrer Wahl verfügbar sind, und davon, wo Sie die Nutzer:innen-Daten speichern.

1. Geben Sie einen [Nachrichtenlink](https://business.facebook.com/business/help/890732351439459?ref=search_new_0) von Ihrer WhatsApp Business-Telefonnummer an.
2. Richten Sie [Quick-Reply-Aktionen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#quick-replies) ein, wenn die Einwilligung mit der Tastatureingabe "Ja" erfolgt.
3. Richten Sie angepasste Trigger für Schlüsselwörter ein.
4. In jedem Fall müssen Sie den Pfad voraussichtlich folgendermaßen vervollständigen:
	- Rufen Sie den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) auf, um Nutzer:innen zu aktualisieren bzw. zu erstellen.
	- Nutzen Sie den [Endpunkt`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) oder verwenden Sie das [SDK](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)/)

#### Eingehende WhatsApp-Nachricht 

Lassen Sie Kunden eine eingehende Nachricht an die WhatsApp-Nummer senden.

Dies kann als Canvas oder als Kampagne eingerichtet werden, je nachdem, ob Sie möchten, dass der Benutzer eine Bestätigungsnachricht über den neuen Kanal erhält.

1. Erstellen Sie eine Kampagne mit dem aktionsbasierten Zustellungsauslöser einer eingehenden Nachricht.
2. Erstellen Sie eine Webhook-Kampagne. Ein Beispiel für einen Webhook finden Sie unter [Abonnementgruppen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#update-subscription-status).

{% alert tip %}
Beachten Sie, dass Sie im [WhatsApp-Manager](https://business.facebook.com/wa/manage/phone-numbers/) unter **Telefonnummer** > **Nachrichtenlinks** eine URL oder einen QR-Code erstellen können, um einem WhatsApp-Kanal beizutreten.<br>![WhatsApp QR-Code Komponist.]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### Braze-gestützte Opt-in-Methoden 

#### SMS-Nachricht

Richten Sie in Canvas eine Kampagne ein, in der Sie nach der Einwilligung zum Empfang von WhatsApp-Nachrichten mit folgenden Methoden fragen:
- Kundensegment: Abonnierte Marketinggruppe außerhalb der USA
- Einrichtung eines benutzerdefinierten Schlüsselwort-Triggers

Erfahren Sie, wie Sie den Abo-Status von Nutzerprofilen aktualisieren können, indem Sie [Abo-Gruppen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status) anzeigen.

#### In-App- oder In-Browser-Nachricht

Erstellen Sie eine In-App-Nachricht oder ein Popup-Fenster im Browser, um Kunden aufzufordern, sich für die Nutzung von WhatsApp zu entscheiden.

Verwenden Sie eine [HTML-In-App-Nachricht](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal) mit einer [JavaScript-"Brücke"]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge) als Schnittstelle zum Braze SDK. Verwenden Sie die ID der Abo-Gruppe in WhatsApp. 

#### Abfrageformular für Telefonnummern

Verwenden Sie die Vorlage für das [Formular zur Erfassung von Telefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) im Drag-and-Drop-Editor für In-App-Nachrichten, um die Telefonnummern der Nutzer zu erfassen und Ihre WhatsApp-Abonnentengruppen zu vergrößern.

## Opt-outs für Ihren Braze WhatsApp-Kanal einrichten

### Allgemeine Opt-in-Schlüsselbegriffe

Sie können eine Kampagne oder ein Canvas einrichten, das es Nutzern, die eine Nachricht mit bestimmten Wörtern verschicken, ermöglicht, zukünftige Nachrichten abzulehnen. Canvase sind besonders vorteilhaft, da sie eine anschließende Abmeldebestätigung enthalten können. 

#### Schritt 1: Erstellen Sie ein Canvas mit dem Auslöser "Eingehende WhatsApp-Nachricht".
 
![Aktionsbasierter Canvas-Schritt für den Eingang, der Nutzer:innen erfasst, die eine eingehende WhatsApp Nachricht senden.]({% image_buster /assets/img/whatsapp/whatsapp116.png %}){: style="max-width:85%;"}

Wenn Sie Schlüsselwörter als Trigger verwenden, sollten Sie auch Formulierungen wie "Stopp" oder "Keine Nachrichten" einbeziehen. Wenn Sie sich für diese Methode entscheiden, stellen Sie sicher, dass diese Begriffe auch wirklich bekannt sind. Fügen Sie z.B. nach dem ersten Opt-in eine Antwort wie "Um diese Nachrichten abzubestellen, können Sie einfach 'Stopp' senden." 

Nachrichtenschritt, um eine eingehende WhatsApp Nachricht zu senden, deren Nachrichtentext "STOP" oder "KEINE NACHRICHT" lautet.]({% image_buster /assets/img/whatsapp/whatsapp117.png %}){: style="max-width:85%;"}

#### Schritt 2: Nutzerprofile aktualisieren

Aktualisieren Sie das Profil des Benutzers mit einer der unter [Abonnementgruppen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status) beschriebenen Methoden.

### Der Zustellung von Werbesendungen widersprechen

Bei der Erstellung von Templates für WhatsApp-Nachrichten können Sie die Option "Keine Werbesendungen erhalten" einfügen. Jedes Mal, wenn Sie dies einbeziehen, stellen Sie sicher, dass die Vorlage in einem Canvas mit einem nachfolgenden Schritt für eine Abonnementgruppenänderung verwendet wird. 

1. Erstellen Sie eine Nachrichtenvorlage mit der Schnellantwort "Keine Werbesendungen erhalten".<br>![Template für Nachrichten mit der Option "Marketing Opt-out" in der Fußzeile]({% image_buster /assets/img/whatsapp/whatsapp121.png %})<br><br>![Abschnitt zur Konfiguration eines Marketing oopt-out Buttons.]({% image_buster /assets/img/whatsapp/whatsapp122.png %})<br><br>
2. Erstellen Sie ein Canvas, das diese Nachrichtenvorlage verwendet.<br><br>
3. Befolgen Sie die Schritte des vorangegangenen Beispiels, aber mit dem Triggertext "STOP PROMOTIONS".<br><br>
4. Aktualisieren Sie den Abonnementstatus des Benutzers, indem Sie eine der unter [Abonnementgruppen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status) beschriebenen Methoden anwenden.

## Workflows für Opt-in und Opt-out einrichten

Mit diesen beiden Methoden können Sie Workflows für die Schlüsselbegriffe "START" und "STOPP" in WhatsApp konfigurieren:

- [Nutzeraktualisierung](#user-update-step)
- [Webhook-Kampagne zum Auslösen einer zweiten WhatsApp-Kampagne](#webhook-campaign-to-trigger-a-second-whatsapp-campaign)

### Nutzeraktualisierung

In dem [Schritt Nutzeraktualisierung]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) können Sie Telefonnummern in die WhatsApp-Abogruppe aufnehmen, von denen aus Schlüsselwörter an die Telefonnummer der Abogruppe gesendet werden.

Der Schritt Benutzer:innen aktualisieren vermeidet Race-Conditions, da der Nutzer:innen nicht zum nächsten Schritt im Canvas gelangt, bevor seine Telefonnummer der Abo-Gruppe hinzugefügt wurde. Außerdem sind weniger Einrichtungsschritte erforderlich als bei den anderen Methoden, weshalb Braze diese Methode im Allgemeinen empfiehlt.

1. Erstellen Sie ein Canvas mit dem aktionsbasierten Schritt **Eingehende WhatsApp Nachricht senden**. Wählen Sie **Wo der Nachrichtentext** und geben Sie "START" für **Ist** ein.

{% alert important %}
Bei "STOPP"-Nachrichten kehren Sie den Nachrichtenschritt zur Bestätigung des Opt-out und die Nutzeraktualisierung um. Wenn Sie dies nicht tun, wird der Benutzer zuerst aus der Abonnementgruppe ausgeschlossen und kann dann die Bestätigungsnachricht nicht erhalten.
{% endalert %}

![Ein WhatsApp-Nachrichtenschritt, bei dem der Nachrichtentext "START" lautet.]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Erstellen Sie im Canvas einen Schritt **Benutzeraktualisierung ein** richten und wählen Sie für **Aktion** die Option **Erweiterter JSON-Editor**. <br><br>Nutzer:in Update-Schritt mit einer Aktion von "Advanced JSON Editor".]({% image_buster /assets/img/whatsapp/user_update.png %})<br><br>
3\. Füllen Sie das **Objekt der Nutzeraktualisierung** mit dem folgenden JSON-Payload und ersetzen Sie `XXXXXXXXXXX` durch die ID der Abogruppe:

{% raw %}
```json
{
    "attributes": [
        {
            "subscription_groups": [
                {
                    "subscription_group_id": "XXXXXXXXXXX",
                    "subscription_state": "subscribed"
                }
            ]
        }
    ]
}
```
{% endraw %}

{: start="4"}
4\. Ergänzen Sie einen weiteren WhatsApp-Nachrichtenschritt. <br><br>![Nutzer:in Update-Schritt in einem Canvas.]({% image_buster /assets/img/whatsapp/message_step.png %}){: style="max-width:25%;"}

#### Überlegungen

Die Aktualisierung kann mit unterschiedlichen Geschwindigkeiten abgeschlossen werden, da Braze die [Benutzeraktualisierungsschritte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) stapelweise anfordert.

### Webhook-Kampagne zum Auslösen einer zweiten WhatsApp-Kampagne

Eine Webhook-Kampagne kann den Eintritt in eine zweite Kampagne auslösen, nachdem die Telefonnummer des Benutzers zur WhatsApp-Abonnementgruppe hinzugefügt wurde, wenn der Benutzer ein Schlüsselwort an die Telefonnummer der Abonnementgruppe sendet.

{% alert important %}
Bei STOPP-Nachrichten ist dies nicht erforderlich. Die Nachricht zur Bestätigung wird gesendet, bevor der Nutzer:innen aus der Abo-Gruppe entfernt wird, so dass Sie einen der beiden anderen Schritte verwenden können.
{% endalert %}

1. Erstellen Sie eine Kampagne oder ein Canvas mit einem aktionsbasierten Schritt **Eingehende WhatsApp-Nachricht senden**. Wählen Sie **Wo der Nachrichtentext** und geben Sie "START" für **Ist** ein.

![WhatsApp-Nachrichtenschritt, bei dem der Nachrichtentext "START" lautet.]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message.png %}){: style="max-width:85%;"}

{: start="2"}
2\. Erstellen Sie in der Kampagne oder im Canvas einen Schritt Webhook-Nachricht und ändern Sie den **Anfragetext** in **Rohtext**.

![Nachrichtenschritt für einen Webhook.]({% image_buster /assets/img/whatsapp/webhook_step.png %}){: style="max-width:85%;"}

{: start="3"}
3\. Geben Sie die kundenspezifische [Endpunkt-URL]({{site.baseurl}}/api/basics/) gefolgt vom Endpunkt-Link in die **Webhook-URL** `campaigns/trigger/send` ein. Zum Beispiel: `https://dashboard-02.braze.eu/campaigns/trigger/send`.

![Feld Webhook URL unter dem Abschnitt "Webhook erstellen".]({% image_buster /assets/img/whatsapp/campaigns_webhook_url.png %}){: style="max-width:70%;"}

{: start="4"}
4\. Geben Sie in den Rohtext die folgende JSON-Payload ein und ersetzen Sie `XXXXXXXXXXX` durch die ID der Abogruppe. Wenn Sie die zweite Kampagne erstellt haben, müssen Sie die `campaign_id` ersetzen.

{% raw %}
```json
{
    "campaign_id": "XXXXXXXXXXX",
    "recipients": [
        {
            "external_user_id": "{{${user_id}}}",
            "attributes": {
                "subscription_groups": [
                    {
                        "subscription_group_id": "XXXXXXXXXXX",
                        "subscription_state": "subscribed"
                    }
                ]
            }
        }
    ]
}
```
{% endraw %}

{: start="5"}
5\. Erstellen Sie eine WhatsApp-Kampagne (als zweite Kampagne) und setzen Sie den Trigger auf API. Stellen Sie sicher, dass Sie die `campaign_id` in die JSON-Payload der ersten Kampagne kopieren.

#### Überlegungen

- Attributänderungen aus dem JSON-Payload des Canvas-API-Triggers werden derzeit nicht unterstützt. Sie können also nur WhatsApp-Kampagnen für WhatsApp-Antwortnachrichten triggern (siehe Schritt 2).
- WhatsApp-Vorlage müssen genehmigt werden, um sie als Antwortnachricht versenden zu können. Der Grund dafür ist, dass der Auslöser für die eingehende Nachricht innerhalb derselben Kampagne oder desselben Canvas liegen muss, damit eine schnelle Antwort möglich ist. Wenn Sie einen [Update-Schritt für Nutzer:innen](#user-update-step) verwenden, können Sie eine Nachricht mit einer schnellen Antwort ohne Meta-Genehmigung senden.

## Den Unterschied zwischen "regex" und "is" Modifikatoren verstehen

In dieser Tabelle wird mit dem Trigger `STOP` veranschaulicht, wie Modifikatoren funktionieren.

| Modifikator | Trigger | Aktion |
| --- | --- | --- |
| `Is` | `STOP` | Erfasst jedes ganze Wort, das "stop" enthält, unabhängig von der Groß- und Kleinschreibung. Erfasst zum Beispiel "stopp", aber nicht "bitte stoppen". |
| `Matches regex` | `STOP` | Fängt jede Verwendung von "STOP" in genau diesem Fall ab. So werden zum Beispiel "STOP" und "BITTE STOPP" erfasst, aber nicht "Stopp". |
| `Matches regex` | `(?i)STOP(?-i)` | Erfasst jede Verwendung von "STOPP". Erfasst zum Beispiel "Stopp", "Bitte stoppen" und "Immer Nachrichten zuschicken". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

