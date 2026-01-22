---
nav_title: KI-Empfehlungen
article_title: KI Artikel-Empfehlungen erstellen
description: "Dieser Artikel beschreibt, wie Sie eine KI-Artikelempfehlung für Katalogposten erstellen."
page_order: 1
---

# KI-Artikel-Empfehlungen erstellen

> Erfahren Sie, wie Sie ein KI-Empfehlungssystem aus Artikeln in Ihrem Katalog erstellen können.

## Über KI-Artikel-Empfehlungen

Nutzen Sie KI-Artikel-Empfehlungen, um die beliebtesten Produkte zu berechnen oder personalisierte KI-Empfehlungen für einen bestimmten [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs/) zu erstellen. Anschließend können Sie die Personalisierung nutzen, um die Produkte in Nachrichten einzufügen.

{% alert tip %}
[Personalisierte KI-Empfehlungen](#recommendation-types) funktionieren am besten bei sehr großen Inventaren und mindestens 30.000 Nutzern mit Kauf- oder Interaktionsdaten. Dies ist nur ein grober Richtwert und kann variieren. Die anderen Empfehlungstypen können mit weniger Daten arbeiten.
{% endalert %}

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## KI-Artikelempfehlungen erstellen

### Voraussetzungen

Bevor Sie beginnen, sollten Sie Folgendes beachten:

- Sie müssen mindestens einen [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs/) haben, um einen der unten beschriebenen Empfehlungstypen zu verwenden.
- Sie benötigen über Kauf- oder Ereignisdaten in Braze (benutzerdefinierte Ereignisse oder das Kaufobjekt), die einen Verweis auf eindeutige Produkt-IDs aus einem Katalog enthalten.

### Schritt 1: Eine neue Empfehlung erstellen

Sie können eine KI-Artikel-Empfehlung von jeder Stelle des Dashboards aus erstellen:

{% tabs local %}
{% tab From the navigation menu %}
1. Gehen Sie zu **Analytics** > **AI-Artikel-Empfehlung**.
2. Wählen Sie **Vorhersage erstellen** > **KI-Artikel-Empfehlung**.
{% endtab %}

{% tab From a catalog %}
Sie können auch eine Empfehlung direkt aus einem einzelnen Katalog erstellen. Wählen Sie Ihren Katalog auf der Seite **Kataloge** aus und wählen Sie dann **Empfehlung erstellen**.
{% endtab %}
{% endtabs %}

### Schritt 2: Details zur Empfehlung hinzufügen

Geben Sie Ihrer Empfehlung einen Namen und eine optionale Beschreibung.

!["Empfehlungsdetails" Schritt mit den Feldern Name und Beschreibung.]({% image_buster /assets/img/item_recs_1.png %})

### Schritt 3: Definieren Sie Ihre Empfehlung {#recommendation-type}

Wählen Sie einen Empfehlungstyp aus. Jeder Typ verwendet die Daten der letzten sechs Monate zur Interaktion mit einem Artikel, z.B. Daten zu einem Kauf oder angepassten Events. Ausführlichere Informationen und Anwendungsfälle finden Sie unter [Typen und Anwendungsfälle]({{site.baseurl}}/user_guide/brazeai/recommendations/).

{% alert tip %}
Wenn Sie die Option **Neueste** oder **KI personalisiert** verwenden, erhalten Benutzer, deren Daten nicht ausreichen, um individuelle Empfehlungen zu erstellen, als Ausweichlösung **die beliebtesten** Artikel. Der Anteil der Nutzer, die den **beliebtesten** Fallback erhalten, wird auf der **Analytics-Seite** angezeigt.
{% endalert %}

#### Schritt 3.1: Frühere Käufe oder Interaktionen ausschließen (optional)

Um zu vermeiden, dass Artikel vorgeschlagen werden, die ein Benutzer bereits gekauft oder mit denen er interagiert hat, wählen Sie **Keine Artikel empfehlen, mit denen Benutzer zuvor interagiert** haben. Diese Option ist nur verfügbar, wenn der **Empfehlungstyp** auf **AI personalisiert** eingestellt ist.

!["Definieren Sie Ihre Empfehlung" mit "KI Personalisiert" als Typ und der ausgewählten Option "Keine Artikel empfehlen, mit denen Nutzer:innen zuvor interagiert haben".]({% image_buster /assets/img/item_recs_2-3.png %})

Diese Einstellung verhindert, dass Nachrichten die Artikel wiederverwenden, die ein Benutzer bereits gekauft oder mit denen er interagiert hat, vorausgesetzt, die Empfehlung wurde kürzlich aktualisiert. Artikel, die Sie zwischen den Empfehlungsaktualisierungen gekauft haben oder mit denen Sie interagiert haben, können weiterhin angezeigt werden. Für die kostenlose Version der Artikel-Empfehlungen werden wöchentlich Aktualisierungen vorgenommen. In der Pro-Version erfolgt die Aktualisierung der KI-Artikelempfehlungen alle 24 Stunden.

Wenn Sie beispielsweise die Pro-Version der KI-Artikel-Empfehlungen verwenden und ein Nutzer etwas kauft und dann innerhalb von 30 Minuten eine Marketing-E-Mail erhält, wird der Artikel, den er gerade gekauft hat, möglicherweise nicht rechtzeitig aus der E-Mail ausgeschlossen. Nachrichten, die später gesendet werden, enthalten diesen Artikel aber nicht mehr.

#### Schritt 3.2: Katalog auswählen

Falls noch nicht ausgefüllt, wählen Sie den [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs/) aus, aus dem diese Empfehlung Artikel beziehen soll.

#### Schritt 3.3: Eine Auswahl hinzufügen (optional)

Wenn Sie mehr Kontrolle über Ihre Empfehlung wünschen, wählen Sie eine [Auswahl]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/), um benutzerdefinierte Filter anzuwenden. Mit Auswahlen können Empfehlungen nach bestimmten Spalten im Katalog wie Marke, Größe oder Standort gefiltert werden. Auswahlen, die Liquid enthalten, können nicht in Ihrer Empfehlung verwendet werden.

