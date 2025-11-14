---
page_order: 20
nav_title: Bewährte Praktiken
article_title: Best Practices für Push-Benachrichtigungen
description: "Auf dieser Seite finden Sie bewährte Push-Verfahren und Anwendungsfälle, mit denen Sie sicherstellen können, dass Ihre Push-Nachrichten Engagement wecken, anstatt zu nerven."
channel: push
---

# Best Practices für Push-Benachrichtigungen

Push-Benachrichtigungen sind leistungsstarke Werkzeuge, um mit den Nutzern Ihrer App in Kontakt zu treten. Sie sollten jedoch mit Bedacht eingesetzt werden, um sicherzustellen, dass sie zeitnahe und relevante Nachrichten liefern. Bevor Sie Ihre Push-Benachrichtigung senden, sollten Sie die folgenden Best Practices beachten.

{% alert important %}
Ihre Push-Nachrichten müssen den Richtlinien des Apple App Stores und des Google Play Stores entsprechen, insbesondere in Bezug auf die Verwendung von Push-Nachrichten als Werbung, Spam, Promotions und mehr. Erfahren Sie mehr über die [Mobile Push-Verordnung]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#mobile-push-regulations-for-apps).
{% endalert %}

## Verfassen Sie Ihre Push-Nachricht

Braze empfiehlt, jede Textzeile für den optionalen Titel und den Nachrichtentext in einer mobilen Push-Benachrichtigung auf etwa 30 bis 40 Zeichen zu beschränken. Beachten Sie, dass der Zeichenzähler im Composer keine flüssigen Zeichen berücksichtigt. Das bedeutet, dass die endgültige Zeichenzahl einer Nachricht davon abhängt, wie Liquid für jeden Benutzer dargestellt wird. Im Zweifelsfall machen Sie es kurz und bündig.

## Größe der Push-Benachrichtigungen reduzieren

Die maximale Größe der Nutzlast hängt von der Plattform ab.

| Plattform | Maximale Größe der Nutzlast |
| --- | --- |
| Internet | 3.807 Bytes |
| Android | 3,930 Bytes |
| iOS | 3.960 Bytes |
| Kindle | 5.985 Bytes |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Wenn Ihr Push die maximale Nutzdatengröße überschreitet, kann die Nachricht möglicherweise nicht gesendet werden. Am besten beschränken Sie Ihre Nutzdaten auf einige hundert Bytes.

### Was ist eine Push-Nutzlast?

Die Anbieter von Push-Diensten berechnen, ob Ihre Push-Benachrichtigung einem Nutzer:innen angezeigt werden kann, indem sie die Bytegröße der gesamten Push-Nutzlast betrachten. Die Nutzlast ist bei den meisten Push Diensten auf **4KB (4.096 Bytes** ) begrenzt, einschließlich:

- Apple Push-Benachrichtigung Dienst (APNs)
- Android's Firebase Cloud Messaging (FCM)
- Web-Push
- Huawei Push

Diese Push-Dienste lehnen jede Push-Benachrichtigung ab, die diese Grenze überschreitet.

Braze reserviert einen Teil der Push-Nutzdaten für die Integration und Analytics. Die maximale Größe der Nutzdaten beträgt daher **3.807 Bytes**. Wenn Ihr Push diese Größe überschreitet, kann die Nachricht möglicherweise nicht gesendet werden. Am besten beschränken Sie Ihre Nutzdaten auf einige hundert Bytes.

Die folgenden Elemente in Ihrem Push machen Ihre Push-Nutzlast aus:

- Texte, wie z.B. den Titel und den Text der Nachricht
- Endgültiges Rendering jeder Liquid Personalisierung
- URLs für Bilder (aber nicht die Größe des Bildes selbst)
- URLs für Klick-Targeting
- Button Namen
- Schlüssel-Wert-Paare

### Tipps zur Reduzierung der Nutzlast

Um die Größe der Nutzlast zu reduzieren:

- Fassen Sie sich mit Ihrer Nachricht kurz. Ein guter allgemeiner Leitfaden ist, dass Sie weniger als 40 Zeichen benötigen, um einen Nutzen zu erzielen.
- Lassen Sie Leerzeichen und Zeilenumbrüche in Ihrer Kopie weg.
- Überlegen Sie, wie Liquid beim Senden gerendert wird. Da die endgültige Darstellung einer Personalisierung in Liquid von Nutzer:innen zu Nutzer:innen unterschiedlich ist, kann Braze nicht feststellen, ob eine Push-Nutzlast die Größenbeschränkung überschreitet, wenn Liquid enthalten ist. Wenn Ihr Liquid eine kürzere Nachricht wiedergibt, dürfte das kein Problem sein. Wenn Ihr Liquid jedoch zu einer längeren Nachricht führt, kann es sein, dass Ihr Push das Limit für die Nutzlast überschreitet. Testen Sie Ihre Push Nachricht immer auf einem echten Gerät, bevor Sie sie an Nutzer:innen senden.
- Erwägen Sie die Verkürzung von URLs mit einem URL-Verkürzer.

