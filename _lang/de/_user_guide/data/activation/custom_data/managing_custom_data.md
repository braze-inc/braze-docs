---
nav_title: Angepasste Daten verwalten
article_title: Angepasste Daten verwalten
page_order: 20
page_type: reference
description: "Dieser Artikel referenziert die Verwaltung angepasster Daten, wie z.B. die Vorbelegung von Kampagnen und Segmenten oder das Blockieren und Löschen von Daten."
---

# Angepasste Daten verwalten

> Auf dieser Seite erfahren Sie, wie Sie angepasste Daten in Ihre Kampagnen und Segmente einfügen, nicht mehr benötigte Daten blockieren und angepasste Events und Attribute sowie Eigenschaften verwalten können.<br><br>Wie Sie angepasste Attribute verwalten können, erfahren Sie unter [Verwaltung angepasster Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes).

## Angepasste Daten vorausgefüllt

Es kann vorkommen, dass Sie Kampagnen und Segmente mit angepassten Daten einrichten möchten, bevor Ihr Entwickler:in diese angepassten Daten integriert hat. Braze ermöglicht es Ihnen, angepasste Events und Attribute auf dem Dashboard vorzubelegen, bevor diese Daten mit dem Tracking beginnen, so dass diese Events und Attribute zur Verwendung in Dropdowns und als Teil der Kampagnenerstellung verfügbar sind.

Um angepasste Events und Attribute vorzubelegen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Dateneinstellungen** > Angepasste Events oder Angepasste Attribute oder Produkte.

![Navigieren Sie zu Angepasste Attribute oder Angepasste Events oder Produkte.]({% image_buster /assets/img_archive/prepopulate_page.png %}){: style="max-width:90%;" }

{: start="2"}
2\. Um ein angepasstes Attribut, Event oder Produkt hinzuzufügen, gehen Sie auf die entsprechende Seite und wählen Sie **Angepasste Attribute hinzufügen** oder **Angepasste Events hinzufügen** oder **Produkte hinzufügen**.<br><br>Für angepasste Attribute wählen Sie einen [Datentyp]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) für dieses Attribut aus (z.B. boolesch oder String). Der Datentyp eines Attributs bestimmt die Filter für die Segmentierung, die für dieses Attribut verfügbar sind. <br><br>![Neues Attribut oder Ereignis hinzufügen]({% image_buster /assets/img_archive/prepopulate_add.png %}){: style="max-width:80%;" }
3\. Wählen Sie **Speichern**.

### Benennung angepasster Events und angepasster Attribute

Bei angepassten Events und angepassten Attributen wird zwischen Groß- und Kleinschreibung unterschieden. Behalten Sie dies im Hinterkopf, wenn Ihr Entwickler:in-Team diese angepassten Events oder Attribute später integriert. Sie müssen die angepassten Events oder Attribute genau so benennen, wie Sie sie hier benannt haben, sonst generiert Braze ein anderes angepasstes Event oder Attribut.

## Eigenschaften verwalten

Nachdem Sie ein angepasstes Event oder Produkt erstellt haben, wählen Sie **Eigenschaften** für dieses Event oder Produkt **verwalten** aus, um neue Eigenschaften hinzuzufügen, vorhandene Eigenschaften zu blockieren und zu sehen, welche Kampagnen oder Canvase diese Eigenschaft in einem [triggernden Event]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) verwenden.

![Angepasste Eigenschaften für ein angepasstes Event.]({% image_buster /assets/img_archive/manageproperties1.png %}){: style="max-width:80%"}

Um diese hinzugefügten angepassten Attribute, Events, Produkte oder Event-Eigenschaften nachvollziehbar zu machen, müssen Sie Ihr Entwickler:in Team bitten, sie im SDK unter demselben Namen zu erstellen, unter dem Sie sie zuvor hinzugefügt haben. Oder Sie können die Braze [API]({{site.baseurl}}/api/basics/) verwenden, um Daten zu diesem Attribut zu importieren. Danach kann das angepasste Attribut, Event oder anderes auf Ihre Nutzer:innen angewendet werden.

{% alert note %}
Alle Nutzerprofildaten (angepasste Events, angepasste Attribute, angepasste Daten) werden gespeichert, solange diese Profile aktiv sind.
{% endalert %}

## Blocklisting angepasster Daten

Es kann vorkommen, dass Sie angepasste Attribute, angepasste Events oder Kauf-Events identifizieren, die entweder zu viele Datenpunkte aufzeichnen, für Ihre Marketing-Strategie nicht mehr nützlich sind oder irrtümlich aufgezeichnet wurden. 

Um zu verhindern, dass diese Daten an Braze gesendet werden, können Sie ein angepasstes Datenobjekt auf eine Blockliste setzen, während Ihr Entwicklerteam daran arbeitet, es aus dem Backend Ihrer App oder Website zu entfernen. Die Blockliste verhindert, dass ein bestimmtes Objekt mit angepassten Daten von Braze aufgezeichnet wird, d.h. es wird bei der Suche nach einem bestimmten Nutzer:in nicht mehr angezeigt.

