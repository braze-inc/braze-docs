---
nav_title: Kanal-Filter
article_title: Intelligenter-Kanal-Filter
page_order: 1.5
description: "Dieser Artikel beschreibt den Filter „Intelligenter Kanal“, der den Teil Ihrer Zielgruppe auswählt, für den der gewählte Nachrichtenkanal der „beste“ Kanal ist. Hier bedeutet „beste“ die höchste Wahrscheinlichkeit von Engagement basierend auf der Nutzerhistorie."
search_rank: 11
---

# [![Braze Learning-Kurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"}Filter „Intelligenter Kanal“

> Der Filter **Intelligenter Kanal** (früher **Most Engaged**) wählt den Teil Ihrer Zielgruppe aus, für den der gewählte Nachrichtenkanal ihr „bester“ Kanal ist.

## Über den Kanal-Filter

![Der Filter „Intelligenter Kanal“ mit Dropdown für die wählbaren Kanäle.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

„Beste“ bedeutet hier den Kanal mit der höchsten Wahrscheinlichkeit von Engagement basierend auf der Nutzerhistorie. Sie können E-Mail, SMS, WhatsApp, Web-Push oder Mobile Push (inkl. verfügbarer mobiler OS/Geräte) als Kanal wählen.

Der Intelligente Kanal berechnet die Engagement-Rate pro Nutzer und Kanal als Verhältnis von Nachrichteninteraktionen (Opens oder Klicks) zu empfangenen Nachrichten in den letzten sechs Monaten. Die Kanäle werden nach ihren Engagement-Raten sortiert; der Kanal mit der höchsten Rate ist für diesen Nutzer „Most Engaged“.

Bei jeder gesendeten Nachricht oder Nutzerinteraktion wird die Engagement-Rate innerhalb von Sekunden neu berechnet. Eine Nachricht zählt nur einmal als interagiert (z. B. Open und Klick derselben E-Mail = eine Interaktion).

Um den Filter „Intelligenter Kanal“ zu aktivieren, wählen Sie beim Erstellen einer E-Mail-, Web-Push- oder Mobile-Push-Kampagne auf der Seite **Zielgruppen** den Filter **Intelligenter Kanal**.

{% alert important %}
Für die Engagement-Rate des SMS-Kanals aktivieren Sie [SMS-Link-Verkürzung]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) mit erweitertem Tracking und Klick-Tracking. Ohne dieses Tracking kann SMS wegen unseres [Tie-Breaking-Verhaltens]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/#tie-breaking) mit 0 % Engagement als Intelligenter Kanal gewählt werden.
{% endalert %}

## Option „Nicht genug Daten“

Damit Braze den „besten“ Kanal ermitteln kann, sind ausreichend Daten nötig: Ein Nutzer muss in mindestens zwei von drei verfügbaren Kanälen mindestens drei Nachrichten pro Kanal erhalten haben (Öffnen ist nicht erforderlich).

Nutzer ohne ausreichend Nachrichten über die Kanäle fallen in die Option „Nicht genug Daten“ dieses Filters. Sie können dann einen beliebigen der drei Kanäle für diese Nutzer verwenden.

Beispiel: Nutzer, die Push bevorzugen, sollen Push erhalten, und Nutzer ohne genug Daten sollen dieselbe Push-Nachricht erhalten. Setzen Sie den Filter „Intelligenter Kanal“ auf **Mobile Push** und fügen Sie mit **OR** einen zweiten Filter „Intelligenter Kanal“ mit **Nicht genug Daten** hinzu. Eine separate Kampagne mit dem Filter „Intelligenter Kanal“ auf E-Mail spricht Nutzer an, die E-Mail bevorzugen.

![Filter „Intelligenter Kanal“ für Mobile Push oder Nicht genug Daten.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
Kampagnen und Canvas-Schritte, die [Frequency-Capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules) ignorieren, werden vom Intelligenten Kanal nicht berücksichtigt und erfüllen die Datenanforderungen nicht.
{% endalert %}

Weitere Best Practices zu Tie-Breaking, nicht erreichbaren Kanälen und Zielgruppengröße finden Sie in der vollständigen Version dieses Artikels im linken Inhaltsverzeichnis oder in der Braze-Dashboard-Hilfe.
