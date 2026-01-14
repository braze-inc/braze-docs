---
nav_title: Dark Mode Themen
article_title: Dunkler Modus für In-App-Nachrichten
page_order: 5
description: "Dieser Referenzartikel behandelt die Unterstützung des Dark Mode für In-App-Nachrichten von Braze, einschließlich der Einstellung eines Dark-Mode-Themas und Kompatibilitätsüberlegungen."
channel:
  - in-app messages

---

# Themen für den dunklen Modus

> Der dunkle Modus bietet Nutzern die Möglichkeit, eine systemweite Farbpräferenz einzustellen (eingeführt in [Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) und [iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)). Die "dunklen" Themen sollen die Akkulaufzeit schonen und die Augen der Benutzer entlasten. Gleichzeitig bieten sie App-Entwicklern eine einfachere Möglichkeit, die von den Benutzern bevorzugten dunklen Farbthemen zu implementieren.

In-App-Nachrichten von Braze unterstützen das Hinzufügen eines alternativen dunklen Themas, um Ihren Nutzer:innen je nach Vorliebe die richtige Nachricht in der richtigen Farbe zuzustellen und die Konsistenz mit dem Design Ihrer App zu gewährleisten.

## So funktioniert der Dunkle Modus

Benutzer mit Versionen von mindestens Android 10 oder iOS 13 und höher können den Dark Mode in den Einstellungen ihres Geräts ein- oder ausschalten.

Wenn der dunkle Modus aktiviert ist, werden die Menüs und Bildschirme des Geräts (Push-Benachrichtigungen, Geräteeinstellungen usw.) in einem dunklen Grau angezeigt. Apps können auch den Dark Mode unterstützen, indem Sie die alternativen Themen im Code der App angeben.

## Einstellen eines Themas für den dunklen Modus

Mit der neuen Option Dunkler Modus, die Sie auf der Registerkarte Stil finden, wenn Sie [eine In-App-Nachricht erstellen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/), können Sie ganz einfach ein alternatives Farbthema für Benutzer hinzufügen, die sich auf ihrem Gerät im dunklen Modus befinden.

![Nutzer:in schaltet beim Erstellen einer In-App-Nachricht auf dem Tab Stil zwischen den Stilen Heller Modus und Dunkler Modus um.]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

Wenn diese Option aktiviert ist, können Sie mit der Farbauswahl dunkle Themenfarben für Ihre In-App-Nachrichten wählen oder vorhandene [Farbprofile]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) auswählen, um vorhandene dunkle oder helle Themen wiederzuverwenden.

{% alert note %}
Sie können dieses Feature auch dann nutzen, wenn Ihre App kein eigenes dunkles Thema anbietet. Geräte, die den Dark Mode nicht unterstützen, zeigen jedoch standardmäßig das Light-Thema an. Wenn Sie das Design Ihres Geräts unter Android ändern, während eine In-App-Nachricht angezeigt wird, ändert sich das für diese In-App-Nachricht verwendete Design nicht.
{% endalert %}

### Den dunklen Modus konsequent nutzen

Um den dunklen Modus für alle In-App-Nachrichten zu verwenden, gehen Sie zu **Vorlagen** > **In-App-Nachrichtenvorlagen**.

Wählen Sie dort die Option [Farbprofil erstellen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) aus dem Dropdown-Menü. Erstellen Sie ein Farbprofil, das auf Ihr Dark-Mode-Thema abgestimmt ist. Dann können Sie jedes Mal, wenn Sie eine Version einer In-App-Nachricht im dunklen Modus erstellen, dieses Farbprofil auswählen und das Aussehen Ihrer In-App-Nachrichten konsistent halten.

## Kompatibilität

- Ihre Benutzer müssen iOS-Geräte der Version 13 oder höher oder Android-Geräte der Version 10 oder höher verwenden.
- Braze iOS SDK v3.21.0+ Braze Android SDK v3.8.0+ ist erforderlich.

{% alert note %}
Dark Mode Apps wurden mit Android 10 und iOS 13 eingeführt. Benutzern, die ihr Telefon nicht mindestens auf diese Versionen aktualisiert haben, wird nur das Light-Theme angezeigt. <br><br>Kampagnen werden weiterhin allen Nutzern zugestellt, die für die von Ihnen ausgewählte Zielgruppe in Frage kommen, unabhängig von der Einstellung des Dark Mode oder der Betriebssystemversion des Nutzers.
{% endalert %}

## HTML In-App Nachrichten verwenden

Um ein dunkles und helles Thema für HTML In-App-Nachrichten zu erstellen, können Sie die [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) CSS Media Feature verwenden, um die Präferenz der Nutzerin oder des Nutzers zu erkennen.

Zum Beispiel:

```css
@media (prefers-color-scheme: dark) {
  body {
    background: #333;
    color: white;
  }
}

@media (prefers-color-scheme: light) {
  body {
    background: white;
    color: #555;
  }
}
```

