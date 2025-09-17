---
nav_title: Shopify Produkt-Synchronisation
article_title: Shopify Produkt-Synchronisation
alias: /shopify_catalogs/
page_order: 4
description: "Dieser referenzierte Artikel beschreibt, wie Sie Ihre Produkte aus Shopify in Braze-Kataloge importieren."
---

# Shopify Produkte synchronisieren 

> Sie können alle Produkte aus Ihrem Shopify Shop mit einem Braze [Katalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) synchronisieren, um die Personalisierung von Nachrichten zu vertiefen. 

Shopify-Kataloge werden nahezu in Realtime aktualisiert, wenn Sie die Produkte in Ihrem Shopify-Shop bearbeiten und ändern. Sie können Ihren Warenkorb-Abbruch, Ihre Bestellbestätigung und vieles mehr mit den aktuellsten Produktdetails und Informationen anreichern.

## Einrichten der Synchronisierung Ihrer Produkte mit Shopify {#setting-up}

Wenn Sie Ihren Shopify Shop bereits installiert haben, können Sie Ihre Produkte trotzdem synchronisieren, indem Sie die folgenden Anweisungen befolgen. 

### Schritt 1: Schalten Sie die Synchronisation ein

Sie können Ihre Produkte mit einem Braze-Katalog über den Shopify-Installationsablauf oder auf der Shopify Partnerseite synchronisieren. 

![Schritt 3 der Einrichtung mit "Shopify Variant ID" als "Bezeichner für das Produkt im Katalog".]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:70%;"}

Produkte, die mit einem Braze-Katalog synchronisiert werden, tragen zu Ihrem [Katalog-Limit]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits) bei.

### Schritt 2: Wählen Sie Ihren Bezeichner für das Produkt aus

Wählen Sie den Bezeichner des Produkts aus, der als Katalog ID verwendet werden soll:
- Shopify-Varianten-ID
- SKU

Die ID- und Kopfwerte für den von Ihnen gewählten Bezeichner des Produkts dürfen nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten. Wenn der Bezeichner des Produkts nicht diesem Format entspricht, filtert Braze ihn aus Ihrer Katalogsynchronisierung heraus.

Dies ist der primäre Bezeichner, mit dem Sie die Kataloginformationen von Braze referenzieren. 

{% alert note %}
Wenn Sie SKU als Katalog-ID auswählen, stellen Sie sicher, dass alle Produkte und Varianten in Ihrem Shop eine SKU haben und eindeutig sind. 
- Wenn ein Artikel eine fehlende SKU hat, kann Braze dieses Produkt nicht mit dem Katalog synchronisieren. 
- Wenn Sie mehr als ein Produkt mit der gleichen SKU haben, kann dies zu unerwartetem Verhalten führen oder dazu, dass die Produktinformationen unbeabsichtigt durch die doppelte SKU überschrieben werden.
{% endalert %}

### Schritt 3: Synchronisierung läuft

Sie erhalten eine Benachrichtigung auf dem Dashboard und Ihr Status wird als "In Bearbeitung" angezeigt, um anzuzeigen, dass die erste Synchronisierung beginnt. Beachten Sie, dass die Dauer der Synchronisierung davon abhängt, wie viele Produkte und Varianten Braze von Shopify synchronisieren muss. Während dieser Zeit können Sie diese Seite verlassen und auf eine Dashboard-Benachrichtigung oder eine E-Mail warten, die Sie benachrichtigt, wenn der Vorgang abgeschlossen ist.

Beachten Sie, dass Braze keine weiteren Produkte mehr synchronisieren wird, wenn die erste Synchronisierung Ihr [Kataloglimit]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits) überschreitet. Wenn Sie das Limit nach erfolgreicher Synchronisierung überschreiten, weil im Laufe der Zeit neue Produkte hinzukommen, wird die Synchronisierung nicht mehr aktiv sein. In beiden Fällen werden Updates für Produkte von Shopify nicht mehr in Braze angezeigt. Wenden Sie sich an Ihren Account Manager:in, um ein Upgrade Ihrer Stufe zu erwägen. 

### Schritt 4: Synchronisierung abgeschlossen

Sie erhalten eine Benachrichtigung auf dem Dashboard und eine E-Mail, nachdem die Synchronisierung erfolgreich war. Auf der Partnerseite von Shopify wird außerdem der Status unter Shopify-Kataloge auf "Synchronisierung" aktualisiert. Sie können sich Ihre Produkte ansehen, indem Sie auf der Shopify Partnerseite auf den Katalognamen klicken.

[Weitere Anwendungsfälle finden Sie unter Kataloge]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases), um mehr darüber zu erfahren, wie Sie Katalogdaten zur Personalisierung Ihrer Nachrichten nutzen können.

#### Unterstützte Shopify Katalogdaten

- `id`
- `store_name`
- `shopify_product_id`
- `shopify_variant_id`
- `product_title`
- `variant_title`
- `status`
- `body_html`
- `product_image_url`
- `variant_image_url`
- `vendor`
- `product_type`
- `product_url`
- `product_handle`
- `published_scope`
- `price`
- `compare_at_price`
- `inventory_quantity`
- `options`
- `option_values`
- `sku`

