---
nav_title: "Rich-Benachrichtigungen erstellen"
article_title: "Erstellen umfangreicher Push-Benachrichtigungen für iOS"
page_order: 3
page_type: tutorial
description: "In diesem Tutorial erfahren Sie, welche Voraussetzungen erfüllt sein müssen und wie Sie iOS Rich Notifications für Ihre Braze-Kampagnen erstellen können."

platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# Erstellen umfangreicher Push-Benachrichtigungen für iOS

> Mit Rich Notifications können Sie Ihre Push-Benachrichtigungen noch individueller gestalten, indem Sie über den Text hinaus zusätzliche Inhalte hinzufügen. Android-Benachrichtigungen enthalten schon seit einiger Zeit Bilder in Push-Benachrichtigungen, die als "Erweitertes Benachrichtigungsbild" angezeigt werden. Ab iOS 10 können Ihre Kunden iOS-Push-Benachrichtigungen erhalten, die GIFs, Bilder, Videos oder Audio enthalten.

## Voraussetzungen

Bevor Sie eine Rich-Push-Benachrichtigung für iOS erstellen, sollten Sie die folgenden Details beachten:

- Um sicherzustellen, dass Ihre App Rich Notifications senden kann, folgen Sie den Anweisungen zur [iOS-Push-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications), da Ihr Entwickler eine Service-Erweiterung zu Ihrer App hinzufügen muss.
- Zu den Dateitypen, die wir derzeit für das direkte Hochladen in unserem Dashboard unterstützen, gehören JPEG, PNG oder GIF. Diese Dateien können zusammen mit diesen zusätzlichen Dateitypen auch in das URL-Feld für Vorlagen eingegeben werden: AIF, M4A, MP3, MP4 oder WAV.
- Informieren Sie sich in [der Dokumentation von Apple](https://developer.apple.com/reference/usernotifications/unnotificationattachment) über die Einschränkungen und Spezifikationen der Medien.
- Rich-Push-Benachrichtigungen für iOS sind nicht verfügbar, wenn Sie eine Quick-Push-Kampagne erstellen.
- iOS skaliert Bilder so, dass sie in den Bildschirm passen und skaliert reiche Bilder für die aktive oder gesperrte Ansicht.

{% alert note %}
Ab Januar 2020 können iOS Rich-Push-Benachrichtigungen Bilder mit einer Größe von 1038x1038 unter 10 MB verarbeiten. Wir empfehlen jedoch, eine möglichst kleine Dateigröße zu verwenden. In der Praxis kann das Versenden großer Dateien sowohl unnötigen Stress für das Netzwerk verursachen als auch dazu führen, dass es häufiger zu Timeouts beim Herunterladen kommt.
{% endalert %}

### Zeichenanzahl

Wir können zwar keine feste Regel für die genaue Anzahl von Zeichen in einer Push-Nachricht aufstellen, aber wir [bieten Ihnen einige Richtlinien]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/), die Sie bei der Gestaltung von iOS-Nachrichten berücksichtigen sollten. Je nach Vorhandensein eines Bildes, dem Benachrichtigungsstatus und der Anzeigeeinstellung des Geräts des Benutzers sowie der Größe des Geräts kann es zu Abweichungen kommen. Im Zweifelsfall machen Sie es kurz und bündig.

Braze empfiehlt, jede Textzeile für den optionalen Titel und den Nachrichtentext in einer mobilen Push-Benachrichtigung auf etwa 30 bis 40 Zeichen zu beschränken.

#### Benachrichtigungsstatus

Ihre Benutzer können Push-Benachrichtigungen in einer Vielzahl von Situationen sehen, und sie können unterschiedliche Textlängen sehen.

<table>
<thead>
  <tr>
    <th>Sperrbildschirm oder Notification Center</th>
    <th>Erweitert</th>
    <th>Gerät aktiv</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">Dies ist das häufigste Szenario.<br><br><b>Titel:</b> 1 Zeile Text<br><b>Text:</b> 4 Zeilen Text<br><b>Bild:</b> Quadratische Miniaturansicht</td>
    <td width="33%">Wenn ein Benutzer lange auf eine Nachricht drückt.<br><br><b>Titel:</b> 1 Zeile Text<br><b>Text:</b> 7 Zeilen Text<br><b>Bild:</b> Seitenverhältnis 2:1 (empfohlen, siehe folgender Hinweis)</td>
    <td width="33%">Wenn ein Benutzer eine Push-Nachricht erhält, während sein Telefon entsperrt und aktiv ist.<br><br><b>Titel:</b> 1 Zeile Text<br><b>Text:</b> 2 Zeilen Text</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

![Beispiel für Push-Benachrichtigungen, die auf dem Sperrbildschirm angezeigt werden, wenn sie erweitert sind und wenn das Gerät aktiv ist.]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
Wir empfehlen ein Seitenverhältnis von 2:1 für erweiterte Push-Benachrichtigungen, aber fast jedes Seitenverhältnis wird unterstützt. Die Bilder erstrecken sich immer über die gesamte Breite der Benachrichtigung, und die Höhe wird entsprechend angepasst.
{% endalert %}

#### Variablen bei der Textkürzung

