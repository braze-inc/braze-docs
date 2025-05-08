---
nav_title: Angepasste Events
article_title: Angepasste Events
page_order: 9
page_type: reference
description: "Dieser Artikel beschreibt angepasste Events und Eigenschaften, Segmentierung, Nutzung, Eigenschaften des Canvas-Eingangs, wo Sie relevante Analytics einsehen können und vieles mehr."
search_rank: 2
---

# [![Braze Lernkurse]](https://learning.braze.com/custom-events-and-attributes) ( [{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Angepasste Events

> Dieser Artikel beschreibt angepasste Events und Eigenschaften, verwandte Segmentierungsfilter, Canvas-Eingangs-Eigenschaften, relevante Analytics und mehr. Mehr über Braze-Ereignisse im Allgemeinen erfahren Sie unter [Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/events).

Angepasste Events sind Aktionen oder Updates, die von Ihren Nutzer:innen durchgeführt werden. Wenn angepasste Events protokolliert werden, können sie beliebig viele und verschiedene Folgekampagnen auslösen. Mit Hilfe von [Segmentierungsfiltern](#segmentation-filters) können Sie die Nutzer:innen dann danach segmentieren, wie häufig und wie kürzlich diese angepassten Events aufgetreten sind. Dadurch eignen sich angepasste Events am besten für das Tracking hochwertiger Nutzer:innen-Interaktionen innerhalb Ihrer Anwendung.

## Anwendungsfälle

Einige häufige Anwendungsfälle für angepasste Events sind:
- Auslösen einer Kampagne oder eines Canvas auf der Grundlage eines angepassten Events mit [aktionsbasierter Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)
- Segmentierung der Nutzer:innen danach, wie oft sie ein angepasstes Event durchgeführt haben, wann das letzte Mal das Event aufgetreten ist und ähnliches
- Mit den [angepassten Analytics]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics) des Dashboards können Sie sich anzeigen lassen, wie oft jedes Ereignis aufgetreten ist.
- Zusätzliche Analytics mit [Funnel-]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps) und [Bindungsberichten]({{site.baseurl}}/user_guide/data_and_analytics/reporting/retention_reports/) finden
- Nutzung von [persistenten Eingangs-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) zur Verwendung von Metadaten aus Ihrem Kund:in Event zur Personalisierung in Ihren Canvas-Schritten
- Erstellen Sie mit [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) anspruchsvollere Analytics
- Einrichten von [Ausnahme-Events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events#canvas-exception-events) im Canvas, um festzulegen, wann Nutzer:innen nicht zum nächsten Schritt Ihres Canvas voranbringen sollen

## Angepasste Events verwalten

Sie können angepasste Events im Dashboard verwalten, erstellen oder blockieren, indem Sie zu **Dateneinstellungen** > Angepasste Events gehen.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **angepasste Events** unter **Einstellungen verwalten**.
{% endalert %}

Wählen Sie das Menü neben einem angepassten Event für die folgenden Aktionen aus:

### Wird auf Sperrliste gesetzt ...

Sie können einzelne angepasste Events über das Aktionsmenü blockieren oder bis zu 10 Events auswählen und in einer Liste zusammenfassen. 

Wenn Sie ein angepasstes Event blockieren:

- Künftige Daten werden für dieses Ereignis nicht mehr erfasst.
- Vorhandene Daten sind erst dann verfügbar, wenn das Ereignis freigegeben wird.
- Dieses Ereignis wird nicht in Filtern oder Diagrammen angezeigt.

Wenn ein blockiertes angepasstes Event derzeit von Filtern oder Triggern in anderen Bereichen von Braze referenziert wird, wird außerdem ein Modal mit einer Warnung angezeigt, in dem erklärt wird, dass alle Instanzen der Filter oder Trigger, die darauf referenzieren, entfernt und archiviert werden.

### Hinzufügen von Beschreibungen

Sie können einem bereits erstellten angepassten Event eine Beschreibung hinzufügen, wenn Sie über die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases` verfügen. Wählen Sie **Beschreibung bearbeiten** für das angepasste Event und geben Sie ein, was immer Sie möchten, z.B. eine Notiz für Ihr Team.

## Tags hinzufügen

Sie können Tags zu bereits erstellten angepassten Events hinzufügen, wenn Sie die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) "Events, Attribute, Einkäufe verwalten" haben. Anhand der Tags können Sie die Events dann filtern. 

{% alert important %}
Dieses Feature befindet sich derzeit in der Early Access-Phase. Wenden Sie sich an Ihren Customer Success Manager, wenn Sie an einem Vorabzugang interessiert sind.
{% endalert %}

### Nutzungsberichte anzeigen

Der Nutzungsbericht listet alle Canvase, Kampagnen und Segmente auf, die ein bestimmtes angepasstes Event verwenden. Die Liste enthält nicht die Verwendung von Liquid. 

Sie können bis zu 10 Nutzungsberichte auf einmal anzeigen, indem Sie die Kontrollkästchen für mehrere angepasste Events auswählen und dann **Nutzungsbericht anzeigen** wählen.

## Daten exportieren

Um die Liste der angepassten Events als CSV-Datei zu exportieren, wählen Sie den Button **Alle exportieren** oben auf der Seite. Die CSV-Datei wird generiert, und ein Download-Link wird Ihnen per E-Mail zugesandt.

{% alert important %}
Dieses Feature befindet sich derzeit in der Early Access-Phase. Wenden Sie sich an Ihren Customer Success Manager, wenn Sie an einem Vorabzugang interessiert sind.
{% endalert %}

## Protokollierung angepasster Events

Angepasste Events erfordern zusätzliche Einstellungen. In der folgenden Liste finden Sie die Dokumentation zu den einzelnen Plattformen. Dort erfahren Sie, welche Methoden zur Protokollierung angepasster Events verwendet werden und wie Sie Ihren angepassten Events Eigenschaften und Mengen hinzufügen können.

{% details Erweitern, um die Dokumentation für einzelne Plattformen anzuzeigen %}

- [Android und FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
- [Internet]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_custom_events/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/)

{% enddetails %}

## Angepasste Events speichern

Alle im **Nutzerprofil** gespeicherten Daten, einschließlich angepasster Event-Metadaten (erstes oder letztes Vorkommen, Gesamtzahl und X in Y über 30 Tage), werden auf unbestimmte Zeit gespeichert, solange das jeweilige Profil [aktiv]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users) ist.

## Filter für die Segmentierung

Die folgende Tabelle zeigt die Filter, die für die Segmentierung der Nutzer:innen nach angepassten Events zur Verfügung stehen.

| Segmentierung Optionen | Dropdown-Filter | Eingabeoptionen |
| ---------------------| --------------- | ------------- |
| Prüfen, ob das angepasste Event **mehr als X-mal** aufgetreten ist | **MEHR ALS** | **ZAHL** |
| Prüfen, ob das angepasste Event **weniger als X-mal** aufgetreten ist | **WENIGER ALS** | **ZAHL** |
| Prüfen, ob das angepasste Event **genau X-mal** aufgetreten ist | **EXAKT** | **ZAHL** |
| Prüfen Sie, ob das angepasste Event zuletzt **nach dem Datum X** aufgetreten ist | **NACH** | **TIME** |
| Prüfen, ob das angepasste Event zuletzt **vor dem Datum X** aufgetreten ist | **BEVOR** | **TIME** |
| Prüfen, ob das angepasste Event zuletzt **vor mehr als X Tagen** stattgefunden hat | **MEHR ALS** | **NUMBER OF DAYS AGO** (Positive Zahl) |
| Prüfen Sie, ob das angepasste Event zuletzt **vor weniger als X Tagen** stattgefunden hat | **WENIGER ALS** | **NUMBER OF DAYS AGO** (Positive Zahl) |
| Prüfen, ob das angepasste Event **mehr als X Mal (max. 50)** aufgetreten ist **.** | **MEHR ALS** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
| Prüfen, ob das angepasste Event **weniger als X Mal (max. 50)** aufgetreten ist **.** | **WENIGER ALS** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
| Prüfen, ob das angepasste Event **genau X Mal (max. 50)** aufgetreten ist **.** | **EXAKT** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Analytics

Braze merkt sich für die Segmentierung, wie oft angepasste Events aufgetreten sind und wann sie von den einzelnen Nutzer:innen zuletzt ausgeführt wurden. Sehen Sie sich diese Analytics an, indem Sie zu **Analytics** > Bericht über angepasste Events gehen.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie den Bericht **Angepasste Events** unter **Daten**.
{% endalert %}

Auf der Seite **Bericht über angepasste Events** im Dashboard können Sie sich ansehen, wie oft jedes angepasste Event auftritt. Die grauen Linien, die die Zeitreihe überlagern, zeigen an, wann zum letzten Mal eine Kampagne gesendet wurde. Dies ist nützlich, um zu sehen, wie sich Ihre Kampagnen auf die Aktivität angepasster Events ausgewirkt haben.

![Diagramm zur Anzahl angepasster Events auf der Seite "Angepasste Events" im Dashboard mit Trends bei angepassten Events][8]

Sie können auch **Filter** verwenden, um Ihre angepassten Events nach Stunden, monatlichen durchschnittlichen Nutzern:innen, Segmenten oder KPI-Formeln aufzuschlüsseln. 

![Angepasste Filter für das Event-Diagramm][9]{: style="max-width:40%;"}

{% alert tip %}
[Ergänzen Sie angepasste Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers), um Nutzeraktionen wie bei angepassten Events zu zählen. Sie können jedoch keine angepassten Attribut-Daten in einer Zeitreihe anzeigen. Nutzer:innen-Aktionen, die nicht in einer Zeitreihe analysiert werden müssen, sollten mit dieser Methode aufgezeichnet werden.
{% endalert %}

### Warum die Analytics für angepasste Events nicht angezeigt werden

In Segmenten, die mit angepassten Event-Daten erstellt wurden, können keine Daten aus der Zeit vor ihrer Erstellung angezeigt werden.

## Benutzerdefinierte Ereigniseigenschaften

Angepasste Event-Eigenschaften sind angepasste Event-Metadaten oder Attribute, die ein bestimmtes Event-Vorkommen beschreiben. Diese Eigenschaften können zur weiteren Qualifizierung von Trigger-Bedingungen, zur stärkeren Personalisierung des Messagings, zum Tracking von Konversionen und zur Erstellung ausgefeilterer Analytics durch den Export von Rohdaten verwendet werden.

Angepasste Event-Eigenschaften werden nicht im Braze Profil gespeichert und verbrauchen daher keine Datenpunkte (siehe [Datenpunkte](#data-points) für Ausnahmen).

{% alert important %}
Jedes angepasste Event und jeder Kauf kann bis zu 256 unterschiedliche Event-Eigenschaften enthalten. Wenn ein angepasstes Event oder ein Kauf mit mehr als 256 Eigenschaften protokolliert wird, werden nur die ersten 256 erfasst und stehen zur Verfügung.
{% endalert %}

### Erwartetes Format

Die Eigenschaftswerte sollten ein Objekt sein, bei dem die Schlüssel die Eigenschaftsnamen und die Werte die Eigenschaftswerte sind. Eigenschaftsnamen dürfen nicht leer sein und dürfen maximal 255 Zeichen enthalten (keine Dollarzeichen (`$`)).

Bei den Eigenschaften kann es sich um jeden der folgenden Datentypen handeln:

| Datentyp | Beschreibung |
| --- | --- |
| Zahlen | Entweder als [Ganzzahlen](https://en.wikipedia.org/wiki/Integer) oder [Gleitkommazahlen](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Boolesche Werte | Wert von `true` oder `false`. |
| Datumsangaben | Formatiert als Strings im [ISO-8601-](https://en.wikipedia.org/wiki/ISO_8601) oder `yyyy-MM-dd'T'HH:mm:ss:SSSZ` -Format. Innerhalb von Arrays nicht unterstützt. |
| Strings | 255 Zeichen oder weniger. |
| Arrays | Arrays können keine Datumsangaben enthalten. |
| Objekte | Die Objekte werden als Strings eingelesen. |
| Verschachtelte Objekte | Objekte, die sich innerhalb von anderen Objekten befinden. Mehr dazu erfahren Sie im Abschnitt über [verschachtelte Objekte](#nested-objects) in diesem Artikel.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Objekte mit Event-Eigenschaften, die Array- oder Objektwerte enthalten, können bis zu 100 KB Nutzlast für Event-Eigenschaften enthalten.

Sie können den Datentyp Ihrer angepassten Event-Eigenschaft ändern, aber seien Sie sich der Auswirkungen bewusst, die eine [Änderung des Datentyps]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) hat, nachdem die Daten erfasst wurden.

### Angepasste Event-Eigenschaften verwenden

Angepasste Event-Eigenschaften können verwendet werden, um Kampagnen-Trigger zu qualifizieren, Konversionen zu verfolgen und Nachrichten zu personalisieren.

#### Nachrichten triggern

Verwenden Sie angepasste Event-Eigenschaften, um Ihre Zielgruppe für eine bestimmte Kampagne oder ein bestimmtes Canvas weiter einzugrenzen. Wenn Sie beispielsweise eine E-Commerce-Anwendung haben und einem Benutzer eine Nachricht senden möchten, wenn er seinen Warenkorb abbricht, können Sie eine angepasste Event-Eigenschaft von `cart value` hinzufügen, um Ihre Zielgruppe zu verbessern und eine stärkere Personalisierung der Kampagne zu ermöglichen.

![Angepasste Event-Eigenschaften Filter für eine verlassene Karte. Zwei Filter werden mit einem UND-Operator kombiniert, um diese Kampagne an Nutzer:innen zu senden, die ihre Karte mit einem Warenkorb-Abbruch zwischen 100 und 200 Dollar abgebrochen haben.][16]

Verschachtelte angepasste Event-Eigenschaften werden auch bei der [aktionsbasierten Zustellung][19] unterstützt.

![Angepasste Event-Eigenschaften Filter für eine verlassene Karte. Ein Filter wird ausgewählt, wenn ein Artikel im Warenkorb mehr als 100 Dollar kostet.][20]

#### Nachrichten personalisieren

Sie können auch angepasste Event-Eigenschaften zur Personalisierung im Messaging-Template verwenden. Kampagnen mit [aktionsbasierter Zustellung][19] mit einem Trigger-Ereignis können angepasste Event-Eigenschaften dieses Ereignisses zur Personalisierung von Nachrichten nutzen.

Wenn Sie z.B. eine Spiele-App haben und Nutzern, die ein Level abgeschlossen haben, eine Nachricht schicken möchten, könnten Sie Ihre Nachricht mit einer Eigenschaft für die Zeit, die die Nutzer für den Abschluss dieses Levels gebraucht haben, weiter personalisieren. In diesem Beispiel wird die Nachricht mithilfe der [bedingten Logik][18]] für drei verschiedene Segmente personalisiert. Die angepasste Event-Eigenschaft `time_spent` kann durch den Aufruf von ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}`` in die Nachricht aufgenommen werden.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
Ist keine Internetverbindung vorhanden, werden getriggerte In-App-Nachrichten mit angepassten Event-Eigenschaften (wie {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) nicht angezeigt.
{% endalert %}

Eine vollständige Liste der Liquid-Tags, die dazu führen, dass In-App-Nachrichten als Templates zugestellt werden, finden Sie unter [Häufig gestellte Fragen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/).

##### Überlegungen mit Filtern

- **API-Aufrufe:** Wenn Sie API-Aufrufe tätigen und den Filter "ist leer" verwenden, wird eine angepasste Event-Eigenschaft als "leer" betrachtet, wenn sie von dem Aufruf ausgeschlossen ist. Wenn Sie zum Beispiel `"event_property": ""` einfügen, werden Nutzer:innen als "nicht leer" betrachtet.
- **Ganze Zahlen:** Wenn Sie nach einer angepassten Eigenschaft eines Events filtern und deren Anzahl sehr hoch ist, verwenden Sie nicht den Filter "genau". Wenn eine Zahl zu groß ist, wird sie möglicherweise auf eine bestimmte Länge gerundet, so dass Ihr Filter nicht wie erwartet funktioniert.

#### Segmentierung

Verwenden Sie die Segmentierung von Event-Eigenschaften, um Nutzer:innen auf der Grundlage angepasster Events und der mit diesen Events verbundenen Eigenschaften zu targetieren. Dies erweitert Ihre Filtermöglichkeiten bei der Segmentierung nach Kauf-Events und angepassten Events.

Event-Eigenschaften für angepasste Events werden für jedes Segment, in dem sie verwendet werden, in Realtime aktualisiert. Sie können die Eigenschaften anpassen, indem Sie zu **Dateneinstellungen** > **Angepasste Events** gehen und **Eigenschaften** für das zugehörige angepasste Event auswählen. Angepasste Event-Eigenschaften, die in bestimmten Segmentfiltern verwendet werden, werden maximal 30 Tage lang gespeichert.

{% alert note %}
Wenn Sie Segmente auf der Grundlage der Häufigkeit von Event-Eigenschaften erstellen möchten, wenden Sie sich an Ihren Customer-Success-Manager, um die Segmentierung nach bestimmten angepassten Event-Eigenschaften zu aktivieren. Wenn diese Option aktiviert ist, können Sie bei der Segmentierung auf zusätzliche Filteroptionen zugreifen.
{% endalert %}

Die Filter für die Segmentierung der Eigenschaften von Ereignissen umfassen:

- Hat ein angepasstes Event mit der Eigenschaft A mit dem Wert B, X Mal in den letzten Y Tagen durchgeführt.
- Hat in den letzten Y Tagen X-mal Käufe mit Eigentum A mit Wert B getätigt.
- Fügt die Möglichkeit hinzu, innerhalb von 1, 3, 7, 14, 21 und 30 Tagen zu segmentieren.

![Eine Filtergruppe, "die 'Abandoned Cart' mit der Eigenschaft 'number of itmes' und dem Wert '2' 'more than' 1'1 time in the last '30' calendary days (720-744 hours) hat."][3]

Daten zu einer bestimmten Event-Eigenschaft werden erst dann protokolliert, wenn dies von Ihrem Customer-Success-Manager aktiviert wurde. Und auch Event-Eigenschaften sind erst ab diesem Zeitpunkt verfügbar.

##### Datenpunkte

In Bezug auf die Abo-Nutzung werden alle angepassten Event-Eigenschaften, die für die Segmentierung mit den folgenden Filtern aktiviert wurden, als separate Datenpunkte gezählt, zusätzlich zu den Datenpunkten, die von dem angepassten Event selbst gezählt werden:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Canvas-Eingangs-Eigenschaften und Event-Eigenschaften

Sie können `canvas_entry_properties` und `event_properties` in Canvas-User-Journeys verwenden. Weitere Informationen und Beispiele finden Sie unter [Canvas-Eingangs-Eigenschaften und Event-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/).

{% tabs local %}
{% tab Canvas-Entry-Eigenschaften %}

[Canvas-Entry-Eigenschaften]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) sind Eigenschaften für Canvase, die durch Aktionen oder die API getriggert werden. Beachten Sie, dass das Objekt `canvas_entry_properties` maximal 50 KB groß sein darf.

{% alert note %}
Insbesondere bei In-App-Nachrichtenkanälen kann `canvas_entry_properties` nur dann in Canvas Flow und dem ursprünglichen Canvas-Editor referenziert werden, wenn Sie in der Early-Access-Phase persistente Entry-Eigenschaften aktiviert haben.
{% endalert %}

Bei Canvas-Flow-Nachrichten kann `canvas_entry_properties` in jedem Nachrichtenschritt in diesem Liquid-Format verwendet werden: ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. Beachten Sie, dass es sich bei den Events um angepasste Events oder Kauf-Events handeln muss, damit dies möglich ist. 

#### Anwendungsfall

{% raw %}
Angenommen, der Shop RetailApp erhält folgende Anfrage: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. RetailApp kann den Produktnamen (Schuhe) in eine Nachricht mit dem Liquid `{{canvas_entry_properties.${product_name}}}` ziehen.
{% endraw %}

RetailApp kann auch spezielle Nachrichten für verschiedene Eigenschaften von `product_name` in einem Canvas triggern, das Nutzer:innen anspricht, nachdem sie ein Kauf-Event ausgelöst haben. Sie können zum Beispiel unterschiedliche Nachrichten an Nutzer:innen, die Schuhe gekauft haben, und Nutzer:innen, die etwas anderes gekauft haben, senden, indem Sie das folgende Liquid in einen Messaging-Schritt einfügen.

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Erweitern für Original Canvas Editor %}

Ab 28\. Februar 2023 können Sie keine Canvase mehr mit dem Original-Editor erstellen oder duplizieren. Dieser Abschnitt ist nur zum Referenzieren verfügbar.

Bei den Canvase, die mit dem Original-Editor erstellt wurden, kann `canvas_entry_properties` nur im ersten vollständigen Schritt eines Canvas referenziert werden.

{% enddetails %}
{% endtab %}

{% tab Event-Eigenschaften %}

{% alert important %}
Sie können `event_properties` nicht für den Schritt "Lead Message" verwenden. Stattdessen müssen Sie `canvas_entry_properties` verwenden oder einen Aktionspfadschritt mit dem entsprechenden Ereignis **vor dem** Nachrichtenschritt  hinzufügen, der `event_properties` enthält.
{% endalert %}

Event-Eigenschaften referenzieren auf die Eigenschaften, die Sie für angepasste Events und Käufe festlegen. Diese `event_properties` können in Kampagnen mit aktionsbasierter Lieferung und Canvases verwendet werden.

In Canvas Flow können angepasste Event- und Kaufevent-Eigenschaften in Liquid in jedem Nachrichtenschritt verwendet werden, der auf einen Aktionspfadschritt folgt. Stellen Sie sicher, dass Sie {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} verwenden, wenn Sie auf diese `event_properties` verweisen. Diese Ereignisse müssen angepasste Events oder Kaufevents sein, damit sie so in der Nachrichtenkomponente verwendet werden können.

Im ersten Nachrichtenschritt nach einem Aktionspfad können Sie `event_properties` für das Ereignis verwenden, das in diesem Aktionspfad referenziert wird. Diese `event_properties` können nur verwendet werden, wenn der Nutzer:in tatsächlich die Aktion durchgeführt hat (und nicht in die Gruppe Alle anderen gegangen ist). Zwischen diesem Aktionspfad und dem Nachrichtenschritt können Sie weitere Schritte einfügen (die selbst keine Aktionspfade oder Nachrichtenschritte sind).

{% details Erweitern für Original Canvas Editor %}

Ab 28\. Februar 2023 können Sie keine Canvase mehr mit dem Original-Editor erstellen oder duplizieren. Dieser Abschnitt ist nur zum Referenzieren verfügbar.

Im ursprünglichen Canvas-Editor kann `event_properties` nicht in geplanten vollständigen Schritten verwendet werden. Sie können jedoch `event_properties` im ersten vollständigen Schritt aktionsbasierter Canvase verwenden, auch wenn ein vollständiger Schritt geplant ist.

{% enddetails %}

{% endtab %}
{% endtabs %}

### Verschachtelte Objekte {#nested-objects}

Sie können verschachtelte Objekte (Objekte innerhalb eines anderen Objekts) verwenden, um verschachtelte JSON-Daten als Eigenschaften von angepassten Events und Käufen zu senden. Diese verschachtelten Daten können als Template für personalisierte Informationen in Nachrichten, zum Triggern von Nachrichtensendungen und zur Segmentierung von Nutzer:innen verwendet werden.

Wenn Sie mehr darüber erfahren möchten, lesen Sie unsere spezielle Seite über [verschachtelte Objekte]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/nested_objects/).

## Speicherung angepasster Event-Eigenschaften

Angepasste Event-Eigenschaften erhöhen die Targeting-Präzision und personalisieren die Nachrichten noch stärker. Angepasste Event-Eigenschaften können in Braze sowohl kurz- als auch langfristig gespeichert werden.

Sie können anhand der Werte von Event-Eigenschaften auf zwei Arten segmentieren:

1. **Innerhalb von 30 Tagen:** Der Braze-Support kann die Segmentierung von Event-Eigenschaften nach Häufigkeit und Aktualität bestimmter Werte von Event-Eigenschaften in Braze-Segmenten aktivieren. Wenn Sie Event-Eigenschaften innerhalb von Segmenten nutzen möchten, wenden Sie sich an Ihren Account- oder Customer-Success-Manager. Diese Option hat Auswirkungen auf die Datennutzung.<br><br>
2. **Bis/nach 30 Tagen:** Um sowohl die kurzfristige als auch die langfristige Segmentierung der Event-Eigenschaften abzudecken, können Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) verwenden. Dieses Feature segmentiert Nutzer:innen auf der Grundlage angepasster Events und Event-Eigenschaften, die innerhalb der letzten zwei Jahre getrackt wurden. Diese Option hat keine Auswirkungen auf die Datennutzung.

Wenden Sie sich an Ihren Customer-Success-Manager:in von Braze, um Empfehlungen für den besten Ansatz je nach Ihren spezifischen Anforderungen zu erhalten.

[1]: {% image_buster /assets/img/nested_object1.png %}
[2]: {% image_buster /assets/img/nested_object2.png %}
[3]: {% image_buster /assets/img/nested_object3.png %}
[4]: {% image_buster /assets/img_archive/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/img_archive/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/img_archive/schema_generation_example.png %}
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[9]: {% image_buster /assets/img/custom_events_report_filters.png %}
[16]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"
