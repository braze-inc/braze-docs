---
nav_title: Produkt-Blöcke
article_title: Drag-and-Drop Produktblöcke
page_order: 7.5
description: "Dieser Artikel referenziert Produktblöcke per Drag-and-Drop, mit denen Nutzer:innen schnell dynamische oder statische Vitrinen für Katalogartikel hinzufügen und konfigurieren können."
tool:
    - Campaigns
    - Canvas
alias: /dnd_product_blocks/
---

# Produktblöcke per Drag-and-Drop verschieben 

> Mit dem Drag-and-Drop-Editor können Sie Ihren Nachrichten schnell Produktblöcke hinzufügen und konfigurieren, um Produkte nahtlos zu präsentieren, ohne dass Sie angepassten Liquid Code erstellen müssen. 

{% alert important %}
Das Drag-and-Drop Feature zum Blockieren von Produkten befindet sich noch im Anfangsstadium und ist derzeit nur per E-Mail verfügbar. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Anforderungen 

| Anforderung | Beschreibung |
| --- | --- |
| E-Commerce empfohlene Veranstaltungen | [Die im E-Commerce empfohlenen Ereignisse]({{site.baseurl}}/ecommerce_events/) bieten standardisierte Datenschemata für wichtige Verhaltensereignisse, die vor und nach einer Bestellung auftreten. Diese Ereignisse werden schließlich das alte Kauf-Event von Braze ersetzen und zum Standard für das Tracking von handelsbezogenem Verhalten werden. <br><br> E-Commerce empfohlene Ereignisse sind für dynamische Produktblöcke erforderlich.<br><br> E-Commerce empfohlene Veranstaltungen sind derzeit im frühen Zugriff. Wenden Sie sich an Ihren Customer-Success-Manager:in von Braze, wenn Sie an diesem frühzeitigen Zugang teilnehmen möchten. |
| E-Commerce Canvas Templates | Die empfohlenen E-Commerce-Ereignisse unterstützen vorgefertigte Templates, einschließlich E-Commerce Canvas-Templates, die für wichtige Anwendungsfälle wie abgebrochenes Browsing, abgebrochene Warenkörbe und Bestellbestätigungen entwickelt wurden. <br><br>Wenn Sie einen dieser wesentlichen E-Commerce Anwendungsfälle mit Hilfe der [E-Commerce Canvas-Vorlagen]({{site.baseurl}}/ecommerce_use_cases/) implementieren möchten, müssen Sie das mitgelieferte Canvas Template verwenden oder befolgen. |
| Braze Katalog | Sie müssen einen Braze-Katalog erstellen, der die folgenden Felder enthält, die in Ihrer Produktblockkonfiguration verwendet werden sollen:{::nomarkdown}<code><ul><li>product_title</li><li>product_url</li><li>variant_image_url</li></ul></code>{:/} |
| Katalogauswahl | Für statische Produktblöcke müssen Sie eine [Katalogauswahl]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) erstellen, um festzulegen, welche Produkte in Ihren Produktblock aufgenommen werden sollen. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

## Arten von Drag-and-Drop-Produktblöcken

| Produkt-Block | Zweck | Anwendungsfälle | Verfügbarkeit |
| --- | --- | --- | --- |
| Dynamisch | Passen Sie Ihr Messaging mit einer Präsentation von Produkten auf der Grundlage von Kundeninteraktionen an, indem Sie [die von E-Commerce empfohlenen Events]({{site.baseurl}}/ecommerce_events/) und Kataloge innerhalb unserer [E-Commerce Canvas Templates]({{site.baseurl}}/ecommerce_use_cases/) verwenden. | {::nomarkdown}<ul><li>Verlassenes Stöbern</li><li>Warenkorb-Abbruch</li><li>Abgebrochene Kasse</li><li>Auftragsbestätigungen</li></ul>{:/} | Nur in Canvas erhältlich. |
| Statisch | Personalisieren Sie Produkte mit Hilfe von Daten, die in einem Braze Katalog gespeichert sind. Sie müssen eine [Katalogauswahl]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) verwenden, um festzulegen, welche Produkte aufgenommen werden sollen. | Perfekt, um neue Produkte oder kategoriespezifische Angebote zu präsentieren.| |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role=”presentation” }

## Konfiguration des Inhalts eines Produkt-Blocks

Jeder Block-Typ hat unterschiedliche Content-Konfigurationen. 

### Produktfelder

Wählen Sie im Bereich **Produktfelder** Ihren Produktblocktyp aus und schalten Sie dann die Felder um, die Sie für jedes Produkt einfügen möchten. Jedes Feld wird aus verschiedenen Quellen bezogen, je nachdem, welche Art von Produktblock Sie auswählen.

#### Dynamischer Produktblock

| Feld Produkt | Quelle |
| --- | --- | 
| Bild für Variante | Kataloge | 
| Produkttitel | Kataloge | 
| Produkt-URL-Button | Kataloge |
| Preis | E-Commerce Empfohlene Eigenschaft eines Ereignisses|
| Menge | E-Commerce Empfohlene Eigenschaft eines Ereignisses| 
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

