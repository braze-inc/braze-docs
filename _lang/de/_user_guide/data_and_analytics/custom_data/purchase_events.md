---
nav_title: Kauf-Events
article_title: Kauf-Events
page_order: 8
page_type: reference
description: "Dieser Referenzartikel beschreibt Kauf-Events und Kaufeigenschaften, ihre Verwendung, Segmentierung, wo Sie relevante Analysen einsehen können und vieles mehr."
search_rank: 3
---

# Kauf-Events

> Erfahren Sie mehr über Kaufereignisse und -eigenschaften, ihre Verwendung, Segmentierung, wo Sie relevante Analysen einsehen können und vieles mehr.

Kaufereignisse sind Kaufaktionen, die von Ihren Benutzern durchgeführt werden. Diese Ereignisse werden verwendet, um In-App-Käufe zu erfassen und den Lifetime Value (LTV) für jedes Benutzerprofil zu ermitteln. Diese Kauf-Events müssen von Ihrem Team eingerichtet werden. Die Protokollierung von Kaufereignissen ermöglicht es Ihnen, Eigenschaften wie Menge und Typ hinzuzufügen, so dass Sie Ihre Nutzer anhand dieser Eigenschaften noch gezielter ansprechen können.

## Kauf-Ereignisse protokollieren

Sie können Einkäufe protokollieren, indem Sie ein [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/) über den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) übergeben.

Im Folgenden finden Sie eine Liste der Methoden, die auf verschiedenen Plattformen zur Protokollierung von Einkäufen verwendet werden. Auf diesen Seiten finden Sie auch eine Dokumentation darüber, wie Sie Ihrem Kaufereignis Eigenschaften und Mengen hinzufügen können. Anhand dieser Eigenschaften können Sie Ihre Nutzer weiter ansprechen.

- [Android und FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/)
- [Internet]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_purchases/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/)

## Anzeigen von Kaufdaten

Nachdem Sie Kauf-Events eingerichtet und mit der Protokollierung begonnen haben, können Sie diese Daten im Profil eines Nutzers auf dem [Tab Übersicht]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#overview-tab) einsehen.

## Verwendung von Kaufdaten

Es gibt mehrere Möglichkeiten, wie Sie Kaufdaten in Braze verwenden können:

- **[Segmentierung](#purchase-event-segmentation):** Verwenden Sie Kaufdaten, um Segmente von Nutzer:innen auf der Grundlage ihres Kaufverhaltens zu erstellen.
- **[Personalisierung](#personalization):** Verwenden Sie Kaufdaten, um Nachrichten an Nutzer:innen zu personalisieren.
- **[Nachrichten triggern](#trigger-messages):** Richten Sie Nachrichten ein, die aufgrund von Kauf-Events getriggert werden.
- **[Analytics](#analytics):** Analysieren Sie Ihre Kaufdaten, um Insights über das Nutzer:innen-Verhalten und die Effektivität Ihrer Kampagnen zu erhalten.

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
- X in Y Tagen gekauftes Produkt
- X Eigenschaft in Y Tagen kaufen
- X Käufe in den letzten Y Tagen

Einzelheiten zu den einzelnen Filtern finden Sie im Glossar der [Segmentierungsfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) und in der Filterung nach "Kaufverhalten".

![Filter für Nutzer:innen, die genau drei Käufe getätigt haben][1]{: style="max-width:80%;"}

{% alert tip %}
Wenn Sie nach der Häufigkeit eines bestimmten Kaufs segmentieren möchten, sollten Sie diesen Kauf einzeln als [inkrementelles angepasstes Attribut]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage) erfassen.
{% endalert %}

### Personalisierung

Wie jede andere Art von Daten, die Sie von Ihren Nutzer:innen erheben, können Sie Kaufdaten verwenden, um Ihr Messaging über Liquid zu personalisieren. Sie können zum Beispiel eine personalisierte E-Mail an einen Nutzer:innen senden, in der Sie Produkte empfehlen, die denen ähnlich sind, die er gerade gekauft hat.

Nehmen wir an, Sie haben eine Kauf-Event-Eigenschaft namens `last_purchased_product`, die den Namen des letzten Produkts speichert, das ein Nutzer:in gekauft hat. Sie können diese Eigenschaft verwenden, um eine E-Mail-Nachricht wie diese zu personalisieren:

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

In diesem Beispiel wird die Nachricht auf der Grundlage der Eigenschaft `last_purchased_product` personalisiert. Wenn das letzte Produkt, das der Nutzer:innen gekauft hat, "Laufschuhe" war, erhält er eine Nachricht, in der Laufshorts und Trinkflaschen empfohlen werden. Wenn das letzte Produkt eine "Yogamatte" war, erhalten sie eine Nachricht, in der Yoga-Blöcke und -Gurte empfohlen werden. Wenn die Nachricht `last_purchased_product` etwas anderes ist, erhalten sie eine allgemeine Dankesnachricht.

### Getriggerte Nachrichten

Ein häufiger Anwendungsfall ist das automatische Versenden einer Nachricht, z.B. einer E-Mail, wenn ein Nutzer:innen einen Kauf tätigt. Sie können zum Beispiel eine Nachricht als Dankeschön oder einen Rabattcode für einen zukünftigen Einkauf versenden.

Erstellen Sie dazu eine aktionsbasierte Kampagne oder ein Canvas und setzen Sie die triggernde Aktion auf **Kauf tätigen**. Sie können auch zusätzliche Bedingungen für den Trigger angeben, z. B. das gekaufte Produkt oder den Kaufbetrag.

Sie können Ihre getriggerte Nachricht mit Liquid auch personalisieren.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

In diesem Beispiel ist `${purchase_product_name}` ein benutzerdefiniertes Attribut, das Sie durch den tatsächlichen Attributnamen ersetzen würden, der den Namen des gekauften Produkts in Ihrer Braze-Einrichtung speichert.

### Analytics

Neben dem Tracking der Metriken für die Segmentierung notiert Braze auch die Anzahl der Käufe für jedes Produkt und den im Laufe der Zeit erzielten Umsatz. Dies kann hilfreich sein, um zu sehen, welche Produkte am beliebtesten sind oder um die Auswirkungen einer Werbekampagne auf den Umsatz zu messen.

Sie können diese Daten auf der Seite [Einnahmebericht]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) einsehen.

### Die Umsatzberechnung

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrisch</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">Lifetime-Umsatz</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Lifetime-Value je Benutzer</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Durchschnittlicher Tagesumsatz</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics#daily-purchases">Tagesabsatz</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Täglicher Umsatz pro Nutzer:in</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

#### Berechnung des Lifetime-Umsatzes

Braze verwendet Kauf-Events, um den Lifetime-Umsatz (auch Lifetime-Value oder LTV genannt) eines Benutzers zu berechnen. Dabei handelt es sich um eine Prognose des Nettogewinns, der der gesamten zukünftigen Beziehung mit einem Kunden zugeschrieben wird. Dies kann Ihnen helfen, fundierte Entscheidungen über Strategien zur Kundengewinnung und -bindung zu treffen.

$$\text{Average purchase value} = \frac{\text{Total spend in dollars}}{\text{Total number of purchase events}}$$  

Es gibt zwei wichtige Stellen in Braze, auf die Sie referenzieren können, um den LTV Ihrer Nutzer:innen zu verstehen:

- Allgemeine Metriken wie den *Lifetime-Umsatz* und den *Lifetime-Value pro Nutzer*:innen für jede App und Website finden Sie in Ihrem [Umsatzbericht]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).
- Um den Lifetime-Umsatz eines oder einer bestimmten Nutzers oder Nutzerin zu verstehen, verweisen Sie auf dessen oder deren [Nutzerprofil]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab).

##### Auswirkungen von Erstattungen auf den Lifetime-Umsatz

Wenn Sie Kauf-Events zum Tracking von Daten verwenden, sollten Sie Rückerstattungen verfolgen, indem Sie ein Kauf-Event von Braze mit einer negativen `price`-Eigenschaft protokollieren. Auf diese Weise erhalten Sie eine genaue Summe für den Lifetime-Umsatz.

Beachten Sie jedoch, dass die Rückerstattung als zusätzliches Kaufereignis zählt. Betrachten wir das folgende Beispiel. Sam kauft zum ersten Mal für $12 ein, gibt aber einen Teil des Einkaufs zurück und erhält dafür eine Rückerstattung von $5. Das Profil von Sam würde protokolliert:

- 1 Kauf zu einem Preis von $12
- 1 Kauf zu einem Preis von -$5
- Lifetime-Umsatz von $7

