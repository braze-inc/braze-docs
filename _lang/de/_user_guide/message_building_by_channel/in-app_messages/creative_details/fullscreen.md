---
nav_title: "Vollbild"
article_title: In-App-Nachrichten im Vollbildmodus
description: "Dieser Referenzartikel behandelt die Anforderungen an die Nachrichten und das Design von In-App-Nachrichten im Vollbildmodus."
page_type: reference
page_order: 0
channel:
  - in-app messages
tool:
  - Media

---

# In-App-Nachrichten im Vollbildmodus

> Nachrichten im Vollbildmodus nehmen den gesamten Bildschirm des Geräts ein! Dieser Nachrichtentyp eignet sich hervorragend, wenn Sie die Aufmerksamkeit Ihrer Nutzer wirklich benötigen, z. B. bei obligatorischen App-Updates.

{% tabs %}
{% tab Portrait %}

\![Zwei In-App-Nachrichten im Vollbildmodus nebeneinander im Hochformat, mit detaillierten Bild- und Textempfehlungen. Siehe die folgenden Abschnitte für Details.]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Landscape %}

\![Zwei In-App-Nachrichten im Vollbildmodus nebeneinander im Querformat, mit detaillierten Bild- und Textempfehlungen. Siehe die folgenden Abschnitte für Details.]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## Bilder

In-App-Nachrichten im Vollbildmodus füllen die gesamte Höhe eines Geräts aus und werden bei Bedarf horizontal (links und rechts) zugeschnitten. Bild- und Textnachrichten im Vollbildmodus füllen 50% der Höhe eines Geräts aus. Alle Vollbild-In-App-Nachrichten füllen die Statusleiste auf „Notch“-Geräten aus.

- Alle Bilder müssen kleiner als 5 MB sein.
- Wir akzeptieren nur die Dateitypen PNG, JPEG und [GIF]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs#gifs).
- Wir empfehlen, dass Ihre Bilder 500 KB groß sind.

{% alert tip %} Erstellen Sie Assets mit Vertrauen! Unsere Templates für In-App-Nachricht-Bilder und Overlays für die sichere Zone sind so konzipiert, dass sie auf Geräten aller Größen gut funktionieren. [Download Design-Vorlagen ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

### Hochformat

| Layout | Assetgröße | Notizen |
|--- | --- | --- |
| Bild und Text | Seitenverhältnis 6:5<br> Hochauflösend 1200 x 1000 px<br> Minimum 600 x 500 px | Der Beschnitt kann an allen Seiten erfolgen, aber das Bild füllt immer die oberen 50 % des Ansichtsfensters aus |
| Nur Bild | Seitenverhältnis 3:5<br> Hochauflösend 1200 x 2000 px<br> Minimum 600 x 1000 px | Bei größeren Geräten kann es am linken und rechten Rand zu Beschneidungen kommen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Querformat

| Layout | Assetgröße | Notizen |
|--- | --- | --- |
| Bild und Text | Seitenverhältnis 10:3<br> Hochauflösend 2000 x 600px<br> Minimum 1000 x 300 px | Der Beschnitt kann an allen Seiten erfolgen, aber das Bild füllt immer die oberen 50 % des Ansichtsfensters aus |
| Nur Bild | Seitenverhältnis 5:3<br> Hochauflösend 2000 x 1200px<br> Minimum 1000 x 600 px | Bei größeren Geräten kann es am linken und rechten Rand zu Beschneidungen kommen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Safe Zone für Bildelemente

Bei der Vorschau einer In-App-Nachricht im Vollbildmodus auf der Braze-Plattform können Sie die Image Safe Zone für den Bereich der Nachricht aktivieren, der bei der Anzeige auf verschiedenen Geräten vor Beschneidung geschützt ist. Zusätzlich zum Testen der Safe Zone für Bildelemente in der Vorschau empfehlen wir Ihnen, [Ihre Nachricht wie gewohnt zu testen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/).

Vorschau einer In-App-Nachricht in Braze mit Enablement "Sichere Zone für Bilder anzeigen". Die sichere Bildzone ist ein Overlay über dem Bild, das anzeigt, welche Teile des Bildes vor dem Beschneiden geschützt sind.]({% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %})

## Größere Bildschirme

Auf einem Tablet oder einem Desktop-Browser wird eine bildschirmfüllende In-App-Nachricht in der Mitte des App-Bildschirms angezeigt, wie im folgenden Screenshot zu sehen ist.

{% tabs %}
{% tab Portrait %}

\![In-App-Nachricht im Vollbildmodus, wie sie auf einem großen Bildschirm im Hochformat erscheinen würde. Die Nachricht erscheint als großes Modal, das in der Mitte des Bildschirms sitzt.]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Landscape %}

\![In-App-Nachricht im Vollbildmodus, wie sie auf einem großen Bildschirm im Querformat erscheinen würde. Die Nachricht erscheint als großes Modal, das in der Mitte des Bildschirms sitzt.]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

