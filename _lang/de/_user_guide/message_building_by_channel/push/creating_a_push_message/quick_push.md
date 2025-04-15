---
nav_title: Schnelle Push-Nachrichten
article_title: Schnelle Push-Nachrichten
alias: "/quick_push/"
description: "Dieser Artikel beschreibt, was Sie bei der Erstellung einer Push-Kampagne oder Cavnas mit der Push-Schnellbearbeitung beachten sollten."
---

# Schnelle Push-Nachrichten

Wenn Sie eine Push-Kampagne oder ein Canvas in Braze erstellen, können Sie mehrere Plattformen und Geräte auswählen, um eine Nachricht für alle Plattformen in einem einzigen Bearbeitungsvorgang, dem so genannten Quick Push, zu erstellen.

## Anwendungsfälle

Diese Art der Bearbeitung eignet sich am besten für die folgenden Anwendungsfälle:

- Mobile Push-Kampagnen und Canvas-Schritte für Nachrichten, die an mehrere Geräte (z. B. sowohl iOS als auch Android) gesendet werden müssen.
- Zeitabhängige Push-Benachrichtigungen, die schnell und präzise auf mehrere Plattformen ausgerichtet werden müssen, wobei der Inhalt auf allen Plattformen gleich ist (z. B. aktuelle Nachrichten oder Live-Spiel-Updates).

## Erstellen einer schnellen Push-Kampagne oder eines Canvas

So erstellen Sie Kampagnen für mehrere Plattformen und Geräte:

1. Erstellen Sie eine Kampagne oder fügen Sie einen [Nachrichten-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) zu einem Canvas hinzu.  
2. Wählen Sie **Push-Benachrichtigung**.
3. Wählen Sie die gewünschten Plattformen (Mobile, Web, Kindle) und Mobilgeräte (iOS, Android). Wenn Sie mehrere Geräte auswählen, sind keine Mehrvariantentests möglich.

### Plattformen für eine Kampagne auswählen
![Möglichkeit zur Auswahl mehrerer Plattformen für Push-Kampagnen wie Mobilgerät, Web und Kindle oder mehrerer Geräte wie iOS und Android.][1]

### Plattformen für einen Canvas-Schritt auswählen
![Optionen, um mehrere Plattformen für einen Push-Nachrichten-Schritt auszuwählen, z. B. Mobile, Internet und Kindle, und mehrere Geräte, z. B. iOS und Android.][8]

{:start="4"}
4\. Wählen Sie **Bestätigen**. Nachdem Sie **Bestätigen** ausgewählt haben, können Sie Ihre ausgewählten Plattformen oder Geräte nicht mehr ändern.
5\. Fahren Sie mit dem Einrichten Ihrer Kampagne oder Ihres Canvas fort.

Der Editor wird etwas anders aussehen als sonst. Lesen Sie weiter, um zu erfahren, was anders ist.

### Was ist anders?

Auf der Registerkarte **Verfassen** können Sie einen Titel, eine Nachricht und das Verhalten beim Anklicken für alle von Ihnen gewählten Plattformen und Geräte festlegen.

Das Vorschaufenster bietet einen ungefähren Eindruck, wie Ihre Nachricht auf den einzelnen Plattformen aussehen wird. Es kann Ihnen zwar einen guten Anhaltspunkt dafür geben, wo Sie die Zeichengrenzen erreichen könnten, aber denken Sie daran, dass Sie Ihre Nachrichten immer auf einem echten Gerät testen sollten, bevor Sie Ihre Kampagne versenden.

![Eine einzige Bearbeitungsansicht mit einem Feld für Titel, Nachricht und Klickverhalten für drei Push-Typen: iOS, Android und Web.][2]

Wählen Sie im Bereich **Assets** die Bilder aus, die für jede Plattform angezeigt werden sollen, oder laden Sie sie hoch. Denken Sie daran, dass verschiedene Geräte unterschiedliche Spezifikationen für Bilder und Zeichenzahlen haben. Weitere Informationen finden Sie unter [Push-Nachrichten- und Bildformate][3] ].

![Abschnitt "Assets" in der Einzelbearbeitungsansicht mit Feldern für Push-Symbolbild, iOS-Benachrichtigungsbild, Android-Benachrichtigungsbild und Web-Benachrichtigungsbild.][4]{:style="max-width:50%"}

Beenden Sie dann die Einrichtung Ihrer Push-Kampagne wie gewohnt. Weitere Informationen finden Sie unter [Erstellen einer Push-Kampagne][5] ].

## Was Sie wissen sollten

### Benachrichtigungstyp

Der Benachrichtigungstyp ist standardmäßig auf "Standard-Push" eingestellt und kann nicht geändert werden. Wenn Sie eine andere Push-Benachrichtigung wie Push-Stories oder Inline-Image (Android) erstellen möchten, erstellen Sie separate Kampagnen für jeden Gerätetyp.

### Mehrvariantentests

Wenn Sie mehrere Geräte für mobile Plattformen also z. B. sowohl iOS als auch Android auswählen, sind keine Mehrvariantentests für Ihre Kampagne verfügbar. Wenn Sie Mehrvariantentests durchführen möchten, erstellen Sie separate Kampagnen für jeden Gerätetyp.

### Gerätespezifische Einstellungen

Sie können plattformspezifische Einstellungen im Editor bearbeiten. Dazu gehören Einstellungen wie [Push-Action-Tasten]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_action_buttons/), Benachrichtigungskanäle und -gruppen, TTL, Anzeigepriorität, Töne und mehr.

Weitere Informationen zu gerätespezifischen Einstellungen finden Sie in den folgenden Artikelsammlungen:

- [iOS-Optionen][6]
- [Android-Optionen][7]


[1]: {% image_buster /assets/img_archive/quick_push_1.png %}
[2]: {% image_buster /assets/img_archive/quick_push_2.png %}
[4]: {% image_buster /assets/img_archive/quick_push_3.png %}
[8]: {% image_buster /assets/img_archive/quick_push_4.png %}
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/ios
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/android