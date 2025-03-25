---
nav_title: Eigenschaften von Canvas-Einträgen und Ereigniseigenschaften
article_title: Eigenschaften von Canvas-Einträgen und Ereigniseigenschaften
page_order: 4.2
page_type: reference
description: "Dieser Referenzartikel beschreibt die Unterschiede zwischen Canvas-Eingabeeigenschaften und Ereigniseigenschaften und wann Sie welche Eigenschaft verwenden sollten."
tool: Canvas
---

# Eigenschaften der Leinwandeinträge und Ereigniseigenschaften

> Dieser Referenzartikel enthält Informationen zu `canvas_entry_properties` und `event_properties`, einschließlich der Frage, wann Sie welche Eigenschaft verwenden sollten und welche Unterschiede im Verhalten bestehen. <br><br> Informationen über benutzerdefinierte Ereigniseigenschaften im Allgemeinen finden Sie unter [Benutzerdefinierte Ereigniseigenschaften]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

{% alert important %}
Ab dem 28\. Februar 2023 können Sie keine Canvase mehr mit dem Original-Editor erstellen oder duplizieren. Dieser Artikel steht als Referenz zur Verfügung, wenn Sie `canvas_entry_properties` und `event_properties` für den ursprünglichen Canvas-Workflow verwenden.
{% endalert %}

Canvas-Eingabeeigenschaften und Ereigniseigenschaften funktionieren innerhalb Ihrer Canvas-Workflows unterschiedlich. Eigenschaften von Events oder API-Aufrufen, die den Entry eines Nutzers oder einer Nutzerin in ein Canvas triggern, werden als `canvas_entry_properties` bezeichnet. Eigenschaften von Events, die auftreten, wenn sich ein:e Nutzer:in durch eine Canvas-Journey bewegt, werden als `event_properties` bezeichnet. Der Hauptunterschied besteht darin, dass `canvas_entry_properties` sich nicht nur auf Events konzentriert, sondern auch auf die Eigenschaften von Entry-Nutzdaten in API-getriggerten Canvase zugreift.

Für den ursprünglichen Canvas-Editor und Canvas Flow können Sie `event_properties` nicht im Hauptschritt „Nachricht“ verwenden. Stattdessen müssen Sie `canvas_entry_properties` verwenden oder einen „Aktionspfade“-Schritt mit dem entsprechenden Event **vor dem** Schritt „Nachricht“ hinzufügen, der `event_properties` enthält.

Das Verhalten variiert auch zwischen Workflows, die mit Canvas Flow und dem Original-Editor erstellt wurden. Im ursprünglichen Canvas-Editor können Sie zum Beispiel `event_properties` im ersten vollständigen Schritt verwenden, wenn es sich um einen aktionsbasierten Schritt handelt. In Canvas Flow werden keine vollständigen Schritte unterstützt, sodass dies nicht zutrifft.

In der folgenden Tabelle finden Sie eine Zusammenfassung der Unterschiede zwischen `canvas_entry_properties` und `event_properties`.

| | Entry-Eigenschaften für Canvas | Event-Eigenschaften
|----|----|----|
| **Liquid** | `canvas_entry_properties` | `event_properties` |
| **Persistenz** | Kann von allen [Nachrichtenschritten][1] während der Dauer eines mit Canvas Flow erstellten Canvas referenziert werden. | \- Kann nur einmal referenziert werden. <br> \- Kann nicht von nachfolgenden „Nachricht“-Schritten referenziert werden. |
| **Original-Canvas-Verhalten** | \- Sie müssen die Eigenschaften für dauerhafte Einträge aktiviert haben. <br> \- Kann nur im ersten vollständigen Schritt eines Canvas auf `canvas_entry_properties` verweisen. Der Canvas muss aktionsbasiert oder API-gesteuert sein. | \- Sie können `event_properties` in jedem vollständigen Schritt referenzieren, der eine aktionsbasierte Zustellung in einem Canvas verwendet. <br> \- Kann nicht in geplanten Vollschritten verwendet werden, außer im ersten Vollschritt eines aktionsbasierten Canvas. Wenn ein:e Nutzer:in jedoch eine [Canvas-Komponente][2] verwendet, folgt das Verhalten den Canvas Flow-Regeln für `event_properties`. |
| **Canvas Flow-Verhalten** | Kann in jedem Schritt eines Canvas auf `canvas_entry_properties` verweisen. Wie Sie sich nach dem Start verhalten, erfahren Sie unter [Bearbeiten von Leinwänden nach dem Start]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties). | \- Kann `event_properties` im ersten „Nachricht“-Schritt **nach** einem [Aktionspfade][3]-Schritt referenzieren, bei dem die durchgeführte Aktion ein angepasstes Event oder Kauf-Event ist. <br> \- Kann nicht nach dem Pfad Everyone Else des Schritts Action Paths stehen. <br> \- Zwischen den Schritten „Aktionspfade“ und „Nachricht“ können andere Canvas-Komponenten, die keine Nachrichten sind, eingefügt werden. Wenn eine dieser Nicht-Nachrichten-Komponenten ein „Aktionspfade“-Schritt ist, kann der oder die Nutzer:in den Pfad „Alle anderen“ dieses Aktionspfads durchlaufen. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Beachten Sie, dass die Canvas-Entry-Eigenschaften nur in Liquid referenziert werden können. Um nach den Eigenschaften innerhalb des Canvas zu filtern, verwenden Sie stattdessen die [Segmentierung von Event-Eigenschaften]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/nested_objects/).

{% alert note %}
Für In-App-Nachricht-Kanäle kann `canvas_entry_properties` nur dann in Canvas Flow und im ursprünglichen Canvas-Editor referenziert werden, wenn Sie [persistente Entry-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) im ursprünglichen Editor als Teil des früheren Early Access aktiviert haben. `event_properties` kann jedoch nicht für In-App-Nachricht-Kanäle verwendet werden.
{% endalert %}

Wenn ein „Aktionspfad“-Schritt einen Trigger vom Typ „Eingehende SMS-Nachricht gesendet“ oder „Eingehende WhatsApp-Nachricht gesendet“ enthält, können die nachfolgenden Canvas-Schritte eine SMS- oder WhatsApp-Liquid-Eigenschaft enthalten. Dies spiegelt wider, wie Event-Eigenschaften in Canvas Flow funktionieren. Auf diese Weise können Sie Ihre Nachrichten nutzen, um First-Party-Daten zu Nutzerprofilen und Gesprächs-Messaging zu speichern und zu referenzieren.

## Anwendungsfall

![][7]{: style="float:right;max-width:30%;margin-left:15px;"}

Um die Unterschiede zwischen `canvas_entry_properties` und `event_properties` besser zu verstehen, lassen Sie uns dieses Szenario betrachten, in dem Benutzer ein aktionsbasiertes Canvas betreten, wenn sie das benutzerdefinierte Ereignis "Artikel zur Wunschliste hinzufügen" ausführen. 

Die `canvas_entry_properties` werden im Schritt [Eingabezeitplan]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) bei der Erstellung eines Canvas konfiguriert und entsprechen dem Zeitpunkt, zu dem ein Benutzer ein Canvas betritt. Diese `canvas_entry_properties` können auch in jedem „Nachricht“-Schritt in Canvas Flow referenziert werden, da Canvas Flow persistente Entry-Eigenschaften unterstützt. 

In diesem Canvas haben wir eine User Journey, die mit einem „Aktionspfad-Schritt“ beginnt, um festzustellen, ob ein:e Nutzer:in einen Artikel zu seiner oder ihrer Wunschliste hinzugefügt hat. Wenn der oder die Nutzer:in einen Artikel hinzugefügt hat, erhält er oder sie erst mit Verzögerung die Nachricht „Neuer Artikel in Ihrer Wunschliste“ aus dem „Nachricht“-Schritt. 

Der erste „Nachricht“-Schritt in einer User Journey hat Zugriff auf die angepasste `event_properties` aus Ihrem „Aktionspfad-Schritt“. In diesem Fall können wir ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` in diesem „Nachricht“-Schritt als Teil des Contents unserer Nachrichten einbinden. Wenn ein:e Nutzer:in keinen Artikel zu seiner oder ihrer Wunschliste hinzufügt, durchläuft er oder sie über den Pfad „Alle anderen“, d. h. `event_properties` kann nicht referenziert werden und zeigt einen Fehler mit ungültigen Einstellungen an.

Beachten Sie, dass Sie nur dann auf `event_properties` zugreifen können, wenn Ihr „Nachricht“-Schritt auf einen Pfad in einem „Aktionspfade“-Schritt zurückverfolgt werden kann, der nicht „Alle anderen“ ist. Wenn der „Nachricht“-Schritt mit einem „Alle anderen“-Pfad verbunden ist, aber auf einen „Aktionspfade“-Schritt in der User Journey zurückverfolgt werden kann, dann haben Sie auch weiterhin Zugriff auf `event_properties`. Weitere Informationen zu diesen Verhaltensweisen finden Sie unter [„Nachricht“-Schritt ][8].

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/
[3]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/
[7]: {% image_buster /assets/img_archive/canvas_entry_properties1.png %}
[8]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
