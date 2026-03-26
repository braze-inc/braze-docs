---
nav_title: Empfehlungen verwenden
article_title: Verwenden Sie Artikelempfehlungen in Ihrem Messaging
description: "Dieser Artikel beschreibt, wie Sie Artikelempfehlungen in Ihrer Nachricht verwenden können."
page_order: 1.2
---

# Verwenden Sie Artikelempfehlungen im Messaging

> Nachdem Ihre Empfehlung trainiert ist, können Sie Liquid verwenden, um empfohlene Artikel in Ihren Nachrichten abzurufen und anzuzeigen, indem Sie direkt mit dem Liquid-Objekt `product_recommendation` arbeiten.

{% alert tip %}
Eine Schritt-für-Schritt-Anleitung finden Sie in unserem Braze-Lernkurs: [Personalisierte Erlebnisse mit KI gestalten](https://learning.braze.com/ai-item-recommendations-use-case/1996254).
{% endalert %}

## Voraussetzungen

Bevor Sie Empfehlungen in Ihrem Messaging verwenden können, müssen Sie [ein Empfehlungssystem erstellen und trainieren]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/). Das Training kann zwischen 10 Minuten und 36 Stunden dauern&#8212;Sie erhalten eine E-Mail, wenn es abgeschlossen ist oder wenn ein Fehler aufgetreten ist.

## Verwendung von Empfehlungen in Ihrem Messaging

### 1. Schritt: Liquid-Code hinzufügen

Nachdem Ihre Empfehlung trainiert wurde, können Sie Ihre Nachrichten mit Liquid personalisieren, um die beliebtesten Produkte aus diesem Katalog einzufügen.

{% tabs local %}
{% tab pre-formatted code %}
![Modal „Personalisierung hinzufügen" mit Artikelempfehlung als Personalisierungstyp.]({% image_buster /assets/img/add_personalization.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

Sie können Liquid über den Abschnitt **Personalisierung hinzufügen** in Ihrem Nachrichten-Editor generieren:

1. Wählen Sie in jedem Nachrichten-Editor, der Personalisierung unterstützt, <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Personalisierung hinzufügen"></i> aus, um das Personalisierungsfenster zu öffnen.
2. Wählen Sie für **Personalisierungstyp** die Option **Artikelempfehlung** aus.
3. Wählen Sie unter **Name der Artikelempfehlung** die Empfehlung aus, die Sie gerade erstellt haben.
4. Geben Sie bei **Anzahl der vorhergesagten Artikel** ein, wie viele Top-Produkte eingefügt werden sollen. Sie können zum Beispiel die drei meistgekauften Artikel anzeigen.
5. Wählen Sie unter **Anzuzeigende Informationen** aus, welche Felder aus dem Katalog für jeden Artikel enthalten sein sollen. Die Werte für diese Felder werden für jeden Artikel aus dem mit dieser Empfehlung verknüpften Katalog entnommen.
6. Wählen Sie das Symbol **Kopieren** aus und fügen Sie den Liquid-Code an der gewünschten Stelle in Ihrer Nachricht ein.
{% endtab %}

{% tab custom code %}
Sie können angepassten Liquid-Code schreiben, indem Sie auf das `product_recommendation`-Objekt eines Katalogs referenzieren. Es enthält alle dynamisch generierten Produktempfehlungsdaten für diesen Katalog, strukturiert als Array von Objekten, wobei jedes Objekt einen empfohlenen Artikel darstellt.

|Spezifikation|Details|
|-------------|-------|
|**Struktur**|Auf jeden Artikel wird als `items[index]` zugegriffen, wobei der Index bei 0 (für den ersten Artikel) beginnt und für nachfolgende Artikel erhöht wird.|
|**Katalogfelder**|Jeder Artikel im Array enthält Schlüssel-Wert-Paare, die den Feldern (Spalten) im Katalog entsprechen. Gängige Katalogfelder für Produktempfehlungen sind zum Beispiel:<br>- `name` oder `title`<br>- `price`<br>- `image_url`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Verwenden Sie den Tag `assign`, um die `product_recommendation`-Daten abzurufen und einer Variablen zuzuweisen.

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
```
{% endraw %}

Ersetzen Sie Folgendes:

|Platzhalter|Beschreibung|
|-----------|-----------|
|`recommendation_name`|Der Name der KI-Empfehlung, die Sie in Braze erstellt haben.|
|`items`|Die Variable, die das Array der empfohlenen Artikel speichert.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Referenzieren Sie als Nächstes bestimmte Artikel und ihre Felder mithilfe der Array-Indizierung und der Punktnotation:

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
```
{% endraw %}

Um mehrere Artikel einzubeziehen, referenzieren Sie jeden Artikel einzeln über seinen Index. `.name` und `.price` ziehen das entsprechende Feld aus dem Katalog.

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```
{% endraw %}

KI-Empfehlungen geben mehrere Produkte als Array zurück, wobei `items[0]` der erste Artikel ist, `items[1]` der zweite und so weiter. Wenn eine Empfehlung nur einen Artikel zurückgibt, führt der Versuch, `items[1]` zu referenzieren, zu einem leeren Feld.
{% endtab %}
{% endtabs %}

### 2. Schritt: Ein Bild referenzieren (optional)

Wenn der Katalog Ihrer Empfehlung Bildlinks enthält, können Sie diese in Ihrer Nachricht referenzieren.

{% tabs %}
{% tab Drag-and-drop%}
Fügen Sie im E-Mail-Drag-and-Drop-Editor einen Bildblock zu Ihrer E-Mail hinzu und wählen Sie dann den Bildblock aus, um die **Bildeigenschaften** zu öffnen.

![Panel „Bildeigenschaften" im Drag-and-Drop-Editor]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:45%"}

Schalten Sie **Bild mit Liquid** um und fügen Sie dann Folgendes in das Feld **Dynamische URL** ein (das URL-Feld unterstützt keine Zeilenumbrüche, stellen Sie also sicher, dass der Code in einer Zeile steht):

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}{{ items[0].image_url_field }}
```
{% endraw %}

Ersetzen Sie Folgendes:

|Platzhalter|Beschreibung|
|-----------|-----------|
|`recommendation_name`|Der Name Ihrer Empfehlung.|
|`image_url_field`|Der Name des Feldes in Ihrem Katalog, das Bild-URLs enthält.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Um ein Platzhalterbild in Ihre Vorschau- und Test-E-Mails einzufügen, wählen Sie **Bild auswählen** und wählen Sie dann entweder ein Bild aus Ihrer Medienbibliothek aus oder geben Sie die URL eines Bildes von Ihrer Hosting-Website ein.
{% endtab %}

{% tab HTML %}
Setzen Sie bei HTML-Bildreferenzen das `src`-Attribut des Bildes auf das Bild-URL-Feld im Katalog. Möglicherweise möchten Sie ein anderes Feld, z. B. einen Produktnamen oder eine Beschreibung, als Alt-Text verwenden.

{% raw %}
```html
{% assign items = {{product_recommendation.${recommendation_name}}} %}
<img src="{{ items[0].image_url_field }}" alt="{{ items[0].name }}">
```
{% endraw %}

Ersetzen Sie Folgendes:

|Platzhalter|Beschreibung|
|-----------|-----------|
|`recommendation_name`|Der Name Ihrer Empfehlung.|
|`image_url_field`|Der Name des Feldes in Ihrem Katalog, das Bild-URLs enthält.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}