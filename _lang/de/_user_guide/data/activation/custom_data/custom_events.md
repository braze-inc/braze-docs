---
nav_title: Angepasste Events
article_title: Benutzerdefinierte Ereignisse
page_order: 9
page_type: reference
description: "Dieser Artikel beschreibt angepasste Events und Eigenschaften, Segmentierung, Nutzung, Eigenschaften des Canvas-Eingangs, wo Sie relevante Analytics einsehen können und vieles mehr."
search_rank: 2
---

# [![Braze Lernkurse]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"} Angepasste Events

> Dieser Artikel beschreibt angepasste Events und Eigenschaften, verwandte Segmentierungsfilter, Canvas-Eingangs-Eigenschaften, relevante Analytics und mehr. Mehr über Braze-Ereignisse im Allgemeinen erfahren Sie unter [Events]({{site.baseurl}}/user_guide/data/custom_data/events/).

Angepasste Events sind Aktionen oder Updates, die von Ihren Nutzer:innen durchgeführt werden. Wenn angepasste Events protokolliert werden, können sie beliebig viele und verschiedene Folgekampagnen auslösen. Mit Hilfe von [Segmentierungsfiltern](#segmentation-filters) können Sie die Nutzer:innen dann danach segmentieren, wie häufig und wie kürzlich diese angepassten Events aufgetreten sind. Dadurch eignen sich angepasste Events am besten für das Tracking hochwertiger Nutzer:innen-Interaktionen innerhalb Ihrer Anwendung.

## Anwendungsfälle

Einige häufige Anwendungsfälle für angepasste Events sind:

- Auslösen einer Kampagne oder eines Canvas auf der Grundlage eines angepassten Events mit [aktionsbasierter Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)
- Segmentierung der Nutzer:innen danach, wie oft sie ein angepasstes Event durchgeführt haben, wann das letzte Mal das Event aufgetreten ist und ähnliches
- Mit den [angepassten Analytics]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics) des Dashboards können Sie sich anzeigen lassen, wie oft jedes Ereignis aufgetreten ist.
- Zusätzliche Analytics mit [Funnel-]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps) und [Bindung-Berichten]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) finden
- Nutzung von [persistenten Eingangs-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) zur Verwendung von Metadaten aus Ihrem Kund:in Event zur Personalisierung in Ihren Canvas-Schritten
- Erstellen Sie mit [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) anspruchsvollere Analytics
- Einrichten von [Ausstiegskriterien]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria), um festzulegen, wann Nutzer:innen Ihren Canvas verlassen sollen

## Angepasste Events verwalten

Sie können angepasste Events im Dashboard verwalten, erstellen oder blockieren, indem Sie zu **Dateneinstellungen** > Angepasste Events gehen.

Wählen Sie das Menü neben einem angepassten Event für die folgenden Aktionen aus:

### Wird auf Sperrliste gesetzt ...

Sie können einzelne angepasste Events über das Aktionsmenü blockieren oder bis zu 100 Events auswählen und in einer Liste zusammenfassen. 

Wenn Sie ein angepasstes Event blockieren:

- Künftige Daten werden für dieses Ereignis nicht mehr erfasst.
- Vorhandene Daten sind erst dann verfügbar, wenn das Ereignis freigegeben wird.
- Dieses Ereignis wird nicht in Filtern oder Diagrammen angezeigt.

Wenn ein blockiertes angepasstes Event derzeit von Filtern oder Triggern in anderen Bereichen von Braze referenziert wird, wird außerdem ein Modal mit einer Warnung angezeigt, in dem erklärt wird, dass alle Instanzen der Filter oder Trigger, die darauf referenzieren, entfernt und archiviert werden.

### Hinzufügen von Beschreibungen

