{% tabs %}
{% tab Abandoned browse %}

### Verlassenes Stöbern

Verwenden Sie das Template **Abgebrochenes Stöbern**, um Nutzer:innen zu engagieren, die sich Produkte angesehen, aber nicht in den Warenkorb gelegt oder eine Bestellung aufgegeben haben.

![Ein angewandtes "Abandoned Browse" Canvas Template mit erweiterten "Eingangsregeln".]({% image_buster /assets/img_archive/abandoned_browse.png %})

#### Einrichtung

Wählen Sie auf der Seite Canvas **eine Canvas-Vorlage verwenden** > **Braze-Vorlagen** und wenden Sie dann die Vorlage **Verlassenes Durchsuchen** an. 

##### Standard Einstellungen

Die folgenden Einstellungen sind in Ihrem Canvas vorkonfiguriert:
- Grundlagen 
    - Canvas Name: **Verlassenes Stöbern**
    - Konversions-Event: `ecommerce.order placed`
        - Frist für die Konversion: 3 Tage 
- Entry-Zeitplan 
    - Aktionsbasiert, wenn ein Nutzer:innen das Ereignis `ecommerce.product_viewed` ausführt
    - Startzeitpunkt ist der Zeitpunkt, an dem Sie die Canvas-Vorlage erstellen<br><br>![„Aktionsbasierte Optionen“ für das Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br> 
- Zielgruppen 
    - Entry-Zielgruppe 
        - E-Mail **ist nicht leer**
        - Sie können die Kriterien für den Eingang der Zielgruppe auch an Ihre geschäftlichen Anforderungen anpassen
    - Eingangskontrollen
        - Nutzer:innen sind berechtigt, diesen Canvas nach Ablauf der gesamten Dauer des Canvas erneut zu betreten.
    - Ausstiegskriterien 
        - Führt `ecommerce.cart_updated`, `ecommerce.checkout_started`, oder `ecommerce.order_placed`<br><br>![Eingangskontrollen und Austrittskriterien für den Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br> 
- Einstellungen senden 
    - Nutzer:innen, die Abonnent:in sind oder ein Opt-in haben 
- Verzögerungsstufe
    - 1 Stunde Verzögerung
- Nachrichtenschritt 
    - Sehen Sie sich die E-Mail-Vorlage und den HTML-Block mit einem Liquid-Templating-Beispiel an, um Ihrer Nachricht in der vorgefertigten Vorlage Produkte hinzuzufügen. Wenn Sie Ihr eigenes Template für E-Mails verwenden, können Sie auch [Liquid-Variablen](#message-personalization) referenzieren, wie im folgenden Abschnitt gezeigt wird.

#### Personalisierung von Produkten für E-Mails (Abandoned browse) 

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

##### Produkt-URL

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

{% endtab %}
{% tab Abandoned cart %}

### Warenkorb-Abbruch

Verwenden Sie das Template **Abgebrochener Warenkorb-Abbruch**, um potenzielle entgangene Umsätze von Kunden zu decken, die Produkte in ihren Warenkorb gelegt haben, aber nicht zur Kasse gegangen sind oder eine Bestellung aufgegeben haben. 

![Ein angewandtes "Warenkorb-Abbruch" Canvas Template mit erweiterten "Eingangsregeln".]({% image_buster /assets/img_archive/abandoned_cart.png %})

#### Einrichtung

Wählen Sie auf der Canvas-Seite **Canvas-Vorlage verwenden** > **Braze-Templates** und wenden Sie dann das Template **Abgebrochener Warenkorb-Abbruch** an. 

##### Standard Einstellungen

Die folgenden Einstellungen sind in Ihrem Canvas vorkonfiguriert:
- Grundlagen 
    - Canvas Name: **Warenkorb-Abbruch**
    - Konversions-Event: `ecommerce.order_placed`
        - Frist für die Konversion: 3 Tage 
- Entry-Zeitplan 
    - Aktionsbasierter Auslöser, wenn ein Nutzer:innen das **Ereignis Warenkorb aktualisiert ausführen** auslöst (im Dropdown-Menü)
    - Startzeitpunkt ist der Zeitpunkt, an dem Sie die Canvas-Vorlage erstellen<br><br>![„Aktionsbasierte Optionen“ für das Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br> 
- Zielgruppe 
    - Entry-Zielgruppe 
        - Hat diese Apps **mehr als 0** Mal benutzt 
        - E-Mail **ist nicht leer**
    - Eingangskontrollen
        - Nutzer:innen sind sofort wieder für den Eingang in Canvas zugelassen.
    - Ausstiegskriterien 
        - Führt `ecommerce.cart_updated`, `ecommerce.checkout_started`, oder `ecommerce.order_placed`<br><br>![Eingangskontrollen und Austrittskriterien für den Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br> 
- Einstellungen senden 
    - Nutzer:innen, die Abonnent:in sind oder ein Opt-in haben 
- Verzögerungsstufe
     - 4 Stunden Verzögerung
- Nachrichtenschritt 
    - Sehen Sie sich die E-Mail-Vorlage und den HTML-Block mit einem Liquid-Templating-Beispiel an, um Ihrer Nachricht in der vorgefertigten Vorlage Produkte hinzuzufügen. Wenn Sie Ihr eigenes Template für E-Mails verwenden, können Sie auch [Liquid-Variablen](#message-personalization) referenzieren, wie im folgenden Abschnitt gezeigt wird.

#### Wie die Logik für den erneuten Eingang bei Warenkorb-Abbrüchen funktioniert

Wenn eine Nutzer:in den Bestellvorgang startet, wird ihr Warenkorb als `checkout_started`markiert. Ab diesem Zeitpunkt berechtigen weitere Updates für den Warenkorb mit derselben ID den Nutzer:in nicht mehr dazu, die Benutzerreise des Warenkorb-Abbruchs erneut zu beginnen.

1. Wenn ein Nutzer:in einen Artikel in seinen Warenkorb legt, gelangt er in den Canvas.
2. Bei jeder Hinzufügung oder Aktualisierung von Artikeln kehren sie zum Canvas zurück, um ihre Daten zum Warenkorb und ihr Messaging auf dem neuesten Stand zu halten.
3. Wenn die Nutzer:in den Bestellvorgang startet, wird ihr Warenkorb mit dem Tag `checkout_started`markiert und sie verlässt Canvas.
4. Zukünftige Updates des Warenkorbs mit derselben Warenkorb-ID triggern keinen erneuten Eingang, da dieser Warenkorb bereits in die Kasse verschoben wurde.

Wenn Nutzer:innen zur Checkout-User Journey übergehen, werden sie stattdessen vom [Canvas](#abandoned-checkout) für [abgebrochene Checkouts](#abandoned-checkout) angesprochen, der für Nutzer:innen konzipiert ist, die sich bereits weiter im Kaufprozess befinden.

#### Personalisierung von Produkten aus abgebrochenen Einkäufen für E-Mails {#abandoned-cart-checkout}

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

##### HTML-URL des Warenkorbs

Wenn Sie Nutzer:innen zurück zu ihrem Warenkorb leiten möchten, können Sie verschachtelte Event-Eigenschaften unter dem Metadatenobjekt hinzufügen, beispielsweise:

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

{% endtab %}
{% tab Abandoned checkout %}

### Abgebrochene Kasse

Verwenden Sie das **Abandoned Checkout** Template, um Kunden:in anzusprechen, die den Checkout-Prozess begonnen, aber vor dem Abschicken der Bestellung verlassen haben. 

![Ein angewandtes "Abgebrochene Kasse" Canvas Template mit erweiterten "Eingangsregeln".]({% image_buster /assets/img_archive/abandoned_checkout.png %})

#### Einrichtung

Wählen Sie auf der Canvas-Seite **Canvas-Vorlage verwenden** > **Braze-Vorlagen** und wenden Sie dann die Vorlage **Abgebrochene Kasse** an. 

##### Standard Einstellungen

Die folgenden Einstellungen sind in Ihrem Canvas vorkonfiguriert:

- Grundlagen 
    - Canvas Name: **Abgebrochene Kasse**
    - Konversions-Event: `ecommerce.order_placed`
        - Frist für die Konversion: 3 Tage 
- Entry-Zeitplan 
    - Aktionsbasierter Trigger, wenn ein Nutzer:innen das Ereignis `ecommerce.checkout_started` ausführt
    - Startzeitpunkt ist der Zeitpunkt, an dem Sie die Canvas-Vorlage erstellen<br><br>![„Aktionsbasierte Optionen“ für das Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- Zielgruppen 
    - Entry-Zielgruppe 
        - Hat diese Apps **mehr als 0** Mal benutzt 
        - E-Mail **ist nicht leer**
    - Eingangskontrollen
        - Nutzer:innen sind sofort wieder für den Eingang in Canvas zugelassen.
        - Ausstiegskriterien 
            - Führt die Ereignisse `ecommerce.order_placed` aus.<br><br>![Eingangskontrollen und Austrittskriterien für den Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- Einstellungen senden 
    - Nutzer:innen, die Abonnent:in sind oder ein Opt-in haben 
- Verzögerungsstufe
    - 4 Stunden Verzögerung
- Nachrichtenschritt 
    - Sehen Sie sich die E-Mail-Vorlage und den HTML-Block mit einem Liquid-Templating-Beispiel an, um Ihrer Nachricht in der vorgefertigten Vorlage Produkte hinzuzufügen. Wenn Sie Ihr eigenes Template für E-Mails verwenden, können Sie auch [Liquid-Variablen](#message-personalization) referenzieren, wie im folgenden Abschnitt gezeigt wird.

#### Personalisierung von E-Mails für abgebrochene Kaufabschlüsse

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

##### Kassen-URL

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

{% endtab %}
{% tab Order confirmation and feedback survey %}

### Auftragsbestätigung und Umfrage

Verwenden Sie das Template **für die Feedback-Umfrage zur &Bestellbestätigung,** um erfolgreiche Bestellungen zu bestätigen und die Kundenzufriedenheit zu steigern.

![Eine angewandte "Auftragsbestätigung" Canvas-Vorlage mit erweiterten "Eingangsregeln".]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

#### Einrichtung

Wählen Sie auf der Seite „Canvas“ **die** **Option „Canvas-Template verwenden“** > **„Braze-Vorlagen“** aus und wählen Sie anschließend die Vorlage **„Umfrage zum Feedback& zur Bestellbestätigung“** aus. 

##### Standard Einstellungen

Die folgenden Einstellungen sind in Ihrem Canvas vorkonfiguriert:

- Grundlagen 
    - Canvas Name: **Auftragsbestätigung mit Umfrage**
    - Konversions-Event: `ecommerce.session_start`
        - Frist für die Konversion: 10 Tage 
- Entry-Zeitplan 
    - Aktionsbasierter Trigger, wenn ein Nutzer:innen das Ereignis `ecommerce.cart_updated` ausführt
    - Startzeitpunkt ist der Zeitpunkt, an dem Sie die Canvas-Vorlage erstellen<br><br>![„Aktionsbasierte Optionen“ für das Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- Zielgruppen 
    - Entry-Zielgruppe 
        - Hat diese Apps **mehr als 0** Mal benutzt 
        - E-Mail **ist nicht leer**
    - Eingangskontrollen
        - Nutzer:innen sind sofort wieder für den Eingang in Canvas zugelassen.
    - Ausstiegskriterien 
        - --<br><br>![Zusätzliche Filter und Eingabekontrollen für das Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- Einstellungen senden 
    - Nutzer:innen, die Abonnent:in sind oder ein Opt-in haben 
- Nachrichtenschritt 
    - Sehen Sie sich die E-Mail-Vorlage und den HTML-Block mit einem Liquid-Templating-Beispiel an, um Ihrer Nachricht in der vorgefertigten Vorlage Produkte hinzuzufügen. Wenn Sie Ihr eigenes Template für E-Mails verwenden, können Sie auch [Liquid-Variablen](#message-personalization) referenzieren, wie im folgenden Abschnitt gezeigt wird.

#### Personalisierung der Auftragsbestätigung für E-Mails

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

##### Auftragsstatus URL

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

{% endtab %}
{% endtabs %}