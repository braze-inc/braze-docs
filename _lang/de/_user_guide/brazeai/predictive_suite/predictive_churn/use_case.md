---
nav_title: Anwendungsfall
article_title: "Anwendungsfall: Abwanderung durch zeitnahe Inhalte verringern"
description: "Dieses Beispiel veranschaulicht, wie eine fiktive Marke Predictive Churn einsetzt, um proaktiv die Abwanderung von Nutzer:innen zu reduzieren."
page_type: tutorial
---

# Anwendungsfälle: Verringern Sie die Abwanderung durch eine zeitnahe erneute Interaktion mit Inhalten.

> Dieses Beispiel veranschaulicht, wie eine fiktive Marke Predictive Churn einsetzt, um proaktiv die Abwanderung von Nutzer:innen zu reduzieren. Anstatt abzuwarten, bis es zu Abwanderungen kommt, sollten Sie vorhersagen, welche Nutzer:innen gefährdet sind, und ihnen maßgeschneiderte Nachrichten zukommen lassen, solange sie noch aktiv sind.

Nehmen wir an, Frau Camila ist CRM-Manager:in bei MovieCanon, einer Streaming-Plattform für Independent-Filme, Dokumentationen und internationale Serien.

Das Team von Camila hat einen besorgniserregenden Trend festgestellt: Nutzer:innen führen eine Registrierung durch, streamen ein oder zwei Filme und verschwinden dann. In der Vergangenheit wurde versucht, eine Woche später eine allgemeine E-Mail mit dem Inhalt „Wir vermissen Sie“ zu versenden – jedoch mit einer Konversionsrate von nur 3 % war dies unzureichend und kam zu spät. Die meisten Nutzer:innen haben keine erneute Interaktion, und sie wandern ab.

Camila möchte dies ändern. Anstatt auf abwandernde Nutzer:innen zu reagieren, nachdem sie bereits abgewandert sind, nutzt sie Predictive Churn, um Nutzer:innen zu identifizieren, die innerhalb der nächsten 14 Tage wahrscheinlich inaktiv werden – so hat ihr Team die Möglichkeit zu einer erneuten Interaktion mit diesen Personen, solange sie noch aktiv sind.

Dieses Tutorial führt Sie durch die Vorgehensweise von Camila:

- Erstellt ein Modell zur Prognose der Abwanderungsrate auf Grundlage des Nutzerverhaltens.
- Segmentiert Nutzer:innen nach Risikostufe
- Entwickelt eine Kampagne zur erneuten Interaktion, die auf die am stärksten gefährdeten Personen zugeschnitten ist.
- Bewertet die Auswirkungen mithilfe von Analytics für Kampagnen.

## Schritt 1: Erstellen Sie ein Modell zur Prognose der Abwanderungsrate.

Camila beginnt damit, das Ergebnis zu modellieren, das sie vermeiden möchte: dass Nutzer:innen inaktiv werden. Für MovieCanon bedeutet abwandern, dass innerhalb von 14 Tagen kein stream gestartet wird – dies ist das Verhalten, das sie vorhersagen möchte.

1. Im Braze-Dashboard navigiert Frau Camila zu **„Analytics“** > **„Voraussichtliche Abwanderung**“.
2. Sie erstellt eine neue Prognose für die voraussichtliche Abwanderung und benennt sie „Abwanderungsrisiko in zwei Wochen“.
3. Um die Abwanderung zu definieren, wählt `do not`sie  und das angepasste Event `stream_started`, das aktives Engagement anzeigt.
4. Sie legt das Fenster für Prognosen auf 14 Tage fest, was bedeutet, dass das Modell Nutzer:innen identifiziert, die wahrscheinlich 14 Tage lang keinen neuen Stream starten werden.

![Definition der Abwanderung, wobei Abwanderung als ein Nutzer:in definiert ist, der in den letzten 14 "stream_started"Tagen kein angepasstes Event durchgeführt hat.]({% image_buster /assets/img/ai_use_cases/churn_definition.png %})

{:start="5"}
5\. Sie wählt eine Prognosegruppe aus, die alle Nutzer:innen umfasst, die in den letzten 30 Tagen relevante Ereignisse ausgelöst haben, sodass das Modell über ausreichend aktuelle Verhaltensdaten verfügt, um daraus zu lernen.
6\. Sie stellt den Zeitplan für die Updates der Prognosen auf wöchentlich ein, damit die Ergebnisse aktuell bleiben.
7\. Sie wählt **„Prognose erstellen“** aus.

Das Modell beginnt dann mit dem Trainieren und analysiert Verhaltensweisen wie kürzlich durchgeführte Sitzungen, die Häufigkeit der Aufrufe und Interaktionen mit Inhalten, um Muster zu erkennen, die eine Prognose für einen Abbruch liefern. Eine Stunde später erhält Camila eine E-Mail, dass ihre Prognose fertig trainiert ist. Sie öffnet sie in Braze und überprüft den Qualitätswert [der Prognose]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#prediction_quality). Es ist mit „Gut“ gekennzeichnet, was bedeutet, dass die Prognosen des Modells wahrscheinlich genau und zuverlässig sind. Überzeugt von der Performance des Modells, setzt sie ihre Arbeit fort.

## Schritt 2: Segmentieren Sie Nutzer:innen nach Abwanderungsrisiko

Nach Abschluss des Trainings weist Braze jeder in Frage kommenden Nutzer:in einen [Churn-Risiko-Score]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/#churn_score) zwischen 0 und 100 zu. 

