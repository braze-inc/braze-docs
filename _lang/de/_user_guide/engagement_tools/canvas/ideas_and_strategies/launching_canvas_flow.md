---
nav_title: Starten mit Canvas flow
article_title: Starten mit Canvas Flow
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie ein mit Canvas Flow erstelltes Canvas vor dem Start vorbereiten und testen."
page_type: reference
tool: Canvas
---

# Starten mit Canvas Flow

> Dieser Referenzartikel beschreibt, wie Sie ein mit Canvas Flow erstelltes Canvas vor dem Start vorbereiten und testen. Dazu gehört die Identifizierung wichtiger Canvas-Kontrollpunkte wie Canvas-Entry-Bedingungen, Zielgruppenzusammenfassungen und Nutzersegmente.

Bei der Vorbereitung des Starts Ihres Canvas empfiehlt Braze, dass Sie Ihr Canvas in jeder Phase des Canvas-Builders auf Einstellungen überprüfen, die sich auf das Versenden von Nachrichten auswirken können, einschließlich:
* [Race-Conditions](#race-conditions)
* [Lieferzeiten](#delivery-times)
* [Benutzer-Segmente](#segment-users)

## Race-Conditions 

Berücksichtigen Sie die [Race Conditions]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/), die auftreten können, bevor Sie Ihr Canvas starten. 

Um an einem Canvas teilzunehmen, müssen Nutzer:innen vor dem Entry-Zeitplan zur Zielgruppe gehören, unabhängig davon, ob das Canvas geplant, aktionsbasiert oder API-gesteuert ist. 

\![Ein aktionsbasiertes Canvas, das Nutzer:innen einträgt, wenn sie während der Ortszeit eines Nutzers vom 30\. April 2025 um 12 Uhr bis zum 7\. Mai 2025 um 12 Uhr einen Kauf tätigen.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Beachten Sie, dass Nutzer:innen, die sich nach dem Start des Canvas für Ihre Zielgruppe qualifizieren, nicht am Canvas teilnehmen.

{% alert tip %}
Unter [Eintragszeitplan-Typen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule) finden Sie Anleitungen und Details dazu, wann Sie eine geplante, aktionsbasierte oder API-ausgelöste Bereitstellung für Ihr Canvas verwenden sollten!
{% endalert %}

### Entry-Zielgruppenfilter überprüfen

Vermeiden Sie es im Allgemeinen, ein aktionsbasiertes oder API-getriggertes Canvas mit demselben Auslöser wie den Zielgruppenfilter zu konfigurieren. Wenn z. B. ein Canvas gestartet wird, werden Nutzer:innen, die eine bestimmte Aktion ausführen, in die Entry-Zielgruppe aufgenommen, sodass es nicht notwendig ist, das Ereignis als Zielgruppenfilter hinzuzufügen. 

Weitere Einzelheiten zu den verfügbaren Segmentierungsfiltern, mit denen Sie Ihre Zielgruppe ansprechen können, finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

### Mehrere API-Anfragen stapeln

Stellen Sie Ihre Anfragen in einem einzigen API-Aufruf und nicht in mehreren Aufrufen, um sicherzustellen, dass das Benutzerprofil zuerst erstellt oder aktualisiert wird. Weitere Beispiele finden Sie unter [Mehrere Endpunkte verwenden]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#using-multiple-api-endpoints).

### Eine Verzögerung hinzufügen

Eine weitere Möglichkeit zur Vermeidung von Race-Conditions besteht darin, den Delay-Schritt (idealerweise auf 5 Minuten eingestellt) als ersten Schritt Ihres Canvas zu verwenden. 

So haben Sie genug Zeit, um Attribute, E-Mail-Adressen und Push-Tokens zu neuen Benutzerprofilen zu verarbeiten, bevor sie für die folgenden Canvas-Schritte ausgewählt werden. Ohne diesen Delay-Schritt ist es möglich, dass eine E-Mail an einen Nutzer oder eine Nutzerin gesendet wird, dessen oder deren E-Mail noch nicht aktualisiert worden ist.

## Lieferzeiten

Das Festlegen einer Canvas-Zustellungszeit in Echtzeit kann zu einer Steigerung des Engagements und der Konversionsraten führen. Notieren Sie sich, welche Lieferfrist Sie für Ihre Leinwand festgelegt haben. Um das Engagement und die Konversionsraten zu erhöhen, ist es am besten, Canvase in Echtzeit auszulösen und nicht auf einer geplanten, wiederkehrenden Basis.

Wenn Sie sich für eine zeitgesteuerte Lieferung Ihres Canvas entschieden haben, empfiehlt Braze, Ihr Canvas mindestens 24 Stunden vor dem gewünschten Start zu planen, um eventuelle Anpassungen an Ihrem Canvas vornehmen zu können.

## Benutzer-Segmente

Bevor Sie Ihre Canvas Flow User Journey mit Komponenten überladen, sollten Sie überlegen, wie Sie eine User Journey einfach halten können. Verwenden Sie die vereinfachte Ansicht im Canvas-Editor, um eine bessere Vorstellung davon zu erhalten, wie sich Ihre User Journey verzweigt. 

Es gibt vier Hauptkomponenten, die Sie verwenden können, um Ihre Nutzer:innen auf einfache und effektive Weise zu segmentieren:

* [Zielgruppenpfade](#audience-paths)
* [Decision-Split](#decision-split)
* [Aktionspfade](#action-paths)
* [Experimentpfade](#experiment-paths)

### Zielgruppenpfade

Verwenden Sie die [Audience Paths-Schritte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/), um Benutzer innerhalb des Canvas auf der Grundlage von benutzerdefinierten Attributen, benutzerdefinierten Ereignissen und früheren Daten zum Nachrichtenverhalten aus Benutzerprofilen zu segmentieren.

### Decision-Split

Mit dem Schritt [Entscheidungsaufteilung]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) können Sie Ihre Benutzer auf der Grundlage ihrer Antworten auf eine polare Frage auf unterschiedliche User Journey-Pfade schicken.

### Aktionspfade

[Aktionspfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) konzentrieren sich auf die Segmentierung von Nutzer:innen auf der Grundlage von Echtzeit-Verhaltensweisen wie angepassten Events, Kaufereignissen und Änderungen an angepassten Attributen. 

### Experimentpfade

Ähnlich wie bei den Aktionspfaden können Sie die Schritte [der Experimentierpfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) in Ihrem Canvas nutzen, um mehrere Canvas-Pfade zusammen mit einer Kontrollgruppe gegeneinander zu testen. So können Sie die Pfad-Performance verfolgen und fundierte Entscheidungen beim Aufbau Ihres Canvas-Journeys treffen. 

## Testen vor dem Start

Nachdem Sie die Feinheiten Ihres Canvas überprüft haben, sehen Sie sich unter [Versenden von Test-Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) verschiedene Methoden an, die Sie nutzen können, um Ihr Canvas mit Testbenutzern zu testen.

## Checkliste für den Start

### Verfügbarkeit der Nutzer:innen prüfen

- Stellen Sie sicher, dass Ihre Nutzer:innen Ihre Segmentierungskriterien erfüllen.
- Bestätigen Sie, dass ihr Abo "abonniert" oder "Opt-in" ist und ihr Push-Token existiert. Wenn Sie diese als Eingangsregeln für Canvas hinzugefügt haben, ist es möglich, dass die Nutzer:innen zwischen dem Eingang in Ihr Canvas und dem Erhalt des Nachrichten-Schritts abgemeldet wurden.
- Bestätigen Sie, dass sie mit Ihren Canvas-Sendeeinstellungen übereinstimmen. (Wenn Nutzer:in "Abonnent:in" sind, die Einstellungen aber auf "Opt-in" stehen, werden Nutzer:in nicht für den Kanal freigeschaltet.)
- Wenn das globale Frequency-Capping für Ihr Canvas aktiviert ist, überprüfen Sie, ob Ihre Regeln die Anzahl der Nachrichten begrenzen, die jeder Nutzer:innen von einem bestimmten Kanal erhalten kann.
- Wenn die Ruhezeiten aktiviert sind, kann die Sendezeit Ihrer Nachrichten beeinträchtigt werden, d.h. Ihre Nachricht wird möglicherweise zum nächsten verfügbaren Zeitpunkt (wenn die Ruhezeiten enden) gesendet oder ganz abgebrochen.
- Prüfen Sie die Verfügbarkeit von Nutzer:innen für zusätzliche Filter in Ihrem Canvas-Schritt.

### Bestätigen Sie, dass sie das erforderliche angepasste Event oder den Kauf durchgeführt haben

- Prüfen Sie, ob es eine Race-Condition gibt, die sich auf die Nachrichten auswirkt, die Nutzer:innen erhalten, wenn sie mehrere Aktionen gleichzeitig triggern.
- Vergewissern Sie sich, dass es in dem Schritt keine spezifischen Filter gibt, die Nutzer:innen am Empfang der Nachricht gehindert haben könnten.
- Suchen Sie nach Konflikten zwischen verschiedenen Schritten innerhalb desselben Canvas. Nutzer:innen, die die Nachricht nicht erhalten haben, könnten zum Beispiel durch einen Filter gestoppt werden, der den Abschluss eines anderen Schritts in einem anderen Branch verlangt.
- Bestätigen Sie, dass Nutzer:innen zusätzliche Überprüfungsregeln erfüllen.
- Bestätigen Sie, dass der Canvas-Schritt zum Zeitpunkt des Sendens mit dem vorhergehenden Schritt verbunden war.

### Bestätigen Sie, dass Ihr Canvas korrekt gespeichert wird und alle Schritte gültig sind

Wenn Ihr Canvas nicht geladen wird und nicht vorankommt, kann dies daran liegen, dass eine frühere Version des Canvas nicht richtig gespeichert wurde und ungültige Schritte enthält. Sie können das Canvas vom Dashboard aus duplizieren. Wenn das Problem persistent ist, öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

## Fehlersuche

{% details Why are my users not receiving my Canvas messages? %}
**Verfügbarkeit der Nutzer:innen prüfen**
- Stellen Sie sicher, dass sie Ihre Segmentierungskriterien erfüllen.
- Bestätigen Sie, dass der Status Ihres Push-Abos "abonniert" oder "Opt-in" ist **und dass** der Status **"Push Enablement** " auf "wahr" gesetzt ist. Wenn Sie diese als Canvas-Entry-Regeln hinzugefügt haben, ist es möglich, dass die Nutzer:innen zwischen der Eingabe Ihres Canvas und dem Erhalt der Nachricht abgemeldet wurden.
- Bestätigen Sie, dass sie mit Ihren Canvas-Sendeeinstellungen übereinstimmen. (Wenn Nutzer:in "Abonnent:in" sind, die Einstellungen aber auf "Opt-in" stehen, werden Nutzer:in nicht für den Kanal freigeschaltet.)
- Wenn das globale Frequency-Capping für Ihr Canvas aktiviert ist, überprüfen Sie, ob Ihre Regeln die Anzahl der Nachrichten begrenzen, die jeder Nutzer:innen von einem bestimmten Kanal erhalten kann. 
- Wenn die Ruhezeiten aktiviert sind, kann die Sendezeit Ihrer Nachrichten beeinträchtigt werden, d.h. Ihre Nachricht wird möglicherweise zum nächsten verfügbaren Zeitpunkt (wenn die Ruhezeiten enden) gesendet oder ganz abgebrochen.

**Prüfen Sie die Verfügbarkeit von Nutzer:innen für zusätzliche Filter in Ihrem Canvas-Schritt**
- Bestätigen Sie, dass sie das erforderliche angepasste Event oder den Kauf durchgeführt haben.
- Prüfen Sie, ob es eine [Race-Condition]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/) gibt, die sich auf die Nachrichten auswirkt, die Nutzer:innen erhalten, wenn sie mehrere Aktionen gleichzeitig triggern.
- Vergewissern Sie sich, dass es in dem Schritt keine spezifischen Filter gibt, die Nutzer:innen am Empfang der Nachricht gehindert haben könnten.
- Suchen Sie nach Konflikten zwischen verschiedenen Schritten innerhalb desselben Canvas. Nutzer:innen, die die Nachricht nicht erhalten haben, könnten zum Beispiel durch einen Filter gestoppt werden, der den Abschluss eines anderen Schritts in einem anderen Branch verlangt.
- Bestätigen Sie, dass Nutzer:innen zusätzliche Überprüfungsregeln erfüllen.
- Bestätigen Sie, dass der Canvas-Schritt zum Zeitpunkt des Sendens mit dem vorhergehenden Schritt verbunden war.
{% enddetails %}