## Targeting optimieren

### Sammeln Sie relevante Benutzerdaten

Push-Benachrichtigungen sollten mit Sorgfalt behandelt werden, damit die Nutzer:innen rechtzeitig und relevant benachrichtigt werden. Braze sammelt nützliche Geräte- und Nutzungsinformationen, die zur gezielten Ansprache relevanter Segmente verwendet werden können. Diese Informationen sollten durch angepasste Events und Attribute ergänzt werden, die speziell für Ihre Anwendung gelten. Anhand dieser Daten können Sie gezielt Nachrichten verschicken, um die Öffnungsraten zu erhöhen und die Anzahl der Nutzer, die Push-Nachrichten deaktivieren, zu verringern.

### Eine Seite mit Benachrichtigungseinstellungen erstellen

Sie können in Ihrer App eine Einstellungsseite einrichten, auf der die Benutzer Ihnen mitteilen können, welche Benachrichtigungen sie erhalten möchten. Ein gängiger Ansatz ist die Erstellung eines angepassten booleschen Attributs in Braze, das dem Status der App-Einstellung entspricht. Eine Nachrichten-App könnte zum Beispiel Abonnementeinstellungen für aktuelle Nachrichten, Sportnachrichten oder Politik haben.

Wenn die Nachrichten-App eine Kampagne erstellen möchte, die sich nur an Nutzer richtet, die sich für Politik interessieren, fügt sie dem Segment den Attributfilter `Subscribes to Politics` hinzu. Wenn diese Option auf true gesetzt ist, erhalten nur Benutzer, die Benachrichtigungen abonniert haben, diese.

Weitere Informationen zum Festlegen von benutzerdefinierten Attributen finden Sie in den folgenden Artikeln für [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes) oder [REST API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification).

## Opt-Ins und Relevanz erhöhen

### Nutzerberechtigung erhalten

Die allgemeinen Statistiken für die Aktivierung von Push beziehen sich darauf, ob der Benutzer Benachrichtigungen mit seinem Betriebssystem genehmigt hat. Wenn Benutzer die Benachrichtigungen auf iOS deaktivieren, werden sie automatisch aus unserem System entfernt, da Apple das Senden des Push-Tokens nicht zulässt.

Für Android 13 und höher ist eine Berechtigung erforderlich, bevor Push-Benachrichtigungen angezeigt werden können. Bei älteren Android-Versionen werden Benachrichtigungen standardmäßig abonniert.

### Hauptnutzer:in für Push

Sie haben nur eine Chance, einen Benutzer um die Erlaubnis für Push zu bitten, und wenn er ablehnt, ist es sehr schwer, ihn davon zu überzeugen, Push in seinen Geräteeinstellungen wieder zu aktivieren. Aus diesem Grund sollten Sie die Nutzer:innen mit einer In-App-Nachricht auf Push vorbereiten, bevor Sie die System-Prompt anzeigen. Unter [Push Primer In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) erfahren Sie mehr über die Steigerung der Opt-Ins.

### Push-Abonnement-Kontrollen hinzufügen

Um zu vermeiden, dass Benutzer die Benachrichtigungen auf Geräteebene deaktivieren, wodurch ihr Push-Token für den Vordergrund vollständig entfernt wird, lassen Sie die Benutzer ihr Push-Abonnement direkt in Ihrer App steuern. Weitere Einzelheiten finden Sie unter [Aktualisieren des Push-Abonnementstatus]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions#update-push-subscription-state).

### Verstehen Sie den Status von Push-Abonnements

Der Status des Push-Abonnements ist keine Garantie dafür, dass eine Push-Nachricht zugestellt wird - die Benutzer müssen auch Push aktivieren, um Benachrichtigungen zu erhalten. Das liegt daran, dass ein Benutzerprofil mehrere Geräte mit unterschiedlichen Push-Berechtigungen für den Vordergrund, aber nur einen einzigen Push-Abonnementstatus haben kann.

Wenn ein:e Nutzer:in kein gültiges Vordergrund-Push-Token für eine App hat (d. h. er oder sie schaltet Push-Token auf Geräteebene über die Einstellungen aus, um keine Benachrichtigungen zu erhalten), kann sein oder ihr Abonnementstatus immer noch als `subscribed` für Push betrachtet werden. Diese:r Nutzer:in wäre jedoch nicht `Foreground Push Enabled for App` in Braze, da das Push-Token für den Vordergrund nicht gültig ist.

