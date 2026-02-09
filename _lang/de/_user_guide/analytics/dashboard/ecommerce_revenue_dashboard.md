---
nav_title: E-Commerce Umsatz Dashboard
article_title: E-Commerce Umsatz Dashboard
alias: "/ecommerce_revenue_dashboard/"
page_order: 6
description: "Dieser Artikel bietet eine Übersicht über das Dashboard E-Commerce Revenue - Last Touch Attribution."
---

# E-Commerce Umsatz Dashboard

> Das Dashboard **E-Commerce Revenue - Last Touch Attribution** verfolgt die Attribution von Last-Touch-Umsätzen für Kampagnen und Canvase anhand von [empfohlenen E-Commerce-Ereignissen]({{site.baseurl}}/ecommerce_events/). Nutzen Sie dieses Dashboard, um zu verstehen, welche Nachrichten den Umsatz ankurbeln und um die gesamte E-Commerce Performance im Laufe der Zeit zu überwachen.

{% alert note %}
E-Commerce empfohlene Veranstaltungen sind derzeit im frühen Zugriff. Wenden Sie sich an Ihren Customer-Success-Manager:in von Braze, wenn Sie an diesem frühzeitigen Zugang teilnehmen möchten. <br><br>Wenn Sie den neuen [Shopify Konnektor]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector) verwenden, werden diese empfohlenen Ereignisse automatisch über die Integration verfügbar sein. Andernfalls müssen diese Ereignisse implementiert werden, bevor die Daten in diesem Dashboard erscheinen.
{% endalert %}

Um Ihr Dashboard für E-Commerce-Umsätze anzuzeigen, gehen Sie zu **Analytics** > **Dashboard Builder** und wählen Sie **E-Commerce-Umsätze - Last Touch Attribution**. Dieses Dashboard berichtet über den Umsatz, der der letzten Kampagne oder dem letzten Canvas zugeschrieben wird, mit dem ein Nutzer:innen innerhalb des ausgewählten Konversionsfensters interagiert hat, bevor er eine Bestellung aufgegeben hat.

## Verfügbare Metriken

| Metrisch | Definition |
| --- | --- |
| E-Commerce-Umsatz | Gesamte Attribution des Umsatzes bei der letzten Berührung, basierend auf dem ausgewählten Datumsbereich und Konversionsfenster. |
| Täglich aufgegebene Bestellungen | Die durchschnittliche Anzahl der einzelnen Bestellungen pro Tag. |
| Durchschnittlicher Tagesumsatz im E-Commerce | Durchschnittlicher attributierter Umsatz pro Tag für den ausgewählten Zeitraum. |
| E-Commerce-Umsatz im Zeitverlauf | Eine Zeitreihe der attributierten Umsätze im ausgewählten Datumsbereich. |
| E-Commerce-Umsatz nach Kampagnen | Attributierter Umsatz aufgeschlüsselt nach Kampagnen. | 
| E-Commerce-Umsatz nach Canvas | Attributierter Umsatz aufgeschlüsselt nach Canvas. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Attribution Modell

Das **E-Commerce Revenue - Last Touch Attribution** Dashboard verwendet Last-Touch Attribution. Das bedeutet, dass der Umsatz der letzten Kampagne oder dem letzten Braze-Canvas zugerechnet wird, mit der/dem sich ein Nutzer:innen vor der Bestellung beschäftigt hat.

{% alert important %}
Nachrichten-Interaktionen müssen innerhalb des ausgewählten Konversionsfensters stattgefunden haben. Bestellungen ohne eine zulässige Nachrichten-Interaktion innerhalb des Konversionsfensters werden nicht attributiert.
{% endalert %}

## Enthaltene Daten

Das Dashboard **eCommerce Revenue - Last Touch Attribution** bezieht Daten aus empfohlenen E-Commerce-Ereignissen:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

Umsatz- und Auftragszahlen verwenden standardisierte Berechnungen von Braze.

| Metrisch | Berechnung |
| --- | --- |
| Umsatz gesamt | Summe der bestellten Werte - Summe der erstatteten Werte |
| Bestellungen gesamt | Getrennte Aufträge - Getrennte Aufträge storniert |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

### Ausgeschlossene Daten

Käufe, die über das alte Kauf-Event protokolliert wurden, sind nicht enthalten. Das **E-Commerce Revenue - Last Touch Attribution** Dashboard unterstützt derzeit keine Features, die an alte Kauf-Events gebunden sind, wie z.B. LTV oder Umsatzberichte innerhalb von Kampagnen oder Canvase. 


## Umgang mit Währungen

Alle Einnahmen werden in USD angezeigt. Nicht-USD-Währungen werden in USD umgerechnet, wobei der Wechselkurs zum Zeitpunkt der Meldung des Ereignisses verwendet wird. Um eine Konversion zu verhindern, codieren Sie die Währung beim Senden von Ereignissen fest in `USD`.
