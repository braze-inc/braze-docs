---
nav_title: Kataloge verwenden
article_title: Kataloge verwenden
page_order: 1.5
description: "In diesem Referenzartikel erfahren Sie, wie Sie Kataloge verwenden, um Nicht-Nutzerdaten in Ihren Braze Kampagnen über Liquid zu referenzieren."
---

# Kataloge verwenden

> Nachdem Sie einen Katalog erstellt haben, können Sie in Ihren Braze-Kampagnen über [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) auf Nicht-Benutzerdaten verweisen. Sie können Kataloge in allen Ihren Nachrichtenkanälen verwenden, auch überall dort, wo Liquid im Drag-and-Drop-Editor unterstützt wird.

## Kataloge in einer Nachricht verwenden

### Schritt 1: Personalisierungsart hinzufügen {#step-one-personalization}

Klicken Sie im Message Composer Ihrer Wahl auf das Plus-Symbol <i class="fas fa-plus-circle"></i>, um das Modal **"Personalisierung hinzufügen"** zu öffnen, und wählen Sie als **Personalisierungstyp**" **Katalogartikel** ". Wählen Sie dann Ihren **Katalognamen**. In unserem vorherigen Beispiel wählen wir den Katalog "Spiele".

\![]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

Wir können sofort die folgende Liquid-Vorschau sehen:

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### Schritt 2: Katalogartikel auswählen

Als Nächstes fügen Sie Ihre Katalogartikel hinzu! Wählen Sie über die Dropdown-Liste die Katalogartikel und die anzuzeigenden Informationen aus. Diese Informationen entsprechen den Spalten in Ihrer hochgeladenen CSV-Datei, die Sie zur Erstellung Ihres Katalogs verwendet haben.

Um beispielsweise den Titel und den Preis unseres Tales-Spiels zu referenzieren, könnten wir die `id` für Tales (1234) als Katalogobjekt auswählen und `title` und `price` für die angezeigten Informationen anfordern.

{% raw %}
```liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

Dies bedeutet Folgendes:

> Holen Sie sich Tales für nur 7.49!

## Kataloge exportieren

Es gibt zwei Möglichkeiten, wie Sie Kataloge aus dem Dashboard exportieren können: 

- Bewegen Sie den Mauszeiger über die Katalogzeile im Bereich **Kataloge**. Wählen Sie dann den Button **Katalog exportieren** aus.
- Wählen Sie Ihren Katalog aus. Wählen Sie dann den Button **Katalog exportieren** auf dem Tab **Vorschau** des Katalogs aus.

Sie erhalten eine E-Mail zum Herunterladen der CSV-Datei, nachdem Sie den Export gestartet haben. Sie haben bis zu vier Stunden Zeit, diese Datei abzurufen.

## Zusätzliche Anwendungsfälle

### Mehrere Artikel

Sie sind nicht auf einen Artikel in einer einzigen Nachricht beschränkt. Sie können das Modal **Personalisierung hinzufügen** verwenden, um bis zu drei Katalogartikel auf einmal hinzuzufügen. Wenn Sie Ihrer Nachricht weitere Elemente hinzufügen möchten, wählen Sie im Nachrichten-Composer die Option **Personalisierung hinzufügen** und wählen Sie die zusätzlichen Katalogelemente und Informationen aus, die angezeigt werden sollen.

Sehen Sie sich dieses Beispiel an, in dem wir die `id` von drei Spielen, Tales, Teslagrad und Acaratus, für **Katalogartikel** hinzufügen und `title` für **Anzuzeigende Informationen** auswählen.

\![]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Wir können unsere Nachricht weiter personalisieren, indem wir etwas Text um unser Liquid herum hinzufügen:

{% raw %}
```liquid
Get the ultimate trio {% catalog_items games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

Das Ergebnis sieht folgendermaßen aus:

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
Schauen Sie sich die [Auswahlmöglichkeiten]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) an, um Datengruppen für personalisierte Nachrichten zu erstellen!
{% endalert %}

### Liquid `if`-Anweisungen verwenden

Sie können Katalogartikel verwenden, um bedingte Anweisungen zu erstellen. Sie können zum Beispiel eine bestimmte Nachricht triggern, die angezeigt wird, wenn ein bestimmter Artikel in Ihrer Kampagne ausgewählt wird.

Dazu verwenden Sie eine Liquid `if` Anweisung, wie in diesem Beispiel:

{% raw %}
```liquid
{% catalog_selection_items item-list selections %} 
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters. 
{% elsif items[0].venue_name.size < 10 %}
Message if the venue name's size is less than 10 characters. 
{% else %} 
{% abort_message(no venue_name) %} 
{% endif %}
```
{% endraw %}

In diesem Beispiel werden unterschiedliche Nachrichten angezeigt, wenn das angepasste Attribut `venue_name` mehr als 10 Zeichen oder weniger als 10 Zeichen hat. Wenn `venue_name` auf `blank` steht, wird nichts angezeigt. 

Beachten Sie, dass Sie die Katalogliste und ggf. die Auswahl deklarieren müssen, bevor Sie `if` Anweisungen verwenden. Im Beispiel ist `item-list` die Katalogliste und `selections` ist der Name der Auswahl.

