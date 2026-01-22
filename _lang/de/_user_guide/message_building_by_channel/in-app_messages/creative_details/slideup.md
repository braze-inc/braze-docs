---
nav_title: Slideup
article_title: Slideup In-App-Nachrichten
page_order: 2
channel:
  - in-app messages
tool:
  - Media
description: "Dieser Artikel erläutert die Kommunikations- und Gestaltungsvorgaben für Slideup-Nachrichten in der App."

---

# Slideup In-App Nachrichten

> Unsere Slideups erscheinen in der Regel am oberen oder unteren Rand des App-Bildschirms (Sie können dies bei der Erstellung Ihrer Nachricht einstellen). Diese sind ideal, um Ihre Benutzer über neue Nutzungsbedingungen, Cookies und andere Informationen zu informieren. Diese sind nicht aufdringlich und ermöglichen es Ihren Benutzern, weiterhin mit Ihrer App zu interagieren, während die Nachricht angezeigt wird.

\![Zwei aufklappbare In-App-Nachrichten, von denen eine am oberen und die andere am unteren Rand des Bildschirms angezeigt wird, mit detaillierten Bild- und Textempfehlungen. Siehe die folgenden Abschnitte für Details.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width: 40%; border: none;"}

## Bild- und Textverhalten

Slideup-Nachrichten können bis zu drei Zeilen Text enthalten, bevor sie durch Ellipsen abgeschnitten werden. Bilder in Slideups werden niemals beschnitten oder abgeschnitten - sie werden immer so verkleinert, dass sie in den 50 x 50 Pixel großen Bildcontainer passen.

- Alle Bilder müssen kleiner als 5 MB sein.
- Wir akzeptieren nur die Dateitypen PNG, JPEG und GIF.
- Wir empfehlen, dass Ihre Bilder 500 KB groß sind.

{% alert tip %} Erstellen Sie Assets mit Vertrauen! Unsere Templates für In-App-Nachricht-Bilder und Overlays für die sichere Zone sind so konzipiert, dass sie auf Geräten aller Größen gut funktionieren. [Download Design-Vorlagen ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Layout | Asset-Größe | Anmerkungen |
|--- | --- | --- |
| Bild + Text | Seitenverhältnis 1:1<br>Hochauflösend 150 x 150 px<br> Minimum 50 x 50 px | Bilder mit unterschiedlichen Seitenverhältnissen passen in einen quadratischen Bildcontainer, ohne dass sie beschnitten werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Sie sollten [Ihre Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) immer [als Vorschau anzeigen und]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) auf verschiedenen Geräten [testen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/), um sicherzustellen, dass Bilder und Nachrichten wie erwartet angezeigt werden. Beachten Sie, dass die Vorschau im Editor von der tatsächlichen Darstellung auf dem Endgerät abweichen kann.

## Mobile Geräte

Auf mobilen Geräten erscheinen Slideups am oberen oder unteren Rand des App-Bildschirms. Sie können dies bei der Erstellung Ihrer Nachricht angeben. Sie können das Slideup mit einer Wischbewegung schließen oder es durch Antippen öffnen, wenn eine Klickaktion enthalten ist. Wenn dem Slideup eine Klickaktion hinzugefügt wird, wird das Größer-als-Zeichen ">" angezeigt.

## Größere Bildschirme

{% tabs %}
{% tab Desktop %}

In Desktop-Browsern werden In-App-Nachrichten wie im Screenshot als Slideup in der Bildschirmecke angezeigt (sofern bei der Erstellung der In-App-Nachricht nicht anders angegeben). Das Slideup kann über den Button "X" geschlossen werden.

In-App-Nachricht von Slideup, wie sie in einem Desktop-Browser erscheint. Die Nachricht erscheint in der unteren rechten Ecke des Bildschirms und nimmt nicht die gesamte Breite des Bildschirms ein.]({% image_buster /assets/img/slideup-large-viewport.png %}){: style="border: none;"}

{% endtab %}
{% tab Tablet %}

Auf einem Tablet erscheint unten auf dem Bildschirm eine In-App-Nachricht. Ähnlich wie auf mobilen Geräten können Nutzer das Slideup mit einer Wischbewegung schließen oder es durch Antippen öffnen, wenn eine Klickaktion enthalten ist. Wenn dem Slideup eine Klickaktion hinzugefügt wird, wird das Größer-als-Zeichen ">" angezeigt. Eine Schaltfläche "X" zum Schließen wird standardmäßig nicht angezeigt.

\![Slideup In-App-Nachricht, wie sie auf einem Tablet-Bildschirm erscheint. Die Nachricht erscheint in der unteren Mitte des Bildschirms und nimmt nicht die gesamte Breite des Bildschirms ein.]({% image_buster /assets/img/slideup-tablet.png %}){: style="border: none;"}

{% endtab %}
{% endtabs %}

