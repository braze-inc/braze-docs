> Lernen Sie, wie Sie den Query Builder verwenden, damit Sie Berichte mit Braze-Daten in Snowflake erstellen können. Der Query Builder wird mit vorgefertigten [SQL-Anfragen-Templates]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) geliefert, die Ihnen den Einstieg erleichtern. Sie können aber auch Ihre eigenen angepassten SQL-Anfragen schreiben, um noch mehr Insights zu erhalten.

## Voraussetzungen

Sie benötigen die [Berechtigung "PII anzeigen"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/), um den Query Builder zu verwenden, da er direkten Zugriff auf einige Kundendaten erlaubt.

## Verwenden des Abfragegenerators

### Schritt 1: Erstellen Sie eine SQL-Abfrage

Um eine neue Abfrage zu erstellen, gehen Sie zu **Analytics** > **Query Builder** und wählen Sie dann **SQL-Abfrage erstellen**.

![Die Optionen "Abfrage-Template" und "SQL-Editor", die sich im Dropdown-Menü "SQL-Abfrage erstellen" befinden.]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

Wenn Sie Inspiration oder Hilfe bei der Gestaltung Ihrer Anfrage benötigen, wählen Sie **Abfragevorlage** und wählen Sie eine [vorgefertigte Vorlage]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) aus. Um mit einer leeren Abfrage zu beginnen, wählen Sie **SQL Editor**.

Ihr Bericht erhält automatisch einen Namen mit dem aktuellen Datum und der Uhrzeit. Bewegen Sie den Mauszeiger über den Namen und wählen Sie <i class="fas fa-pencil" alt="Edit"></i>, um Ihrer SQL-Abfrage einen aussagekräftigen Namen zu geben.

![Ein Beispielbericht mit dem Namen "Kanal Engagement für Mai 2025".]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### Schritt 2: Erstellen Sie Ihre Abfrage

Bei der Erstellung Ihrer Abfrage können Sie sich von der KI helfen lassen oder sie selbst erstellen.

