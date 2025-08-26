---
nav_title: Anwendungsfälle
article_title: "Shopify Anwendungsfälle in Braze"
description: "Dieser referenzierte Artikel beschreibt häufige Anwendungsfälle für Anfänger und Fortgeschrittene in Shopify."
page_type: partner
search_tag: Partner
alias: "/shopify_use_cases_legacy/"
page_order: 2
---

# Anwendungsfälle

> Möchten Sie wissen, wie Sie Ihre Shopify Integration nutzen können, um zeitnahe und effektive Nachrichten für Ihre Nutzer:innen zu erstellen? Lesen Sie die folgenden Abschnitte über gängige Anwendungsfälle [für Anfänger](#beginner) und [Fortgeschrittene](#advanced), um mehr zu erfahren!

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## Anfänger

Dies sind einige einfache, aber effektive Anwendungsfälle, die Sie kurz nach der Einrichtung von Shopify erstellen können. Es sind keine zusätzlichen Arbeiten erforderlich. 

### Kampagnen

Diese Anwendungsfälle für Transaktionen erlauben es Ihnen, Ihre Nutzer:innen zu benachrichtigen, wenn es ein Update ihrer Shopify-Bestellung gibt.

{% tabs local %}
{% tab Erstattung %}
**Shopify Rückerstattung Ereignis** - `shopify_created_refund`

Die Nutzer:innen erhielten eine teilweise oder vollständige Rückerstattung. Diese Kampagne informiert die Nutzer:innen, dass ihre Bestellung erfolgreich erstattet wurde.

![Aktionsbasierte Kampagne, die Nutzer:innen erfasst, die das angepasste Event "shopify_created_refund" ausführen.]({% image_buster /assets/img/Shopify/refund.png %}){: style="max-width:45%;"}

**Beispiel für Messaging**

![E-Mail mit dem Text "Ihre Bestellung wurde zurückerstattet. Es tut uns leid, dass Sie von Ihrer Bestellung enttäuscht waren. Wir haben Ihre Rückerstattung erfolgreich abgeschickt. Bitte warten Sie 3-5 Werktage, bis der Betrag auf Ihrem Kontoauszug erscheint" und einen Button "Konto einsehen".]({% image_buster /assets/img/Shopify/refund2.png %}){: style="max-width:80%;border:0;"}
{% endtab %}
{% tab Stornierung %}
**Shopify Stornierung Ereignis** - `shopify_cancelled_order`

Nutzer:innen konnten ihre Bestellungen vor der Auslieferung stornieren. Diese Kampagne teilt dem Nutzer:innen mit, dass sein Kauf erfolgreich storniert wurde. 

![Aktionsbasierte Kampagne, die Nutzer:innen erfasst, die das angepasste Event "shopify_cancelled_order" ausführen.]({% image_buster /assets/img/Shopify/cancellation.png %}){: style="max-width:45%;"}

**Beispiel für Messaging**

![E-Mail mit dem Text "Ihre Bestellung wurde storniert, Sorry, dass Sie gehen müssen! Wir haben Ihre Bestellung erfolgreich storniert. Bitte warten Sie 3-5 Werktage, bis der Betrag auf Ihrem Kontoauszug erscheint" und einen Button "Konto einsehen".]({% image_buster /assets/img/Shopify/cancellation2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab Erfüllte Bestellung %}
**Shopify erfüllt Ereignis** - `shopify_fulfilled_order`

Alle Artikel in der Bestellung eines Nutzers:innen wurden erfolgreich erfüllt. Diese Kampagne informiert die Nutzer:innen, dass ihre Bestellung vollständig erfüllt wurde.

![Aktionsbasierte Kampagne, die Nutzer:innen erfasst, die das angepasste Event "shopify_fulfilled_order" ausführen.]({% image_buster /assets/img/Shopify/fulfilled.png %}){: style="max-width:45%;"}

**Beispiel für Messaging**

![Messaging mit dem Text "Ihre Bestellung wurde erfüllt! Alle Artikel in Ihrem Warenkorb wurden zugestellt! Bitte gehen Sie zu Ihrem Konto und bestätigen Sie den Empfang. Bonuspunkte für das Hinterlassen von Feedback."]({% image_buster /assets/img/Shopify/fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Teilweise erfüllte Bestellung %}
**Shopify teilweise erfülltes Ereignis** - `shopify_partially_fulfilled_order`

Einige Artikel in der Bestellung eines Nutzers:innen wurden erfolgreich erfüllt. Diese Kampagne lässt Nutzer:innen wissen, dass ein Teil ihrer gesamten Bestellung erfüllt wurde.

![Aktionsbasierte Kampagne, die Nutzer:innen erfasst, die das angepasste Event "shopify_partially_fulfilled_order" ausführen.]({% image_buster /assets/img/Shopify/partially_fulfilled.png %}){: style="max-width:45%;"}

**Beispiel für Messaging**

![Messaging mit dem Text "Ihre Bestellung wurde teilweise erfüllt! Wir haben einige Artikel Ihrer Bestellung zugestellt und der Rest ist auf dem Weg! Wir werden Ihnen eine weitere Benachrichtigung schicken, wenn die Zustellung vollständig abgeschlossen ist."]({% image_buster /assets/img/Shopify/partially_fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Bezahlte Bestellung %}
**Shopify Ereignis für bezahlte Bestellungen** - `shopify_paid_order`

Nutzer:innen zahlen für ihre Bestellung, und der Bestellstatus ändert sich in bezahlt. Diese Kampagne informiert die Nutzer:innen darüber, dass ihre Kreditkartenzahlung erfasst wurde oder dass die Bestellung als bezahlt markiert wurde, wenn eine manuelle Zahlung erfolgt ist.

![Aktionsbasierte Kampagne, die Nutzer:innen erfasst, die das angepasste Event "shopify_paid_order" ausführen.]({% image_buster /assets/img/Shopify/paid.png %}){: style="max-width:45%;"}

**Beispiel für Messaging**

![E-Mail mit dem Text "Wir haben Ihre Zahlung erhalten! Juhu, Ihre Bestellung ist bezahlt! Bitte warten Sie 1-2 Werktage, bis wir die Zahlung bearbeitet und Ihre Artikel vorbereitet haben. Dann verschicken wir es!" und einen Button "Konto ansehen".]({% image_buster /assets/img/Shopify/paid2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% endtabs  %}
### Canvase

{% tabs local %}
{% tab Verlassene Kasse Canvas %}

**Verlassene Kasse Canvas**

Nutzer:innen brechen den Bestellvorgang ab und schließen Transaktionen nicht ab, bevor sie das Geschäft verlassen. Mit diesem Canvas können Sie automatische Erinnerungen an Nutzer:innen senden, die ihre Transaktionen noch nicht abgeschlossen haben, um sie wieder in den Checkout-Prozess zu bringen.

Aktionsbasiertes Eingangsereignis: `shopify_abandoned_checkout`<br>
Ausnahme-Event: `shopify_created_order` oder Kauf

![]({% image_buster /assets/img/Shopify/abandoned_checkout_canvas.gif %})

{% endtab %}
{% tab Canvas nach dem Kauf %}

**Canvas nach dem Kauf**

Nutzer:innen haben erfolgreich eingekauft, und jetzt möchten Sie wissen, wie ihnen der Kauf gefallen hat. Mit diesem Canvas können Sie Nachrichten an Ihre Nutzer:innen senden, um Feedback einzuholen. 

Aktionsbasiertes Eingangs-Event: `shopify_created_order` oder Kauf-Event

![]({% image_buster /assets/img/Shopify/post_purchase_canvas.gif %})

{% endtab %}
{% endtabs %}

## Erweitert

Sobald Sie sich mit der Plattform vertraut gemacht haben, können Sie einige komplexere Anwendungsfälle einrichten.

### Kampagnen

{% tabs local %}
{% tab Nutzer:in Empfehlungen %}
**Nutzer:in Empfehlungen**
![]({% image_buster /assets/img/Shopify/product_view.png %}){: style="max-width:30%;border:0;float:right;"}

Nutzer:innen haben einen Artikel angeklickt oder angesehen, aber nicht gekauft. Diese Kampagne sendet dem Nutzer:innen eine Nachricht mit den gleichen oder ähnlichen Artikeln (empfohlen von Connected-Content), um ihn zum Kauf eines dieser Artikel zu bewegen.

Aktionsbasiertes Eingangsereignis: `shopify_product_clicked` oder `shopify_product_viewed`<br>
![]({% image_buster /assets/img/Shopify/product_view3.png %}){: style="max-width:45%;border:0;"}
<br><br>
Ausnahme-Event: `shopify_created_order` oder Kauf<br>
![]({% image_buster /assets/img/Shopify/product_view2.png %}){: style="max-width:50%;"}

{% endtab %}
{% endtabs %}

### Canvas

{% tabs local %}
{% tab Rückerstattung winback Canvas %}

**Rückerstattung winback Canvas**

Die Nutzer:innen erhielten eine teilweise oder vollständige Rückerstattung. Dieses Canvas sendet Nachrichten, um den Nutzer:innen zu einem erneuten Kauf zu bewegen.

Aktionsbasiertes Eingangsereignis: `shopify_created_refund`<br>
Ausnahme-Event: `shopify_created_order` oder Kauf

![]({% image_buster /assets/img/Shopify/winback_canvas_refund.gif %})


{% endtab %}
{% tab Winback Stornierung Canvas %}

**Winback Stornierung Canvas**

Nutzer:innen konnten ihre Bestellungen vor der Auslieferung stornieren. Dieses Canvas sendet Nachrichten, um den Nutzer:innen zu einem erneuten Kauf zu bewegen.

Aktionsbasiertes Eingangsereignis: `shopify_cancelled_order`<br>
Ausnahme-Event: `shopify_created_order` oder Kauf

![]({% image_buster /assets/img/Shopify/winback_canvas_cancel.gif %})


{% endtab %}
{% endtabs %}