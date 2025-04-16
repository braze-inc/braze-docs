---
nav_title: Kreative Details
article_title: Kreative Details für Inhaltskarten
page_order: 1
description: "Dieser Artikel befasst sich mit kreativen Details wie Empfehlungen für die Bildgröße und das Verhalten bei der Entlassung aus den drei Content-Card-Standardtypen."
channel:
  - content cards
tool: Media

---

# Kreative Details für Content-Cards

> Die Anpassung der Content Cards und des Feeds, in dem sie sich befinden, kann nicht während der Kampagnenerstellung erfolgen - Sie müssen mit Ihren Technikern und Entwicklern zusammenarbeiten, um Ihre Karten zu erstellen und anzupassen. Für technische Details besuchen Sie unsere [Entwicklerdokumentation][7].

## Content-Card-Typen

{% tabs %}
{% tab Classic %}

Die klassische Karte eignet sich hervorragend für Standardnachrichten und Benachrichtigungen oder sogar für die visuelle Kategorisierung von Nachrichten mit Symbolen. Das Bild ist optional, aber es muss im Verhältnis 1:1 sein.

![Bild einer klassischen Karte mit empfohlenen Details und einem klassischen Kartenbeispiel]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}

| Kartenkapazität | Details |
| --- | ---|
| Header-Text | 18px; Fettgedruckt <br> Eine Textzeile ist ideal. <br> Hier können Sie Liquid verwenden, um Ihre Nachricht zu personalisieren. |
| Nachrichtentext | 13px; Regular Weight <br> Zwei bis vier Zeilen Text sind ideal. <br> Hier können Sie Liquid verwenden, um Ihre Nachricht zu personalisieren. |
| Link-Text | Optional. <br> 13 px <br> Link zu einer Webseite oder Deep Link innerhalb Ihrer App. |
| Bild | Optional. <br> Das Verhältnis muss 1:1 sein. <br> Wir empfehlen eine Bildqualität von 60 x 60 px. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Bild mit Bildunterschrift %}

Die Karte mit Bildunterschrift ist eine großartige Möglichkeit, um wichtige Inhalte, wie z. B. einen großen Verkauf oder eine neue App-Funktion, zu präsentieren und die Aufmerksamkeit darauf zu lenken.

![Abbildung einer Bildunterschriftenkarte mit empfohlenen Details und ein Beispiel für eine Bildunterschriftenkarte]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}

| Kartenkapazität | Details |
| --- | ---|
| Header-Text | 18px; Fettgedruckt <br> Eine Textzeile ist ideal. <br> Hier können Sie Liquid verwenden, um Ihre Nachricht zu personalisieren. |
| Nachrichtentext | 13px; Regular Weight <br> Zwei bis vier Zeilen Text sind ideal. <br> Hier können Sie Liquid verwenden, um Ihre Nachricht zu personalisieren. |
| Link-Text | Optional. <br> 13 px <br> Link zu einer Webseite oder Deep Link innerhalb Ihrer App. |
| Bild | Vorgeschlagen wird ein Verhältnis von 4:3. <br> 600 px Mindestbreite.  <br> Unterstützt hochauflösendes PNG, JPEG und GIF. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Banner %}

Wenn Sie etwas Ausgefallenes wollen, ist die Bannerkarte genau das Richtige für Sie. Diese wird vollständig an Ihre Wünsche angepasst. Erstellen Sie Ihre Inhalte einfach an anderer Stelle und laden Sie sie hoch, um eine wunderschöne Karte zu gestalten, die ganz Ihnen gehört.

![Bild eines Banners mit empfohlenen Details und ein Bannerbeispiel]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}

| Kartenkapazität | Details |
| --- | ---|
| Verknüpfte Karte | Optional. <br> 13 px <br> Das Klickverhalten verweist auf eine Webseite oder einen Deep Link innerhalb Ihrer App. |
| Bild | Jedes Seitenverhältnis wird unterstützt. <br> 600 px Mindestbreite.  <br> Unterstützt hochauflösendes PNG, JPEG und GIF. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Globale kreative Details {#general}

Content Cards verfügen von Anfang an über eine großartige Funktionalität. Derzeit ist die Gestaltung von Karten in Ihrem Braze-Konto noch nicht möglich, aber Sie können Ihre Content-Card nach Typ und Content-Card-Feed während der Integration gestalten. Weitere Informationen finden Sie unter [Anpassen von Inhaltskarten][4] ].

### Ausblendungsverhalten

Um eine Karte abzulegen, kann der Benutzer sie auf dem Handy entweder wegwischen oder die Funktion `close X` verwenden, wie im folgenden Screenshot gezeigt. `x` wird nur für das Web-SDK angezeigt, wenn Sie den Mauszeiger darüber bewegen.

![Bild, das das Verhalten beim Durchziehen oder Schließen einer Karte zeigt][5]

Wenn ein Benutzer alle seine Karten verworfen hat oder Sie keine neuen Aktualisierungen veröffentlicht haben, sieht der Feed des Benutzers in der Regel etwa so aus:

![Bild eines leeren Content-Card-Feeds][6]{: style="max-width:45%"}

{% alert tip %}
Sorgen Sie dafür, dass Content-Cards relevant bleiben, indem Sie sie ausblenden, wenn ein:e Nutzer:in entsprechende Aktionen durchführt. Legen Sie z.B. fest, dass Content-Cards für Werbezwecke ausgeblendet werden, sobald Nutzer:innen einen Kauf tätigen, damit sie nicht weiterhin ein Angebot für etwas sehen, das sie bereits gekauft haben.
{% endalert %}

### GIFs in Inhaltskarten verwenden

| Inhaltskarten für Android | Inhaltskarten für iOS | Content-Cards für das Internet |
| --- | --- |---|
| Das Android-SDK bietet standardmäßig keine Unterstützung für animierte GIFs. Weitere Einzelheiten zur Aktivierung der GIF-Unterstützung finden Sie unter [GIFs]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android). | Das Swift-SDK bietet standardmäßig keine Unterstützung für animierte GIFs. Weitere Einzelheiten zur Aktivierung der GIF-Unterstützung finden Sie in der [Anleitung zur GIF-Unterstützung](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support). | Die GIF-Unterstützung ist standardmäßig in der Web SDK-Integration enthalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<br><br>

[1]: {% image_buster /assets/img/content_card_classic.png %}
[2]: {% image_buster /assets/img/content_card_captioned.png %}
[3]: {% image_buster /assets/img/content_card_banner.png %}
[4]: {{site.baseurl}}/developer_guide/customization_guides/content_cards
[5]: {% image_buster /assets/img/dismissal-cc.png %}
[6]: {% image_buster /assets/img/empty-cc.png %}
[7]: {{site.baseurl}}/developer_guide/getting_started/customization_overview