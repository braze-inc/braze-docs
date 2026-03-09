---
nav_title: Kontext 
article_title: Kontext 
alias: /context/
page_order: 6
page_type: reference
toc_headers: "h2"
description: "Dieser referenzierte Artikel beschreibt, wie Sie Kontext-Schritte in Ihrem Canvas erstellen und verwenden."
tool: Canvas

---

# Kontext

> Mit Kontext-Schritten können Sie eine oder mehrere Variablen für einen Nutzer:in erstellen und aktualisieren, während dieser sich durch ein Canvas bewegt. Wenn Sie zum Beispiel ein Canvas haben, das saisonale Rabatte verwaltet, können Sie eine Kontextvariable verwenden, um jedes Mal, wenn ein Nutzer:in das Canvas eintritt, einen anderen Rabattcode zu speichern.

## Funktionsweise

![Ein Context-Schritt als erster Schritt eines Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Mit Kontext-Schritten können Sie temporäre Daten erstellen und verwenden, während eine Nutzer:in eine bestimmte Canvas-Umgebung durchläuft. Diese Daten existieren nur innerhalb dieser Canvas-Reise und bleiben nicht über verschiedene Canvase oder außerhalb der Sitzung bestehen.

Kontextvariablen existieren nur für diese spezifische Canvas-Journey. Sie ändern das Nutzerprofil nicht dauerhaft und werden nicht in anderen Canvase-Ansichten angezeigt. Dadurch eignen sie sich ideal für temporäre Informationen, die nur für eine bestimmte Kampagne oder einen bestimmten Arbeitsablauf relevant sind.

{% alert tip %}
Eine vollständige Referenz zu Kontextvariablen, einschließlich Datentypen, Verwendung und bewährten Verfahren, finden Sie in der [Referenz zu Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).
{% endalert %}

Innerhalb eines Kontext-Schritts können Sie bis zu 10 Kontextvariablen definieren oder eine Update-Aktivität durchführen. Diese Variablen können verwendet werden, um Verzögerungen zu personalisieren, Nutzer:innen dynamisch zu segmentieren und das Messaging im gesamten Canvas zu optimieren. Beispielsweise könnten Sie eine Kontextvariable für die geplante Flugzeit einer Nutzer:in erstellen und diese dann verwenden, um personalisierte Verspätungen festzulegen und Erinnerungen zu versenden.

Sie können Kontextvariablen auf zwei Arten setzen:

- **Am Eingang von Canvas:** Daten aus dem Ereignis oder dem API-Trigger können automatisch Kontextvariablen füllen.
- **In einem Context-Schritt:** Definieren oder Updateen Sie Kontextvariablen manuell, indem Sie einen Kontext-Schritt hinzufügen.

Jede Kontextvariable erfordert einen Namen, einen Datentyp und einen Wert (festgelegt mit Liquid oder dem Tool „Personalisierung hinzufügen“). Nach der Definition können Sie Kontextvariablen im gesamten Canvas mithilfe von Liquid referenzieren, beispielsweise {% raw %}`{{context.${flight_time}}}`{% endraw %}.

Jeder Canvas-Eintrag definiert Kontextvariablen auf Grundlage der neuesten Daten und der Canvas-Einstellungen neu, sodass Nutzer:innen mehrere aktive Journeys mit ihrem eigenen Kontext haben können. Wenn eine Kund:in beispielsweise zwei bevorstehende Flüge hat, gibt es zwei separate Reisestatus, die gleichzeitig ablaufen – jeder mit seinen eigenen flugspezifischen Kontextvariablen wie Abflugzeit und Ziel:e. Auf diese Weise ist es zulässig, personalisierte Erinnerungen für den Flug um 14 Uhr nach New York zu versenden und gleichzeitig verschiedene Updates für den Flug um 8 Uhr nach Los Angeles morgen bereitzustellen, sodass jede Nachricht für die jeweilige Buchung relevant bleibt.

### Nutzer:innen-Verarbeitung und Stapelverarbeitung

Der Kontext verarbeitet Nutzer:innen in Stapeln, um die Performance zu optimieren. Wenn Nutzer:innen einen Kontext-Schritt eingeben, verarbeitet Braze diese standardmäßig in Gruppen von 1.000 Nutzer:innen. Diese Stapel werden parallel verarbeitet, jedoch werden die Nutzer:innen innerhalb jedes Stapels sequenziell verarbeitet.

Dies bedeutet:

**Beispiel**: Wenn 3.500 Nutzer:innen einen Kontext-Schritt mit Connected-Content ausführen, der pro Nutzer:in 650 ms dauert:
- Braze erstellt vier Gruppen von Nutzern (in diesem Beispiel 1.000, 1.000, 1.000 und 500 Nutzer:innen).
- Jeder Stapel verarbeitet die Nutzer:innen nacheinander, sodass ein Stapel von 1.000 Nutzer:innen etwa 10,8 Minuten (650 Sekunden; 1.000 × 650 ms) benötigt.
- Die Batches werden zu unterschiedlichen Zeitpunkten abgeschlossen, sodass die Nutzer:innen nach Abschluss ihres Batches zum nächsten Schritt übergehen.
- Die ersten Nutzer:innen können den nächsten Schritt einige Minuten vor den letzten Nutzer:innen erreichen, abhängig von der Batchgröße und den Antwortzeiten von Connected-Content.

Ohne Connected-Content werden Kontext-Schritte wesentlich schneller verarbeitet, da keine externen API-Aufrufe abgewartet werden müssen.

## Überlegungen

- Sie können bis zu 10 Kontextvariablen pro Kontextschritt definieren.
- Jede Variable benötigt einen eindeutigen Namen (nur Buchstaben, Zahlen und Unterstriche, maximal 100 Zeichen).
- Die Gesamtgröße aller Variablen in einem Schritt darf 50 KB nicht überschreiten.
- Variablen, die über API-Trigger übergeben werden, verwenden denselben Namespace wie die in Kontext-Schritten erstellten Variablen. Wenn eine Variable in einem Kontext-Schritt neu definiert wird, überschreibt dies den API-Wert.

Weitere Informationen und erweiterte Anwendungsmöglichkeiten finden Sie in [der Referenz zu Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

## Erstellen eines Kontextschritts

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Schritt 1: Einen Schritt hinzufügen

Fügen Sie Ihrem Canvas einen Schritt hinzu, und ziehen Sie die Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie die Plus-Schaltfläche <i class="fas fa-plus-circle"></i> und dann **Kontext**.

### Schritt 2: Definieren Sie die Variablen

{% alert note %}
Sie können bis zu 10 Kontextvariablen für jeden Context-Schritt definieren.
{% endalert %}

So definieren Sie eine Kontextvariable:

1. Geben Sie Ihrer Kontextvariablen einen **Namen**.
2. Wählen Sie einen [Datentyp]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types) aus.
3. Schreiben Sie einen Liquid-Ausdruck manuell oder verwenden Sie **Personalisierung hinzufügen**, um ein Liquid-Snippet aus bereits vorhandenen Attributen zu erstellen.
4. Wählen Sie **Vorschau**, um den Wert Ihrer Kontextvariablen zu überprüfen.
5. (Optional) Um weitere Variablen hinzuzufügen, wählen Sie **„Kontextvariable hinzufügen”** und wiederholen Sie die Schritte 1 bis 4.
6. Wenn Sie fertig sind, wählen Sie **Fertig**.

Jetzt können Sie Ihre Kontextvariable überall dort verwenden, wo Sie Liquid einsetzen, z.B. in den Schritten Nachrichten und Nutzer:innen Update, indem Sie **Personalisierung hinzufügen** auswählen. Eine vollständige Anleitung finden Sie unter [der Referenz zu Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

{% alert important %}
Bei der Referenzierung von Kontextvariablen ist stets das Format zu verwenden{% raw %}`{{context.${variable_name}}}`{% endraw %}.
{% endalert %}

### Kontextvariable Filter

Sie können Filter mithilfe von Kontextvariablen in den Schritten [„Zielgruppen-Pfade“]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) und [„Decision-Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split)-Schritte“ erstellen. Informationen zur Filtereinrichtung, Vergleichslogik und fortgeschrittenen Beispielen finden Sie unter [Referenz zu Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters).

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

## Vorschau der Benutzerpfade

Wir empfehlen Ihnen[, Ihre Benutzerpfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) zu testen und [in der Vorschau anzuzeigen,]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) um sicherzustellen, dass Ihre Nachrichten an die richtige Zielgruppe gesendet werden und die Kontextvariablen zu den erwarteten Ergebnissen führen.

