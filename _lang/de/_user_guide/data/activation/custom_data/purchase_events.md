---
nav_title: Kauf-Events
article_title: Kauf-Events
page_order: 8
page_type: reference
description: "Dieser Referenzartikel beschreibt Kauf-Events und Kaufeigenschaften, ihre Verwendung, Segmentierung, wo Sie relevante Analytics einsehen können und vieles mehr."
search_rank: 3
---

# Kauf-Events

> Diese Seite befasst sich mit Kauf-Events und Eigenschaften, ihrer Verwendung, Segmentierung, wo Sie relevante Analytics einsehen können und mehr.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

Kauf-Events sind Kaufaktionen Ihrer Nutzer:innen und werden verwendet, um In-App-Käufe zu erfassen und den Lifetime-Value (LTV) für jedes Nutzerprofil zu ermitteln. Diese Events müssen von Ihrem Team eingerichtet werden. Die Protokollierung von Kauf-Events ermöglicht es Ihnen, Eigenschaften wie Menge und Typ hinzuzufügen, sodass Sie Ihre Nutzer:innen auf der Grundlage dieser Eigenschaften noch gezielter ansprechen können.

## Kauf-Events protokollieren

Sie können Käufe protokollieren, indem Sie ein [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/) über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) übermitteln oder eine unserer unten aufgeführten SDK-Bibliotheken verwenden.

