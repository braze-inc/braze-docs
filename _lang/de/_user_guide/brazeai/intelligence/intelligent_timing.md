---
nav_title: Intelligentes Timing
article_title: Intelligentes Timing
page_order: 2
description: "Dieser Artikel gibt Ihnen einen Überblick über Intelligentes Timing (früher Intelligenter Versand) und wie Sie diese Funktion in Ihren Kampagnen und Canvases nutzen können."

---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligentes Timing

> Verwenden Sie Intelligent Timing, um Ihre Nachricht zu dem Zeitpunkt zu versenden, zu dem Braze feststellt, dass der Nutzer sie am ehesten öffnen oder anklicken wird. Dies wird als optimaler Sendezeitpunkt bezeichnet. So können Sie leichter überprüfen, ob Sie Ihre Nutzer zu ihrer bevorzugten Zeit benachrichtigen, was zu einem höheren Engagement führen kann.

## Anwendungsfälle

- Senden Sie wiederkehrende Kampagnen, die nicht zeitkritisch sind
- Automatisieren Sie Kampagnen mit Benutzern aus verschiedenen Zeitzonen
- Wenn Sie Ihre am stärksten engagierten Benutzer anschreiben (sie haben die meisten Engagement-Daten)

## Funktionsweise

Braze berechnet den optimalen Sendezeitpunkt auf der Grundlage einer statistischen Analyse der bisherigen Interaktionen Ihrer Benutzer mit Ihrer App und ihrer Interaktionen mit den einzelnen Messaging-Kanälen. Die folgenden Interaktionsdaten werden verwendet: 

