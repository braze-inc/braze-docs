---
nav_title: Retargeting-Kampagnen
article_title: Retargeting-Kampagnen
page_order: 2
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie und warum Sie Retargeting-Kampagnen auf der Grundlage der Nachrichten, die Ihre Nutzer erhalten, in Betracht ziehen sollten."
tool:
  - Campaigns
  
---

# Retargeting-Kampagnen

> Durch Retargeting-Kampagnen, die auf den früheren Aktionen des Benutzers basieren, z. B. ob er eine E-Mail geöffnet hat oder nicht, können Sie Ihre Benutzer neu klassifizieren und so die Tür zu einem effektiven, datengesteuerten Marketingansatz öffnen.

{% alert note %}
Dieser Artikel enthält Informationen zum News Feed, der nicht mehr verwendet wird. Braze empfiehlt Kunden, die unser News Feed-Tool verwenden, auf unseren Nachrichtenkanal Content Cards umzusteigen - er ist flexibler, anpassbarer und zuverlässiger. Weitere Informationen finden Sie im [Migrationsleitfaden]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

Braze unterstützt das Retargeting von Nutzern auf Grundlage des Nachrichtenempfangs. Sie können Nutzer auf der Grundlage ihrer Interaktionen mit Ihren Kampagnen, Canvases und News Feed-Karten erneut ansprechen. 

Jeder Retargeting-Filter bietet nach dem Hinzufügen mehrere Optionen. Wenn Sie mehr über das Targeting von Benutzern erfahren möchten, besuchen Sie unseren [Braze Learning-Kurs](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) zur Einrichtung von Kampagnen!

![Abschnitt Segmentdetails mit dem Dropdown-Menü für die verfügbaren Filter.][1]{: style="max-width:80%;"}

## Retargeting-Filter

Sie können die Retargeting-Filter in diesem Abschnitt für Ihre Nutzer innerhalb Ihrer Kampagnen, Canvases und News Feed-Karten verwenden.

### Angeklickte Karte

Verwenden Sie den Filter, um Nutzer zu finden, die eine bestimmte News Feed-Karte angeklickt haben oder nicht.

![][2]

### Kampagne angeklickt/geöffnet

Mit diesem Filter können Sie Benutzer finden, die Folgendes getan oder nicht getan haben:

- Auf eine E-Mail geklickt
- Auf eine In-App-Nachricht geklickt
- Direkt eine Push-Benachrichtigung geöffnet
- E-Mail geöffnet
- In-App-Nachricht angesehen

![][3]

Dies kann weiter eingegrenzt werden, indem Sie die Kampagne auswählen, die Sie erneut ausführen möchten.

### Kampagne oder Canvas mit Tag angeklickt oder geöffnet

Verwenden Sie diesen Filter, um Nutzer zu finden, die mit Kampagnen oder Canvases mit einem bestimmten Tag interagiert haben oder nicht:

- Auf eine E-Mail geklickt
- Auf eine In-App-Nachricht geklickt
- Direkt eine Push-Benachrichtigung geöffnet
- E-Mail geöffnet
- In-App-Nachricht angesehen

![][16]

### Von Kampagne konvertiert 

Verwenden Sie diesen Filter, um Nutzer zu finden, die in Ihrer Zielkampagne konvertiert haben oder nicht (basierend auf der primären Konversion). 

Bei wiederkehrenden Kampagnen bezieht sich dieser Filter darauf, ob Nutzer auf die letzte Nachricht der Kampagne konvertiert haben.

![][12]

### Von Canvas konvertiert 

Verwenden Sie diesen Filter, um Nutzer zu finden, die in Ihrem Ziel-Canvas konvertiert haben oder nicht (basierend auf der primären Konversion).

Bei regelmäßigen Canvases bezieht sich dieser Filter darauf, ob Benutzer jemals etwas gekauft haben, nachdem sie das Canvas durchlaufen haben.

![][18]

### In Kampagnen-Kontrollgruppe 

Verwenden Sie diesen Filter, um Nutzer zu finden, die in der Kontrollgruppe Ihrer Zielkampagne vorkommen bzw. nicht vorkommen.

![][13]

### In Canvas-Kontrollgruppe 

Verwenden Sie diesen Filter, um Benutzer zu finden, die in der Kontrollgruppe Ihres Ziel-Canvas vorkommen bzw. nicht vorkommen. Ihre Auswahl können Sie im Dropdown-Menü treffen.

