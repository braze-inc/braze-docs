---
page_order: 20
nav_title: Best Practices
article_title: Best Practices für Push-Benachrichtigungen
description: "Auf dieser Seite finden Sie Best Practices und Anwendungsfälle für Push-Benachrichtigungen, mit denen Sie sicherstellen können, dass Ihre Push-Nachrichten Engagement fördern, anstatt zu nerven."
channel: push
---

# Best Practices für Push-Benachrichtigungen

Push-Benachrichtigungen sind leistungsstarke Werkzeuge, um mit den Nutzer:innen Ihrer App in Kontakt zu treten. Sie sollten jedoch mit Bedacht eingesetzt werden, um sicherzustellen, dass sie zeitnahe und relevante Nachrichten liefern. Bevor Sie Ihre Push-Nachricht senden, sollten Sie die folgenden Best Practices beachten.

{% alert important %}
Ihre Push-Nachrichten müssen den Richtlinien des Apple App Store und des Google Play Store entsprechen, insbesondere in Bezug auf die Verwendung von Push-Nachrichten als Werbung, Spam, Aktionen und mehr. Erfahren Sie mehr über die [Richtlinien für mobile Push-Benachrichtigungen]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#mobile-push-regulations-for-apps).
{% endalert %}

## Verfassen Sie Ihre Push-Nachricht

Braze empfiehlt, jede Textzeile für den optionalen Titel und den Nachrichtentext in einer mobilen Push-Benachrichtigung auf etwa 30 bis 40 Zeichen zu beschränken. Beachten Sie, dass der Zeichenzähler im Composer keine Liquid-Zeichen berücksichtigt. Das bedeutet, dass die endgültige Zeichenzahl einer Nachricht davon abhängt, wie Liquid für jede:n Nutzer:in gerendert wird. Im Zweifelsfall: Fassen Sie sich kurz und bündig.

## Größe der Push-Nutzlast reduzieren

Die maximale Größe der Nutzlast hängt von der Plattform ab.

| Plattform | Maximale Größe der Nutzlast |
| --- | --- |
| Internet | 3.807 Bytes |
| Android | 3.930 Bytes |
| iOS | 3.960 Bytes |
| Kindle | 5.985 Bytes |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Wenn Ihr Push die maximale Nutzlastgröße überschreitet, kann die Nachricht möglicherweise nicht gesendet werden. Am besten beschränken Sie Ihre Nutzlast auf einige hundert Bytes.

### Was ist eine Push-Nutzlast?

Push-Dienstanbieter prüfen anhand der Bytegröße der gesamten Push-Nutzlast, ob Ihre Push-Benachrichtigung einer:m Nutzer:in angezeigt werden kann. Die Nutzlast ist bei den meisten Push-Diensten auf **4 KB (4.096 Bytes)** begrenzt, einschließlich:

- Apple Push Notification service (APNs)
- Android's Firebase Cloud Messaging (FCM)
- Web-Push
- Huawei Push

Diese Push-Dienste lehnen jede Benachrichtigung ab, die diese Grenze überschreitet.

Braze reserviert einen Teil der Push-Nutzlast für Integrations- und Analytics-Zwecke. Die maximale Nutzlastgröße beträgt daher **3.807 Bytes**. Wenn Ihr Push diese Größe überschreitet, kann die Nachricht möglicherweise nicht gesendet werden. Am besten beschränken Sie Ihre Nutzlast auf einige hundert Bytes.

Die folgenden Elemente in Ihrem Push machen Ihre Push-Nutzlast aus:

- Texte, wie z. B. Titel und Nachrichtentext
- Endgültiges Rendering jeder Liquid-Personalisierung
- URLs für Bilder (aber nicht die Größe des Bildes selbst)
- URLs für Klick-Ziele
- Button-Namen
- Schlüssel-Wert-Paare

### Tipps zur Reduzierung der Nutzlast

Um die Größe der Nutzlast zu reduzieren:

- Fassen Sie Ihre Nachricht kurz. Eine gute allgemeine Richtlinie ist, sie in weniger als 40 Zeichen handlungsrelevant und nützlich zu gestalten.
- Lassen Sie Leerzeichen und Zeilenumbrüche in Ihrem Text weg.
- Überlegen Sie, wie Liquid beim Senden gerendert wird. Da die endgültige Darstellung einer Liquid-Personalisierung von Nutzer:in zu Nutzer:in unterschiedlich ist, kann Braze nicht feststellen, ob eine Push-Nutzlast die Größenbeschränkung überschreitet, wenn Liquid enthalten ist. Wenn Ihr Liquid eine kürzere Nachricht rendert, dürfte das kein Problem sein. Wenn Ihr Liquid jedoch zu einer längeren Nachricht führt, kann es sein, dass Ihr Push das Nutzlast-Limit überschreitet. Testen Sie Ihre Push-Nachricht immer auf einem echten Gerät, bevor Sie sie an Nutzer:innen senden.
- Erwägen Sie die Verkürzung von URLs mit einem URL-Shortener.

