---
nav_title: Kontext- und Event-Eigenschaften
article_title: Kontext- und Event-Eigenschaften
page_order: 4.2
page_type: reference
description: "Dieser Referenzartikel erläutert die Unterschiede zwischen Kontext-Eigenschaften und Event-Eigenschaften und wann die jeweilige Eigenschaft verwendet werden sollte."
tool: Canvas
---

# Kontext- und Event-Eigenschaften

> Dieser Referenzartikel enthält Informationen zu `context` und `event_properties`, einschließlich der Frage, wann Sie welche Eigenschaft verwenden sollten und welche Unterschiede im Verhalten bestehen. <br><br> Informationen über benutzerdefinierte Ereigniseigenschaften im Allgemeinen finden Sie unter [Benutzerdefinierte Ereigniseigenschaften]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

Kontexteigenschaften und Event-Eigenschaften funktionieren in Ihren Canvas-Workflows unterschiedlich. Eigenschaften von Events oder API-Aufrufen, die den Entry eines Nutzers oder einer Nutzerin in ein Canvas triggern, werden als `context` bezeichnet. Die Eigenschaften von Ereignissen, die auftreten, wenn sich ein Nutzer:in innerhalb einer Canvas-Journey bewegt, werden`event_properties` als bezeichnet. Der Hauptunterschied besteht darin, dass `context` sich auf mehr als nur Ereignisse konzentriert, indem es auch auf die Eigenschaften von Eingangs-Nutzlasten in API-getriggerten Canvase zugreift.

In der folgenden Tabelle werden die Unterschiede zwischen Kontext-Eigenschaften und Event-Eigenschaften referenziert.

| | Kontexteigenschaften | Event-Eigenschaften |
|----|----|----|
| **Liquid** | `context` | `event_properties` |
| **Persistenz** | Kann während der gesamten Dauer eines mit Canvas erstellten Canvas von allen Nachrichtenschritten referenziert werden. | \- Kann nur einmal referenziert werden. <br> \- Kann nicht von nachfolgenden „Nachricht“-Schritten referenziert werden. |
| **Canvas Verhalten** | Kann in jedem Schritt eines Canvas auf `context` verweisen. Wie Sie sich nach dem Start verhalten, erfahren Sie unter [Bearbeiten von Leinwänden nach dem Start]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties). | \- Kann `event_properties` im ersten „Nachricht“-Schritt **nach** einem [Aktionspfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)-Schritt referenzieren, bei dem die durchgeführte Aktion ein angepasstes Event oder Kauf-Event ist. <br> \- Kann nicht nach dem Pfad Everyone Else des Schritts Action Paths stehen. <br> \- Zwischen den Aktions-Pfaden und den Schritten für Nachrichten können andere Komponenten stehen, die keine Nachrichten sind. Wenn eine dieser Nicht-Nachrichten-Komponenten ein „Aktionspfade“-Schritt ist, kann der oder die Nutzer:in den Pfad „Alle anderen“ dieses Aktionspfads durchlaufen. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details Original Canvas editor details %}

Sie können Canvase nicht mehr mit dem Original-Editor erstellen oder duplizieren. Bitte beachten Sie, dass Canvas Context im ursprünglichen Canvas-Editor nicht unterstützt wird. Dieser Abschnitt dient daher als Referenz, wenn Sie Canvas-Eingangs-Eigenschaften und Event-Eigenschaften für den vorherigen Canvas-Workflow verwenden.

**Canvas Eingang-Eigenschaften:**
- Die Eigenschaften für persistente Eingänge müssen aktiviert sein. 
- Kann nur `canvas_entry_properties` im ersten vollständigen Schritt eines Canvas referenzieren. Der Canvas muss aktionsbasiert oder API-gesteuert sein.

**Eingangs-Eigenschaften:**
- Sie können `event_properties` in jedem vollständigen Schritt referenzieren, der eine aktionsbasierte Zustellung in einem Canvas verwendet.
- Kann nicht in anderen Zeitplänen für vollständige Schritte als dem ersten vollständigen Schritt eines aktionsbasierten Canvas verwendet werden. Wenn ein Nutzer:in jedoch eine [Canvas-Komponente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) verwendet, folgt das Verhalten den aktuellen Canvas-Workflow-Regeln für `event_properties`.

**Event-Eigenschaften:**
- Sie können `event_properties` nicht im Schritt Lead Message verwenden. Stattdessen müssen Sie `canvas_entry_properties` verwenden oder einen Aktionspfadschritt mit dem entsprechenden Event **vor dem** Nachrichtenschritt hinzufügen, der `event_properties` enthält.

{% enddetails %}

### Was Sie wissen sollten

- Der Kontext ist nur als Referenz in Liquid verfügbar. Um nach den Eigenschaften innerhalb des Canvas zu filtern, verwenden Sie stattdessen die [Segmentierung von Event-Eigenschaften]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).
- Für In-App-Nachrichtenkanäle können Sie in einem Canvas`event_properties` auf`context`  und  referenzieren. `event_properties`Auf  kann zugegriffen werden, wenn es im ersten Canvas-Schritt enthalten ist, da es triggerbasiert ist.
- Sie können `event_properties` nicht für den Lead-Nachrichtenschritt verwenden. Alternativ können Sie einen Schritt „Aktions-Pfade“ mit dem entsprechenden Ereignis **vor** dem Schritt „Nachricht“ verwenden`context`oder hinzufügen, der Folgendes enthält`event_properties`: .
- Wenn ein „Aktionspfad“-Schritt einen Trigger vom Typ „Eingehende SMS-Nachricht gesendet“ oder „Eingehende WhatsApp-Nachricht gesendet“ enthält, können die nachfolgenden Canvas-Schritte eine SMS- oder WhatsApp-Liquid-Eigenschaft enthalten. Dies spiegelt die Funktionsweise der Event-Eigenschaften in Canvase wider. Auf diese Weise können Sie Ihre Nachrichten nutzen, um First-Party-Daten zu Nutzerprofilen und Gesprächs-Messaging zu speichern und zu referenzieren.

{% alert note %}
Die Teilnahmeberechtigung der Zielgruppen wird einmalig beim Eingang in Canvas überprüft. Wenn eine Nutzer:in während der Eingabe zusammengeführt wird, durchläuft die identifizierte Nutzer:in weiterhin das Canvas und wird nicht erneut anhand der Canvas-Segmentierungskriterien bewertet.
{% endalert %}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Zeitstempel für Trigger

Wenn Sie Zeitstempel mit einem [Datums-/Zeit-Typ]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) aus Ereignissen verwenden, die aktionsbasierte Canvases triggern, die über [den Kontext]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) referenziert werden, werden die Zeitstempel auf UTC normalisiert.

Angesichts dieses Verhaltens empfiehlt Braze dringend die Verwendung eines Liquid Zeitzonen-Filters wie dem folgenden Beispiel, um zu gewährleisten, dass Ihre Nachrichten in der von Ihnen [bevorzugten Zeitzone]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter) gesendet werden.

{% raw %}
```liquid
{{context.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }}
```
{% endraw %}

#### Ausnahmen

- Zeitstempel werden im ersten Schritt eines Canvas nicht auf UTC normalisiert, wenn dieser Schritt ein Nachrichten-Schritt ist.
- Zeitstempel werden in jedem Nachrichten-Schritt, der den In-App-Nachrichten-Kanal verwendet, nicht auf UTC normalisiert, unabhängig von der Reihenfolge im Canvas.

## Anwendungsfall

![Ein Aktions-Pfad, gefolgt von einem Verzögerungsschritt und einem Nachrichten-Schritt für Nutzer:innen, die einen Artikel zu ihrer Wunschliste hinzugefügt haben, und ein Pfad für alle anderen.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Um die Unterschiede zwischen`context`und besser zu `event_properties`verstehen, betrachten wir das folgende Szenario, in dem Nutzer:innen ein aktionsbasiertes Canvas aufrufen, wenn sie das angepasste Event „Artikel zur Wunschliste hinzufügen” ausführen. 

Der Kontext wird im Canvas-Schritt beim Erstellen einer Leinwand konfiguriert und entspricht dem Zeitpunkt, zu dem eine Nutzer:in eine Leinwand betritt. Der Kontext kann auch in jedem Schritt des Nachrichten-Prozesses referenziert werden.

In diesem Canvas haben wir eine User Journey, die mit einem „Aktionspfad-Schritt“ beginnt, um festzustellen, ob ein:e Nutzer:in einen Artikel zu seiner oder ihrer Wunschliste hinzugefügt hat. Wenn die Nutzer:in einen Artikel hinzugefügt hat, kommt es zu einer Verzögerung, bevor sie die Nachricht „Neuer Artikel in Ihrer Wunschliste!“ aus dem Schritt „Nachricht“ erhält. 

Der erste Schritt „Nachricht“ in einer User Journey hat Zugriff auf die benutzerdefinierten Einstellungen`event_properties` aus Ihrem Schritt „Aktions-Pfade“. In diesem Fall können wir ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` in diesem „Nachricht“-Schritt als Teil des Contents unserer Nachrichten einbinden. Wenn ein Nutzer:in keinen Artikel zu seiner Wunschliste hinzufügt, durchläuft er den Pfad „Alle anderen“, was bedeutet, dass der Artikel`event_properties`nicht referenziert werden kann und einen ungültigen Einstellungsfehler anzeigt.

Beachten Sie, dass Sie nur dann auf `event_properties` zugreifen können, wenn Ihr „Nachricht“-Schritt auf einen Pfad in einem „Aktionspfade“-Schritt zurückverfolgt werden kann, der nicht „Alle anderen“ ist. Wenn der Schritt „Nachricht“ mit einem Pfad „Alle anderen“ verbunden ist, jedoch zu einem Schritt „Aktions-Pfade“ in der Benutzerreise zurückverfolgt werden kann, haben Sie weiterhin Zugriff auf `event_properties`. Weitere Informationen zu diesen Verhaltensweisen finden Sie unter [Nachrichtenschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

