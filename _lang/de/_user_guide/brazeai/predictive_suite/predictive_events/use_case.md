---
nav_title: Anwendungsfall
article_title: "Anwendungsfall: Prognose für Abonnement-Upgrades"
description: "Dieses Beispiel veranschaulicht, wie eine fiktive Marke Braze Predictive Events einsetzt, um die für ihr Geschäft relevanten Ergebnisse zu definieren – wie beispielsweise das Upgraden auf eine Pro-Mitgliedschaft – und gezielte Strategien zu entwickeln, die die Ergebnisse verbessern."
page_type: tutorial
---

# Anwendungsfälle: Prognostizieren Sie Upgrades für Abonnements mit intelligenterem Targeting.

> Dieses Beispiel veranschaulicht, wie eine fiktive Marke Braze Predictive Events einsetzt, um die für ihr Geschäft relevanten Ergebnisse zu definieren – wie beispielsweise das Upgraden auf eine Pro-Mitgliedschaft – und gezielte Strategien zu entwickeln, die die Ergebnisse verbessern. 

Nehmen wir an, Jordan ist Lebenszyklusstrateg:in bei Steppington, einer Gesundheits- und Fitness-App mit kostenlosen und kostenpflichtigen Angeboten. Das Team von Jordan hat sich zum Ziel gesetzt, die Anzahl der Nutzer:innen, die den Pro-Tarif upgraden, zu erhöhen, ohne die gesamte Nutzerbasis mit Rabattnachrichten zu überfluten. Derzeit versenden sie nach sieben Tagen eine Werbeaktion mit dem Titel „Profi-Version mit 50 % Rabatt testen“ an alle Nutzer:innen der kostenlosen Version. Es führt zwar zu einigen Konversionen (etwa 5 % über 7 Tage), jedoch auch zu einer übermäßigen Reichweite – einschließlich der Abwertung von Nutzern:innen, die wahrscheinlich ohnehin upgradet hätten.

Um das Targeting zu verbessern und die Ermüdung durch Messaging zu reduzieren, verwendet Jordan Predictive Events, um die Wahrscheinlichkeit zu modellieren, dass eine Nutzer:in innerhalb der nächsten 7 Tage upgradet und Pro nutzt. Er definiert ein angepasstes Event: `upgraded_to_pro`und nutzt dieses anschließend, um ein Vorhersagemodell zu trainieren und die Nutzer:innen in intelligente, handlungsorientierte Gruppen zu segmentieren. 

Dieses Tutorial führt Sie durch den Entstehungsprozess von Jordans Werk:

- Ein Modell für die `upgraded_to_pro`Prognose für einen Zeitraum von sieben Tagen
- Segmente, die dazu beitragen, die Konversion zu erhöhen und gleichzeitig weniger Nachrichten zu versenden

## Schritt 1: Erstellen Sie ein Vorhersagemodell für das Upgraden.

Jordan beginnt damit, das für seine Upgrade-Strategie wichtigste Ergebnis zu definieren: einen Nutzer:in, der von der kostenlosen Version zur Pro-Version upgradet. Anstatt sich auf allgemeine Auslöser wie „Zeit seit der Anmeldung“ zu verlassen, möchte er prognostizieren, welche Nutzer:innen tatsächlich wahrscheinlich konvertieren werden. Auf diese Weise kann sein Team auf tatsächliche Signale reagieren und nicht nur auf Annahmen.

1. Im Braze-Dashboard navigiert Jordan zu **„Analytics“** > **„Predictive Events**“.
2. Er [erstellt eine neue Ereignisprognose]({{site.baseurl}}/user_guide/brazeai/predictive_events/creating_an_event_prediction/) und benennt sie „Upgraden auf Pro in 7 Tagen”.
3. Als Zielereignis wählt er sein angepasstes Event aus: `upgraded_to_pro`.
4. Jordan legt das Prognosefenster auf 7 Tage fest, erstellt einen Zeitplan für Updates und erstellt die Prognose.

![Prognoseeinstellungen, die die Definition, das Fenster, die Zielgruppe und den Zeitplan für die Prognose anzeigen.]({% image_buster /assets/img/ai_use_cases/prediction_settings.png %})

## Schritt 2: Segmentieren Sie die Nutzer:innen anhand der Wahrscheinlichkeit, dass sie upgraden.

Nach Abschluss des Trainings weist Braze jeder berechtigten Nutzer:in einen [Ereigniswahrscheinlichkeitswert]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#purchase_score) (0–100) zu. Jordan nutzt diese Punktzahl, um umsetzbare Segmente zu erstellen – eines für Nutzer:innen mit hoher Kaufabsicht, die möglicherweise keinen Rabatt benötigen, und ein weiteres für Nutzer:innen, die ohne Unterstützung wahrscheinlich nicht konvertieren werden.

1. Jordan navigiert zu „Segmente“ in Braze.
2. Er erstellt zwei [Segmente]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) mithilfe des [Filters „Event Likelihood Score“]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#event-likelihood-score) und wählt die von ihm erstellte Prognose aus. Die beiden Segmente sind:
  - **Wahrscheinliche Upgrade:** Erreichen Sie mehr als 70 Punkte.
  - **Es ist erforderlich, das System zu upgraden:** Erreichen Sie mehr als 40 und weniger als 70 Punkte.

