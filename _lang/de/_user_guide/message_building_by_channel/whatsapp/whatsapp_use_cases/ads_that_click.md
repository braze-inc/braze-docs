---
nav_title: "Anzeigen, die auf WhatsApp klicken"
article_title: "Anzeigen, die auf WhatsApp klicken"
page_order: 1
description: "Dieser referenzierte Artikel enthält eine Schritt-für-Schritt-Anleitung zur Einrichtung und Verwendung von Ads That Click für WhatsApp."
page_type: reference
alias: /whatsapp_use_cases/
channel:
  - WhatsApp
---

# Anzeigen, die auf WhatsApp klicken

> Auf dieser Seite finden Sie eine Schritt-für-Schritt-Anleitung zur Einrichtung und Verwendung von Ads That Click für WhatsApp, damit Sie und Ihr Team Ihr WhatsApp-Programm aufwerten können.

Ads That Click to WhatsApp sind ein effizienter Weg, um neue und bestehende Kund:innen über Meta-Anzeigen auf Facebook, Instagram oder anderen Plattformen zu gewinnen. Nutzen Sie diese Anzeigen, um für Ihre Produkte und Serviceleistungen zu werben und Nutzer:innen auf Ihre WhatsApp-Präsenz aufmerksam zu machen.

![Eine Facebook-Anzeige von Calorie Rocket, die für eine kostenlose Zustellung wirbt, und die entsprechende WhatsApp-Konversation, die entsteht, wenn ein Nutzer:innen den Button der Anzeige auswählt.]({% image_buster /assets/img/whatsapp/ads_that_click_whatsapp.png %}){: style="max-width:70%;"}

## Einrichten von Anzeigen, die auf WhatsApp klicken

1. Erstellen Sie im Meta Ads Manager eine Anzeige auf Facebook, Instagram oder anderen Plattformen, indem Sie der Schritt-für-Schritt-Anleitung [Wie man Anzeigen erstellt, die auf WhatsApp klicken](https://business.whatsapp.com/products/create-ads-that-click-to-whatsapp), folgen. Richten Sie **keine** automatisierten Antworten ein; Sie werden stattdessen Antworten in Braze einrichten.

![Ads Manager:in mit einem Composer, um eine Engagement-Anzeige zu erstellen.]({% image_buster /assets/img/whatsapp/meta_ads_composer.png %})

Wenn Sie die vorausgefüllte Nachricht einrichten, die der Nutzer:innen an Ihr WhatsApp Business-Konto sendet, fügen Sie ein bestimmtes Wort oder eine bestimmte Phrase ein, mit der Sie eine Reaktion auf die jeweilige Anzeige triggern wollen. In diesem Beispiel verwendet eine App für die Zustellung von Lebensmitteln den Begriff "kostenlose Zustellung", weil dies in ihrer Anzeige beworben wird. 

![Ads Manager:in Template-Editor mit einer vorgefertigten Nachricht "Ich möchte eine kostenlose Zustellung".]({% image_buster /assets/img/whatsapp/pre_filled_message.png %})

{% alert tip %}
Machen Sie in der Anzeigenbeschreibung deutlich, dass ein Klick auf die Anzeige eine Konversation mit Ihrer Marke einleitet, indem Sie Phrasen wie "Chatten Sie jetzt auf WhatsApp" verwenden.
{% endalert %}

{: start="2"}
2\. Richten Sie in Braze ein aktionsbasiertes Canvas ein, bei dem die aktionsbasierte Option **Eingehende WhatsApp-Nachricht senden** lautet und der Nachrichtentext “YOUR_TRIGGER_WORD”. lautet. In diesem Beispiel verwendet eine App für die Zustellung von Lebensmitteln die "kostenlose Zustellung".

![Zeitplan für den Eingang eines aktionsbasierten Braze-Canvas, mit dem Trigger-Ereignis "Senden Sie eine eingehende WhatsApp-Nachricht" und einem Nachrichtentext, der mit dem Regex von "kostenlose Zustellung" übereinstimmt.]({% image_buster /assets/img/whatsapp/action_based_free_delivery.png %})

{: start="3"}
3\. Richten Sie eine Antwortnachricht im Canvas ein, die sofort versendet wird, nachdem der Kund:in den Canvas eingetreten ist (z.B. ohne Verzögerung). Obwohl ein Klick auf die Anzeige technisch gesehen ein Opt-in darstellt, empfehlen wir, Ihre Antwortnachricht so einzurichten, dass der Nutzer:innen gefragt wird, ob er in Zukunft Marketing Nachrichten von Ihnen auf WhatsApp erhalten möchte. 

{% alert tip %}
Richten Sie Ihre Nachrichten mit Schnellantworten ein (z.B. "Ja" oder "Nein, danke"), damit Nutzer:innen schnell angeben können, ob sie ein Opt-in wünschen.
{% endalert %}

Vergessen Sie nicht, auch den Rabattcode, das Angebot oder andere in der Anzeige versprochene Informationen anzugeben!

![WhatsApp Nachrichten-Editor mit Button-Antworten von "Ja" und "Nein Danke".]({% image_buster /assets/img/whatsapp/quick_replies.png %})

![Canvas-Schritt mit einer "Opt-in"-Gruppe mit einem Trigger-Ereignis von "Eingehende WhatsApp an Abo-Gruppe gesendet" und einem Trigger-Wort von "JA".]({% image_buster /assets/img/whatsapp/opting_in_step.png %})

{: start="4"}
4\. Opt-in Nutzer:innen, indem Sie den Abo-Status von Nutzerprofilen mit einer der folgenden Update-Methoden aktualisieren:
    \- Erstellen Sie einen Braze-to-Braze-Webhook, der den Abo-Status über die REST API aktualisiert.  
    \- Verwenden Sie den erweiterten JSON-Editor, um das Nutzerprofil mit dem Template zu aktualisieren, um [den Status des Abonnements eines Nutzers:innen in einem WhatsApp Canvas zu aktual]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#whatsapp-opt-in-and-opt-out-process)isieren.

![User Update Canvas-Schritt, der den fortschrittlichen JSON-Editor zum Update des Nutzerprofils verwendet.]({% image_buster /assets/img/whatsapp/user_update_step_json.png %})

![Canvas, das den Arbeitsablauf für das Senden von Ads That Click an WhatsApp zeigt, einschließlich dreier Aktions-Pfade: Opt-in, Opt-out, und alle anderen.]({% image_buster /assets/img/whatsapp/ads_that_click_canvas.png %})

## Überlegungen

Konversationen, die von einer Anzeige ausgehen, die auf WhatsApp geklickt wird, sind kostenlos, wenn die folgenden Bedingungen erfüllt sind:

- Wenn ein Nutzer:innen Ihnen über einen [kostenlosen Eingang](https://developers.facebook.com/docs/whatsapp/pricing#free-entry-point-conversations), wie z.B. eine Anzeige, die auf WhatsApp klickt, eine Nachricht sendet, öffnet sich ein [24-Stunden-Fenster für den Kundenservice](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages#customer-service-windows), in dem Sie dem Nutzer:innen jede Art von Nachricht senden können.
- Wenn Sie innerhalb des Zeitfensters des Kundendienstes (innerhalb von 24 Stunden) antworten, öffnet sich ein kostenloser Eingang für 72 Stunden, und alle Nachrichten innerhalb des 72-Stunden-Fensters werden kostenlos sein.
- Das Messaging von responsiven Nachrichten ist kostenlos.