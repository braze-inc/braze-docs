---
nav_title: Abfrage-Builder
article_title: Abfrage-Builder
page_order: 15
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie mit dem Abfrage-Builder Berichte mit Braze-Daten aus Snowflake erstellen können."
tool: Reports
---

# Abfrage-Builder

> Der Query Builder erstellt Berichte unter Verwendung von Braze Daten in Snowflake. Der Query Builder wird mit vorgefertigten [SQL-Anfragen-Templates]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) geliefert, die Ihnen den Einstieg erleichtern. Sie können aber auch Ihre eigenen angepassten SQL-Anfragen schreiben, um noch mehr Insights zu erhalten.

Da der Abfrage-Builder den direkten Zugriff auf einige Kundendaten erlaubt, können Sie nur darauf zugreifen, wenn Sie die [Berechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) "PII anzeigen" haben.

## Ausführen von Berichten im Abfrage-Builder

So führen Sie einen Query Builder-Bericht aus:

1. Gehen Sie zu **Analytics** > **Query Builder**.
2. Wählen Sie **SQL-Abfrage erstellen**. Wenn Sie Inspiration oder Hilfe bei der Gestaltung Ihrer Anfrage benötigen, wählen Sie **Abfragevorlage** und wählen Sie eine Vorlage aus der Liste. Andernfalls wählen Sie **SQL Editor**, um direkt zum Editor zu gelangen.
3. Ihr Bericht erhält automatisch einen Namen mit dem aktuellen Datum und der Uhrzeit. Bewegen Sie den Mauszeiger über den Namen und wählen Sie <i class="fas fa-pencil" alt="Edit"></i>, um Ihrer SQL-Abfrage einen aussagekräftigen Namen zu geben.
4. Verfassen Sie Ihre SQL-Abfrage im Editor oder [lassen Sie sich von der KI](#ai-query-builder) im Tab **Abfrage-Builder** helfen. Wenn Sie Ihr eigenes SQL schreiben, finden Sie unter Anforderungen und Ressourcen unter [Anpassen von SQL-Anfragen](#custom-sql).
5. Wählen Sie **Abfrage ausführen**.
6. Speichern Sie Ihre Anfrage.
7. Um eine CSV-Datei mit Ihrem Bericht herunterzuladen, wählen Sie **Exportieren**.

![Der Abfrage-Builder zeigt die Ergebnisse zur Template-Abfrage "Engagement und Umsatz auf diesem Kanal in den letzten 30 Tagen".]({% image_buster /assets/img_archive/query_builder.png %})

Die Ergebnisse der einzelnen Berichte können einmal pro Tag erstellt werden. Wenn Sie denselben Bericht mehr als einmal pro Kalendertag ausführen, enthalten beide Berichte dieselben Ergebnisse.

### Templates für Abfragen

Greifen Sie auf Abfragevorlagen zu, indem Sie beim ersten Erstellen eines Berichts **SQL-Abfrage erstellen** > **Abfragevorlage** auswählen.

Unter [Abfragevorlagen]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) finden Sie eine Liste der verfügbaren Templates.

### Datenzeitraum

Alle Abfragen beziehen sich auf die Daten der letzten 60 Tage. 

## SQL per Abfrage-Builder mit KI generieren

Der Abfrage-Builder mit KI nutzt [GPT](https://openai.com/gpt-4) von OpenAI, um SQL für Ihre Abfrage zu empfehlen.

![][2]{: style="max-width:60%;" }

So erzeugen Sie SQL per KI im Abfrage-Builder:

1. Wenn Sie einen Bericht im Abfrage-Builder erstellt haben, wählen Sie den Tab **Abfrage-Builder mit KI**.
2. Geben Sie Ihren Prompt ein oder wählen Sie einen Beispielprompt aus und wählen Sie **Generieren**, um Ihren Prompt in SQL zu übersetzen.
3. Überprüfen Sie das generierte SQL auf Richtigkeit und wählen Sie dann **In Editor einfügen**.

### Tipps

- Machen Sie sich mit den verfügbaren [Snowflake Datentabellen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) vertraut. Wenn Sie nach Daten fragen, die in diesen Tabellen nicht vorhanden sind, kann es sein, dass ChatGPT eine gefälschte Tabelle erstellt.
- Machen Sie sich mit den [SQL-Schreibregeln]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) für dieses Feature vertraut. Die Nichtbeachtung dieser Regeln führt zu einem Fehler.
- Sie können bis zu 20 Prompts pro Minute senden.