{% alert tip %}
Prädiktive Filter können mit beliebigen anderen Attributen oder Verhaltensweisen von Nutzer:innen kombiniert werden. Jordan plant, diese Segmente auf Grundlage der Nutzerinteressen weiter zu verfeinern, beispielsweise durch die Priorisierung von Nutzer:innen, die häufig Fitness-Tracking-Features verwenden. Dadurch erhält er vier Untergruppen, die er genauer ansprechen kann, sodass Inhalte und Messaging auf die Bedürfnisse jeder Nutzer:in abgestimmt werden können.
{% endalert %}

![Segment-Generator mit zwei Filtern für den Event Likelihood Score.]({% image_buster /assets/img/ai_use_cases/event_likelihood_score.png %})

## Schritt 3: Personalisieren Sie Messaging nach Absichtsstufe

Da Jordan nun eindeutige Signale für eine Absicht, das System zu upgraden, hat und die Untergruppen auf der Grundlage des Nutzerverhaltens verfeinert hat, entwickelt er eine Messaging-Strategie, die sich an die Bedürfnisse jeder Nutzer:in anpasst. Keine pauschalen Nachrichten mehr.

Er wählt E-Mail als primären Kanal für diese Kampagne. Und warum? Da Jordan den Wert von Pro für Nutzer:innen mit hoher Kaufabsicht erläutern und überzeugende Argumente für eher zögerliche Nutzer:innen liefern möchte, sind für beide Zwecke Platz, visuelle Elemente und ein aussagekräftiger CTA erforderlich. E-Mails bieten ihm die Flexibilität, dies effektiv zu tun, ohne die Nutzer:innen unter Druck zu setzen, und ermöglichen es ihm, die Performance anhand des Klickverhaltens zu verfolgen.

Jordan [erstellt ein Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), das die Erfahrung auf der Grundlage der von ihm gerade erstellten Segmente aufteilt. Er fügt einen Schritt „Zielgruppen-Pfade“ hinzu, um Folgendes anzusprechen:

- Nutzer:innen mit hoher Absicht und Fokus auf Fitness
- Hohe Absicht, andere Nutzer:innen
- Nutzer:innen mit geringer Kaufabsicht, die sich auf Fitness konzentrieren
- Geringe Absicht, andere Nutzer:innen

![Canvas-Zielgruppen-Pfad mit vier Pfaden für jeden Intent-Typ.]({% image_buster /assets/img/ai_use_cases/canvas_paths_by_intent.png %})

Er legt außerdem das Canvas-Konversions-Event als angepasstes Event fest`upgraded_to_pro`, sodass Braze die Upgrade-Konversionen automatisch verfolgt, während die Nutzer:innen den Ablauf durchlaufen.

### Beispielnachrichten pro Pfad

{% tabs %}
{% tab High intent, fitness %}

Diese Nutzer:innen sind bereits aktiv und nutzen die Fitness-Tracking-Features intensiv. Es ist wahrscheinlich, dass sie ohne zusätzliche Anreize upgraden werden. Daher konzentriert sich die Nachricht darauf, tiefere Insights und fortschrittliche Tools zu erschließen, die auf ihren bestehenden Gewohnheiten aufbauen.

- **Betreffzeile:** Erreichen Sie Ihre Fitnessziele
- **Überschrift:** Ihr Fortschritt verdient Pro
- **Text:** Sie haben bereits eine solide Routine aufgebaut. Mit Pro können Sie noch tiefer gehen – verfolgen Sie Ihre Fortschritte über verschiedene Muskelgruppen hinweg, legen Sie wöchentliche Ziele für die Performance fest und erschließen Sie sich erweiterte Analytics, die auf Ihre Bewegungsabläufe zugeschnitten sind.
- **CTA:** Beginnen Sie Ihre kostenlose Demo-Version von Pro

{% endtab %}
{% tab High intent, other %}
Diese Nutzer:innen zeigen deutliche Anzeichen für ein starkes Engagement – beispielsweise durch das Durchsuchen der Pro-Features oder häufige App-Aktivitäten –, konzentrieren sich jedoch nicht speziell auf das Fitness-Tracking. Die Nachricht hebt die umfassenderen Vorteile von Pro hervor, wie Coaching und Personalisierung, um sie zum Kauf zu bewegen.

- **Betreffzeile:** Sie sind fast am Ziel – Pro ist bereit, wenn Sie es sind.
- **Überschrift:** Entdecken Sie weitere Möglichkeiten, sich fortzubewegen
- **Text:** Sie haben sich mit den Funktionen von Pro vertraut gemacht. Dies ist Ihre Gelegenheit, auf angepasste Pläne, 1:1-Coaching-Inhalte und geführte Programme zuzugreifen, die auf Ihre eindeutigen Ziele zugeschnitten sind – sei es Kraft, Gleichgewicht oder Beständigkeit.
- **CTA:** Beginnen Sie Ihre kostenlose Demo-Version von Pro

