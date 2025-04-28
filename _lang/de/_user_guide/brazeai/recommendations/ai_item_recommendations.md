---
nav_title: KI-Artikelempfehlungen
article_title: KI-Artikelempfehlungen
page_order: 15
alias: "/ai_item_recommendations/"
description: "Dieser Artikel beschreibt, wie Sie eine KI-Artikelempfehlung für Katalogposten erstellen."
---

# KI-Artikelempfehlungen

> Erfahren Sie, wie Sie eine KI-Artikelempfehlung für Katalogposten erstellen.

Nutzen Sie die KI-Artikelempfehlungen, um die beliebtesten Produkte zu berechnen, oder erstellen Sie personalisierte KI-Empfehlungen für einen bestimmten [Katalog][Katalog]. Anschließend können Sie die Personalisierung nutzen, um die Produkte in Nachrichten einzufügen.

## Voraussetzungen

Bevor Sie beginnen, sollten Sie Folgendes beachten:

- Für die unten beschriebenen Empfehlungsarten ist mindestens ein [Katalog][Katalog] erforderlich.
- Sie benötigen über Kauf- oder Ereignisdaten in Braze (benutzerdefinierte Ereignisse oder das Kaufobjekt), die einen Verweis auf eindeutige Produkt-IDs aus einem Katalog enthalten.

