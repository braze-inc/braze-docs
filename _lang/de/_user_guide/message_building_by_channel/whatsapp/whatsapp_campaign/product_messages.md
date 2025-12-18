---
nav_title: Nachrichten über Produkte
article_title: Produkt Messaging
page_order: 2
description: "Auf dieser Seite erfahren Sie, wie Sie WhatsApp Messaging verwenden können, um interaktive Nachrichten zu versenden, in denen Produkte aus Ihrem Meta-Katalog vorgestellt werden."
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
 - Campaigns
channel:
 - WhatsApp
---

# Nachrichten über Produkte

> Mit Messaging können Sie interaktive WhatsApp Nachrichten versenden, in denen Produkte direkt aus Ihrem Meta-Katalog vorgestellt werden.

Wenn Sie eine Nachricht über ein Produkt per WhatsApp an einen Nutzer:in senden, durchläuft dieser Nutzer:innen die folgende Customer Journey:

1. Der Nutzer:innen erhält Ihre Produkt- oder Katalognachricht in WhatsApp.
2. Die Nutzer:innen legen Produkte direkt über WhatsApp in ihren Warenkorb.
3. Der Nutzer:in tippt auf **Bestellung aufgeben** in WhatsApp.
4. Ihre Website oder App empfängt die Daten des Warenkorbs von Braze und generiert einen Link zur Kasse.
5. Der Nutzer:innen wird auf Ihre Website oder App weitergeleitet, um den Checkout abzuschließen.

Wenn Nutzer:innen über Nachrichten aus dem Katalog Artikel in ihren Warenkorb legen, erhält Braze Webhook-Daten für Folgeaktionen.

## Anforderungen