## Targeting optimieren

### Relevante Nutzerdaten sammeln

Push-Benachrichtigungen sollten mit Sorgfalt behandelt werden, damit Nutzer:innen zeitnahe und relevante Benachrichtigungen erhalten. Braze sammelt nützliche Geräte- und Nutzungsinformationen, die zur gezielten Ansprache relevanter Segmente verwendet werden können. Diese Informationen sollten durch angepasste Events und Attribute ergänzt werden, die speziell für Ihre App gelten. Anhand dieser Daten können Sie gezielt Nachrichten versenden, um die Öffnungsraten zu erhöhen und die Anzahl der Nutzer:innen, die Push-Nachrichten deaktivieren, zu verringern.

### Eine Seite mit Benachrichtigungseinstellungen erstellen

Sie können in Ihrer App eine Einstellungsseite einrichten, auf der Nutzer:innen Ihnen mitteilen können, welche Benachrichtigungen sie erhalten möchten. Ein gängiger Ansatz ist die Erstellung eines angepassten booleschen Attributs in Braze, das dem Status der App-Einstellung entspricht. Eine Nachrichten-App könnte zum Beispiel Abo-Einstellungen für aktuelle Nachrichten, Sportnachrichten oder Politik haben.

Wenn die Nachrichten-App eine Kampagne erstellen möchte, die sich nur an Nutzer:innen richtet, die sich für Politik interessieren, fügt sie dem Segment den Attributfilter `Subscribes to Politics` hinzu. Wenn diese Option auf „true" gesetzt ist, erhalten nur Nutzer:innen, die Benachrichtigungen abonniert haben, diese auch.

Weitere Informationen zum Festlegen angepasster Attribute finden Sie in den folgenden Artikeln für [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes) oder [REST API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification).

## Opt-ins und Relevanz erhöhen

### Nutzerberechtigungen einholen

Die allgemeine Statistik für Push-Aktivierung bezieht sich darauf, ob Nutzer:innen Benachrichtigungen über ihr Betriebssystem genehmigt haben. Wenn Nutzer:innen die Benachrichtigungen auf iOS deaktivieren, werden sie automatisch aus unserem System entfernt, da Apple das Senden des Push-Tokens nicht zulässt.

Für Android 13 und höher ist eine Berechtigung erforderlich, bevor Push-Benachrichtigungen angezeigt werden können. Bei älteren Android-Versionen werden Nutzer:innen standardmäßig für Benachrichtigungen angemeldet.

### Nutzer:innen auf Push vorbereiten

Sie haben nur eine Chance, Nutzer:innen um die Erlaubnis für Push zu bitten, und wenn sie ablehnen, ist es sehr schwer, sie davon zu überzeugen, Push in ihren Geräteeinstellungen wieder zu aktivieren. Aus diesem Grund sollten Sie die Nutzer:innen mit einer In-App-Nachricht auf Push vorbereiten, bevor Sie die Systemaufforderung anzeigen. Unter [Push-Primer-In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) erfahren Sie mehr über die Steigerung der Opt-ins.

### Push-Abo-Kontrollen hinzufügen

Um zu vermeiden, dass Nutzer:innen die Benachrichtigungen auf Geräteebene deaktivieren – wodurch ihr Vordergrund-Push-Token vollständig entfernt wird –, lassen Sie Nutzer:innen ihr Push-Abo direkt in Ihrer App steuern. Weitere Einzelheiten finden Sie unter [Push-Abo-Status aktualisieren]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions#update-push-subscription-state).

### Push-Abo-Status verstehen

Der Push-Abo-Status garantiert nicht, dass ein Push zugestellt wird – Nutzer:innen müssen auch Push aktiviert haben, um Benachrichtigungen zu erhalten. Das liegt daran, dass ein Nutzerprofil mehrere Geräte mit unterschiedlichen Vordergrund-Push-Berechtigungen, aber nur einen einzigen Push-Abo-Status haben kann.

Wenn ein:e Nutzer:in kein gültiges Vordergrund-Push-Token für eine App hat (d. h. Push-Token auf Geräteebene über die Einstellungen deaktiviert und sich gegen den Empfang von Benachrichtigungen entschieden hat), kann der Abo-Status immer noch als `subscribed` für Push betrachtet werden. Diese:r Nutzer:in wäre jedoch in Braze nicht `Foreground Push Enabled for App`, da das Vordergrund-Push-Token nicht gültig ist.

