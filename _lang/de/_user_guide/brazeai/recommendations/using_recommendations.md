---
nav_title: Artikel-Empfehlungen verwenden
article_title: Artikel-Empfehlungen in Ihrem Messaging verwenden
description: "Dieser Artikel beschreibt, wie Sie Artikel-Empfehlungen in Ihrer Nachricht verwenden können."
page_order: 20
---

# Verwendung von Artikel-Empfehlungen in Ihrem Messaging

> Nachdem Ihre Empfehlung trainiert wurde, können Sie Liquid verwenden, um empfohlene Artikel in Ihren Nachrichten abzurufen und anzuzeigen. Der Schlüssel dazu ist die direkte Arbeit mit dem Objekt `product_recommendation` Liquid. Dieser Artikel behandelt das Objekt `product_recommendation` Liquid und enthält eine Anleitung, die Ihnen hilft, dieses Wissen in die Praxis umzusetzen.

{% alert tip %}
Dieser Artikel beschreibt die Syntax des Liquid-Objekts im Detail. Sie können jedoch [vorformatierte Variablen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables) mit Standardwerten über das Modal **Personalisierung hinzufügen** einfügen, das sich rechts oben in jedem Textfeld des Templates befindet.
{% endalert %}

Weitere Anleitungen zur Verwendung von KI-Artikel-Empfehlungen in Braze finden Sie in unserem [Braze-Lernkurs zur Erstellung personalisierter Erlebnisse mit KI][1]. Dieser Kurs umfasst Anwendungsfälle aus der Branche, Schritt-für-Schritt-Anleitungen und einen zusätzlichen Anwendungsfall für die Erstellung einer In-App-Nachricht mit KI-gesteuerten Empfehlungen.

## Anatomie des Empfehlungsobjekts

Das Objekt `product_recommendation` stellt die Menge der vom Modell empfohlenen Artikel dar. Es liefert Daten direkt aus dem zugehörigen Katalog, strukturiert als Array von Objekten, wobei jedes Objekt einen empfohlenen Artikel darstellt.

- **Struktur:** Auf jeden Artikel wird als `items[index]` zugegriffen, wobei der Index bei 0 (für den ersten Artikel) beginnt und für nachfolgende Artikel erhöht wird.
- **Katalogfelder:** Jeder Artikel im Array enthält Schlüssel-Wert-Paare, die den Feldern (Spalten) im Katalog entsprechen. Gängige Katalogfelder für Produktempfehlungen sind zum Beispiel:
   - `name` oder `title`
   - `price`
   - `image_url`

## Liquid-Tags

Das Objekt `product_recommendation` enthält dynamisch generierte Produktempfehlungen. Um auf diese in Liquid zuzugreifen, müssen Sie die Daten zunächst einer Variablen zuweisen, bevor Sie sie in Ihrer Nachricht verwenden.

### Zuweisung von Empfehlungsdaten

Beginnen Sie immer mit dem Tag assign, um die Daten von `product_recommendation` abzurufen und in einer Variablen zu speichern.

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
```

{% endraw %}

- `RECOMMENDATION_NAME`: Ersetzen Sie dies durch den Namen der KI-Empfehlung, die Sie in Braze erstellt haben.
- `items`: Die Variable, die das Array der empfohlenen Artikel speichert.

### Zugriff auf einzelne Artikel

Nachdem die Empfehlungsdaten zugewiesen wurden, können Sie bestimmte Artikel und ihre Felder mithilfe der Array-Indizierung und der Punktnotation referenzieren:

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].name }} for {{ items[0].price }}
```

{% endraw %}

Um mehrere Artikel aufzunehmen, referenzieren Sie jeden Artikel einzeln über seinen Index. `.name` und `.price` ziehen das entsprechende Feld aus dem Katalog. 

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```

{% endraw %}

KI-Empfehlungen geben mehrere Produkte als Array zurück, wobei `items[0]` der erste Artikel ist, `items[1]` der zweite und so weiter. Wenn eine Empfehlung nur einen Artikel liefert, führt der Versuch, `items[1]` zu referenzieren, zu einem leeren Feld.

## Bilder hinzufügen

Wenn der Katalog, den Ihre Empfehlung verwendet, Bildlinks enthält, können Sie diese Bilder in Ihrer Nachricht referenzieren. 

{% tabs %}

{% tab Drag-and-Drop%}
In Composern mit Bildfeldern fügen Sie das folgende Liquid zu dem entsprechenden Feld im Composer hinzu:

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].IMAGE_URL_FIELD }}
```

{% endraw %}

Für den Drag-and-Drop-Editor für E-Mails:

1. Fügen Sie einen Bildblock zu Ihrer E-Mail hinzu.
2. Wählen Sie den Bildblock aus (nicht den Button **Durchsuchen** ), um das Panel mit **den Eigenschaften des Bildes** zu öffnen.
3. Schalten Sie **Bild mit Liquid** ein. 
4. Fügen Sie das Liquid Snippet in das Feld **Dynamische URL** ein.

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].IMAGE_URL_FIELD }}
```

{% endraw %}

![Panel für Bildeigenschaften im Drag-and-Drop-Editor]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:60%"}

{:start="5"}

5. Um ein Platzhalterbild in Ihre Vorschau- und Test-E-Mails einzufügen, klicken Sie auf **Bild auswählen**, um ein Platzhalterbild aus der Bibliothek hinzuzufügen, oder geben Sie eine URL ein, unter der Ihr Bild gehostet wird.

{% endtab %}

{% tab HTML %}

Bei HTML-Bildern, die referenziert werden, setzen Sie das Attribut image `src` auf das Feld image URL im Katalog. Möglicherweise möchten Sie ein anderes Feld, z. B. den Namen oder die Beschreibung eines Produkts, als Alt-Text verwenden.

{% raw %}

```html
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
<img src="{{ items[0].IMAGE_URL_FIELD }}" alt="{{ items[0].name }}">
```

{% endraw %}

{% endtab %}

{% endtabs %}

-  Ersetzen Sie `MY_RECOMMENDATION_NAME` durch den Namen Ihrer Empfehlung
- Ersetzen Sie `IMAGE_URL_FIELD` durch den Namen des Feldes in Ihrem Katalog, das Bild-URLs enthält.


## Anleitung: E-Mail für den Warenkorb-Abbruch erstellen

In diesem Tutorial lernen Sie, wie Sie mit Hilfe der Braze AI Artikel-Empfehlungen eine dynamische E-Mail erstellen, die Nutzern:innen Produkte auf der Grundlage ihrer Vorlieben oder ihres Verhaltens empfiehlt. 

Nehmen wir an, Sie sind ein Marketer bei "Flash & Thread", einem Online-Kleiderhändler. Sie möchten Kunden, die Artikel in ihrem Warenkorb liegen gelassen haben, wieder engagieren und zusätzliche Produkte verkaufen. Ihr Ziel ist es, eine E-Mail zu erstellen, in der die verlassenen Artikel und personalisierte Empfehlungen angezeigt werden.

### Schritt 1: Bereiten Sie Ihren Katalog vor

Ihre Empfehlung wird Artikel aus einem Katalog ziehen. Folgen Sie den Schritten zur Erstellung eines Katalogs. Stellen Sie sicher, dass Ihr Katalog diese Felder enthält:

| Feld | Datentyp | Beschreibung |
| --- | --- | --- |
| id | String | Ein eindeutiger Bezeichner für jeden Artikel in Ihrem Katalog |
| Name | String | Der Name des Produkts, z.B. "Gestreifter Strickpullover". |
| Preis | Zahl | Der Preis des Produkts, z.B. "49.99". |
| image_url | String | Eine URL, die auf das Bild des Produkts verweist. Muss HTTPS-gesichert sein. Wenn Ihre Bilder in der Bibliothek gehostet werden, bewegen Sie den Mauszeiger über ein Asset, um dessen URL zu kopieren. |
| Kategorie | String | Die Produktkategorie, wie "Pullover" oder "Accessoires". |
| Farbe | String | Eine beschreibende Farbe für das Produkt, z.B. "Navy/Grau". |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


#### Beispielkatalog

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table class="tg">
  <tr>
    <th>id</th>
    <th>Name</th>
    <th>Preis</th>
    <th>image_url</th>
    <th>Kategorie</th>
    <th>Farbe</th>
  </tr>
  <tr>
    <td>1001</td>
    <td>Gestreifter Strickpullover</td>
    <td>49.99</td>
    <td>https://{{media_library}}/images/67a41294f5eac400685ce908/original.png?1738805908</td>
    <td>Pullover</td>
    <td>Marineblau/Grau</td>
  </tr>
  <tr>
    <td>1002</td>
    <td>Angepasste Yacht Club Schuhe</td>
    <td>79.99</td>
    <td>https://{{media_library}}/images/67a4136fe5a7660068bbe046/original.png?1738806127</td>
    <td>Schuhe</td>
    <td>Marine</td>
  </tr>
  <tr>
    <td>1003</td>
    <td>Zurück zur Arbeit Schuhe</td>
    <td>89.99</td>
    <td>https://{{media_library}}/images/67a41370f542c1006798c26e/original.png?1738806128</td>
    <td>Schuhe</td>
    <td>Rosa/Gold</td>
  </tr>
  <tr>
    <td>1004</td>
    <td>Ende des Sommers Hut</td>
    <td>29.99</td>
    <td>https://{{media_library}}/images/67a4136fbf6f620068511b67/original.png?1738806127</td>
    <td>Zubehör</td>
    <td>Weiß Floral</td>
  </tr>
</table>


### Schritt 2: Richten Sie Ihre Empfehlung ein

1. Wählen Sie in Ihrem Katalog die Option **Empfehlung erstellen**.
2. Folgen Sie den Schritten für [Erstellen einer KI-Artikel-Empfehlung][3]. 
3. Wählen Sie für den Empfehlungstyp **KI Personalisiert** aus.
4. Verwenden Sie den Katalog, den Sie gerade erstellt haben, um die Empfehlung zu trainieren. Das kann einige Zeit dauern - Sie erhalten eine E-Mail, wenn das Training abgeschlossen ist.

### Schritt 3: Eine E-Mail erstellen

Wenn die Empfehlung trainiert ist, können Sie sie in Ihrem Messaging verwenden.

1. Erstellen Sie eine E-Mail mit dem Drag-and-Drop-Editor.
2. Fügen Sie in den Nachrichtentext einen Bildblock ein, wenn Sie eine Empfehlung aus dem Katalog ziehen möchten. 
3. Wählen Sie den Bildblock aus und aktivieren Sie **Bild mit Liquid** im Panel **Eigenschaften von Bild**. 
4. Fügen Sie dieses Liquid Snippet in das Feld Dynamische URL ein.


{% raw %}

```liquid
{% assign items = {{product_recommendation.${abandoned_cart}}} %}
{{ items[0].image_url }}
```

{% endraw %}

{: start="5"}

5. Fügen Sie unter dem Bild einen Absatzblock hinzu. Hier fügen Sie den Namen des Produkts und alle weiteren Details hinzu. 
6. Fügen Sie das folgende Liquid-Snippet in den Block ein. Dies zieht den Namen, die Kategorie, die Farbe und den Preis der ersten Empfehlung aus dem Katalog und fügt sie als separate Zeilen hinzu. 

{% raw %}

```liquid
{% assign items = {{product_recommendation.${abandoned_cart}}} %}
{{ items[0].name }}
{{ items[0].category }}
{{ items[0].color }}
${{ items[0].price }}
```

{% endraw %}

{: start="7"}

7. Ersetzen Sie bei beiden Snippets `abandoned_cart` durch den Namen Ihrer Empfehlung in Braze.
8. Vergewissern Sie sich, dass die Feldnamen der Artikel (`{{ items[0].field_name }}`) mit den Spaltennamen in Ihrem Katalog übereinstimmen.
9. Erhöhen Sie das Feld jedes Mal um eins, wenn Sie den Block wiederholen, um den nächsten empfohlenen Artikel aus dem Katalog zu holen. Zum Beispiel beginnt das Array mit `{{ items[0].name }}`, der nächste Artikel wäre also `{{ items[1].name }}`.

### Schritt 4: Vorschau auf Ihre Nachricht

Um zu sehen, wie Ihre Nachricht für einen echten Nutzer:innen aussieht:

1. Gehen Sie in Ihrem Editor auf den Tab **Vorschau & Test**.
2. Wählen Sie **Zufällige Nutzer**:in aus der Dropdown-Liste.
3. Wählen Sie **Zufälligen Nutzer:innen auswählen**, um einen Nutzer:innen aus Ihrer Zielgruppe auszuwählen und eine Vorschau zu erhalten, wie die E-Mail mit dessen Daten aussehen wird.

Die Vorschau rendert Liquid vollständig, einschließlich der KI-Empfehlungen, sofern der ausgewählte Nutzer:innen über die erforderlichen Attribute oder Ereignisdaten verfügt, die mit der Empfehlung verknüpft sind.

Wenn die Empfehlung nicht in der Vorschau angezeigt wird, überprüfen Sie Folgendes:

- Der Nutzer:in hat mit relevanten Produkten oder Ereignissen interagiert, die das Empfehlungsmodell trainiert haben
- Die Empfehlung selbst wurde erfolgreich trainiert
- Der Liquid Code referenziert korrekt die richtige Empfehlung und die richtigen Felder



[1]: https://learning.braze.com/ai-item-recommendations-use-case/1996254
[2]: {% image_buster /assets/img/image_with_liquid.png %}
[3]: {{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations#creating-an-ai-item-recommendation