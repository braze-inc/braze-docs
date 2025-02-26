---
nav_title: Angepasste Daten verwalten
article_title: Angepasste Daten verwalten
page_order: 20
page_type: reference
description: "Dieser Artikel referenziert die Verwaltung angepasster Daten, wie z.B. die Vorbelegung von Kampagnen und Segmenten oder das Blockieren und Löschen von Daten."
---

# Benutzerdefinierte Daten verwalten

> Lernen Sie, wie Sie benutzerdefinierte Daten in Ihren Kampagnen und Segmenten vorausfüllen, nicht mehr benötigte Daten blockieren und benutzerdefinierte Ereignisse, Attribute und Eigenschaften verwalten.

## Benutzerdefinierte Daten vorausgefüllt

Es kann vorkommen, dass Sie Kampagnen und Segmente mit angepassten Daten einrichten möchten, bevor Ihr Entwickler:in diese angepassten Daten integriert hat. Braze ermöglicht es Ihnen, angepasste Events und Attribute auf dem Dashboard vorzubelegen, bevor diese Daten mit dem Tracking beginnen, so dass diese Events und Attribute zur Verwendung in Dropdowns und als Teil der Kampagnenerstellung verfügbar sind.

Um angepasste Events und Attribute vorab auszufüllen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Dateneinstellungen** > Angepasste Events oder Angepasste Attribute oder Produkte.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie diese Seiten unter **Einstellungen verwalten**.
{% endalert %}

![Navigieren Sie zu Angepasste Attribute oder Angepasste Events oder Produkte.][21]{: style="max-width:90%;" }

{: start="2"}
2\. Um ein angepasstes Attribut, Event oder Produkt hinzuzufügen, gehen Sie auf die entsprechende Seite und wählen Sie **Angepasste Attribute hinzufügen** oder **Angepasste Events hinzufügen** oder **Produkte hinzufügen**.<br><br>Für angepasste Attribute wählen Sie einen [Datentyp][20] für dieses Attribut (z. B. boolesch oder String). Der Datentyp eines Attributs bestimmt die Filter für die Segmentierung, die für dieses Attribut verfügbar sind. <br><br>![Neues Attribut oder Event hinzufügen][22]{: style="max-width:80%;" }
3\. Wählen Sie **Speichern**.

### Benennung angepasster Events und angepasster Attribute

Bei angepassten Events und angepassten Attributen wird zwischen Groß- und Kleinschreibung unterschieden. Behalten Sie dies im Hinterkopf, wenn Ihr Entwicklungsteam diese angepassten Events oder Attribute später integriert. Sie müssen die angepassten Events oder Attribute genau so benennen, wie Sie sie hier benannt haben, sonst generiert Braze ein anderes angepasstes Event oder Attribut.

## Eigenschaften verwalten

Nachdem Sie ein angepasstes Event oder Produkt erstellt haben, wählen Sie **Eigenschaften** für dieses Event oder Produkt **verwalten** aus, um neue Eigenschaften hinzuzufügen, vorhandene Eigenschaften zu blockieren und zu sehen, welche Kampagnen oder Canvase diese Eigenschaft in einem [triggernden Event]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#step-1-select-a-trigger-event) verwenden.

![Angepasste Eigenschaften für ein angepasstes Event.][73]{: style="max-width:80%"}

Um diese hinzugefügten angepassten Attribute, Events, Produkte oder Event-Eigenschaften nachvollziehbar zu machen, müssen Sie Ihr Entwicklungsteam bitten, sie im SDK unter demselben Namen zu erstellen, unter dem Sie sie zuvor hinzugefügt haben. Alternativ dazu können Sie auch die Braze-[API]({{site.baseurl}}/api/basics/) verwenden, um Daten zu diesem Attribut zu importieren. Danach kann das angepasste Attribut, Event oder anderes auf Ihre Nutzer:innen angewendet werden.

{% alert note %}
Alle Nutzerprofildaten (angepasste Events, angepasste Attribute, angepasste Daten) werden gespeichert, solange diese Profile aktiv sind.
{% endalert %}

## Angepasste Daten auf die Sperrliste setzen

Es kann vorkommen, dass Sie angepasste Attribute, angepasste Events oder Kaufereignisse identifizieren, die entweder zu viele Datenpunkte verbrauchen, für Ihre Marketingstrategie nicht mehr nützlich sind oder irrtümlich aufgezeichnet wurden. Um zu verhindern, dass diese Daten an Braze gesendet werden, können Sie ein angepasstes Datenobjekt auf eine Blockliste setzen, während Ihr Entwicklerteam daran arbeitet, es aus dem Backend Ihrer App oder Website zu entfernen.