- Zeiten der Sitzung
- Push Direct Öffnet
- Push Beeinflusst Öffnet
- E-Mail-Klicks
- Öffnungen von E-Mails (ohne [Öffnungen von Maschinen]({{site.baseurl}}/user_guide/data/report_metrics#machine-opens))

So öffnet Sam vielleicht morgens regelmäßig Ihre E-Mails, aber abends öffnet sie Ihre App und interagiert mit Benachrichtigungen. Das bedeutet, dass Sam eine E-Mail-Kampagne mit intelligentem Timing am Morgen erhält, während sie Kampagnen mit Push-Benachrichtigungen am Abend erhält, wenn die Wahrscheinlichkeit größer ist, dass sie sich engagiert.

Wenn ein Benutzer nicht über genügend Engagementdaten verfügt, damit Braze den optimalen Sendezeitpunkt berechnen kann, können Sie einen [Ausweichzeitpunkt](#fallback-time) festlegen.

## Intelligentes Timing verwenden

In diesem Abschnitt wird beschrieben, wie Sie das intelligente Timing für Ihre Kampagnen und Canvase konfigurieren.

### Kampagnen

So verwenden Sie Intelligentes Timing in Ihren Kampagnen:

1. Erstellen Sie eine Kampagne und verfassen Sie Ihre Nachricht.
2. Wählen Sie als Zustellungsart **"Geplante Zustellung** ".
3. Wählen Sie unter **Zeitbasierte Planungsoptionen** die Option **Intelligentes Timing**.
4. Wählen Sie das Sendedatum aus. Siehe [Kampagnennuancen](#campaign-nuances) für Überlegungen.
5. Legen Sie fest, ob Sie [Nachrichten nur innerhalb bestimmter Stunden versenden](#sending-within-specific-hours) möchten.
6. Geben Sie eine [Ausweichzeit](#fallback-time) an. Dies ist der Zeitpunkt, zu dem die Nachricht gesendet wird, wenn das Profil eines Benutzers nicht genügend Daten enthält, um eine optimale Zeit zu berechnen.

![Zeitplan für eine Kampagne mit intelligentem Timing][1]

#### Versenden von Nachrichten innerhalb bestimmter Stunden {#sending-within-specific-hours}

Falls gewünscht, können Sie die optimale Zeit auf ein bestimmtes Zeitfenster begrenzen. Dies ist nützlich, wenn sich Ihre Kampagne auf ein bestimmtes Ereignis, einen Verkauf oder eine Werbeaktion bezieht, wird aber ansonsten im Allgemeinen nicht empfohlen. Das Senden innerhalb bestimmter Stunden funktioniert ähnlich wie die Ruhezeiten, die bei Intelligentem Timing nicht empfohlen werden, da sie kontraproduktiv sind. Weitere Informationen finden Sie im Abschnitt über [Einschränkungen](#limitations) in diesem Artikel.

1. Wählen Sie bei der Konfiguration von Intelligent Timing die Option **Nur Nachrichten innerhalb bestimmter Stunden senden**.
2. Geben Sie die Start- und Endzeit des Lieferfensters ein.

![Kontrollkästchen für "Nachrichten nur innerhalb bestimmter Stunden senden" ausgewählt, wobei das Zeitfenster auf 8 bis 12 Uhr in der Ortszeit der Nutzerin oder des Nutzers festgelegt ist.][4]

Wenn ein Zeitfenster für die Zustellung angegeben wird, berücksichtigt Braze nur die Daten zum Engagement innerhalb dieses Zeitfensters, um den optimalen Zeitpunkt für einen Benutzer zu ermitteln. Wenn innerhalb dieses Zeitfensters nicht genügend Engagement-Daten vorhanden sind, wird die Nachricht zum angegebenen [Ausweichzeitpunkt](#fallback-time) gesendet.

#### Vorschau der Lieferzeiten

Um eine Schätzung zu erhalten, wie viele Nutzer die Nachricht in jeder Stunde des Tages erhalten werden, verwenden Sie das Vorschaudiagramm (nur Kampagnen).

1. Fügen Sie im Schritt Zielgruppen Segmente oder Filter hinzu.
2. Wählen Sie im Abschnitt **Vorschau der Zustellungszeiten für** (der sowohl in den Schritten Zielgruppen als auch Zeitplan der Zustellung erscheint) Ihren Kanal aus.
3. Klicken Sie auf **Daten aktualisieren**.

![][2]

Wann immer Sie die Einstellungen für Intelligent Timing oder die Zielgruppe Ihrer Kampagne ändern, aktualisieren Sie die Daten erneut, um ein aktualisiertes Diagramm anzuzeigen.

Das Diagramm zeigt Benutzer, die genügend Daten hatten, um eine optimale Zeit zu berechnen, in blau und Benutzer, die die Ausweichzeit nutzen werden, in rot. Verwenden Sie die Berechnungsfilter, um die Vorschau für einen detaillierteren Blick auf die einzelnen Nutzer:innen anzupassen.

#### Nuancen der Kampagne

Hier finden Sie einige Nuancen, die Sie bei der Planung von Kampagnen mit intelligentem Timing beachten sollten.

##### Die Kampagne starten

Starten Sie Ihre Kampagne mindestens 48 Stunden vor dem geplanten Versanddatum. Das liegt an den unterschiedlichen Zeitzonen. Braze berechnet die optimale Zeit um Mitternacht in Samoa-Zeit (UTC+13), eine der ersten Zeitzonen der Welt. Ein einziger Tag umfasst weltweit etwa 48 Stunden. Wenn Sie also eine Kampagne innerhalb dieses 48-Stunden-Puffers starten, ist es möglich, dass die optimale Zeit eines Nutzers in seiner Zeitzone bereits verstrichen ist und die Nachricht nicht gesendet wird.

{% alert important %}
Wenn eine Kampagne gestartet wird und die optimale Zeit eines Nutzers weniger als eine Stunde in der Vergangenheit liegt, wird die Nachricht sofort verschickt. Liegt die optimale Zeit mehr als eine Stunde zurück, wird die Nachricht gar nicht gesendet.
{% endalert %}

##### Segmente auswählen

Wenn Sie eine Zielgruppe zusammenstellen, die in einem bestimmten Zeitraum eine Aktion durchgeführt hat, sollten Sie in Ihren Segmentfiltern ein Zeitfenster von mindestens 3 Tagen vorsehen. Verwenden Sie zum Beispiel statt `First used these apps more than 1 day ago` und `First used these apps less than 3 days ago` 1 Tag und 4 Tage.

![Filter für die Zielgruppe, wobei die Kampagne auf Nutzer abzielt, die diese Apps vor 1 bis 4 Tagen zum ersten Mal verwendet haben.][3]

Dies liegt auch an den Zeitzonen - die Auswahl eines Zeitraums von weniger als 3 Tagen kann dazu führen, dass einige Nutzer aus dem Segment herausfallen, bevor ihre optimale Sendezeit erreicht ist.

Erfahren Sie mehr darüber, [wann Braze die Zulassungskriterien für Segmente und Filter überprüft]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#when-does-braze-check-the-eligibility-criteria-for-segment-and-audience-filters).

##### A/B-Tests mit Optimierungen

Wenn Sie [A/B-Tests mit einer Optimierung]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) nutzen, z. B. dem automatischen Versand der Gewinnervariante nach Abschluss des A/B-Tests, verlängert sich die Dauer der Kampagne. Standardmäßig senden Intelligent Timing-Kampagnen die Gewinnvariante am Tag nach dem ersten Test an die verbleibenden Benutzer, aber Sie können dieses Versanddatum ändern.

Wenn Sie sowohl Intelligentes Timing als auch A/B-Tests verwenden, empfehlen wir Ihnen, die Gewinnervariante 2 Tage nach dem ersten Test zu versenden, anstatt 1 Tag.

![A/B-Tests im Schritt Zielgruppen, wo der Test endet und die Gewinner-Variante zwei Tage nach Beginn des ursprünglichen Tests gesendet wird.][5]

### Canvas

Dieser Abschnitt beschreibt, wie Sie Intelligentes Timing in Ihren Canvases verwenden können. Die Schritte variieren leicht, je nachdem, welchen Canvas-Workflow Sie verwenden.

{% alert important %}
Ab dem 28\. Februar 2023 können Sie keine Canvase mehr mit dem Original-Editor erstellen oder duplizieren. In diesem Abschnitt können Sie referenzieren, wie intelligentes Timing im Original-Editor funktioniert.<br><br>Braze empfiehlt Kund:innen, die die ursprüngliche Canvas-Umgebung nutzen, den Wechsel zu Canvas Flow. Es handelt sich um eine verbesserte Bearbeitungsfunktion, mit der Sie Canvases besser erstellen und verwalten können. Erfahren Sie mehr über das [Klonen Ihrer Canvases in Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

{% tabs %}
{% tab Canvas Fluss %}

In Canvas Flow wird das intelligente Timing in Nachrichtenschritten eingestellt. So verwenden Sie Intelligentes Timing in Ihrem Canvas:

1. Fügen Sie einen [Nachrichtenschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) zu Ihrem Canvas hinzu.
2. Gehen Sie zu **Zustellungseinstellungen**.
3. Wählen Sie **Intelligentes Timing verwenden**.
4. Geben Sie eine [Ausweichzeit](#fallback-time) an.

Ein:e Nutzer:in, die:der diesen Schritt eingibt, erhält die Nachricht zu seiner optimalen Uhrzeit an dem Tag, an dem er sie eingibt, WENN diese Uhrzeit noch nicht verstrichen ist. Beachten Sie, dass, wenn die optimale Zeit (in Ortszeit) einer Nutzerin oder eines Nutzers  an dem Tag, an dem er einen Nachrichtenschritt eingibt, vergangen ist, diese am nächsten Tag zur optimalen Zeit gesendet wird. Nachrichtenschritte, die auf mehrere Kanäle abzielen, können Nachrichten zu verschiedenen Zeiten für verschiedene Kanäle senden oder versuchen, sie zu senden. Wenn die erste Nachricht in einem Nachrichtenschritt zu senden versucht wird, werden alle Nutzer:innen automatisch vorangebracht.

#### Verzögerungsstufen und intelligentes Timing

Wenn Sie Intelligentes Timing nach einem [Verzögerungsschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) verwenden, kann das Lieferdatum unterschiedlich sein, je nachdem, wie Sie Ihre Verzögerung berechnen. Dies gilt nur, wenn Ihre Verzögerung auf **Nach einer Dauer** eingestellt ist, da es einen Unterschied zwischen der Berechnung von "Tagen" und "Kalendertagen" gibt.

- **Tage:** 1 Tag sind 24 Stunden, gerechnet ab dem Zeitpunkt, an dem die:der Nutzer:in den Schritt Verzögerung eingibt.
- **Kalendertage:** 1 Tag ist der Zeitraum von der Eingabe des Schritts Verzögerung durch die:den Nutzer:in bis Mitternacht in seiner Zeitzone. Das bedeutet, dass 1 Kalendertag nur wenige Minuten lang sein kann.

Wenn Sie Intelligentes Timing verwenden, empfehlen wir Ihnen, für Ihre Verspätungen Kalendertage anstelle von 24-Stunden-Tagen zu verwenden. Denn bei Kalendertagen wird die Nachricht am letzten Tag der Verzögerung zum optimalen Zeitpunkt versendet. Bei einem 24-Stunden-Tag besteht die Möglichkeit, dass die optimale Zeit der Nutzerin oder des Nutzers vor der Eingabe des Schritts liegt, was bedeutet, dass ein zusätzlicher Tag zu seiner Verzögerung hinzukommt.

Nehmen wir zum Beispiel an, Lukas optimale Zeit ist 14:00 Uhr. Er betritt den Schritt Verzögerung um 14:01 Uhr am 1\. März und die Verzögerung ist auf 2 Tage eingestellt.

- Tag 1 endet am 2\. März um 2:01 Uhr
- Tag 2 endet am 3\. März um 2:01 Uhr

Intelligent Timing soll jedoch um 14 Uhr liefern, was bereits geschehen ist. Luka wird die Nachricht also erst am nächsten Tag erhalten: 4\. März um 14:00 Uhr.

![Grafik zur Darstellung des Unterschieds zwischen Tagen und Kalendertagen, wenn die optimale Zeit einer Nutzerin oder eines Nutzers  14:00 Uhr ist, er aber den Verzögerungsschritt um 14:01 Uhr eingibt und die Verzögerung auf 2 Tage eingestellt ist. Tage stellt die Nachricht 3 Tage später zu, weil die:der Nutzer:in den Schritt nach seiner optimalen Zeit eingegeben hat, während Kalendertage die Nachricht 2 Tage später, am letzten Tag der Verzögerung, zustellen.]({% image_buster /assets/img/intelligent_timing_daysvcalendardays.png %}){: style="border:none;"}

{% endtab %}
{% tab Original-Canvas-Arbeitsablauf %}

Im Original-Canvas-Arbeitsablauf wird das intelligente Timing in der Verzögerungssektion eines Vollschritts eingestellt. So verwenden Sie Intelligentes Timing in Ihrem Canvas:

1. Fügen Sie einen Schritt zu Ihrem Canvas hinzu.
2. Öffnen Sie die **Verzögerung** für Ihren Schritt.
3. Wählen Sie **Geplant**.
4. Legen Sie eine Verzögerung fest, indem Sie *nach*, *in* oder *am nächsten Tag* verwenden.
   - Wenn Sie *nach* wählen, legen Sie die Verzögerung in Tagen oder Wochen fest. Verzögerungen werden automatisch anhand von Kalendertagen berechnet, d.h. die Nachricht wird am letzten Tag der Verzögerung zur optimalen Zeit des Benutzers gesendet. Intelligent Timing ist nicht verfügbar für Verspätungen von weniger als 1 Tag.
5. Wählen Sie **Intelligentes Timing verwenden**.
6. Geben Sie eine [Ausweichzeit](#fallback-time) an.

{% endtab %}
{% endtabs %}

#### Starten des Canvas

Anders als bei Kampagnen müssen Sie sich nicht darum kümmern, Ihr Canvas 48 Stunden vor dem Versanddatum einzuführen. Das liegt daran, dass Intelligentes Timing auf der Ebene der Schritte und nicht auf der Ebene des Canvas eingestellt wird. Stattdessen empfehlen wir, dass zwischen der Eingabe der Nutzerin oder des Nutzers in den Canvas und dem Erhalt des Schritts, bei dem intelligentes Timing verwendet wird, mindestens 48 Stunden vergehen.

### Fallback-Zeit {#fallback-time}

Sie müssen einen Ausweichzeitpunkt für die Nachricht wählen, die an Benutzer in Ihrer Zielgruppe gesendet werden soll, für die Braze nicht genügend Engagement-Daten hat, um einen optimalen Sendezeitpunkt zu berechnen. Es gibt zwei Optionen:

- die beliebteste Zeit für die Nutzung der App unter allen Nutzern
- eine spezielle angepasste Fallback-Zeit (zur Nutzerortszeit)

#### Beliebteste App Zeit

Die beliebteste App-Zeit wird durch die durchschnittliche Sitzungsstartzeit für Ihren Workspace (in Ortszeit) bestimmt. Diese Zeit wird in der [Vorschautabelle](#preview-delivery-times) in Rot angezeigt (nur bei Kampagnen).

Wenn Sie für Kampagnen ein [Zeitfenster für die Zustellung](#sending-within-specific-hours) angegeben haben und die beliebteste Zeit für die Nutzung Ihrer App außerhalb dieses Zeitfensters liegt, wird die Nachricht so nah wie möglich an den Rand des Zeitfensters gesendet. Wenn Ihr Zustellungsfenster beispielsweise zwischen 13 und 20 Uhr liegt und die beliebteste App-Zeit 22 Uhr ist, wird die Nachricht um 20 Uhr gesendet.

**Nicht genügend Sitzungsdaten**<br>
Für den seltenen Fall, dass Ihre App nicht über genügend Sitzungsdaten verfügt, um zu berechnen, wann die App am meisten genutzt wird (eine völlig neue App ohne Daten), wird die Nachricht um 17 Uhr in der Ortszeit der Nutzerin oder des Nutzers gesendet. Wenn die Ortszeit der Nutzerin oder des Nutzers nicht bekannt ist, wird sie um 17 Uhr in der Zeitzone Ihres Unternehmens gesendet.

Es ist wichtig, dass Sie sich der Einschränkungen bewusst sind, die der Einsatz von Intelligent Timing zu einem frühen Zeitpunkt im Lebenszyklus eines Nutzers mit sich bringt, wenn nur wenige Daten verfügbar sind. Sie kann dennoch wertvoll sein, denn selbst Nutzer mit wenigen aufgezeichneten Sitzungen können Einblicke in ihr Verhalten geben. Braze kann jedoch den optimalen Sendezeitpunkt später im Lebenszyklus einer Nutzerin oder eines Nutzers besser berechnen.

#### Benutzerdefinierte Ausweichzeit

Verwenden Sie die angepasste Fallback-Zeit, um eine andere Zeit für den Versand der Nachricht zu wählen. Ähnlich wie bei der beliebtesten App-Zeit wird die Nachricht zur Ausweichzeit in der lokalen Zeitzone des Benutzers gesendet. Wenn die lokale Zeitzone des Benutzers unbekannt ist, wird sie in der Zeitzone Ihres Unternehmens gesendet.

Wenn Sie bei Kampagnen mit einer benutzerdefinierten Ausweichzeit die Kampagne innerhalb von 24 Stunden nach dem Versanddatum starten, erhalten Benutzer, deren optimale Zeit bereits verstrichen ist, die Kampagne zur benutzerdefinierten Ausweichzeit. Wenn die benutzerdefinierte Ausweichzeit in ihrer Zeitzone bereits abgelaufen ist, wird die Nachricht sofort gesendet.

## Beschränkungen

- In-App-Nachrichten, Content Cards und Webhooks werden sofort zugestellt und nicht mit optimalen Zeiten versehen.
- Intelligentes Timing ist nicht verfügbar für aktionsbasierte oder API-ausgelöste Kampagnen.
- Intelligent Timing sollte in den folgenden Szenarien nicht verwendet werden:
    - **Ruhezeiten:** Die Verwendung von Quiet Hours und Intelligent Timing ist kontraproduktiv, da Quiet Hours auf einer Top-Down-Annahme über das Benutzerverhalten basiert, z. B. dass man mitten in der Nacht keine Nachrichten verschickt, während Intelligent Timing auf der Benutzeraktivität basiert. Vielleicht prüft Sam ihre App-Benachrichtigungen um 3 Uhr nachts sehr oft. Wir urteilen nicht.
    - **Rate-Limiting:** Wenn sowohl die Ratenbegrenzung als auch Intelligent Timing verwendet werden, gibt es keine Garantie dafür, wann die Nachricht zugestellt wird. Täglich wiederkehrende Kampagnen mit intelligentem Timing unterstützen keine genaue Obergrenze für den Versand von Nachrichten.
    - **IP-Warming-Kampagnen:** Einige der Intelligentes-Timing-Verhaltensweisen können dazu führen, dass Sie die täglichen Volumina, die beim ersten Aufwärmen Ihrer IP benötigt werden, nicht erreichen. Das liegt daran, dass Intelligent Timing die Segmente zweimal auswertet - einmal bei der Erstellung der Kampagne oder des Canvas und ein zweites Mal vor dem Versand an die Benutzer, um zu überprüfen, ob sie noch in diesem Segment sein sollten. Dies kann dazu führen, dass sich die Segmente verschieben und verändern, was oft dazu führt, dass einige Nutzer:innen bei der zweiten Auswertung aus dem Segment herausfallen. Diese Nutzer:innen werden nicht ersetzt, was sich darauf auswirkt, wie nah Sie an die maximale Nutzerobergrenze herankommen können.

## Fehlersuche

### Vorschaudiagramm mit wenigen Benutzern mit optimalen Zeiten

Braze benötigt eine gewisse Menge an Daten über das Engagement, um eine gute Schätzung vornehmen zu können. Wenn nicht genügend Sitzungsdaten vorhanden sind oder die anvisierten Benutzer nur wenige oder gar keine Klicks oder Öffnungen aufweisen (z. B. neue Benutzer), wird Braze standardmäßig die Ausweichzeit verwenden. Je nach Ihrer Konfiguration kann dies entweder die beliebteste App-Zeit oder eine benutzerdefinierte Ausweichzeit sein.

### Versenden nach dem Zeitplan

Ihre Kampagne mit intelligentem Timing sendet möglicherweise über das geplante Datum hinaus, wenn Sie [A/B-Tests mit einer Optimierung]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) nutzen. Kampagnen, die A/B-Testing-Optimierungen verwenden, können automatisch die Gewinner-Variante senden, nachdem der erste Test abgeschlossen ist, wodurch sich die Dauer der Kampagne verlängert. Standardmäßig wird bei Kampagnen mit einer Optimierung die Gewinner-Variante am Tag nach dem ersten Test an die verbleibenden Benutzer gesendet, aber Sie können dieses Sendedatum ändern.

Wenn Sie Intelligent Timing verwenden, empfehlen wir Ihnen, mehr Zeit für den Abschluss des A/B-Tests einzuplanen und den Versand der Gewinnervariante für 2 Tage nach dem ersten Test zu planen, anstatt für 1 Tag.


[1]: {% image_buster /assets/img/intelligent_timing_1.png %}
[2]: {% image_buster /assets/img/intel-timing-preview.png %}
[3]: {% image_buster /assets/img/intelligent_timing.png %}
[4]: {% image_buster /assets/img/intelligent_timing_hours.png %}
[5]: {% image_buster /assets/img/intelligent_timing_ab_test_duration.png %}
