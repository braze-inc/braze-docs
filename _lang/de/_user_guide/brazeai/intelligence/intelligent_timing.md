---
nav_title: Intelligentes Timing
article_title: Intelligentes Timing
page_order: 1.3
description: "Dieser Artikel gibt Ihnen einen Überblick über Intelligentes Timing (früher Intelligenter Versand) und wie Sie diese Funktion in Ihren Kampagnen und Canvases nutzen können."

---

# [![Braze Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"} Intelligentes Timing

> Verwenden Sie Intelligent Timing, um Ihre Nachricht zu dem Zeitpunkt zu versenden, zu dem Braze feststellt, dass der Nutzer sie am ehesten öffnen oder anklicken wird. Dies wird als optimaler Sendezeitpunkt bezeichnet. So können Sie leichter überprüfen, ob Sie Ihre Nutzer zu ihrer bevorzugten Zeit benachrichtigen, was zu einem höheren Engagement führen kann.

## Über Intelligentes Timing

Braze berechnet den optimalen Sendezeitpunkt auf der Grundlage einer statistischen Analyse der bisherigen Interaktionen Ihrer Benutzer mit Ihrer App und ihrer Interaktionen mit den einzelnen Messaging-Kanälen. Die folgenden Interaktionsdaten werden verwendet: 

- Zeiten der Sitzung
- Push Direct Öffnet
- Push Beeinflusst Öffnet
- E-Mail-Klicks
- Öffnungen von E-Mails (ohne [Öffnungen von Maschinen]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens))

So öffnet Sam vielleicht morgens regelmäßig Ihre E-Mails, aber abends öffnet sie Ihre App und interagiert mit Benachrichtigungen. Das bedeutet, dass Sam eine E-Mail-Kampagne mit intelligentem Timing am Morgen erhält, während sie Kampagnen mit Push-Benachrichtigungen am Abend erhält, wenn die Wahrscheinlichkeit größer ist, dass sie sich engagiert.

Wenn ein Nutzer:innen nicht über genügend Daten zum Engagement verfügt, damit Braze den optimalen Sendezeitpunkt berechnen kann, können Sie einen Ausweichzeitpunkt festlegen.

## Anwendungsfälle

- Senden Sie wiederkehrende Kampagnen, die nicht zeitkritisch sind
- Automatisieren Sie Kampagnen mit Benutzern aus verschiedenen Zeitzonen
- Wenn Sie Ihre am stärksten engagierten Benutzer anschreiben (sie haben die meisten Engagement-Daten)

## Intelligentes Timing verwenden

In diesem Abschnitt wird beschrieben, wie Sie das intelligente Timing für Ihre Kampagnen und Canvase konfigurieren.

{% tabs local %}
{% tab Campaign %}
### Schritt 1: Intelligentes Timing hinzufügen

