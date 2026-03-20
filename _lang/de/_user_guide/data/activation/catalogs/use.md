---
nav_title: Verwendung von Katalogen
article_title: Kataloge verwenden
page_order: 1.5
description: "In diesem Referenzartikel erfahren Sie, wie Sie Kataloge verwenden, um Nicht-Nutzerdaten in Ihren Braze-Kampagnen über Liquid zu referenzieren."
---

# Verwendung von Katalogen

> Nachdem Sie einen Katalog erstellt haben, können Sie in Ihren Braze-Kampagnen über [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) auf Nicht-Nutzerdaten verweisen. Sie können Kataloge in allen Ihren Messaging-Kanälen verwenden, auch überall dort, wo Liquid im Drag-and-Drop-Editor unterstützt wird.

## Kataloge in einer Nachricht verwenden

### 1. Schritt: Personalisierungsart hinzufügen {#step-one-personalization}

Wählen Sie im Nachrichten-Editor Ihrer Wahl das <i class="fas fa-plus-circle"></i> Plus-Symbol, um das Modal **Personalisierung hinzufügen** zu öffnen, und wählen Sie **Katalogartikel** als **Personalisierungstyp** aus. Wählen Sie anschließend den Namen Ihres Katalogs aus. In unserem vorherigen Beispiel wählen wir den Katalog „Games".

![]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

Wir können sofort die folgende Liquid-Vorschau sehen:

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### 2. Schritt: Katalogartikel auswählen

Als Nächstes fügen Sie Ihre Katalogartikel hinzu! Wählen Sie über die Dropdown-Liste die Katalogartikel und die anzuzeigenden Informationen aus. Diese Informationen entsprechen den Spalten in Ihrer hochgeladenen CSV-Datei, die Sie zur Erstellung Ihres Katalogs verwendet haben.

Um beispielsweise den Titel und den Preis unseres Tales-Spiels zu referenzieren, könnten wir die `id` für Tales (1234) als Katalogartikel auswählen und `title` und `price` für die angezeigten Informationen anfordern.

{% raw %}
```liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

Dies wird folgendermaßen gerendert:

> Get Tales for just 7.49!

## Kataloge exportieren

Es gibt zwei Möglichkeiten, wie Sie Kataloge aus dem Dashboard exportieren können: 

- Bewegen Sie den Mauszeiger über die Katalogzeile im Abschnitt **Kataloge**. Wählen Sie dann den Button **Katalog exportieren** aus.
- Wählen Sie Ihren Katalog aus. Wählen Sie dann den Button **Katalog exportieren** auf dem Tab **Vorschau** des Katalogs aus.

Sie erhalten eine E-Mail zum Herunterladen der CSV-Datei, nachdem Sie den Export gestartet haben. Sie haben bis zu vier Stunden Zeit, diese Datei abzurufen.

## Zusätzliche Anwendungsfälle

### Mehrere Artikel

Sie sind nicht auf einen Artikel pro Nachricht beschränkt. Verwenden Sie das Modal **Personalisierung hinzufügen**, um bis zu drei Katalogartikel gleichzeitig hinzuzufügen. Um weitere hinzuzufügen, wählen Sie im Editor erneut **Personalisierung hinzufügen** und wählen Sie zusätzliche Katalogartikel und anzuzeigende Informationen aus.

Sehen Sie sich dieses Beispiel an, in dem wir die `id` von drei Spielen – Tales, Teslagrad und Acaratus – für **Katalogartikel** hinzufügen und `title` für **Anzuzeigende Informationen** auswählen.

![]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Wir können unsere Nachricht weiter personalisieren, indem wir etwas Text um unser Liquid herum hinzufügen:

{% raw %}
```liquid
Get the ultimate trio {% catalog_items Games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

Das Ergebnis sieht folgendermaßen aus:

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
Check out [selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) to create groups of data for more personalized messaging!
{% endalert %}

### Using Liquid `if` statements

You can use catalog items to create conditional statements. For example, you can trigger a certain message to display when a specific item is selected in your campaign. You must declare the catalog (and, if applicable, the selection) before referencing `items` in an `if` statement.

#### With catalog items

{% raw %}
```liquid
{% catalog_items Games 1234 %}
{% if items[0].on_sale == true %}
  {{ items[0].title }} is on sale! Get it for {{ items[0].price }}.
{% else %}
  Check out {{ items[0].title }} at full price.
{% endif %}
```
{% endraw %}

In diesem Beispiel ruft der `catalog_items`-Tag den Artikel `1234` aus dem `Games`-Katalog ab, und die `if`-Anweisung prüft das Feld `on_sale`, um unterschiedliche Nachrichten anzuzeigen.

#### Mit Katalogauswahlen

{% raw %}
```liquid
{% catalog_selection_items item-list selections %} 
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters. 
{% elsif items[0].venue_name.size <= 10 %}
Message if the venue name's size is 10 characters or fewer. 
{% else %} 
{% abort_message('no venue_name') %} 
{% endif %}
```
{% endraw %}

In diesem Beispiel werden je nachdem, ob das Feld `venue_name` mehr oder weniger als 10 Zeichen hat, unterschiedliche Nachrichten angezeigt. Wenn `venue_name` leer ist, wird die Nachricht abgebrochen.

{% alert tip %}
Um Liquid-Syntaxfehler zu vermeiden, wählen Sie den **+** Plus-Button im Nachrichten-Editor, um Katalog-Liquid-Tags automatisch einzufügen.
{% endalert %}

### Bilder verwenden {#using-images}

Sie können auch Bilder aus dem Katalog referenzieren, um sie in Ihrem Messaging zu verwenden. Verwenden Sie dazu den `catalogs`-Tag und das `item`-Objekt im Liquid-Feld für Bilder.

Wenn Sie z. B. den `image_link` aus unserem Games-Katalog zu unserer Aktionsnachricht für Tales hinzufügen möchten, wählen Sie die `id` für das Feld **Katalogartikel** und `image_link` für das Feld **Anzuzeigende Informationen**. Dadurch werden die folgenden Liquid-Tags zu unserem Bildfeld hinzugefügt:

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![Content-Card-Editor mit dem Katalog-Liquid-Tag, der im Bildfeld verwendet wird.]({% image_buster /assets/img_archive/catalog_image_link1.png %})

So sieht das aus, wenn das Liquid gerendert wird:

![Beispiel einer Content-Card mit gerenderten Katalog-Liquid-Tags.]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

### Templates für Katalogartikel

Sie können auch Templates verwenden, um Katalogartikel auf der Grundlage angepasster Attribute dynamisch abzurufen. Nehmen wir zum Beispiel an, eine Nutzer:in hat das angepasste Attribut `wishlist`, das ein Array von Spiele-IDs aus Ihrem Katalog enthält.

```json
{
    "attributes": [
        {
            "external_id": "user_id",
            "wishlist": ["1234", "1235"]
        }
    ]
}
```

{% alert note %}
JSON-Objekte in Katalogen werden nur über die API aufgenommen. Sie können ein JSON-Objekt nicht über eine CSV-Datei hochladen.
{% endalert %}

Mit Liquid-Templates können Sie die Wunschlisten-IDs dynamisch abrufen und sie dann in Ihrer Nachricht verwenden. Dazu weisen Sie Ihrem angepassten Attribut [eine Variable zu]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) und verwenden dann das Modal **Personalisierung hinzufügen**, um einen bestimmten Artikel aus dem Array abzurufen. Variablen, die als ID eines Katalogartikels referenziert werden, müssen in geschweifte Klammern eingeschlossen werden, um korrekt referenziert zu werden, z. B. `{{result}}`.

