---
nav_title: Kontext 
article_title: Kontext 
alias: /context/
page_order: 1.5
page_type: reference
toc_headers: "h2"
description: "Dieser referenzierte Artikel beschreibt, wie Sie Kontext-Schritte in Ihrem Canvas erstellen und verwenden."
tool: Canvas

---

# Kontext

> Kontextschritte erlauben es Ihnen, eine oder mehrere Variablen für einen Nutzer:innen zu erstellen und zu aktualisieren, während er sich durch ein Canvas bewegt. Wenn Sie zum Beispiel ein Canvas haben, das saisonale Rabatte verwaltet, können Sie eine Kontextvariable verwenden, um jedes Mal, wenn ein Nutzer:in das Canvas eintritt, einen anderen Rabattcode zu speichern.

{% alert important %}
Context Steps befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Konto Manager:in, wenn Sie an der Teilnahme an diesem frühen Zugang interessiert sind.<br><br>Beachten Sie, dass das Opt-in für den frühen Zugriff auf den Canvas-Kontext-Schritt die Handhabung von Zeitstempeln für alle Ihre Canvase aktualisiert. Um mehr darüber zu erfahren, referenzieren Sie auf [Standardisierung der Zeitzonenkonsistenz](#time-zone-consistency-standardization).
{% endalert %}

## Funktionsweise

![Ein Context-Schritt als erster Schritt eines Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Mit Kontextschritten können Sie temporäre Daten während der Reise eines Nutzers:innen durch einen bestimmten Canvas erstellen und verwenden. Diese Daten existieren nur innerhalb dieser Canvas-Reise und bleiben nicht über verschiedene Canvase oder außerhalb der Sitzung bestehen.

Eine vollständige Referenz zu Kontextvariablen, einschließlich Datentypen, Verwendung und bewährter Verfahren, finden Sie in der [Referenz zu Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

Innerhalb eines Kontextschritts können Sie bis zu 10 Kontextvariablen definieren oder aktualisieren. Diese Variablen können verwendet werden, um Verzögerungen zu personalisieren, Nutzer:innen dynamisch zu segmentieren und das Messaging im gesamten Canvas anzureichern. Sie könnten zum Beispiel eine Kontextvariable für die geplante Flugzeit eines Nutzers:innen erstellen und diese dann verwenden, um personalisierte Verspätungen festzulegen und Erinnerungen zu versenden.

Sie können Kontextvariablen auf zwei Arten setzen:

- **Am Eingang von Canvas:** Daten aus dem Ereignis oder dem API-Trigger können automatisch Kontextvariablen auffüllen.
- **In einem Context-Schritt:** Definieren oder aktualisieren Sie Kontextvariablen manuell, indem Sie einen Kontextschritt hinzufügen.

Jede Kontextvariable benötigt einen Namen, einen Datentyp und einen Wert (der mit Liquid oder dem Tool Personalisierung hinzufügen festgelegt wird). Wenn sie definiert sind, können Sie mit Liquid im gesamten Canvas auf Kontextvariablen referenzieren, z. B. {% raw %}`{{context.${flight_time}}}`{% endraw %}.

Jeder Canvas-Eingang definiert die Kontextvariablen auf der Grundlage der neuesten Daten und der Canvas-Einstellungen neu, was es Nutzern:innen erlaubt, mehrere aktive Reisen mit eigenem Kontext zu haben. Wenn eine Kund:in beispielsweise zwei Flüge ansteht, hat sie zwei verschiedene Reisezustände, die gleichzeitig ablaufen - jeder mit seinen eigenen flugspezifischen Kontextvariablen wie Abflugzeit und Ziel. So ist es zulässig, personalisierte Erinnerungen an den 14-Uhr-Flug nach New York zu senden und gleichzeitig verschiedene Updates für den morgigen 8-Uhr-Flug nach Los Angeles zu verschicken, so dass jede Nachricht für die jeweilige Buchung relevant bleibt.

### Nutzer:in und Stapelverarbeitung

Kontextbezogene Schritte verarbeiten Nutzer:innen in Batches, um die Performance zu optimieren. Wenn Nutzer:innen einen Kontextschritt eingeben, verarbeitet Braze sie standardmäßig in Stapeln von 1.000 Nutzer:innen. Diese Stapel werden parallel verarbeitet, aber innerhalb jedes Stapels werden die Nutzer:innen nacheinander verarbeitet.

Dies bedeutet:
- **Parallele Stapelverarbeitung**: Mehrere Stapel von 1.000 Nutzer:innen werden gleichzeitig verarbeitet, was eine effiziente Bearbeitung großer Zielgruppen zulässig macht.
- **Sequentielle Verarbeitung innerhalb von Stapeln**: Innerhalb jedes Stapels werden die Nutzer:innen nacheinander bearbeitet. Wenn Ihr Kontextschritt [Connected-Content-Aufrufe]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) enthält, muss die Anfrage jedes Nutzers:innen für Connected-Content abgeschlossen sein, bevor der nächste Nutzer:innen in diesem Stapel verarbeitet wird.
- **Unabhängige Chargenprogression**: Jede Charge wird unabhängig voneinander bearbeitet. Wenn die Verarbeitung eines Stapels abgeschlossen ist, bringen diese Nutzer:innen sofort den nächsten Schritt voran, auch wenn andere Stapel noch in Bearbeitung sind. Das bedeutet, dass Nutzer:innen aus verschiedenen Chargen die nachfolgenden Schritte zu unterschiedlichen Zeiten erreichen können.

**Beispiel**: Wenn 3.500 Nutzer:innen einen Context-Schritt mit Connected-Content eingeben, dauert das 650 ms pro Nutzer:in:
- Braze erstellt etwa 4 Stapel von Nutzer:innen (612, 802, 1.000, 880 und 120 in diesem Beispiel).
- Jeder Stapel verarbeitet Nutzer:innen nacheinander, so dass ein Stapel von 1.000 Nutzer:innen etwa 11 Minuten (1.000 × 650ms) dauert.
- Die Batches werden zu unterschiedlichen Zeiten abgeschlossen, so dass die Nutzer:innen nach und nach in den nächsten Schritt übergehen, wenn ihr Batch beendet ist.
- Die ersten Nutzer:innen erreichen den nächsten Schritt möglicherweise mehrere Minuten vor den letzten Nutzer:innen, je nach Stapelgröße und Connected-Content-Antwortzeiten.

Ohne Connected-Content laufen die Kontextschritte viel schneller ab, da keine externen API-Aufrufe abgewartet werden müssen.

## Überlegungen

- Sie können bis zu 10 Kontextvariablen pro Context-Schritt definieren.
- Jede Variable benötigt einen eindeutigen Namen (nur Buchstaben, Zahlen, Unterstriche, bis zu 100 Zeichen).
- Die Gesamtgröße aller Variablen in einem Schritt darf 50 KB nicht überschreiten.
- Variablen, die mit Hilfe von API-Triggern übergeben werden, teilen sich denselben Namensraum wie die in Kontextschritten erstellten Variablen; die Neudefinition einer Variablen in einem Kontextschritt setzt den API-Wert außer Kraft.

Weitere Einzelheiten und die fortgeschrittene Verwendung finden Sie unter [Kontextvariablen referenzieren]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

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
2. Wählen Sie einen [Datentyp](#context-variable-types) aus.
3. Schreiben Sie einen Liquid-Ausdruck manuell oder verwenden Sie **Personalisierung hinzufügen**, um ein Liquid-Snippet aus bereits vorhandenen Attributen zu erstellen.
4. Wählen Sie **Vorschau**, um den Wert Ihrer Kontextvariablen zu überprüfen.
5. (Optional) Um weitere Variablen hinzuzufügen, wählen Sie **Kontextvariable hinzufügen** und wiederholen Sie die Schritte 1-4.
6. Wenn Sie fertig sind, wählen Sie **Fertig**.

Jetzt können Sie Ihre Kontextvariable überall dort verwenden, wo Sie Liquid einsetzen, z.B. in den Schritten Nachrichten und Nutzer:innen Update, indem Sie **Personalisierung hinzufügen** auswählen. Eine vollständige Beschreibung finden Sie unter [Kontextvariablen referenzieren]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

### Kontextabhängige Filter

Sie können in [Zielgruppen-Pfaden]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) und [Decision-Split-Schritten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) Filter mit Hilfe von Kontextvariablen erstellen. Für die Einrichtung des Filters, die Vergleichslogik und die vorgebrachten Beispiele lesen Sie bitte die [Referenz der Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters).

## Vorschau der Nutzer:innen Pfade

Wir empfehlen Ihnen, [Ihre Nutzer:innen-Pfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) zu testen und [eine Vorschau zu erstellen]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths), um sicherzustellen, dass Ihre Nachrichten an die richtige Zielgruppe gesendet und die Kontextvariablen entsprechend den erwarteten Ergebnissen ausgewertet werden.

{% alert note %}
Wenn Sie eine Vorschau Ihres Canvas im Bereich **Vorschau & Testversand** des Editors anzeigen, wird der Zeitstempel in der Vorschau der Testnachricht **nicht** auf UTC standardisiert, da dieses Panel Vorschauen als Strings generiert. Wenn ein Canvas so eingerichtet ist, dass er ein `time` Objekt akzeptiert, bedeutet dies, dass die Vorschau der Nachricht nicht genau das zeigt, was passiert, wenn der Canvas live ist. Um Ihr Canvas möglichst genau zu testen, empfehlen wir stattdessen eine Vorschau der Nutzer:innen.
{% endalert %}

Achten Sie auf häufige Szenarien, die ungültige Kontextvariablen erzeugen. Bei der Vorschau Ihres Nutzerpfads können Sie die Ergebnisse der personalisierten Verzögerungsschritte anhand von Kontextvariablen sowie alle Vergleiche von Zielgruppen-, Entscheidungs- oder Aktions-Pfad-Schritten sehen, die Nutzer:innen mit Kontextvariablen abgleichen.

Wenn die Kontextvariable gültig ist, können Sie die Variable in Ihrem gesamten Canvas referenzieren. Wenn die Kontextvariable jedoch nicht korrekt erstellt wurde, werden auch zukünftige Schritte in Ihrem Canvas nicht korrekt ausgeführt. Wenn Sie z.B. einen Kontextschritt erstellen, um Nutzern:innen einen Termin zuzuweisen, und den Wert des Termins auf ein vergangenes Datum setzen, wird die Erinnerungs-E-Mail in Ihrem Schritt Nachricht nicht gesendet.

## Connected-Content-Strings in JSON umwandeln

Bei einem [Connected-Content-Aufruf]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) in einem Context-Schritt wird das vom Aufruf zurückgegebene JSON aus Gründen der Konsistenz und Fehlervermeidung als String-Datentyp ausgewertet. Wenn Sie diesen String in JSON umwandeln möchten, konvertieren Sie ihn mit `as_json_string`. Zum Beispiel:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Standardisierung der Zeitzonenkonsistenz

Während die meisten Event-Eigenschaften, die den Typ Zeitstempel verwenden, in Canvas bereits in UTC vorliegen, gibt es einige Ausnahmen. Mit der Hinzufügung von Canvas Context sind alle Standard Zeitstempel Event-Eigenschaften in aktionsbasierten Canvase in UTC. Diese Änderung ist Teil umfassenderer Bemühungen, die Bearbeitung von Canvas-Schritten und Nachrichten berechenbarer und konsistenter zu gestalten. Beachten Sie, dass sich diese Änderung auf alle aktionsbasierten Canvase auswirkt, unabhängig davon, ob das jeweilige Canvas einen Kontext-Schritt verwendet oder nicht.

{% alert important %}
In jedem Fall empfehlen wir dringend die Verwendung von [Liquid time_zone Filtern]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know), damit die Zeitstempel in der gewünschten Zeitzone dargestellt werden. Als Beispiel können Sie auf diese [häufig gestellte Frage](#faq-example) referenzieren.
{% endalert %}

## Fehlersuche

### Ungültige Kontextvariablen

Eine Kontextvariable wird als ungültig betrachtet, wenn:

- Ein Aufruf eines eingebetteten Connected-Content schlägt fehl.
- Der Liquid-Ausdruck gibt zur Laufzeit einen Wert zurück, der nicht mit dem Datentyp übereinstimmt oder leer ist (null).

Wenn zum Beispiel der Datentyp der Kontextvariablen **Number** ist, der Liquid-Ausdruck aber einen String zurückgibt, ist er ungültig.

Unter diesen Umständen:
- Der Nutzer:in bringt den nächsten Schritt voran.
- Die Analytics des Canvas-Schritts zählen dies als _Nicht aktualisiert_.

Überwachen Sie bei der Fehlerbehebung die Metrik _Nicht aktualisiert_, um zu prüfen, ob Ihre Kontextvariable korrekt aktualisiert wird. Wenn die Kontextvariable ungültig ist, können Ihre Nutzer:innen nach dem Kontext-Schritt in Ihrem Canvas weitermachen, sich aber möglicherweise nicht für spätere Schritte qualifizieren.

Unter [Datentypen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types) finden Sie die Beispiel-Setups für jeden Datentyp.

### Verzögerungen beim Senden mit Connected-Content

Wenn Connected-Content in einem Kontextschritt fehlschlägt, bringen erfolgreiche Nutzer:innen sofort den nächsten Schritt voran, während fehlgeschlagene Nutzer:innen separat erneut versucht werden. Das bedeutet, dass ein Stapel nicht darauf wartet, dass alle Nutzer:innen erfolgreich sind, bevor er fortschreitet. Erfolgreiche Nutzer:innen kommen weiter, sobald ihr Connected-Content-Aufruf abgeschlossen ist.

**Verhalten bei Wiederholung**: Context-Schritte (und alle Canvas-Schritte) verwenden Canvas-spezifische Wiederholungsmechanismen und nicht das standardmäßige Wiederholungsverhalten von Connected-Content. Wenn ein Connected-Content-Aufruf fehlschlägt, wiederholt Braze den Schritt etwa 13 Mal mit exponentiellem Backoff. Wenn alle Wiederholungsversuche fehlschlagen, verlässt der Nutzer:innen den Canvas.

**Anmerkung**: Der Tag `:retry`, der in standardmäßigen Connected-Content verwendet wird, gilt nicht für Connected-Content-Aufrufe, die innerhalb von Canvas-Schritten erfolgen. Canvas-Schritte haben ihre eigene Wiederholungslogik, die für Canvas-Workflows optimiert ist.

**Bearbeitungszeit**: Die Zeit, die benötigt wird, um alle Nutzer:innen durch einen Kontextschritt zu führen, hängt ab von:
- Die Anzahl der Nutzer:innen, die den Schritt betreten
- Ob Connected-Content verwendet wird (und seine Reaktionszeit)
- Die Stapelgröße (Standard 1.000 Nutzer:innen pro Stapel)

Wenn Ihr Connected-Content Endpunkt Rate-Limits hat, sollten Sie bedenken, dass Context-Steps die Nutzer:innen innerhalb jedes Stapels nacheinander verarbeiten, wodurch Rate-Limits auf natürliche Weise eingehalten werden können. Mehrere Stapel werden jedoch parallel verarbeitet. Stellen Sie also sicher, dass Ihr Endpunkt Anfragen aus mehreren Stapeln gleichzeitig bearbeiten kann.

## Häufig gestellte Fragen

### Was ändert sich, wenn Canvas Context allgemein verfügbar wird?

Wenn Canvas Context allgemein verfügbar wird, gelten die folgenden Details:

- Alle Zeitstempel vom [Typ datetime]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) aus [Event-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) in aktionsbasierten Canvase sind in [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). 
- Diese Änderung wirkt sich auf alle aktionsbasierten Canvase aus, unabhängig davon, ob der jeweilige Canvas einen Kontext-Schritt verwendet oder nicht.

#### Was ist der Grund für diese Änderung?

Diese Änderung ist Teil umfassenderer Bemühungen, die Bearbeitung von Canvas-Schritten und Nachrichten berechenbarer und konsistenter zu gestalten.

#### Wann tritt diese Änderung in Kraft?

- Wenn Sie am Canvas Context Frühzugang teilnehmen, wurde diese Änderung bereits vorgenommen. 
- Wenn Sie nicht am frühen Zugang zu Canvas Context teilnehmen, gilt diese Änderung, wenn Sie dem frühen Zugang beitreten oder wenn Canvas Context allgemein verfügbar wird.

#### Sind API-getriggerte oder geplante Canvase von dieser Änderung betroffen?

Nein.

#### Wirkt sich diese Änderung auf die Eigenschaften von Canvas-Eingängen aus?

Ja, dies wirkt sich auf `canvas_entry_properties` aus, wenn die `canvas_entry_property` in einem aktionsbasierten Canvas verwendet wird und die Eigenschaft `time` ist. Wir empfehlen in jedem Fall die Verwendung von Liquid `time_zone` Filtern, damit die Zeitstempel in der gewünschten Zeitzone dargestellt werden.

Hier ist ein Beispiel dafür, wie Sie dies tun können:

| Liquid im Schritt Nachrichten | Ausgabe | Ist das die richtige Art, Zeitzonen in Liquid darzustellen? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | Kein:e |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | Kein:e
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | Ja |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Was ist ein praktisches Beispiel dafür, wie sich das neue Zeitstempelverhalten auf meine Nachrichten auswirken könnte? {#faq-example}

Nehmen wir an, wir haben ein aktionsbasiertes Canvas, das in einem Messaging-Schritt den folgenden Inhalt hat:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Das Ergebnis ist die folgende Nachricht: 

```
Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!
```

Da in Liquid keine Zeitzone angegeben ist, ist der Zeitstempel hier in UTC. 

Um eine Zeitzone eindeutig anzugeben, können wir Liquid `time_zone` Filter wie diesen verwenden: 

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Das Ergebnis ist die folgende Nachricht: 

```
Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!
```

Da die Zeitzone Amerika/Los Angeles mit Liquid angegeben wird, ist der Zeitstempel hier in PST.

Die bevorzugte Zeitzone kann auch in der Nutzlast der Event-Eigenschaften gesendet und in der Liquid-Logik verwendet werden:

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### Wie unterscheiden sich die Kontextvariablen von den Eigenschaften der Canvas-Eingänge?

Wenn Sie am frühen Zugriff auf den Canvas-Schritt teilnehmen, sind die Eingangs-Eigenschaften von Canvas jetzt als Canvas-Kontextvariablen enthalten. Das bedeutet, dass Sie die Eingangs-Eigenschaften von Canvas über die Braze API senden und in anderen Schritten referenzieren können, ähnlich wie bei der Verwendung einer Kontextvariablen mit dem Liquid-Snippet.

### Können sich Variablen in einem Singular Context Schritt gegenseitig referenzieren?

Ja Alle Variablen in einem Context-Schritt werden nacheinander ausgewertet, d.h. Sie könnten die folgenden Context-Variablen eingerichtet haben:

| Kontextvariable | Wert | Beschreibung |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | Die Lieblingsküche eines Nutzers:in. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | Der verfügbare Rabattcode für einen Nutzer:innen. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.promo_code}} "on delivery from your favorite" {{context.favorite_cuisine}} restaurants!"`{% endraw %} | Eine personalisierte Nachricht, die die vorherigen Variablen kombiniert. In einem Messaging-Schritt könnten Sie das Liquid Snippet {% raw %}`{{context.${personalized_message}}}`{% endraw %} verwenden, um die Kontextvariable zu referenzieren und jedem Nutzer:in eine personalisierte Nachricht zu liefern. Sie können auch einen Context-Schritt verwenden, um den Wert des [Promo-Codes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) zu speichern und ihn als Template in anderen Schritten eines Canvas zu verwenden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Dies gilt auch für mehrere Context-Schritte. Stellen Sie sich zum Beispiel diese Sequenz vor:
1. Ein anfänglicher Context-Schritt erstellt eine Variable namens `JobInfo` mit dem Wert `job_title`.
2. Der Schritt Nachricht referenziert {% raw %}`{{context.${JobInfo}}}`{% endraw %} und zeigt dem Nutzer:innen `job_title` an.
3. Später aktualisiert ein Context-Schritt die Kontextvariable und ändert den Wert von `JobInfo` in `job_description`.
4. Alle nachfolgenden Schritte, die auf `JobInfo` referenzieren, verwenden nun den aktualisierten Wert `job_description`.

Kontextvariablen verwenden im gesamten Canvas ihren neuesten Wert, wobei sich jedes Update auf alle folgenden Schritte auswirkt, die auf diese Variable referenzieren.
