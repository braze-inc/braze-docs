---
nav_title: Angepasste Daten verwalten
article_title: Angepasste Daten verwalten
page_order: 20
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie angepasste Daten verwalten, z. B. Kampagnen und Segmente vorbelegen oder Daten blockieren und löschen."
---

# Angepasste Daten verwalten

> Auf dieser Seite erfahren Sie, wie Sie angepasste Daten in Ihren Kampagnen und Segmenten vorbelegen, nicht mehr benötigte Daten blockieren und angepasste Events, Attribute sowie Eigenschaften verwalten können.<br><br>Wie Sie angepasste Attribute im Einzelnen verwalten, erfahren Sie unter [Angepasste Attribute verwalten]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes).

## Angepasste Daten vorbelegen

Es kann vorkommen, dass Sie Kampagnen und Segmente mit angepassten Daten einrichten möchten, bevor Ihr Entwicklerteam diese angepassten Daten integriert hat. Braze ermöglicht es Ihnen, angepasste Events und Attribute im Dashboard vorzubelegen, bevor das Tracking dieser Daten beginnt, sodass diese Events und Attribute in Dropdowns und als Teil des Kampagnenerstellungsprozesses verfügbar sind.

Um angepasste Events und Attribute vorzubelegen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Dateneinstellungen** > **Angepasste Events** oder **Angepasste Attribute** oder **Produkte**.

![Navigieren Sie zu Angepasste Attribute oder Angepasste Events oder Produkte.]({% image_buster /assets/img_archive/prepopulate_page.png %}){: style="max-width:90%;" }

{: start="2"}
2. Um ein angepasstes Attribut, Event oder Produkt hinzuzufügen, gehen Sie auf die entsprechende Seite und wählen Sie **Angepasste Attribute hinzufügen** oder **Angepasste Events hinzufügen** oder **Produkte hinzufügen**.<br><br>Für angepasste Attribute wählen Sie einen [Datentyp]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) für dieses Attribut aus (z. B. Boolescher Wert oder String). Der Datentyp eines Attributs bestimmt die Segmentierungsfilter, die für dieses Attribut verfügbar sind. <br><br>![Neues Attribut oder Event hinzufügen]({% image_buster /assets/img_archive/prepopulate_add.png %}){: style="max-width:80%;" }
3. Wählen Sie **Speichern**.

### Benennung angepasster Events und angepasster Attribute

Bei angepassten Events und angepassten Attributen wird zwischen Groß- und Kleinschreibung unterschieden. Behalten Sie dies im Hinterkopf, wenn Ihr Entwicklerteam diese angepassten Events oder Attribute später integriert. Die angepassten Events oder Attribute müssen genau so benannt werden, wie Sie sie hier benannt haben, sonst generiert Braze ein anderes angepasstes Event oder Attribut.

## Eigenschaften verwalten

Nachdem Sie ein angepasstes Event oder Produkt erstellt haben, wählen Sie **Eigenschaften verwalten** für dieses Event oder Produkt aus, um neue Eigenschaften hinzuzufügen, vorhandene Eigenschaften zu blockieren und zu sehen, welche Kampagnen oder Canvase diese Eigenschaft in einem [triggernden Event]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) verwenden.

![Angepasste Eigenschaften für ein angepasstes Event.]({% image_buster /assets/img_archive/manageproperties1.png %}){: style="max-width:80%"}

Um diese hinzugefügten angepassten Attribute, Events, Produkte oder Event-Eigenschaften nachverfolgbar zu machen, müssen Sie Ihr Entwicklerteam bitten, sie im SDK unter genau dem Namen zu erstellen, den Sie zuvor verwendet haben. Alternativ können Sie die Braze [API]({{site.baseurl}}/api/basics/) verwenden, um Daten zu diesem Attribut zu importieren. Danach ist das angepasste Attribut, Event oder andere Datenobjekt aktiv und wird auf Ihre Nutzer:innen angewendet.

{% multi_lang_include alerts/note_alerts.md alert='Manage custom data storage' %}

## Angepasste Daten blockieren