{% alert note %}
Wenn Sie Ihre Canvas-Vorlage im Abschnitt **„Vorschau/Testversand“** des**&** Editors in der **Vorschau** anzeigen, **wird** der Zeitstempel in der Vorschau der Testnachricht **nicht** auf UTC standardisiert, da dieses Panel Vorschauen als Strings generiert. Dies bedeutet, dass, wenn ein Canvas so eingerichtet ist, dass es ein`time`Objekt akzeptiert, die Vorschau für Nachrichten nicht genau wiedergibt, was passiert, wenn das Canvas live ist. Um Ihre Canvas-Umgebung möglichst genau zu testen, empfehlen wir Ihnen, stattdessen eine Vorschau der Pfade der Nutzer:innen anzuzeigen.
{% endalert %}

Bitte beachten Sie alle gängigen Szenarien, die zu ungültigen Kontextvariablen führen können. Bei der Vorschau Ihres Benutzerpfads können Sie die Ergebnisse personalisierter Verzögerungsschritte mithilfe von Kontextvariablen sowie alle Zielgruppen- oder Entscheidungsschrittvergleiche anzeigen, die Nutzer:innen mit Kontextvariablen abgleichen.

Wenn die Kontextvariable gültig ist, können Sie die Variable in Ihrem gesamten Canvas referenzieren. Wenn die Kontextvariable jedoch nicht korrekt erstellt wurde, werden auch die nachfolgenden Canvas-Schritte nicht ordnungsgemäß ausgeführt. Wenn Sie beispielsweise einen Kontext-Schritt erstellen, um Nutzern einen Termin zuzuweisen, und den Wert des Termins auf ein Datum in der Vergangenheit festlegen, wird die Erinnerungs-E-Mail in Ihrem Nachrichten-Schritt nicht versendet.

