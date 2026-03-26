---
nav_title: Kontext 
article_title: Kontext 
alias: /context/
page_order: 6
page_type: reference
toc_headers: "h2"
description: "Dieser Referenzartikel beschreibt, wie Sie Kontext-Schritte in Ihrem Canvas erstellen und verwenden."
tool: Canvas

---

# Kontext

> Mit Kontext-Schritten können Sie eine oder mehrere Variablen für Nutzer:innen erstellen und aktualisieren, während diese sich durch ein Canvas bewegen. Wenn Sie zum Beispiel ein Canvas haben, das saisonale Rabatte verwaltet, können Sie eine Kontextvariable verwenden, um jedes Mal einen anderen Rabattcode zu speichern, wenn Nutzer:innen das Canvas betreten.

## Funktionsweise

![Ein Kontext-Schritt als erster Schritt eines Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Mit Kontext-Schritten können Sie temporäre Daten erstellen und verwenden, während Nutzer:innen eine bestimmte Canvas-Journey durchlaufen. Diese Daten existieren nur innerhalb dieser Canvas-Journey und bleiben nicht über verschiedene Canvase hinweg oder außerhalb der Sitzung bestehen.

Kontextvariablen existieren nur für diese spezifische Canvas-Journey. Sie ändern das Profil der Nutzer:innen nicht dauerhaft und werden nicht in anderen Canvasen angezeigt. Dadurch eignen sie sich ideal für temporäre Informationen, die nur für eine bestimmte Kampagne oder einen bestimmten Workflow relevant sind.

{% alert tip %}
Eine vollständige Referenz zu Kontextvariablen, einschließlich Datentypen, Verwendung und Best Practices, finden Sie in der [Referenz zu Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).
{% endalert %}

Innerhalb eines Kontext-Schritts können Sie bis zu 10 Kontextvariablen definieren oder aktualisieren. Diese Variablen können verwendet werden, um Verzögerungen zu personalisieren, Nutzer:innen dynamisch zu segmentieren und das Messaging im gesamten Canvas zu bereichern. Beispielsweise könnten Sie eine Kontextvariable für die geplante Flugzeit von Nutzer:innen erstellen und diese dann verwenden, um personalisierte Verzögerungen festzulegen und Erinnerungen zu versenden.

Sie können Kontextvariablen auf zwei Arten setzen:

- **Beim Canvas-Eintritt:** Daten aus dem Ereignis oder dem API-Trigger können automatisch Kontextvariablen befüllen.
- **In einem Kontext-Schritt:** Definieren oder aktualisieren Sie Kontextvariablen manuell, indem Sie einen Kontext-Schritt hinzufügen.

Jede Kontextvariable erfordert einen Namen, einen Datentyp und einen Wert (festgelegt mit Liquid oder dem Tool „Personalisierung hinzufügen"). Nach der Definition können Sie Kontextvariablen im gesamten Canvas mithilfe von Liquid referenzieren, beispielsweise {% raw %}`{{context.${flight_time}}}`{% endraw %}. Im Feld **Name der Kontextvariablen** können Sie auch den Namen der Kontextvariablen eingeben oder ihn aus dem Dropdown im Schritt-Editor auswählen. Weitere Details finden Sie in der [Referenz zu Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

Jeder Canvas-Eintritt definiert Kontextvariablen auf Grundlage der neuesten Eintrittsdaten und der Canvas-Einstellungen neu, sodass Nutzer:innen mehrere aktive Journeys mit eigenem Kontext haben können. Wenn Kund:innen beispielsweise zwei bevorstehende Flüge haben, gibt es zwei separate Journey-Zustände, die gleichzeitig ablaufen – jeder mit seinen eigenen flugspezifischen Kontextvariablen wie Abflugzeit und Ziel. Auf diese Weise können Sie personalisierte Erinnerungen für den Flug um 14 Uhr nach New York versenden und gleichzeitig andere Updates für den Flug um 8 Uhr nach Los Angeles am nächsten Tag bereitstellen, sodass jede Nachricht für die jeweilige Buchung relevant bleibt.

### Verarbeitung und Stapelverarbeitung von Nutzer:innen

Kontext-Schritte verarbeiten Nutzer:innen in Stapeln, um die Performance zu optimieren. Wenn Nutzer:innen einen Kontext-Schritt betreten, verarbeitet Braze diese standardmäßig in Gruppen von 1.000 Nutzer:innen. Diese Stapel werden parallel verarbeitet, jedoch werden die Nutzer:innen innerhalb jedes Stapels sequenziell verarbeitet.

Dies bedeutet:

**Beispiel**: Wenn 3.500 Nutzer:innen einen Kontext-Schritt mit Connected-Content betreten, der pro Nutzer:in 650 ms dauert:
- Braze erstellt 4 Gruppen von Nutzer:innen (in diesem Beispiel 1.000, 1.000, 1.000 und 500 Nutzer:innen).
- Jeder Stapel verarbeitet die Nutzer:innen nacheinander, sodass ein Stapel von 1.000 Nutzer:innen etwa 10,8 Minuten (650 Sekunden; 1.000 × 650 ms) benötigt.
- Die Stapel werden zu unterschiedlichen Zeitpunkten abgeschlossen, sodass die Nutzer:innen nach Abschluss ihres Stapels zum nächsten Schritt übergehen.
- Die ersten Nutzer:innen können den nächsten Schritt einige Minuten vor den letzten Nutzer:innen erreichen, abhängig von der Stapelgröße und den Antwortzeiten von Connected-Content.

Ohne Connected-Content werden Kontext-Schritte wesentlich schneller verarbeitet, da keine externen API-Aufrufe abgewartet werden müssen.

## Überlegungen

- Sie können bis zu 10 Kontextvariablen pro Kontext-Schritt definieren.
- Jede Variable benötigt einen eindeutigen Namen (nur Buchstaben, Zahlen und Unterstriche, maximal 100 Zeichen).
- Die Gesamtgröße aller Variablen in einem Schritt darf 50 KB nicht überschreiten.
- Variablen, die über API-Trigger übergeben werden, verwenden denselben Namespace wie die in Kontext-Schritten erstellten Variablen. Wenn eine Variable in einem Kontext-Schritt neu definiert wird, überschreibt dies den API-Wert.

Weitere Informationen und erweiterte Anwendungsmöglichkeiten finden Sie in der [Referenz zu Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

## Erstellen eines Kontext-Schritts

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### 1. Schritt: Einen Schritt hinzufügen

Fügen Sie Ihrem Canvas einen Schritt hinzu, und ziehen Sie die Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie die Plus-Schaltfläche <i class="fas fa-plus-circle"></i> und dann **Kontext**.

### 2. Schritt: Variablen definieren

{% alert note %}
Sie können bis zu 10 Kontextvariablen für jeden Kontext-Schritt definieren.
{% endalert %}

So definieren Sie eine Kontextvariable:

1. Geben Sie Ihrer Kontextvariablen einen **Namen**.
2. Wählen Sie einen [Datentyp]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types) aus.
3. Schreiben Sie einen Liquid-Ausdruck manuell oder verwenden Sie **Personalisierung hinzufügen**, um ein Liquid-Snippet aus bereits vorhandenen Attributen zu erstellen.
4. Wählen Sie **Vorschau**, um den Wert Ihrer Kontextvariablen zu überprüfen.
5. (Optional) Um weitere Variablen hinzuzufügen, wählen Sie **Kontextvariable hinzufügen** und wiederholen Sie die Schritte 1–4.
6. Wenn Sie fertig sind, wählen Sie **Fertig**.

Jetzt können Sie Ihre Kontextvariable überall dort verwenden, wo Sie Liquid einsetzen, z. B. in den Schritten „Nachricht" und „Nutzer:innen-Update", indem Sie **Personalisierung hinzufügen** auswählen. Im Feld **Name der Kontextvariablen** können Sie auch den Namen der Kontextvariablen eingeben oder ihn aus dem Dropdown im Schritt-Editor auswählen. Eine vollständige Anleitung finden Sie in der [Referenz zu Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

{% alert important %}
Verwenden Sie beim Referenzieren von Kontextvariablen immer das Format {% raw %}`{{context.${variable_name}}}`{% endraw %}.
{% endalert %}

### Filter für Kontextvariablen

Sie können Filter mithilfe von Kontextvariablen in den Schritten [Zielgruppenpfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) und [Decision-Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) erstellen. Informationen zur Filtereinrichtung, Vergleichslogik und fortgeschrittenen Beispielen finden Sie in der [Referenz zu Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters).

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

## Vorschau der Nutzerpfade

Wir empfehlen, Ihre [Nutzerpfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) zu testen und in der Vorschau anzuzeigen, um sicherzustellen, dass Ihre Nachrichten an die richtige Zielgruppe gesendet werden und die Kontextvariablen zu den erwarteten Ergebnissen führen.

{% alert note %}
Wenn Sie Ihr Canvas im Abschnitt **Vorschau & Testversand** des Editors in der Vorschau anzeigen, wird der Zeitstempel in der Testnachrichtenvorschau **nicht** auf UTC standardisiert, da dieses Panel Vorschauen als Strings generiert. Das bedeutet: Wenn ein Canvas so eingerichtet ist, dass es ein `time`-Objekt akzeptiert, gibt die Nachrichtenvorschau nicht genau wieder, was passiert, wenn das Canvas live ist. Um Ihr Canvas möglichst genau zu testen, empfehlen wir Ihnen, stattdessen eine Vorschau der Nutzerpfade anzuzeigen.
{% endalert %}

Achten Sie auf alle gängigen Szenarien, die zu ungültigen Kontextvariablen führen können. Bei der Vorschau Ihres Nutzerpfads können Sie die Ergebnisse personalisierter Verzögerungsschritte mithilfe von Kontextvariablen sowie alle Zielgruppen- oder Entscheidungsschrittvergleiche anzeigen, die Nutzer:innen mit Kontextvariablen abgleichen.

Wenn die Kontextvariable gültig ist, können Sie die Variable in Ihrem gesamten Canvas referenzieren. Wenn die Kontextvariable jedoch nicht korrekt erstellt wurde, werden auch die nachfolgenden Canvas-Schritte nicht ordnungsgemäß ausgeführt. Wenn Sie beispielsweise einen Kontext-Schritt erstellen, um Nutzer:innen einen Termin zuzuweisen, und den Wert des Termins auf ein Datum in der Vergangenheit festlegen, wird die Erinnerungs-E-Mail in Ihrem Nachrichten-Schritt nicht versendet.

## Connected-Content-Strings in JSON umwandeln

Bei einem [Connected-Content-Aufruf]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) in einem Kontext-Schritt wird das vom Aufruf zurückgegebene JSON aus Gründen der Konsistenz und Fehlervermeidung als String-Datentyp ausgewertet. Wenn Sie diesen String in JSON umwandeln möchten, verwenden Sie `as_json_string`. Zum Beispiel:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Fehlerbehebung

### Ungültige Kontextvariablen

Eine Kontextvariable wird als ungültig betrachtet, wenn:

- Ein Aufruf eines eingebetteten Connected-Content fehlschlägt.
- Der Liquid-Ausdruck zur Laufzeit einen Wert zurückgibt, der nicht mit dem Datentyp übereinstimmt oder leer ist (null).

Wenn zum Beispiel der Datentyp der Kontextvariablen **Number** ist, der Liquid-Ausdruck aber einen String zurückgibt, ist die Variable ungültig.

Unter diesen Umständen:
- Werden die Nutzer:innen zum nächsten Schritt weitergeleitet.
- Zählt die Canvas-Schritt-Analytics dies als _Nicht aktualisiert_.

Überwachen Sie bei der Fehlerbehebung die Metrik _Nicht aktualisiert_, um zu prüfen, ob Ihre Kontextvariable korrekt aktualisiert wird. Wenn die Kontextvariable ungültig ist, können Ihre Nutzer:innen nach dem Kontext-Schritt in Ihrem Canvas weitermachen, sich aber möglicherweise nicht für spätere Schritte qualifizieren.

Die Beispiele für die Konfiguration der einzelnen Datentypen finden Sie unter [Datentypen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types).

### Verzögerungen beim Senden mit Connected-Content

Alle Nutzer:innen in einem Stapel werden verarbeitet, bevor Nutzer:innen weitergeführt werden. Nach Abschluss der Stapelverarbeitung werden erfolgreiche Nutzer:innen zum nächsten Schritt weitergeleitet, während fehlgeschlagene Nutzer:innen separat erneut verarbeitet werden – erfolgreiche Nutzer:innen warten nicht auf erfolgreiche Wiederholungsversuche, bevor sie weitergeführt werden.

**Wiederholungsverhalten**: Kontext-Schritte (und alle Canvas-Schritte) verwenden Canvas-spezifische Wiederholungsmechanismen und nicht das standardmäßige Wiederholungsverhalten von Connected-Content. Sollte ein Connected-Content-Aufruf fehlschlagen, wiederholt Braze den Schritt etwa 13 Mal mit exponentiellem Backoff. Sollten alle Wiederholungsversuche fehlschlagen, verlassen die Nutzer:innen das Canvas.

{% alert note %}
Der `:retry`-Tag, der in Standard-Connected-Content verwendet wird, gilt nicht für Connected-Content-Aufrufe innerhalb von Canvas-Schritten. Canvas-Schritte verfügen über eine eigene Wiederholungslogik, die für Canvas-Workflows optimiert ist.
{% endalert %}

**Bearbeitungszeit**: Die Zeit, die benötigt wird, um alle Nutzer:innen durch einen Kontext-Schritt zu verarbeiten, hängt von folgenden Faktoren ab:
- Die Anzahl der Nutzer:innen, die den Schritt betreten
- Ob Connected-Content verwendet wird (und dessen Antwortzeit)
- Die Stapelgröße (Standardwert: 1.000 Nutzer:innen pro Stapel)

Wenn Ihr Connected-Content-Endpunkt Rate-Limits aufweist, beachten Sie, dass Kontext-Schritte Nutzer:innen innerhalb jedes Stapels sequenziell verarbeiten, was dazu beiträgt, Rate-Limits auf natürliche Weise einzuhalten. Da jedoch mehrere Stapel parallel verarbeitet werden, stellen Sie sicher, dass Ihr Endpunkt gleichzeitige Anfragen von mehreren Stapeln verarbeiten kann.

## Standardisierung der Zeitzonenkonsistenz

Mit der allgemeinen Verfügbarkeit von Canvas Context sind alle Standard-Zeitstempel-Event-Eigenschaften in aktionsbasierten Canvasen in UTC angegeben. Diese Änderung ist Teil einer umfassenderen Maßnahme, um eine vorhersehbarere und konsistentere Erfahrung bei der Bearbeitung von Canvas-Schritten und -Nachrichten zu gewährleisten. Bitte beachten Sie, dass diese Änderung alle aktionsbasierten Canvase betrifft, unabhängig davon, ob das jeweilige Canvas einen Kontext-Schritt verwendet oder nicht.

{% alert important %}
Unter allen Umständen empfehlen wir dringend, [Liquid-`time_zone`-Filter]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) für Zeitstempel zu verwenden, die in der gewünschten Zeitzone dargestellt werden sollen. Ein Beispiel finden Sie in dieser [häufig gestellten Frage](#faq-example).
{% endalert %}

## Häufig gestellte Fragen

### Was hat sich geändert, seit Canvas Context allgemein verfügbar ist?

Da Canvas Context nun allgemein verfügbar ist, gelten die folgenden Details:

- Alle Zeitstempel mit einem [Datums-/Zeittyp]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) aus [Trigger-Event-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) in aktionsbasierten Canvasen sind in [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) angegeben.
- Diese Änderung betrifft alle aktionsbasierten Canvase, unabhängig davon, ob das jeweilige Canvas einen Kontext-Schritt verwendet oder nicht.

#### Was ist der Grund für diese Änderung?

Diese Änderung ist Teil einer umfassenderen Maßnahme, um eine vorhersehbarere und konsistentere Erfahrung bei der Bearbeitung von Canvas-Schritten und -Nachrichten zu schaffen.

#### Sind API-getriggerte oder geplante Canvase von dieser Änderung betroffen?

Nein.

#### Hat diese Änderung Auswirkungen auf die Canvas-Eingangs-Eigenschaften?

Ja, dies hat Auswirkungen auf `canvas_entry_properties`, wenn `canvas_entry_property` in einem aktionsbasierten Canvas verwendet wird und der Eigenschaftstyp `time` ist. Unter allen Umständen empfehlen wir die Verwendung von Liquid-`time_zone`-Filtern, damit Zeitstempel in der gewünschten Zeitzone dargestellt werden.

Hier ist ein Beispiel, wie Sie dies umsetzen können:

| Liquid im Nachrichten-Schritt | Ausgabe | Ist dies die korrekte Methode, um Zeitzonen in Liquid darzustellen? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | Nein |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | Nein
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | Ja |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Was ist ein praktisches Beispiel dafür, wie sich das neue Zeitstempelverhalten auf meine Nachrichten auswirken könnte? {#faq-example}

Angenommen, wir haben ein aktionsbasiertes Canvas, das in einem Nachrichten-Schritt den folgenden Inhalt aufweist:

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

Um eine Zeitzone eindeutig anzugeben, können wir Liquid-`time_zone`-Filter wie folgt verwenden: 

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Dies führt zu folgender Nachricht: 

```
Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!
```

Da die Zeitzone „America/Los_Angeles" mit Liquid angegeben wird, ist der Zeitstempel hier in PST angegeben.

Die bevorzugte Zeitzone kann auch in der Event-Eigenschaften-Payload übermittelt und in der Liquid-Logik verwendet werden:

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### Wie unterscheiden sich Kontextvariablen von Canvas-Eingangs-Eigenschaften?

Canvas-Eingangs-Eigenschaften sind als Canvas-Kontextvariablen enthalten. Das bedeutet, dass Sie Canvas-Eingangs-Eigenschaften über die Braze-API senden und in anderen Schritten referenzieren können, ähnlich wie bei der Verwendung einer Kontextvariablen mit dem Liquid-Snippet.

### Können sich Variablen in einem einzelnen Kontext-Schritt gegenseitig referenzieren?

Ja. Alle Variablen in einem Kontext-Schritt werden nacheinander ausgewertet, d. h. Sie könnten die folgenden Kontextvariablen einrichten:

| Kontextvariable | Wert | Beschreibung |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | Die Lieblingsküche der Nutzer:innen. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | Der verfügbare Rabattcode für Nutzer:innen. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.${promo_code}}} "on delivery from your favorite" {{context.${favorite_cuisine}}} restaurants!"`{% endraw %} | Eine personalisierte Nachricht, die die vorherigen Variablen kombiniert. In einem Nachrichten-Schritt könnten Sie das Liquid-Snippet {% raw %}`{{context.${personalized_message}}}`{% endraw %} verwenden, um die Kontextvariable zu referenzieren und jeder Nutzer:in eine personalisierte Nachricht zu liefern. Sie können auch einen Kontext-Schritt verwenden, um den Wert des [Aktionscodes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) zu speichern und ihn in anderen Schritten innerhalb eines Canvas als Template zu verwenden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Dies gilt auch für mehrere Kontext-Schritte. Stellen Sie sich zum Beispiel diese Sequenz vor:

1. Ein anfänglicher Kontext-Schritt erstellt eine Variable namens `JobInfo` mit dem Wert `job_title`.
2. Ein Nachrichten-Schritt referenziert {% raw %}`{{context.${JobInfo}}}`{% endraw %} und zeigt den Nutzer:innen `job_title` an.
3. Später aktualisiert ein Kontext-Schritt die Kontextvariable und ändert den Wert von `JobInfo` in `job_description`.
4. Alle nachfolgenden Schritte, die `JobInfo` referenzieren, verwenden nun den aktualisierten Wert `job_description`.

Kontextvariablen verwenden im gesamten Canvas ihren neuesten Wert, wobei sich jedes Update auf alle folgenden Schritte auswirkt, die diese Variable referenzieren.