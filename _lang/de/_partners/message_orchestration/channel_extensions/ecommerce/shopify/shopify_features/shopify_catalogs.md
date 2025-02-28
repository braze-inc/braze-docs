---
nav_title: Shopify Produkt-Synchronisation
article_title: Shopify Produkt-Synchronisation
alias: /shopify_catalogs/
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie Ihre Produkte aus Shopify in Braze-Kataloge importieren können."
---

# Shopify Produkt-Synchronisation 

> Sie können alle Produkte aus Ihrem Shopify-Shop mit einem [Braze-Katalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) synchronisieren, um Ihre Nachrichten besser zu personalisieren. 

Shopify-Kataloge werden nahezu in Echtzeit aktualisiert, wenn Sie Bearbeitungen und Änderungen an den Produkten in Ihrem Shopify-Shop vornehmen. Sie können Ihren abgebrochenen Einkaufswagen, Ihre Auftragsbestätigung und vieles mehr mit den aktuellsten Produktdetails und Informationen anreichern.

## Einrichten Ihrer Shopify-Produktsynchronisation {#setting-up}

Wenn Sie Ihren Shopify-Shop bereits installiert haben, können Sie Ihre Produkte dennoch synchronisieren, indem Sie die folgenden Anweisungen befolgen. 

### Schritt 1: Schalten Sie die Synchronisation ein

Sie können Ihre Produkte über den Shopify-Installationsablauf oder über die Shopify-Partnerseite mit einem Braze-Katalog synchronisieren. 

![Schritt 3 des Einrichtungsvorgangs mit "Shopify Variant ID" als "Katalog-Produktidentifikator".][1]{: style="max-width:70%;"}

Produkte, die mit einem Braze-Katalog synchronisiert werden, tragen zu Ihrem [Katalog-Limit]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits) bei.

### Schritt 2: Wählen Sie Ihren Produktidentifikator

Wählen Sie aus, welche Produktkennung als Katalog-ID verwendet werden soll:
- Shopify-Varianten-ID
- SKU

Die ID- und Kopfwerte für den von Ihnen gewählten Produktidentifikator dürfen nur Buchstaben, Zahlen, Bindestriche und Unterstriche enthalten. Wenn die Produktbezeichnung nicht diesem Format entspricht, filtert Braze sie aus Ihrer Katalogsynchronisierung heraus.

Dies ist die primäre Kennung, die Sie verwenden, um auf die Kataloginformationen von Braze zu verweisen. 

{% alert note %}
Wenn Sie SKU als Katalog-ID wählen, stellen Sie sicher, dass alle Ihre Produkte und Varianten in Ihrem Shop eine SKU haben und eindeutig sind. 
- Wenn ein Artikel eine fehlende SKU hat, kann Braze dieses Produkt nicht mit dem Katalog synchronisieren. 
- Wenn Sie mehr als ein Produkt mit der gleichen SKU haben, kann dies zu unerwartetem Verhalten führen oder dazu, dass die Produktinformationen unbeabsichtigt durch die doppelte SKU überschrieben werden.
{% endalert %}

### Schritt 3: Synchronisierung läuft

Sie erhalten eine Benachrichtigung auf dem Dashboard und Ihr Status wird als "In Bearbeitung" angezeigt, um anzuzeigen, dass die erste Synchronisierung beginnt. Beachten Sie, dass die Zeit, die für die Synchronisierung benötigt wird, davon abhängt, wie viele Produkte und Varianten Braze von Shopify synchronisieren muss. Während dieser Zeit können Sie diese Seite verlassen und auf eine Dashboard-Benachrichtigung oder eine E-Mail warten, die Sie über den Abschluss des Vorgangs informiert.

Beachten Sie, dass Braze keine weiteren Produkte mehr synchronisieren wird, wenn Ihre erste Synchronisierung Ihr [Kataloglimit]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#limits) überschreitet. Wenn Sie das Limit nach erfolgreicher Synchronisierung überschreiten, weil im Laufe der Zeit neue Produkte hinzukommen, wird die Synchronisierung nicht mehr aktiv sein. In diesen beiden Fällen werden Produktaktualisierungen von Shopify nicht mehr in Braze angezeigt. Wenden Sie sich an Ihren Kundenbetreuer, um ein Upgrade Ihrer Stufe zu erwägen. 

### Schritt 4: Synchronisierung abgeschlossen

Sie erhalten eine Benachrichtigung auf dem Dashboard und eine E-Mail, nachdem die Synchronisierung erfolgreich war. Auf der Shopify-Partnerseite wird außerdem der Status unter Shopify-Kataloge auf "Synchronisierung" aktualisiert. Sie können Ihre Produkte ansehen, indem Sie auf der Shopify-Partnerseite auf den Katalognamen klicken.

Unter [Kataloge weitere Anwendungsfälle]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases) erfahren Sie mehr darüber, wie Sie Katalogdaten zur Personalisierung Ihrer Nachricht nutzen können.

#### Unterstützte Shopify-Katalogdaten

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
Wenn Sie den Shopify-Katalog in irgendeiner Weise ändern, kann dies unbeabsichtigt die Echtzeit-Produktsynchronisierung beeinträchtigen. Nehmen Sie keine Änderungen am Shopify-Katalog vor, da diese von Shopify außer Kraft gesetzt werden könnten. Nehmen Sie stattdessen die notwendigen Produktaktualisierungen in Ihrer Shopify-Instanz vor.<br><br>Um Ihren Shopify-Katalog zu löschen, gehen Sie auf die Shopify-Seite und deaktivieren Sie die Synchronisierung. Löschen Sie den Shopify-Katalog nicht direkt auf der Seite Kataloge.
{% endalert %}