Beachten Sie bei der Erstellung von Inhalten die folgenden Szenarien, die sich darauf auswirken können, wie viel Text angezeigt wird.

{% tabs %}
{% tab Timing %}

Je nachdem, wann ein:e Nutzer:in eine Push-Benachrichtigung öffnet, kann der Zeitstempel den Titeltext verkürzen.

![Beispiel einer Push-Benachrichtigung mit dem Zeitstempel "jetzt" und der Anzahl der Zeichen im Titel von 35.]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>Anzahl der Zeichen im Titel: **35**

![Beispiel einer Push-Benachrichtigung mit einem Zeitstempel von "vor 3 Stunden" und einer Anzahl von 33 Zeichen im Titel.]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>Anzahl der Zeichen im Titel: **33**

![Beispiel einer Push-Benachrichtigung mit einem Zeitstempel von "Gestern, 8:37 AM" und einer Anzahl von 22 Zeichen im Titel.]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>Anzahl der Zeichen im Titel: **22**

{% endtab %}
{% tab Images %}

Der Text wird um etwa 10 Zeichen pro Zeile gekürzt, wenn ein Bild vorhanden ist.

![Beispiel einer Push-Benachrichtigung ohne Bild und mit 179 Zeichen im Text.]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>Anzahl der Zeichen im Text: **179**

![Beispiel einer Push-Benachrichtigung mit einem Bild und einer Zeichenanzahl von 154 im Text.]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>Anzahl der Zeichen im Text: **154**

{% endtab %}
{% tab Interruption level %}

In iOS 15 wird bei den Bezeichnungen "Zeitkritisch" und "Kritisch" der Titel in eine neue Zeile ohne den Zeitstempel verschoben, so dass er etwas mehr Platz erhält.

![Beispiel für eine Push-Benachrichtigung, die weder als zeitkritisch noch als kritisch bezeichnet wird und deren Titel 35 Zeichen enthält.]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>Anzahl der Zeichen im Titel: **35**

![Beispiel für eine Push-Benachrichtigung mit der Bezeichnung Time Sensitive und einer Zeichenanzahl von 39 im Titel.]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>Anzahl der Zeichen im Titel: **39**

{% endtab %}
{% tab More %}

Die folgenden Details können sich ebenfalls auf die Textkürzung auswirken:

- **Einstellungen für das Telefondisplay:** Ein:e Nutzer:in kann die globale Schriftgröße der Benutzeroberfläche auf seinem oder ihrem Telefon erhöhen oder verringern, in der Regel aus Gründen der Barrierefreiheit.
- **Gerätebreite:** Die Nachricht könnte auf einem kleinen Telefon oder einem breiten iPad angezeigt werden.
- **Content-Typen:** Emojis und breite Zeichen wie „m“ und „w“ nehmen mehr Platz ein als „i“ oder „t“, und längere Wörter wie „Engagement“ können einen abrupteren Zeilenumbruch verursachen als kürzere Wörter.

{% endtab %}
{% endtabs %}

## Einrichten Ihrer iOS Rich Notification

### Schritt 1: Erstellen Sie eine Push-Kampagne

Folgen Sie den [Schritten]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) der [Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message), um eine Push-Benachrichtigung für iOS zu verfassen. Sie verwenden denselben Composer, den Sie auch für die Einrichtung von Push-Benachrichtigungen verwenden, die keinen Rich Content enthalten.

### Schritt 2: Medien hinzufügen

Fügen Sie Ihre Bild-, GIF-, Audio- oder Videodatei in das Feld **Rich Notification Media** im Composer der Nachricht ein. Lesen Sie in den [Anforderungen nach](#requirements), wie Sie Ihre Inhaltsdateien hinzufügen können.

![Ein Beispiel für einen zusammenfassenden Text für eine Push-Benachrichtigung.]({% image_buster /assets/img_archive/rich_notification_add_image.png %}){: style="max-width:70%;" }

Sie können diese Nachricht auch so einschränken, dass sie nur an Benutzer gesendet wird, die ein Gerät mit iOS 10 besitzen. Für Benutzer, die nicht auf iOS 10 aktualisiert haben, erscheinen die Benachrichtigungen als reiner Text ohne Rich Content, wenn Sie die Option **Nur an Geräte mit Rich Notification-Unterstützung senden** nicht aktivieren.

![Der Bereich Erweitertes Benachrichtigungsbild, wo Sie ein Bild hinzufügen oder eine Bild-URL eingeben können.]({% image_buster /assets/img_archive/rich_notification_ios10_select.png %}){: style="max-width:70%;" }

### Schritt 3: Fahren Sie mit der Erstellung Ihrer Kampagne fort

Sobald Ihre Rich-Benachrichtigung auf das Dashboard hochgeladen ist, können Sie mit der [Zeitplanung Ihrer Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign) fortfahren.

Wenn ein:e Nutzer:in die Push-Benachrichtigung erhält, kann er oder sie auf die Push-Nachricht drücken, um das Bild zu vergrößern.

Ein Nutzer:innen erhält eine Push-Benachrichtigung und drückt die Nachricht, um ein erweitertes Bild mit dem Text "Hallo!" anzuzeigen.]({% image_buster /assets/img_archive/rich_notification_ios.gif %}){: style="max-width:50%;" }

