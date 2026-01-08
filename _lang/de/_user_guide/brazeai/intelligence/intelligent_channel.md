---
nav_title: Kanal Filter
article_title: Intelligenter Kanalfilter
page_order: 1.5
description: "Dieser Artikel behandelt den Intelligenten Kanalfilter, einen Filter, der den Teil Ihrer Zielgruppe auswählt, für den der ausgewählte Nachrichtenkanal der beste Kanal ist. In diesem Fall ist die Wahrscheinlichkeit eines Engagements angesichts des Verlaufs der Nutzer:innen am höchsten."
search_rank: 11
---

# [![Braze Lernkurse]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/most-engaged-channel){: style="float:right;width:120px;border:0;" class="noimgborder"} Intelligenter Kanal Filter

> Der Filter `Intelligent Channel` (zuvor `Most Engaged`) wählt den Teil Ihrer Zielgruppe aus, für den der ausgewählte Messaging-Kanal der "beste" Kanal ist. 

## Über den Kanal Filter

![Der Filter für intelligente Kanäle mit einem Dropdown-Menü für die verschiedenen Kanäle, die Sie auswählen können.]({% image_buster /assets/img/intelligent_channel_filter.png %}){: style="float:right;max-width:40%;margin-left:10px;margin-top:10px;border:0"}

In diesem Fall bedeutet "am besten" den Kanal, der angesichts des Verlaufs der Nutzerin oder des Nutzers die höchste Wahrscheinlichkeit für ein Engagement aufweist. Sie können E-Mail, SMS, WhatsApp, Web-Push oder Mobile-Push (einschließlich aller verfügbaren mobilen Betriebssysteme oder Geräte) als Kanal auswählen.

Der Intelligente Kanal berechnet die Engagement-Rate für jeden Nutzer für jeden der drei Kanäle, indem er das Verhältnis von Nachrichteninteraktionen (Öffnungen oder Klicks) zur Anzahl der erhaltenen Nachrichten über die letzten sechs Monate der Aktivität nimmt. Die verfügbaren Kanäle werden nach ihrem jeweiligen Engagement-Verhältnis geordnet, und der Kanal mit dem höchsten Verhältnis ist der "Engagierteste" für diesen Nutzer. 

Jedes Mal, wenn eine Nachricht an einen Benutzer gesendet wird oder ein Benutzer mit einer Nachricht interagiert, wird das Engagement-Verhältnis innerhalb von Sekunden neu berechnet. Ein:e Nutzer:in kann nur einmal als mit einer Nachricht interagierend gezählt werden (z. B. wird eine Öffnung und ein Klick auf dieselbe E-Mail als einmaliges Engagement gewertet, nicht zweimal). 

Um den Filter für den intelligenten Kanal zu aktivieren, wählen Sie den Filter für **den intelligenten Kanal** auf der Seite **Zielgruppen** aus, wenn Sie eine E-Mail-, Web-Push- oder Mobile-Push-Kampagne erstellen.

{% alert important %}
Um die Engagement-Rate des SMS-Kanals zu berechnen, schalten Sie die [SMS-Linkverkürzung]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#overview/) mit erweitertem Tracking und Click-Tracking ein. Ohne dieses Tracking kann es sein, dass SMS als intelligenter Kanal für eine Engagement-Rate von 0 % ausgewählt wird, da wir [bei einem Gleichstand die Entscheidung treffen]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/#tie-breaking).
{% endalert %}

## Die Option "Nicht genug Daten"

Damit Braze feststellen kann, welcher Kanal der "beste" ist, müssen genügend Daten vorhanden sein. Das bedeutet, dass ein Nutzer:innen mindestens drei oder mehr Nachrichten pro Kanal über mindestens zwei der drei verfügbaren Kanäle erhalten haben muss. Die Nachrichten müssen nicht unbedingt geöffnet worden sein. 

Wenn Benutzer nicht genügend Nachrichten über die Kanäle erhalten haben, fallen diese Benutzer unter die Option "Nicht genügend Daten" dieses Filters. So können Sie jeden der drei verfügbaren Nachrichtenkanäle nutzen, um diese Nutzer anzusprechen.