{% endtab %}
{% tab Low intent, fitness %}
Diese Nutzer:innen beschäftigen sich mit Fitness-Features, haben jedoch noch keine Schritte unternommen, um zu upgraden. Die Nachricht spricht das Interesse der Kunden an Fitness an und reduziert gleichzeitig die Hemmschwelle durch ein zeitlich begrenztes Angebot. So wird Pro für sie zu einer risikoarmen Möglichkeit, ihre Routine zu verbessern.

- **Betreffzeile:** Sind Sie bereit, intelligenter zu trainieren? Testen Sie Pro mit 50 % Rabatt
- **Überschrift:** Ihr Training kann upgradet werden.
- **Text:** Pro bietet Ihnen alles, was Sie für einen erfolgreichen Start benötigen – leicht verständliche Trainingspläne, Expertentipps und zuverlässiges Tracking. Testen Sie es jetzt mit 50 % Rabatt und kündigen Sie jederzeit.
- **CTA:** Erhalten Sie 50 % Rabatt auf Pro

{% endtab %}
{% tab Low intent, other %}

Diese Nutzer:innen zeigen insgesamt nur ein geringes Engagement. Ohne einen überzeugenden Anreiz ist es unwahrscheinlich, dass sie upgraden. Daher verfolgt die Nachricht einen einfachen Ansatz, bei dem die Vorteile im Vordergrund stehen, mit einem Rabatt und einer freundlichen Sprache, um ohne Druck zum Ausprobieren einzuladen.

- **Betreffzeile:** 50 % Rabatt auf Pro – nur an diesem Wochenende
- **Überschrift:** Wir sind bereit, sobald Sie es sind.
- **Text:** Erstellen Sie Ihren ersten personalisierten Fitnessplan, verfolgen Sie Ihre Fortschritte und greifen Sie auf exklusive Workouts zu – und das alles zum halben Preis. Testen Sie Pro zu einem reduzierten Preis und kündigen Sie jederzeit.
- **CTA:** Erhalten Sie 50 % Rabatt auf Pro

{% endtab %}
{% endtabs %}

## Schritt 4: Messen Sie die Ergebnisse und optimieren Sie Ihre Strategie.

Nach Abschluss der Kampagne überprüft Jordan die Performance in [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), um zu ermitteln, wie erfolgreich die personalisierten Pfade waren und ob die Kombination aus vorhersagbarer Absicht und Verhaltenssignalen zu einer Verbesserung der Upgrade-Raten geführt hat.

E-Mail-Performance nach Pfad:

- **Hohe Absicht, Fitness**
   - *Öffnungsrate:* 34 %
   - *Klickrate:* 20%
   - *Konversionsrate:* 13 %
   - Es wurde kein Rabatt in Anspruch genommen.
- **Hohe Absicht, Sonstiges**
   - *Öffnungsrate:* 30
   - *Klickrate:* 17 %
   - *Konversionsrate:* elf Prozent
   - Es wurde kein Rabatt in Anspruch genommen.
- **Geringe Absicht, Fitness**
   - *Öffnungsrate:* 27 %
   - *Klickrate:* Zwölf Prozent
   - *Konversionsrate:* acht Prozent
   - 50 % Rabatt inklusive
- **Geringe Absicht, Sonstiges**
   - *Öffnungsrate:* 23 %
   - *Klickrate:* 9 %
   - *Konversionsrate:* 6 %
   - 50 % Rabatt inklusive

Im Vergleich zur vorherigen einheitlichen Kampagne des Teams (bei der ein pauschaler Rabatt nach 7 Tagen zu einer Konversionsrate von nur 5 % und einer Überflutung mit Messaging-Nachrichten führte) zeigt der zielgerichtete Ansatz eine deutliche Steigerung in allen Gruppen, mit verbesserter Effizienz und weniger unnötigen Rabatten.

Der [Funnel-Bericht]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) zeigt auch einen deutlichen Rückgang der Abbrüche in wichtigen Schritten, insbesondere bei Nutzern:innen mit geringer Kaufabsicht, die personalisierte Messaging-Kommunikation erhalten haben. Immer mehr Nutzer:innen öffnen, klicken und upgraden – ein Beweis für den Wert des absichtsbasierten Targetings.

Jordan nutzt diese Insights, um:

- Erkunden Sie A/B-Tests zu Betreffzeilen und CTA-Formulierungen.
- Bitte überprüfen Sie die Rabattschwelle für Nutzer:innen mit mittlerer Kaufabsicht.
- Die Segmente auf der Grundlage zusätzlicher Verhaltensweisen wie Inhaltsaufrufe oder Nutzung von App-Features weiter verfeinern.

Dank Predictive Events und mehrstufiger Segmentierung verfügt sein Team nun über eine skalierbare Strategie, die das Messaging an die Absichten und das Verhalten der Nutzer:innen anpasst und so mehr Upgrades generiert, während das Vertrauen in die Marke gewahrt bleibt.