Gelegentlich stellen Sie fest, dass angepasste Attribute, angepasste Events oder Kauf-Events entweder zu viele Datenpunkte protokollieren, für Ihre Marketingstrategie nicht mehr nützlich sind oder versehentlich aufgezeichnet wurden.

Um zu verhindern, dass diese Daten an Braze gesendet werden, können Sie ein angepasstes Datenobjekt auf die Blockliste setzen, während Ihr Entwicklerteam daran arbeitet, es aus dem Backend Ihrer App oder Website zu entfernen. Die Blockliste verhindert, dass ein bestimmtes angepasstes Datenobjekt von Braze aufgezeichnet wird, d. h. es wird bei der Suche nach einer bestimmten Nutzer:in nicht mehr angezeigt.

Daten auf der Blockliste werden nicht vom SDK gesendet, und das Braze-Dashboard verarbeitet keine blockierten Daten aus anderen Quellen (z. B. der API). Durch die Blockierung werden jedoch keine Daten aus Nutzerprofilen entfernt oder die Anzahl der Datenpunkte, die für dieses angepasste Datenobjekt angefallen sind, rückwirkend verringert.

### Erforderliche Berechtigungen

Um angepasste Daten zu blockieren, benötigen Sie die [Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) im folgenden Dropdown-Menü für Ihren Workspace.

{% details Berechtigungen für das Blockieren angepasster Daten %}

{% multi_lang_include deprecations/user_permissions.md %}

- Kampagnen anzeigen
- Kampagnen bearbeiten
- Kampagnen archivieren
- Canvase anzeigen
- Canvase bearbeiten
- Canvase archivieren
- Frequency-Capping-Regeln anzeigen
- Frequency-Capping-Regeln bearbeiten
- Nachrichtenpriorisierung anzeigen
- Nachrichtenpriorisierung bearbeiten
- Content-Blöcke anzeigen
- Feature-Flags anzeigen
- Feature-Flags bearbeiten
- Feature-Flags archivieren
- Segmente anzeigen
- Segmente bearbeiten
- IAM-Templates anzeigen
- IAM-Templates bearbeiten
- IAM-Templates archivieren
- E-Mail-Templates anzeigen
- E-Mail-Templates bearbeiten
- E-Mail-Templates archivieren
- Webhook-Templates anzeigen
- Webhook-Templates bearbeiten
- Webhook-Templates archivieren
- E-Mail-Link-Templates anzeigen
- E-Mail-Link-Templates bearbeiten
- Mediathek-Assets anzeigen
- Mediathek-Assets bearbeiten
- Mediathek-Assets löschen
- Standorte anzeigen
- Standorte bearbeiten
- Standorte archivieren
- Aktionscodes anzeigen
- Aktionscodes bearbeiten
- Aktionscodes exportieren
- Präferenzzentren anzeigen
- Präferenzzentren bearbeiten
- Berichte anzeigen
- Berichte bearbeiten

{% enddetails %}

### Angepasste Attribute, angepasste Events und Produkte blockieren

{% alert important %}
Wenn ein Event oder Attribut auf der Blockliste steht, werden alle Segmente, Kampagnen oder Canvase, die dieses Event oder Attribut verwenden, archiviert.
{% endalert %}

Um das Tracking eines bestimmten angepassten Attributs, Events oder Produkts zu beenden, gehen Sie folgendermaßen vor:

1. Suchen Sie danach auf den Seiten **Angepasste Attribute**, **Angepasste Events** oder **Produkte**.
2. Wählen Sie das angepasste Attribut, Event oder Produkt aus. Für angepasste Attribute und Events können Sie bis zu 100 gleichzeitig auswählen, um sie zu blockieren.
3. Wählen Sie **Blockliste**.