\![Produktfelder für einen dynamischen Produktblock, die in Katalogdaten und Ereignisdaten unterteilt sind]({% image_buster /assets/img/product_blocks/dynamic_fields.png %}){: style="max-width:50%;"}

#### Statischer Produktblock

| Feld Produkt | Quelle |
| --- | --- | --- |
| Bild für Variante | Kataloge |
| Produkttitel | Kataloge |
| Produkt-URL-Button | Kataloge |
| Preis | Kataloge |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role=“presentation” }

\![Produktfelder für einen statischen Produktblock, die alle als Katalogdaten kategorisiert sind.]({% image_buster /assets/img/product_blocks/static_fields.png %}){: style="max-width:50%;"}

### Layout-Optionen

Verwenden Sie die Layout-Optionen, um die Darstellung Ihrer Produkte innerhalb Ihres Produktblocks anzupassen.

| Option | Beschreibung |
| --- | --- |
| Produktorientierung | Wählen Sie, wie die Bild- und Produktfelder innerhalb des Blocks ausgerichtet sind. |
| Ausrichtung | Passen Sie die Ausrichtung der Textfelder und des Buttons innerhalb des Blocks an. |
| Max. Produkte pro Zeile | Zeigen Sie bis zu drei Produkte pro Zeile an, bis zu 12 Produkte insgesamt für statische Produktblöcke und bis zu 24 Produkte insgesamt für dynamische Produktblöcke. |
| Produktabstand | Legen Sie die Abstände zwischen den Produkten fest. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

Layout-Optionen für die Produktausrichtung, die Ausrichtung, die maximale Anzahl von Produkten pro Zeile und die Produktabstände.]({% image_buster /assets/img/product_blocks/layout_options.png %}){: style="max-width:50%;"}

### Globale Einstellungen für den E-Mail-Stil 

Mit [den globalen Einstellungen für den E-Mail-Stil]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings) können Sie innerhalb von Braze ein einheitliches Design für Ihre E-Mails verwenden. Das bedeutet, dass Sie bestimmte Stile - wie z.B. Schriftarten, Farben und Button-Designs - definieren können, die dann automatisch für alle Ihre E-Mails gelten.

#### Wie globale Einstellungen für E-Mails mit Produktblöcken funktionieren

Vorhandene Stile für Absätze und Buttons werden automatisch auf die Text- und Button-Elemente innerhalb des Produktblocks angewendet. Das bedeutet, dass alle Formatierungen, die Sie für Absätze und Buttons festgelegt haben, konsistent in Ihrem Produktblock verwendet werden, so dass die gesamte E-Mail ein einheitliches Erscheinungsbild aufweist.

## Einrichten von Produktblöcken

### Katalog einrichten 

{% alert important %}
Wenn Sie die Integration von Braze und Shopify für die [Produktsynchronisierung]({{site.baseurl}}/shopify_catalogs/) verwenden, müssen Sie keine zusätzlichen Schritte unternehmen, um Drag-and-Drop-Produktblöcke zu verwenden.<br><br> Wenn Sie nicht über Informationen zu Produktvarianten verfügen, müssen Sie die Informationen zu den Produkten der obersten Ebene sowohl in den Feldern für das Produkt als auch für die Produktvariante in den Ereignis-Nutzlasten und Katalogen duplizieren. Das bedeutet, dass Sie für beide Bezeichner dieselben Produktdetails angeben müssen, damit der Produktblock richtig funktioniert.
{% endalert %}

Um Drag-and-Drop-Produktblöcke zu verwenden, müssen Sie einen Braze-Katalog einrichten, der bestimmte Feldwerte enthält. Diese Felder werden in der Konfiguration Ihres Produktblocks verwendet. Stellen Sie sicher, dass Ihr Katalog die folgenden Felder enthält:

| Feld | Beschreibung |
| --- | --- |
|`product_title` | Der Titel des Produkts.|
|`product_url` | Die URL, unter der Kund:innen das Produkt ansehen oder kaufen können. |
|`variant_image_url` | Die URL für das Bild der Variante. |

Beginnen Sie mit diesem [Muster-Produktkatalog]({{site.baseurl}}/assets/download_file/ecommerce_product_catalog_sample.csv), der die erforderlichen Felder enthält. 

\![Eine Beispiel-CSV-Datei mit den erforderlichen Feldern zusätzlich zu anderen.]({% image_buster /assets/img/ecommerce/sample_product_catalog.png %})

## Produktblöcke erstellen

In dieser Anleitung erfahren Sie, wie Sie mit unserem E-Mail Drag-and-Drop-Editor einen dynamischen oder statischen Produkt-Block erstellen, testen und seine Funktionalität sicherstellen.

### Schritt 1: Erstellen einer E-Mail Kampagne oder eines E-Mail Canvas-Schrittes

#### Dynamischer Produktblock