{% alert note %}
Kauf-Event-Eigenschaften verwenden dieselben Datentypen wie [angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/#expected-format).
{% endalert %}

Im Folgenden finden Sie eine Liste der Methoden, die auf verschiedenen Plattformen zur Protokollierung von Käufen verwendet werden. Auf diesen Seiten finden Sie auch eine Dokumentation darüber, wie Sie Eigenschaften und Mengen zu Ihrem Kauf-Event hinzufügen können. Sie können Ihre Nutzer:innen auf der Grundlage dieser Eigenschaften gezielter ansprechen.

- [Android und FireOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=swift)
- [Internet]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=unity)
- [.NET MAUI (früher Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=roku)

## Kaufdaten anzeigen

Nachdem Sie Kauf-Events eingerichtet und mit der Protokollierung begonnen haben, können Sie diese Kaufdaten im Profil eines Nutzers auf dem [Tab „Übersicht"]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#overview-tab) einsehen.

## Kaufdaten verwenden

Es gibt mehrere Möglichkeiten, wie Sie Kaufdaten in Braze verwenden können:

- **[Segmentierung](#purchase-event-segmentation):** Verwenden Sie Kaufdaten, um Segmente von Nutzer:innen auf der Grundlage ihres Kaufverhaltens zu erstellen.
- **[Personalisierung](#personalization):** Verwenden Sie Kaufdaten, um Nachrichten an Nutzer:innen zu personalisieren.
- **[Nachrichten triggern](#trigger-messages):** Richten Sie Nachrichten ein, die aufgrund von Kauf-Events getriggert werden.
- **[Analytics](#analytics):** Analysieren Sie Ihre Kaufdaten, um Insights über das Verhalten der Nutzer:innen und die Effektivität Ihrer Marketingkampagnen zu erhalten.

### Segmentierung {#purchase-event-segmentation}

Sie können auf der Grundlage protokollierter Kauf-Events eine beliebige Anzahl oder Art von Folgekampagnen triggern. Sie können zum Beispiel ein Segment von Nutzer:innen erstellen, die in den letzten 30 Tagen einen Kauf getätigt haben, oder ein Segment von Nutzer:innen, die mehr als einen bestimmten Betrag ausgegeben haben.

Beim Targeting von Nutzer:innen stehen Ihnen die folgenden Filter zur Segmentierung zur Verfügung:

- Erster Kauf erfolgt
- Erster Kauf für App
- Letztes gekauftes Produkt
- Ausgegebener Betrag
- Gekauftes Produkt
- Gesamtzahl der Käufe
- X Geld ausgegeben in Y Tagen
- X Produkt gekauft in Y Tagen
- X Kauf-Eigenschaft in Y Tagen
- X Käufe in den letzten Y Tagen

Einzelheiten zu den einzelnen Filtern finden Sie im Glossar der [Segmentierungsfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) – filtern Sie dort nach „Kaufverhalten".

![Filter für Nutzer:innen, die genau drei Käufe getätigt haben]({% image_buster /assets/img/purchase_filter_example.gif %}){: style="max-width:80%;"}

{% alert tip %}
Wenn Sie nach der Häufigkeit eines bestimmten Kaufs segmentieren möchten, erfassen Sie diesen Kauf einzeln als [inkrementelles angepasstes Attribut]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage).
{% endalert %}

### Personalisierung

Wie jede andere Art von Daten, die Sie von Ihren Nutzer:innen erheben, können Sie Kaufdaten verwenden, um Ihr Messaging über Liquid zu personalisieren. Sie können zum Beispiel eine personalisierte E-Mail an Nutzer:innen senden, in der Sie Produkte empfehlen, die denen ähnlich sind, die sie gerade gekauft haben.

Angenommen, Sie verfügen über eine Kauf-Event-Eigenschaft namens `last_purchased_product`, die den Namen des zuletzt gekauften Produkts speichert. Sie können diese Eigenschaft verwenden, um eine E-Mail-Nachricht wie folgt zu personalisieren:

{% raw %}

```liquid
{% if ${last_purchased_product} == "Running Shoes" %}
  We hope you're enjoying your new running shoes! Based on your recent purchase, you might also like these running shorts and water bottles.
{% elsif ${last_purchased_product} == "Yoga Mat" %}
  We hope you're enjoying your new yoga mat! Based on your recent purchase, you might also like these yoga blocks and straps.
{% else %}
  Thank you for your recent purchase! We hope you're enjoying your new item.
{% endif %}
```

{% endraw %}

In diesem Beispiel wird die Nachricht auf der Grundlage der Eigenschaft `last_purchased_product` personalisiert. Wenn das letzte Produkt, das der/die Nutzer:in gekauft hat, „Running Shoes" war, erhält er/sie eine Nachricht, in der Laufshorts und Trinkflaschen empfohlen werden. Wenn das letzte Produkt „Yoga Mat" war, erhält er/sie eine Nachricht mit Empfehlungen für Yogablöcke und -gurte. Wenn `last_purchased_product` etwas anderes ist, wird eine allgemeine Dankesnachricht gesendet.

### Getriggerte Nachrichten

Ein häufiger Anwendungsfall ist das automatische Versenden einer Nachricht, z. B. einer E-Mail, wenn ein/e Nutzer:in einen Kauf tätigt. Sie können zum Beispiel eine Dankesnachricht oder einen Rabattcode für einen zukünftigen Einkauf versenden.

Erstellen Sie dazu eine aktionsbasierte Kampagne oder ein Canvas und setzen Sie die Aktion zum Triggern auf **Kauf tätigen**. Sie können auch zusätzliche Bedingungen für den Trigger angeben, z. B. das gekaufte Produkt oder den Kaufbetrag.

Sie können Ihre getriggerte Nachricht auch mit Liquid personalisieren. Im folgenden Beispiel ist `${purchase_product_name}` ein angepasstes Attribut, das Sie durch den tatsächlichen Attributnamen ersetzen würden, der den Namen des gekauften Produkts in Ihrem Braze-Setup speichert.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

### Analytics

Neben dem Tracking von Kaufmetriken für die Segmentierung erfasst Braze auch die Anzahl der Käufe für jedes Produkt und den im Laufe der Zeit erzielten Umsatz. Dies kann hilfreich sein, um die beliebtesten Produkte zu identifizieren oder die Auswirkungen einer Werbekampagne auf den Umsatz zu messen.

Sie finden diese Daten auf der Seite [Umsatzbericht]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

### Umsatzberechnungen

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">Lifetime-Umsatz</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Lifetime-Value pro Nutzer:in</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Durchschnittlicher Tagesumsatz</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics#daily-purchases">Tägliche Käufe</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Täglicher Umsatz pro Nutzer:in</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

#### Währungsumrechnung

Wenn Kauf-Events in einer anderen Währung als USD protokolliert werden, rechnet Braze den Betrag mithilfe der Wechselkurse von [Open Exchange Rates](http://openexchangerates.org) in USD um. Diese Kurse werden alle 24 Stunden aktualisiert. Da die Wechselkurse zwischengespeichert werden, kann es zu geringfügigen Abweichungen vom Echtzeit-Marktkurs kommen, insbesondere bei Währungen mit starken Schwankungen.

#### Berechnung des Lifetime-Umsatzes

Braze verwendet Kauf-Events, um den Lifetime-Umsatz (auch Lifetime-Value oder LTV genannt) eines Nutzers zu berechnen. Dabei handelt es sich um eine Prognose des Nettogewinns, der der gesamten zukünftigen Beziehung mit einem Kunden zugeschrieben wird. Dies kann Ihnen helfen, fundierte Entscheidungen über Strategien zur Kundengewinnung und -bindung zu treffen.

$$\text{Average purchase value} = \frac{\text{Total spend in dollars}}{\text{Total number of purchase events}}$$  

Es gibt zwei wichtige Stellen in Braze, an denen Sie den LTV Ihrer Nutzer:innen einsehen können:

- Allgemeine Metriken wie den *Lifetime-Umsatz* und den *Lifetime-Value pro Nutzer:in* für jede App und Website finden Sie in Ihrem [Umsatzbericht]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).
- Um den Lifetime-Umsatz eines bestimmten Nutzers einzusehen, schauen Sie in dessen [Nutzerprofil]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab).

##### Auswirkungen von Rückerstattungen auf den Lifetime-Umsatz

Wenn Sie Kauf-Events zum Tracking von Kaufdaten verwenden, sollten Sie Rückerstattungen erfassen, indem Sie ein Braze-Kauf-Event mit einer negativen `price`-Eigenschaft protokollieren. Auf diese Weise bleibt die Gesamtsumme für den Lifetime-Umsatz korrekt.

Beachten Sie jedoch, dass die Rückerstattung als zusätzliches Kauf-Event zählt. Betrachten wir das folgende Beispiel: Sam tätigt seinen ersten Einkauf über $12, gibt aber einen Teil davon zurück und erhält eine Rückerstattung von $5. Sams Profil würde Folgendes protokollieren:

- 1 Kauf zu einem Preis von $12
- 1 Kauf zu einem Preis von -$5
- Lifetime-Umsatz von $7

Obwohl Sam zwei Kauf-Events in seinem Profil hat, hat er in Wirklichkeit nur einen Kauf getätigt. Dies ist wichtig zu beachten, wenn Sie Segmente oder Anwendungsfälle haben, die auf der Anzahl der Käufe eines Nutzers basieren. Häufige Rückerstattungen erhöhen die Kaufanzahl im Profil der Nutzer:innen.

## Kauf-Event-Eigenschaften {#purchase-properties}

Mit Kauf-Event-Eigenschaften können Sie Eigenschaften für Käufe festlegen, die zur weiteren Qualifizierung von Trigger-Bedingungen, zur stärkeren Personalisierung des Messagings und zur Erstellung ausgefeilterer Analytics durch Rohdatenexport verwendet werden können. Die Typen der Eigenschaftswerte (String, numerisch, boolesch, Datum) variieren je nach Plattform und werden oft als Schlüssel-Wert-Paare zugewiesen.

{% alert warning %}
Die folgenden Schlüssel sind reserviert und können nicht als Namen für Kauf-Event-Eigenschaften verwendet werden: `time`, `product_id`, `quantity`, `event_name`, `price` und `currency`. Die Verwendung eines reservierten Schlüssels im Objekt `properties` gibt den Fehler „Ungültiges Feld ‚properties'" zurück.
{% endalert %}

Wenn Sie beispielsweise eine E-Commerce-Anwendung haben und einem/einer Nutzer:in nach einem Kauf eine Nachricht senden möchten, können Sie Ihre Zielgruppe zusätzlich verfeinern und eine stärkere Personalisierung der Kampagne ermöglichen, indem Sie eine Kauf-Event-Eigenschaft `brand_name` hinzufügen.

**Beispiel für das Triggern auf der Basis von Kauf-Event-Eigenschaften:**

![Einstellungen für die aktionsbasierte Zustellung, um eine Kampagne an Nutzer:innen zu senden, die Kopfhörer mit einem Markennamen gleich HeadphoneMart kaufen]({% image_buster /assets/img/purchase2.png %}){: style="max-width:80%;margin-left:15px;"}

Weitere Informationen finden Sie unter [Kauf-Details-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object).

### Segmentierung nach Event-Eigenschaften

Die Segmentierung nach Event-Eigenschaften ermöglicht es Ihnen, Nutzer:innen nicht nur anhand von angepassten Events anzusprechen, sondern auch anhand der mit diesen Events verbundenen Eigenschaften. Dies bietet zusätzliche Filteroptionen bei der Segmentierung von Kauf-Events und angepassten Events.

![Segmentierungsfilter für Kauf-Event-Eigenschaften mit Optionen zum Filtern von Nutzer:innen anhand bestimmter Event-Eigenschaftswerte, z. B. das Filtern von Nutzer:innen, die innerhalb eines festgelegten Zeitraums ein Produkt mit einer bestimmten Eigenschaft erworben haben.]({% image_buster /assets/img/purchase_event_property.png %}){: style="max-width:80%;margin-left:15px;"}

Diese Segmentierungsfilter umfassen:
- Hat das angepasste Event mit der Eigenschaft Y mit dem Wert V X-mal in den letzten Y Tagen durchgeführt
- Hat in den letzten Y Tagen X-mal einen Kauf mit der Eigenschaft Y mit dem Wert V getätigt
- Ermöglicht eine Segmentierung von 1–30 Tagen für alle Käufe, Events und Eigenschaften innerhalb von Käufen und Events

Anders als bei [Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) werden die verwendeten Segmente in Realtime aktualisiert, unterstützen eine unbegrenzte Anzahl von Segmenten, bieten einen Rückblick-Verlauf von maximal 30 Tagen und verbrauchen Datenpunkte. Aufgrund der zusätzlichen Kosten für Datenpunkte müssen Sie sich an Ihren Customer-Success-Manager von Braze wenden, um die Event-Eigenschaften für Ihre angepassten Events aktivieren zu lassen.

Nach der Genehmigung können Sie im Dashboard unter **Dateneinstellungen** > **Angepasste Events** zusätzliche Eigenschaften hinzufügen, indem Sie **Eigenschaften verwalten** auswählen. Sie können diese Event-Eigenschaften dann im Targeting-Schritt des Kampagnen- oder Canvas-Builders verwenden.

### Canvas-Eingangs-Eigenschaften und Event-Eigenschaften

{% multi_lang_include canvas_entry_event_properties.md %}

### Käufe auf Bestellebene protokollieren

Um Käufe auf Bestellebene statt auf Produktebene zu protokollieren, verwenden Sie den Bestellnamen oder die Bestellkategorie als `product_id`. Weitere Informationen finden Sie in unserer [Spezifikation für Kauf-Objekte]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions).

### Namenskonventionen für Produkt-IDs

Bei Braze bieten wir einige allgemeine Namenskonventionen für die `product_id` des Kauf-Objekts an. Bei der Wahl der `product_id` empfiehlt Braze, einfache Namen wie den Produktnamen oder die Produktkategorie (anstelle von SKUs) zu verwenden, um alle protokollierten Artikel nach dieser `product_id` zu gruppieren.

Dadurch lassen sich Produkte für die Segmentierung und das Triggern leicht identifizieren.

## Kauf-Events auf die Blockliste setzen

Es kann vorkommen, dass Sie Kauf-Events identifizieren, die entweder zu viele Datenpunkte protokollieren, für Ihre Marketingstrategie nicht mehr relevant sind oder versehentlich aufgezeichnet wurden. Um zu verhindern, dass diese Daten an Braze gesendet werden, können Sie das angepasste Datenobjekt auf eine Blockliste setzen, während Ihr Entwicklerteam daran arbeitet, es aus dem Backend Ihrer App oder Website zu entfernen.

Im Braze-Dashboard können Sie das Blocklisting unter **Dateneinstellungen** > **Produkte** verwalten. Weitere Informationen finden Sie unter [Angepasste Daten verwalten]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/).