![Mehrere ausgewählte angepasste Attribute, die auf der Seite „Angepasste Attribute" blockiert sind.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Sie können bis zu 300 angepasste Attribute und 300 angepasste Events auf die Blockliste setzen. Um die Erfassung bestimmter Geräteattribute zu verhindern, lesen Sie unseren [SDK-Leitfaden]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection).

{% alert important %}
Angepasste Attribute oder angepasste Events mit dem Status **Verworfen** werden auf das Blocklisting-Limit angerechnet, bis sie gelöscht werden.
{% endalert %}

Wenn ein angepasstes Event oder Attribut auf der Blockliste steht, gilt Folgendes:

- Es werden keine an Braze gesendeten Daten verarbeitet, und blockierte Events und Attribute zählen nicht mehr als Datenpunkte
- Vorhandene Daten sind nicht verfügbar, sofern sie nicht reaktiviert werden
- Blockierte Events und Attribute werden in Filtern und Diagrammen nicht angezeigt
- Referenzen auf blockierte Daten in Entwürfen aktiver Canvase werden als ungültige Werte geladen, was zu Fehlern führen kann
- Alles, was das blockierte Event oder Attribut verwendet, wird archiviert

Um dies zu erreichen, sendet Braze die Blocklisting-Informationen an jedes Gerät. Dies ist wichtig, wenn Sie eine große Anzahl von Events und Attributen (Hunderttausende oder Millionen) blockieren möchten, da dies eine datenintensive Operation wäre.

### Überlegungen zum Blockieren

Das Blockieren einer großen Anzahl von Events und Attributen ist möglich, aber nicht ratsam. Das liegt daran, dass jedes Mal, wenn ein Event ausgeführt oder ein Attribut (möglicherweise) an Braze gesendet wird, dieses Event oder Attribut mit der gesamten Blockliste abgeglichen werden muss.

Bis zu 300 Einträge werden an das SDK für die Blockierung gesendet. Wenn Sie mehr als 300 Einträge blockieren, werden diese Daten trotzdem vom SDK gesendet. Wenn Sie das Event oder Attribut in Zukunft nicht mehr benötigen, sollten Sie es bei der nächsten Version aus dem Code Ihrer App entfernen. Es kann einige Minuten dauern, bis Änderungen an der Blockliste übernommen werden. Sie können jedes blockierte Event oder Attribut jederzeit wieder aktivieren.

## Angepasste Daten löschen

Wenn Sie zielgerichtete Kampagnen und Segmente erstellen, stellen Sie möglicherweise fest, dass Sie ein angepasstes Event oder angepasstes Attribut nicht mehr benötigen. Wenn Sie beispielsweise ein bestimmtes angepasstes Attribut als Teil einer einmaligen Kampagne verwendet haben, können Sie diese Daten nach dem [Blockieren](#blocklisting-custom-attributes-custom-events-and-products) löschen und die Referenzen aus Ihrer App entfernen. Sie können beliebige Datentypen löschen (z. B. Strings, Zahlen und verschachtelte angepasste Attribute).

{% alert important %}
Sie müssen [Braze-Administrator:in]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) sein, um angepasste Daten zu löschen.
{% endalert %}

Um ein angepasstes Event oder angepasstes Attribut zu löschen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Dateneinstellungen** > **Angepasste Attribute** oder **Angepasste Events**, je nachdem, welchen Datentyp Sie löschen möchten.
2. Gehen Sie zu den angepassten Daten und wählen Sie <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Aktionen** > **Blockliste**.
3. Nachdem Ihre angepassten Daten 7 Tage lang auf der Blockliste standen, wählen Sie <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Aktionen** > **Löschen**.

### So funktioniert die Löschung

Wenn Sie angepasste Daten löschen, geschieht Folgendes:

- **Für angepasste Attribute:** Entfernt die Attributdaten dauerhaft aus dem Profil jeder Nutzer:in.
- **Für angepasste Events:** Entfernt die Event-Metadaten dauerhaft aus dem Profil jeder Nutzer:in.

Wenn ein Attribut oder Event zum Löschen ausgewählt wird, ändert sich sein Status in **Verworfen**. In den nächsten sieben Tagen ist es möglich, das Attribut oder Event wiederherzustellen. Wenn Sie es nach sieben Tagen nicht wiederherstellen, werden die Daten endgültig gelöscht. Wenn Sie das Attribut oder Event wiederherstellen, wird es in den blockierten Zustand zurückversetzt.

Das Löschen verhindert nicht die weitere Aufzeichnung der angepassten Datenobjekte in Nutzerprofilen. Stellen Sie daher sicher, dass die angepassten Daten nicht mehr aufgezeichnet werden, bevor Sie das Event oder Attribut löschen.

### Was Sie wissen sollten

Wenn Sie angepasste Daten löschen, beachten Sie die folgenden Details:

* **Die Löschung ist dauerhaft.** Daten können nicht wiederhergestellt werden.
* Daten werden von der Braze-Plattform und aus den Nutzerprofilen entfernt.
* Sie können den Namen des angepassten Attributs oder des angepassten Events nach dem Löschen „wiederverwenden". Wenn Sie also feststellen, dass angepasste Daten nach dem Löschen in Braze „wieder auftauchen", kann dies durch eine Integration verursacht werden, die nicht gestoppt wurde und Daten mit demselben angepassten Datennamen sendet.
* Möglicherweise müssen Sie einen Eintrag erneut blockieren, wenn Ihre Löschung dazu führt, dass angepasste Daten wieder auftauchen. Der Blockierungsstatus bleibt nicht erhalten, da die angepassten Daten gelöscht werden.
* Das Löschen angepasster Daten protokolliert keine [Datenpunkte]({{site.baseurl}}/user_guide/data/data_points) und generiert auch keine neuen Datenpunkte.

## Datentypvergleiche erzwingen

Braze erkennt automatisch die Datentypen für Attributdaten, die an uns gesendet werden. Falls jedoch mehrere Datentypen auf ein einzelnes Attribut angewendet werden, können Sie den Datentyp eines beliebigen Attributs erzwingen, um uns mitzuteilen, um welchen Typ es sich handelt. Wählen Sie aus dem Dropdown-Menü in der Spalte **Datentyp**.

{% alert note %}
Das Erzwingen von Datentypen gilt nicht für Event-Eigenschaften oder Kauf-Details.
{% endalert %}

![Dropdown für den Datentyp angepasster Attribute]({% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %})

{% alert warning %}
Wenn Sie den Datentyp für ein Attribut erzwingen, werden alle eingehenden Daten, die nicht dem angegebenen Typ entsprechen, in diesen Typ umgewandelt. Wenn eine solche Umwandlung nicht möglich ist (z. B. ein String mit Buchstaben, der in eine Zahl umgewandelt werden soll), werden die Daten ignoriert. Alle Daten, die vor der Typänderung aufgenommen wurden, werden weiterhin als der alte Typ gespeichert (und können daher möglicherweise nicht segmentiert werden), und in den Profilen der betroffenen Nutzer:innen wird neben dem Attribut eine Warnung angezeigt.
{% endalert %}

### Datentypumwandlung

| Erzwungener Datentyp | Beschreibung |
|------------------|-------------|
| Boolescher Wert | Eingaben von `1`, `true`, `t` (Groß-/Kleinschreibung wird nicht berücksichtigt) werden als `true` gespeichert |
| Boolescher Wert | Eingaben von `0`, `false`, `f` (Groß-/Kleinschreibung wird nicht berücksichtigt) werden als `false` gespeichert |
| Zahl | Ganzzahlen oder Gleitkommazahlen (wie `1`, `1.5`) werden als Zahlen gespeichert |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Informationen zu den spezifischen Filteroptionen, die bei verschiedenen Datentypvergleichen zur Verfügung stehen, finden Sie unter [Berichte konfigurieren]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting). Weitere Informationen zu den verschiedenen verfügbaren Datentypen finden Sie unter [Datentypen angepasster Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types).

{% alert note %}
An Braze gesendete Daten sind unveränderlich und können nicht gelöscht oder verändert werden, nachdem wir sie erhalten haben. Sie können jedoch jeden der in den vorangegangenen Abschnitten aufgeführten Schritte verwenden, um zu kontrollieren, was Sie in Ihrem Dashboard tracken.
{% endalert %}