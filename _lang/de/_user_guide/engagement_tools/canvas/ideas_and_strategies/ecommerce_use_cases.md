---
nav_title: E-Commerce Anwendungsfälle
article_title: E-Commerce Anwendungsfälle
alias: /ecommerce_use_cases/
page_order: 4
description: "Dieser Artikel referenziert mehrere vorgefertigte Templates von Braze, die speziell auf E-Commerce Marketer zugeschnitten sind und die Umsetzung wichtiger Strategien erleichtern."
toc_headers: h2
---

# E-Commerce Anwendungsfälle

> Braze-Canvas bietet mehrere vorgefertigte Templates, die speziell auf E-Commerce Marketer zugeschnitten sind und die Umsetzung wichtiger Strategien erleichtern. Auf dieser Seite finden Sie einige wichtige Templates, die Sie verwenden können, um Ihre Customer Journey zu verbessern.

{% alert important %}
[E-Commerce empfohlene Veranstaltungen]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/) sind derzeit im frühen Zugriff. Wenden Sie sich an Ihren Customer-Success-Manager:in von Braze, wenn Sie an diesem frühzeitigen Zugang teilnehmen möchten. <br><br>Wenn Sie den neuen Shopify Konnektor verwenden, werden die empfohlenen E-Commerce-Ereignisse automatisch über die Integration verfügbar sein.
{% endalert %}

## Verwendung einer Canvas-Vorlage