### Bilder verwenden {#using-images}

Sie können auch Bilder aus dem Katalog referenzieren, um sie in Ihrem Messaging zu verwenden. Verwenden Sie dazu den Tag `catalogs` und das Objekt `item` im Feld Liquid für Bilder.

Wenn Sie z.B. die `image_link` aus unserem Spielekatalog zu unserer Werbebotschaft für Tales hinzufügen möchten, wählen Sie `id` für das Feld **Katalogartikel** und `image_link` für das Feld **Anzuzeigende Informationen**. Dadurch werden die folgenden Liquid-Tags zu unserem Bildfeld hinzugefügt:

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

\![Content-Card-Komponist mit dem im Bildfeld verwendeten Liquid-Tag des Katalogs.]({% image_buster /assets/img_archive/catalog_image_link1.png %})

So sieht das aus, wenn das Liquid gerendert wird:

\![Beispiel Content-Card mit gerenderten Liquid-Tags.]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

### Template für Katalogartikel

Sie können auch Templates verwenden, um Katalogartikel auf der Grundlage angepasster Attribute dynamisch abzurufen. Nehmen wir zum Beispiel an, ein Benutzer hat das benutzerdefinierte Attribut `wishlist`, das ein Array von Spiele-IDs aus Ihrem Katalog enthält.

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
JSON-Objekte in Katalogen werden nur über die API aufgenommen. Sie können ein JSON-Objekt nicht mit einer CSV-Datei hochladen.
{% endalert %}

Mit Liquid-Templates können Sie die IDs der Wunschlisten dynamisch herausziehen und sie dann in Ihrer Nachricht verwenden. Dazu weisen Sie Ihrem angepassten Attribut [eine Variable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) zu und verwenden dann das Modal **Personalisierung hinzufügen**, um einen bestimmten Artikel aus dem Array zu ziehen. Variablen, die als ID eines Katalogartikels referenziert werden, müssen in geschweifte Klammern eingeschlossen werden, um richtig referenziert zu werden, z.B. `{{result}}`.

{% alert tip %}
Denken Sie daran, dass Arrays bei `0` beginnen, nicht bei `1`.
{% endalert %}

Um einen Benutzer zum Beispiel darüber zu informieren, dass Tales (ein Artikel aus unserem Katalog, den er sich gewünscht hat) im Angebot ist, können wir unserem Message Composer Folgendes hinzufügen:

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now, for just {{ items[0].price }}!
```
{% endraw %}

Sie wird wie folgt angezeigt:
> Holen Sie sich Tales jetzt, für nur 7.49!

Mit Hilfe von Templates können Sie für jede:n Nutzer:in einen anderen Katalogartikel rendern, der auf seinen angepassten Attributen, Event-Eigenschaften oder einem anderen in Templates definierbaren Feld basiert.

### Hochladen einer CSV

Sie können eine CSV-Datei mit neu hinzuzufügenden Katalogartikeln oder zu aktualisierenden Katalogartikeln hochladen. Um eine Liste von Artikeln zu löschen, können Sie eine CSV-Datei mit den IDs der Artikel hochladen, um sie zu löschen.

### Liquid verwenden

Sie können Kataloge auch manuell mit Liquid logic zusammenstellen. Beachten Sie jedoch, dass Braze, wenn Sie eine ID eingeben, die nicht existiert, trotzdem ein Artikel-Array ohne Objekte zurückgibt. Wir empfehlen Ihnen, eine Fehlerbehandlung einzubauen, wie z. B. die Überprüfung der Größe des Arrays und die Verwendung einer `if` Anweisung, um den Fall eines leeren Arrays zu berücksichtigen.

{% alert note %}
Liquid kann derzeit nicht in Katalogen verwendet werden. Wenn die Liquid-Personalisierung innerhalb einer Zelle in Ihrem Katalog aufgeführt ist, wird der dynamische Wert nicht gerendert und nur das eigentliche Liquid wird angezeigt.
{% endalert %}

#### Template für Katalogartikel einschließlich Liquid

Ähnlich wie bei [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) müssen Sie das Kennzeichen `:rerender` in einem Liquid-Tag verwenden, um den Liquid-Inhalt eines Katalogartikels darzustellen. Beachten Sie, dass das `:rerender` Flag nur eine Ebene tief ist, d. h. es gilt nicht für verschachtelte Liquid-Tag-Aufrufe.

Wenn ein Katalogeintrag Felder für Benutzerprofile enthält (innerhalb eines Liquid-Personalisierungs-Tags), müssen diese Werte in Liquid zu einem früheren Zeitpunkt in der Nachricht und vor der Schablonenerstellung definiert werden, damit das Liquid ordnungsgemäß dargestellt werden kann. Wenn das Flag `:rerender` nicht angegeben wird, wird der rohe Liquid-Inhalt wiedergegeben.

Wenn zum Beispiel ein Katalog mit dem Namen "Messages" einen Artikel mit diesem Liquid enthält:

\![]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

Um den folgenden Liquid-Inhalt wiederzugeben:

{% raw %}
```liquid
Hi ${first_name}

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
Catalog Liquid-Tags können innerhalb von Katalogen nicht rekursiv verwendet werden.
{% endalert %}


[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}