{% alert note %}
Dynamische Produktblöcke erfordern von [E-Commerce empfohlene Ereignisse]({{site.baseurl}}/ecommerce_events/) und können nur innerhalb von [Canvase]({{site.baseurl}}/ecommerce_use_cases) verwendet werden. Für Braze Shopify Nutzer:innen sind diese Ereignisse automatisch Teil der Integration. Für Nutzer:innen, die nicht Shopify verwenden, müssen Sie mit Ihren Entwicklern zusammenarbeiten, um diese Ereignisse an Braze weiterzuleiten und sicherzustellen, dass der primäre Bezeichner des Produkts in den Ereignissen als ID des Artikels im Katalog hinzugefügt wird.
{% endalert %}

Erstellen Sie ein neues Canvas, das eine der verfügbaren Braze-Templates für Ihren speziellen Anwendungsfall verwendet:
- Verlassenes Stöbern
- Warenkorb-Abbruch
- Checkout-Abbruch
- Auftragsbestätigungen

Ausführliche Anweisungen zur Erstellung Ihrer E-Commerce Canvase finden Sie unter [Anwendungsfälle im E-Commerce]({{site.baseurl}}/ecommerce_use_cases/).

#### Statischer Produktblock

Erstellen Sie eine Drag-and-Drop-E-Mail-Kampagne, ein aktionsbasiertes Canvas oder ein Template, das einen Drag-and-Drop-Schritt für eine E-Mail-Nachricht enthält.

### Schritt 2: Einen Produktblock hinzufügen

{% tabs %}
{% tab Dynamic product block %}

Erstellen Sie im Schritt Nachrichten eine E-Mail oder ändern Sie die vorhandene Vorlage mit dem Drag-and-Drop Nachrichten-Editor.
Ziehen Sie einen Produktblock in Ihre E-Mail Nachricht.
Bestätigen Sie, dass der dynamische Blocktyp ausgewählt ist.
Wählen Sie den Produktkatalog aus, den Sie für die Personalisierung verwenden möchten. Vergewissern Sie sich, dass es zu den Produkten aus den eingehenden Veranstaltungen passt, auf die Sie Targeting betreiben.

{% endtab %}
{% tab Static product block %}

Ziehen Sie einen Produktblock in Ihre E-Mail Nachricht und wählen Sie den statischen Blocktyp aus.
Wählen Sie den Katalog aus, den Sie für Ihren Produktblock verwenden möchten. Sie müssen eine Katalogauswahl auswählen, um festzulegen, welche Produkte in Ihrem Produktblock angezeigt werden.

{% endtab %}
{% endtabs %}

\![Der Tab "Inhalt" mit Editor-Blöcken, wie z.B. Produkt-Blöcken.]({% image_buster /assets/img/product_blocks/product_block.png %}){: style="max-width:40%;"}

### Schritt 3: Produktfelder konfigurieren

Wählen Sie aus, welche [Produktfelder](#product-fields) im Produktblock angezeigt werden sollen. Wählen Sie nach jeder Änderung **Einstellungen übernehmen** aus, um die Updates im Editor zu sehen. 

Sie können auch den Text vor Ihren Liquid-Tags anpassen. Sie können zum Beispiel ein Dollarzeichen ($) für den Preis eines Artikels voranstellen oder den Begriff für die Menge auf "Menge" oder eine andere bevorzugte Bezeichnung aktualisieren.

\![Produktblock mit einem vorangestellten Dollarzeichen vor dem Preis des Artikels.]({% image_buster /assets/img/product_blocks/liquid.png %}){: style="max-width:45%;"}

### Schritt 4: Layout-Einstellungen konfigurieren

Ändern Sie die [Layout-Optionen](#layout-options), um zu aktualisieren, wie die Produkte in Ihrem Produktblock angezeigt werden, und wählen Sie nach jeder Änderung die Option **Einstellungen übernehmen** aus.

### Schritt 5: Vorschau und Test Ihrer Nachricht

{% tabs %}
{% tab Dynamic product block %}

1. Im Bereich **Vorschau & Test** können Sie eine Vorschau der Nachricht als angepasster Nutzer:in anzeigen.
2. Geben Sie an, wie viele Artikel Sie in der Vorschau darstellen möchten.
3. Vergewissern Sie sich, dass die richtige Anzahl von Artikeln angezeigt wird und dass Ihre Layout-Optionen korrekt angewendet werden. Beachten Sie, dass die angezeigten Artikel zufällig ausgewählt werden.

\!["Vorschau als Nutzer:innen" Tab mit einem Dropdown-Bereich "Dynamischer Produktblock", der angibt, dass 4 Artikel angezeigt werden sollen.]({% image_buster /assets/img/product_blocks/preview_as_a_user.png %}){: style="max-width:40%;"}

{% endtab %}
{% tab Static product block %}

Eine Vorschau wird im Drag-and-Drop Composer generiert, wenn Sie Änderungen an Ihrem Produktblock vornehmen. 

\![E-Mail Drag-and-Drop Composer zeigt einen generierten Produktblock mit verschiedenen Artikel-Kacheln.]({% image_buster /assets/img/product_blocks/static_block_preview.png %})

{% endtab %}
{% endtabs %}

Nachdem Sie Ihre Nachricht erstellt und bestätigt haben, dass sie wie erwartet aussieht, können Sie sie versenden!