![Ein Beispiel für die für die Empfehlung ausgewählte "vorrätige" Auswahl.]({% image_buster /assets/img/item_recs_2-2.png %})

{% alert tip %}
Wenn Sie keine Auswahl finden können, vergewissern Sie sich zunächst, dass sie im Katalog eingerichtet ist.
{% endalert %}

### Schritt 4: Wählen Sie die Interaktion, um Empfehlungen auszusprechen

Wählen Sie das Ereignis aus, auf das Sie die Empfehlung abstimmen möchten. Bei diesem Ereignis handelt es sich in der Regel um einen Kauf, aber es kann auch jede andere Interaktion mit einem Artikel sein.

Möglich sind:

- Kaufereignisse mit dem [Kaufobjekt]({{site.baseurl}}/api/objects_filters/purchase_object/)
- Benutzerdefinierte Ereignisse, die einen Kauf darstellen
- Benutzerdefinierte Ereignisse, die eine andere Artikelinteraktion darstellen (z. B. Produktansichten, Klicks oder Medienwiedergabe)

Unter **Benutzerdefiniertes Ereignis** können Sie ein Ereignis aus der Liste auswählen.

![Das angepasste Event "Abgeschlossener Kauf" ausgewählt, wie die Events derzeit getrackt werden.]({% image_buster /assets/img/item_recs_3.png %})

### Schritt 5: Wählen Sie den entsprechenden Eigenschaftsnamen {#property-name}

Um eine Empfehlung zu erstellen, müssen Sie Braze mitteilen, welches Feld Ihres Interaktionsereignisses (Kaufobjekt oder benutzerdefiniertes Ereignis) die eindeutige Kennung hat, die mit dem Feld `id` eines Artikels im Katalog übereinstimmt. Nicht sicher? [Anforderungen anzeigen](#requirements).

Wählen Sie dieses Feld für den **Eigenschaftsnamen**.

Das Feld **Eigenschaftsname** wird mit einer Liste von Feldern vorausgefüllt, die über das SDK an Braze gesendet werden. Wenn genügend Daten zur Verfügung gestellt werden, werden diese Eigenschaften auch in der Reihenfolge der Wahrscheinlichkeit, dass es sich um die richtige Eigenschaft handelt, eingeordnet. Wählen Sie daraus das aus, das zu dem Katalogfeld `id` passt.

![Der Name der Eigenschaft "purchase_item" wurde ausgewählt, die den IDs der Artikel im Katalog entspricht.]({% image_buster /assets/img/item_recs_4.png %})

#### Anforderungen {#requirements}

Es gibt einige Vorbedingungen zur Auswahl von Eigenschaften:

- Sie muss dem Feld `id` des ausgewählten Katalogs zugeordnet sein.
- **Wenn Sie Kaufobjekt ausgewählt haben,** muss sie die `product_id` oder ein `properties`-Ereignisfeld sein.
- **Wenn Sie Benutzerdefiniertes Ereignis ausgewählt haben,** Muss ein Feld aus dem `properties` Ihres benutzerdefinierten Ereignisses sein.
- Verschachtelte Felder müssen in der Dropdown-Liste **Eigenschaftsname** in Punktschreibweise im Format `event_property.nested_property` eingegeben werden. Wenn Sie zum Beispiel die verschachtelte Eigenschaft `district_name` in der Ereigniseigenschaft `location` auswählen, geben Sie `location.district_name` ein.
- Das Feld kann sich innerhalb eines Arrays von Produkten befinden oder mit einem Array von IDs enden. In beiden Fällen werden die Produkt-IDs als separate aufeinanderfolgende Ereignisse mit demselben Zeitstempel behandelt.

#### Beispiel-Zuordnungen

Die folgenden Beispiel-Zuordnungen beziehen sich beide auf diesen Beispielkatalog:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">Titel</th>
    <th class="tg-0pky">Preis</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">ADI-BL-7</td>
    <td class="tg-0pky">Adidas Schwarz Größe 7</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-RD-8</td>
    <td class="tg-0pky">Adidas Rot Größe 8</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-WH-9</td>
    <td class="tg-0pky">Adidas Weiß Größe 9</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-PP-10</td>
    <td class="tg-0pky">Adidas Lila Größe 10</td>
    <td class="tg-0pky">75.00 USD</td>
  </tr>
</tbody>
</table>

{% tabs %}
{% tab Custom event %}

Nehmen wir an, Sie möchten das benutzerdefinierte Ereignis `added_to_cart` verwenden, damit Sie ähnliche Produkte empfehlen können, bevor der Kunde zur Kasse geht. Das Ereignis `added_to_cart` enthält die Ereigniseigenschaft `product_sku`.

Daher muss die Eigenschaft `product_sku` mindestens einen der Werte aus Spalte `id` im Musterkatalog enthalten: "ADI-BL-7", "ADI-RD-8", "ADI-WH-9" oder "ADI-PP-10". Sie benötigen nicht für jeden Katalogartikel Ereignisse, aber doch so viele, dass das Empfehlungssystem genügend Inhalte bekommt.

##### Beispiel für ein benutzerdefiniertes Ereignisobjekt

Das Ereignis enthält `"product_sku": "ADI-BL-7"`, die mit dem ersten Artikel im Musterkatalog übereinstimmt.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "product_sku": "ADI-BL-7"
      }
    }
  ]
}
```

##### Beispiel für ein benutzerdefiniertes Ereignisobjekt mit einem Array von Produkten

Wenn die Ereigniseigenschaften mehrere Produkte aus einem Array enthalten, wird jede Produkt-ID als separates aufeinanderfolgendes Ereignis behandelt. Das Ereignis kann mit der Eigenschaft `products.sku` den ersten und dritten Artikel im Musterkatalog finden.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "2ff3f9a9-8803-4c3a-91da-14adbf93dc99",
        "products": [
          { "sku": "ADI-BL-7" },
          { "sku": "ADI-WH-9" }
        ]
      }
    }
  ]
}
```

