---
nav_title: Yotpo
article_title: Yotpo
alias: /partners/yotpo/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Yotpo, einer führenden E-Commerce-Marketing-Plattform, die Tausenden von zukunftsorientierten Marken hilft, das Wachstum im Direktvertrieb zu beschleunigen."
page_type: partner
search_tag: Partner
---

# Yotpo

> [Yotpo](https://www.yotpo.com/), die führende E-Commerce-Marketing-Plattform, hilft Tausenden von zukunftsorientierten Marken, das Wachstum im Direktvertrieb zu beschleunigen. Der plattformübergreifende Ansatz von Yotpo integriert datengesteuerte Lösungen für Bewertungen, Loyalität, SMS-Marketing und vieles mehr und ermöglicht es Marken, intelligentere und konversionsstärkere Kundenerlebnisse zu schaffen.

Mit der Integration von Braze und Yotpo können Sie dynamisch Sternebewertungen, Top-Bewertungen und visuelle nutzergenerierte Inhalte (UGC) zu Produkten in E-Mails und anderen Kommunikationskanälen innerhalb von Braze abrufen und anzeigen. Sie können auch Daten zur Kundentreue in E-Mails und andere Kommunikationsmethoden einbeziehen, um eine persönlichere Interaktion zu schaffen, die den Umsatz und die Loyalität steigert.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Yotpo-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Yotpo-Konto. |
| Yotpo Bewertungen API Schlüssel | Diese API wird innerhalb des Code-Snippets Connected Content implementiert.<br><br>Weitere Informationen finden Sie unter [Finden Ihres Yotpo-App-Schlüssels und geheimen Schlüssels](https://support.yotpo.com/en/article/finding-your-yotpo-app-key-and-secret-key). |
| Yotpo Treue API Schlüssel | Dieser API-Schlüssel und die GUID werden in das Code-Snippet Connected Content implementiert.<br><br>Weitere Informationen finden Sie unter [Suche nach Ihrem Treue- und Empfehlungs-API-Schlüssel und GUID](https://support.yotpo.com/en/article/finding-your-loyalty-referrals-api-key-and-guid)|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Bevor Sie fortfahren, vergewissern Sie sich, dass die Yotpo-Produkt-ID mit der `product_id` übereinstimmt, die dynamisch von Braze abgerufen wird. Dies ist zwingend erforderlich, damit die Integration funktioniert. 

Um Ihre Yotpo-Produkt-ID zu finden, führen Sie die folgenden Schritte aus:

1. Gehen Sie auf die Website Ihres Shops.
2. Öffnen Sie die Produktseite.
3. Klicken Sie mit der rechten Maustaste und wählen Sie **Untersuchen**.
4. Drücken Sie <kbd>Strg</kbd> + <kbd>F</kbd> und suchen Sie im Code nach `yotpo-main`. Die Variable `data-product ID` und ihr Wert erscheinen im Yotpo-Div.

![Untersuchen Sie und suchen Sie nach yotpo-main, um die Variable data-product ID zu finden][1]

## Integration

Um Yotpo und Braze zu integrieren, führen Sie die folgenden Schritte aus:

1. Gehen Sie zu Ihrem Braze Dashboard.
2. Auf der Seite **Kampagnen** klicken Sie auf **Kampagne erstellen** und wählen **E-Mail**.
3. Wählen Sie Ihre bevorzugte Vorlage.
4. Klicken Sie auf **E-Mail-Text bearbeiten** und fügen Sie das entsprechende [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) Snippet für Ihren Anwendungsfall hinzu:
    - [Zeigen Sie die Sternebewertung und die Anzahl der Bewertungen eines Produkts an.](#star-review-count)
    - [Eine aktuelle 5-Sterne-Bewertung für ein Produkt anzeigen](#five-star-review)
    - [Visuellen UGC nach Produkt anzeigen](#visual-ugc)
    - [Anzeige des Treueguthabens eines Kunden in einer E-Mail](#loyalty-balance)

### Zeigen Sie die Sternebewertung und die Anzahl der Bewertungen eines Produkts an. {#star-review-count}

Verwenden Sie dieses Snippet, um die öffentliche Durchschnittsbewertung und die Anzahl der Gesamtbewertungen für ein Produkt anzugeben, das in der E-Mail enthalten ist:

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/products/<YOTPO-API-KEY>/{{event_properties.${product_id}}}/bottomline :save result %}      

{% if {{result.response.bottomline.average_score}} != 0 %}

The average rating for this product is:

{{result.response.bottomline.average_score}}/5, based on {{result.response.bottomline.total_reviews}} reviews.

{% else %}                    
{% endif %}
```
{% endraw %}

Ersetzen Sie `<YOTPO-API-KEY>` durch Ihren Yotpo-Bewertungs-API-Schlüssel. Die `product_id` wird dynamisch aus Braze gezogen. Damit die Integration funktioniert, muss die `product_id` in Braze mit der Produkt-ID in Yotpo übereinstimmen (in der Regel die übergeordnete Produkt-ID im E-Commerce).

![Ersetzen Sie YOTPO-API-KEY durch Ihren Yotpo Reviews API-Schlüssel][2]

### Eine aktuelle 5-Sterne-Bewertung für ein Produkt anzeigen {#five-star-review}

Verwenden Sie dieses Snippet, um eine Top-Rezension (veröffentlicht) für ein bestimmtes Produkt bereitzustellen, das in der E-Mail enthalten ist:

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/products/{{event_properties.${product_id}}}/reviews.json?per_page=50&star=5&sort=votes_up :save result %}

{% if {{result.response.reviews[0].score}} == 5 %}

Recent 5 Star Review for this product:

{{result.response.reviews[0].content}}

{% else %}              
{% endif %}
```
{% endraw %}

Ersetzen Sie `<YOTPO-API-KEY>` durch Ihren Yotpo-Bewertungs-API-Schlüssel. Die `product_id` wird dynamisch aus Braze gezogen. Damit die Integration funktioniert, muss die `product_id` in Braze mit der Produkt-ID in Yotpo übereinstimmen (in der Regel die übergeordnete Produkt-ID im E-Commerce).

So sieht das Snippet in Ihrem E-Mail-Editor aus:

![Beispiel für einen E-Mail-Editor, der ein Snippet für aktuelle 5-Sterne-Bewertungen anzeigt][3]

### Visuellen UGC nach Produkt anzeigen {#visual-ugc}

Verwenden Sie dieses Snippet, um getaggte und veröffentlichte Yotpo-Bilder abzurufen und sie anstelle des Stockbildes oder als zusätzliche Galerie in Ihre E-Mails einzufügen:

{% raw %}
```liquid

{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/albums/product/{{event_properties.${product_id}}}?per_page=1 :save result %}

{% if {{result.response.images[0].tagged_products[0].image_url}} != null %}

The Visual content of the product: 

<img src="{{result.response.images[0].tagged_products[0].image_url}}" border="0" width="200" height="200" alt="" />

{% else %}

Image return NULL

{% endif %}
```
{% endraw %}

Ersetzen Sie `<YOTPO-API-KEY>` durch Ihren Yotpo-Bewertungs-API-Schlüssel. Die `product_id` wird dynamisch aus Braze gezogen. Damit die Integration funktioniert, muss die `product_id` in Braze mit der Produkt-ID in Yotpo übereinstimmen (in der Regel die übergeordnete Produkt-ID im E-Commerce).

Das Snippet sieht dann etwa so aus:

![Beispiel für einen E-Mail-Editor, der einen Ausschnitt der in Yotpo veröffentlichten Bilder zeigt][4]

### Anzeige des Treueguthabens eines Kunden in einer E-Mail {#loyalty-balance}

Verwenden Sie dieses Snippet, um das Treuepunktesaldo eines Kunden abzurufen und es in Ihren E-Mail-Nachrichten zu verwenden:

{% raw %}
```liquid
{% connected_content 

https://loyalty.yotpo.com/api/v2/customers?customer_email=**{{${email_address}}}**
:method get
:headers {
    "x-guid": "<YOTPO-LOYALTY-GUID>",
    "x-api-key": "<YOTPO-LOYALTY-API-KEY>"
        }
:content_type application/json
:save publication
%}

You have {{publication.points_balance}} points

Only {{publication.vip_tier_upgrade_requirements.points_needed}} more points to become part of our VIP Tier!
```
{% endraw %}

Ersetzen Sie `<YOTPO-LOYALTY-GUID>` und `<YOTPO-LOYALTY-API-KEY>` durch Ihre Yotpo-Treueausweise. Die `email_address` wird dynamisch aus Braze gezogen. Damit die Integration funktioniert, muss es sich bei der E-Mail-Adresse um die E-Mail-Adresse des Kunden handeln, der die E-Mail erhält.

Das Snippet sieht dann etwa so aus:

![Beispiel für einen E-Mail-Editor, der einen Ausschnitt aus dem Treuekonto eines Kunden anzeigt][5]

## Häufig gestellte Fragen {#faq}

#### Was ist, wenn ich keine 5-Sterne-Bewertung habe?

Wenn Sie keine 5-Sterne-Bewertungen haben (z.B. wenn die Endpunktantwort für die 5-Sterne-Bewertung NULL zurückgibt), wird kein Inhalt angezeigt.

#### Was ist, wenn ich kein Bild für ein Produkt veröffentlicht habe?

Wenn Sie keine Bilder für ein Produkt haben (z.B. wenn die Endpunktantwort NULL für das Produktbild zurückgibt), wird kein Inhalt angezeigt.

#### Kann ich das Erscheinungsbild anpassen oder andere Datenfelder von Yotpo übernehmen?

Ja! Weitere Datenpunkte und Anpassungsoptionen finden Sie unter [API-Aufrufe tätigen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/). Möglicherweise benötigen Sie dazu die Hilfe eines Front-End-Entwicklers.

{% alert note %}
Yotpo unterstützt keine benutzerdefinierten Anforderungen, die über das hinausgehen, was in diesem Leitfaden beschrieben ist.
{% endalert %}

[1]: {% image_buster /assets/img/yotpo/image1.png %}
[2]: {% image_buster /assets/img/yotpo/image2.png %}
[3]: {% image_buster /assets/img/yotpo/image3.png %}
[4]: {% image_buster /assets/img/yotpo/image4.png %}
[5]: {% image_buster /assets/img/yotpo/image5.png %}