Wenn ein Nutzerprofil außerdem kein gültiges oder registriertes Push-Token für andere Apps hat, ist der Filter `Foreground Push Enabled` in der Segmentierung ebenfalls „false".

## Sunset-Richtlinie für nicht reagierende Nutzer:innen implementieren

Selbst wenn Sie nur relevante, zeitnahe Push-Benachrichtigungen senden, kann es sein, dass einige Nutzer:innen nicht darauf reagieren und sie als Spam empfinden. Angenommen, ein:e Nutzer:in ignoriert wiederholt Ihre Push-Benachrichtigungen. In diesem Fall ist es eine gute Idee, den Versand von Push-Nachrichten einzustellen, bevor sie sich über die Kommunikation Ihrer App ärgern oder sie ganz deinstallieren. 

Erstellen Sie dazu eine [Sunset-Richtlinie]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies), die den Versand von Push-Benachrichtigungen an Nutzer:innen, die seit längerer Zeit keine direkte oder beeinflusste Öffnung hatten, einstellt.

1. Identifizieren Sie nicht reagierende Nutzer:innen anhand von direkten oder beeinflussten Öffnungen.
2. Stellen Sie das Senden von Push-Benachrichtigungen an diese Nutzer:innen nach und nach ein.
3. Bevor Sie die Push-Benachrichtigungen ganz entfernen, senden Sie eine letzte Benachrichtigung, in der Sie erklären, warum sie keine weiteren erhalten werden. Dies gibt den Nutzer:innen die Möglichkeit, ihr Interesse an weiteren Push-Nachrichten zu bekunden, indem sie diese Benachrichtigung öffnen.
4. Nachdem die Sunset-Richtlinie in Kraft getreten ist, erinnern Sie diese Nutzer:innen mit einer [In-App-Nachricht]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) daran, dass sie zwar keine Push-Nachrichten mehr erhalten werden, die In-App-Messaging-Kanäle aber weiterhin interessante und hilfreiche Informationen liefern werden.

Auch wenn Sie vielleicht zögern, den Versand von Push-Nachrichten an Nutzer:innen einzustellen, die sich ursprünglich dafür entschieden haben, denken Sie daran, dass andere Messaging-Kanäle diese Nutzer:innen effektiver erreichen können – insbesondere wenn sie Ihre Push-Nachrichten zuvor ignoriert haben. Wenn Nutzer:innen Ihre E-Mails öffnen, sind E-Mail-Kampagnen eine gute Möglichkeit, sie auch außerhalb Ihrer App zu erreichen. Wenn nicht, sind In-App-Nachrichten der beste Weg, Inhalte zu liefern, ohne zu riskieren, dass Nutzer:innen Ihre App deinstallieren.

## Konversions-Events für App-Öffnungen festlegen

Wenn Sie einer Push-Kampagne [Konversions-Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) zuweisen, können Sie App-Öffnungen für einen bestimmten Zeitraum nach Erhalt der Kampagne verfolgen. Wenn Sie ein Konversions-Event für App-Öffnungen festlegen, erhalten Sie andere Insights als bei den Ergebnisstatistiken, die Sie normalerweise nach einer Push-Kampagne erhalten.

Während alle Ergebnisse von Push-Kampagnen die direkten Öffnungen und Öffnungen einer Nachricht aufschlüsseln (was sowohl direkte als auch [beeinflusste Öffnungen]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/) einschließt), wird beim Konversions-Tracking jede Art von Öffnung verfolgt, ob direkt oder beeinflusst.

Darüber hinaus können Sie mit dem Konversions-Event „Öffnet App" App-Öffnungen verfolgen, die vor Ablauf dieser Konversionsfrist (z. B. drei Tage) stattfinden. Der Unterschied zu einer beeinflussten Öffnung besteht darin, dass die Zeit, die ein:e Nutzer:in für die Registrierung einer beeinflussten Öffnung hat, von Person zu Person variieren kann, je nach dem früheren Engagement-Verhalten.

## Verwandte Artikel

Haben Sie nicht gefunden, wonach Sie gesucht haben? Sehen Sie sich diese zusätzlichen Best-Practices-Artikel an:

- [Bild- und Textspezifikationen für Push-Benachrichtigungen]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)
- [Push-Primer-In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)
- [Zustellbarkeit für chinesische Android-Geräte]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/)
- [Informationen vor dem Versand: Kanäle]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/know_before_send/)