{% alert warning %}
Wenn Sie den Shopify-Katalog in irgendeiner Weise ändern, kann dies die Realtime-Synchronisierung von Produkten unbeabsichtigt beeinträchtigen. Nehmen Sie keine Änderungen am Shopify-Katalog vor, da diese von Shopify außer Kraft gesetzt werden könnten. Nehmen Sie stattdessen die notwendigen Updates für die Produkte in Ihrer Shopify Instanz vor.<br><br>Um Ihren Shopify-Katalog zu löschen, gehen Sie auf die Shopify-Seite und deaktivieren Sie die Synchronisierung. Löschen Sie den Shopify-Katalog nicht direkt auf der Seite Kataloge.
{% endalert %}

##### Verwenden Sie `product_handle` oder `product_url`

Die Felder `product_handle` und `product_url` sind in Ihren Shopify-Katalogdaten verfügbar.

## Anwendungsfälle für Back-in-Stock und Preisreduzierung

Um Benachrichtigungen über die Wiederverfügbarkeit von Waren einzurichten, folgen Sie bitte den Schritten [hier]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications#back-in-stock-notifications).

Um Benachrichtigungen über Preissenkungen einzurichten, folgen Sie den Schritten [hier]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications/).

Beachten Sie, dass Sie bei der Shopify Integration für jeden Anwendungsfall ein angepasstes Event erstellen müssen, das den Status des Abos eines Nutzers:innen in Ihrem Katalog erfasst. Für das angepasste Event benötigen Sie eine Event-Eigenschaft, die entweder der [SKU- oder der Shopify-Varianten-ID]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs#step-2-select-your-product-identifier) zugeordnet ist, die Sie im Rahmen Ihrer Shopify-Produktsynchronisierung ausgewählt haben. 

## Ändern der Katalog ID

Um den Bezeichner der Produkte in Ihrem Shopify-Katalog zu ändern, müssen Sie die Synchronisierung deaktivieren. Vergewissern Sie sich zunächst, dass Sie keine Nachrichten mehr mit diesen Shopify Katalogdaten versenden. Führen Sie die erste Synchronisierung des Shopify-Katalogs erneut durch und wählen Sie den gewünschten Bezeichner für Ihr Produkt aus, indem Sie die Schritte für [die Produktsynchronisierung](#setting-up) befolgen.

## Deaktivieren der Synchronisierung Ihrer Produkte {#deactivate}

Wenn Sie das Shopify Feature zur Produktsynchronisierung deaktivieren, werden Ihr gesamter Katalog und Ihre Produkte gelöscht. Dies kann sich auch auf alle Nachrichten auswirken, die die Daten dieses Katalogs aktiv nutzen. Vergewissern Sie sich, dass Sie diese Kampagnen oder Canvase vor der Deaktivierung entweder aktualisiert oder pausiert haben, da dies dazu führen kann, dass Nachrichten ohne Produktangaben versendet werden. Löschen Sie den Shopify-Katalog nicht direkt auf der Seite Kataloge.

## Fehlersuche
Wenn bei der Synchronisierung Ihrer Produkte in Shopify ein Fehler auftritt, kann dies auf die folgenden Fehler zurückzuführen sein. Folgen Sie den Anweisungen, um das Problem zu beheben und die Synchronisierung zu lösen:

| Fehler | Grund | Lösung |
| --- | --- | --- |
| Server Fehler | Dies tritt auf, wenn ein Server-Fehler auf Seiten von Shopify auftritt, wenn wir versuchen, Ihre Produkte zu synchronisieren. | [Deaktivieren Sie die Synchronisierung](#deactivate) und synchronisieren Sie Ihren gesamten Bestand an Produkten erneut. |
| SKU duplizieren | Dies tritt auf, wenn Sie eine SKU als ID für Ihren Katalogartikel verwenden und Produkte mit der gleichen SKU haben. Da die ID von Katalogartikeln eindeutig sein muss, müssen alle Ihre Produkte eindeutige SKUs haben. | Prüfen Sie Ihre vollständige Liste der Produkte und Varianten in Shopify, um sicherzustellen, dass es keine doppelten SKUs gibt. Wenn es doppelte SKUs gibt, aktualisieren Sie diese so, dass sie nur in Ihrem Shopify-Konto eindeutige SKUs sind. Nachdem das Problem behoben ist, [deaktivieren Sie die Synchronisierung](#deactivate) und synchronisieren Sie Ihren gesamten Bestand an Produkten erneut. |
| Kataloggrenze überschritten | Dies geschieht, wenn Sie Ihr Kataloglimit überschreiten. Braze ist nicht in der Lage, die Synchronisierung zu beenden oder aktiv zu halten, da kein Speicherplatz mehr verfügbar ist. | Es gibt zwei Lösungen für dieses Problem:<br><br>1\. Wenden Sie sich an Ihren Account Manager:in, um Ihre Stufe zu upgraden und Ihr Kataloglimit zu erhöhen. <br><br>2\. Geben Sie Speicherplatz frei, indem Sie eine der folgenden Dateien löschen:<br>\- Katalogartikel aus anderen Katalogen<br>\- Andere Kataloge<br>\- Auswahlen erstellt<br><br> Nachdem Sie eine der beiden Lösungen verwendet haben, müssen Sie die Synchronisierung deaktivieren und dann erneut synchronisieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