| Anforderung | Beschreibung |
| --- | --- |
| WhatsApp-Business-Konto | Um WhatsApp Nachrichten für Produkte zu verwenden, müssen Sie über ein WhatsApp Business-Konto verfügen, das mit Braze verbunden ist. |
| Meta-Katalog | Sie müssen einen Meta-Katalog in Ihrem Commerce Manager:in einrichten. |
| Einhaltung der Frist | Halten Sie sich an die [Meta-Commerce-Bedingungen und -Richtlinien](https://www.facebook.com/policies_center/commerce). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Arten von Nachrichten über Produkte

{% alert note %}
Verbessern Sie Ihr Messaging-Erlebnis mit dem integrierten SELEKTOR, auf den Sie in Schritt 4 von [Einrichten von Messaging-Nachrichten](#setting-up-product-messages) zugreifen können.
{% endalert %}

{% tabs local %}
{% tab Catalog messages %}

Katalog Nachrichten zeigen Ihren gesamten Produktkatalog in einem interaktiven Format an. Sie sind als [Template- und Antwort-Nachrichten](#building-a-product-message) verfügbar.

Wenn Sie bei der [Einrichtung](#setting-up-product-messages) die Katalogberechtigungen für Braze aktiviert haben, können Sie auswählen, welche Miniaturansicht für Nutzer:innen sichtbar ist. 

{% alert note %}
Sie brauchen in Braze keine zusätzliche Produktauswahl zu treffen, da die Katalogverbindung von Meta verwaltet wird und somit in Ihren Produktkatalog übernommen wird.
{% endalert %}


{% endtab %}
{% tab Multi-product messages %}

Nachrichten mit mehreren Produkten heben bestimmte Produkte aus Ihrem Katalog hervor, mit bis zu 30 hervorgehobenen Artikeln pro Nachricht. Sie sind als [Template- und Antwort-Nachrichten](#building-a-product-message) verfügbar.

Sie können die Produkte entweder manuell mit IDs auswählen oder, wenn Sie bei der [Einrichtung](#setting-up-product-messages) Katalogberechtigungen aktiviert haben, den Dropdown SELEKTOR verwenden.

{% alert important %}
Es gibt ein bekanntes Problem mit der Anzeige von Kopfzeilen bei Nachrichten-Templates für mehrere Produkte auf Meta. Meta ist sich dieses Problems bewusst und arbeitet an einer Lösung.
{% endalert %}

{% endtab %}
{% tab Single product %}

Nachrichten über einzelne Produkte heben ein bestimmtes Produkt aus Ihrem Produktkatalog hervor. Sie sind als [Nachrichten mit Antwortfunktion](#building-a-product-message) verfügbar.

Sie können die Produkte entweder manuell mit IDs auswählen oder, wenn Sie bei der [Einrichtung](#setting-up-product-messages) Katalogberechtigungen aktiviert haben, den Dropdown SELEKTOR verwenden.

{% endtab %}
{% endtabs %}

## Einrichten von Nachrichten über Produkte

1. Folgen Sie im [Meta Commerce Manager:](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#)in den [Anweisungen von Meta](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1), um Ihren Meta-Katalog zu erstellen. Vergewissern Sie sich, dass Sie sich in demselben Meta Business Portfolio befinden, in dem sich auch Ihr mit Braze verbundener WhatsApp Business Accont befindet.
2. Folgen Sie den Anweisungen von Meta, um [Ihren Meta-Katalog](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715) mit Ihrem mit Braze verbundenen WhatsApp Business Account [zu verbinden](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715), indem Sie die Berechtigung "Katalog verwalten" im Meta Business Manager zuweisen. 

![Meta-Seite "Kataloge" mit einem Pfeil, der auf den Button "Partner zuweisen" für den Katalog namens "sweeney_catalog".]({% image_buster /assets/img/whatsapp/meta_catalog.png %}){: style="max-width:90%;"}

Stellen Sie sicher, dass Sie die Braze Business Manager:in ID, `332231937299182`, als Partner Business ID verwenden.

![Fenster zur Freigabe eines Katalogs für einen Partner, das Felder zur Eingabe einer Partner Business ID enthält und die Berechtigung "Katalog verwalten" zuweist.]({% image_buster /assets/img/whatsapp/share_meta_catalog.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Wählen Sie Ihre Meta-Katalogeinstellungen aus. Sie müssen **Katalogsymbol in der Kopfzeile des Chats** auswählen, um Nachrichten aus dem Katalog zu versenden.

![WhatsApp Manager:in Einstellungsseite für den Katalog "Catalog_products".]({% image_buster /assets/img/whatsapp/meta_catalog_settings.png %}){: style="max-width:90%;"}

{: start="4"}
4\. Führen Sie in Braze den [eingebetteten Anmeldeprozess]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) durch, um Berechtigungen zu erteilen. Achten Sie darauf, dass Sie **alle** Kataloge auswählen, für die Sie Berechtigungen erteilen möchten. Dadurch wird der integrierte SELEKTOR von Braze freigeschaltet.

![Fenster mit fünf ausgewählten Katalogen bieten Berechtigungen.]({% image_buster /assets/img/whatsapp/select_catalogs.png %}){: style="max-width:50%;"}

{% alert tip %}
Die besten Vorgehensweisen für die Erstellung von Meta-Katalogen finden Sie unter [Tipps für die Erstellung eines hochwertigen Katalogs im Commerce Manager:in](https://www.facebook.com/business/help/2086567618225367?id=725943027795860).
{% endalert %}

## Erstellen einer Nachricht über ein Produkt

Sie können eine Nachricht über ein Produkt erstellen, indem Sie eine WhatsApp Template Nachricht oder eine Antwortnachricht verwenden.

{% tabs local %}
{% tab WhatsApp message template %}

1. Gehen Sie in Ihrem Meta Business Manager zu **Nachrichten Templates**.
2. Wählen Sie als Format **Katalog** aus, und wählen Sie dann zwischen einer **Nachricht aus dem Katalog** (zeigt den gesamten Katalog an) und einer **Nachricht aus dem Mehrproduktkatalog** (hebt bestimmte Artikel hervor).
3. Erstellen Sie in Braze eine WhatsApp-Kampagne oder einen Canvas-Schritt für Nachrichten.
4. Wählen Sie die Abo-Gruppe aus, die dem Ort entspricht, an dem Sie das Template eingereicht haben.
5. Wählen Sie **WhatsApp Template Nachricht**.
6. Wählen Sie das Template aus, das Sie verwenden möchten.
    - Wenn Sie eine Vorlage für mehrere Produkte auswählen, geben Sie den Titel des Abschnitts und die IDs der Produkte an, die Sie hervorheben möchten. Sie können die Content ID entweder direkt aus Ihrem Meta Commerce Manager:in übernehmen oder, wenn Sie die Berechtigungen für den integrierten SELEKTOR aktiviert haben, die Artikel auswählen.

![Artikelliste mit Feldern zur Eingabe der Titel Ihrer Abschnitte und der ID Ihrer Inhalte.]({% image_buster /assets/img/whatsapp/multi_product_template.png %}){: style="max-width:60%;"}

![Artikelliste mit Dropdown-Menü zum Auswählen von Artikeln.]({% image_buster /assets/img/whatsapp/content_id_items.png %}){: style="max-width:60%;"}

{: start="7"}
7\. Setzen Sie den Aufbau Ihrer Nachricht fort.

{% endtab %}
{% tab Response message %}

1. Erstellen Sie in Braze eine WhatsApp-Kampagne oder einen Canvas-Schritt für Nachrichten.
2. Wählen Sie eine Abo-Gruppe aus.
3. Wählen Sie **Antwort Nachricht**.
4. Wählen Sie **Meta Produkt Messages**.

Optionen zum Auswählen eines Nachrichtentyps und eines Layouts für Antwortnachrichten, wobei "Antwortnachricht" und "Meta Produkt Nachrichten" hervorgehoben sind.]({% image_buster /assets/img/whatsapp/response_message_layouts.png %}){: style="max-width:90%;"}

{: start="5"}
5\. Wählen Sie die [Art der Nachricht](#product-message-types), die Sie verwenden möchten.

![Mesage Layout Auswahl von "Multi-Produkt".]({% image_buster /assets/img/whatsapp/multi-product_message_layout.png %}){: style="max-width:90%;"}

{: start="6"}
6\. Setzen Sie den Aufbau Ihrer Nachricht fort.

![Beispiel Meta Produkt Nachricht mit ausgefüllten Informationen für Produkte.]({% image_buster /assets/img/whatsapp/example_response_message.png %}){: style="max-width:90%;"}

{% endtab %}
{% endtabs %}

## Produkte verwalten

### Zugriff auf Commerce Manager:in

Gehen Sie in Ihrem Meta Business Manager zu **Commerce Manager** und wählen Sie Ihr Unternehmen aus. Hier können Sie Ihre Katalog-Assets verwalten, wie z.B.:
- Neue Kataloge erstellen
- Produkte zu bestehenden Katalogen hinzufügen
- Update der Produktinformationen
- Ausgelaufene Artikel entfernen

{% alert important %}
Wenn Sie referenzierte Produkte aus Ihrem Katalog entfernen, werden die zugehörigen Nachrichten nicht gesendet.
{% endalert %}

## Entgegennahme eingehender Fragen zu Produkten 

Nutzer:innen können auf Ihre Nachrichten zu Produkten oder Katalogen mit Fragen zum Produkt antworten. Diese gehen als eingehende Nachrichten ein, die dann mit einem [Aktions-Pfad]({{site.baseurl}}/action_paths/) sortiert werden können. 

Außerdem extrahiert Braze die ID des Produkts und des Katalogs aus diesen Fragen. Wenn Sie also Antworten automatisieren oder Fragen an ein anderes Team (z.B. den Kundensupport) senden möchten, können Sie diese Details mit einbeziehen. Sie könnten zum Beispiel Antworten mit den WhatsApp Eigenschaften von `inbound_product_id` oder `inbound_catalog_id` personalisieren.

!["Fenster "Personalisierung hinzufügen" mit dem Personalisierungstyp "WhatsApp-Eigenschaften" und einem hervorgehobenen Attribut "inbound_product_id".]({% image_buster /assets/img/whatsapp/inbound_product_questions.png %}){: style="max-width:60%;"}

## Zur Kasse: Warenkorb-Verarbeitung und Webhooks

Wenn Nutzer:innen mit Ihren Messaging Nachrichten über Produkte interagieren, können sie diese durchsuchen und Artikel in ihren Warenkorb legen. Allerdings gibt es derzeit keine integrierte Kassenfunktion für Versandinformationen oder Zahlungsabwicklung. Stattdessen empfehlen wir Ihnen, einen Warenkorb in Ihrer eigenen App oder Website zu erstellen und die Nutzer:innen über einen angepassten Link zu diesem Warenkorb zu leiten.

### Überlegungen

- **Keine In-App-Kasse:** Nutzer:innen können Einkäufe nicht direkt in WhatsApp abschließen. Alle Transaktionen müssen auf Ihre Website oder App umgeleitet werden.
- **Angepasster Link erforderlich:** Sie müssen einen angepassten Link erstellen, der die Nutzer:innen zu ihrem Warenkorb auf Ihrer Plattform führt.
- **Manuelle Einrichtung:** Der Einrichtungsprozess erfordert eine manuelle Konfiguration Ihres Warenkorbs und Ihrer Messaging-Workflows.

{% alert note %}
Wir unterstützen derzeit keine Zahlungen, die direkt in WhatsApp stattfinden, und die zukünftige Unterstützung wird länderspezifisch sein (derzeit bietet Meta sie nur für Unternehmen an, die in Indien, Brasilien und Singapur ansässig sind und direkt mit Nutzer:innen arbeiten).
{% endalert %}

### Einrichten von Warenkorb-Ereignis-Triggern

Wenn ein Kund:in eine WhatsApp-Bestellung aufgibt, wird Braze automatisch eingeschaltet:
1. Empfängt den Inhalt des Warenkorbs von WhatsApp (Produkt IDs, Mengen und andere Daten der Bestellung).
2. Erstellen Sie ein `ecommerce.cart_update` E-Commerce Ereignis mit allen relevanten Daten, einschließlich `source = whats_app`.
3. Triggert eine Antwort, so dass Sie automatisierte Kampagnen zur Beantwortung der Bestellung einrichten können.

Das E-Commerce-Ereignis `ecommerce.cart_update` wird in Braze erst aufgelistet, nachdem ein Ereignis gesendet wurde. Dazu können Sie eine Nachricht über ein Testprodukt aus Braze erstellen und ein Warenkorb-Ereignis übermitteln.
Das Warenkorb-Ereignis umfasst:

- **Warenkorb ID:** Eindeutiger Bezeichner für den Warenkorb
- **Produkte:** Liste der Artikel mit Produkt IDs, Mengen und Preisen
- **Gesamtwert:** Summe aller Artikel
- **Währung:** Die Währung des Warenkorbs
- **Quelle:** Markiert als "whats_app"
- **Metadaten:** Zusätzliche Daten wie Katalog ID und Nachrichtentext

Weitere Informationen zu den Ereignissen im Warenkorb von Braze finden Sie unter [Arten von E-Commerce empfohlenen Ereignissen]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events).

### Einrichten einer getriggerten Reaktion

1. Erstellen Sie einen angepassten Event Trigger für `ecommerce.cart_updated`.
2. Fügen Sie einen Filter für die Eigenschaft `source = "whats_app"` hinzu.

![Canvas-Schritt für einen `ecommerce.cart_updated` angepassten Event-Trigger mit der grundlegenden Eigenschaft von "source" gleich `whats_app`.]({% image_buster /assets/img/whatsapp/product_message_canvas_step.png %})

{: start="3"}
3\. Konfigurieren Sie Folgeaktionen auf der Grundlage von Daten aus dem Warenkorb.

### Empfohlene Checkout-Implementierungen 

{% tabs local %}
{% tab Simple Liquid-based cart links %}

Verwenden Sie Liquid, um Warenkorb-URLs direkt in Ihrer Nachricht zu erstellen. Dies ist am besten, wenn Sie konsistente Produkt IDs zwischen WhatsApp und Ihrer E-Commerce Plattform haben.

#### Beispiel Liquid

{% raw %}
```liquid
{% assign cart_link = "http://alejandro-test-new.myshopify.com/cart/" %}
{% for product in event_properties.products %}
 {% assign variant_id = product.product_id %}
 {% assign quantity = product.quantity %}
 {% if forloop.first %}
   {% assign cart_link = cart_link | append: variant_id | append: ":" | append: quantity %}
 {% else %}
   {% assign cart_link = cart_link | append: "," | append: variant_id | append: ":" | append: quantity %}
 {% endif %}
{% endfor %}
{{ cart_link }}
```
{% endraw %}

#### Einrichtung

1. Erstellen Sie eine Messaging-Kampagne mit responsiven Nachrichten, die durch ein E-Commerce-Ereignis auf `ecommerce.cart_update` getriggert wird.
2. Erstellen Sie eine nachfolgende Nachricht mit der URL des Warenkorbs.
3. Erstellen Sie die URL Ihres Warenkorbs mit Liquid. Wenn Sie Shopify verwenden, können Sie [einen Warenkorb-Permalink](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks) mit dem vorherigen Beispiel Liquid [erstellen](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks).

![Diagramm, das den Checkout-Workflow für einen mit Liquid erstellten Warenkorb zeigt: Meta sendet eine Nachricht über den Eingang einer Bestellung an Braze, die einen aktionsbasierten Trigger auslöst und eine Nachricht mit einem Warenkorb-Link erstellt, der dann eine WhatsApp-Nachricht versendet.]({% image_buster /assets/img/whatsapp/liquid_generated_cart_link_checkout.png %})

{% endtab %}
{% tab Connected Content %}

Rufen Sie Ihr E-Commerce-System über eine API auf, um eine personalisierte Checkout-URL zu generieren. Dies ist die beste Lösung, wenn Sie eine dynamische URL-Generierung für den Warenkorb oder eine komplexe Abbildung der Produkte benötigen.

#### Einrichtung

1. Erstellen Sie eine Webhook-Kampagne oder einen Canvas-Schritt, der durch das [`ecommerce.cart_update`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated) eCommerce-Ereignis ausgelöst wird, der die Daten des Warenkorbs an Ihr E-Commerce-System sendet.
2. Erstellen Sie eine WhatsApp-Kampagne oder einen Canvas-Schritt, der durch dasselbe E-Commerce-Ereignis getriggert wird, um dem Nutzer:innen eine WhatsApp-Nachricht mit der URL des Warenkorbs zu senden. Folgen Sie den Anweisungen in der folgenden Nachricht, um [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) zu verwenden.

![Diagramm, das den Checkout-Workflow für einen Connected-Content-Aufruf zeigt: Meta sendet eine Nachricht über den Eingang einer Bestellung an Braze, das mit einer E-Commerce-Plattform hin und her telefoniert, und schickt dann eine WhatsApp-Nachricht.]({% image_buster /assets/img/whatsapp/connected_content_checkout.png %})

{% endtab %}
{% tab Webhook and custom events %}

Verwenden Sie Webhooks, um Daten aus dem Warenkorb an Ihr System zu senden und dann über angepasste Events Nachrichten zu triggern. Dies eignet sich am besten für komplexe Integrationen, die eine umfangreiche Bearbeitung des Warenkorbs oder mehrstufige Arbeitsabläufe erfordern.

#### Einrichtung

Erstellen Sie eine Webhook-Kampagne oder einen Canvas-Schritt, der durch das E-Commerce-Ereignis `ecommerce.cart_update` getriggert wird und der die Daten des Warenkorbs an Ihr E-Commerce-System sendet. Ihre API wird dann:
1. Daten aus dem Warenkorb empfangen
2. Erstellen Sie einen Warenkorb in Ihrem System
3. Generieren Sie die Kassen-URL
4. Senden Sie ein `checkout_started` Ereignis an Braze, das den Versand Ihrer WhatsApp Nachricht mit dem Kassenlink triggert.

![Diagramm zum Checkout-Workflow für Webhooks und angepasste Events: Meta sendet eine Nachricht über den Eingang einer Bestellung an Braze, das mit einer E-Commerce-Plattform hin- und hertelefoniert, und schickt dann eine WhatsApp-Nachricht mit der URL des Warenkorbs.]({% image_buster /assets/img/whatsapp/webhooks_custom_events_checkout.png %})

{% endtab %}
{% endtabs %}

## Prüfung und Validierung

### Anforderungen für Messaging testen

Die Funktionalität des Warenkorbs wird zwischen den Nachrichten übertragen, aber die Verarbeitung des eingehenden Ergebnisses wird nicht übertragen.

### Nachrichtenvorschau

- Produktbilder und -details werden aus Ihrem Meta-Katalog übernommen.
- Die interaktive Vorschau zeigt Platzhalter an, bis die Integration abgeschlossen ist.

### Fehlercodes 

- Wenn eine Produkt ID nicht im Katalog vorhanden ist, erhalten Sie die Fehlermeldung `product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359`.
- Wenn ein Katalog nicht mehr mit der WABA verbunden ist, erhalten Sie die Fehlermeldung `Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings`.