##### Beispiel für ein benutzerdefiniertes Ereignisobjekt mit einem verschachtelten Objekt, das ein Produkt-ID-Array enthält

Wenn es sich bei Ihren Produkt-IDs um Werte in einem Array statt um Objekte handelt, können Sie dieselbe Notation verwenden und jede Produkt-ID wird als separates, sequenzielles Ereignis behandelt. Dies kann im folgenden Ereignis auch mit verschachtelten Objekten kombiniert werden. Dazu konfigurieren Sie die Eigenschaft als `purchase.product_skus`, damit sie mit dem ersten und dritten Objekt im Beispielkatalog übereinstimmt.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "13791e08-7c22-4f6c-8cc6-832c76af3743",
        "purchase": {
          "product_skus": ["ADI-BL-7", "ADI-WH-9"]
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Purchase object %}

Ein Kaufobjekt wird von der API übergeben, wenn ein Kauf getätigt wird.

Was die Zuordnung betrifft, so gilt für Kaufobjekte eine ähnliche Logik wie für benutzerdefinierte Ereignisse, mit dem Unterschied, dass Sie zwischen der Verwendung des `product_id` des Kaufobjekts oder eines Feldes im `properties` Objekt wählen können.

Beachten Sie: Sie benötigen nicht für jeden Katalogartikel Ereignisse, aber doch so viele, dass das Empfehlungssystem genügend Inhalte bekommt.

##### Beispiel eines Kaufobjekts, das einer Produkt-ID zugeordnet ist

Das Ereignis enthält `"product_id": "ADI-BL-7`, die mit dem ersten Artikel im Musterkatalog übereinstimmt.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "ADI-BL-7",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "color": "black",
        "checkout_duration": 180,
        "size": "7",
        "brand": "Adidas"
      }
    }
  ]
}
```

##### Beispiel für ein Kaufobjekt, das einem Eigenschaftsfeld zugeordnet ist

Dieses Ereignis hat die Eigenschaft `"sku": "ADI-RD-8"`, die auf den zweiten Artikel im Katalog verweist.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "shoes",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "sku": "ADI-RD-8",
        "color": "red",
        "checkout_duration": 180,
        "size": "8",
        "brand": "Adidas"
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### Schritt 6: Empfehlungen verbessern

Wenn Sie so weit sind, gehen Sie auf **Empfehlung erstellen**. Dieser Vorgang kann zwischen 10 Minuten und 36 Stunden in Anspruch nehmen. Sie erhalten eine E-Mail-Aktualisierung, wenn die Empfehlung erfolgreich trainiert wurde, oder eine Erklärung, warum die Erstellung möglicherweise fehlgeschlagen ist.

Sie finden die Empfehlung auf der Seite **Vorhersagen**, wo Sie sie dann nach Bedarf bearbeiten oder archivieren können. Die Empfehlungen werden automatisch einmal pro Woche (kostenpflichtig) oder pro Monat (kostenlos) neu trainiert.