{% alert tip %}
[Personalisierte KI-Empfehlungen](#recommendation-types) funktionieren am besten bei sehr großen Inventaren und mindestens 30.000 Nutzern mit Kauf- oder Interaktionsdaten. Dies ist nur ein grober Richtwert und kann variieren. Die anderen Empfehlungstypen können mit weniger Daten arbeiten.
{% endalert %}

## KI-Artikelempfehlungen erstellen

So erstellen Sie eine Artikelempfehlung:

1. Gehen Sie zu **Analytics** > **AI-Artikel-Empfehlung**.
2. Wählen Sie **Vorhersage erstellen** > **KI-Artikel-Empfehlung**.

Sie können auch eine Empfehlung direkt aus einem einzelnen Katalog erstellen. Wählen Sie Ihren Katalog auf der Seite **Kataloge** aus und wählen Sie dann **Empfehlung erstellen**.

### Schritt 1: Details zur Empfehlung hinzufügen

Geben Sie Ihrer Empfehlung einen Namen und eine optionale Beschreibung.

![Schritt "Empfehlungsdetails" mit den Feldern Name und Beschreibung.][1]

### Schritt 2: Definieren Sie Ihre Empfehlung {#recommendation-type}

Wählen Sie den Empfehlungstyp. Alle Empfehlungstypen verwenden die Daten der letzten sechs Monate der Artikelinteraktion (Kauf oder benutzerdefiniertes Ereignis). Die unten erwähnte Interaktion bezieht sich entweder auf ein Kaufereignis oder ein in [Schritt 3](#step-3-select-the-interaction-to-drive-recommendations) ausgewähltes benutzerdefiniertes Ereignis.

- **Beliebt:** Berechnet bis zu 30 Katalogartikel, mit denen alle Benutzer im Arbeitsbereich besonders häufig interagieren, also z. B. die am häufigsten gekauften Produkte.
- **Neu:** Erstellt eine Liste mit bis zu 30 Produkten, mit denen ein Benutzer zuletzt interagiert hat.
- **KI-personalisiert:** Verwendet Transformers, eine neue Art von Deep Learning, um die wahrscheinlichste Gruppe von Objekten vorherzusagen, mit denen ein Nutzer als nächstes interagieren wird. Wir berechnen bis zu 30 der nächstwahrscheinlichen Artikel in der Reihenfolge von am wahrscheinlichsten bis am unwahrscheinlichsten. Bei dieser Art der Empfehlung werden keine großen Sprachmodelle (LLMs) verwendet, um Ihre Daten mit denen anderer Braze-Kunden zu kombinieren.
- **Im Trend:** Berechnet bis zu 30 Objekte aus dem Arbeitsbereich, die in letzter Zeit die meisten positiven Impulse in Bezug auf Benutzerinteraktionen hatten.

{% alert tip %}
Wenn Sie die Option **Neueste** oder **KI personalisiert** verwenden, erhalten Benutzer, deren Daten nicht ausreichen, um individuelle Empfehlungen zu erstellen, als Ausweichlösung **die beliebtesten** Artikel. Der Anteil der Nutzer, die den **beliebtesten** Fallback erhalten, wird auf der **Analytics-Seite** angezeigt.
{% endalert %}

#### Schritt 2a: Frühere Käufe oder Interaktionen ausschließen (optional)

Um zu vermeiden, dass Artikel vorgeschlagen werden, die ein Benutzer bereits gekauft oder mit denen er interagiert hat, wählen Sie **Keine Artikel empfehlen, mit denen Benutzer zuvor interagiert** haben. Diese Option ist nur verfügbar, wenn der **Empfehlungstyp** auf **AI personalisiert** eingestellt ist.

![Schritt "Definieren Sie Ihre Empfehlung" mit dem Typ "Beliebteste" und der ausgewählten Option "Keine Artikel empfehlen, mit denen Nutzer:innen zuvor interagiert haben".][2-3]

Diese Einstellung verhindert, dass Nachrichten die Artikel wiederverwenden, die ein Benutzer bereits gekauft oder mit denen er interagiert hat, vorausgesetzt, die Empfehlung wurde kürzlich aktualisiert. Artikel, die Sie zwischen den Empfehlungsaktualisierungen gekauft haben oder mit denen Sie interagiert haben, können weiterhin angezeigt werden. Für die kostenlose Version der Artikel-Empfehlungen werden wöchentlich Aktualisierungen vorgenommen. In der Pro-Version erfolgt die Aktualisierung der KI-Artikelempfehlungen alle 24 Stunden.

Wenn Sie beispielsweise die Pro-Version der KI-Artikel-Empfehlungen verwenden und ein Nutzer etwas kauft und dann innerhalb von 30 Minuten eine Marketing-E-Mail erhält, wird der Artikel, den er gerade gekauft hat, möglicherweise nicht rechtzeitig aus der E-Mail ausgeschlossen. Nachrichten, die später gesendet werden, enthalten diesen Artikel aber nicht mehr.

#### Schritt 2b: Katalog auswählen

Falls er noch nicht eingetragen ist, wählen Sie den [Katalog][Katalog] aus, aus dem Artikel empfohlen werden sollen.

#### Schritt 2c: Eine Auswahl hinzufügen (optional)

Wenn Sie mehr Kontrolle über Ihre Empfehlung wünschen, wählen Sie eine [Auswahl]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/), um benutzerdefinierte Filter anzuwenden. Mit Auswahlen können Empfehlungen nach bestimmten Spalten im Katalog wie Marke, Größe oder Standort gefiltert werden. Auswahlen, die Liquid enthalten, können nicht in Ihrer Empfehlung verwendet werden.

![Ein Beispiel für die Auswahl "vorrätig", die für die Empfehlung ausgewählt wurde.][2-2]

{% alert tip %}
Wenn Sie keine Auswahl finden können, vergewissern Sie sich zunächst, dass sie im Katalog eingerichtet ist.
{% endalert %}

### Schritt 3: Wählen Sie die Interaktion, um Empfehlungen auszusprechen

Wählen Sie das Ereignis aus, auf das Sie die Empfehlung abstimmen möchten. Bei diesem Ereignis handelt es sich in der Regel um einen Kauf, aber es kann auch jede andere Interaktion mit einem Artikel sein.

Möglich sind:

- Kaufereignisse mit dem [Kaufobjekt]({{site.baseurl}}/api/objects_filters/purchase_object/)
- Benutzerdefinierte Ereignisse, die einen Kauf darstellen
- Benutzerdefinierte Ereignisse, die eine andere Artikelinteraktion darstellen (z. B. Produktansichten, Klicks oder Medienwiedergabe)

Unter **Benutzerdefiniertes Ereignis** können Sie ein Ereignis aus der Liste auswählen.

![Das angepasste Event "Abgeschlossener Kauf" ausgewählt, wie Events derzeit getrackt werden.][3]

### Schritt 4: Wählen Sie den entsprechenden Eigenschaftsnamen {#property-name}

Um eine Empfehlung zu erstellen, müssen Sie Braze mitteilen, welches Feld Ihres Interaktionsereignisses (Kaufobjekt oder benutzerdefiniertes Ereignis) die eindeutige Kennung hat, die mit dem Feld `id` eines Artikels im Katalog übereinstimmt. Nicht sicher? [Anforderungen anzeigen](#requirements).

Wählen Sie dieses Feld für den **Eigenschaftsnamen**.

Das Feld **Eigenschaftsname** wird mit einer Liste von Feldern vorausgefüllt, die über das SDK an Braze gesendet werden. Wenn genügend Daten zur Verfügung gestellt werden, werden diese Eigenschaften auch in der Reihenfolge der Wahrscheinlichkeit, dass es sich um die richtige Eigenschaft handelt, eingeordnet. Wählen Sie daraus das aus, das zu dem Katalogfeld `id` passt.

![Die Eigenschaft "purchase_item" wurde ausgewählt, die den IDs der Artikel im Katalog entspricht.][4]

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
{% tab Benutzerdefiniertes Ereignis %}

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
{% tab Kaufobjekt %}

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

### Schritt 5: Empfehlungen verbessern

Wenn Sie so weit sind, gehen Sie auf **Empfehlung erstellen**. Dieser Vorgang kann zwischen 10 Minuten und 36 Stunden in Anspruch nehmen. Sie erhalten eine E-Mail-Aktualisierung, wenn die Empfehlung erfolgreich trainiert wurde, oder eine Erklärung, warum die Erstellung möglicherweise fehlgeschlagen ist.

Sie finden die Empfehlung auf der Seite **Vorhersagen**, wo Sie sie dann nach Bedarf bearbeiten oder archivieren können. Die Empfehlungen werden automatisch einmal im Monat trainiert.

## Analytics

Sie können die Analysen für Ihre Empfehlungen einsehen, um zu sehen, welche Artikel Benutzern empfohlen wurden und wie genau das Empfehlungsmodell war.

1. Gehen Sie zu **Analytics** > **Artikel-Empfehlung**.
2. Wählen Sie Ihre Empfehlung aus der Liste aus.

Oben auf der Seite finden Sie Statistiken zu Ihrer Empfehlung, z. B. zur Genauigkeit und Reichweite.

![Metriken für die Zielgruppe der Empfehlungen zeigen die Genauigkeit (21,1%), die Abdeckung (83,0%) und die Empfehlungsarten, die sich in personalisierte und beliebteste Artikel aufteilen.][5]

Diese Metriken sind in der folgenden Tabelle definiert. 

| Metrisch              | Beschreibung |
| ------------------- | ---------- |
| Präzision           | Der Prozentsatz der Zeit, in der das Modell den nächsten Artikel, den ein Benutzer gekauft hat, richtig erraten hat. Die Genauigkeit hängt stark von Ihrer spezifischen Kataloggröße und -mischung ab und sollte als Richtwert dienen, um zu verstehen, wie oft das Modell korrekt ist.<br><br>Bei Tests haben wir festgestellt, dass Modelle mit einer Genauigkeit von 6–20% am besten abschneiden. Diese Metrik wird aktualisiert, wenn das Modell das nächste Mal neu trainiert wird.  |
| Abdeckung            | Wie viel Prozent der verfügbaren Artikel im Katalog werden mindestens einem Benutzer empfohlen. Sie können davon ausgehen, dass Sie eine höhere Artikelabdeckung mit personalisierten Artikelempfehlungen als mit den beliebtesten Artikeln erreichen. |
| Empfehlungstyp | Prozentualer Anteil der Nutzer, die personalisierte oder neueste Empfehlungen erhalten, im Gegensatz zu den beliebtesten Artikeln. Der Fallback wird an Benutzer gesendet, die nicht über genügend Daten verfügen, um eine personalisierte oder aktuelle Empfehlung zu erstellen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Der nächste Abschnitt enthält eine Aufteilung der Katalogartikel in zwei mögliche Spalten:

- **Personalisierte Artikel** oder **Neueste Artikel:** Diese Spalte listet jeden Artikel im Katalog in absteigender Reihenfolge der am häufigsten empfohlenen Artikel auf. In dieser Spalte sehen Sie auch, wie viele Benutzer den einzelnen Artikeln durch das Modell zugeordnet wurden.
- **Beliebteste Artikel:** Diese Spalte listet jeden Artikel im Katalog in absteigender Reihenfolge seiner Beliebtheit auf. Beliebtheit bezieht sich hier auf die Objekte im Katalog, mit denen Benutzer im gesamten Arbeitsbereich am häufigsten interagieren. Beliebteste wird als Ausweichlösung verwendet, wenn für einen einzelnen Benutzer keine personalisierte oder neueste Version berechnet werden kann.

![Nebeneinander angeordnete Tabellen mit den den Nutzer:innen zugewiesenen Artikeln, getrennt nach personalisierten Empfehlungen und beliebtesten Empfehlungen.][6]

Die **Empfehlungsübersicht** zeigt eine Zusammenfassung der von Ihnen gewählten Empfehlungskonfiguration, einschließlich des Zeitpunkts, zu dem die Empfehlung zuletzt aktualisiert wurde.

![Übersichtstabelle für Empfehlungen, die den Typ, den Katalog, den Ereignistyp, den Namen des angepassten Events, den Namen der Eigenschaft und das Datum des letzten Updates anzeigt.][7]{: style="max-width:45%" }

## Empfehlungen in der Nachrichtenübermittlung verwenden

![Modal "Personalisierung hinzufügen" mit Artikel-Empfehlung als Personalisierungstyp.][10]{: style="max-width:30%;float:right;margin-left:15px;"}

Wenn die Empfehlung trainiert worden ist, können Sie Ihre Nachrichten mit Liquid personalisieren, um die beliebtesten Produkte aus dem Katalog einzufügen. Das Liquid kann über das Personalisierungsfenster in den Nachrichtenkompilern für Sie erstellt werden:

1. Wählen Sie in jedem Nachrichtenkomponisten, der Personalisierung unterstützt, die Option <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Personalisierung hinzufügen"></i> um das Fenster für die Personalisierung zu öffnen.
2. Wählen Sie für **Personalisierungstyp** die Option **Artikelempfehlung**.
3. Wählen Sie unter **Name der Produktempfehlung** die Empfehlung aus, die Sie gerade erstellt haben.
4. Geben Sie bei **Anzahl der voraussichtlichen Artikel** ein, wie viele Top-Produkte Sie einfügen möchten. Sie können zum Beispiel die drei meistgekauften Artikel anzeigen.
5. Wählen Sie unter **Anzuzeigende Informationen**, welche Felder aus dem Katalog für jeden Artikel angezeigt werden sollen. Die Werte für diese Felder werden für jeden Artikel aus dem mit dieser Empfehlung verbundenen Katalog entnommen.
6. Wählen Sie das Symbol **Kopieren** und fügen Sie die Flüssigkeit an der Stelle ein, an der sie in Ihrer Nachricht erscheinen soll.

## KI-Artikelempfehlungen – Tarifstufen

Die folgende Tabelle beschreibt die Unterschiede zwischen der kostenlosen und der Pro-Version der KI-Empfehlungstypen Personalisiert, Beliebt und Tendenziell:

| Bereich                   | Kostenlose Version                          | Pro Version            |
| :---------------------- | ------------------------------------- | :--------------------------------------- |
| Aktualisierungshäufigkeit<sup>1</sup>   | Wöchentlich                                | Täglich                                    |
| Häufigkeit der Nachschulung des Modells  | Monatlich                               | Monatlich                                   |
| Modelle für maximale Empfehlungen | 1 Modell pro <sup>Typ2</sup> | 100 Modelle je Typ<sup>2</sup> |

<sup>1\. Dies ist die Häufigkeit, mit der benutzerspezifische Artikelempfehlungen aktualisiert werden (alle Modelle mit Ausnahme der beliebtesten Artikel, die aktualisiert werden, wenn das Modell neu trainiert wird). Wenn ein Benutzer beispielsweise einen Artikel auf Grundlage von KI-Empfehlungen kauft, werden die empfohlenen Artikel in dieser Häufigkeit aktualisiert</sup><br>
<sup>2\. Verfügbare Empfehlungsarten sind KI-personalisiert, Neu, Beliebt und Im Trend.</sup>

## Häufig gestellte Fragen

### Wie kommt es dazu, dass "Beliebteste" Artikel mit den Empfehlungen anderer Modelle vermischt werden?

Wenn das Empfehlungssystem eine Liste für Sie zusammenstellt, priorisiert sie zunächst die personalisierte Auswahl auf der Grundlage des von Ihnen gewählten Modells, also z. B. "Neu" oder "KI personalisiert". Wenn dieses Modell aus irgendeinem Grund nicht die komplette Liste mit 30 Empfehlungen füllen kann, werden einige Ihrer bei allen Nutzern beliebtesten Artikel hinzugefügt, um sicherzustellen, dass jeder Nutzer immer einen vollständigen Satz an Empfehlungen hat.

Dies geschieht unter einigen besonderen Bedingungen:

- Das Modell findet weniger als 30 Artikel, die Ihren Kriterien entsprechen.
- Die entsprechenden Artikel sind nicht mehr verfügbar oder auf Lager.
- Die Artikel entsprechen nicht den aktuellen Auswahlkriterien, z.B. weil sich der Bestand oder die Präferenzen des Benutzers geändert haben.

### Werden bestehende Empfehlungen nach dem Upgrade auf Item Recommendations Pro wöchentlich trainiert?

Ja, aber erst nach ihrem nächsten geplanten Update. Bestehende Empfehlungen schalten beim Upgrade auf Artikel-Empfehlungen Pro nicht sofort auf wöchentliches Training und tägliche Prognosen um. Sie werden den neuen Zeitplan jedoch automatisch bei ihrem nächsten Umschulungszyklus übernehmen. Wenn eine Empfehlung zum Beispiel zuletzt am 1\. Februar trainiert wurde und so eingestellt ist, dass sie alle 30 Tage neu trainiert wird, übernimmt sie den neuen wöchentlichen Zeitplan nach dem nächsten Update am 2\. März.

[1]: {% image_buster /assets/img/item_recs_1.png %}
[2-1]: {% image_buster /assets/img/item_recs_2-1.png %}
[2-2]: {% image_buster /assets/img/item_recs_2-2.png %}
[2-3]: {% image_buster /assets/img/item_recs_2-3.png %}
[3]: {% image_buster /assets/img/item_recs_3.png %}
[4]: {% image_buster /assets/img/item_recs_4.png %}
[5]: {% image_buster /assets/img/item_recs_analytics_1.png %}
[6]: {% image_buster /assets/img/item_recs_analytics_2.png %}
[7]: {% image_buster /assets/img/item_recs_analytics_3.png %}
[10]: {% image_buster /assets/img/add_personalization.png %}
[catalog]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/
