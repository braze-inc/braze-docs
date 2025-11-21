---
nav_title: Anwendungsfall
article_title: Anwendungsfälle ABWANDERUNG VERRINGERN mit zeitnahen Inhalten
description: "Dieses Beispiel zeigt, wie eine fiktive Marke voraussichtliche ABWANDERUNG VERRINGERN nutzt, um die Abwanderung von Nutzer:innen proaktiv zu reduzieren."
page_type: tutorial
---

# Anwendungsfälle: ABWANDERUNG VERRINGERN durch rechtzeitige erneute Interaktion mit den Inhalten

> Dieses Beispiel zeigt, wie eine fiktive Marke voraussichtliche ABWANDERUNG VERRINGERN nutzt, um die Abwanderung von Nutzer:innen proaktiv zu reduzieren. Anstatt auf die Abwanderung zu warten, können Sie vorhersagen, welche Nutzer:innen gefährdet sind, und ihnen maßgeschneiderte Nachrichten zustellen, solange sie noch aktiv sind.

Nehmen wir an, Camila ist ein CRM Manager bei MovieCanon, einer Streaming-Plattform für Indie-Filme, Dokumentarfilme und internationale Serien.

Camilas Team hat einen beunruhigenden Trend festgestellt: Nutzer:innen melden sich an, streamen ein oder zwei Filme und verschwinden dann. In der Vergangenheit haben sie versucht, eine Woche später eine generische E-Mail mit dem Satz "Wir vermissen Sie" zu versenden - aber mit einer Konversionsrate von nur 3 % ist das zu wenig und zu spät. Die meisten Nutzer:innen engagieren sich nicht erneut und die Abwanderung ist unvermeidlich.

Camila möchte das ändern. Anstatt erst nach der Abwanderung zu reagieren, nutzt sie die Prognose, um Nutzer:innen zu identifizieren, die wahrscheinlich innerhalb der nächsten 14 Tage inaktiv werden. So hat ihr Team die Opportunity, die Nutzer:innen zu erneuern, solange sie noch aktiv sind.

In dieser Anleitung erfahren Sie, wie Camila:

- Erstellt ein Modell zur Prognose der Abwanderung auf der Grundlage des Verhaltens der Nutzer:in
- Segmentierung der Nutzer:innen nach Risikoniveau
- Entwickelt eine Kampagne zur erneuten Interaktion, die auf die am meisten gefährdeten Personen zugeschnitten ist
- Bewertet die Wirkung mithilfe von Analytics für Kampagnen

## Schritt 1: Erstellen Sie ein Modell zur Prognose der Abwanderung

Camila beginnt mit der Modellierung des Ergebnisses, das sie vermeiden möchte: Nutzer:innen werden inaktiv. Für MovieCanon bedeutet Abwandern, dass ein Stream nicht innerhalb von 14 Tagen gestartet wird - das ist also das Verhalten, das sie prognostizieren möchte.

1. Auf dem Braze-Dashboard geht Camila zu **Analytics** > Predictive Churn.
2. Sie erstellt eine neue Prognose für die Abwanderung und nennt sie "Abwanderungsrisiko in 2 Wochen".
3. Um die Abwanderung zu definieren, wählt sie `do not` und das angepasste Event `stream_started`, das aktives Engagement anzeigt.
4. Sie setzt das Prognose-Fenster auf 14 Tage - das heißt, das Modell wird Nutzer:innen identifizieren, die wahrscheinlich 14 Tage lang keinen neuen Stream starten.

![Churn-Definition, die zeigt, dass ein Nutzer:in den letzten 14 Tagen kein angepasstes Event "stream_started" durchgeführt hat.]({% image_buster /assets/img/ai_use_cases/churn_definition.png %})

{:start="5"}
5\. Sie wählt eine Zielgruppe für Prognosen aus, die alle Nutzer:innen umfasst, die in den letzten 30 Tagen relevante Ereignisse getriggert haben, so dass das Modell aus dem jüngsten Verhalten lernen kann.
6\. Sie stellt den Zeitplan für das Update der Prognosen auf wöchentlich, damit die Ergebnisse aktuell bleiben.
7\. Sie wählt die Option **Prognose erstellen** aus.

Das Modell beginnt dann zu trainieren, indem es Verhaltensweisen wie die letzten Sitzungen, die Häufigkeit des Betrachtens und die Interaktionen mit Inhalten analysiert, um Muster zu erkennen, die den Abbruch prognostizieren. Camila erhält eine Stunde später eine E-Mail, dass ihre Prognose das Training abgeschlossen hat. Sie öffnet sie in Braze und überprüft die [Qualitätsbewertung der Prognose]({{site.baseurl}}/user_guide/brazeai/predictive_events/analytics/#prediction_quality). Es ist mit "Gut" gekennzeichnet, was bedeutet, dass die Prognosen des Modells wahrscheinlich genau und zuverlässig sind. Sie ist von der Performance des Modells überzeugt und geht weiter.

## Schritt 2: Segmentierung der Nutzer:innen nach Abwanderungsrisiko

Nachdem das Modell das Training abgeschlossen hat, weist Braze jedem in Frage kommenden Nutzer:innen einen [Churn Risk Score]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/#churn_score) zwischen 0-100 zu. 

Um einen Anfangsschwellenwert für das Targeting festzulegen, verwendet Camila den Schieberegler für die Zielgruppe, um eine Vorschau darauf zu erhalten, wie viele Nutzer:innen in die einzelnen Bewertungsbereiche fallen und wie genau die Vorhersage auf dieser Ebene ist. Sie sorgt für ein Gleichgewicht zwischen Reichweite und Präzision auf der Grundlage der zu erwartenden echten positiven Ergebnisse. Auf dieser Grundlage entscheidet sie sich für ein Targeting von Risikowerten über 70. 

1. Camila navigiert zu Segmente in Braze.
2. Sie erstellt ein [Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) mithilfe des [Filters Churn Risk Score]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#churn-risk-score) und wählt die von ihr erstellte Prognose zur Abwanderung aus:
   - **Wahrscheinlich abwandern:** Ergebnis mehr als 70

Segmentierung für Nutzer:innen mit einem Abwanderungsrisiko von mehr als 70.]({% image_buster /assets/img/ai_use_cases/churn_risk_score.png %})