{% tabs local %}
{% tab BrazeAI verwenden %}
Der Abfrage-Builder mit KI nutzt [GPT](https://openai.com/gpt-4) von OpenAI, um SQL für Ihre Abfrage zu empfehlen. So erzeugen Sie SQL per KI im Abfrage-Builder:

1. Wenn Sie einen Bericht im Abfrage-Builder erstellt haben, wählen Sie den Tab **Abfrage-Builder mit KI**.
2. Geben Sie Ihren Prompt ein oder wählen Sie einen Beispielprompt aus und wählen Sie **Generieren**, um Ihren Prompt in SQL zu übersetzen.
3. Überprüfen Sie das generierte SQL auf Richtigkeit und wählen Sie dann **In Editor einfügen**.

![Der SQL KI Query Builder.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### Tipps

- Machen Sie sich mit den verfügbaren [Snowflake Datentabellen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) vertraut. Wenn Sie nach Daten fragen, die in diesen Tabellen nicht vorhanden sind, kann es sein, dass ChatGPT eine gefälschte Tabelle erstellt.
- Machen Sie sich mit den [SQL-Schreibregeln]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/#custom-sql) für dieses Feature vertraut. Die Nichtbeachtung dieser Regeln führt zu einem Fehler.
- Sie können bis zu 20 Prompts pro Minute senden.

\##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab Auf eigene Faust %}
Schreiben Sie Ihre SQL-Abfrage mit der [Snowflake-Syntax](https://docs.snowflake.com/en/sql-reference). In der [Tabellenreferenz]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) finden Sie eine vollständige Liste der Tabellen und Spalten, die abgefragt werden können.

Um Tabellendetails im Query Builder anzuzeigen:

1. Öffnen Sie auf der Seite **Query Builder** das Panel **Referenz** und wählen Sie **Verfügbare Datentabellen**, um die verfügbaren Datentabellen und ihre Namen anzuzeigen.
3. Wählen Sie <i class="fas fa-chevron-down" alt=""></i> **Details ansehen**, um die Tabellenbeschreibung und Informationen über die Tabellenspalten, wie z.B. Datentypen, anzuzeigen.
4. Um den Tabellennamen in Ihr SQL einzufügen, wählen Sie <i class="fas fa-copy" title="Tabellenname in SQL-Editor kopieren"></i>.

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

#### Fehlerbehebung

Ihre Abfrage kann aus einem der folgenden Gründe fehlschlagen:

- Syntaxfehler in Ihrer SQL-Abfrage
- Zeitüberschreitung (nach 6 Minuten)
    - Bei Berichten, deren Erstellung länger als 6 Minuten dauert, tritt ein Timeout ein.
    - Versuchen Sie in diesem Fall, den Zeitraum Ihrer Datenabfrage zu verkürzen oder einen begrenzteren Datensatz abzufragen.
{% endtab %}
{% endtabs %}

### Schritt 3: Erzeugen Sie Ihren Bericht

Wenn Sie mit der Erstellung Ihrer Abfrage fertig sind, wählen Sie **Abfrage ausführen**. Wenn keine Fehler oder [Zeitüberschreitungen](#report-timeouts) auftreten, wird aus der Abfrage eine CSV-Datei erstellt.

Um den CSV-Bericht herunterzuladen, wählen Sie **Exportieren**.

![Der Abfrage-Builder zeigt die Ergebnisse zur Template-Abfrage "Engagement und Umsatz auf diesem Kanal in den letzten 30 Tagen".]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
Jeder Bericht kann nur einmal pro Tag Ergebnisse liefern. Wenn Sie denselben Bericht mehrmals an einem Kalendertag ausführen, sehen Sie in jedem Bericht dieselben Ergebnisse.
{% endalert %}

## Zeitüberschreitungen melden

Bei Berichten, deren Erstellung länger als sechs Minuten dauert, tritt ein Timeout ein. Wenn dies die erste Abfrage seit längerer Zeit ist, kann die Verarbeitung etwas länger dauern und die Wahrscheinlichkeit eines Timeouts ist daher höher. Versuchen Sie in diesem Fall, den Bericht erneut zu erstellen.

Wenn Ihr Bericht auch nach mehreren Versuchen nicht funktioniert, [wenden Sie sich an den Support]({{site.baseurl}}/help/support#braze-support).

## Daten und Ergebnisse

Alle Abfragen beziehen sich auf die Daten der letzten 60 Tage. Wenn Sie Ihre Ergebnisse exportieren, werden sie nur bis zu 1.000 Zeilen enthalten. Für Berichte, die größere Datenmengen erfordern, können Sie Tools wie [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) oder den [Endpunkt der Export-API]({{site.baseurl}}/api/endpoints/export) verwenden.

## Snowflake Kredite

Jedem Unternehmen stehen 5 Snowflake Credits pro Monat zur Verfügung, die auf alle Workspaces aufgeteilt werden. Ein kleiner Teil eines Snowflake-Guthabens wird immer dann verwendet, wenn Sie eine Abfrage ausführen oder eine Vorschau einer Tabelle anzeigen.

{% alert note %}
Snowflake Credits werden nicht zwischen Features geteilt. So sind zum Beispiel Gutschriften über SQL-Segmenterweiterungen und Query Builder unabhängig voneinander.
{% endalert %}

Der Verbrauch hängt von der Laufzeit Ihrer SQL-Anfrage ab. Je länger die Laufzeit, desto mehr Guthaben wird aufgezehrt. Die Laufzeit kann sich je nach Komplexität und Umfang der Abfrage unterscheiden. Je komplexere und häufigere Abfragen Sie durchführen, desto mehr Ressourcen werden Ihnen zugewiesen und desto schneller die Laufzeit.

Credits werden beim Schreiben, Bearbeiten oder Speichern von Berichten im Braze SQL-Editor nicht verwendet. Ihr Guthaben wird am ersten eines jeden Monats um 12 Uhr UTC auf 5 zurückgesetzt. Sie können den Verbrauch Ihres monatlichen Guthabens oben im Abfrage-Builder-Seite kontrollieren.

![Query Builder zeigt die Höhe der im aktuellen Monat verbrauchten Guthaben an.]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

Wenn Sie Ihr Guthaben aufgebraucht haben, können Sie keine Abfragen mehr ausführen, aber weiterhin SQL-Berichte erstellen, bearbeiten und speichern. Wenn Sie weitere Kontingente für den Abfrage-Builder erwerben möchten, wenden Sie sich bitte an Ihren Account Manager.