Die Blockliste verhindert, dass ein bestimmtes Objekt mit angepassten Daten von Braze aufgezeichnet wird, d.h. es wird bei der Suche nach einem bestimmten Nutzer:in nicht mehr angezeigt. Daten auf der Sperrliste werden nicht vom SDK gesendet, und das Braze-Dashboard verarbeitet keine Daten auf der Sperrliste aus anderen Quellen (z. B. der API). Durch die Sperrung werden jedoch keine Daten aus Nutzerprofilen entfernt oder die Anzahl der Datenpunkte, die für dieses angepasste Datenobjekt anfallen, rückwirkend verringert.

### Setzen von angepassten Attribute, angepasstern Events und Produkten auf die Sperrliste

{% alert important %}
Wenn ein Event oder Attribut auf der Sperrliste steht, werden alle Segmente, Kampagnen oder Canvas, die dieses Event oder Attribut verwenden, archiviert.
{% endalert %}

Um das Tracking eines bestimmten angepassten Attributs, Events oder Produkts zu beenden, gehen Sie folgendermaßen vor:

1. Suchen Sie danach auf den Seiten **Angepasste Attribute**, **Angepasste Events** oder **Produkte**.
2. Wählen Sie das angepasste Attribut, das Event oder das Produkt aus. Bei angepassten Attributen und Event können Sie bis zu 10 auf einmal auf die Sperrliste setzen.
3. Wählen Sie **Sperrliste** aus.