{% alert important %}
Um angepasste Daten zu blockieren, benötigen Sie die [Nutzer:innen die Berechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions), auf Kampagnen, Canvase und Segmente zuzugreifen und diese zu bearbeiten.
{% endalert %}

Daten auf der Blockliste werden nicht vom SDK gesendet, und das Braze-Dashboard verarbeitet keine Daten auf der Blockliste aus anderen Quellen (z.B. der API). Durch die Sperrung werden jedoch keine Daten aus Nutzerprofilen entfernt oder die Anzahl der Datenpunkte, die für dieses angepasste Datenobjekt anfallen, rückwirkend verringert.

### Blocklisting angepasster Attribute, angepasster Events und Produkte

{% alert important %}
Wenn ein Ereignis oder Attribut auf der Blockliste steht, werden alle Segmente, Kampagnen oder Canvas, die dieses Ereignis oder Attribut verwenden, archiviert.
{% endalert %}

Um das Tracking eines bestimmten angepassten Attributs, Ereignisses oder Produkts zu beenden, gehen Sie folgendermaßen vor:

1. Suchen Sie danach auf den Seiten **Angepasste Attribute**, **Angepasste Events** oder **Produkte**.
2. Wählen Sie das angepasste Attribut, das Event oder das Produkt aus. Für angepasste Attribute und Events können Sie jeweils bis zu 100 auswählen, um sie zu blockieren.
3. Wählen Sie **Blockliste**.

![Mehrere ausgewählte angepasste Attribute, die auf der Seite Angepasste Attribute in einer Blockliste aufgeführt sind.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Sie können bis zu 300 angepasste Attribute und 300 angepasste Events in eine Blockliste aufnehmen. Um die Erfassung bestimmter Attribute von Geräten zu verhindern, lesen Sie unseren [SDK-Leitfaden]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection). 

{% alert important %}
Angepasste Attribute oder angepasste Events mit dem Status **"Entfernt"** werden auf die Blockliste angerechnet, bis sie gelöscht werden.
{% endalert %}

Wenn ein angepasstes Event oder Attribut auf der Blockliste steht, gilt Folgendes:

- Es werden keine an Braze gesendeten Daten verarbeitet, und blockierte Ereignisse und Attribute zählen nicht mehr als Datenpunkte.
- Vorhandene Daten sind nicht mehr verfügbar, wenn sie nicht reaktiviert werden.
- Ereignisse und Attribute, die auf der Blockliste stehen, werden in Filtern und Diagrammen nicht angezeigt.
- Referenzen auf blockierte Daten in Entwürfen von aktiven Canvase werden als ungültige Werte geladen, was zu Fehlern führen kann.
- Alles, was das blockierte Ereignis oder Attribut verwendet, wird archiviert.

Um dies zu erreichen, sendet Braze die Blocklisting-Informationen an jedes Gerät. Dies ist wichtig, wenn Sie eine große Anzahl von Ereignissen und Attributen (Hunderttausende oder Millionen) auf eine Blockliste setzen wollen, da dies eine datenintensive Operation wäre.

### Überlegungen zur Blocklistung

Das Blockieren einer großen Anzahl von Ereignissen und Attributen ist möglich, aber nicht ratsam. Das liegt daran, dass jedes Mal, wenn ein Ereignis ausgeführt oder ein Attribut (möglicherweise) an Braze gesendet wird, dieses Ereignis oder Attribut mit der gesamten Blockliste abgeglichen werden muss.

Bis zu 300 Artikel werden an das SDK für die Blocklistung gesendet. Wenn Sie mehr als 300 Artikel auf der Blockliste haben, werden diese Daten vom SDK gesendet. Wenn Sie das Ereignis oder Attribut in Zukunft nicht mehr benötigen, sollten Sie es bei der nächsten Version aus dem Code Ihrer App entfernen. Es kann ein paar Minuten dauern, bis Änderungen an der Blockliste übertragen werden. Sie können jedes Blocklistenereignis oder Attribut jederzeit wieder aktivieren.

## Anpassen von Daten löschen

Wenn Sie zielgerichtete Kampagnen und Segmente erstellen, werden Sie vielleicht feststellen, dass Sie kein angepasstes Event oder angepasstes Attribut mehr benötigen. Wenn Sie z.B. ein bestimmtes angepasstes Attribut als Teil einer einmaligen Kampagne verwendet haben, können Sie diese Daten nach der [Blocklistung](#blocklisting-custom-attributes-custom-events-and-products) löschen und ihre Referenzen aus Ihrer App entfernen. Sie können beliebige Datentypen löschen (z.B. Strings, Zahlen und verschachtelte angepasste Attribute).

{% alert important %}
Sie müssen ein [Braze-Administrator]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) sein, um angepasste Daten zu löschen.
{% endalert %}

Um ein angepasstes Event oder ein angepasstes Attribut zu löschen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Dateneinstellungen** > **Angepasste Attribute** oder **Angepasste Events**, je nachdem, welche Art von Daten Sie löschen möchten.
2. Gehen Sie zu den angepassten Daten und wählen Sie <i class="fa-solid fa-ellipsis-vertical"></i> **Aktionen** > **Blockliste**.
3. Nachdem Ihre angepassten Daten für 7 Tage auf der Sperrliste stehen, wählen Sie <i class="fa-solid fa-ellipsis-vertical"></i> **Aktionen** > Löschen.

