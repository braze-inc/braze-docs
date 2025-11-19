---
nav_title: SQL-Variablen
article_title: Query Builder SQL-Variablen
page_order: 2
page_type: reference
description: "Lernen Sie, wie Sie Variablen im Query Builder verwenden, damit Sie Ihre Abfragen wiederverwenden können und keine Daten in Ihrem Code fest codieren müssen."
tool: Reports
---

# Query Builder SQL-Variablen

> Lernen Sie, wie Sie SQL-Variablen im Query Builder verwenden, damit Sie Ihre Abfragen wiederverwenden können und keine Daten in Ihrem Code fest codieren müssen.

## Warum SQL-Variablen verwenden?

Zu den Vorteilen der Verwendung von SQL-Variablen gehören:

- Sparen Sie Zeit, indem Sie eine Kampagnenvariable erstellen, die Sie beim Erstellen Ihres Berichts aus einer Liste auswählen können, anstatt Kampagnen IDs einzufügen.
- Tauschen Sie Werte aus, indem Sie Variablen hinzufügen, um den Bericht in Zukunft für andere Anwendungsfälle wiederzuverwenden (z.B. für ein anderes angepasstes Event).
- Vermeiden Sie Nutzerfehler bei der Bearbeitung Ihres SQL, indem Sie den Bearbeitungsaufwand für Berichte möglichst gering halten. Teammitglieder, die mit SQL vertraut sind, können Berichte erstellen, die dann von technisch weniger versierten Teammitgliedern verwendet werden können.

## Variablen verwenden

### Schritt 1: Eine Variable hinzufügen

Um eine Variable zu Ihrer Abfrage hinzuzufügen, verwenden Sie die folgende Syntax:

{% raw %}
```sql
{{variable_type.${custom_label}}}
```
{% endraw %}

Ersetzen Sie Folgendes:

| Platzhalter      | Beschreibung                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `variable_type`   | Der vordefinierte Variablentyp, den Sie verwenden möchten, z. B. `campaign` oder `catalog_fields`. Die vollständige Liste finden Sie unter [Unterstützte Variablentypen](#variable-types). |
| `custom_label` | Der Bezeichner, der zur Identifizierung der Variablen im Tab **Variablen** Ihres Query Builders verwendet wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Im folgenden Beispiel wird die Gesamtzahl der Nutzer:innen zwischen dem ersten und letzten Tag eines Monats für eine Kampagne abgefragt. Jeder Variable wird im nächsten Schritt ein Wert zugewiesen.

{% raw %}
```sql
SELECT COUNT(*) AS total_users
FROM USERS_CAMPAIGNS_REVENUE_SHARED
WHERE campaign_id = '{{campaign.${Campaign}}}'
  AND TIME > '{{start_date.${Month First Day}}}'
  AND TIME < '{{end_date.${Month Last Day}}}';
```
{% endraw %}

### Schritt 2: Einen Wert zuweisen

Standardmäßig wird der Tab **Variablen** im Query Builder nicht angezeigt. Sie erscheint erst, nachdem Sie Ihre erste Variable zur Abfrage hinzugefügt haben. Dort können Sie ihm einen Wert zuweisen. Die spezifischen Werte, die Sie wählen können, hängen vom [Typ](#variable-types) der jeweiligen Variablen ab.

Im folgenden Beispiel wird die Kampagne "Summer Feature Launch" als Wert zugewiesen, zusammen mit dem ersten und letzten Tag des Juni 2025.

![Der Tab "Variable" im Query Builder mit dem angegebenen Beispiel.]({% image_buster /assets/img/query_builder_example.png %})

## Allgemeine Variablentypen {#variable-types}

### Zahl

`number` kann in Kombination mit anderen Nicht-String-Variablen verwendet werden. Akzeptiert jede positive oder negative Zahl, einschließlich Dezimalzahlen, wie `5.5`.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
some_number_column < {{number.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### String

Zum Ändern von sich wiederholenden String-Werten zwischen den Berichtsläufen. Verwenden Sie diese Variable, damit Werte nicht mehrfach in Ihrem SQL codiert werden.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
'{{string.${add a string here.}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Liste {#list}

Zum Auswählen aus einer Liste von Optionen.

{% tabs local %}
{% tab choose one %}
{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab choose multiple %}
{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Radiobutton

Für die Anzeige von Optionen als Radio-Buttons anstelle eines ausgewählten Dropdowns auf dem Tab " **Variablen"**. Dies kann nicht allein verwendet werden, sondern nur in Kombination mit einer [Liste](#list).

{% tabs %}
{% tab usage %}
```sql
is_radio_button: 'true'
```
{% endtab %}
{% endtabs %}

![Ein Beispiel für einen in Braze gerenderten Radio Button.]({% image_buster /assets/img_archive/sql_variables_campaigns.png %}){: style="max-width:50%;"}

#### Mehrfachauswahl

Ob das Dropdown-Menü Einfach- oder Mehrfachauswahl zulässt. Dies kann nicht allein verwendet werden, sondern nur in Kombination mit einer [Liste](#list).

{% tabs %}
{% tab usage %}
```sql
is_multi_select: 'true'
```
{% endtab %}
{% endtabs %}

![Ein Beispiel für eine in Braze gerenderte Mehrfachauswahlliste.]({% image_buster /assets/img_archive/sql_variables_productname.png %}){: style="max-width:50%;"}

#### Optionen 

Zur Bereitstellung der Liste auswählbarer Optionen mit Label und Wert. Die Beschriftung ist das, was angezeigt wird. Der Wert ersetzt die Variable, wenn die Option ausgewählt ist. Dies kann nicht allein verwendet werden, sondern nur in Kombination mit einer [Liste](#list).

{% tabs %}
{% tab usage %}
```sql
options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'
```
{% endtab %}
{% endtabs %}

## Braze-spezifische Variablentypen

### Datumsbereich

Zur Anzeige eines Kalenders, aus dem Sie Daten auswählen können. Ersetzen Sie `start_date` und `end_date` durch einen Unix-Zeitstempel in Sekunden für ein bestimmtes Datum in UTC, z. B. `1696517353`. Optional können Sie auch nur ein `start_date` oder `end_date` einstellen, um nur ein einziges Datum im Kalender anzuzeigen. Wenn die Beschriftungen Ihrer `start_date` und `end_date` nicht übereinstimmen, werden sie als zwei getrennte Daten und nicht als ein Datumsbereich behandelt.

{% tabs %}
{% tab usage %}
{% raw %}
```
time > {{start_date.${custom_label}}} AND time < {{end_date.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

Sie können den Datumsbereich auf eine der folgenden Optionen einstellen. Wenn sowohl `start_date` als auch `end_date` verwendet werden und dieselbe Bezeichnung haben, werden alle Optionen angezeigt. Andernfalls, wenn nur eine Option verwendet wird, wird nur die angegebene Option angezeigt.

| Option | Beschreibung | Erforderliche Werte |
| --- | --- | --- |
| Relativ | Gibt die letzten X Tage an | Erfordert `start_date` |
| Startdatum | Gibt ein Anfangsdatum an | Erfordert `start_date` |
| Enddatum | Gibt ein Abschlussdatum an | Erfordert `end_date` |
| Datumsbereich | Gibt sowohl ein Start- als auch ein Enddatum an | Benötigt sowohl `start_date` als auch `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Ihr Liquid wird verwendet, um einen Kalender innerhalb des angegebenen Datumsbereichs anzuzeigen:

![Ein in Braze gerenderter Beispielkalender.]({% image_buster /assets/img_archive/query_builder_time_range.png %}){: style="max-width:50%;"}

### Kampagnen

{% tabs local %}
{% tab one campaign %}
Zum Auswählen einer Kampagne. Wenn Sie dasselbe Etikett mit einem Canvas teilen, wird auf dem Tab **Variablen** ein Button angezeigt, mit dem Sie entweder ein Canvas oder eine Kampagne auswählen können.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
campaign_id = '{{campaign.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab multiple campaigns %}
Für Kampagnen mit Mehrfachauswahl. Wenn Sie dasselbe Etikett mit einem Canvas verwenden, wird auf dem Tab **Variablen** ein Button angezeigt, über den Sie entweder ein Canvas oder eine Kampagne auswählen können.

- **Ersatzwert:** Kampagnen BSON IDs

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
campaign_id IN ({{campaigns.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab campaign variants %}
Zum Auswählen von Kampagnenvarianten, die zu der ausgewählten Kampagne gehören. Sie muss in Verbindung mit einer Kampagne oder Kampagnen-Variablen verwendet werden.

- **Ersatzwert:** Kampagnenvarianten API IDs, durch Kommas getrennte Strings wie z.B. `api-id1, api-id2`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
message_variation_api_id IN ({{campaign_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Alle Kampagnen- und Canvas-Variablen müssen die gleichen Bezeichner verwenden, um die Zustände innerhalb einer Gruppe zu synchronisieren.
{% endalert %}

### Canvase

{% tabs local %}
{% tab one canvas %}
Zur Auswahl eines Canvas. Wenn Sie dasselbe Etikett mit einer Kampagne teilen, wird auf dem Tab **Variablen** ein Button angezeigt, mit dem Sie entweder Canvas oder Kampagne auswählen können.

- **Ersatzwert:** Canvas BSON ID

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_id = '{{canvas.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab multiple canvases %}
Zum Auswählen mehrerer Canvase. Wenn Sie dasselbe Etikett mit einer Kampagne teilen, wird auf dem Tab **Variablen** ein Button angezeigt, mit dem Sie entweder Canvas oder Kampagne auswählen können.

- **Ersatzwert:** BSON-IDs von Canvasen

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_id IN ({{canvases.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab canvas variants %}
Zum Auswählen von Canvas-Varianten, die zu einem gewählten Canvas gehören. Sie muss mit einer Canvas- oder Canvase-Variablen verwendet werden. Setzen Sie auf eine oder mehrere Canvas-Varianten API IDs, als kommagetrennter String, wie in `api-id1, api-id2`.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_variation_api_id IN ({{canvas_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab one canvas step %}
Zum Auswählen eines Canvas-Schrittes, der zu einem gewählten Canvas gehört. Sie muss mit einer Canvas-Variablen verwendet werden.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_step_api_id = '{{canvas_step.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab multiple canvas steps %}
Zum Auswählen von Canvas-Schritten, die zu den gewählten Canvase gehören. Sie muss mit einer Canvas- oder Canvase-Variablen verwendet werden.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
canvas_step_api_id IN ({{canvas_steps.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
Alle Kampagnen- und Canvas-Variablen müssen die gleichen Bezeichner verwenden, um die Zustände innerhalb einer Gruppe zu synchronisieren.
{% endalert %}

### Produkte

`products` wird verwendet, um ein oder mehrere Produkte aus dem Braze-Dashboard auszuwählen.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
({{products.${custom_label}}})
```
{% endraw %}
{% endtab %}

{% tab example %}
{% raw %}
```sql
SELECT product_name
FROM FULL_GAME_AND_DLC
WHERE product_id IN ({{products.${Games with DLC}}});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Angepasste Events

Wählen Sie ein oder mehrere angepasste Events oder angepasste Event-Eigenschaften aus einer Liste aus.

{% tabs local %}
{% tab event %}
`custom_events` wird verwendet, um ein oder mehrere angepasste Events aus dem Braze-Dashboard auszuwählen.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
'{{custom_events.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}

{% subtab example %}
{% raw %}
```sql
SELECT event_name
FROM CUSTOM_EVENTS_TABLE
WHERE event_name IN ({{custom_events.${Purchased Game}}}); 
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab properties %}
`custom_event_properties` wird verwendet, um eine oder mehrere Eigenschaften aus dem aktuell ausgewählten angepassten Event auszuwählen.  Erfordert eine gesetzte `custom_events` Variable.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
name = '{{custom_event_properties.${property names)}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Workspace

`workspace` wird verwendet, um einen einzelnen Workspace aus dem Braze-Dashboard auszuwählen.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
workspace_id = '{{workspace.${app_group_id}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Kataloge

Wählen Sie ein oder mehrere Katologe oder Katologfelder aus einer Liste aus.

{% tabs local %}
{% tab catologs %}
`catalogs` wird verwendet, um ein oder mehrere Kataloge aus dem Braze-Dashboard auszuwählen.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
catalog_id = '{{catalogs.${catalog}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab catolog fields %}
`catalog_fields` wird verwendet, um ein oder mehrere Felder aus dem aktuell ausgewählten Katalog einzustellen. Erfordert eine gesetzte `catalogs` Variable.

{% subtabs %}
{% subtab usage %}
{% raw %}
```sql
field_name = '{{catalog_fields.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Segmente

Zum Auswählen von Segmenten, für die [Analytics Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) aktiviert ist. Setzen Sie dies auf die Analytics ID des Segments, die den IDs entspricht, die in der Spalte `user_segment_membership_ids` in den Tabellen gespeichert sind, in denen diese Spalte verfügbar ist.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{segments.${analytics_segments}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Tags

Zum Auswählen von Tags für Kampagnen und Canvase. Setzen Sie auf Kampagnen und Canvase mit durch Kommata getrennten BSON IDs, die mit den ausgewählten Tags verknüpft sind.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{tags.${some tags}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Variable Metadaten

Metadaten können an eine Variable angehängt werden, um ihr Verhalten zu ändern, indem Sie die Metadaten mit einem Pipe-Zeichen ( | ) nach der Variablenbezeichnung anhängen. Die Reihenfolge der Metadaten spielt keine Rolle und Sie können eine beliebige Anzahl von Metadaten anhängen. Außerdem können alle Arten von Metadaten für jede Variable verwendet werden, mit Ausnahme spezieller Metadaten, die für bestimmte Variablen spezifisch sind (dies wird in diesen Fällen angegeben). Die Verwendung aller Metadaten ist optional und dient dazu, das Verhalten der Variablen des Standards zu ändern.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{string.${my var}| is_required: 'false' | description: 'My optional string var'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Boolesch

Um zu wissen, ob der Wert einer Variablen gefüllt ist. Dies ist nützlich für optionale Variablen, bei denen Sie eine Bedingung kurzschließen möchten, wenn der Wert einer Variablen nicht gefüllt ist. Kann auf `true` oder `false` gesetzt werden, je nach dem Wert der anderen Variablen.

{% tabs %}
{% tab usage %}
{% raw %}
```sql
{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

`type` und `name` referenzieren auf die referenzierte Variable. Zum Beispiel, um die folgende optionale Variable kurzzuschließen: {% raw %}`{{campaigns.${messaging}}`{% endraw %}:

{% raw %}
```sql
{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: 'false'}})
```
{% endraw %}

### Sichtbar

Dafür, ob Variablen sichtbar sind. Alle Variablen sind standardmäßig auf dem Tab **Variablen** sichtbar, wo Sie Werte eingeben können.

Es gibt einige spezielle Variablen, deren Wert von einer anderen Variable oder deren Wert abhängt. Diese speziellen Variablen sind als nicht sichtbar markiert, so dass sie auf dem Tab **Variablen** nicht angezeigt werden.

{% tabs %}
{% tab usage %}
```sql
visible: 'false'
```
{% endtab %}
{% endtabs %}

### Erforderlich

Für die Frage, ob Variablen standardmäßig erforderlich sind. Ein leerer Wert für eine Variable führt normalerweise zu einem Abfragefehler.

{% tabs %}
{% tab usage %}
```sql
required: 'false'
```
{% endtab %}
{% endtabs %}

### Bestellung

Zum Auswählen der Position der Variablen auf dem Tab **Variablen**.

{% tabs %}
{% tab usage %}
```sql
order: '1'
```
{% endtab %}
{% endtabs %}

### Zitate einbeziehen

{% tabs local %}
{% tab single quotes %}
Umgeben Sie die Werte einer Variablen mit einfachen Anführungszeichen.

{% subtabs %}
{% subtab usage %}
```sql
include_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab double quotes %}
Umgeben Sie die Werte einer Variablen mit doppelten Anführungszeichen.

{% subtabs %}
{% subtab usage %}
```sql
include_double_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Platzhalter

Zum Festlegen des Platzhaltertextes, der im Eingabefeld der Variablen angezeigt wird.

{% tabs %}
{% tab usage %}
```sql
placeholder: 'enter some value'
```
{% endtab %}
{% endtabs %}

### Beschreibung

Zum Festlegen des Beschreibungstextes, der unter dem Eingabefeld der Variablen angezeigt wird.

{% tabs %}
{% tab usage %}
```sql
description: 'some description'
```
{% endtab %}
{% endtabs %}

### Standardwert

Zum Festlegen des Standardwerts für die Variable, wenn kein Wert angegeben ist.

{% tabs %}
{% tab usage %}
```sql
default_value: '5'
```
{% endtab %}
{% endtabs %}

### Etikett ausblenden

Um die Beschriftung der Variablen auszublenden.

{% tabs %}
{% tab usage %}
```sql
hide_label: 'true'
```
{% endtab %}
{% endtabs %}