## Connected-Content-Strings in JSON umwandeln

Bei der Ausführung eines [Connected-Content-Aufrufs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) in einem Kontext-Schritt wird das vom Aufruf zurückgegebene JSON aus Gründen der Konsistenz und Fehlervermeidung als String-Datentyp ausgewertet. Wenn Sie diesen String in JSON umwandeln möchten, konvertieren Sie ihn mit `as_json_string`. Zum Beispiel:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Fehlersuche

### Ungültige Kontextvariablen

Eine Kontextvariable wird als ungültig betrachtet, wenn:

- Ein Aufruf eines eingebetteten Connected-Content schlägt fehl.
- Der Liquid-Ausdruck gibt zur Laufzeit einen Wert zurück, der nicht mit dem Datentyp übereinstimmt oder leer ist (null).

Wenn zum Beispiel der Datentyp der Kontextvariablen **Number** ist, der Liquid-Ausdruck aber einen String zurückgibt, ist er ungültig.

Unter diesen Umständen:
- Der Nutzer:in bringt den nächsten Schritt voran.
- Die Canvas-Schritt-Analytics wertet dies als _„Nicht aktualisiert“_ aus.

Überwachen Sie bei der Fehlerbehebung die Metrik _Nicht aktualisiert_, um zu prüfen, ob Ihre Kontextvariable korrekt aktualisiert wird. Wenn die Kontextvariable ungültig ist, können Ihre Nutzer:innen nach dem Kontext-Schritt in Ihrem Canvas weitermachen, sich aber möglicherweise nicht für spätere Schritte qualifizieren.

Die Beispiele für die Konfiguration der einzelnen Datentypen referenzieren [Datentypen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types).

### Verzögerungen beim Senden mit Connected-Content

