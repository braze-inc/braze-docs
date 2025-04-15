---
nav_title: Sonnenuntergang-Policen
article_title: Sunset-Richtlinien für E-Mail
page_order: 8
page_type: reference
description: "Dieser Artikel befasst sich mit bewährten Sunsetting-Richtlinien und mit der Frage, wann es besser ist, Nachrichten an desinteressierte Nutzer:innen einzustellen."
channel: email

---

# Sunsetting-Richtlinien

> Auch wenn Sie versucht sind, Kampagnen an so viele Nutzer wie möglich zu senden, gibt es Situationen, in denen es tatsächlich von Vorteil ist, Nachrichten an uninteressierte Nutzer zu stoppen. 

Für E-Mails verfügt Ihre Sende-IP über einen Reputationswert, der Engagement, Spam-Berichte, Blocklisten und vieles mehr berücksichtigt. Sie können Tools wie [Sender Score](https://www.senderscore.org/ "Sender Score") oder den [Smart Network Data Service von Outlook](https://postmaster.live.com/snds/ "Smart Network Data Service von Outlook") verwenden, um Ihren Reputationswert zu überwachen. Wenn Ihr Reputationswert konstant niedrig ist, sortieren ISP- und Mailbox-Filter Ihre E-Mails möglicherweise automatisch in einen Spam-Ordner oder in einen Ordner mit niedriger Priorität für alle Empfänger, selbst für engagierte Empfänger. Die Erstellung einer Sunset-Policy hilft Ihnen dabei, Ihre E-Mails nur an aktive Empfänger zuzustellen. 

Mit Segmentierungsfiltern können Sie verhindern, dass Ihre Nachrichten wie Spam erscheinen, indem Sie ganz einfach Sunset-Richtlinien für E-Mails, Push- und In-App-Benachrichtigungen implementieren. Hier sind einige Dinge, die Sie bei der Erstellung einer Sunsetting-Richtlinie beachten sollten:

- Was gilt als "unengagierter" Benutzer? 
- Wird Engagement durch Klicks, Käufe, App-Nutzung oder eine Kombination dieser Verhaltensweisen definiert? 
- Wie lange muss das Engagement ausbleiben, damit Sie keine Nachrichten mehr versenden?
- Werden Sie Nutzern spezielle Kampagnen zukommen lassen, bevor Sie sie aus Ihren Segmenten ausschließen?
- Für welche Messaging-Kanäle gilt Ihre Sunsetting-Richtlinie? 

Wenn Sie beispielsweise Benutzer haben, die sich für [Apples Mail Privacy Protection (MPP)]({{site.baseurl}}/user_guide/message_building_by_channel/email/apple_mail/mpp/) entscheiden, sollten Sie überlegen, wie sich dies auf Ihre E-Mail-Kampagnen und Zustellbarkeitskennzahlen auswirken kann und wie Sie Ihre Sunset Policy am besten strukturieren.

Um Sunset-Richtlinien in Ihre Kampagnen einzubauen, erstellen Sie ein [Segment][19], das automatisch Nutzer ausschließt, die Ihre E-Mails als Spam markiert haben oder die eine bestimmte Zeit lang nicht mit Ihren Nachrichten interagiert haben.  

Um diese Segmente einzurichten, wählen Sie die Filter `Has Marked You As Spam` und `Last Engaged With Message`, die sich unter dem Abschnitt **Marketingaktivitäten** in der Filter-Dropdown-Liste befinden. 

Wenn Sie den Filter `Last Engaged With Message` anwenden, geben Sie die Art des Messagings (Push, E-Mail oder In-App-Benachrichtigung) an, mit dem die:der Nutzer:in interagiert hat bzw. nicht interagiert hat, sowie die Anzahl der Tage, die seit der letzten Interaktion der Nutzerin oder des Nutzers vergangen sind. Nachdem Sie ein Segment erstellt haben, können Sie dieses Segment mit einem beliebigen [Messaging-Kanal]({{site.baseurl}}/user_guide/message_building_by_channel/) adressieren.

![Seite "Details zum Segment", wobei der Filter "Letzte Interaktion mit Nachricht" ausgewählt ist.][20]

Während Braze den Versand von E-Mails an Benutzer, die Sie als Spam markiert haben, automatisch stoppt, können Sie mit dem Filter `Has Marked You As Spam` diesen Benutzern auch gezielte Push-Nachrichten und In-App-Benachrichtigungen senden. Dieser Filter ist nützlich für [Retargeting-Kampagnen][21]. Sie können beispielsweise ungebundenen Nutzer:innen Nachrichten schicken, die sie an die Features und Angebote erinnern, die sie verpassen, wenn sie Ihre E-Mails nicht öffnen.

Sunsetting-Richtlinien können besonders hilfreich bei E-Mail-Kampagnen sein, die sich an passive Nutzer:innen richten. Diese Kampagnen konzentrieren sich zwar auf Segmente, die über einen bestimmten Zeitraum nicht mit Ihrer App interagiert haben, aber sie können die Zustellbarkeit Ihrer E-Mails gefährden, wenn sie wiederholt uninteressierte Empfänger einschließen. Sunsetting-Richtlinien ermöglichen Ihnen das Targeting von passiven Nutzer:innen, ohne im Spam-Ordner zu landen.

[19]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[20]: {% image_buster /assets/img_archive/email_sunset_policies_new.png %}
[21]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