Um einen Startschwellenwert für das Targeting zu ermitteln, nutzt Camila den Schieberegler für die Prognose der Zielgruppe, um eine Vorschau anzuzeigen, wie viele Nutzer:innen in jeden Punktbereich fallen und wie genau die Prognose auf dieser Ebene ist. Sie wägt Abdeckung und Präzision auf der Grundlage der erwarteten echten Positiven ab. Auf dieser Grundlage beschließt sie, Risikowerte über 70 zu berücksichtigen. 

1. Camila navigiert zu „Segmente“ in Braze.
2. Sie erstellt ein [Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) mithilfe des [Filters „Churn Risk Score“]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#churn-risk-score) und wählt die von ihr erstellte Abwanderungsprognose aus:
   - **Wahrscheinliche Abwanderung:** Erreichen Sie mehr als 70 Punkte.

![Segmentfilterung für Nutzer:innen mit einem Churn-Risiko-Score von über 70.]({% image_buster /assets/img/ai_use_cases/churn_risk_score.png %})

## Schritt 3: Richten Sie sich mit wiederkehrenden Inhalten für die erneute Interaktion an gefährdete Nutzer:innen aus.

Nachdem ihre Prognose und ihr Segment fertig sind, richtet Camila eine wiederkehrende Kampagne ein, die jede Woche automatisch Nutzer:innen erreicht, die einem Risiko ausgesetzt sind.

1. Camila erstellt eine wiederkehrende Kampagne und aktiviert [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), sodass jede Nachricht zu dem Zeitpunkt zugestellt wird, zu dem die Wahrscheinlichkeit des Engagements durch die jeweilige Nutzer:in am höchsten ist, anstatt sich auf einen festen Tag und eine feste Uhrzeit zu verlassen.
2. Sie richtet sich an das Segment „Wahrscheinliche Abwanderer“, das sie gerade erstellt hat.
3. Sie legt das Konversions-Event der Kampagne als angepasstes Event fest`stream_started`, um zu verfolgen, wie viele Nutzer:innen tatsächlich zurückkehren, um Inhalte anzusehen.
4. Camila wählt E-Mail als ihren primären Kanal – dieser bietet ihr die Möglichkeit, mehrere personalisierte Inhalte in einem visuell ansprechenden Format ohne allzu großen Druck hervorzuheben. Die E-Mail enthält:
   - Eine personalisierte Watchlist, die auf [KI-basierten Artikelempfehlungen]({{site.baseurl}}/user_guide/brazeai/recommendations/) basiert und dynamisch aus dem Katalog von MovieCanon ausgewählt wird.
   - Ein Aufruf zum Handeln, der sie direkt in die App führt.

Dadurch wird sichergestellt, dass MovieCanon jede Woche nur die Nutzer:innen erreicht, die eine Erinnerung benötigen – ohne übermäßiges Messaging und ohne Spekulationen.

### Beispiel-E-Mail

- **Betreffzeile:** Bitte lassen Sie diese Titel nicht offen.
- **Überschrift:** Ihre nächste außergewöhnliche Uhr wartet auf Sie.
- **Text:** Haben Sie schon länger nicht mehr auf „Play“ geklickt? Keine Sorge – wir haben einige Empfehlungen speziell für Sie zusammengestellt. Von spannungsgeladenen Thrillern bis hin zu preisgekrönten Dokumentarfilmen – hier ist für jeden Geschmack etwas dabei.
- **CTA:** Weitere Empfehlungen anzeigen

## Schritt 4: Performance messen

Nach einigen Wochen überprüft Frau Camila ihre [Analytics für die Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/), um die Performance der Strategie zu bewerten. 

Sie sieht:

- *Öffnungsrate:* 31 %
- *Klickrate:* 15%
- *Konversionsrate* (Stream innerhalb von 48 Stunden gestartet): elf Prozent

Im Vergleich zur früheren „Wir vermissen Sie“-Kampagne (bei der die Konversionsraten bei etwa 3 % lagen) verringert dieser neue Ablauf die Abwanderung in der Zielgruppe um 28 %. Sie analysiert den [Funnel-Bericht,]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) um festzustellen, an welcher Stelle die Nutzer:innen abspringen. Obwohl die Öffnungs- und Klickraten gut sind, stellt sie eine leichte Diskrepanz zwischen Klick und Konversion fest, was sie dazu veranlasst, den CTA-Text zu testen oder mit dem Layout zu experimentieren.

Um die langfristigen Auswirkungen zu verstehen, verfolgt Frau Camila auch die Anzahl der Nutzer:innen, die Woche für Woche in das Segment „Wahrscheinliche Abwanderung“ gelangen. Dies unterstützt sie dabei, den allgemeinen Gesundheitszustand des Lebenszyklus zu beurteilen und die Strategie zur Bindung der Kunden auf einer breiteren Ebene zu gestalten. Abschließend kehrt sie zur Seite [„Prognose-Analytics“]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) zurück, um ihre Prognose für die Abwanderung zu überprüfen und die prognostizierten Abwanderten mit den tatsächlichen Abgewanderten zu vergleichen – eine nützliche Überprüfung, um sicherzustellen, dass das Modell wie erwartet funktioniert.

Auf Grundlage dieser Insights plant Camila, Betreffzeilen einem A/B-Test zu unterziehen, verschiedene Zeitfenster zu testen und mit Inhaltsformaten wie Empfehlungen im Karussellstil in einer In-App-Nachricht zu experimentieren.

Dank voraussichtlicher Abwanderungen, intelligentem Timing und KI-gestützter Personalisierung reagiert Camilas Team nicht nur auf Abwanderungen, sondern ist ihnen sogar einen Schritt voraus. Ihre Kampagne läuft diskret im Hintergrund und erreicht die richtigen Personen zur richtigen Zeit mit Inhalten, die für sie tatsächlich von Interesse sind.
