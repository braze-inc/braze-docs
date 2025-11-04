---
nav_title: Nachrichten-Formate
article_title: Push-Nachrichten und Bildformate
page_order: 5
page_type: reference
description: "Dieser Artikel beschreibt Nachrichten- und Bildformate für Push-Benachrichtigungen."
channel: push

---

# Push-Nachrichten und Bildformate

> Dieser Referenzartikel beschreibt Nachrichten- und Bildformate für Push-Benachrichtigungen.

Die besten Ergebnisse erzielen Sie, wenn Sie sich bei der Gestaltung Ihrer Push-Nachrichten an die folgenden Richtlinien für Bildgröße und Nachrichtenlänge halten. Je nach Vorhandensein eines Bildes, dem Benachrichtigungsstatus (iOS) und der Anzeigeeinstellung des Geräts des Benutzers sowie der Größe des Geräts kann es zu Abweichungen kommen. Im Zweifelsfall sollten Sie Ihre Texte kurz und knapp halten.

## iOS und Android Push

{% tabs local %}
{% tab Images %}

**Bildtyp** | **Empfohlene Bildgröße** | **Maximale Bildgröße** | **Dateitypen**
--- | --- | --- | ---
(iOS) 2:1 *Empfohlen* | 500 KB | 5 MB | PNG, JPEG, GIF
(Android) Push-Symbol | 500 KB | 5 MB | PNG, JPEG
(Android) Erweitertes Benachrichtigungssystem | 500 KB | 5 MB | PNG, JPEG
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% tab Text %}

| Nachrichtentyp | Empfohlene Nachrichtenlänge (nur Text) | Empfohlene Nachrichtenlänge (Rich)
--- | ---
(iOS) Sperrbildschirm | 160 Zeichen | 130 Zeichen
(iOS) Benachrichtigungszentrale | 160 Zeichen | 130 Zeichen
(iOS) Banner-Alarm | 80 Zeichen | 65 Zeichen
(Android) Sperrbildschirm | 49 Zeichen | --
(Android) Notification Drawer | 597 Zeichen | --
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

Sie fragen sich, wie viele Zeichen Sie in einer iOS-Push-Benachrichtigung verwenden können, ohne dass diese abgeschnitten wird? Sehen Sie sich unsere [Richtlinien für iOS-Zeichen]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count) an.

{% endtab %}
{% tab Payload Size %}

**Plattform** | **Größe**
--- | ---
vor iOS 8 | 0.256 KB
nach iOS 8 | 2 KB
Android (FCM) | 4 KB
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Image Example %}
{% subtabs %}
{% subtab iOS %}

\![iOS Push-Benachrichtigung mit Text, der lautet: "Hallo! Dies ist ein iOS Push mit einem Bild" mit einem Emoji. Neben dem Text befindet sich ein kleines Bild.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
\![iOS Push-Benachrichtigung über einen Hard Push mit dem gleichen Text wie die vorherige Nachricht mit einem erweiterten Bild vor dem Text.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endsubtab %}
{% subtab Android %}

\![Android Push-Benachrichtigung mit einem großen Bild unter dem Text der Nachricht.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Große Bildbenachrichtigungen werden am besten angezeigt, wenn Sie ein Bild mit einer Größe von mindestens 600x300 Pixeln verwenden.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Text Example %}
{% subtabs %}
{% subtab iOS %}

\![iOS Push-Benachrichtigung mit Text, der lautet: "Hallo! Dies ist ein iOS Push".]({% image_buster /assets/img_archive/iOS_push_notification_small.png %})

{% endsubtab %}
{% subtab Android %}
\![Android Push-Benachrichtigung wird auf dem Startbildschirm angezeigt.]({% image_buster /assets/img_archive/Push_Android_2.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Web-Push

{% tabs local %}
{% tab Images %}

| **Browser** | **Empfohlene Symbolgröße**
| --- | ---
Chrome | 192 x 192 ≥
Firefox | 192 x 192 ≥
Safari | 192 x 192 ≥ (Die Symbole sind pro Kampagne mit Safari 16 unter macOS 13+ konfigurierbar)
Opera | 192x192 ≥
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| **Browser** | **Plattform** | **Großes Bildformat**
| --- | --- | ---
Chrome | Android | Seitenverhältnis 2:1
Firefox | Android | --
Chrome | Windows | Seitenverhältnis 2:1
Edge | Windows | Seitenverhältnis 2:1
Firefox | Windows | --
Firefox | Windows | Seitenverhältnis 2:1
Safari | macOS | --
Chrome | macOS | --
Firefox | macOS | --
Opera | macOS | --
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Text %}

| **Browser** | **Plattform** | **Maximale Titellänge**  | **Maximale Länge des Nachrichtentexts**
| --- | --- | --- | ---
Chrome | Android | 35 | (50 %)
Firefox | Android | 35 | (50 %)
Chrome | Windows | (50 %) | 120
Edge | Windows | (50 %) | 120
Firefox | Windows | 54 | 200
Opera | Windows | (50 %) | 120
Chrome | macOS | 35 | (50 %)
Safari | macOS | 38 | 84
Firefox | macOS | 38 | 42
Opera | macOS | 38 | 42
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}