### So funktioniert die Löschung

Wenn Sie angepasste Daten löschen, geschieht Folgendes: 

- **Für angepasste Attribute:** Entfernt dauerhaft die Attributdaten aus dem Profil jedes Nutzers:innen.
- **Für angepasste Events:** Entfernt dauerhaft die Ereignis-Metadaten aus dem Profil jedes Nutzers:innen.

Wenn ein Attribut oder ein Ereignis zum Löschen ausgewählt wird, ändert sich sein Status in **"Verworfen"**. Für die nächsten sieben Tage ist es möglich, das Attribut oder Ereignis wiederherzustellen. Wenn Sie sie nach sieben Tagen nicht wiederherstellen, werden die Daten endgültig gelöscht. Wenn Sie das Attribut oder das Ereignis wiederherstellen, wird es in den Zustand der Sperrliste zurückversetzt.

Das Löschen verhindert nicht die weitere Aufzeichnung der angepassten Datenobjekte in Nutzerprofilen. Stellen Sie also sicher, dass die angepassten Daten nicht mehr aufgezeichnet werden, bevor Sie das Ereignis oder Attribut löschen.

### Was Sie wissen sollten

Wenn Sie angepasste Daten löschen, sollten Sie die folgenden Details beachten:

* **Die Löschung ist dauerhaft**. Daten können nicht wiederhergestellt werden.
* Die Daten werden von der Braze-Plattform und aus den Nutzer:innen-Profilen entfernt.
* Sie können den Namen des angepassten Attributs oder den Namen des angepassten Events nach dem Löschen "wiederverwenden". Wenn Sie also feststellen, dass angepasste Daten nach dem Löschen in Braze "wieder auftauchen", kann dies durch eine Integration verursacht werden, die nicht gestoppt wurde und Daten mit demselben Namen für angepasste Daten sendet.
* Möglicherweise müssen Sie einen Artikel erneut auf die Sperrliste setzen, wenn Ihre Löschung dazu führt, dass angepasste Daten wieder auftauchen. Der Status der Sperrliste bleibt nicht erhalten, da die angepassten Daten gelöscht werden.
* Wenn Sie angepasste Daten löschen, werden keine [Datenpunkte]({{site.baseurl}}/user_guide/data/data_points) protokolliert und es werden auch keine neuen Datenpunkte zur Verwendung generiert.

## Erzwingen von Datentypvergleichen

Braze erkennt automatisch die Datentypen für Attribut-Daten, die an uns gesendet werden. Falls jedoch mehrere Datentypen auf ein einzelnes Attribut angewendet werden, können Sie den Datentyp eines beliebigen Attributs erzwingen, um uns mitzuteilen, um welchen Typ es sich handelt. Wählen Sie aus dem Dropdown-Menü in der Spalte **Datentyp**.

{% alert note %}
Das Erzwingen von Datentypen gilt nicht für Event-Eigenschaften oder Kauf-Details.
{% endalert %}

![Angepasste Attribute Datentyp Dropdown]({% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %})

{% alert warning %}
Wenn Sie den Datentyp für ein Attribut erzwingen möchten, werden alle Daten, die nicht dem angegebenen Typ entsprechen, in diesen Typ gezwungen. Wenn eine solche Umwandlung nicht möglich ist (z.B. wenn ein String mit Buchstaben in eine Zahl umgewandelt wird), werden die Daten ignoriert. Alle Daten, die vor der Änderung des Typs aufgenommen wurden, werden weiterhin als der alte Typ gespeichert (und können daher möglicherweise nicht segmentiert werden), und in den Profilen der betroffenen Nutzer:innen wird neben dem Attribut eine Warnung angezeigt.
{% endalert %}

### Zwang zum Datentyp

| Erzwungener Datentyp | Beschreibung |
|------------------|-------------|
| Boolesch | Die Eingaben von `1`, `true`, `t` (Groß- und Kleinschreibung wird nicht berücksichtigt) werden gespeichert als `true` |
| Boolesch | Die Eingaben von `0`, `false`, `f` (Groß- und Kleinschreibung wird nicht berücksichtigt) werden gespeichert als `false` |
| Zahl | Ganzzahlen oder Gleitkommazahlen (wie `1`, `1.5`) werden als Zahlen gespeichert. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Informationen zu den spezifischen Filteroptionen, die bei verschiedenen Datentypenvergleichen zur Verfügung stehen, finden Sie unter [Konfigurieren von Berichten]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting). Weitere Informationen zu den verschiedenen verfügbaren Datentypen finden Sie unter [Angepasste Attribut-Datentypen]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types).

{% alert note %}
An Braze gesendete Daten sind unveränderlich und können nicht gelöscht oder verändert werden, nachdem wir sie erhalten haben. Sie können jedoch jeden der in den vorangegangenen Abschnitten aufgeführten Schritte verwenden, um zu kontrollieren, was Sie in Ihrem Dashboard tracken.
{% endalert %}