1. Erstellen Sie eine Kampagne und verfassen Sie Ihre Nachricht.
2. Wählen Sie die **geplante Zustellung** als Zustellungsart aus.
3. Wählen Sie unter **Zeitbasierte Planungsoptionen** die Option **Intelligentes Timing**.
4. Legen Sie die Häufigkeit der Eingänge fest. Für einmalige Sendungen wählen Sie **Einmalig** und wählen Sie ein Sendedatum aus. Für wiederkehrende Sendungen wählen Sie **Täglich**, **Wöchentlich** oder **Monatlich** und konfigurieren die Wiederholungsoptionen. Siehe [Einschränkungen](#limitations) für weitere Hinweise.
5. Optional können Sie [Ruhezeiten](#quiet-hours) konfigurieren.
6. Geben Sie eine [Ausweichzeit](#campaign-fallback) an. Dies ist der Zeitpunkt, zu dem die Nachricht gesendet wird, wenn das Profil eines Benutzers nicht genügend Daten enthält, um eine optimale Zeit zu berechnen.

![Bildschirm zur Planung von Kampagnen mit intelligentem Timing mit Fallback-Zeit und Ruhezeiten]({% image_buster /assets/img/intelligent_timing/campaign_scheduling.png %})

#### Ruhezeiten {#quiet-hours}

Verwenden Sie Ruhezeiten, um das Senden von Nachrichten während bestimmter Stunden zu verhindern. Dies ist hilfreich, wenn Sie vermeiden möchten, Nachrichten in den frühen Morgenstunden oder über Nacht zu versenden, und gleichzeitig zulassen, dass Intelligent Timing das beste Zeitfenster für die Zustellung bestimmt.

{% alert note %}
Ruhezeiten hat die Einstellung **Nur innerhalb bestimmter Stunden senden** ersetzt. Anstatt zu wählen, wann Nachrichten gesendet werden können, wählen Sie jetzt, wann sie nicht gesendet werden sollen. Wenn Sie z.B. Nachrichten zwischen 16 und 18 Uhr senden möchten, stellen Sie Ruhezeiten von 18 bis 16 Uhr am nächsten Tag ein.
{% endalert %}

1. Wählen Sie **Enablement Ruhezeiten**.
2. Wählen Sie die Start- und Endzeit, zu der **keine** Nachrichten gesendet werden sollen.

![Ruhezeiten umschalten mit eingestellter Start- und Endzeit, um die Zustellung von Nachrichten über Nacht zu blockieren]({% image_buster /assets/img/intelligent_timing/quiet_hours.png %})

Wenn die Ruhezeiten aktiviert sind, sendet Braze während der Ruhezeiten keine Nachrichten - selbst wenn diese Zeit mit der optimalen Sendezeit eines Nutzers:innen übereinstimmt. Wenn die optimale Zeit eines Nutzers:innen in das Ruhefenster fällt, wird die Nachricht stattdessen am nächstgelegenen Rand des Fensters gesendet.

Wenn zum Beispiel die Ruhezeiten von 22:00 Uhr bis 6:00 Uhr morgens eingestellt sind und die optimale Zeit für einen Nutzer:innen 5:30 Uhr ist, hält Braze die Nachricht zurück und stellt sie um 6:00 Uhr morgens zu - die nächstgelegene Zeit außerhalb des Ruhezeitfensters.

#### Vorschau der Lieferzeiten

Um eine Schätzung zu erhalten, wie viele Nutzer die Nachricht in jeder Stunde des Tages erhalten werden, verwenden Sie das Vorschaudiagramm (nur Kampagnen).

1. Fügen Sie im Schritt Zielgruppen Segmente oder Filter hinzu.
2. Wählen Sie im Abschnitt **Vorschau der Zustellungszeiten für** (der sowohl in den Schritten Zielgruppen als auch Zeitplan der Zustellung erscheint) Ihren Kanal aus.
3. Klicken Sie auf **Daten aktualisieren**.

![Zustellungsvorschau-Chart für Android Push zeigt die Zeit des größten Engagements zwischen 12 und 14 Uhr, wobei 14 Uhr die beliebteste App-Zeit ist.]({% image_buster /assets/img/intel-timing-preview.png %})

### Schritt 2: Wählen Sie ein Sendedatum

Wählen Sie dann ein Sendedatum für Ihre Kampagne aus. Beachten Sie Folgendes, wenn Sie Kampagnen mit Intelligent Timing planen:

#### Kampagne 48 Stunden im Voraus einführen

Starten Sie Ihre Kampagne mindestens 48 Stunden vor dem geplanten Versanddatum. Das liegt an den unterschiedlichen Zeitzonen. Braze berechnet die optimale Zeit um Mitternacht in Samoa-Zeit (UTC+13), eine der ersten Zeitzonen der Welt. Ein einziger Tag umfasst weltweit etwa 48 Stunden. Wenn Sie also eine Kampagne innerhalb dieses 48-Stunden-Puffers starten, ist es möglich, dass die optimale Zeit eines Nutzers in seiner Zeitzone bereits verstrichen ist und die Nachricht nicht gesendet wird.

{% alert important %}
Wenn eine Kampagne gestartet wird und die optimale Zeit eines Nutzers weniger als eine Stunde in der Vergangenheit liegt, wird die Nachricht sofort verschickt. Liegt die optimale Zeit mehr als eine Stunde zurück, wird die Nachricht gar nicht gesendet.
{% endalert %}

#### 3-Tage-Fenster für Segmente-Filter

Wenn Sie eine Zielgruppe zusammenstellen, die in einem bestimmten Zeitraum eine Aktion durchgeführt hat, sollten Sie in Ihren Segmentfiltern ein Zeitfenster von mindestens 3 Tagen vorsehen. Verwenden Sie zum Beispiel statt `First used app more than 1 day ago` und `First used app less than 3 days ago` 1 Tag und 4 Tage.

![Filter für die Zielgruppe, bei der die Kampagne auf Nutzer:innen abzielt, die die App vor 1 bis 4 Tagen zum ersten Mal genutzt haben.]({% image_buster /assets/img/intelligent_timing/first_used_app.png %})

Dies liegt auch an den Zeitzonen - die Auswahl eines Zeitraums von weniger als 3 Tagen kann dazu führen, dass einige Nutzer aus dem Segment herausfallen, bevor ihre optimale Sendezeit erreicht ist.

Weitere Informationen finden Sie unter [FAQ: Intelligentes Timing](#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

#### Zeitplan für gewinnende Varianten 2 Tage nach dem A/B-Test

Wenn Sie [A/B-Tests mit einer Optimierung]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) nutzen, z. B. die automatische Versendung der **Gewinner-Variante** oder die Verwendung einer **personalisierten Variante**, kann das intelligente Timing die Dauer und das Timing Ihrer Kampagne beeinflussen.

Wenn Sie intelligentes Timing verwenden, empfehlen wir, den Zeitplan für den Versand der Gewinner-Variante mindestens **2 Tage nach** Beginn des A/B-Tests festzulegen. Wenn Ihr A/B-Test beispielsweise am 16\. April um 16:00 Uhr beginnt, planen Sie den Versand der Gewinner-Variante frühestens für den 18\. April um 16:00 Uhr. So hat Braze genügend Zeit, das Verhalten der Nutzer:innen zu bewerten und Nachrichten zum optimalen Zeitpunkt zu versenden.

A/B-Tests zeigen A/B-Tests mit ausgewählter Gewinnvariante, mit ausgewählten Gewinnkriterien, Sendedatum und Ortszeit.]({% image_buster /assets/img/intelligent_timing/ab_testing_intelligent_timing.png %})

### Schritt 3: Wählen Sie ein Zeitfenster für die Zustellung (optional)

Optional können Sie das Zeitfenster für die Zustellung begrenzen. Dies kann nützlich sein, wenn sich Ihre Kampagne auf ein bestimmtes Ereignis, einen Verkauf oder eine Aktion bezieht, wird aber im Allgemeinen nicht empfohlen, wenn Sie Intelligent Timing verwenden. Weitere Informationen finden Sie unter [Einschränkungen](#limitations).

Wenn Sie dies angeben, verwendet Braze nur Daten über das Engagement innerhalb dieses Zeitfensters, um die optimale Zustellung für einen Nutzer:innen zu bestimmen. Wenn innerhalb dieses Zeitfensters nicht genügend Daten zum Engagement vorhanden sind, wird die Nachricht zu der von Ihnen festgelegten Fallback-Zeit gesendet.

So legen Sie ein Zeitfenster für die Zustellung fest:

1. Wählen Sie bei der Konfiguration von Intelligent Timing die Option **Nur Nachrichten innerhalb bestimmter Stunden senden**.
2. Geben Sie die Start- und Endzeit des Lieferfensters ein.

![Kontrollkästchen für "Nachrichten nur innerhalb bestimmter Stunden senden" ausgewählt, wobei das Zeitfenster auf 8 Uhr bis 12 Uhr in der Ortszeit des Nutzers:innen festgelegt ist.]({% image_buster /assets/img/intelligent_timing_hours.png %})

### Schritt 4: Wählen Sie eine Fallback-Zeit {#campaign-fallback}

Wählen Sie einen Fallback-Zeitpunkt, der verwendet werden soll, wenn das Profil eines Nutzers:innen nicht genügend Daten für die Berechnung eines optimalen Zustellungszeitpunkts enthält.

![Zeitplan für eine Kampagne mit intelligentem Timing]({% image_buster /assets/img/intelligent_timing_1.png %})

{% multi_lang_include brazeai/intelligent_suite/fallback_time.md type="campaign" %}

### Schritt 5: Vorschau der Lieferzeiten

Um eine Schätzung zu erhalten, wie viele Nutzer:innen die Nachricht in jeder Stunde des Tages erhalten werden, verwenden Sie die Vorschau im Chart.

1. Fügen Sie im Schritt Zielgruppen Segmente oder Filter hinzu.
2. Wählen Sie im Abschnitt **Vorschau der Zustellungszeiten für** (der sowohl in den Schritten Zielgruppen als auch Zeitplan der Zustellung erscheint) Ihren Kanal aus.
3. Wählen Sie **Daten aktualisieren**.

![Beispiel Vorschau der Zustellungszeiten für Android Push.]({% image_buster /assets/img/intel-timing-preview.png %})

Wann immer Sie die Einstellungen für Intelligent Timing oder die Zielgruppe Ihrer Kampagne ändern, aktualisieren Sie die Daten erneut, um ein aktualisiertes Diagramm anzuzeigen.

Das Diagramm zeigt Benutzer, die genügend Daten hatten, um eine optimale Zeit zu berechnen, in blau und Benutzer, die die Ausweichzeit nutzen werden, in rot. Verwenden Sie die Berechnungsfilter, um die Vorschau für einen detaillierteren Blick auf die einzelnen Nutzer:innen anzupassen.
{% endtab %}

{% tab Canvas %}

### Schritt 1: Intelligentes Timing hinzufügen

Fügen Sie in Ihrem Canvas einen [Nachrichten-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) hinzu, gehen Sie dann zu **Zustellungseinstellungen** und wählen Sie **Intelligentes Timing verwenden**.

Nachrichten werden an Nutzer:innen gesendet, die den Schritt an diesem Tag zu ihrer optimalen Ortszeit eingegeben haben. Wenn ihre optimale Zeit an diesem Tag jedoch bereits verstrichen ist, wird sie stattdessen am nächsten Tag zu dieser Zeit zugestellt. Nachrichtenschritte, die auf mehrere Kanäle abzielen, können Nachrichten zu verschiedenen Zeiten für verschiedene Kanäle senden oder versuchen, sie zu senden. Wenn die erste Nachricht in einem Nachrichtenschritt zu senden versucht wird, werden alle Nutzer:innen automatisch vorangebracht.

### Schritt 2: Wählen Sie eine Fallback-Zeit

Wählen Sie eine Fallback-Zeit für die Nachricht, die an Nutzer:innen Ihrer Zielgruppe gesendet werden soll, die nicht über genügend Daten zum Engagement verfügen, damit Braze eine optimale Sendezeit berechnen kann. {% multi_lang_include brazeai/intelligent_suite/fallback_time.md %}

### Schritt 4: Verzögerungsschritt hinzufügen

Anders als bei Kampagnen müssen Sie Ihr Canvas nicht 48 Stunden vor dem Versanddatum einführen, da das intelligente Timing auf der Ebene der Schritte und nicht auf der Ebene des Canvas eingestellt wird.

Fügen Sie stattdessen einen [Verzögerungsschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) von mindestens zwei Kalendertagen zwischen der Eingabe des Nutzers:innen in den Canvas und dem Erhalt des Intelligentes Timing-Schrittes hinzu.

#### Kalender vs. 24-Stunden-Tage

Wenn Sie Intelligentes Timing nach einem Verzögerungsschritt verwenden, kann das Zustellungsdatum variieren, je nachdem, wie Sie Ihre Verzögerung berechnen. Dies gilt nur, wenn Ihre Verzögerung auf **Nach einer Dauer** eingestellt ist, da es einen Unterschied zwischen der Berechnung von "Tagen" und "Kalendertagen" gibt.

- **Tage:** 1 Tag sind 24 Stunden, gerechnet ab dem Zeitpunkt, an dem die:der Nutzer:in den Schritt Verzögerung eingibt.
- **Kalendertage:** 1 Tag ist der Zeitraum von der Eingabe des Schritts Verzögerung durch die:den Nutzer:in bis Mitternacht in seiner Zeitzone. Das bedeutet, dass 1 Kalendertag nur wenige Minuten lang sein kann.

Wenn Sie Intelligentes Timing verwenden, empfehlen wir Ihnen, für Ihre Verspätungen Kalendertage anstelle von 24-Stunden-Tagen zu verwenden. Denn bei Kalendertagen wird die Nachricht am letzten Tag der Verzögerung zum optimalen Zeitpunkt versendet. Bei einem 24-Stunden-Tag besteht die Möglichkeit, dass die optimale Zeit der Nutzerin oder des Nutzers vor der Eingabe des Schritts liegt, was bedeutet, dass ein zusätzlicher Tag zu seiner Verzögerung hinzukommt.

Nehmen wir zum Beispiel an, Lukas optimale Zeit ist 14:00 Uhr. Er betritt den Schritt Verzögerung um 14:01 Uhr am 1\. März und die Verzögerung ist auf 2 Tage eingestellt.

- Tag 1 endet am 2\. März um 2:01 Uhr
- Tag 2 endet am 3\. März um 2:01 Uhr

Intelligent Timing soll jedoch um 14 Uhr liefern, was bereits geschehen ist. Luka wird die Nachricht also erst am nächsten Tag erhalten: 4\. März um 14:00 Uhr.

![Grafik, die den Unterschied zwischen Tagen und Kalendertagen veranschaulicht, wenn die optimale Zeit eines Nutzers:innen 14:00 Uhr ist, er aber den Verzögerungsschritt um 14:01 Uhr eingibt und die Verzögerung auf 2 Tage eingestellt ist. Tage stellt die Nachricht 3 Tage später zu, weil der Nutzer:innen den Schritt nach seiner optimalen Zeit eingegeben hat, während Kalender:innen die Nachricht 2 Tage später, am letzten Tag der Verzögerung, zustellt.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}
{% endtab %}
{% endtabs %}

## Beschränkungen

- In-App-Nachrichten, Content Cards und Webhooks werden sofort zugestellt und nicht mit optimalen Zeiten versehen.
- Intelligentes Timing ist nicht verfügbar für aktionsbasierte oder API-ausgelöste Kampagnen.
- Intelligent Timing sollte in den folgenden Szenarien nicht verwendet werden:
    - **Rate-Limiting:** Wenn sowohl die Ratenbegrenzung als auch Intelligent Timing verwendet werden, gibt es keine Garantie dafür, wann die Nachricht zugestellt wird. Täglich wiederkehrende Kampagnen mit intelligentem Timing unterstützen keine genaue Obergrenze für den Versand von Nachrichten.
    - **IP-Warming-Kampagnen:** Einige der Intelligentes-Timing-Verhaltensweisen können dazu führen, dass Sie die täglichen Volumina, die beim ersten Aufwärmen Ihrer IP benötigt werden, nicht erreichen. Das liegt daran, dass Intelligent Timing die Segmente zweimal auswertet - einmal bei der Erstellung der Kampagne oder des Canvas und ein zweites Mal vor dem Versand an die Benutzer, um zu überprüfen, ob sie noch in diesem Segment sein sollten. Dies kann dazu führen, dass sich die Segmente verschieben und verändern, was oft dazu führt, dass einige Nutzer:innen bei der zweiten Auswertung aus dem Segment herausfallen. Diese Nutzer:innen werden nicht ersetzt, was sich darauf auswirkt, wie nah Sie an die maximale Nutzerobergrenze herankommen können.

## Fehlersuche

### Vorschaudiagramm mit wenigen Benutzern mit optimalen Zeiten

Braze benötigt eine gewisse Menge an Daten über das Engagement, um eine gute Schätzung vornehmen zu können. Wenn nicht genügend Sitzungsdaten vorhanden sind oder die anvisierten Benutzer nur wenige oder gar keine Klicks oder Öffnungen aufweisen (z. B. neue Benutzer), wird Braze standardmäßig die Ausweichzeit verwenden. Je nach Ihrer Konfiguration kann dies entweder die beliebteste App-Zeit oder eine benutzerdefinierte Ausweichzeit sein.

### Einfluss der Zeitzone auf die Zustellung von Intelligent Timing

Intelligentes Timing basiert auf der angegebenen Ortszeit jedes Nutzers, so dass das geplante Datum und die Uhrzeit der Zustellung bei den einzelnen Nutzer:innen variieren können.

Wenn Nutzer:innen Nachrichten nicht wie erwartet erhalten, überprüfen Sie, ob das Zeitzonenfeld in ihrem Profil korrekt ausgefüllt ist. Wenn das Feld für die Zeitzone leer ist, erhält der Nutzer:innen möglicherweise Nachrichten, die sich an der Zeitzone des Unternehmens und nicht an seiner Ortszeit orientieren.

### Versenden nach dem Zeitplan

Ihre Kampagne mit intelligentem Timing sendet möglicherweise über das geplante Datum hinaus, wenn Sie [A/B-Tests mit einer Optimierung]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) nutzen. Kampagnen, die A/B-Testing-Optimierungen verwenden, können automatisch die Gewinner-Variante senden, nachdem der erste Test abgeschlossen ist, wodurch sich die Dauer der Kampagne verlängert. Standardmäßig wird bei Kampagnen mit einer Optimierung die Gewinner-Variante am Tag nach dem ersten Test an die verbleibenden Benutzer gesendet, aber Sie können dieses Sendedatum ändern.

Wenn Sie Intelligent Timing verwenden, empfehlen wir Ihnen, mehr Zeit für den Abschluss des A/B-Tests einzuplanen und den Versand der Gewinnervariante für 2 Tage nach dem ersten Test zu planen, anstatt für 1 Tag.

## Häufig gestellte Fragen (FAQ) {#faq}

### Allgemein

#### Was sagt Intelligentes Timing voraus?

Intelligentes Timing konzentriert sich auf die Prognose, wann ein Nutzer Ihre Nachrichten am ehesten öffnet oder klickt, um sicherzustellen, dass Ihre Nachrichten die Nutzer:innen zum optimalen Zeitpunkt erreichen.

#### Wird das intelligente Timing für jeden Wochentag separat berechnet?

Nein, Intelligentes Timing ist nicht an bestimmte Tage gebunden. Stattdessen personalisiert es die Sendezeiten auf der Grundlage des eindeutigen Engagements jedes Nutzers und des von Ihnen verwendeten Kanals, wie E-Mail oder Push-Benachrichtigungen. So können Sie sicherstellen, dass Ihre Nachrichten die Nutzer:innen dann erreichen, wenn sie am empfänglichsten sind.

### Berechnungen

#### Welche Daten werden verwendet, um die optimale Zeit für jeden Nutzer:innen zu berechnen?

Um die optimale Zeit zu berechnen, verwenden Sie Intelligentes Timing:

1. Analysiert die Interaktionsdaten für jeden Nutzer:innen, die vom Braze SDK aufgezeichnet wurden. Dies beinhaltet:
  - Zeiten der Sitzung
  - Push direkt öffnet
  - Push beeinflusst Öffnungen
  - E-Mail Klicks
  - Öffnungen von E-Mails (ohne Öffnungen durch den Computer)
2. Gruppiert diese Ereignisse nach Zeit und identifiziert die optimale Sendezeit für jeden Nutzer:innen.

#### Werden die Öffnungen der Maschinen bei der Berechnung der optimalen Zeit berücksichtigt?

Nein, [Öffnungen der Maschine]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens) sind von den Berechnungen für die optimale Zeit ausgeschlossen. Das bedeutet, dass die Sendezeiten ausschließlich auf dem echten Engagement der Nutzer:innen beruhen, was eine genauere Zeitplanung für Ihre Kampagnen ermöglicht.

#### Wie genau ist der optimale Zeitpunkt?

Intelligentes Timing plant Nachrichten während der "engagiertesten Stunde" jedes Nutzers, basierend auf dem Beginn der Sitzung und der Öffnung von Nachrichten. Innerhalb dieser Stunde wird der Zeitpunkt der Nachrichten auf die nächsten fünf Minuten gerundet. Wenn beispielsweise die optimale Zeit eines Nutzers:innen mit 16:58 Uhr berechnet wird, wird die Nachricht für 17:00 Uhr geplant. Es kann zu leichten Verzögerungen bei der Zustellung kommen, da das System in Stoßzeiten aktiv ist.

#### Wie sehen die Fallback-Berechnungen aus, wenn nicht genügend Daten vorhanden sind?

Wenn es weniger als fünf relevante Ereignisse für einen Nutzer:innen gibt, verwendet Intelligentes Timing die Ausweichzeit in Ihren Nachrichteneinstellungen. 

### Kampagnen

#### Wie weit im Voraus sollte ich eine Intelligent Timing Kampagne starten, um sie erfolgreich an alle Nutzer:innen in allen Zeitzonen zu bringen?

Braze berechnet die optimale Zeit um Mitternacht in Samoa-Zeit, eine der ersten Zeitzonen der Welt. An einem einzigen Tag erstreckt er sich über etwa 48 Stunden. Zum Beispiel hat jemand, dessen optimale Zeit 12:01 Uhr ist und der in Australien lebt, seine optimale Zeit bereits überschritten, und es ist "zu spät", um ihm zu senden. Aus diesen Gründen müssen Sie einen Zeitplan von 48 Stunden vorbringen, um Ihre App erfolgreich an alle Nutzer weltweit zuzustellen.

#### Warum werden in meiner Intelligent Timing-Kampagne nur wenige oder gar keine Sendungen angezeigt?

Braze benötigt eine ausreichende Anzahl von Datenpunkten, um eine gute Schätzung vornehmen zu können. Wenn die Sitzungsdaten nicht ausreichen oder die anvisierten Benutzer nur wenige oder gar keine E-Mail-Klicks oder -Öffnungen aufweisen (z. B. neue Benutzer), kann Intelligent Timing die beliebteste Stunde des Arbeitsbereichs an diesem Wochentag als Standard festlegen. Wenn es nicht genügend Informationen über den Workspace gibt, greifen wir auf die Standardzeit von 17 Uhr zurück. Sie können auch eine bestimmte Fallback-Zeit festlegen.

#### Warum wird meine Intelligent Timing-Kampagne nach dem geplanten Datum gesendet?

Ihre Kampagne mit intelligentem Timing versendet möglicherweise über das geplante Datum hinaus, weil Sie A/B-Tests nutzen. Kampagnen, die A/B-Tests verwenden, können die Gewinner-Variante automatisch versenden, nachdem der A/B-Test beendet ist, wodurch sich die Dauer des Kampagnenversands verlängert. Standardmäßig werden Intelligent Timing-Kampagnen so geplant, dass die Gewinner-Variante am nächsten Tag an die verbleibenden Nutzer versendet wird, aber Sie können dieses Versanddatum ändern.

Wir empfehlen Ihnen, bei intelligenten Timing-Kampagnen mehr Zeit für den Abschluss des A/B-Tests einzuplanen und die Gewinnervariante für zwei Tage statt für einen Tag zu versenden. 

### Funktionsweise

#### Wann prüft Braze die Zulassungskriterien für Segmente und Zielgruppenfilter?

Braze führt zwei Prüfungen durch, wenn eine Kampagne gestartet wird:

1. **Erste Überprüfung:** Um Mitternacht in der ersten Zeitzone am Tag des Versands.
2. **Prüfung des Zeitplans:** Kurz vor dem Senden zu der für den Nutzer:innen ausgewählten Zeit Intelligent Timing.

Seien Sie vorsichtig, wenn Sie auf der Grundlage anderer Kampagnensendungen filtern, um das Targeting von nicht geeigneten Segmenten zu vermeiden. Wenn Sie z.B. zwei Kampagnen am selben Tag zu unterschiedlichen Zeiten versenden und einen Filter hinzufügen, der es Nutzern:innen nur erlaubt, die zweite Kampagne zu erhalten, wenn sie die erste erhalten haben, werden die Nutzer:innen die zweite Kampagne nicht erhalten. Das liegt daran, dass niemand berechtigt war, als die Kampagne ins Leben gerufen und die Segmente gebildet wurden.

#### Kann ich Ruhezeiten in meiner Intelligent Timing-Kampagne verwenden?

Ruhezeiten können in einer Kampagne verwendet werden, die Intelligentes Timing einsetzt. Der Algorithmus des intelligenten Timings vermeidet Ruhezeiten, so dass die Nachricht trotzdem an alle in Frage kommenden Nutzer:innen gesendet wird. Wir empfehlen jedoch, die Ruhezeiten zu deaktivieren, es sei denn, es gibt Richtlinien, Compliance- oder andere rechtliche Gründe dafür, wann Nachrichten gesendet werden können und wann nicht.

#### Was passiert, wenn die optimale Zeit für einen Nutzer:innen innerhalb der Ruhezeiten liegt? 

Wenn die ermittelte optimale Zeit in die Ruhezeiten fällt, findet Braze den nächstgelegenen Rand der Ruhezeiten und plant die Nachricht für die nächste zulässige Stunde vor oder nach den Ruhezeiten. Die Nachricht wird in die Warteschlange gestellt, um an der nächstgelegenen Grenze der Ruhezeiten in Bezug auf die optimale Zeit gesendet zu werden.

#### Kann ich Intelligent Timing und Ratenbegrenzung verwenden?

Rate-Limiting kann bei einer Kampagne verwendet werden, die Intelligent Timing einsetzt. Rate-Limiting bedeutet jedoch, dass einige Nutzer:innen ihre Nachrichten zu einem suboptimalen Zeitpunkt erhalten, insbesondere wenn eine große Anzahl von Nutzer:innen im Verhältnis zur Rate-Limiting-Größe aufgrund unzureichender Daten auf den Zeitplan für den Fallback-Zeitpunkt gesetzt wird. 

Wir empfehlen die Verwendung von Rate-Limits bei einer Intelligent Timing Kampagne nur dann, wenn es technische Anforderungen gibt, die mit Rate-Limits erfüllt werden müssen.

#### Kann ich Intelligent Timing während der IP-Erwärmung verwenden?

Braze rät davon ab, Intelligent Timing zu verwenden, wenn Nutzer:innen zum ersten Mal IP-Warming betreiben, da einige seiner Verhaltensweisen zu Schwierigkeiten beim Erreichen des täglichen Volumens führen können. Das liegt daran, dass Intelligent Timing die Kampagnensegmente doppelt auswertet. Einmal bei der Erstellung der Kampagne und ein zweites Mal vor dem Versand an die Nutzer, um zu überprüfen, ob sie noch in diesem Segment sein sollten.

Dies kann dazu führen, dass sich die Segmente verschieben und verändern, was oft dazu führt, dass einige Nutzer:innen bei der zweiten Auswertung aus dem Segment herausfallen. Diese Nutzer:innen werden nicht ersetzt, was sich darauf auswirkt, wie nah Sie an die maximale Nutzer:innen-Obergrenze herankommen können.

#### Wie wird die Zeit der beliebtesten App ermittelt?

Die beliebteste App-Zeit wird durch die durchschnittliche Sitzungsstartzeit für den Workspace (in Ortszeit) bestimmt. Diese Metrik finden Sie im Dashboard bei der Vorschau der Zeiten für eine Kampagne, die in Rot angezeigt wird.

#### Berücksichtigt Intelligentes Timing die Öffnungen maschinelle Öffnungen?

Ja, maschinelle Öffnungen werden von Intelligent Timing herausgefiltert, so dass sie die Ausgabe nicht beeinflussen.

#### Wie kann ich sicherstellen, dass Intelligent Timing so gut wie möglich funktioniert?

Intelligentes Timing verwendet den individuellen Verlauf des Engagements jedes Nutzers:innen bei Nachrichten, unabhängig davon, zu welchen Zeiten sie diese erhalten haben. Bevor Sie intelligentes Timing verwenden, vergewissern Sie sich, dass Sie den Nutzer:innen Nachrichten zu verschiedenen Tageszeiten geschickt haben. Auf diese Weise können Sie "ausprobieren", wann der beste Zeitpunkt für die einzelnen Nutzer:innen ist. Eine unzureichende Auswahl verschiedener Tageszeiten kann dazu führen, dass Intelligent Timing eine suboptimale Sendezeit für eine:n Nutzer:in auswählt.