Sie können einem bereits erstellten angepassten Event eine Beschreibung hinzufügen, wenn Sie über die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases` verfügen. Wählen Sie **Beschreibung bearbeiten** für das angepasste Event und geben Sie ein, was immer Sie möchten, z.B. eine Notiz für Ihr Team.

## Tags hinzufügen

Sie können Tags zu bereits erstellten angepassten Events hinzufügen, wenn Sie die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) "Events, Attribute, Einkäufe verwalten" haben. Anhand der Tags können Sie dann die Liste der Ereignisse filtern.

### Nutzungsberichte anzeigen

Der Nutzungsbericht listet alle Canvase, Kampagnen und Segmente auf, die ein bestimmtes angepasstes Event verwenden. Die Liste enthält nicht die Verwendung von Liquid. 

Sie können bis zu 100 Nutzungsberichte auf einmal anzeigen, indem Sie die Kontrollkästchen für mehrere angepasste Events auswählen und dann **Nutzungsbericht anzeigen** wählen.

## Daten exportieren

Um die Liste der angepassten Events als CSV-Datei zu exportieren, wählen Sie den Button **Alle exportieren** oben auf der Seite. Die CSV-Datei wird generiert, und ein Download-Link wird Ihnen per E-Mail zugesandt.

## Protokollierung angepasster Events

Angepasste Events erfordern zusätzliche Einstellungen. In der folgenden Liste finden Sie die Dokumentation zu den einzelnen Plattformen. Dort erfahren Sie, welche Methoden zur Protokollierung angepasster Events verwendet werden und wie Sie Ihren angepassten Events Eigenschaften und Mengen hinzufügen können.

{% details Expand for documentation by platform %}

- [Android und FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Internet]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=unity)
- [.NET MAUI]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

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

Auf der Seite **Bericht über angepasste Events** im Dashboard können Sie sich ansehen, wie oft jedes angepasste Event auftritt. Die grauen Linien, die die Zeitreihe überlagern, zeigen an, wann zum letzten Mal eine Kampagne gesendet wurde. Dies ist nützlich, um zu sehen, wie sich Ihre Kampagnen auf die Aktivität angepasster Events ausgewirkt haben.

![Grafische Darstellung der Anzahl angepasster Events auf der Seite Custom Events im Dashboard, die Trends für ein angepasstes Event anzeigt]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

Sie können auch **Filter** verwenden, um Ihre angepassten Events nach Stunden, monatlichen durchschnittlichen Nutzern:innen, Segmenten oder KPI-Formeln aufzuschlüsseln. 

![Angepasste Event Graph Filter]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[Ergänzen Sie angepasste Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers), um Nutzeraktionen wie bei angepassten Events zu zählen. Sie können jedoch keine angepassten Attribut-Daten in einer Zeitreihe anzeigen. Nutzer:innen-Aktionen, die nicht in einer Zeitreihe analysiert werden müssen, sollten mit dieser Methode aufgezeichnet werden.
{% endalert %}

### Warum die Analytics für angepasste Events nicht angezeigt werden

In Segmenten, die mit angepassten Event-Daten erstellt wurden, können keine Daten aus der Zeit vor ihrer Erstellung angezeigt werden.

## Benutzerdefinierte Ereigniseigenschaften

Angepasste Event-Eigenschaften sind angepasste Event-Metadaten oder Attribute, die ein bestimmtes Vorkommen eines Events beschreiben. Diese Eigenschaften können zur weiteren Qualifizierung von Trigger-Bedingungen, zur stärkeren Personalisierung des Messagings, zum Tracking von Konversionen und zur Erstellung ausgefeilterer Analytics durch den Export von Rohdaten verwendet werden.

Angepasste Event-Eigenschaften werden nicht im Braze-Profil gespeichert und protokollieren daher auch keine Datenpunkte (siehe [Datenpunkte](#data-points) für Ausnahmen).

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
| Verschachtelte Objekte | Objekte, die sich innerhalb von anderen Objekten befinden. Mehr dazu erfahren Sie im Abschnitt über [verschachtelte Objekte](#nested-objects) in diesem Artikel.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Objekte mit Event-Eigenschaften, die Array- oder Objektwerte enthalten, können eine Nutzlast für Event-Eigenschaften von bis zu 100 KB haben.

Sie können den Datentyp Ihrer angepassten Event-Eigenschaft ändern, aber seien Sie sich der Auswirkungen bewusst, die eine [Änderung des Datentyps]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) hat, nachdem die Daten erfasst wurden.

### Angepasste Event-Eigenschaften verwenden

Angepasste Event-Eigenschaften können verwendet werden, um Kampagnen-Trigger zu qualifizieren, Konversionen zu verfolgen und Nachrichten zu personalisieren.

#### Nachrichten triggern

Verwenden Sie angepasste Event-Eigenschaften, um Ihre Zielgruppe für eine bestimmte Kampagne oder ein bestimmtes Canvas weiter einzugrenzen. Wenn Sie beispielsweise eine E-Commerce-Anwendung haben und einem Benutzer eine Nachricht senden möchten, wenn er seinen Warenkorb abbricht, können Sie eine angepasste Event-Eigenschaft von `item price` hinzufügen, um Ihre Zielgruppe zu verbessern und eine stärkere Personalisierung der Kampagne zu ermöglichen.

![Angepasste Event-Eigenschaften Filter für eine aufgegebene Karte. Zwei Filter werden mit einem AND Operator kombiniert, um diese Kampagne an Nutzer:innen zu senden, die ihre Karte mit einem Artikelpreis zwischen 100 und 200 Dollar aufgegeben haben]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

Verschachtelte Event-Eigenschaften werden auch bei [aktionsbasierter Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) unterstützt.

![Angepasste Event-Eigenschaften Filter für eine aufgegebene Karte. Ein Filter wird ausgewählt, wenn ein Artikel im Warenkorb mehr als 100 Dollar kostet.]({% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png")

#### Nachrichten personalisieren

Sie können auch angepasste Event-Eigenschaften zur Personalisierung innerhalb des Messaging Templates verwenden. Jede Kampagne, die eine [aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) mit einem Trigger Event verwendet, kann angepasste Event-Eigenschaften dieses Events für die Personalisierung von Nachrichten nutzen.

Wenn Sie z.B. eine Spiele-App haben und Nutzern, die ein Level abgeschlossen haben, eine Nachricht schicken möchten, könnten Sie Ihre Nachricht mit einer Eigenschaft für die Zeit, die die Nutzer für den Abschluss dieses Levels gebraucht haben, weiter personalisieren. In diesem Beispiel wird die Nachricht mithilfe [bedingter Logik]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/) für drei verschiedene Segmente personalisiert. Die angepasste Event-Eigenschaft `time_spent` kann durch den Aufruf von ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}`` in die Nachricht aufgenommen werden.

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

- **API-Aufrufe:** Wenn Sie API-Aufrufe tätigen und den Filter "ist leer" verwenden, wird eine angepasste Event-Eigenschaft als "leer" betrachtet, wenn sie von dem Aufruf ausgeschlossen ist. Wenn Sie zum Beispiel `"event_property": ""` einfügen, werden Ihre Nutzer:innen als "nicht leer" betrachtet.
- **Ganze Zahlen:** Wenn Sie nach einer angepassten Eigenschaft eines Events filtern und deren Anzahl sehr hoch ist, verwenden Sie nicht den Filter "genau". Wenn eine Zahl zu groß ist, wird sie möglicherweise auf eine bestimmte Länge gerundet, so dass Ihr Filter nicht wie erwartet funktioniert.

#### Segmentierung

Verwenden Sie die Segmentierung von Event-Eigenschaften, um Nutzer:innen auf der Grundlage angepasster Events und der mit diesen Events verbundenen Eigenschaften zu targetieren. Dies erweitert Ihre Filtermöglichkeiten bei der Segmentierung nach Kauf-Events und angepassten Events.

Event-Eigenschaften für angepasste Events werden für jedes Segment, das sie verwendet, in Realtime aktualisiert. Sie können Einstellungen verwalten, indem Sie zu **Dateneinstellungen** > **Angepasste Events** gehen und **Eigenschaften** für das entsprechende angepasste Event auswählen. Angepasste Event-Eigenschaften, die in bestimmten Segmentfiltern verwendet werden, werden maximal 30 Tage lang gespeichert.

##### Hinzufügen von Event-Eigenschaften für die Segmentierung

Sie benötigen die [Nutzerzustimmung]({{site.baseurl}}/user_guide/data/data_points/#viewing-data-point-usage) "Angepasste Event-Eigenschaft Segmentierung verwalten", um Segmente auf der Grundlage der Häufigkeit von Event-Eigenschaften zu erstellen.

Standardmäßig können Sie 20 segmentierbare Event-Eigenschaften pro Workspace haben. Wenden Sie sich an Ihren Braze-Konto Manager:in, um dieses Limit zu erhöhen.

Um Event-Eigenschaften für die Segmentierung hinzuzufügen, gehen Sie wie folgt vor:

1. Gehen Sie zu Ihrem angepassten Event und wählen Sie **Eigenschaften verwalten**.
2. Wählen Sie die Option **Enablement** umschalten, um die Eigenschaft des Ereignisses für die Segmentierung hinzuzufügen. Sie können bei der Segmentierung auf zusätzliche Filteroptionen zugreifen.

Die Filter für die Segmentierung der Eigenschaften von Ereignissen umfassen:

- Hat ein angepasstes Event mit der Eigenschaft A mit dem Wert B, X Mal in den letzten Y Tagen durchgeführt.
- Hat in den letzten Y Tagen X-mal mit Eigenschaft A mit Wert B eingekauft.
- Fügt die Möglichkeit der Segmentierung innerhalb von 1 bis 30 Tagen hinzu.

![Eine Filtergruppe, die 'Warenkorb-Abbruch' mit der Eigenschaft 'Anzahl der Itemes' und dem Wert 2 mehr als 1 Mal in den letzten 30 Kalendertagen hat.]({% image_buster /assets/img/nested_object3.png %})

Daten werden für eine bestimmte Event-Eigenschaft erst protokolliert, nachdem sie von Ihrem Customer-Success-Manager aktiviert wurde, und Event-Eigenschaften sind erst ab diesem Zeitpunkt verfügbar.

##### Datenpunkte

In Bezug auf die Abo-Nutzung werden alle angepassten Event-Eigenschaften, die für die Segmentierung mit den folgenden Filtern aktiviert wurden, als separate Datenpunkte gezählt, zusätzlich zu den Datenpunkten, die von dem angepassten Event selbst gezählt werden:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Canvas-Eingangs-Eigenschaften und Event-Eigenschaften

{% multi_lang_include canvas_entry_event_properties.md %}

### Verschachtelte Objekte {#nested-objects}

Sie können verschachtelte Objekte (Objekte innerhalb eines anderen Objekts) verwenden, um verschachtelte JSON-Daten als Eigenschaften von angepassten Events und Käufen zu senden. Diese verschachtelten Daten können als Template für personalisierte Informationen in Nachrichten, zum Triggern von Nachrichtensendungen und zur Segmentierung von Nutzer:innen verwendet werden.

Wenn Sie mehr darüber erfahren möchten, lesen Sie unsere spezielle Seite über [verschachtelte Objekte]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

## Speicherung angepasster Event-Eigenschaften

Angepasste Event-Eigenschaften helfen Ihnen dabei, die Targeting-Präzision zu erhöhen und die Nachrichten noch stärker zu personalisieren. Angepasste Event-Eigenschaften können in Braze sowohl kurz- als auch langfristig gespeichert werden.

Sie können anhand der Werte von Event-Eigenschaften auf zwei Arten segmentieren:

1. **Innerhalb von 30 Tagen:** Die Mitarbeiter des Braze-Supports können die Segmentierung von Event-Eigenschaften auf der Grundlage der Häufigkeit und Häufigkeit bestimmter Werte von Event-Eigenschaften in Segmenten von Braze aktivieren. Wenn Sie Event-Eigenschaften innerhalb von Segmenten nutzen möchten, wenden Sie sich an Ihren Braze Account Manager oder Customer-Success-Manager. Diese Option hat Auswirkungen auf die Datennutzung.<br><br>
2. **Bis/nach 30 Tagen:** Um sowohl die kurzfristige als auch die langfristige Segmentierung der Event-Eigenschaften abzudecken, können Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) verwenden. Dieses Feature segmentiert Nutzer:innen auf der Grundlage angepasster Events und Event-Eigenschaften, die innerhalb der letzten zwei Jahre getrackt wurden. Diese Option hat keine Auswirkungen auf die Datennutzung.

Wenden Sie sich an Ihren Customer-Success-Manager:in von Braze, um Empfehlungen für den besten Ansatz je nach Ihren spezifischen Anforderungen zu erhalten.