{% alert tip %}
Denken Sie daran, dass Arrays bei `0` beginnen, nicht bei `1`.
{% endalert %}

Um eine Nutzer:in zum Beispiel darüber zu informieren, dass Tales (ein Artikel aus unserem Katalog, den sie sich gewünscht hat) im Angebot ist, können wir unserem Nachrichten-Editor Folgendes hinzufügen:

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now for {{ items[0].price }}!
```
{% endraw %}

Dies wird wie folgt angezeigt:
> Get Tales now for just 7.49!

Mit Templates können Sie für jede Nutzer:in einen anderen Katalogartikel rendern, der auf den individuellen angepassten Attributen, Event-Eigenschaften oder einem anderen in Templates verwendbaren Feld basiert.

### Hochladen einer CSV-Datei

Sie können eine CSV-Datei mit neuen Katalogartikeln zum Hinzufügen oder mit zu aktualisierenden Katalogartikeln hochladen. Um eine Liste von Artikeln zu löschen, können Sie eine CSV-Datei mit den Artikel-IDs hochladen, um sie zu löschen.

### Liquid verwenden

Sie können Kataloge auch manuell mit Liquid-Logik zusammenstellen. Beachten Sie jedoch, dass Braze, wenn Sie eine ID eingeben, die nicht existiert, trotzdem ein Artikel-Array ohne Objekte zurückgibt. Wir empfehlen Ihnen, eine Fehlerbehandlung einzubauen, wie z. B. die Überprüfung der Größe des Arrays und die Verwendung einer `if`-Anweisung, um den Fall eines leeren Arrays zu berücksichtigen.

#### Templates für Katalogartikel einschließlich Liquid

Ähnlich wie bei [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) müssen Sie das `:rerender`-Flag in einem Liquid-Tag verwenden, um den Liquid-Inhalt eines Katalogartikels zu rendern. Beachten Sie, dass das `:rerender`-Flag nur eine Ebene tief wirkt, d. h. es gilt nicht für verschachtelte Liquid-Tag-Aufrufe.

Wenn ein Katalogartikel Nutzerprofil-Felder enthält (innerhalb eines Liquid-Personalisierungs-Tags), müssen diese Werte in Liquid zu einem früheren Zeitpunkt in der Nachricht und vor dem Templating definiert werden, damit das Liquid ordnungsgemäß gerendert werden kann. Wenn das `:rerender`-Flag nicht angegeben wird, wird der rohe Liquid-Inhalt ausgegeben.

Wenn zum Beispiel ein Katalog mit dem Namen „Messages" einen Artikel mit diesem Liquid enthält:

![]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

Um den folgenden Liquid-Inhalt zu rendern:

{% raw %}
```liquid
Hi ${first_name},

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

Dies wird wie folgt angezeigt:

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
Katalog-Liquid-Tags können innerhalb von Katalogen nicht rekursiv verwendet werden.
{% endalert %}


[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}