### Wie werden meine Daten verwendet und an OpenAI gesendet?
<!-- Contact Legal for changes. -->

Um Ihr SQL zu generieren, sendet Braze Ihre Prompts an die API-Plattform von OpenAI. Alle Abfragen, die von Braze an OpenAI gesendet werden, sind anonymisiert, d.h. OpenAI kann nicht feststellen, von wem die Abfrage gesendet wurde, es sei denn, Sie enthalten eindeutige Bezeichner in den von Ihnen bereitgestellten Inhalten. Wie in den [API Platform Commitments von OpenAI](https://openai.com/policies/api-data-usage-policies) beschrieben, werden Daten, die über Braze an die API von OpenAI gesendet werden, nicht zum Trainieren oder Verbessern ihrer Modelle verwendet und nach 30 Tagen gelöscht. Bitte stellen Sie sicher, dass Sie sich an die für Sie relevanten Richtlinien von OpenAI halten, einschließlich der [Nutzungsrichtlinie](https://openai.com/policies/usage-policies). Braze übernimmt keinerlei Garantie in Bezug auf KI-generierte Inhalte. 

## Anpassen von SQL-Anfragen {#custom-sql}

Schreiben Sie Ihre SQL-Abfrage mit der [Snowflake-Syntax](https://docs.snowflake.com/en/sql-reference). In der [Tabellenreferenz]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) finden Sie eine vollständige Liste der Tabellen und Spalten, die abgefragt werden können.

Um Tabellendetails im Query Builder anzuzeigen:

1. Öffnen Sie auf der Seite **Query Builder** das Panel **Referenz** und wählen Sie **Verfügbare Datentabellen**, um die verfügbaren Datentabellen und ihre Namen anzuzeigen.
3. Wählen Sie <i class="fas fa-chevron-down" alt=""></i> **Details ansehen**, um die Tabellenbeschreibung und Informationen über die Tabellenspalten, wie z.B. Datentypen, anzuzeigen.
4. Um den Tabellennamen in Ihr SQL einzufügen, wählen Sie <i class="fas fa-copy" title="Tabellenname in SQL-Editor kopieren"></i>.

Um von Braze bereitgestellte vorgefertigte Abfragen zu verwenden, wählen Sie **Abfragevorlage**, wenn Sie zum ersten Mal einen Bericht im Abfrage-Builder erstellen.

Wenn Sie Ihre Abfrage auf einen bestimmten Zeitraum beschränken, können Sie schneller Ergebnisse erzielen. Hier eine Beispielabfrage, die die Anzahl der Käufe und die in der letzten Stunde erzielten Einnahmen ermittelt.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

Diese Abfrage ruft die Anzahl der E-Mails ab, die im letzten Monat versendet wurden:

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

Wenn Sie nach den Spalten `CANVAS_ID`, `CANVAS_VARIATION_API_ID` oder `CAMPAIGN_ID` suchen, werden die zugehörigen Namensspalten automatisch in die Ergebnistabelle aufgenommen. Sie müssen sie nicht in die `SELECT` Abfrage selbst aufnehmen.

| ID Name | Spalte "Zugehöriger Name" |
| --- | --- |
| `CANVAS_ID` | Canvas-Name |
| `CANVAS_VARIATION_API_ID` | Canvas-Variante Name |
| `CAMPAIGN_ID` | Kampagnenname |
{: .reset-td-br-1 .reset-td-br-2 }

Diese Abfrage ruft alle drei IDs und ihre zugehörigen Namensspalten mit maximal 100 Zeilen ab:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED 
LIMIT 100
```

### Fehlerbehebung

Ihre Abfrage kann aus einem der folgenden Gründe fehlschlagen:

- Syntaxfehler in Ihrer SQL-Abfrage
- Zeitüberschreitung (nach 6 Minuten)
    - Bei Berichten, deren Erstellung länger als 6 Minuten dauert, tritt ein Timeout ein.
    - Versuchen Sie in diesem Fall, den Zeitraum Ihrer Datenabfrage zu verkürzen oder einen begrenzteren Datensatz abzufragen.

## Variablen verwenden

Verwenden Sie Variablen, um mit vordefinierten SQL-Variablentypen Werte zu referenzieren, ohne diese manuell kopieren zu müssen. Anstatt die ID einer Kampagne manuell in den SQL-Editor zu kopieren, können Sie beispielsweise mit {% raw %}`{{campaign.${My campaign}}}`{% endraw %} direkt eine Kampagne aus einem Dropdown-Menü auf dem Tab **Variablen** auswählen.

![][3]

Nachdem eine Variable erstellt wurde, erscheint sie auf dem Tab **Variablen** in Ihrem Query Builder-Bericht. Zu den Vorteilen der Verwendung von SQL-Variablen gehören:

- Sparen Sie Zeit, indem Sie eine Kampagnenvariable erstellen, die Sie beim Erstellen Ihres Berichts aus einer Liste auswählen können, anstatt Kampagnen IDs einzufügen.
- Tauschen Sie Werte aus, indem Sie Variablen hinzufügen, um den Bericht in Zukunft für andere Anwendungsfälle wiederzuverwenden (z.B. für ein anderes angepasstes Event).
- Vermeiden Sie Nutzerfehler bei der Bearbeitung Ihres SQL, indem Sie den Bearbeitungsaufwand für Berichte möglichst gering halten. Teammitglieder, die mit SQL vertraut sind, können Berichte erstellen, die dann von technisch weniger versierten Teammitgliedern verwendet werden können.

### Leitlinien

Variablen müssen sich an die folgende Liquid-Syntax halten: {% raw %}`{{ type.${name}}}`{% endraw %}, wobei `type` einer der akzeptierten Typen sein muss und `name` ein beliebiger Typ sein kann. Die Bezeichnungen für diese Variablen entsprechen standardmäßig dem Variablennamen.

Standardmäßig sind alle Variablen Pflichtfelder (und Ihr Bericht wird nur ausgeführt, wenn die Variablenwerte ausgewählt sind), mit Ausnahme des Datumsbereichs, der standardmäßig auf die letzten 30 Tage eingestellt ist, wenn der Wert nicht angegeben wird.

### Variable Typen

Die folgenden Variablentypen werden akzeptiert:

- [Zahl](#number)
- [Datumsbereich](#date-range)
- [Messaging](#messaging)
- [Produkte](#products)
- [Angepasste Events](#custom-events)
- [Angepasste Events-Eigenschaften](#custom-event-properties)
- [Workspace](#workspace)
- [Kataloge](#catalogs)
- [Katalogfelder](#catalog-fields)
- [Optionen](#options)
- [Segmente](#segments)
- [String](#string)
- [Tags](#tags)

#### Zahl

- **Ersatzwert:** Der angegebene Wert, wie zum Beispiel `5.5`
- **Beispiel für die Verwendung:** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### Datumsbereich

![][4]{: style="max-width:50%;"}

Wenn Sie sowohl `start_date` als auch `end_date` verwenden, müssen sie denselben Namen haben, damit Sie sie als Datumsbereich verwenden können.

##### Beispielwerte

Mögliche Datumsbereichstypen sind relativ, Anfangsdatum, Abschlussdatum und Datumsbereich.

Alle vier Typen werden angezeigt, wenn sowohl `start_date` als auch `end_date` mit demselben Namen verwendet werden. Wenn Sie nur einen verwenden, werden nur die relevanten Typen angezeigt.

| Datumsbereichstyp | Beschreibung | Erforderliche Werte |
| --- | --- | --- |
| Relativ | Gibt die letzten X Tage an | Erfordert `start_date` |
| Startdatum | Gibt ein Anfangsdatum an | Erfordert `start_date` |
| Enddatum | Gibt ein Abschlussdatum an | Erfordert `end_date` |
| Datumsbereich | Gibt sowohl ein Start- als auch ein Enddatum an | Benötigt sowohl `start_date` als auch `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

- **Ersatzwert:** Ersetzt `start_date` und `end_date` durch einen Unix-Zeitstempel in Sekunden für ein bestimmtes Datum in UTC, z.B. `1696517353`.
- **Verwendungsbeispiel:** Für alle Variablen des Typs relativ, Anfangsdatum, Abschlussdatum und Datumsbereich:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - Sie können entweder `start_date` oder `end_date` verwenden, wenn Sie keinen Datumsbereich wünschen.

#### Messaging

Alle Messaging-Variablen müssen denselben Bezeichner enthalten, wenn Sie ihren Status in einer Gruppe zusammenfassen wollen.

![][5]{: style="max-width:50%;"}

##### Canvas

Zur Auswahl eines Canvas. Wenn Sie den gleichen Namen wie eine Kampagne verwenden, erscheint auf dem Tab **Variablen** ein Button, mit dem Sie entweder Canvas oder Kampagne auswählen können.

- **Ersatzwert:** Canvas BSON ID
- **Beispiel für die Verwendung:** {% raw %}`canvas_id = ‘{{canvas.${some name}}}’`{% endraw %}

##### Canvase

Zum Auswählen mehrerer Canvase. Wenn Sie den gleichen Namen wie eine Kampagne verwenden, erscheint auf dem Tab **Variablen** ein Button, mit dem Sie entweder Canvas oder Kampagne auswählen können.

- **Ersatzwert:** BSON-IDs von Canvasen
- **Beispiel für die Verwendung:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### Kampagne

Zum Auswählen einer Kampagne. Wenn Sie den gleichen Namen wie ein Canvas verwenden, erscheint auf dem Tab **Variablen** ein Button, mit dem Sie entweder ein Canvas oder eine Kampagne auswählen können.

- **Ersatzwert:** Kampagne BSON ID
- **Beispiel für die Verwendung:** {% raw %}`campaign_id = ‘{{campaign.${some name}}}’`{% endraw %}

##### Kampagnen

Für Kampagnen mit Mehrfachauswahl. Wenn Sie den gleichen Namen wie ein Canvas verwenden, erscheint auf dem Tab **Variablen** ein Button, mit dem Sie entweder ein Canvas oder eine Kampagne auswählen können.

- **Ersatzwert:** Kampagnen BSON IDs
- **Beispiel für die Verwendung:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### Kampagnenvarianten

Zum Auswählen von Kampagnenvarianten, die zu der ausgewählten Kampagne gehören. Sie muss in Verbindung mit einer Kampagne oder Kampagnen-Variablen verwendet werden.

- **Ersatzwert:** Kampagnenvarianten API IDs, durch Kommas getrennte Strings wie z.B. `api-id1, api-id2`.
- **Beispiel für die Verwendung:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### Canvas-Varianten

Zum Auswählen von Canvas-Varianten, die zu einem gewählten Canvas gehören. Sie muss mit einer Canvas- oder Canvase-Variablen verwendet werden.

- **Ersatzwert:** Canvas-Varianten API IDs, durch Kommas getrennte Strings wie in `api-id1, api-id2`.
- **Beispiel für die Verwendung:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### Canvas-Schritt

Zum Auswählen eines Canvas-Schrittes, der zu einem gewählten Canvas gehört. Sie muss mit einer Canvas-Variablen verwendet werden.

- **Ersatzwert:** Canvas-Schritt API ID
- **Beispiel für die Verwendung:** {% raw %}`canvas_step_api_id = ‘{{canvas_step.${some name}}}’`{% endraw %}

##### Canvas-Schritte

Zum Auswählen von Canvas-Schritten, die zu den gewählten Canvase gehören. Sie muss mit einer Canvas- oder Canvase-Variablen verwendet werden.

- **Ersatzwert:** Canvas-Schritte API IDs
- **Beispiel für die Verwendung:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}

#### Produkte

Zum Auswählen einer Liste von Produktnamen.

- **Ersatzwert:** Produktnamen sind von einfachen Anführungszeichen umgeben und durch Kommas getrennt, wie z.B. in `product1, product2`
- **Beispiel für die Verwendung:** {% raw %}`product_id IN ({{products.${product name (optional)}}})`{% endraw %}

#### Angepasste Events

Zum Auswählen einer Liste von angepassten Events.

- **Ersatzwert:** Die Namen der benutzerdefinierten Ereigniseigenschaften werden durch Kommas voneinander getrennt, wie bei `event1, event2`
- **Beispiel für die Verwendung:** {% raw %}`name = ‘{{custom_events.${event names)}}}’`{% endraw %}

#### Benutzerdefinierte Ereigniseigenschaften

Zum Auswählen einer Liste mit den Namen der angepassten Event-Eigenschaften. Sie muss mit der Variable für angepasste Events verwendet werden.

- **Ersatzwert:** Die Namen der benutzerdefinierten Ereigniseigenschaften werden durch Kommas voneinander getrennt, wie bei `property1, property2`
- **Beispiel für die Verwendung:** {% raw %}`name = ‘{{custom_event_properties.${property names)}}}’`{% endraw %}

#### Workspace

Zum Auswählen eines Workspace.

- **Ersatzwert:** BSON-ID des Workspace
- **Beispiel für die Verwendung:** {% raw %}`workspace_id = ‘{{workspace.${app_group_id}}}’`{% endraw %}

#### Kataloge

Zum Auswählen von Katalogen.

- **Ersatzwert:** Katalog BSON IDs
- **Beispiel für die Verwendung:** {% raw %}`catalog_id = ‘{{catalogs.${catalog}}}’`{% endraw %}

#### Katalog Felder

Zum Auswählen von Katalogfeldern. Sie muss zusammen mit der Variable catalogs verwendet werden.

- **Ersatzwert:** Namen der Katalogfelder
- **Beispiel für die Verwendung:** {% raw %}`field_name = '{{catalog_fields.${some name}}}’`{% endraw %}

#### Optionen {#options}

Zum Auswählen aus einer Liste von Optionen.

- **Ersatzwert:** Der Wert der ausgewählten Optionen
- **Verwendungsbeispiel:**
    - Zum Auswählen von Dropdowns: {% raw %}`{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}
        - Mit `is_multi_select` können Sie einstellen, ob mehr als eine Option ausgewählt werden kann.
    - Für Radiobutton: {% raw %}`{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}`{% endraw %}

#### Segmente

Zum Auswählen von Segmenten, für die [Analytics Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) aktiviert ist.

- **Ersatzwert:** Die Analytics ID des Segments, die den IDs entspricht, die in der Spalte `user_segment_membership_ids` in den Tabellen, in denen diese Spalte verfügbar ist, gespeichert sind.
- **Beispiel für die Verwendung:** {% raw %}`{{segments.${analytics_segments}}}`{% endraw %}

#### String

Zum Ändern von sich wiederholenden String-Werten zwischen den Berichtsläufen. Verwenden Sie diese Variable, damit Werte nicht mehrfach in Ihrem SQL codiert werden.

- **Ersatzwert:** Der String wie er ist, ohne umgebende Anführungszeichen
- **Beispiel für die Verwendung:** {% raw %}`{{string.${some name}}}`{% endraw %}

#### Tags

Zum Auswählen von Tags für Kampagnen und Canvase.

- **Ersatzwert:** Kampagnen und Canvase mit kommagetrennten BSON-IDs, die mit den ausgewählten Tags verknüpft sind
- **Beispiel für die Verwendung:** {% raw %}`{{tags.${some tags}}}`{% endraw %}

### Variable Metadaten

Metadaten können an eine Variable angehängt werden, um ihr Verhalten zu ändern, indem Sie die Metadaten mit einem senkrechten Strich ( | ) an den Variablennamen anhängen. Die Reihenfolge der Metadaten spielt keine Rolle und Sie können eine beliebige Anzahl von Metadaten anhängen. Außerdem können alle Arten von Metadaten für jede Variable verwendet werden, mit Ausnahme spezieller Metadaten, die für bestimmte Variablen spezifisch sind (dies wird in diesen Fällen angegeben). Die Verwendung aller Metadaten ist optional und dient dazu, das Verhalten der Variablen des Standards zu ändern.

**Beispiel für die Verwendung:** {% raw %}`{{string.${my var}| is_required: ‘false’ | description: ‘My optional string var’}}`{% endraw %}

#### Sichtbar

Dafür, ob Variablen sichtbar sind. Alle Variablen sind standardmäßig auf dem Tab **Variablen** sichtbar, wo Sie Werte eingeben können.

Es gibt einige spezielle Variablen, deren Wert von einer anderen Variable oder deren Wert abhängt. Diese speziellen Variablen sind als nicht sichtbar markiert, so dass sie auf dem Tab **Variablen** nicht angezeigt werden.

**Beispiel für die Verwendung:** `visible: ‘false’`

#### Erforderlich

Für die Frage, ob Variablen standardmäßig erforderlich sind. Ein leerer Wert für eine Variable führt normalerweise zu einem Abfragefehler.

**Beispiel für die Verwendung:** `required: ‘false’`

#### Bestellung

Zum Auswählen der Position der Variablen auf dem Tab **Variablen**.

**Beispiel für die Verwendung:** `order: ‘1’`

#### Mit einfachen Anführungszeichen

Umgeben Sie die Werte einer Variablen mit einfachen Anführungszeichen.

**Beispiel für die Verwendung:** `include_quotes: ‘true’`

#### Mit doppelten Anführungszeichen

Umgeben Sie die Werte einer Variablen mit doppelten Anführungszeichen.

**Beispiel für die Verwendung:** `include_double_quotes: ‘true’`

#### Mehrfachauswahl

Ob das Dropdown-Menü Einfach- oder Mehrfachauswahl zulässt. Im Moment können Sie diese Metadaten nur einfügen, wenn Sie die Variable [Optionen](#options) verwenden.

**Beispiel für die Verwendung:** `is_multi_select: ‘true’`

![][7]{: style="max-width:50%;"}

#### Radiobutton

Für die Anzeige von Optionen als Radio-Buttons anstelle eines ausgewählten Dropdowns auf dem Tab " **Variablen"**. Sie können diese Metadaten nur verwenden, wenn Sie die Variable [Optionen](#options) verwenden.

**Beispiel für die Verwendung:** `is_radio_button: ‘true’`

![][6]{: style="max-width:50%;"}

#### Optionen 

Zur Bereitstellung der Liste auswählbarer Optionen mit Label und Wert. Die Beschriftung ist das, was angezeigt wird. Der Wert ersetzt die Variable, wenn die Option ausgewählt ist. Sie können diese Metadaten nur verwenden, wenn Sie die Variable [Optionen](#options) verwenden.

**Beispiel für die Verwendung:** `options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'`

#### Platzhalter

Zum Festlegen des Platzhaltertextes, der im Eingabefeld der Variablen angezeigt wird.

**Beispiel für die Verwendung:** `placeholder: ‘enter some value’`

#### Beschreibung

Zum Festlegen des Beschreibungstextes, der unter dem Eingabefeld der Variablen angezeigt wird.

**Beispiel für die Verwendung:** `description: ‘some description’`

#### Standardwert

Zum Festlegen des Standardwerts für die Variable, wenn kein Wert angegeben ist.

**Beispiel für die Verwendung:** `default_value: ‘5’`

#### Etikett ausblenden

Zum Ausblenden der Beschriftung der Variablen. Der Name der Variablen wird als Standardbeschriftung verwendet.

**Beispiel für die Verwendung:** `hide_label: ‘true’`

### Besondere Variablen

Die folgenden Variablen können mit anderen Variablen verwendet werden:

#### Vorhandensein oder Nichtvorhandensein des Wertes einer anderen Variablen

Um zu wissen, ob der Wert einer Variablen gefüllt ist. Dies ist nützlich bei optionalen Variablen, bei denen Sie eine Bedingung kurzschließen möchten, wenn kein Variablenwert vorhanden ist.

- **Ersatzwert:** `true` oder `false` je nach dem Wert der anderen Variablen
- **Beispiel für die Verwendung:** {% raw %}`{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}`{% endraw %}

`type` und `name` referenzieren auf die referenzierte Variable. Um zum Beispiel die optionale Variable {% raw %}`{{campaigns.${messaging}}` kurzzuschließen, können Sie Folgendes verwenden:
`{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: ‘false’}})`{% endraw %}

## Zeitüberschreitung melden

Bei Berichten, deren Erstellung länger als sechs Minuten dauert, tritt ein Timeout ein. Wenn dies die erste Abfrage seit längerer Zeit ist, kann die Verarbeitung etwas länger dauern und die Wahrscheinlichkeit eines Timeouts ist daher höher. Versuchen Sie in diesem Fall, den Bericht erneut zu erstellen.

Wenn ein Bericht eine Zeitüberschreitung aufweist oder auch nach erneuten Versuchen auf Fehler stößt, wenden Sie sich an den [Support]({{site.baseurl}}/help/support#braze-support).

## Daten und Ergebnisse

Ergebnisse und Ergebnisexporte sind Tabellen mit bis zu 1.000 Zeilen. Für Berichte, die größere Datenmengen erfordern, können Sie Tools wie [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) oder den [Endpunkt der Export-API]({{site.baseurl}}/api/endpoints/export) verwenden.

## Überwachung Ihrer Query Builder-Nutzung

Jeder Braze-Workspace verfügt über fünf Snowflake-Credits pro Monat. Ein kleiner Teil eines Snowflake-Guthabens wird immer dann verwendet, wenn Sie eine Abfrage ausführen oder eine Vorschau einer Tabelle anzeigen.

{% alert note %}
Snowflake Credits werden nicht zwischen Features geteilt. So sind zum Beispiel Gutschriften über SQL-Segmenterweiterungen und Query Builder unabhängig voneinander.
{% endalert %}

Der Verbrauch hängt von der Laufzeit Ihrer SQL-Anfrage ab. Je länger die Laufzeit, desto mehr Guthaben wird aufgezehrt. Die Laufzeit kann sich je nach Komplexität und Umfang der Abfrage unterscheiden. Je komplexere und häufigere Abfragen Sie durchführen, desto mehr Ressourcen werden Ihnen zugewiesen und desto schneller die Laufzeit.

Credits werden beim Schreiben, Bearbeiten oder Speichern von Berichten im Braze SQL-Editor nicht verwendet. Ihr Guthaben wird am ersten eines jeden Monats um 12 Uhr UTC auf 5 zurückgesetzt. Sie können den Verbrauch Ihres monatlichen Guthabens oben im Abfrage-Builder-Seite kontrollieren.

![Der Abfrage-Builder zeigt das im laufenden Monat verbrauchte Guthaben an.][1]{: style="max-width:60%;"}

Wenn Sie Ihr Guthaben aufgebraucht haben, können Sie keine Abfragen mehr ausführen, aber weiterhin SQL-Berichte erstellen, bearbeiten und speichern. Wenn Sie weitere Kontingente für den Abfrage-Builder erwerben möchten, wenden Sie sich bitte an Ihren Account Manager.

[1]: {% image_buster /assets/img_archive/query_builder_credits.png %}
[2]: {% image_buster /assets/img_archive/query_builder_ai_tab.png %}
[3]: {% image_buster /assets/img_archive/sql_variables_panel.png %}
[4]: {% image_buster /assets/img_archive/query_builder_time_range.png %}
[5]: {% image_buster /assets/img_archive/sql_variables_canvases.png %}
[6]: {% image_buster /assets/img_archive/sql_variables_campaigns.png %}
[7]: {% image_buster /assets/img_archive/sql_variables_productname.png %}