Während Sam zwei Kauf-Events in seinem Profil hat, hat er in Wirklichkeit nur einen Kauf getätigt. Dies ist wichtig, wenn Sie Segmente oder Anwendungsfälle haben, die sich auf die Anzahl der Einkäufe eines Nutzer:innen beziehen. Ständige Erstattungen erhöhen die Anzahl der Käufe im Profil der Nutzer:innen.

## Kauf-Event-Eigenschaften {#purchase-properties}

Mit den Kauf-Event-Eigenschaften können Sie Eigenschaften für Einkäufe festlegen, die zur weiteren Qualifizierung von Trigger-Bedingungen, zur stärkeren Personalisierung des Messagings und zur Erstellung ausgefeilterer Analytics durch Rohdatenexport verwendet werden können. Die Typen der Eigenschaftswerte (String, numerisch, boolesch, Datum) variieren je nach Plattform und werden oft als Schlüssel-Wert-Paare zugewiesen.

Wenn beispielsweise eine E-Commerce-Anwendung nach einem Kauf eine Nachricht an einen Benutzer senden möchte, könnte sie ihre Zielgruppe zusätzlich verbessern und eine stärkere Personalisierung der Kampagne ermöglichen, indem sie eine Kaufereigniseigenschaft von `brand_name` hinzufügt.

**Beispiel für das Triggern auf der Basis von Kauf-Event-Eigenschaften:**

![Einstellungen für die aktionsbasierte Zustellung, um eine Kampagne an Nutzer:innen zu senden, die Kopfhörer mit einem Markennamen wie HeadphoneMart kaufen][2]{: style="max-width:80%;margin-left:15px;"}

Weitere Informationen finden Sie unter [Kauf-Details-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object).

### Segmentierung der Eigenschaften von Ereignissen

Die Segmentierung von Event-Eigenschaften ermöglicht Ihnen das Targeting von Nutzern:innen nicht nur auf der Grundlage angepasster Events, sondern auch auf der Grundlage der Eigenschaften, die mit diesen Events verbunden sind. Dieses Feature bietet zusätzliche Filteroptionen bei der Segmentierung von Kauf-Events und angepassten Events.

![][6]{: style="max-width:80%;margin-left:15px;"}

Diese Segmentierungsfilter umfassen:
- Hat das benutzerdefinierte Ereignis mit der Eigenschaft Y mit dem Wert V in den letzten Y Tagen X Mal ausgeführt.
- Hat in den letzten Y Tagen X-mal Käufe mit Eigentum Y im Wert von V getätigt.
- Fügt die Möglichkeit hinzu, innerhalb von 1, 3, 7, 14, 21 und 30 Tagen zu segmentieren.

Anders als bei [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) werden die verwendeten Segmente in Echtzeit aktualisiert, unterstützen eine unbegrenzte Anzahl von Segmenten, bieten einen Rückblick von maximal 30 Tagen und verursachen Datenpunkte. Aufgrund der zusätzlichen Kosten für Datenpunkte müssen Sie sich an Ihren Customer-Success-Manager von Braze wenden, um die Event-Eigenschaften für Ihre angepassten Events zu aktivieren.

Nach der Genehmigung können Sie im Dashboard unter **Dateneinstellungen** > **Benutzerdefinierte Ereignisse** zusätzliche Eigenschaften hinzufügen, indem Sie auf **Eigenschaften verwalten** klicken. Sie können diese Event-Eigenschaften dann im Targeting-Schritt der Kampagne oder des Canvas-Erstellers verwenden.

### Canvas-Eingangs-Eigenschaften und Event-Eigenschaften

{% alert important %}
Ab dem 28\. Februar 2023 können Sie keine Canvase mehr mit dem Original-Editor erstellen oder duplizieren. Dieser Abschnitt steht als Referenz zur Verfügung, wenn Sie `canvas_entry_properties` und `event_properties` für den ursprünglichen Canvas-Workflow verwenden.
{% endalert %}

Sie können `canvas_entry_properties` und `event_properties` für Ihre Nutzer:innen in Canvas nutzen. Weitere Informationen und Beispiele finden Sie unter [Canvas-Eingabeeigenschaften und Ereigniseigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/).

{% alert important %}
Sie können `event_properties` nicht für den Lead-Nachrichtenschritt verwenden. Stattdessen müssen Sie `canvas_entry_properties` verwenden oder einen Aktionspfadschritt mit dem entsprechenden Event **vor dem** Nachrichtenschritt hinzufügen, der `event_properties` enthält.
{% endalert %}

{% tabs local %}
{% tab Canvas-Entry-Eigenschaften %}