Nehmen wir an, Sie möchten, dass Benutzer, die Push-Nachrichten bevorzugen, eine Push-Nachricht erhalten und Benutzer, die nicht über genügend Daten verfügen, dieselbe Push-Nachricht erhalten. In diesem Fall könnten Sie den Intelligenten Kanalfilter auf **Mobile Push** einstellen und mit **ODER** einen zweiten Intelligenten Kanalfilter hinzufügen, der auf **Nicht genügend Daten** eingestellt ist. Mit einer separaten Kampagne, bei der der Filter für den intelligenten Kanal auf E-Mail eingestellt ist, können Sie Nutzer ansprechen, die E-Mail bevorzugen.

![Intelligenter Kanal Filter für mobilen Push oder nicht genügend Daten.]({% image_buster /assets/img/intelligent_example.png %}){:style="border:none"}

{% alert note %}
Kampagnen und Canvas-Schritte, die die [Frequenzbegrenzung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-rules) ignorieren, werden von Intelligent Channel nicht berücksichtigt und können nicht zu den Datenanforderungen beitragen.
{% endalert %}

## Die Option "Mobiler Push"

Mobile Push umfasst Android, iOS, Kindle und andere Kanäle für mobile Geräte, die auf Braze verfügbar sind. Bei der Berechnung des intelligenten Kanals betrachtet Braze jede Art von mobilem Gerät separat und wählt dann die höchste Engagement-Rate unter ihnen aus, um die Kategorie "Mobile Push" beim Vergleich mit E-Mail und Web-Push zu repräsentieren. 

Wenn ein:e Nutzer:in zum Beispiel mehrere mobile Geräte besitzt, wird seine Engagement-Rate durch die höchste Rate auf allen Geräten repräsentiert. Dies würde den Benutzer jedoch nicht dazu zwingen, Push-Benachrichtigungen ausschließlich auf diesem Gerät zu empfangen. Diese Rate wird nur beim Vergleich mit E-Mail und Web-Push verwendet.

## Einzelne Kanäle

Anstatt Braze den besten Kanal für einen Benutzer auswählen zu lassen, können Sie die Benutzer auch einfach danach filtern, ob sie eine Nachricht auf einem bestimmten von Ihnen ausgewählten Kanal öffnen werden oder nicht. Dazu können Sie den Filter Offene Wahrscheinlichkeit der Nachricht in den [Segmentierungsfiltern]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#message-open-likelihood) verwenden.

## Bewährte Praktiken und effektive Nutzungsstrategie

### Tie-Break

Da einige Benutzer nur wenige Nachrichten erhalten, ist es nicht ungewöhnlich, dass die Engagement-Raten für einen bestimmten Benutzer über die verfügbaren Kanäle hinweg gleich sind (z. B. hat ein einzelner Benutzer eine Engagement-Rate von 0,2 **sowohl** für E-Mail als auch für Mobile Push). In solchen Fällen werden Gleichstände aufgelöst, indem der Kanal mit den zuletzt geöffneten Events bevorzugt (höher bewertet) wird.

### Nicht erreichbare Kanäle

Wenn der Benutzer über genügend Daten verfügt, um ein Ranking zu erstellen, aber auf dem Kanal, auf dem er am meisten aktiv ist, nicht mehr erreichbar ist, wird er "herausfallen" und keine Nachrichten mehr erhalten. Nutzer:innen, die auf bestimmten Kanälen nicht erreichbar sind, sollten gesondert Targeting erhalten.

### Größe der Zielgruppe

Mit Intelligent Channel können Sie im Voraus gezielt den Teil der Nutzer ansprechen, bei dem die Wahrscheinlichkeit, dass er sich mit einer Nachricht beschäftigt, wesentlich höher ist als beim Rest Ihrer Zielgruppe. Dies entspricht wahrscheinlich nicht der Mehrheit der Nutzer in einer typischen Zielgruppe. Vielmehr können Sie davon ausgehen, dass dieser Filter die 5-20 % Ihrer üblichen Zielgruppe findet, die sich nachweislich auf einem bestimmten Kanal engagiert haben.