Alle Nutzer:innen in einem Stapel werden verarbeitet, bevor weitere Nutzer:innen voranbringen können. Nach Abschluss der Stapelverarbeitung werden erfolgreiche Nutzer:innen zum nächsten Schritt weitergeleitet, während fehlgeschlagene Nutzer:innen separat erneut versucht werden – erfolgreiche Nutzer:innen warten nicht auf erfolgreiche Wiederholungsversuche, bevor sie voranbringen.

**Wiederholungsverhalten**: Kontextschritte (und alle Canvas-Schritte) verwenden Canvas-spezifische Wiederholungsmechanismen und nicht das standardmäßige Wiederholungsverhalten von Connected-Content. Sollte ein Aufruf von Connected-Content fehlschlagen, wiederholt Braze den Schritt etwa 13 Mal mit exponentiellem Backoff. Sollten alle Wiederholungsversuche fehlschlagen, verlässt die Nutzer:in die Canvas.

{% alert note %}
Der in `:retry`Standard-Connected-Content-Tags verwendete Tag gilt nicht für Connected-Content-Aufrufe, die innerhalb von Canvas-Schritten erfolgen. Canvas-Schritte verfügen über eine eigene Wiederholungslogik, die für Canvas-Workflows optimiert ist.
{% endalert %}

**Bearbeitungszeit**: Die Zeit, die benötigt wird, um alle Nutzer:innen durch einen Kontext-Schritt zu verarbeiten, hängt von folgenden Faktoren ab:
- Die Anzahl der Nutzer:innen, die den Schritt betreten
- Ob Connected-Content verwendet wird (und dessen Reaktionszeit)
- Die Stapelgröße (Standardwert: 1.000 Nutzer:innen pro Stapel)

Wenn Ihr Connected-Content-Endpunkt Rate-Limits aufweist, beachten Sie bitte, dass Context-Schritte Nutzer:innen innerhalb jedes Batches sequenziell verarbeiten, was dazu beiträgt, Rate-Limits auf natürliche Weise einzuhalten. Bitte beachten Sie, dass mehrere Batches parallel verarbeitet werden. Stellen Sie daher sicher, dass Ihr Endpunkt gleichzeitige Anfragen von mehreren Batches verarbeiten kann.

## Standardisierung der Zeitzonenkonsistenz

Während die meisten Event-Eigenschaften, die den Zeitstempeltyp verwenden, in Canvas bereits in UTC vorliegen, gibt es einige Ausnahmen. Mit der Einführung von Canvas Context werden alle Standard-Zeitstempel-Event-Eigenschaften in aktionsbasierten Canvases in UTC angegeben. Diese Änderung ist Teil einer umfassenderen Maßnahme, um eine vorhersehbarere und konsistentere Erfahrung bei der Bearbeitung von Canvas-Schritten und -Nachrichten zu gewährleisten. Bitte beachten Sie, dass diese Änderung alle aktionsbasierten Canvases betrifft, unabhängig davon, ob der jeweilige Canvas einen Kontext-Schritt verwendet oder nicht.

{% alert important %}
Unter allen Umständen empfehlen wir dringend, [time_zoneLiquid-Filter]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) für Zeitstempel zu verwenden, die in der gewünschten Zeitzone dargestellt werden sollen. Bitte referenzieren Sie diese [häufig gestellte Frage](#faq-example) als Beispiel.
{% endalert %}

## Häufig gestellte Fragen

### Was hat sich geändert, seit Canvas Context allgemein verfügbar ist?

Da Canvas Context nun allgemein verfügbar ist, gelten die folgenden Details:

- Alle Zeitstempel mit einem [Datums-/Zeit-Typ]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) aus [den Event-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) in aktionsbasierten Canvases sind in [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) angegeben.
- Diese Änderung betrifft alle aktionsbasierten Canvases, unabhängig davon, ob das jeweilige Canvas einen Kontext-Schritt verwendet oder nicht.

#### Was ist der Grund für diese Änderung?

Diese Änderung ist Teil einer umfassenderen Maßnahme, um eine vorhersehbarere und konsistentere Erfahrung bei der Bearbeitung von Canvas-Schritten und -Nachrichten zu schaffen.

#### Sind API-gesteuerte oder geplante Canvases von dieser Änderung betroffen?

Nein.