[Canvas-Entry-Eigenschaften]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) sind Eigenschaften für Canvase, die durch Aktionen oder die API getriggert werden. Beachten Sie, dass das Objekt `canvas_entry_properties` maximal 50 KB groß sein darf.

{% alert important %}
Insbesondere bei In-App-Nachrichtenkanälen kann `canvas_entry_properties` nur dann in Canvas Flow und dem ursprünglichen Canvas-Editor referenziert werden, wenn Sie in der Early-Access-Phase persistente Entry-Eigenschaften aktiviert haben.
{% endalert %}

Für Canvas Flow-Messaging kann `canvas_entry_properties` in Liquid in jedem Nachrichtenschritt verwendet werden. Verwenden Sie dieses Liquid, wenn Sie auf diese Eigenschaften verweisen: ``{% raw %} canvas_entry_properties${property_name} {% endraw %}``. Beachten Sie, dass es sich bei den Events um angepasste Events oder Kauf-Events handeln muss, um auf diese Weise verwendet werden zu können. 

{% raw %}
Nehmen wir zum Beispiel die folgende Anfrage: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Sie können einer Nachricht mit dem Liquid `{{canvas_entry_properties.${product_name}}}` das Wort „Schuhe“ hinzufügen.
{% endraw %}

Bei den Canvase, die mit dem Original-Editor erstellt wurden, kann `canvas_entry_properties` nur im ersten vollständigen Schritt eines Canvas referenziert werden.

{% endtab %}

{% tab Event-Eigenschaften %}
Event-Eigenschaften referenzieren auf die Eigenschaften, die Sie für angepasste Events und Käufe festlegen. Diese `event_properties` können in Kampagnen mit aktionsbasierter Lieferung und Canvases verwendet werden.

In Canvas Flow können angepasste Event- und Kaufevent-Eigenschaften in Liquid in jedem Nachrichtenschritt verwendet werden, der auf einen Aktionspfadschritt folgt. Für Canvas Flow sollten Sie {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} verwenden, wenn Sie auf diese `event_properties` verweisen. DiDiese Events müssen angepasste Events oder Kauf-Events sein, um auf diese Weise in der Komponente „Nachricht“ verwendet werden zu können.

Im ursprünglichen Canvas-Editor kann `event_properties` nicht in geplanten vollständigen Schritten verwendet werden. Sie können jedoch `event_properties` im ersten vollständigen Schritt aktionsbasierter Canvase verwenden, auch wenn ein vollständiger Schritt geplant ist.

Im ersten Nachrichten-Schritt, der einem Aktionspfad folgt, können Sie `event_properties` verwenden, das sich auf das Event bezieht, das in diesem Aktionspfad referenziert wird. Diese `event_properties` können nur verwendet werden, wenn der Nutzer:in tatsächlich die Aktion durchgeführt hat (und nicht in die Gruppe Alle anderen gegangen ist). Zwischen diesem Aktionspfad und dem Nachrichtenschritt können Sie weitere Schritte einfügen (die selbst keine Aktionspfade oder Nachrichtenschritte sind).

{% endtab %}
{% endtabs %}

### Käufe auf der Ebene der Bestellung protokollieren
Wenn Sie Einkäufe auf der Bestellebene statt auf der Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Spezifikation für Kaufobjekte]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

## Setzen von Kauf-Events auf die Blockliste

Gelegentlich werden Sie Kauf-Events identifizieren, die entweder zu viele Datenpunkte verbrauchen, für Ihre Marketing Strategie nicht mehr nützlich sind oder irrtümlich aufgezeichnet wurden. Um zu verhindern, dass diese Daten an Braze gesendet werden, können Sie das angepasste Datenobjekt auf eine Blockliste setzen, während Ihr Entwicklerteam daran arbeitet, es aus dem Backend Ihrer App oder Website zu entfernen.

Im Braze-Dashboard können Sie das Blocklisting unter **Dateneinstellungen** > Produkte verwalten. Weitere Informationen finden Sie unter [Verwalten angepasster Daten]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/managing_custom_data/).

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, können Sie **Produkte** unter **Einstellungen verwalten** finden.
{% endalert %}

[1]: {% image_buster /assets/img/purchase_filter_example.gif %}
[2]: {% image_buster /assets/img/purchase2.png %}
[5]: {% image_buster /assets/img/purchase5.png %}
[6]: {% image_buster /assets/img/nested_object3.png %}
