---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Erfahren Sie, wie Sie auf BrazeAI Operator<sup>TM</sup> zugreifen und diesen nutzen können, einen in das Braze-Dashboard integrierten KI-gestützten Assistenten, einschließlich seiner Features und Best Practices."
---

# BrazeAI Operator

> BrazeAI Operator<sup>TM</sup> ist ein KI-gestützter Assistent, der in das Dashboard integriert ist. Operator unterstützt Sie bei der Erledigung Ihrer Aufgaben – beantwortet Fragen, führt Sie durch die Einrichtung, hilft bei der Fehlerbehebung und entwickelt gemeinsam mit Ihnen Ideen.

## Auf Operator zugreifen

Öffnen Sie Operator von jeder Seite im Braze-Dashboard aus.  

1. Wählen Sie **BrazeAI Operator<sup>TM</sup>** neben Ihrem Nutzerprofil aus.

![Das Symbol „BrazeAI Operator" neben einem Nutzerprofil.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2. Das Operator-Chat-Panel öffnet sich auf der rechten Seite des Bildschirms.

![Das Chat-Panel von Operator.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximieren Sie das Panel, um es für eine bessere Lesbarkeit zu vergrößern, oder minimieren Sie es, um Operator während der Arbeit verfügbar zu halten.  
{% endalert %} 

## Operator verwenden

Beschreiben Sie in natürlicher Sprache, was Sie erreichen möchten. Prompts können von einfachen Fragen bis hin zu komplexen Anfragen reichen:

- **Einfach:** Warum wird mein Liquid nicht gerendert?
- **Komplex:** Wie kann ich sicherstellen, dass der `abort_message`-Tag meiner Nachricht das Nutzerattribut enthält, das den Abbruch verursacht hat?

Operator kann Schritt-für-Schritt-Anleitungen, Links zur Braze-Dokumentation und Erklärungen in einfacher Sprache bereitstellen. Klare und spezifische Fragen führen zu hilfreicheren Antworten. Operator verwendet [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2), das über starke Schlussfolgerungsfähigkeiten verfügt und sich für komplexe, mehrstufige Aufgaben eignet. 

## Best Practices

Behandeln Sie Operator wie eine Konversation, nicht wie eine Suchmaschine. Kurze, natürliche Prompts funktionieren am besten.

- **Seien Sie konkret:** Anstelle von „Erzählen Sie mir etwas über Canvas" versuchen Sie es mit „Wie verwende ich Aktionspfade in Canvas?".  
- **Stellen Sie Folgefragen:** Sollte die erste Antwort Ihre Frage nicht vollständig beantworten, bitten Sie um eine Klarstellung oder um weitere Details.
- **Nutzen Sie den seitenbezogenen Kontext:** Operator erkennt Ihren Standort in Braze. Öffnen Sie Operator, während Sie die entsprechende Seite anzeigen, um die genauesten Ergebnisse zu erhalten.

## Passen Sie Ihr Erlebnis an

### Markenrichtlinien anwenden

Fügen Sie Markenrichtlinien als Kontext zu Operator-Abfragen hinzu, damit die Antworten dem Stil, Tonfall und der Persönlichkeit Ihrer Marke entsprechen. Operator nutzt die in Ihrem Workspace konfigurierten Markenrichtlinien, was dazu beiträgt, ein einheitliches Messaging zu gewährleisten, wenn er Texte vorschlägt oder Features erläutert.

Um Markenrichtlinien festzulegen, navigieren Sie zu **Einstellungen** > **Markenrichtlinien**. Weitere Informationen finden Sie unter [Markenrichtlinien]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

![Auswahl der Markenrichtlinien im Chat-Panel von Operator.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Seitenbezogenen Kontext nutzen

Operator erkennt automatisch Ihren Standort in Braze und passt die Antworten entsprechend an. Wenn Sie beispielsweise Operator während der Erstellung eines Canvas öffnen, kann er Ihnen relevante Schritte vorschlagen oder Anleitungen zu Canvas-Features geben, ohne dass Sie erklären müssen, an welcher Stelle Ihres Arbeitsablaufs Sie sich befinden.

Dank dieser Kontextbezogenheit können Sie kürzere, natürlichere Fragen stellen, wie beispielsweise „Wie füge ich eine Verzögerung hinzu?" anstelle von „Wie füge ich einen Verzögerungsschritt in einen Canvas-Workflow ein?"

## Arbeiten mit Operator-Antworten

### Starten Sie mit den vorgeschlagenen Prompts

Wenn Sie Operator öffnen, werden Ihnen auf Basis häufiger Aufgaben und Ihrer aktuellen Seite vorgeschlagene Prompts angezeigt. Wählen Sie einen aus, um schnell loszulegen, oder geben Sie Ihre eigene Frage ein.

### Verstehen Sie, wie Operator denkt

Operator zeigt seine Argumentationsschritte in ausblendbaren Abschnitten mit der Bezeichnung **„Reasoned"** an. Wählen Sie das Dropdown-Menü aus, um diese Abschnitte zu erweitern und nachzuvollziehen, wie Operator zu einer Antwort gelangt ist. Dies ist hilfreich, wenn Sie die Logik hinter einem Vorschlag verstehen oder den Ansatz überprüfen möchten.

![Das ausgeblendete Dropdown-Menü „Reasoned" in einer Antwort von Operator.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Aktionen mit Operator ausführen

Operator kann direkt im Braze-Dashboard Änderungen vorschlagen und ausführen, beispielsweise Formularfelder ausfüllen, Einstellungen aktualisieren oder Inhalte generieren. Jede vorgeschlagene Änderung wird Ihnen als Aktionskarte zur Überprüfung und Genehmigung vorgelegt, bevor sie wirksam wird. Weitere Informationen zur Funktionsweise finden Sie unter [Aktionen überprüfen]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/).

## Ihre Sitzung verwalten

### Eine Antwort stoppen

Während Operator eine Antwort generiert, wird der Button **Senden** zu einem Button **Stopp**. Wählen Sie **Stopp** aus, um die Antwort vorzeitig zu beenden, falls Sie Ihre Frage umformulieren müssen oder die Antwort in eine unerwünschte Richtung geht.

### Verlauf löschen

Um neu zu starten oder sensible Informationen aus der Unterhaltung zu entfernen, wählen Sie **Chat-Verlauf löschen**. Dadurch werden alle aktuellen Inhalte gelöscht und der Konversationskontext zurückgesetzt.

### Feedback geben

Verwenden Sie am Ende jeder Antwort die Daumen-hoch- oder Daumen-runter-Buttons, um schnelles Feedback zu geben. Ihr Feedback trägt dazu bei, die Antworten von Operator im Laufe der Zeit zu verbessern.

## Datenschutz und Sicherheit

### Konformität mit dem US-Gesetz zum Schutz medizinischer Daten (HIPAA)

Der KI-Operator nutzt eine Multi-Turn-Konversationstechnologie, die derzeit nicht für die Zero-Data-Retention-Richtlinie von OpenAI in Frage kommt. Der KI-Operator verwendet die modifizierte Richtlinie zur Überwachung von Missbrauch (Modified Abuse Monitoring) von OpenAI zur Datenspeicherung, fällt jedoch nicht unter die Business Associate Agreement (BAA) zwischen Braze und OpenAI. Nutzer:innen sollten den KI-Operator nicht auffordern, auf geschützte Gesundheitsdaten (Protected Health Information, PHI) zuzugreifen, die in Braze gespeichert sind, oder PHI anderweitig an dieses Feature zu übermitteln.

### Modellanbieter als Unterauftragsverarbeiter oder Drittanbieter

Wenn Sie eine Integration mit einem LLM-Anbieter nutzen, der von Braze über die Braze-Dienste bereitgestellt wird („von Braze bereitgestelltes LLM"), fungieren die Anbieter dieses von Braze bereitgestellten LLM als Unterauftragsverarbeiter von Braze, vorbehaltlich der Bestimmungen des Datenverarbeitungszusatzes (DPA) zwischen Ihnen und Braze. BrazeAI Operator<sup>TM</sup> verfügt über eine Integration mit OpenAI.

### Wie Daten mit OpenAI verwendet werden

Um KI-Ausgaben über BrazeAI-Features zu generieren, die OpenAI nutzen („Ausgabe"), übermittelt Braze bestimmte Informationen („Eingabe") an OpenAI. Die Eingabe umfasst Ihre Prompts, die im Dashboard angezeigten Inhalte und die für Ihre Anfragen relevanten Workspace-Daten. Gemäß [den Verpflichtungen der API-Plattform von OpenAI](https://openai.com/enterprise-privacy/) werden Daten, die über Braze an die API von OpenAI gesendet werden, nicht zum Trainieren oder Verbessern von OpenAI-Modellen verwendet. Zwischen Ihnen und Braze ist die Ausgabe Ihr geistiges Eigentum. Braze erhebt keine Ansprüche auf das Urheberrecht an solchen Ausgaben. Braze übernimmt keinerlei Gewährleistung in Bezug auf KI-generierte Inhalte, einschließlich der Ausgabe.

## Nächste Schritte

- [Aktionen überprüfen]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/): Erfahren Sie, wie Sie die von Operator vorgeschlagenen Änderungen überprüfen und genehmigen können.
- [Support-Tickets einreichen]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets/): Reichen Sie Support-Tickets direkt über Operator ein.
- [Fehlerbehebung]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/): Häufige Probleme und Lösungen