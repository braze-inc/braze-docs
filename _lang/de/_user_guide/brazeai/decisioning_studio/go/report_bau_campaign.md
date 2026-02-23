---
nav_title: Bericht über die BAU-Kampagne
article_title: Berichterstattung über die BAU-Kampagne
page_order: 10
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zur Berichterstattung über eine Business as Usual (BAU) Kampagne im BrazeAI Decisioning Studio Go Portal."
---

# Berichterstattung über die Business as Usual Kampagne

> Dieser Artikel enthält Antworten auf häufig gestellte Fragen zur Berichterstattung über eine Business as Usual (BAU) Kampagne im BrazeAI Decisioning Studio™ Go Portal.

## Über die Berichterstattung zur BAU-Kampagne

Standardmäßig vergleicht der BrazeAI Decisioning Studio™ Go-Portalbericht die BrazeAI Decisioning Studio™ Go- und die zufällige Kontrollgruppe. Zusätzlich zum Vergleich dieser beiden Gruppen haben Sie vielleicht eine "Business as Usual"-Gruppe (auch bekannt als BAU), mit der Sie die Performance von BrazeAI Decisioning Studio™ Go vergleichen möchten. Wenn Sie BAU-Berichte einrichten, können Sie die Performance aller drei Gruppen an einem einzigen Ort im BrazeAI Decisioning Studio™ Go-Portal einsehen.

Der Hauptvorteil der BAU-Berichterstellung ist die Anwendung des Filters für ungültige Klicks von BrazeAI Decisioning Studio™ Go, der, wenn er auf alle drei Versuchsgruppen angewandt wird, den genauesten und fairsten (oder "Äpfel zu Äpfeln") Vergleich der Klick-Performance ermöglicht, indem er jegliches zusätzliche Rauschen von mutmaßlichen Maschinenklicks und Klicks auf den Abmelde-Link entfernt.

## Anforderungen

Bevor Sie die BAU-Berichterstattung einrichten, stellen Sie zunächst sicher, dass es einen Vergleich zwischen der BAU-Behandlungsgruppe, dem BrazeAI Decisioning Studio™ Go und der zufälligen Kontrollgruppe gibt, bei dem Äpfel mit Äpfeln verglichen werden. Dazu gehört die Überprüfung, ob:

- Kein Empfänger:innen kann zu mehr als einer Gruppe gehören (für die gesamte Dauer des Experiments).
- Die Empfänger:innen werden nach dem Zufallsprinzip den Gruppen zugewiesen, so dass es keine Verzerrungen bei der Gruppenzuweisung gibt.
- Alle Optionen, die der BAU-Gruppe zur Verfügung stehen (Kreativität, Häufigkeit, Zeit, Anreiz oder Angebot), stehen auch dem BrazeAI Decisioning Studio™ Go und der zufälligen Kontrollgruppe zur Verfügung.

Ohne ein "Äpfel mit Äpfeln"-Experiment kann die BAU-Berichterstattung verwirrend oder irreführend sein.

Nachdem Sie Ihren Versuchsplan validiert haben, sind die folgenden Angaben erforderlich, um die BAU-Berichterstattung einzurichten:
- Eine oder mehrere IDs für Kampagnen von Ihrer integrierten Aktivierungsplattform (Braze, Salesforce Marketing Cloud oder Klaviyo), wobei alle Mitteilungen in der Kampagne BAU-Mitteilungen sind
    - Für Braze werden Kampagnen und Canvase akzeptiert
    - Für Salesforce Marketing Cloud werden nur Journeys akzeptiert.
    - Für Klaviyo werden nur Flows akzeptiert
- Eine ID von Ihrer integrierten Aktivierungsplattform, die die Empfänger:innen der BAU-Zielgruppe täglich trackt
    - Für Braze werden nur Segmente akzeptiert.
    - Für Salesforce Marketing Cloud werden nur Datenerweiterungen akzeptiert.
    - Für Klaviyo werden nur Segmente akzeptiert

Wenn Sie keine bestehende Zielgruppe haben, die Ihr BAU-Publikum trackt, müssen Sie eine erstellen.

{% alert note %}
**Nur für Kund:innen von Braze:** Stellen Sie sicher, dass Ihr Braze-Currents-Export in BrazeAI Decisioning Studio™ Go Daten aus Ihren BAU-Kampagnen enthält.
{% endalert %}

## Überlegungen

Ähnlich wie bei BrazeAI Decisioning Studio™ Go deckt das BAU-Reporting nur Klick-KPIs ab, nicht aber Konversions-KPIs.

Derzeit unterstützen wir das Filtern nach bestimmten Canvas-Schritt IDs noch nicht. Ereignisse aus allen Canvas-Schritten werden in die BAU-Daten aufgenommen. Beachten Sie, dass dadurch Vergleiche mit BAU ungültig werden können, wenn nur bestimmte Canvas-Schritte berücksichtigt werden sollen.

## Einrichten einer BAU-Kampagne 

Folgen Sie den Anweisungen in Ihrem BrazeAI Decisioning Studio™ Go Portal. Sie müssen über eine oder mehrere [Kampagnen IDs und eine Zielgruppe ID](#what-are-the-requirements-to-use-in-portal-bau-reporting) verfügen.