![Mehrere ausgewählte angepasste Attribute, die auf der Seite "Angepasste Attribute" in einer Blockliste aufgeführt sind.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Sie können bis zu 300 angepasste Attribute und 300 angepasste Events in eine Sperrliste aufnehmen. Um das Sammeln bestimmter Geräteattribute zu verhindern, lesen Sie unseren [SDK-Leitfaden][88].

Wenn ein angepasstes Event oder Attribut auf der Sperrliste steht, gilt Folgendes:

- Es werden keine an Braze gesendeten Daten verarbeitet, und gesperrte Events und Attribute zählen nicht mehr als Datenpunkte.
- Vorhandene Daten sind nicht mehr verfügbar, wenn sie nicht erneut aktiviert werden.
- Events und Attribute, die auf der Sperrliste stehen, werden in Filtern und Diagrammen nicht angezeigt.
- Referenzen auf blockierte Daten in Entwürfen von aktiven Canvase werden als ungültige Werte geladen, was zu Fehlern führen kann.
- Alles, was das gesperrte Event oder Attribut verwendet, wird archiviert.

Um dies zu erreichen, sendet Braze die Sperrlisteninformationen an jedes Gerät. Dies ist wichtig, wenn Sie eine große Anzahl von Events und Attributen (Hunderttausende oder Millionen) auf eine Sperrliste setzen möchten, da dies eine datenintensive Operation wäre.

### Überlegungen zum Setzen auf die Sperrliste

Sie sollten bedenken, dass das Sperren einer großen Anzahl von Events und Attributen zwar möglich, aber nicht ratsam ist. Das liegt daran, dass jedes Mal, wenn ein Event ausgeführt oder ein Attribut (möglicherweise) an Braze gesendet wird, dieses Event oder Attribut mit der gesamten Sperrliste abgeglichen werden muss. Wenn es auf der Liste erscheint, wird es nicht nach oben gesendet. Dieser Vorgang nimmt Zeit in Anspruch, und wenn die Liste groß genug wird, könnte Ihre App langsam werden. Wenn Sie das Event oder Attribut in Zukunft nicht mehr benötigen, sollten Sie es bei der nächsten Version aus dem Code Ihrer App entfernen.

Es kann ein paar Minuten dauern, bis Änderungen an der Sperrliste übertragen werden. Sie können jedes Blocklistenereignis oder Attribut jederzeit wieder aktivieren.

## Anpassen von Daten löschen

Wenn Sie zielgerichtete Kampagnen und Segmente erstellen, werden Sie vielleicht feststellen, dass Sie kein angepasstes Event oder angepasstes Attribut mehr benötigen. Wenn Sie z.B. ein bestimmtes angepasstes Attribut als Teil einer einmaligen Kampagne verwendet haben, können Sie diese Daten nach der [Blocklistung](#blocklisting-custom-attributes-custom-events-and-products) löschen und ihre Referenzen aus Ihrer App entfernen. Sie können beliebige Datentypen löschen (z.B. Strings, Zahlen und verschachtelte angepasste Attribute).

Um ein angepasstes Event oder ein angepasstes Attribut zu löschen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Dateneinstellungen** > **Angepasste Attribute** oder **Angepasste Events**, je nachdem, welche Art von Daten Sie löschen möchten.
2. Gehen Sie zu den angepassten Daten und wählen Sie <i class="fa-solid fa-ellipsis-vertical"></i> **Aktionen** > **Blockliste**.
3. Nachdem Ihre angepassten Daten für 7 Tage auf der Sperrliste stehen, wählen Sie <i class="fa-solid fa-ellipsis-vertical"></i> **Aktionen** > Löschen.

### So funktioniert die Löschung

Wenn Sie angepasste Daten löschen, geschieht Folgendes: 

- **Für angepasste Attribute:** Entfernt dauerhaft die Attributdaten aus dem Profil jedes Nutzers:innen.
- **Für angepasste Events:** Entfernt dauerhaft die Ereignis-Metadaten aus dem Profil jedes Nutzers:innen.

Wenn ein Attribut oder ein Event zum Löschen ausgewählt wird, ändert sich sein Status in **Verworfen**. Für die nächsten sieben Tage ist es möglich, das Attribut oder Event wiederherzustellen. Wenn Sie es nach 7 Tagen nicht wiederhergestellt haben, werden die Daten dauerhaft gelöscht. Wenn Sie das Attribut oder das Event wiederherstellen, wird es auf den Status „Auf der Sperrliste“ zurückgesetzt.

{% alert important %}
Die Löschung angepasster Daten befindet sich derzeit im Early Access-Status. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren. Wenn Sie weitere Hilfe beim Löschen von benutzerdefinierten Daten benötigen, wenden Sie sich an Ihren Kundenbetreuer oder das Support-Team.<br><br>Das Löschen verhindert nicht die weitere Aufzeichnung von benutzerdefinierten Datenobjekten in Benutzerprofilen. Stellen Sie also sicher, dass die benutzerdefinierten Daten nicht mehr aufgezeichnet werden, bevor Sie das Ereignis oder Attribut löschen.
{% endalert %}

### Was Sie wissen sollten

Wenn Sie angepasste Daten löschen, sollten Sie die folgenden Details beachten:

* **Die Löschung ist dauerhaft**. Daten können nicht wiederhergestellt werden.
* Die Daten werden von der Braze-Plattform und aus den Nutzer:innen-Profilen entfernt.
* Sie können den Namen des angepassten Attributs oder den Namen des angepassten Events nach dem Löschen „erneut verwenden“. Wenn Sie also feststellen, dass angepasste Daten nach dem Löschen in Braze "wieder auftauchen", kann dies durch eine Integration verursacht werden, die nicht gestoppt wurde und Daten mit demselben Namen für angepasste Daten sendet.
* Möglicherweise müssen Sie einen Artikel erneut auf die Sperrliste setzen, wenn Ihre Löschung dazu führt, dass angepasste Daten wieder auftauchen. Der Status der Sperrliste bleibt nicht erhalten, da die angepassten Daten gelöscht werden.

## Erzwingen von Datentypvergleichen

Braze erkennt automatisch die Datentypen für Attributdaten, die an uns gesendet werden. Falls jedoch mehrere Datentypen auf ein einzelnes Attribut angewendet werden, können Sie den Datentyp eines beliebigen Attributs erzwingen, um uns mitzuteilen, um welchen Typ es sich handelt. Wählen Sie aus dem Dropdown-Menü in der Spalte **Datentyp**.

{% alert note %}
Das Erzwingen von Datentypen gilt nicht für Event-Eigenschaften oder Kauf-Details.
{% endalert %}

![Dropdown-Liste für den Datentyp „Angepasste Attribute“][75]

{% alert warning %}
Wenn Sie den Datentyp für ein Attribut erzwingen möchten, werden alle Daten, die nicht dem angegebenen Typ entsprechen, ignoriert.
{% endalert %}

### Datentyp-Erzwingung

| Erzwungener Datentyp | Beschreibung |
|------------------|-------------|
| Boolesch | Die Eingaben von `1`, `true`, `t` (Groß- und Kleinschreibung wird nicht berücksichtigt) werden gespeichert als `true` |
| Boolesch | Die Eingaben von `0`, `false`, `f` (Groß- und Kleinschreibung wird nicht berücksichtigt) werden gespeichert als `false` |
| Zahl | Ganzzahlen oder Gleitkommazahlen (wie `1`, `1.5`) werden als Zahlen gespeichert. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Informationen zu den spezifischen Filteroptionen, die bei den verschiedenen Datentypvergleichen zur Verfügung stehen, finden Sie unter [Konfigurieren der Berichterstattung][43]. Weitere Informationen zu den verschiedenen verfügbaren Datentypen finden Sie unter [Datentypen von ngepassten Attributen][44].

{% alert note %}
An Braze gesendete Daten sind unveränderlich und können nicht gelöscht oder verändert werden, nachdem wir sie erhalten haben. Sie können jedoch jeden der in den vorangegangenen Abschnitten aufgeführten Schritte verwenden, um zu kontrollieren, was Sie in Ihrem Dashboard tracken.
{% endalert %}


[1]: {% image_buster/assets/img_archive/blocklist_warning.png %}
[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[21]: {% image_buster /assets/img_archive/prepopulate_page.png %}
[22]: {% image_buster /assets/img_archive/prepopulate_add.png %}
[43]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[44]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[73]: {% image_buster /assets/img_archive/manageproperties1.png %}
[75]: {% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %}
[88]: {{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection
