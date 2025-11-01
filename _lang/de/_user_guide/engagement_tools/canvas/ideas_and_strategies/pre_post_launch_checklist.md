---
nav_title: Checkliste vor und nach der Markteinführung
article_title: Checkliste vor und nach dem Start
page_order: 2
description: "Dieser Artikel enthält eine Anleitung für Aufgaben, die Sie vor und nach dem Start eines Canvas überprüfen sollten."
tool: Canvas

---

# Checkliste vor und nach der Markteinführung

> Dieser Artikel enthält eine Anleitung für Aufgaben, die Sie vor und nach dem Start eines Canvas überprüfen sollten.

## Vor dem Start zu berücksichtigende Aspekte

Bevor Sie ein Canvas starten, können Sie einige Details überprüfen, um sicherzustellen, dass Ihre Nachrichten und Sendezeiten mit den Präferenzen Ihrer Zielgruppe übereinstimmen. Zu berücksichtigen sind dabei unter anderem unterschiedliche Zeitzonen, Eingabeeinstellungen und mehr. Verwenden Sie diese Checkliste als Leitfaden, um diese Bereiche auf der Grundlage Ihres Anwendungsfalls zu optimieren und so zum Erfolg Ihres Canvas beizutragen. 

### Überprüfen Sie die Zeitzoneneinstellungen

Wenn Sie die Nutzer:innen entsprechend ihrer lokalen Zeitzone mit einem Zeitplan für die Eingabe eingeben, sollten Sie Ihren Canvas mindestens 24 Stunden vor dem Zeitpunkt starten, an dem die Nutzer:innen Ihren Canvas aufrufen sollen. Im Folgenden finden Sie ein Beispiel für ein Canvas, das nicht genug Zeit zwischen dem Start und der geplanten Eintrittszeit gelassen hat. In diesem Szenario gibt es möglicherweise einige Benutzer, die Ihr Canvas nicht betreten werden, da die geplante Eintrittszeit in bestimmten Zeitzonen bereits verstrichen ist. 

{% alert tip %}
Sie erhalten eine Meldung, wenn Sie nicht genügend Puffer eingeplant haben. Eine schnelle Lösung ist die Anpassung der Sendezeit, um sicherzustellen, dass die Nutzer:innen volle 24 Stunden lang im Zielsegment bleiben können.
{% endalert %}

\![Ein Canvas mit einem Zeitplan, der Nutzer:innen am 30\. April 2025 ab 10 Uhr morgens in ihrer Ortszeit erfasst.]({% image_buster /assets/img_archive/canvas_checklist1.png %}){: style="max-width:75%;"}

### Verwendung regulärer Ausdrücke für Zielgruppenfilter in Betracht ziehen

Nachdem Sie die ersten Details festgelegt haben, wann Ihre Benutzer ein Canvas betreten sollen, sollten Sie nun Ihre Segmente oder Filter im Schritt **Zielgruppe** bei der Erstellung eines Canvas überprüfen. In diesem Schritt können Sie auch die Übersicht über die **Zielgruppen** einsehen, um zu sehen, wie Ihre Zielgruppe eingerichtet wurde. 

Hier sollten Sie in Betracht ziehen, einen regulären Ausdruck für Segmente oder Filter in den Schritten „Zielgruppenpfade“ und Einstellungen für die Zustellungsvalidierung im Nachrichtenschritt und im Decision-Split zu verwenden. Ein [regulärer Ausdruck]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/) (auch Regex genannt) ist eine Zeichenkette, d.h. er erkennt Muster und berücksichtigt Zeichen anstelle von Dingen wie Großschreibung. Das bedeutet, dass Sie bei Verwendung von „Gleich/Ungleich“ aufgrund einfacher Syntaxfehler Ihre Zielgruppe möglicherweise einschränken.

Wenn Sie feststellen, dass Ihre Zielgruppe kleiner ist als erwartet, versuchen Sie es mit „Entspricht Regex“ oder „Entspricht nicht Regex“ anstelle von „Ist gleich“ oder „Ist nicht gleich“. So können Sie die fehlenden Nutzer berücksichtigen und eine größere Zielgruppe ansprechen. 

### Entry-Einstellungen und Race-Condition identifizieren

Eine Race-Condition kann auftreten, wenn Sie in den Einstellungen für den**Entry-Zeitplan** und die **Zielgruppe** dieselben Entry-Kriterien verwendet haben. 

Wenn Sie eine aktionsbasierte Entry verwenden, stellen Sie sicher, dass Sie hier nicht dieselbe Trigger-Aktion wie bei Ihrer Zielgruppe verwendet haben. Es kann eine Race-Condition auftreten, bei der der oder die Nutzer:in zum Zeitpunkt der Ausführung des Trigger-Events nicht in der Zielgruppe ist, was bedeutet, dass er oder sie das Canvas nicht aufrufen wird.

{% alert tip %}
Informieren Sie sich über die [besten Methoden]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#scenario-3-matching-action-based-triggers-and-audience-filters) zur Vermeidung dieser Race-Condition, wenn Sie ein aktionsbasiertes Canvas mit demselben Trigger wie der Zielgruppen-Filter einrichten.
{% endalert %}

### Prüfen Sie die Eigenschaften von Canvas-Einträgen und Ereignissen

Obwohl der Name ähnlich ist, funktionieren [Canvas-Eingabeeigenschaften und Ereigniseigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) innerhalb Ihrer Canvas-Workflows unterschiedlich. Canvas-Eingabeeigenschaften sind an Ihre Eingabeeinstellungen gebunden und können in jeder Nachrichtenkomponente in Ihrem Canvas referenziert werden. Canvas-Entry-Eigenschaften sind Eigenschaften des Events oder des API-Aufrufs, der den Entry eines Nutzers oder einer Nutzerin in ein Canvas auslöst, wobei aktionsbasierte oder API-getriggerte Entry-Einstellungen verwendet werden.

Entry-Eigenschaften hingegen können nur im ersten Nachrichtenschritt nach einem Aktionspfadschritt referenziert werden. Entry-Eigenschaften sind Eigenschaften eines angepassten Events oder eines Kauf-Events, das der oder die Nutzer:in während des Auswertungsfensters eines Aktionspfads durchgeführt hat und das seinen Fortschritt auf einem der definierten Aktionspfade auslöst.

Überprüfen Sie Ihre Nachrichtenvorschau auf Nachrichtenschritte, die auf Canvas-Entry-Eigenschaften oder Event-Eigenschaften verweisen.

### Nachrichtenschritte für den Nutzerfortschritt überprüfen

Standardmäßig durchlaufen die Nutzer:innen alle Schritte der Nachricht, unabhängig davon, ob sie die Nachricht erhalten haben. Wenn Sie die Nutzer:innen, die eine bestimmte Nachricht erhalten, weiterleiten möchten, können Sie dies tun, indem Sie direkt nach Ihrer Nachrichtenkomponente einen Decision-Split-Schritt hinzufügen. Fügen Sie den Filter „Nachricht von Canvas-Schritt erhalten“ als zusätzlichen Filter hinzu und wählen Sie dann den Canvas-Schritt und den Nachrichtenschritt aus.

Für Nachrichtenschritte mit In-App-Benachrichtigung sollten Sie statt der Decision-Split-Komponente eine Aktionspfad-Komponente verwenden. So können Sie Nutzer weiterleiten, je nachdem, ob sie Ihre In-App-Nachricht gesehen haben. Definieren Sie eine Aktionsgruppe, indem Sie den Filter „Mit Schritt interagieren“ hinzufügen und die Option **In App-Nachricht anzeigen** auswählen. Dann setzen Sie das Bewertungsfenster des Schritts auf das Ablauffenster der In-App-Nachricht.

Für eine Nachrichtenkomponente im Multichannel-Messaging empfehlen wir Folgendes:
* Fügen Sie zwischen dem Nachrichtenschritt und dem Decision-Split-Schritt einen Delay-Schritt ein und setzen Sie den Delay auf mindestens fünf Sekunden.
* Wenn die Komponente „Intelligentes Timing“ enthält, stellen Sie die Verzögerung auf 24 Stunden ein.
* Wenn die Komponente eine Ratenbegrenzung enthält, teilen Sie Ihre Nachrichten in mehrere einkanalige Nachrichtenschritte auf und verbinden Sie diese miteinander. Verbinden Sie dann den Decision-Split-Schritt direkt nach dem letzten Nachrichtenschritt, um zu prüfen, ob ein:e Nutzer:in eine der Nachrichten erhalten hat. Sie können diese Methode auch als Alternative für einen Multichannel-Messaging-Schritt mit intelligentem Timing verwenden.

## Was Sie nach dem Start beachten sollten

Sie haben Ihr Canvas gestartet! Was nun? Verwenden Sie diese Checkliste, um zu sehen, wie Sie Ihr Canvas im Falle von Unstimmigkeiten nach dem Start anhand dieser Szenarien überprüfen und anpassen können.

### Viele Einträge, aber wenig Sendungen

Nehmen wir an, Sie haben ein Missverhältnis zwischen der Anzahl Ihrer gesendeten Nachrichten und der Gesamtzahl Ihrer Eingänge festgestellt. Sie können Bereiche identifizieren und aufdecken, in denen Sie Ihren Canvas anpassen müssen, indem Sie diese Schlüsselbereiche überprüfen.

#### Entry-Zielgruppe

Wenn Sie eine Kampagne mit geplantem Versand verwenden, überprüfen Sie Ihre Zielgruppe, indem Sie Ihre Zielpopulation überprüfen. Wie sehen die Zahlen auf den verschiedenen Kanälen aus, und in welchem Verhältnis stehen sie zu den Kanälen, die Sie in Ihrem Canvas verwendet haben? Wenn die niedrigsten Zahlen mit den Kanälen übereinstimmen, die Sie in Ihrem Canvas verwendet haben, haben Sie das Problem möglicherweise gefunden.

#### Erste Komponente des Canvas

Überprüfen Sie alle Zielgruppenfilter, Aktions-Trigger oder Segmente, die in den ersten Komponenten Ihres Canvas verwendet wurden. Gibt es Rechtschreibfehler oder zu strenge Bedingungen, die Ihren Canvas daran hindern, richtig zu starten? Verwenden Sie „Ist gleich“, obwohl Sie „Stimmt mit Regex überein“ verwenden sollten?

#### Canvas-Kontrollgruppe 

Überprüfen Sie die Verteilung der Nutzer zwischen Ihren Varianten und Ihrer Kontrollgruppe. Ist die Kontrollgruppe größer, als Sie es beabsichtigt haben? Wenn ja, können Sie diese Einstellung bearbeiten. Wenn Sie die **Intelligente Auswahl** aktiviert haben und die Kontrollgruppe gewinnt, sollten Sie Ihr Canvas stoppen und einen neuen Ansatz versuchen.

### Ein leeres Gesamtpublikum

Wenn Sie keine Entry-Daten für Ihr Canvas sehen, kann der Grund dafür, dass Nutzer:innen Ihr Canvas nicht betreten, in Race-Conditions und restriktiven Zielgruppensegmentierungsfiltern liegen.

Wenn Sie in Ihrem Entry-Zeitplan die aktionsbasierte Entry verwenden, stellen Sie sicher, dass Sie hier nicht die gleiche Trigger-Aktion verwendet haben wie in Ihrer **Zielgruppe**. Es kann eine Race-Condition auftreten, bei der der oder die Nutzer:in zum Zeitpunkt der Ausführung des Trigger-Events nicht in der Zielgruppe ist, was bedeutet, dass er oder sie das Canvas nicht aufrufen wird.

Prüfen Sie außerdem, ob das ausgewählte Segment Nutzer enthält, indem Sie die Tabelle **Zielpopulation** in den **Zielgruppeneinstellungen** überprüfen. Wenn diese Zahl niedrig ist, sehen Sie nach, wie Sie Ihre Eingabeeinstellungen anpassen oder Ihre ausgewählten Segmente oder Filter auf Fehler überprüfen können.

### Unerwarteter Abfall zwischen den Stufen

Eine weitere offensichtliche Möglichkeit, Bereiche zu identifizieren, in denen Ihr Canvas angepasst werden muss, besteht darin, dass es einen großen Abfall von einem Canvas-Schritt zum nächsten gibt. Überprüfen Sie in diesem Fall, dass Ihre Zielgruppenfilter und Ausnahme-Events keine Rechtschreib- oder Großschreibfehler enthalten. Und wie immer sollten Sie sich vergewissern, dass Ihre Zielgruppenfilter nicht so streng sind, dass sie die Mehrheit Ihrer Nutzer:innen von der Teilnahme am Canvas ausschließen. 

Als Nächstes ist es wichtig, die Einstellungen zu ermitteln, die beeinflussen können, ob und wann Nachrichten an Ihre Nutzer:innen gesendet werden:
- [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)
- Ruhezeiten
- Zustellungsvalidierungen

Im Allgemeinen wählen Sie für Ihren Canvas entweder Intelligent Timing oder Quiet Hours, nicht beides. Es gilt der gleiche Vorschlag, entweder Intelligent Timing oder [Ratenbegrenzung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) zu verwenden, nicht beides. Wenn Sie mehr darüber erfahren möchten, wie Sie die Intelligence Suite am besten nutzen, lesen Sie unsere [Anwendungsfälle zur Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence/#use-cases).

### Verdächtiges Sendevolumen zwischen Pfaden

Wenn das Sendevolumen zwischen zwei oder mehreren Pfaden (entweder Zielgruppenpfade oder Aktionspfade) nicht Ihren Erwartungen entspricht, kann dies eine Gelegenheit sein, Ihre Segmente, Filter oder Trigger-Aktionen zu überprüfen. Stellen Sie außerdem sicher, dass Sie alle überlappenden Filter identifizieren und entfernen.

