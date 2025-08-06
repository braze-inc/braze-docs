# SQL-Segment-Erweiterungen

> Sie können eine Segmenterweiterung mithilfe von Snowflake SQL-Abfragen von [Snowflake-Daten]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) erstellen. SQL kann Ihnen helfen, neue Segmentierungs-Anwendungsfälle zu erschließen, da es die Flexibilität bietet, die Beziehungen zwischen Daten auf eine Weise zu beschreiben, die mit anderen Segmentierungs-Features nicht möglich ist.
>
> Wie bei den Standard Segmenterweiterungen können Sie in Ihrer SQL-Segmenterweiterung Events aus den letzten zwei Jahren (730 Tage) abfragen.

## Voraussetzungen

Da es möglich ist, über dieses Feature auf PII-Daten zuzugreifen, müssen Sie über PII-Berechtigungen verfügen, um SQL-Segmentierungsabfragen durchzuführen.

## Erstellen einer Segment-Erweiterung

### Schritt 1: Wählen Sie einen Editor

Bei der Erstellung Ihrer SQL-Segmenterweiterung können Sie zwischen zwei Arten von SQL-Editoren wählen: dem SQL-Editor und dem inkrementellen SQL-Editor.

- **Vollständige Auffrischung:** Jedes Mal, wenn Ihr Segment aktualisiert wird, fragt Braze alle verfügbaren Daten ab, um Ihr Segment zu aktualisieren, was mehr Credits verbraucht als inkrementelle Aktualisierungen. Erweiterungen mit vollständiger Aktualisierung können die Mitgliedschaft automatisch täglich erneuern, können aber nicht mit inkrementeller Aktualisierung aktualisiert werden.
- **Inkrementelle Aktualisierung:** Bei der inkrementellen Aktualisierung werden nur die Daten der letzten zwei Tage berechnet, was kosteneffizienter ist und weniger Guthaben verbraucht. Wenn Sie ein SQL-Segment zur inkrementellen Aktualisierung erstellen, können Sie es so einstellen, dass die Mitgliedschaft automatisch täglich neu generiert wird. Damit können Sie Ihr Segment so einstellen, dass die Mitgliedschaft automatisch täglich aktualisiert wird, was die Kosten für eine tägliche Datenaktualisierung für SQL Segment-Erweiterungen reduziert.
- **KI SQL-Generator:** Mit dem KI SQL-Generator können Sie eine Eingabeaufforderung in einfacher Sprache schreiben und sie in eine SQL-Abfrage für Ihr Segment umwandeln. So können Sie schnell loslegen, ohne selbst SQL schreiben zu müssen.

{% alert tip %}
Sie können alle SQL Segmente, die in einem der beiden SQL-Editoren erstellt wurden, manuell vollständig aktualisieren.
{% endalert %}

{% tabs local %}
{% tab Vollständige Aktualisierung %}

So erstellen Sie eine vollständige Aktualisierung der SQL-Segmenterweiterung:

1. Gehen Sie zu **Zielgruppe** > **Segmenterweiterungen**.
2. Klicken Sie auf **Neue Erweiterung erstellen** und wählen Sie **Vollständige Aktualisierung**.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. Fügen Sie einen Namen für Ihre Segmenterweiterung hinzu und geben Sie Ihr SQL ein. Lesen Sie den Abschnitt [SQL schreiben](#writing-sql) für Anforderungen und Ressourcen.<br><br>
   ![SQL-Editor mit einem Beispiel für eine SQL-Segmenterweiterung.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. Speichern Sie Ihre Segmenterweiterung.

{% endtab %}
{% tab Inkrementelle Aktualisierung %}

Der SQL-Editor für die inkrementelle Aktualisierung ermöglicht dem Benutzer die Aggregation von Abfragen pro Datum für ein Ereignis innerhalb eines bestimmten Zeitrahmens. So erstellen Sie eine inkrementelle Aktualisierung der SQL Segment Extension:

1. Gehen Sie zu **Zielgruppe** > **Segmenterweiterungen**.
{% alert note %}

Wenn Sie die [ältere Navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/) verwenden, finden Sie diese Seite unter **Engagement** > **Segmente** > **Segmenterweiterungen**.
{% endalert %}

{:start="2"}
2\. Klicken Sie auf **Neue Erweiterung erstellen** und wählen Sie **Inkrementelle Aktualisierung**.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3\. Fügen Sie einen Namen für Ihre Segmenterweiterung hinzu und geben Sie Ihr SQL ein. Lesen Sie den Abschnitt [SQL schreiben](#writing-sql) für Anforderungen und Ressourcen.<br><br>
   ![SQL-Editor mit einem Beispiel für eine inkrementelle SQL-Segmenterweiterung.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4\. Falls gewünscht, wählen Sie **Erweiterung täglich regenerieren**.<br><br>
   ![Aktivieren Sie das Kontrollkästchen, um die Erweiterung täglich neu zu generieren.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   Wenn Sie diese Option auswählen, aktualisiert Braze die Segmentmitgliedschaft jeden Tag automatisch. Das bedeutet, dass Braze jeden Tag um Mitternacht in der Zeitzone Ihres Unternehmens (mit einer möglichen Verzögerung von einer Stunde) nach neuen Benutzern in Ihrem Segment sucht und diese automatisch zu Ihrem Segment hinzufügt. Wenn eine Segmenterweiterung 7 Tage lang nicht verwendet wurde, unterbricht Braze automatisch die tägliche Regeneration. Eine ungenutzte Segmenterweiterung ist eine, die nicht Teil einer Kampagne oder eines Canvas ist (die Kampagne oder das Canvas muss nicht aktiv sein, damit die Erweiterung als "genutzt" gilt).<br><br>
5\. Speichern Sie Ihre Segmenterweiterung.

{% endtab %}

{% tab AI SQL Generator %}

{% alert note %}
Der AI SQL-Generator ist derzeit als Beta-Funktion verfügbar. Wenden Sie sich an Ihren Customer-Success-Manager, wenn Sie an der Teilnahme an diesem Betatest interessiert sind.
{% endalert %}

Der KI-SQL-Generator nutzt [GPT](https://openai.com/gpt-4), powered by OpenAI, um SQL-Empfehlungen für Ihr SQL-Segment zu geben.

![AI SQL Generator mit der Abfrage "Benutzer, die im letzten Monat eine Benachrichtigung erhalten haben"]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

Um den KI SQL-Generator zu verwenden, gehen Sie wie folgt vor:

1. Klicken Sie auf **AI SQL Generator starten**, nachdem Sie ein [SQL-Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) mit einer vollständigen oder inkrementellen Aktualisierung erstellt haben.
2. Geben Sie Ihre Eingabeaufforderung ein und klicken Sie auf **Generieren**, um Ihre Eingabeaufforderung in SQL zu übersetzen.
3. Überprüfen Sie das generierte SQL, um sicherzustellen, dass es korrekt aussieht, und speichern Sie dann Ihr Segment.

#### Beispiel-Eingabeaufforderungen
- Benutzer, die im letzten Monat eine E-Mail erhalten haben
- Nutzer, die im letzten Jahr weniger als fünf Einkäufe getätigt haben

#### Tipps
- Machen Sie sich mit den verfügbaren [Snowflake Datentabellen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) vertraut. Wenn Sie nach Daten fragen, die in diesen Tabellen nicht vorhanden sind, kann es sein, dass ChatGPT eine gefälschte Tabelle erstellt.
- Machen Sie sich mit den [SQL-Schreibregeln]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql) für dieses Feature vertraut. Die Nichtbeachtung dieser Regeln führt zu einem Fehler. Zum Beispiel muss Ihr SQL Code die Spalte `user_id` auswählen. Beginnen Sie Ihre Eingabeaufforderung mit "Nutzer:innen".
- Mit dem KI SQL Generator können Sie bis zu 20 Prompts pro Minute senden.

\##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}
{% endtabs %}

{% alert note %}
SQL-Anfragen, die länger als 20 Minuten dauern, werden nicht mehr ausgeführt.
{% endalert %}

Wenn die Verarbeitung der Erweiterung abgeschlossen ist, können Sie mit Ihrer Segment-Erweiterung [ein Segment erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment) und dieses neue Segment mit Ihren Kampagnen und Canvase ansprechen.

### Schritt 2: Schreiben Sie Ihr SQL

Ihre SQL-Abfrage sollte in [Snowflake-Syntax](https://docs.snowflake.com/en/sql-reference.html) geschrieben sein. In der [Tabellenreferenz]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/) finden Sie eine vollständige Liste der Tabellen und Spalten, die abgefragt werden können.

{% alert important %}
Beachten Sie, dass die zur Abfrage verfügbaren Tabellen nur Event-Daten enthalten. Wenn Sie nach Benutzerattributen suchen möchten, sollten Sie Ihr SQL-Segment mit benutzerdefinierten Attributfiltern aus dem [klassischen Segmentierer]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) kombinieren.
{% endalert %} 

{% tabs %}
{% tab SQL-Editor %}

Ihr SQL muss zusätzlich die folgenden Regeln einhalten:

- Schreiben Sie eine einzelne SQL-Anweisung. Fügen Sie keine Semikolons ein.
- Ihr SQL muss nur eine Spalte auswählen: die Spalte `user_id`. Das bedeutet, dass Ihr SQL Folgendes enthalten muss:

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- Es ist nicht möglich, Nutzer:innen mit null Events abzufragen. Das bedeutet, dass jede Abfrage nach Nutzer:innen, die ein Event weniger als X-mal durchgeführt haben, diesen Workaround befolgen muss:
   1. Schreiben Sie eine Abfrage, um Nutzer:innen auszuwählen, die das Event MEHR als X-mal haben.
   2. Wenn Sie Ihre Segmenterweiterung in Ihrem Segment referenzieren, wählen Sie `doesn't include`, um das Ergebnis zu invertieren.

#### Zusätzliche Regeln

Außerdem muss Ihre Standard-SQL-Abfrage die folgenden Regeln einhalten:

- Sie können keine `DECLARE` Anweisungen verwenden.
{% endtab %}
{% tab Inkrementeller SQL-Editor %}

Alle inkrementellen Aktualisierungsabfragen bestehen aus zwei Teilen: einer Abfrage und Schemadetails.

1. Schreiben Sie im Editor eine Abfrage, die `user_id`s aus der gewünschten Tabelle auswählt.
2. Fügen Sie Schemadetails hinzu, indem Sie einen **Operator**, die **Anzahl der Zeitpunkte** und den **Zeitraum** aus den Feldern oberhalb des Editors auswählen. Die Abfrage prüft, ob die Summe der Aggregatspalte eine bestimmte Bedingung erfüllt, die in den Platzhaltern {% raw %}`{{operator}}` und `{{number of times}}`{% endraw %} angegeben ist. Dies funktioniert ähnlich wie der Arbeitsablauf zur Erstellung klassischer Segmenterweiterungen.<br><br>
   - **Operator:** Geben Sie an, ob das Event mehr als, weniger als oder gleich einer Anzahl von Vorkommen stattgefunden hat.<br>
   ![Operator-Feld mit ausgewähltem "Mehr als".]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **Anzahl von Malen:** Wie oft Sie das Ereignis in Bezug auf den Betreiber auswerten möchten.<br>
   ![Anzahl der Eingaben mit "5".]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **Der Zeitraum:** Anzahl der Tage von 1 bis 730, in denen Sie Instanzen des Events überprüfen möchten. Dieser Zeitraum bezieht sich auf vergangene Tage im Verhältnis zum aktuellen Tag. Das folgende Beispiel zeigt die Abfrage nach Nutzer:innen, die das Event in den letzten 365 Tagen mehr als 5 Mal durchgeführt haben.<br>
   ![Zeitspannenfeld mit "365" eingegeben.]({% image_buster /assets/img_archive/sql_segments_period.png %})

Im folgenden Beispiel würde das resultierende Segment Benutzer enthalten, die das Ereignis `favorited` mehr als 3 Mal in den letzten 30 Tagen nach einem bestimmten Datum durchgeführt haben.

![SQL-Editor mit einem Beispiel für eine inkrementelle SQL-Segmenterweiterung.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![SQL-Vorschau auf eine inkrementelle SQL-Segmenterweiterung.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

{% alert tip %}
Segmente für die inkrementelle Aktualisierung berücksichtigen späte Events, d. h. Events, die mehr als 2 Tage zurückliegen (z. B. SDK-Events, die zum Zeitpunkt ihrer Erfassung noch nicht gesendet wurden).
{% endalert %}

#### Zusätzliche Regeln

Außerdem muss Ihre Abfrage zur inkrementellen Aktualisierung die folgenden Regeln einhalten:

- Schreiben Sie eine einzelne SQL-Anweisung. Fügen Sie keine Semikolons ein.
- Ihr inkrementelles SQL-Segment könnte sich nur auf ein einziges Ereignis beziehen. Ihre Dropdowns für Datum und Anzahl beziehen sich auf das von Ihnen gewählte Ereignis.
- Ihr SQL muss die folgenden Spalten enthalten: `user_id`, `$start_date`, und eine Aggregationsfunktion (wie `COUNT`). Jedes SQL, das ohne diese drei Felder gespeichert wird, führt zu einem Fehler.
- Sie können keine `DECLARE` Anweisungen verwenden.
{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Sie ein SQL-Segment erstellen, das die Tabelle `CATALOGS_ITEMS_SHARED` verwendet, müssen Sie eine Katalog ID angeben. Zum Beispiel:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Schritt 3: Vorschau auf die Abfrage

Vor dem Speichern können Sie eine Vorschau Ihrer Abfrage durchführen. Die Vorschau von Abfragen ist automatisch auf 100 Zeilen begrenzt und wird nach 60 Sekunden abgebrochen. Die Anforderung der Spalte `user_id` gilt nicht, wenn Sie eine Vorschau ausführen.

Bei inkrementellen SQL-Segmenterweiterungen enthält die Vorschau nicht die zusätzlichen Kriterien Ihres Operators, die Anzahl der Zeitpunkte und die Felder für den Zeitraum.

## Verwalten Ihrer Segment-Erweiterungen

Auf der Seite **Segmenterweiterungen** sind Segmente, die mit SQL generiert wurden, mit <i class="fas fa-code" alt="SQL Segment Extension"></i> neben ihrem Namen gekennzeichnet.

Wählen Sie eine SQL-Segmenterweiterung aus, um zu sehen, wo die Erweiterung verwendet wird, die Erweiterung zu archivieren oder [die Segment-Mitgliedschaft manuell zu aktualisieren](#refreshing-segment-membership).

![Messaging Abschnitt des SQL-Editors verwenden, der zeigt, wo das SQL-Segment verwendet wird.]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

## Segmentmitgliedschaft aktualisieren

Um die Segmentzugehörigkeit einer mit SQL erstellten Segmenterweiterung zu aktualisieren, öffnen Sie die Segmenterweiterung und wählen Sie **Aktualisieren**.

{% alert tip %}
Wenn Sie ein Segment erstellt haben, bei dem Sie erwarten, dass die Benutzer es regelmäßig betreten und verlassen, aktualisieren Sie die verwendete Segmenterweiterung manuell, bevor Sie dieses Segment in einer Kampagne oder einem Canvas anvisieren.
{% endalert %}

### Festlegen der Aktualisierungseinstellungen

{% multi_lang_include segments.md section='Refresh settings' %}

## Snowflake Kredite

Jeder Braze Workspace verfügt über 5 Snowflake Credits pro Monat. Wenn Sie mehr Credits benötigen, wenden Sie sich an Ihren Kundenbetreuer. Credits werden immer dann verwendet, wenn Sie die Mitgliedschaft eines SQL Segments aktualisieren oder speichern und aktualisieren. Credits werden nicht verwendet, wenn Sie Vorschauen innerhalb eines SQL Segments ausführen oder eine klassische Segmenterweiterung speichern oder aktualisieren.

{% alert note %}
Snowflake Credits werden nicht zwischen Features geteilt. So sind zum Beispiel Gutschriften über SQL-Segmenterweiterungen und Query Builder unabhängig voneinander.
{% endalert %}

Der Kreditverbrauch hängt von der Laufzeit Ihrer SQL-Anfrage ab. Je länger die Laufzeit ist, desto mehr Credits kostet eine Abfrage. Die Laufzeit kann je nach Komplexität und Umfang Ihrer Abfragen im Laufe der Zeit variieren. Je komplexer und häufiger Sie Abfragen durchführen, desto größer ist Ihre Ressourcenzuweisung und desto schneller wird Ihre Laufzeit.

Um Credits zu sparen, sollten Sie eine Vorschau Ihrer Abfrage anzeigen, um sicherzustellen, dass sie korrekt ist, bevor Sie die SQL-Segmenterweiterung speichern.

Ihr Guthaben wird am ersten eines jeden Monats um 12 Uhr UTC auf 5 zurückgesetzt. Sie können die Nutzung Ihres Guthabens im Laufe des Monats im Panel für die Kreditnutzung überwachen. Klicken Sie auf der Seite **Segment Extensions** auf <i class="fa-solid fa-chart-column"></i> **View SQL Credit Usage**.

![SQL Credit Usage Panel auf der Seite SQL Segment-Erweiterungen]({% image_buster /assets/img_archive/sql_segments_credits.png %}){: style="max-width:60%"}

Wenn Ihr Guthaben Null erreicht, geschieht Folgendes:

- Alle SQL-Segmenterweiterungen, die so eingerichtet sind, dass sie automatisch aktualisiert werden, werden nicht mehr aktualisiert, was sich auf die Mitgliedschaft in diesen Segmenten und auf alle Kampagnen oder Canvases auswirkt, die auf diese Segmente abzielen.
- Sie können neue SQL-Segmenterweiterungen nur noch für den Rest des Monats als Entwurf speichern.

Alle Unternehmensnutzer, die ein SQL-Segment erstellt haben, und Ihre Unternehmensadministratoren erhalten eine Benachrichtigung per E-Mail, wenn Sie 50 %, 80 % und 100 % Ihres Guthabens aufgebraucht haben. Nachdem Ihr Guthaben zu Beginn des nächsten Monats zurückgesetzt wurde, können Sie weitere SQL Segmente erstellen, und die automatischen Aktualisierungen werden wieder aufgenommen.

Wenn Sie mehr SQL-Segment-Guthaben oder zusätzliche Segmenterweiterungen erwerben möchten, wenden Sie sich bitte an Ihren Account Manager.
