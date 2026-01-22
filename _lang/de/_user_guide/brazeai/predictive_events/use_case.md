---
nav_title: Anwendungsfall
article_title: Anwendungsfälle Prognosen für Abo-Upgrades
description: "Dieses Beispiel zeigt, wie eine fiktive Marke Braze Predictive Events verwendet, um die Ergebnisse zu definieren, die für ihr Unternehmen wichtig sind - wie das Upgraden auf eine Profi-Mitgliedschaft - und gezielte Strategien zu entwickeln, die die Ergebnisse verbessern."
page_type: tutorial
---

# Anwendungsfälle: Prognosen für Abo-Upgrades mit intelligentem Targeting

> Dieses Beispiel zeigt, wie eine fiktive Marke Braze Predictive Events verwendet, um die Ergebnisse zu definieren, die für ihr Unternehmen wichtig sind - wie das Upgraden auf eine Profi-Mitgliedschaft - und gezielte Strategien zu entwickeln, die die Ergebnisse verbessern. 

Nehmen wir an, Jordan ist ein Strateg:in bei Steppington, einer App für Gesundheit und Fitness mit kostenlosen und kostenpflichtigen Angeboten. Das Team von Jordan hat sich zum Ziel gesetzt, die Upgrades für den Pro-Tarif zu erhöhen, ohne die gesamte kostenlose Nutzer:innen-Basis mit Nachrichten über Rabatte zu bombardieren. Gegenwärtig erhalten alle Nutzer:innen der kostenlosen Version nach sieben Tagen ein Angebot mit dem Titel "Try Pro for 50% off". Das führt zwar zu einigen Konversionen (ca. 5 % in 7 Tagen), aber auch zu übermäßiger Reichweite - einschließlich Rabatten für Nutzer:innen, die wahrscheinlich ohnehin upgraden würden.

Um das Targeting zu verbessern und die Ermüdung durch Messaging zu verringern, verwendet Jordan Predictive Events, um die Wahrscheinlichkeit zu modellieren, dass ein Nutzer:innen innerhalb der nächsten 7 Tage auf Pro upgraden wird. Er definiert ein angepasstes Event: `upgraded_to_pro` Er trainiert damit ein Prognosemodell und segmentiert die Nutzer:innen in intelligente, handlungsorientierte Gruppen. 

In dieser Anleitung erfahren Sie, wie Jordan diese erstellt hat:

- Ein Prognosemodell für `upgraded_to_pro` innerhalb von 7 Tagen
- Segmente, die dazu beitragen, die Konversion zu steigern und gleichzeitig weniger Nachrichten zu versenden

## Schritt 1: Erstellen Sie ein Prognosemodell für Upgrades

Jordan beginnt mit der Definition des Ergebnisses, das für seine upgraden Strategie am wichtigsten ist: ein Nutzer:innen wechselt von der kostenlosen Stufe zu Pro. Anstatt sich auf generische Trigger wie "Zeit seit Anmeldung" zu verlassen, möchte er vorhersagen, welche Nutzer:innen tatsächlich konvertieren werden. Auf diese Weise kann sein Team auf echte Signale reagieren und nicht nur auf Annahmen.

1. Im Braze-Dashboard geht Jordan zu **Analytics** > Prognosen Events.
2. Er [erstellt eine neue Prognose]({{site.baseurl}}/user_guide/brazeai/predictive_events/creating_an_event_prediction/) und nennt sie "Upgrade auf Pro in 7 Tagen".
3. Als Targeting Event wählt er sein angepasstes Event: `upgraded_to_pro`.
4. Jordan setzt das Prognosefenster auf 7 Tage, legt einen Zeitplan für das Update fest und erstellt die Prognose.

![Prognose-Einstellungen mit Definition, Fenster, Zielgruppe und Zeitplan für das Update der Prognose.]({% image_buster /assets/img/ai_use_cases/prediction_settings.png %})

## Schritt 2: Segmentierung der Nutzer:innen auf der Grundlage der Wahrscheinlichkeit eines Upgrades

Nachdem das Training abgeschlossen ist, vergibt Braze für jede in Frage kommende Nutzer:innen einen [Event Likelihood Score]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#purchase_score) (0-100). Jordan verwendet diese Bewertung, um Segmente zu erstellen - eines für Nutzer:innen mit hoher Absicht, die keinen Rabatt benötigen, und ein weiteres für Nutzer:innen, die ohne Unterstützung wahrscheinlich nicht konvertieren werden.