## Schritt 3: Targeting gefährdeter Nutzer:innen mit Inhalten zur erneuten Interaktion

Mit ihren Prognosen und Segmenten richtet Camila eine wiederkehrende Kampagne ein, die automatisch jede Woche Nutzer:innen erreicht, die ein Risiko darstellen.

1. Camila erstellt eine wiederkehrende Kampagne und ermöglicht [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), so dass jede Nachricht dann zugestellt wird, wenn jeder einzelne Nutzer:innen sich am ehesten engagiert, anstatt sich auf einen festen Tag und eine feste Uhrzeit zu verlassen.
2. Sie targeting das soeben erstellte Segment "Likely to churn".
3. Sie setzt das Konversions-Event der Kampagne auf das angepasste Event `stream_started`, um zu verfolgen, wie viele Nutzer:innen tatsächlich zurückkehren, um sich den Inhalt anzusehen.
4. Camila wählt die E-Mail als primären Kanal - sie gibt ihr die Möglichkeit, mehrere personalisierte Inhalte in einem visuell reichhaltigen Format hervorzuheben, ohne dabei zu viel Druck auszuüben. Die E-Mail enthält:
   - Eine personalisierte Watchlist mit [KI Artikel-Empfehlungen]({{site.baseurl}}/user_guide/brazeai/recommendations/), dynamisch ausgewählt aus dem MovieCanon Katalog
   - Ein Aufruf zum Handeln, der sie direkt in die App bringt.

So wird sichergestellt, dass MovieCanon jede Woche nur die Nutzer:innen erreicht, die einen Anstoß brauchen - kein übermäßiges Messaging, kein Rätselraten.

### Beispiel E-Mail

- **Betreffzeile:** Lassen Sie diese Titel nicht hängen
- **Überschrift:** Ihre nächste große Uhr wartet schon
- **Text:** Haben Sie schon lange nicht mehr auf Play gedrückt? Keine Sorge - wir haben ein paar Tipps für Sie zusammengestellt. Von langatmigen Thrillern bis hin zu preisgekrönten Dokumentarfilmen - hier ist etwas dabei, das Ihren Namen trägt.
- **CTA:** Mehr Plektren ansehen

## Schritt 4: Performance messen

Nach einigen Wochen prüft Camila die [Analytics]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/) ihrer [Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/), um zu beurteilen, wie gut die Strategie performt. 

Sie sieht:

- *Öffnungsrate:* 31%
- *Klickrate:* 15%
- *Konversionsrate* (gestarteter Stream innerhalb von 48 Stunden): 11%

Verglichen mit der alten Kampagne "Wir vermissen Sie" (bei der die Konversionsraten um die 3 % lagen), reduziert dieser neue Fluss die ABWANDERUNG VERRINGERN in der Zielgruppe um 28 %. Sie schaut sich den [Funnel-Bericht]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) an, um zu sehen, wo Nutzer:innen abspringen. Während die Öffnungs- und Klickraten gut sind, bemerkt sie eine leichte Reibung zwischen Klick und Konversion - was sie dazu veranlasst, CTA-Texte zu testen oder mit dem Layout zu experimentieren.

Um die langfristigen Auswirkungen zu verstehen, verfolgt Camila auch das Volumen der Nutzer:innen, die Woche für Woche in das Segment "Wahrscheinlich abwandern" eintreten. Dies hilft ihr, den Gesamtzustand des Lebenszyklus zu beurteilen und die Strategie der Bindung auf einer breiteren Ebene zu informieren. Schließlich besucht sie die Seite [Predictive Analytics]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) für ihre Prognose der Abwanderung, um die prognostizierten mit den tatsächlichen Abgewanderten zu vergleichen - eine nützliche Überprüfung, um sicherzustellen, dass das Modell die erwartete Performance erzielt.

Auf der Grundlage dieser Insights plant Camila A/B-Tests für Betreffzeilen, verschiedene Zeitfenster und Experimente mit Inhaltsformaten wie Empfehlungen im Karussell-Stil in einer In-App-Nachricht.

Mit Prognosen zur Abwanderung, intelligentem Timing und KI-gestützter Personalisierung reagiert das Team von Camila nicht nur auf die Abwanderung, sondern kommt ihr sogar zuvor. Und ihre Kampagne läuft leise im Hintergrund und erreicht die richtigen Leute zur richtigen Zeit mit Inhalten, die sie tatsächlich interessieren.