##### Verwenden Sie `product_handle` oder `product_url`

Um auf `product_handle` und `product_url` zuzugreifen und diese zu verwenden, trennen Sie Ihren Shopify-Katalog und verbinden Sie ihn erneut, indem Sie Folgendes tun.

1. Gehen Sie zur Shopify-Integrationsseite und wählen Sie **Konfiguration bearbeiten**.

![Shopify Integrationsseite.]({% image_buster /assets/img/Shopify/edit_config.png %})

{: start="2"}
2\. Schalten Sie im Schritt **Katalog synchronisieren** den Katalog aus und aktualisieren Sie dann die Einstellungen.
3\. Schalten Sie den Katalog ein und aktualisieren Sie die Einstellungen.

![Shopify Schritt "Katalog synchronisieren" mit Katalogumschaltung.]({% image_buster /assets/img/Shopify/catalog_toggle.png %})

## Back-in-Stock und Preisreduzierung als Anwendungsfälle

Um Benachrichtigungen über die Wiederverfügbarkeit von Waren einzurichten, folgen Sie bitte den Schritten [hier]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications#back-in-stock-notifications).

Um Benachrichtigungen über Preissenkungen einzurichten, folgen Sie den Schritten [hier]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/price_drop_notifications).

Beachten Sie, dass Sie mit der Shopify-Integration ein benutzerdefiniertes Ereignis erstellen müssen, das den Abonnementstatus eines Benutzers in Ihrem Katalog für jeden Anwendungsfall erfasst. Für das benutzerdefinierte Ereignis ist eine Ereigniseigenschaft erforderlich, die entweder der [SKU oder der Shopify-Varianten-ID]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs#step-2-select-your-product-identifier) entspricht, die Sie im Rahmen der Shopify-Produktsynchronisierung ausgewählt haben. 

## Ändern der Katalog-ID

Um die Produktkennung für Ihren Shopify-Katalog zu ändern, müssen Sie die Synchronisierung deaktivieren. Vergewissern Sie sich zunächst, dass Sie keine Nachrichten mehr mit diesen Shopify-Katalogdaten versenden. Führen Sie die erste Synchronisierung des Shopify-Katalogs erneut durch und wählen Sie die gewünschte Produktkennung, indem Sie die Schritte zur [Produktsynchronisierung](#setting-up) befolgen.

## Deaktivieren Sie Ihre Produktsynchronisation {#deactivate}

Wenn Sie die Shopify-Produktsynchronisierungsfunktion deaktivieren, werden Ihr gesamter Katalog und Ihre Produkte gelöscht. Dies kann sich auch auf alle Nachrichten auswirken, die aktiv die Produktdaten aus diesem Katalog verwenden. Vergewissern Sie sich, dass Sie diese Kampagnen oder Canvases vor der Deaktivierung entweder aktualisiert oder pausiert haben, da dies dazu führen könnte, dass Nachrichten ohne Produktdetails versendet werden. Löschen Sie den Shopify-Katalog nicht direkt auf der Seite Kataloge.

## Fehlersuche
Wenn Ihre Shopify-Produktsynchronisierung auf einen Fehler stößt, könnte dies an den folgenden Fehlern liegen. Folgen Sie den Anweisungen, um das Problem zu beheben und die Synchronisierung zu lösen:

| Fehler | Grund | Lösung |
| --- | --- | --- |
| Server Fehler | Dies tritt auf, wenn ein Serverfehler auf Seiten von Shopify auftritt, wenn wir versuchen, Ihre Produkte zu synchronisieren. | [Deaktivieren Sie die Synchronisierung](#deactivate) und synchronisieren Sie Ihren gesamten Produktbestand erneut. |
| SKU duplizieren | Dies tritt auf, wenn Sie eine SKU als Katalogartikel-ID verwenden und Produkte mit der gleichen SKU haben. Da die Katalogartikel-ID eindeutig sein muss, müssen alle Ihre Produkte eindeutige SKUs haben. | Prüfen Sie Ihre vollständige Liste der Produkte und Varianten in Shopify, um sicherzustellen, dass es keine doppelten SKUs gibt. Wenn es doppelte SKUs gibt, aktualisieren Sie diese so, dass sie in Ihrem Shopify-Konto nur noch eindeutige SKUs sind. Nachdem das Problem behoben ist, [deaktivieren Sie die Synchronisierung](#deactivate) und synchronisieren Sie Ihren gesamten Produktbestand erneut. |
| Kataloggrenze überschritten | Dies geschieht, wenn Sie Ihr Kataloglimit überschreiten. Braze ist nicht in der Lage, die Synchronisierung zu beenden oder aktiv zu halten, da kein Speicherplatz mehr verfügbar ist. | Es gibt zwei Lösungen für dieses Problem:<br><br>1\. Wenden Sie sich an Ihren Kundenbetreuer, um Ihre Stufe zu erhöhen und Ihr Kataloglimit zu steigern. <br><br>2\. Geben Sie Speicherplatz frei, indem Sie eine der folgenden Dateien löschen:<br>\- Katalogartikel aus anderen Katalogen<br>\- Andere Kataloge<br>\- Erstellte Auswahlen<br><br> Nachdem Sie eine der beiden Lösungen verwendet haben, müssen Sie die Synchronisierung deaktivieren und dann erneut synchronisieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

[1]: {% image_buster /assets/img/Shopify/sync_products_step1.png %}