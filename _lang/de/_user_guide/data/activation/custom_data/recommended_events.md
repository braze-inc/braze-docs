---
nav_title: Empfohlene Ereignisse
article_title: Empfohlene Veranstaltungen
alias: /recommended_events/
page_type: reference
description: "Dieser referenzierte Artikel beschreibt empfohlene Ereignisse, d.h. Empfehlungen von Braze für E-Commerce-Ereignisse."
---

# Empfohlene Ereignisse

> Die empfohlenen Ereignisse sind den häufigsten E-Commerce-Anwendungsfällen zugeordnet. Durch die Verwendung von empfohlenen Events können Sie vorgefertigte Canvas-Templates, Dashboards zur Berichterstellung, die an den Kundenlebenszyklus angepasst sind, und vieles mehr freischalten.

Sie können z.B. ein angepasstes Event mit dem Namen “cart_updated” oder “update_to_cart” haben, um zu erfassen, wenn ein Nutzer:in Produkte in seinem Warenkorb hinzugefügt, entfernt oder aktualisiert hat. Für empfohlene Ereignisse stellt Braze ein Template zur Verfügung, das einen definierten Namen und relevante Eigenschaften für dieses Ereignis enthält.

{% alert important %}
Empfohlene Ereignisse sind derzeit im frühen Zugriff. Wenden Sie sich an Ihren Customer-Success-Manager:in von Braze, wenn Sie an diesem frühzeitigen Zugang teilnehmen möchten. <br><br>Wenn Sie den neuen [Shopify Konnektor]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector) nutzen, werden diese empfohlenen Ereignisse automatisch über die Integration verfügbar sein.
{% endalert %}

## Funktionsweise

Braze wendet auf alle empfohlenen Ereignisse eine spezielle Validierung an, und für einige empfohlene Ereignisse gibt es spezielle Nachbearbeitungsaktionen. Für bestimmte von der Branche empfohlene Ereignisse kann Braze eine besondere Handhabung unterstützen, wie z.B. neue aktionsbasierte Auslöser für Kampagnen und Canvase.

Empfohlene Events funktionieren ähnlich wie [angepasste Events]({{site.baseurl}}/user_guide/data/custom_data/custom_events). Sie können empfohlene Ereignisse aus Currents exportieren, sie in eine Blockliste aufnehmen und für die Berichterstattung verwenden. Sie können auch Daten zum Tracking dieser Ereignisse über das [Braze SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) oder den [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) an Braze senden.

### E-Commerce empfohlene Veranstaltungen

Die [im E-Commerce empfohlenen Ereignisse]({{site.baseurl}}/ecommerce_events/) basieren auf den empfohlenen Ereignissen. Diese im E-Commerce empfohlenen Events verfolgen die Aktionen Ihrer Kund:in, wie z.B. das Betrachten eines Produkts, das Aktualisieren des Warenkorbs oder das Starten des Kassiervorgangs. 

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

#### E-Commerce Canvas Templates

In unseren speziellen [E-Commerce Anwendungsfällen]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/) finden Sie weitere Ideen, wie Sie die vorgefertigten Templates von Braze-Canvas zur Umsetzung wichtiger Strategien nutzen können.

## Häufig gestellte Fragen

### Sind empfohlene Events dasselbe wie angepasste Events?

Nein. Braze wird meinungsbildende Datenschemata für empfohlene Ereignisse definieren. Dazu gehören erforderliche und optionale Event-Eigenschaften, die in Braze einer Validierung unterzogen werden. [Angepasste Events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) sind bestimmte Aktionen oder Updates Ihrer Nutzer:innen in Ihrer App oder Website, die Sie tracken möchten. Sie können den Namen des Events anpassen und festlegen, was getrackt werden soll.

### Kann ich den Namen der empfohlenen Events anpassen?

Nein. Empfohlene Ereignisse haben standardisierte Ereignisnamen und Eigenschaften. Diese Standardisierungen tragen zur Konsistenz Ihrer Daten bei.

### Kann ich weiterhin Kauf-Events verwenden, um Einkäufe zu protokollieren?

Mit der Einführung der empfohlenen E-Commerce-Ereignisse wird Braze das alte Kauf-Event in Zukunft auslaufen lassen. Wenn Sie derzeit das Kauf-Event verwenden, erhalten Sie eine Vorankündigung zu den Abschreibungsplänen. In der Zwischenzeit können Sie die Kauf-Events bis zum offiziellen Auslaufdatum weiter verwenden.