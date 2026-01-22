---
nav_title: Sunsetting-Richtlinien
article_title: Sunset-Richtlinien für E-Mail
page_order: 8
page_type: reference
description: "Dieser Artikel befasst sich mit bewährten Sunsetting-Richtlinien und mit der Frage, wann es besser ist, Nachrichten an desinteressierte Nutzer:innen einzustellen."
channel: email

---

# Sunsetting-Richtlinien

> Auch wenn Sie versucht sind, Kampagnen an so viele Nutzer wie möglich zu senden, gibt es Situationen, in denen es tatsächlich von Vorteil ist, Nachrichten an uninteressierte Nutzer zu stoppen. 

Für E-Mails verfügt Ihre Sende-IP über einen Reputationswert, der Engagement, Spam-Berichte, Blocklisten und vieles mehr berücksichtigt. You can use tools like [Sender Score](https://www.senderscore.org/) or [Outlook's Smart Network Data Service](https://postmaster.live.com/snds/) to monitor your reputation score. Wenn Ihr Reputationswert konstant niedrig ist, sortieren ISP- und Mailbox-Filter Ihre E-Mails möglicherweise automatisch in einen Spam-Ordner oder in einen Ordner mit niedriger Priorität für alle Empfänger, selbst für engagierte Empfänger. Die Erstellung einer Sunset-Policy hilft Ihnen dabei, Ihre E-Mails nur an aktive Empfänger zuzustellen. 

Mit Segmentierungsfiltern können Sie verhindern, dass Ihre Nachrichten wie Spam erscheinen, indem Sie ganz einfach Sunset-Richtlinien für E-Mails, Push- und In-App-Benachrichtigungen implementieren. Hier sind einige Dinge, die Sie bei der Erstellung einer Sunsetting-Richtlinie beachten sollten:

- Was gilt als "unengagierter" Benutzer? 
- Wird Engagement durch Klicks, Käufe, App-Nutzung oder eine Kombination dieser Verhaltensweisen definiert? 
- Wie lange muss das Engagement ausbleiben, damit Sie keine Nachrichten mehr versenden?
- Werden Sie Nutzern spezielle Kampagnen zukommen lassen, bevor Sie sie aus Ihren Segmenten ausschließen?
- Für welche Messaging-Kanäle gilt Ihre Sunsetting-Richtlinie? 

Wenn Sie beispielsweise Benutzer haben, die sich für [Apples Mail Privacy Protection (MPP)]({{site.baseurl}}/user_guide/message_building_by_channel/email/apple_mail/mpp/) entscheiden, sollten Sie überlegen, wie sich dies auf Ihre E-Mail-Kampagnen und Zustellbarkeitskennzahlen auswirken kann und wie Sie Ihre Sunset Policy am besten strukturieren.

To incorporate sunset policies into your campaigns, create a [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment) that automatically excludes users who have marked your emails as spam or have not interacted with a your messages for a certain period of time.  

To set up these segments, choose the `Has Marked You As Spam` and `Last Engaged With Message` filters located under the **Retargeting** section in the filter dropdown. 

Wenn Sie den Filter `Last Engaged With Message` anwenden, geben Sie die Art des Messagings (Push, E-Mail oder In-App-Benachrichtigung) an, mit dem die:der Nutzer:in interagiert hat bzw. nicht interagiert hat, sowie die Anzahl der Tage, die seit der letzten Interaktion der Nutzerin oder des Nutzers vergangen sind. Nachdem Sie ein Segment erstellt haben, können Sie dieses Segment mit einem beliebigen [Messaging-Kanal]({{site.baseurl}}/user_guide/message_building_by_channel/) adressieren.

![Segment-Detailseite mit ausgewähltem Filter "Zuletzt mit Nachricht engagiert".]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Während Braze den Versand von E-Mails an Benutzer, die Sie als Spam markiert haben, automatisch stoppt, können Sie mit dem Filter `Has Marked You As Spam` diesen Benutzern auch gezielte Push-Nachrichten und In-App-Benachrichtigungen senden. This filter is useful for [retargeting campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns). Sie können beispielsweise ungebundenen Nutzer:innen Nachrichten schicken, die sie an die Features und Angebote erinnern, die sie verpassen, wenn sie Ihre E-Mails nicht öffnen.

Sunsetting-Richtlinien können besonders hilfreich bei E-Mail-Kampagnen sein, die sich an passive Nutzer:innen richten. Diese Kampagnen konzentrieren sich zwar auf Segmente, die über einen bestimmten Zeitraum nicht mit Ihrer App interagiert haben, aber sie können die Zustellbarkeit Ihrer E-Mails gefährden, wenn sie wiederholt uninteressierte Empfänger einschließen. Sunsetting-Richtlinien ermöglichen Ihnen das Targeting von passiven Nutzer:innen, ohne im Spam-Ordner zu landen.