#### Hat diese Änderung Auswirkungen auf die Eingangs-Eigenschaften der Canvas-Einträge?

Ja, dies hat Auswirkungen`canvas_entry_properties`, wenn das Element in einem `canvas_entry_property`aktionsbasierten Canvas verwendet wird und die Eigenschaft ist`time`. Unter allen Umständen empfehlen wir die Verwendung von`time_zone`Liquid-Filtern für Zeitstempel, die in der gewünschten Zeitzone dargestellt werden sollen.

Hier ist ein Beispiel, wie Sie dies umsetzen können:

| Liquid im Schritt „Nachricht“ | Ausgabe | Ist dies die korrekte Methode, um Zeitzonen in Liquid darzustellen? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | Kein:e |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | Kein:e
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | Ja |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Könnten Sie bitte ein praktisches Beispiel dafür geben, wie sich das neue Zeitstempelverhalten auf meine Nachrichten auswirken könnte? {#faq-example}

Angenommen, wir verfügen über ein aktionsbasiertes Canvas, das in einem Nachrichtenschritt den folgenden Inhalt aufweist:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Dies führt zu folgender Nachricht: 

```
Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!
```

Da mit Liquid keine Zeitzone angegeben wird, ist der Zeitstempel hier in UTC angegeben. 

Um eine Zeitzone eindeutig anzugeben, können wir `time_zone`Liquid-Filter wie folgt verwenden: 

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Dies führt zu folgender Nachricht: 

```
Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!
```

Da die Zeitzone „America/Los Angeles“ mit Liquid angegeben wird, ist der Zeitstempel hier in PST angegeben.

Die bevorzugte Zeitzone kann auch in den Event-Eigenschaften der Nutzlast übermittelt und in der Liquid-Logik verwendet werden:

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### Wie unterscheiden sich die Kontextvariablen von den Eigenschaften der Canvas-Eingänge?

Die Eingangs-Eigenschaften des Canvases sind als Canvas-Kontextvariablen enthalten. Das bedeutet, dass Sie die Eingangs-Eigenschaften von Canvas über die Braze API senden und in anderen Schritten referenzieren können, ähnlich wie bei der Verwendung einer Kontextvariablen mit dem Liquid-Snippet.

### Können sich Variablen in einem Singular Context Schritt gegenseitig referenzieren?

Ja Alle Variablen in einem Kontext-Schritt werden nacheinander ausgewertet, d. h. Sie könnten die folgenden Kontextvariablen einrichten:

| Kontextvariable | Wert | Beschreibung |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | Die Lieblingsküche eines Nutzers:in. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | Der verfügbare Rabattcode für einen Nutzer:innen. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.${promo_code}}} "on delivery from your favorite" {{context.${favorite_cuisine}}} restaurants!"`{% endraw %} | Eine personalisierte Nachricht, die die vorherigen Variablen kombiniert. In einem Messaging-Schritt könnten Sie das Liquid Snippet {% raw %}`{{context.${personalized_message}}}`{% endraw %} verwenden, um die Kontextvariable zu referenzieren und jedem Nutzer:in eine personalisierte Nachricht zu liefern. Sie können auch einen Kontext-Schritt verwenden, um den Wert [des Aktionscodes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) zu speichern und ihn in anderen Schritten innerhalb eines Canvas als Template zu verwenden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Dies gilt auch für mehrere Context-Schritte. Stellen Sie sich zum Beispiel diese Sequenz vor:

1. Ein anfänglicher Context-Schritt erstellt eine Variable namens `JobInfo` mit dem Wert `job_title`.
2. Der Schritt Nachricht referenziert {% raw %}`{{context.${JobInfo}}}`{% endraw %} und zeigt dem Nutzer:innen `job_title` an.
3. Später aktualisiert ein Context-Schritt die Kontextvariable und ändert den Wert von `JobInfo` in `job_description`.
4. Alle nachfolgenden Schritte, die darauf referenzieren, verwenden`JobInfo` nun den aktualisierten Wert`job_description`.

Kontextvariablen verwenden im gesamten Canvas ihren neuesten Wert, wobei sich jedes Update auf alle folgenden Schritte auswirkt, die auf diese Variable referenzieren.
