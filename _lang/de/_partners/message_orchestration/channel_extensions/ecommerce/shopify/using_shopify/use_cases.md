---
nav_title: Anwendungsfälle
article_title: "Shopify Anwendungsfälle in Braze"
description: "Dieser Referenzartikel beschreibt häufige Anwendungsfälle für Einsteiger und Fortgeschrittene bei Shopify."
page_type: partner
search_tag: Partner
alias: "/shopify_use_cases/"
page_order: 2
---

# Anwendungsfälle

> Möchten Sie wissen, wie Sie Ihre Shopify-Integration nutzen können, um zeitnahe und effektive Nachrichten für Ihre Nutzer zu erstellen? Lesen Sie die folgenden Abschnitte über häufige Anwendungsfälle [für Anfänger](#beginner) und [Fortgeschrittene](#advanced), um mehr zu erfahren!

## Anfänger

Dies sind einige einfache, aber effektive Anwendungsfälle, die Sie kurz nach der Einrichtung von Shopify erstellen können. Es sind keine zusätzlichen Arbeiten erforderlich. 

### Kampagnen

Diese transaktionalen Anwendungsfälle ermöglichen es Ihnen, Ihre Benutzer zu benachrichtigen, wenn eine Aktualisierung ihrer Shopify-Bestellung vorliegt.

{% tabs local %}
{% tab Rückerstattung %}
**Shopify Rückerstattung Ereignis** - `shopify_created_refund`

Die Benutzer erhielten eine teilweise oder vollständige Rückerstattung. Diese Kampagne teilt dem Benutzer mit, dass seine Bestellung erfolgreich erstattet wurde.

![Aktionsbasierte Kampagne, die Benutzer erfasst, die das benutzerdefinierte Ereignis "shopify_created_refund" ausführen.]({% image_buster /assets/img/Shopify/refund.png %}){: style="max-width:45%;"}

**Beispiel für Nachrichtenübermittlung**

![E-Mail mit dem Text "Ihre Bestellung wurde zurückerstattet. Es tut uns leid, dass Sie von Ihrer Bestellung enttäuscht waren. Wir haben Ihre Erstattung erfolgreich abgeschickt. Bitte warten Sie 3-5 Werktage, bis der Betrag auf Ihrem Kontoauszug erscheint" und eine Schaltfläche "Konto einsehen".]({% image_buster /assets/img/Shopify/refund2.png %}){: style="max-width:80%;border:0;"}
{% endtab %}
{% tab Stornierung %}
**Shopify Stornierung Ereignis** - `shopify_cancelled_order`

Die Benutzer konnten ihre Bestellungen vor der Ausführung stornieren. Diese Kampagne teilt dem Benutzer mit, dass sein Kauf erfolgreich storniert wurde. 

![Aktionsbasierte Kampagne, die Benutzer erfasst, die das benutzerdefinierte Ereignis "shopify_cancelled_order" ausführen.]({% image_buster /assets/img/Shopify/cancellation.png %}){: style="max-width:45%;"}

**Beispiel für Nachrichtenübermittlung**

![E-Mail mit dem Text "Ihre Bestellung wurde storniert, schade, dass Sie gehen! Wir haben Ihre Bestellung erfolgreich storniert. Bitte warten Sie 3-5 Werktage, bis der Betrag auf Ihrem Kontoauszug erscheint" und eine Schaltfläche "Konto einsehen".]({% image_buster /assets/img/Shopify/cancellation2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab Erfüllte Bestellung %}
**Shopify erfüllt Veranstaltung** - `shopify_fulfilled_order`

Alle Positionen in der Bestellung eines Benutzers wurden erfolgreich erfüllt. Diese Kampagne informiert den Nutzer darüber, dass seine Bestellung vollständig erfüllt wurde.

![Aktionsbasierte Kampagne, die Benutzer erfasst, die das benutzerdefinierte Ereignis "shopify_fulfilled_order" ausführen.]({% image_buster /assets/img/Shopify/fulfilled.png %}){: style="max-width:45%;"}

**Beispiel für Nachrichtenübermittlung**

![Textnachricht mit dem Text "Ihre Bestellung wurde erfüllt! Alle Artikel in Ihrem Warenkorb wurden geliefert! Bitte gehen Sie zu Ihrem Konto und bestätigen Sie den Empfang. Bonuspunkte für das Hinterlassen von Feedback."]({% image_buster /assets/img/Shopify/fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Teilweise erfüllte Bestellung %}
**Shopify teilweise erfülltes Ereignis** - `shopify_partially_fulfilled_order`

Einige Positionen in der Bestellung eines Benutzers wurden erfolgreich erfüllt. Diese Kampagne lässt die Nutzer wissen, dass ein Teil ihrer gesamten Bestellung erfüllt wurde.

![Aktionsbasierte Kampagne, die Benutzer erfasst, die das benutzerdefinierte Ereignis "shopify_partially_fulfilled_order" ausführen.]({% image_buster /assets/img/Shopify/partially_fulfilled.png %}){: style="max-width:45%;"}

**Beispiel für Nachrichtenübermittlung**

![Textnachricht mit dem Text "Ihre Bestellung wurde teilweise erfüllt! Wir haben einen Teil der Artikel Ihrer Bestellung geliefert und der Rest ist unterwegs! Wir werden Ihnen eine weitere Benachrichtigung schicken, wenn die Lieferung vollständig abgeschlossen ist."]({% image_buster /assets/img/Shopify/partially_fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Bezahlte Bestellung %}
**Shopify Ereignis für bezahlte Bestellungen** - `shopify_paid_order`

Der Benutzer bezahlt seine Bestellung und der Status der Bestellung ändert sich in bezahlt. Diese Kampagne informiert den Benutzer darüber, dass seine Kreditkartenzahlung erfasst wurde oder die Bestellung als bezahlt markiert wurde, wenn eine manuelle Zahlung erfolgt ist.

![Aktionsbasierte Kampagne, die Benutzer erfasst, die das benutzerdefinierte Ereignis "shopify_paid_order" ausführen.]({% image_buster /assets/img/Shopify/paid.png %}){: style="max-width:45%;"}

**Beispiel für Nachrichtenübermittlung**

![E-Mail mit dem Text "Wir haben Ihre Zahlung erhalten! Juhu, Ihre Bestellung ist bezahlt! Bitte warten Sie 1-2 Werktage, bis wir die Zahlung bearbeitet und Ihre Artikel vorbereitet haben. Dann verschicken wir es!" und eine Schaltfläche "Konto anzeigen".]({% image_buster /assets/img/Shopify/paid2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% endtabs  %}
### Canvase

{% tabs local %}
{% tab Abgebrochene Kasse Canvas %}

**Abgebrochene Kasse Canvas**

Die Benutzer brechen die Kaufabwicklung ab und schließen die Transaktionen nicht ab, bevor sie die Seite verlassen. Mit diesem Canvas können Sie automatische Erinnerungen an Benutzer senden, die ihre Transaktionen nicht abgeschlossen haben, um sie wieder in den Kassenfluss zu bringen.

Aktionsbasiertes Eintrittsereignis: `shopify_abandoned_checkout`<br>
Ausnahmeereignis: `shopify_created_order` oder Kauf

![]({% image_buster /assets/img/Shopify/abandoned_checkout_canvas.gif %})

{% endtab %}
{% tab Post-Kauf Leinwand %}

**Post-Kauf Leinwand**

Der Kunde hat einen erfolgreichen Kauf getätigt, und nun möchten Sie wissen, wie ihm der Kauf gefallen hat. Mit diesem Canvas können Sie Ihren Nutzern Follow-up-Nachrichten senden, um Feedback einzuholen. 

Aktionsbasiertes Eintrittsereignis: `shopify_created_order` oder Kauf

![]({% image_buster /assets/img/Shopify/post_purchase_canvas.gif %})

{% endtab %}
{% endtabs %}

## Erweitert

Sobald Sie sich mit der Plattform vertraut gemacht haben, können Sie einige komplexere Anwendungsfälle einrichten.

### Kampagnen

{% tabs local %}
{% tab Empfehlungen der Benutzer %}
**Empfehlungen der Benutzer**
![]({% image_buster /assets/img/Shopify/product_view.png %}){: style="max-width:30%;border:0;float:right;"}

Der Benutzer hat einen Artikel angeklickt oder angesehen, ihn aber nicht gekauft. Diese Kampagne sendet dem Nutzer eine Folge-Nachricht mit den gleichen oder ähnlichen Artikeln (die von Connected Content empfohlen werden), um ihn zum Kauf eines dieser Artikel zu bewegen.

Aktionsbasiertes Eintrittsereignis: `shopify_product_clicked` oder `shopify_product_viewed`<br>
![]({% image_buster /assets/img/Shopify/product_view3.png %}){: style="max-width:45%;border:0;"}
<br><br>
Ausnahmeereignis: `shopify_created_order` oder Kauf<br>
![]({% image_buster /assets/img/Shopify/product_view2.png %}){: style="max-width:50%;"}

{% endtab %}
{% endtabs %}

### Canvas

{% tabs local %}
{% tab Rückerstattung winback Canvas %}

**Rückerstattung winback Canvas**

Die Benutzer erhielten eine teilweise oder vollständige Rückerstattung. Diese Canvas sendet Folge-Nachrichten, um den Nutzer zu einem erneuten Kauf zu bewegen.

Aktionsbasiertes Eintrittsereignis: `shopify_created_refund`<br>
Ausnahmeereignis: `shopify_created_order` oder Kauf

![]({% image_buster /assets/img/Shopify/winback_canvas_refund.gif %})


{% endtab %}
{% tab Winback Stornierung Leinwand %}

**Winback Stornierung Leinwand**

Die Benutzer konnten ihre Bestellungen vor der Ausführung stornieren. Diese Canvas sendet Folge-Nachrichten, um den Nutzer zu einem erneuten Kauf zu bewegen.

Aktionsbasiertes Eintrittsereignis: `shopify_cancelled_order`<br>
Ausnahmeereignis: `shopify_created_order` oder Kauf

![]({% image_buster /assets/img/Shopify/winback_canvas_cancel.gif %})


{% endtab %}
{% endtabs %}