1. Jordan navigiert zu Segmente in Braze.
2. Er erstellt zwei [Segmente]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) unter Verwendung des [Event Likelihood Score Filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#event-likelihood-score) und wählt die von ihm erstellte Prognose aus. Die beiden Segmente sind:
  - **Wahrscheinlich wird er upgraden:** Ergebnis mehr als 70
  - **Braucht einen Anstoß zum upgraden:** Punktzahl mehr als 40 und weniger als 70

{% alert tip %}
Prognostische Filter können mit beliebigen anderen Nutzer:innen-Attributen oder Verhaltensweisen kombiniert werden. Jordan plant, diese Segmente auf der Grundlage von Nutzerinteressen weiter zu verfeinern, z.B. indem er Nutzern:innen, die häufig Fitness Tracking Features verwenden, Priorität einräumt. Damit hat er vier Untergruppen, die er genauer ansprechen kann, was es zulässig macht, Inhalte und Nachrichten auf die Bedürfnisse der einzelnen Nutzer:innen abzustimmen.
{% endalert %}

![Segmentierung mit zwei Filtern für die Ereigniswahrscheinlichkeitsbewertung.]({% image_buster /assets/img/ai_use_cases/event_likelihood_score.png %})

## Schritt 3: Personalisieren Sie Messaging nach Absicht

Jetzt, da Jordan klare Signale für seine upgraden Absichten hat und die Untergruppen auf der Grundlage des Nutzerverhaltens verfeinert hat, entwickelt er eine Messaging Strategie, die sich an die Bedürfnisse der einzelnen Nutzer:innen anpasst. Keine Einheitsgröße mehr.

Er wählt E-Mail als primären Kanal für diese Kampagne. Und warum? Denn Jordan möchte Nutzern:innen mit hoher Absicht den Wert von Pro erklären und zögernden Nutzern:innen ein überzeugendes Argument liefern - beides erfordert Platz, Bildmaterial und einen starken CTA. E-Mail gibt ihm die Flexibilität, dies gut zu tun, ohne die Nutzer:innen unter Druck zu setzen, und ermöglicht ihm das Tracking der Performance durch das Klickverhalten.

Jordan [erstellt ein Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), das das Erlebnis auf der Grundlage der soeben erstellten Segmente aufteilt. Er fügt einen Zielgruppen-Pfade-Schritt zum Targeting hinzu:

- Nutzer:innen mit hoher Absicht, die sich auf Fitness konzentrieren
- Hohe Absicht, andere Nutzer:innen
- Nutzer:innen mit geringer Absicht, die sich auf Fitness konzentrieren
- Geringe Absicht, andere Nutzer:innen

![Canvas Zielgruppen-Pfad mit vier Pfaden für jede Absichtsart.]({% image_buster /assets/img/ai_use_cases/canvas_paths_by_intent.png %})

Außerdem setzt er das Canvas-Konversions-Event auf das angepasste Event `upgraded_to_pro`, so dass Braze die upgraden Konversionen automatisch verfolgt, wenn die Nutzer:innen den Fluss durchlaufen.

### Beispiel Nachrichten pro Pfad

{% tabs %}
{% tab High intent, fitness %}

Diese Nutzer:innen sind bereits aktiv und beschäftigen sich intensiv mit den Features des Fitness Trackings. Sie werden wahrscheinlich auch ohne zusätzliche Anreize upgraden, also konzentriert sich die Nachricht darauf, tiefere Insights und fortschrittliche Tools freizuschalten, die auf ihren bestehenden Gewohnheiten aufbauen.

- **Betreffzeile:** Verfolgen Sie Ihre Fitnessziele weiter
- **Überschrift:** Ihr Fortschritt verdient Pro
- **Text:** Sie haben bereits eine starke Routine aufgebaut. Mit der Pro-Version können Sie noch tiefer gehen - verfolgen Sie Ihren Fortschritt über alle Muskelgruppen hinweg, setzen Sie sich wöchentliche Performance-Ziele und schalten Sie erweiterte Analytics frei, die auf Ihre Bewegungen zugeschnitten sind.
- **CTA:** Starten Sie Ihre kostenlose Pro-Testversion

{% endtab %}
{% tab High intent, other %}
Diese Nutzer:innen zeigen starke Signale des Engagements, wie z.B. das Stöbern in den Features von Pro oder häufige Aktivitäten in der App, sind aber nicht speziell auf das Fitness Tracking ausgerichtet. Die Nachricht hebt weitere Pro-Vorteile wie Coaching und Personalisierung hervor, um sie zum Umstieg zu bewegen.

- **Betreffzeile:** Sie sind fast fertig - Pro ist bereit, wenn Sie es sind
- **Überschrift:** Schalten Sie mehr Möglichkeiten zur Bewegung frei
- **Text:** Sie haben erkundet, was Pro zu bieten hat. Jetzt haben Sie die Chance, auf angepasste Pläne, 1:1-Coaching-Inhalte und geführte Programme zuzugreifen, die speziell für Ihre eindeutigen Ziele entwickelt wurden - ganz gleich, ob es sich um Kraft, Balance oder Beständigkeit handelt.
- **CTA:** Starten Sie Ihre kostenlose Pro-Testversion

{% endtab %}
{% tab Low intent, fitness %}
Diese Nutzer:innen beschäftigen sich mit den Fitness Features, haben aber noch keine Schritte in Richtung eines Upgrades unternommen. Die Nachricht geht auf ihre Fitnessinteressen ein und reduziert gleichzeitig die Reibungsverluste durch ein zeitlich begrenztes Angebot, so dass sie Pro als eine risikoarme Möglichkeit sehen, ihre Routine zu verbessern.

- **Betreffzeile:** Sind Sie bereit, intelligenter zu trainieren? Testen Sie Pro mit 50% Rabatt
- **Überschrift:** Ihr Workout-Upgrade wartet schon
- **Text:** Pro bietet Ihnen alles, was Sie brauchen, um stark zu werden - einfach zu befolgende Trainingspläne, Expertentipps und echtes Tracking Ihrer Fortschritte. Testen Sie es jetzt für 50% Rabatt und kündigen Sie jederzeit.
- **CTA:** Erhalten Sie 50% Rabatt auf Pro

{% endtab %}
{% tab Low intent, other %}

Diese Nutzer:innen zeigen insgesamt wenig Engagement. Es ist unwahrscheinlich, dass sie ohne einen überzeugenden Anreiz upgraden. Daher verfolgt die Nachricht einen einfachen Ansatz, bei dem die Vorteile im Vordergrund stehen, mit einem Rabatt und einer sanften Sprache, die zur Erkundung ohne Druck einlädt.

- **Betreffzeile:** 50% Rabatt auf Pro-just für dieses Wochenende
- **Überschrift:** Bereit, wenn Sie es sind
- **Text:** Erstellen Sie Ihren ersten personalisierten Fitnessplan, tracken Sie Ihre Fortschritte und erhalten Sie Zugang zu exklusiven Workouts - alles zum halben Preis. Testen Sie Pro für weniger und kündigen Sie jederzeit.
- **CTA:** Erhalten Sie 50% Rabatt auf Pro

{% endtab %}
{% endtabs %}

## Schritt 4: Messen Sie die Ergebnisse und optimieren Sie Ihre Strategie

Nachdem die Kampagne gelaufen ist, überprüft Jordan die Performance in [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), um zu verstehen, wie gut die personalisierten Pfade funktioniert haben - und ob die Kombination von prognostischen Absichten mit Verhaltenssignalen die Upgraderaten verbessert hat.

E-Mail Performance nach Pfad:

- **Hohe Absicht, Fitness**
   - *Öffnungsrate:* 34%
   - *Klickrate:* 20%
   - *Konversionsrate:* 13%
   - Kein Rabatt verwendet
- **Hohe Absicht, andere**
   - *Öffnungsrate:* 30%
   - *Klickrate:* 17%
   - *Konversionsrate:* 11%
   - Kein Rabatt verwendet
- **Geringe Absicht, Fitness**
   - *Öffnungsrate:* 27%
   - *Klickrate:* 12%
   - *Konversionsrate:* 8%
   - Angebot mit 50% Rabatt
- **Geringe Absicht, Sonstiges**
   - *Öffnungsrate:* 23%
   - *Klickrate:* 9%
   - *Konversionsrate:* 6%
   - Angebot mit 50% Rabatt

Im Vergleich zu der vorherigen Kampagne des Teams, bei der ein pauschaler Rabatt nach 7 Tagen zu nur 5 % Konversion und zu viel Messaging führte, zeigt der gezielte Ansatz eine deutliche Steigerung in allen Gruppen, mit verbesserter Effizienz und weniger unnötigen Rabatten.

Der [Funnel-Bericht]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) zeigt auch eine deutliche Verringerung der Absprungrate bei den wichtigsten Schritten, insbesondere bei Nutzern:innen mit geringer Absicht, die personalisierte Nachrichten erhalten haben. Mehr Nutzer:innen öffnen, klicken und upgraden - ein Beweis für den Wert von Targeting, das auf Absichten basiert.

Jordan nutzt diese Insights, um:

- Entdecken Sie A/B-Tests für Betreffzeilen und CTA-Formulierungen
- Überprüfen Sie die Rabattschwelle für Nutzer:innen mit mittlerer Absicht
- Verfeinern Sie die Segmentierung auf der Grundlage zusätzlicher Verhaltensweisen wie der Ansicht von Inhalten oder der Nutzung von Features in der App.

Mit Prognosen und einer mehrschichtigen Segmentierung verfügt sein Team nun über eine skalierbare Strategie, die das Messaging an die Absichten und das Verhalten der Nutzer:innen anpasst und so für mehr Upgrades sorgt und gleichzeitig das Vertrauen in die Marke bewahrt.
