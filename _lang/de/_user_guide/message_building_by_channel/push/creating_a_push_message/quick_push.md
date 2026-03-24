---
nav_title: Schnelle Push-Nachrichten
article_title: Schnelle Push-Nachrichten
alias: "/quick_push/"
description: "Dieser Artikel beschreibt, was Sie bei der Erstellung einer Push-Kampagne oder eines Canvas mit der Push-Schnellbearbeitung beachten sollten."
---

# Schnelle Push-Nachrichten

Wenn Sie eine Push-Kampagne oder ein Canvas in Braze erstellen, können Sie mehrere Plattformen und Geräte auswählen, um eine Nachricht für alle Plattformen in einem einzigen Bearbeitungsvorgang – dem sogenannten Quick Push – zu erstellen.

## Anwendungsfälle

Diese Art der Bearbeitung eignet sich am besten für die folgenden Anwendungsfälle:

- Mobile Push-Kampagnen und Canvas-Nachrichten-Schritte, die an mehrere Gerätetypen (z. B. sowohl iOS als auch Android) gesendet werden müssen.
- Zeitkritische Push-Benachrichtigungen, die schnell und präzise auf mehrere Plattformen ausgerichtet werden müssen, wobei der Inhalt auf allen Plattformen gleich ist (z. B. Eilmeldungen oder Live-Spiel-Updates).

## Erstellen einer schnellen Push-Kampagne oder eines Canvas

So erstellen Sie eine Kampagne für mehrere Plattformen und Geräte:

1. Erstellen Sie eine Kampagne oder fügen Sie einen [Nachrichten-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) zu einem Canvas hinzu.  
2. Wählen Sie **Push-Benachrichtigung** aus.
3. Wählen Sie die gewünschten Plattformen (Mobilgerät, Internet, Kindle) und Mobilgeräte (iOS, Android) aus. Wenn Sie mehrere Geräte auswählen, sind keine Mehrvariantentests für Ihre Kampagne verfügbar.

### Plattformen für eine Kampagne auswählen
![Optionen zur Auswahl mehrerer Plattformen für eine Push-Kampagne, z. B. Mobilgerät, Internet und Kindle, sowie mehrerer Geräte, z. B. iOS und Android.]({% image_buster /assets/img_archive/quick_push_1.png %})

### Plattformen für einen Canvas-Schritt auswählen
![Optionen zur Auswahl mehrerer Plattformen für einen Push-Nachrichten-Schritt, z. B. Mobilgerät, Internet und Kindle, sowie mehrerer Geräte, z. B. iOS und Android.]({% image_buster /assets/img_archive/quick_push_4.png %})

{:start="4"}
4. Wählen Sie **Bestätigen** aus. Nachdem Sie **Bestätigen** ausgewählt haben, können Sie Ihre ausgewählten Plattformen oder Geräte nicht mehr ändern.
5. Fahren Sie mit der Einrichtung Ihrer Kampagne oder Ihres Canvas fort.

Der Editor wird etwas anders aussehen als gewohnt. Lesen Sie weiter, um zu erfahren, was anders ist.

### Was ist anders?

Auf dem Tab **Verfassen** können Sie einen Titel, eine Nachricht und das Klickverhalten für alle von Ihnen gewählten Plattformen und Geräte festlegen.

Das Vorschaufenster bietet einen ungefähren Eindruck davon, wie Ihre Nachricht auf den einzelnen Plattformen aussehen wird. Es kann Ihnen zwar einen guten Anhaltspunkt dafür geben, wo Sie die Zeichengrenzen erreichen könnten, aber denken Sie daran, Ihre Nachrichten immer auf einem echten Gerät zu testen, bevor Sie Ihre Kampagne versenden.

![Eine einzige Bearbeitungsansicht mit einem Feld für Titel, Nachricht und Klickverhalten für drei Push-Typen: iOS, Android und Web.]({% image_buster /assets/img_archive/quick_push_2.png %})

Wählen Sie im Abschnitt **Assets** die Bilder aus, die für jede Plattform angezeigt werden sollen, oder laden Sie sie hoch. Beachten Sie, dass verschiedene Geräte unterschiedliche Spezifikationen für Bilder und Zeichenzahlen haben. Hilfe finden Sie unter [Push-Bild- und Textspezifikationen]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push).

![Abschnitt „Assets" in der Einzelbearbeitungsansicht mit Feldern für Push-Symbolbild, iOS-Benachrichtigungsbild, Android-Benachrichtigungsbild und Web-Benachrichtigungsbild.]({% image_buster /assets/img_archive/quick_push_3.png %}){:style="max-width:50%"}

Schließen Sie dann die Einrichtung Ihrer Push-Kampagne wie gewohnt ab. Weitere Informationen finden Sie unter [Erstellen einer Push-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/).

## Wissenswertes

### Benachrichtigungstyp

Der Benachrichtigungstyp ist standardmäßig auf „Standard-Push" eingestellt und kann nicht geändert werden. Wenn Sie eine andere Art von Push erstellen möchten, z. B. Push-Storys oder Inline-Image (Android), erstellen Sie separate Kampagnen für jeden Gerätetyp.

### Mehrvariantentests

Wenn Sie mehrere Geräte für mobile Plattformen auswählen, also z. B. sowohl iOS als auch Android, sind keine Mehrvariantentests für Ihre Kampagne verfügbar. Wenn Sie Mehrvariantentests durchführen möchten, erstellen Sie separate Kampagnen für jeden Gerätetyp.

### Gerätespezifische Einstellungen

Sie können plattformspezifische Einstellungen im Editor bearbeiten. Dazu gehören Einstellungen wie [Push-Action-Buttons]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_action_buttons/), Benachrichtigungskanäle und -gruppen, TTL, Anzeigepriorität, Töne und mehr. 

Beachten Sie, dass Push-Action-Buttons beim Targeting von sowohl iOS als auch Android mit schnellen Push-Kampagnen nicht unterstützt werden. Weitere Informationen zu gerätespezifischen Einstellungen finden Sie in den folgenden Artikelsammlungen:

- [iOS-Optionen]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios)
- [Android-Optionen]({{site.baseurl}}/user_guide/message_building_by_channel/push/android)