So verwenden Sie eine Canvas-Vorlage:
1. Gehen Sie zu **Messaging** > **Canvas**.
2. Wählen Sie **Canvas erstellen** > **Eine Canvas-Vorlage verwenden**.
3. Suchen Sie auf dem Tab **Braze-Vorlagen** nach der gewünschten Vorlage. Sie können eine Vorschau eines Templates anzeigen, indem Sie seinen Namen auswählen.
4. Wählen Sie **Vorlage anwenden** für die Vorlage, die Sie verwenden möchten.<br><br>!["Canvas-Vorlagen" öffnete den Tab "Braze-Vorlagen" und zeigt eine Liste der zuletzt verwendeten Templates und der auswählbaren Braze-Vorlagen.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## E-Commerce Templates

- [Verlassenes Stöbern](#abandoned-browse)
- [Warenkorb-Abbruch](#abandoned-cart)
- [Abgebrochene Kasse](#abandoned-checkout)
- [Auftragsbestätigung und Umfrage](#order-confirmation--feedback-survey)

## Verlassenes Stöbern

Verwenden Sie das Template **Abgebrochenes Stöbern**, um Nutzer:innen zu engagieren, die sich Produkte angesehen, aber nicht in den Warenkorb gelegt oder eine Bestellung aufgegeben haben.

![Ein angewandtes "Abandoned Browse" Canvas Template mit erweiterten "Eingangsregeln".]({% image_buster /assets/img_archive/abandoned_browse.png %})

### Einrichtung

Wählen Sie auf der Seite Canvas **eine Canvas-Vorlage verwenden** > **Braze-Vorlagen** und wenden Sie dann die Vorlage **Verlassenes Durchsuchen** an. 

#### Standard Einstellungen

Die folgenden Einstellungen sind in Ihrem Canvas vorkonfiguriert:
- Grundlagen 
    - Canvas Name: **Verlassenes Stöbern**
    - Konversions-Event: `ecommerce.order placed`
        - Frist für die Konversion: 3 Tage 
- Entry-Zeitplan 
    - Aktionsbasiert, wenn ein Nutzer:innen das Ereignis `ecommerce.product_viewed` ausführt
    - Startzeitpunkt ist der Zeitpunkt, an dem Sie die Canvas-Vorlage erstellen<br><br>!["Aktionsbasierte Optionen" für den Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br> 
- Zielgruppen 
    - Entry-Zielgruppe 
        - E-Mail **ist nicht leer**
        - Sie können die Kriterien für den Eingang der Zielgruppe auch an Ihre geschäftlichen Anforderungen anpassen
    - Eingangskontrollen
        - Nutzer:innen sind berechtigt, diesen Canvas nach Ablauf der gesamten Dauer des Canvas erneut zu betreten.
    - Ausstiegskriterien 
        - Führt `ecommerce.cart_updated`, `ecommerce.checkout_started`, oder `ecommerce.order_placed`<br><br>![Eingangskontrollen und Ausgangskriterien für den Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br> 
- Einstellungen senden 
    - Nutzer:innen, die Abonnent:in sind oder ein Opt-in haben 
- Verzögerungsstufe
    - 1 Stunde Verzögerung
- Nachrichtenschritt 
    - Sehen Sie sich die E-Mail-Vorlage und den HTML-Block mit einem Liquid-Templating-Beispiel an, um Ihrer Nachricht in der vorgefertigten Vorlage Produkte hinzuzufügen. Wenn Sie Ihr eigenes Template für E-Mails verwenden, können Sie auch [Liquid-Variablen](#message-personalization) referenzieren, wie im folgenden Abschnitt gezeigt wird.

### Personalisierung von Produkten für E-Mails (Abandoned browse) 

Hier sehen Sie ein Beispiel dafür, wie Sie einen HTML-Produktblock für Ihre E-Mail "Abandoned Browse" hinzufügen können. 

{% raw %}
```java
<table style="width:100%">
  <tr>
    <th><img src="{{context.${image_url}}}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{context.${product_name}}}</li>
        <li>Price: ${{context.${price}}}</li>
      </ul>
    </th>
  </tr>
</table>
```
{% endraw %}

#### Produkt-URL

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

## Warenkorb-Abbruch

Verwenden Sie das Template **Abgebrochener Warenkorb-Abbruch**, um potenzielle entgangene Umsätze von Kunden zu decken, die Produkte in ihren Warenkorb gelegt haben, aber nicht zur Kasse gegangen sind oder eine Bestellung aufgegeben haben. 

![Ein angewandtes "Warenkorb-Abbruch" Canvas Template mit erweiterten "Eingangsregeln".]({% image_buster /assets/img_archive/abandoned_cart.png %})

### Einrichtung

Wählen Sie auf der Canvas-Seite **Canvas-Vorlage verwenden** > **Braze-Templates** und wenden Sie dann das Template **Abgebrochener Warenkorb-Abbruch** an. 

#### Standard Einstellungen

Die folgenden Einstellungen sind in Ihrem Canvas vorkonfiguriert:
- Grundlagen 
    - Canvas Name: **Warenkorb-Abbruch**
    - Konversions-Event: `ecommerce.order_placed`
        - Frist für die Konversion: 3 Tage 
- Entry-Zeitplan 
    - Aktionsbasierter Auslöser, wenn ein Nutzer:innen das **Ereignis Warenkorb aktualisiert ausführen** auslöst (im Dropdown-Menü)
    - Startzeitpunkt ist der Zeitpunkt, an dem Sie die Canvas-Vorlage erstellen<br><br>!["Aktionsbasierte Optionen" für den Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br> 
- Zielgruppe 
    - Entry-Zielgruppe 
        - Hat diese Apps **mehr als 0** Mal benutzt 
        - E-Mail **ist nicht leer**
    - Eingangskontrollen
        - Nutzer:innen sind sofort wieder für den Eingang in Canvas zugelassen.
    - Ausstiegskriterien 
        - Führt `ecommerce.cart_updated`, `ecommerce.checkout_started`, oder `ecommerce.order_placed`<br><br>![Eingangskontrollen und Ausgangskriterien für den Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br> 
- Einstellungen senden 
    - Nutzer:innen, die Abonnent:in sind oder ein Opt-in haben 
- Verzögerungsstufe
     - 4 Stunden Verzögerung
- Nachrichtenschritt 
    - Sehen Sie sich die E-Mail-Vorlage und den HTML-Block mit einem Liquid-Templating-Beispiel an, um Ihrer Nachricht in der vorgefertigten Vorlage Produkte hinzuzufügen. Wenn Sie Ihr eigenes Template für E-Mails verwenden, können Sie auch [Liquid-Variablen](#message-personalization) referenzieren, wie im folgenden Abschnitt gezeigt wird.

### Personalisierung von Produkten aus abgebrochenen Einkäufen für E-Mails {#abandoned-cart-checkout}

Nutzer:innen mit abgebrochenem Warenkorb benötigen einen speziellen `shopping_cart` Liquid-Tag für die Personalisierung von Produkten. 

Hier sehen Sie ein Beispiel dafür, wie Sie mit Ihrem `shopping_cart` Liquid-Tag einen HTML-Block hinzufügen, um Produkte in Ihre E-Mail aufzunehmen. 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

{% alert note %}
Wenn Sie Shopify verwenden, fügen Sie Ihren Katalognamen hinzu, um die URL der Variante zu erhalten.
{% endalert %}

#### HTML-URL des Warenkorbs

Wenn Sie Nutzer:in zurück zu ihrem Warenkorb leiten möchten, können Sie eine verschachtelte Event-Eigenschaft unter dem medata-Objekt hinzufügen, wie z.B.:

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Wenn Sie Shopify verwenden, erstellen Sie die URL Ihres Warenkorbs mit Hilfe dieses Liquid Templates:

{% raw %}
```liquid
{{context.${source}}}/checkouts/cn/{{context.${cart_id}}} 
```
{% endraw %}

## Abgebrochene Kasse

Verwenden Sie das **Abandoned Checkout** Template, um Kunden:in anzusprechen, die den Checkout-Prozess begonnen, aber vor dem Abschicken der Bestellung verlassen haben. 

![Eine angewandte "Abgebrochene Kasse"-Canvas-Vorlage mit erweiterten "Eingangsregeln".]({% image_buster /assets/img_archive/abandoned_checkout.png %})

### Einrichtung

Wählen Sie auf der Canvas-Seite **Canvas-Vorlage verwenden** > **Braze-Vorlagen** und wenden Sie dann die Vorlage **Abgebrochene Kasse** an. 

#### Standard Einstellungen

Die folgenden Einstellungen sind in Ihrem Canvas vorkonfiguriert:

- Grundlagen 
    - Canvas Name: **Abgebrochene Kasse**
    - Konversions-Event: `ecommerce.order_placed`
        - Frist für die Konversion: 3 Tage 
- Entry-Zeitplan 
    - Aktionsbasierter Trigger, wenn ein Nutzer:innen das Ereignis `ecommerce.checkout_started` ausführt
    - Startzeitpunkt ist der Zeitpunkt, an dem Sie die Canvas-Vorlage erstellen<br><br>!["Aktionsbasierte Optionen" für den Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- Zielgruppen 
    - Entry-Zielgruppe 
        - Hat diese Apps **mehr als 0** Mal benutzt 
        - E-Mail **ist nicht leer**
    - Eingangskontrollen
        - Nutzer:innen sind sofort wieder für den Eingang in Canvas zugelassen.
        - Ausstiegskriterien 
            - Führt die Ereignisse `ecommerce.order_placed` aus.<br><br>![Eingangskontrollen und Ausgangskriterien für den Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- Einstellungen senden 
    - Nutzer:innen, die Abonnent:in sind oder ein Opt-in haben 
- Verzögerungsstufe
    - 4 Stunden Verzögerung
- Nachrichtenschritt 
    - Sehen Sie sich die E-Mail-Vorlage und den HTML-Block mit einem Liquid-Templating-Beispiel an, um Ihrer Nachricht in der vorgefertigten Vorlage Produkte hinzuzufügen. Wenn Sie Ihr eigenes Template für E-Mails verwenden, können Sie auch [Liquid-Variablen](#message-personalization) referenzieren, wie im folgenden Abschnitt gezeigt wird.

### Personalisierung von E-Mails für abgebrochene Kaufabschlüsse

Nutzer:innen, die die Kasse verlassen haben, benötigen einen speziellen `shopping_cart` Liquid-Tag für die Personalisierung ihrer Produkte. 

Hier sehen Sie ein Beispiel dafür, wie Sie mit Ihrem `shopping_cart` Liquid-Tag einen HTML-Block hinzufügen, um Produkte in Ihre E-Mail aufzunehmen. 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
    {% endfor %}
</table>
```
{% endraw %}

#### Kassen-URL

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

## Auftragsbestätigung und Umfrage

Verwenden Sie die Vorlage für die **Feedback-Umfrage zur Bestellbestätigung & **, um erfolgreiche Bestellungen zu bestätigen und die Kundenzufriedenheit zu erhöhen.

![Eine angewandte "Auftragsbestätigung" Canvas-Vorlage mit erweiterten "Eingangsregeln".]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

### Einrichtung

Wählen Sie auf der Canvas-Seite **Canvas-Vorlage verwenden** > **Braze-Vorlagen** und wenden Sie dann die Vorlage für die **Umfrage zur Bestellbestätigung & ** an. 

#### Standard Einstellungen

Die folgenden Einstellungen sind in Ihrem Canvas vorkonfiguriert:

- Grundlagen 
    - Canvas Name: **Auftragsbestätigung mit Umfrage**
    - Konversions-Event: `ecommerce.session_start`
        - Frist für die Konversion: 10 Tage 
- Entry-Zeitplan 
    - Aktionsbasierter Trigger, wenn ein Nutzer:innen das Ereignis `ecommerce.cart_updated` ausführt
    - Startzeitpunkt ist der Zeitpunkt, an dem Sie die Canvas-Vorlage erstellen<br><br>!["Aktionsbasierte Optionen" für den Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- Zielgruppen 
    - Entry-Zielgruppe 
        - Hat diese Apps **mehr als 0** Mal benutzt 
        - E-Mail **ist nicht leer**
    - Eingangskontrollen
        - Nutzer:innen sind sofort wieder für den Eingang in Canvas zugelassen.
    - Ausstiegskriterien 
        - --<br><br>![Zusätzliche Filter und Eingangskontrollen für den Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- Einstellungen senden 
    - Nutzer:innen, die Abonnent:in sind oder ein Opt-in haben 
- Nachrichtenschritt 
    - Sehen Sie sich die E-Mail-Vorlage und den HTML-Block mit einem Liquid-Templating-Beispiel an, um Ihrer Nachricht in der vorgefertigten Vorlage Produkte hinzuzufügen. Wenn Sie Ihr eigenes Template für E-Mails verwenden, können Sie auch [Liquid-Variablen](#message-personalization) referenzieren, wie im folgenden Abschnitt gezeigt wird.

### Personalisierung der Auftragsbestätigung für E-Mails

Hier ist ein Beispiel dafür, wie Sie einen HTML-Produktblock in Ihre Auftragsbestätigung einfügen, nachdem eine Bestellung aufgegeben wurde.

{% raw %}
```json
<table style="width:100%">
  {% for item in {{context.${products}}} %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200" /></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{item.product_name}}</li>
        <li>Price: {{item.price}}</li>
        <li>Quantity: {{item.quantity}}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

#### Auftragsstatus URL

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

## Personalisierung von Nachrichten

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) ist eine leistungsstarke Template-Sprache, die von Braze verwendet wird und mit der Sie dynamische und personalisierte Inhalte für Ihre Kund:in erstellen können. Mit Liquid-Tags können Sie Nachrichten auf der Grundlage von Kundendaten, Produktinformationen und anderen Variablen anpassen, um das Einkaufserlebnis zu verbessern und das Engagement zu fördern.

### Wichtigste Features von Liquid

- **Dynamische Inhalte:** Fügen Sie kundenspezifische Informationen wie Namen, Bestelldetails und Präferenzen in Ihre Nachrichten ein.
- **Bedingte Logik:** Verwenden Sie if/else-Anweisungen, um anhand bestimmter Bedingungen (z.B. Standort der Kund:in und Verlauf des Einkaufs) unterschiedliche Inhalte anzuzeigen.
- **Schleifen:** Iterieren Sie über Sammlungen von Produkten oder Kundendaten, um Listen oder Raster von Artikeln anzuzeigen.

### Erste Schritte mit Liquid

Um mit der Personalisierung Ihrer Nachrichten mit Liquid-Tags zu beginnen, können Sie auf die folgenden Ressourcen referenzieren:

- [Shopify Daten]({{site.baseurl}}/shopify_features/#shopify-data) referenzieren mit vordefinierten Liquid-Tags
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## Segmentierung

Verwenden Sie Braze Segmente, um gezielte Kundensegmente auf der Grundlage bestimmter Attribute und Verhaltensweisen zu erstellen und personalisierte Messaging-Nachrichten und Kampagnen zu liefern. Mit diesem leistungsstarken Feature können Sie Ihre Kund:in effektiv einbinden, indem Sie die richtige Zielgruppe mit der richtigen Nachricht zur richtigen Zeit erreichen.

Weitere Informationen zu den ersten Schritten mit Segmenten finden Sie unter [Über Braze Segmente]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments).

### Empfohlene Ereignisse

Die E-Commerce-Ereignisse basieren auf den [empfohlenen Ereignissen]({{site.baseurl}}/recommended_events/).
Da es sich bei den empfohlenen Events um angepasste Events handelt, können Sie nach den Namen der empfohlenen E-Commerce Events suchen, indem Sie einen beliebigen [angepassten Event-Filter]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters) auswählen.

### E-Commerce Filter

Segmentieren Sie Ihre Nutzer:innen mit E-Commerce-Filtern, wie z.B. **E-Commerce-Quelle** und **Gesamtumsatz**, indem Sie den Abschnitt **E-Commerce** im Segmentierer aufrufen.

![Segmente Filter Dropdown mit "E-Commerce" Filter.]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:80%"}

{% alert important %}
Das Kauf-Event wird in Zukunft veraltet sein und durch die [im E-Commerce empfohlenen Events]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/) ersetzt werden. In diesem Fall werden die Filter für die Segmente nicht mehr unter Kaufverhalten angezeigt. Eine vollständige Liste der Kauf-Events finden Sie unter [Kauf-Events protokollieren]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

## Verschachtelte Event-Eigenschaften

Um nach verschachtelten Event-Eigenschaften zu segmentieren, können Sie [Segment-Erweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions) nutzen. Mit Segment-Erweiterungen können Sie zum Beispiel herausfinden, wer das Produkt "SKU-123" in den letzten 90 Tagen gekauft hat.

## Analytics

{% alert note %}
Zur Zeit unterstützt die Shopify Integration das Auffüllen des [Kauf-Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events) von Braze nicht. Folglich sollten Kauf-Filter, Liquid-Tags, aktionsbasierte Trigger und Analytics das Ereignis ecommerce.order_placed verwenden.
{% endalert %}

Um einen [Bericht über angepasste Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#analytics) zu erstellen, der darauf basiert, wer ein durch die Integration unterstütztes Event durchgeführt hat, können Sie den spezifischen [Eventnamen]({{site.baseurl}}/shopify_data_features/) angeben.

Um Insights über die Trends bei den Bestellungen zu erhalten, die von Ihren lancierten Canvase aus getätigt wurden, müssen Sie ein [Conversions Dashboard]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard#conversions-dashboard) einrichten und Ihre Canvase angeben.

Für fortgeschrittene Anwendungsfälle der Berichterstellung können Sie den Braze [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) verwenden, um angepasste Berichte zu erstellen. 