Wenn ein Nutzerprofil kein gültiges oder registriertes Push-Token für andere Apps hat, ist der Filter `Foreground Push Enabled` in der Segmentierung ebenfalls falsch.

## Implementieren Sie eine Sunset Policy für nicht reagierende Benutzer

Selbst wenn Sie nur relevante, zeitnahe Push-Benachrichtigungen senden, kann es sein, dass einige Benutzer nicht darauf reagieren und sie als spammig empfinden. Angenommen, ein Nutzer ignoriert wiederholt Ihre Push-Benachrichtigungen. In diesem Fall ist es eine gute Idee, ihnen keine Push-Nachrichten mehr zu schicken, bevor sie sich über die Kommunikation mit Ihrer App ärgern oder sie ganz deinstallieren. 

Erstellen Sie dazu eine [Sunset-Richtlinie]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies), die den Versand von Push-Benachrichtigungen an Nutzer:innen, die seit längerer Zeit keine direkte oder beeinflusste Nachricht geöffnet haben, einstellt.

1. Identifizieren Sie nicht reagierende Nutzer:innen anhand von direkten oder beeinflussten Zugriffen.
2. Stellen Sie das Senden von Push-Benachrichtigungen an diese Benutzer nach und nach ein.
3. Bevor Sie die Push-Benachrichtigungen ganz entfernen, sollten Sie eine letzte Benachrichtigung versenden, in der Sie erklären, warum Sie diese nicht mehr erhalten werden. Dies gibt den Nutzer:innen die Möglichkeit, ihr Interesse an weiteren Push-Nachrichten zu bekunden, indem sie diese Benachrichtigung öffnen.
4. Nachdem die Sunset Policy in Kraft getreten ist, erinnern Sie diese Nutzer mit einer [In-App-Nachricht]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) daran, dass sie zwar keine Push-Nachrichten mehr erhalten werden, aber dass die In-App-Nachrichtenkanäle weiterhin interessante und hilfreiche Informationen liefern werden.

Auch wenn Sie vielleicht zögern, den Versand von Push-Nachrichten an Nutzer einzustellen, die sich ursprünglich dafür entschieden haben, denken Sie daran, dass andere Nachrichtenkanäle diese Nutzer effektiver erreichen können, insbesondere wenn sie Ihre Push-Nachrichten zuvor ignoriert haben. Wenn der Nutzer Ihre E-Mails öffnet, sind E-Mail-Kampagnen eine gute Möglichkeit, ihn auch außerhalb Ihrer App zu erreichen. Wenn nicht, sind In-App-Nachrichten der beste Weg, Inhalte zu liefern, ohne zu riskieren, dass der Nutzer Ihre App deinstalliert.

## Konversions-Events für App-Zugriffe festlegen

Wenn Sie einer Push-Kampagne [Conversion-Ereignisse]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) zuweisen, können Sie das Öffnen von Apps für einen bestimmten Zeitraum nach dem Eingang der Kampagne verfolgen. Wenn Sie ein Conversion-Ereignis für das Öffnen einer App festlegen, erhalten Sie einen anderen Einblick als bei den Ergebnisstatistiken, die Sie normalerweise nach einer Push-Kampagne erhalten.

Während alle Ergebnisse von Push-Kampagnen die direkten Öffnungen und Öffnungen einer Nachricht aufschlüsseln (was sowohl direkte als auch [beeinflusste Öffnungen]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/) einschließt), wird beim Conversion-Tracking jede Art von Öffnung verfolgt, ob direkt oder beeinflusst.

Darüber hinaus können Sie mit dem Konversions-Event „Öffnet App“ App-Zugriffe verfolgen, die vor Ablauf dieser Konversionsfrist (z. B. drei Tage) stattfinden. Der Unterschied zu einem beeinflussten Zugriff besteht darin, dass die Zeit, die ein:e Nutzer:in für die Registrierung eines beeinflussten Zugriffs benötigt, von Person zu Person variieren kann, je nach dem früheren Engagement des Nutzers oder der Nutzerin.

## Ähnliche Artikel

Haben Sie nicht gefunden, wonach Sie gesucht haben? Sehen Sie sich diese zusätzlichen Artikel über bewährte Verfahren an:

- [Push-Benachrichtigungen und Bildformate]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/)
- [Push-Benachrichtigungen in der App]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)
- [Zustellbarkeit für chinesische Android-Geräte]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/)
- [Informationen vor dem Versand: Kanäle]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/know_before_send/)