![][19]

### Zuletzt empfangene Nachricht von einer bestimmten Kampagne 

Verwenden Sie diesen Filter, um Benutzer zu finden, die eine bestimmte Kampagne zuletzt vor oder nach einem bestimmten Datum oder einer bestimmten Anzahl von Tagen erhalten haben. Dieser Filter berücksichtigt nicht, wann Benutzer andere Kampagnen erhalten haben.

![][14]

### Zuletzt empfangene Nachricht von einer bestimmten Kampagne oder Canvas mit Tag 

Verwenden Sie diesen Filter, um Benutzer zu finden, die zuletzt eine bestimmte Kampagne oder ein Canvas mit einem bestimmten Tag vor oder nach einem bestimmten Datum oder einer bestimmten Anzahl von Tagen erhalten haben. Dieser Filter berücksichtigt nicht, wenn Benutzer andere Kampagnen oder Canvases erhalten haben.

![][17]

### Empfangene Nachricht von der Kampagne 

Verwenden Sie diesen Filter, um Nutzer zu finden, die Ihre Zielkampagne erhalten bzw. nicht erhalten haben.

![][4]

### Empfangene Nachricht von Kampagne oder Canvas mit Tag 

Verwenden Sie diesen Filter, um Nutzer zu finden, die eine Kampagne oder ein Canvas mit Ihrem Ziel-Tag erhalten oder nicht erhalten haben.

![][15]

## Vorteile von Retargeting-Kampagnen

Das Retargeting ist besonders effektiv, wenn das ursprüngliche Segment auch eine bestimmte Aktion enthält, die Sie sich von den Nutzern wünschen. Nehmen wir zum Beispiel an, Sie haben eine Karte, die sich an Nutzer richtet, die noch nie etwas gekauft haben. Die Karte wirbt für einen vergünstigten In-App-Kauf. Das erste Segment sieht wie folgt aus:

- In der App ausgegebenes Geld ist genau 0
- Zuletzt verwendet App vor weniger als 14 Tagen

Die Gesamtzahl der Nutzer in dem Segment beträgt 100.000 und Sie wissen aus den News-Feed-Statistiken, dass 60.000 einzelne Nutzer die Karte angesehen und 20.000 einzelne Nutzer die Karte angeklickt haben. Mit Hilfe des Segmenters können wir sehen, wie viele der Nutzer, die auf die Karte geklickt haben, tatsächlich einen Kauf getätigt haben:

- In der App ausgegebenes Geld ist mehr als 0
- Angeklickte Karte ist Name der Karte

Nach Prüfung dieser Statistiken können wir ein Segment von Nutzern erstellen, die die Karte angeklickt, aber keinen Kauf getätigt haben:

- In der App ausgegebenes Geld ist genauer als 0
- Angeklickte Karte ist Name der Karte

Wir können dieses Segment mit zusätzlichen Nachrichten rund um die Werbeaktion oder einen weiteren In-App-Kauf erneut ansprechen. Das Retargeting kann mit einer anderen Newsfeed-Card oder Messaging-Kampagne erfolgen. Mit einem kanalübergreifenden Ansatz können Sie die Nutzer dort erreichen, wo sie am ehesten reagieren, und so die Wirksamkeit Ihrer Kampagnen erhöhen.

[1]: {% image_buster /assets/img_archive/retarget.png %}
[2]: {% image_buster /assets/img_archive/clickedcard.png %}
[3]: {% image_buster /assets/img_archive/clickedopened.png %}
[4]: {% image_buster /assets/img_archive/receivedcamp.png %}
[12]: {% image_buster /assets/img_archive/converted_from_campaign.png %}
[13]: {% image_buster /assets/img_archive/campaign_control_group.png %}
[14]: {% image_buster /assets/img_archive/last_received_specific_campaign.png %}
[15]: {% image_buster /assets/img_archive/received_campaign_with_tag.png %}
[16]: {% image_buster /assets/img_archive/retarget_tag_filter.png %}
[17]: {% image_buster /assets/img_archive/last_received_campaign_with_tag.png %}
[18]: {% image_buster /assets/img_archive/converted_from_canvas.png %}
[19]: {% image_buster /assets/img_archive/canvas_control_group.png %}
