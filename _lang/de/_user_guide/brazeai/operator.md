---
nav_title: Operator
article_title: BrazeAI-Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Erfahren Sie, wie Sie auf BrazeAI Operator<sup>TM</sup> zugreifen und diesen nutzen können, einen in das Braze-Dashboard integrierten KI-gestützten Assistenten, einschließlich seiner Features und bewährten Verfahren."
---

# BrazeAI-Operator

> BrazeAI Operator<sup>TM</sup> ist ein KI-gestützter Assistent, der in das Dashboard integriert ist. Der Operator unterstützt Sie bei der Erledigung Ihrer Aufgaben – er beantwortet Ihre Fragen, führt Sie durch die Einrichtung, übernimmt die Fehlerbehebung und entwickelt gemeinsam mit Ihnen Ideen.

## Access Operator

Öffnen Sie Operator von jeder Seite im Braze-Dashboard aus.  

1. Bitte wählen Sie **BrazeAI Operator<sup>TM</sup>** neben Ihrem Nutzerprofil aus.

![Das Symbol „BrazeAI Operator“ neben einem Nutzerprofil.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2\. Das Operator-Chat-Panel öffnet sich auf der rechten Seite des Bildschirms.

![Das Chat-Panel des Operators.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximieren Sie das Panel, um es für eine bessere Lesbarkeit zu vergrößern, oder minimieren Sie es, um Operator während der Arbeit verfügbar zu halten.  
{% endalert %} 

## Operator verwenden

Bitte beschreiben Sie in natürlicher Sprache, was Sie erreichen möchten. Aufforderungen können von einfachen Fragen bis hin zu komplexen Anfragen reichen:

- **Einfach:** Warum wird mein Liquid nicht gerendert?
- **Komplex:** Wie kann ich sicherstellen, dass der`abort_message`Tag meiner Nachricht das Attribut des Nutzers enthält, das den Abbruch verursacht hat?

Der Operator kann Schritt-für-Schritt-Anleitungen, Links zur Braze-Dokumentation und Erklärungen in einfacher Sprache bereitstellen. Klare und spezifische Fragen führen zu hilfreicheren Antworten. Der Operator verwendet [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2), das über starke Schlussfolgerungsfähigkeiten verfügt und sich für komplexe, mehrstufige Aufgaben eignet. 

## Bewährte Praktiken

Behandeln Sie den Operator wie eine Konversation, nicht wie eine Suchmaschine. Kurze, natürliche Aufforderungen sind am effektivsten.

- **Bitte seien Sie konkret:** Anstelle von „Bitte informieren Sie mich über Canvas“ versuchen Sie es mit „Wie verwende ich Aktions-Pfade in Canvas?“.  
- **Stellen Sie Folgefragen:** Sollte die erste Antwort Ihre Frage nicht vollständig beantworten, bitten Sie um eine Klarstellung oder um weitere Informationen.
- **Verwenden Sie den seitenbezogenen Kontext:** Der Operator erkennt Ihren Standort in Braze. Bitte öffnen Sie Operator, während Sie die entsprechende Seite anzeigen, um die genauesten Ergebnisse zu erhalten.

## Passen Sie Ihr Kundenerlebnis an

### Markenrichtlinien anwenden

Fügen Sie Markenrichtlinien als Kontext zu Operator-Abfragen hinzu, damit die Antworten dem Stil, Tonfall und der Persönlichkeit Ihrer Marke entsprechen. Der Operator nutzt die in Ihrer Workspace konfigurierten Markenrichtlinien, was dazu beiträgt, ein einheitliches Messaging zu gewährleisten, wenn er Texte vorschlägt oder Features erläutert.

Um Markenrichtlinien festzulegen, navigieren Sie bitte zu **Einstellungen** > **Markenrichtlinien**. Weitere Informationen finden Sie in [den Markenrichtlinien]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

![Auswahl der Markenrichtlinien im Chat-Panel des Operators.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Seitenbezogenen Kontext nutzen

Der Operator erkennt automatisch Ihren Standort in Braze und passt die Antworten entsprechend diesem Kontext an. Wenn Sie beispielsweise Operator während der Erstellung eines Canvas öffnen, kann es Ihnen relevante Schritte vorschlagen oder Ihnen Anleitungen zu den Canvas-Features geben, ohne dass Sie erklären müssen, an welcher Stelle Ihres Arbeitsablaufs Sie sich befinden.

Dank dieser Kontextbezogenheit können Sie kürzere, natürlichere Fragen stellen, wie beispielsweise „Wie füge ich eine Verzögerung hinzu?“ anstelle von „Wie füge ich einen Verzögerungsschritt in einen Canvas-Workflow ein?“

## Arbeiten mit Antworten des Operators

### Beginnen Sie mit den vorgeschlagenen Eingabeaufforderungen

Bei der Öffnung von Operator werden Ihnen auf der Grundlage häufiger Aufgaben und Ihrer aktuellen Seite vorgeschlagene Eingabeaufforderungen angezeigt. Bitte wählen Sie eine Option aus, um schnell zu beginnen, oder geben Sie Ihre eigene angepasste Frage ein.

### Verstehen Sie, wie Operator denkt

Der Operator zeigt seine Argumentationsschritte in ausblendbaren Abschnitten mit der Bezeichnung **„Begründet“** an. Bitte wählen Sie das Dropdown-Menü aus, um diese Abschnitte zu erweitern und zu erfahren, wie der Operator zu einer Antwort gelangt ist. Dies ist hilfreich, wenn Sie die Logik hinter einem Vorschlag verstehen oder den Ansatz überprüfen möchten.

![Das ausgeblendete Dropdown-Menü „Begründet“ in einer Antwort des Operators.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Bitte ergreifen Sie Maßnahmen mit dem Operator.

Der Operator kann direkt im Braze-Dashboard Änderungen vorschlagen und ausführen, beispielsweise Formularfelder ausfüllen, Einstellungen aktualisieren oder Inhalte generieren. Jede vorgeschlagene Änderung wird Ihnen in Form einer Aktionskarte zur Überprüfung und Genehmigung vorgelegt, bevor sie in Kraft tritt. Weitere Informationen zur Funktionsweise finden Sie unter [Überprüfen von Aktionen]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/).

## Verwalten Sie Ihre Sitzung

### Eine Antwort unterbrechen

Während Operator eine Antwort generiert, wird der Button **„Senden“** zu einem Button **„Stopp**“. Auswählen Sie **„Beenden“,** um die Antwort vorzeitig zu beenden, falls Sie Ihre Frage umformulieren müssen oder die Antwort in eine unerwünschte Richtung geht.

### Bitte löschen Sie Ihren Verlauf.

Um einen Neuanfang zu machen oder sensible Informationen aus der Unterhaltung zu entfernen, wählen Sie **bitte „Chat-Verlauf löschen**“. Dadurch werden alle aktuellen Inhalte gelöscht und der Konversationskontext zurückgesetzt.

### Bitte geben Sie uns Ihr Feedback

Bitte verwenden Sie am Ende jeder Antwort die Daumen-hoch- oder Daumen-runter-Buttons, um ein kurzes Feedback zu geben. Ihr Feedback trägt dazu bei, die Antworten des Operators im Laufe der Zeit zu verbessern.

## Datenschutz und -sicherheit

### HIPAA-Konformität

KI-Operator nutzt eine Multi-Turn-Konversationstechnologie, die derzeit nicht für die Zero-Data-Retention-Richtlinie von OpenAI in Frage kommt. AI Operator verwendet die modifizierte Richtlinie zur Bindung der Daten von OpenAI zur Überwachung von Missbrauch, jedoch fällt AI Operator nicht unter die Business Associate Agreement (BAA) zwischen Braze und OpenAI. Nutzer:innen sollten den KI-Operator nicht auffordern, auf geschützte Gesundheitsdaten (Protected Health Information, PHI) zuzugreifen, die in Braze gespeichert sind, oder PHI anderweitig an dieses Feature zu übermitteln.

### Modellanbieter als Unterauftragsverarbeiter oder Drittanbieter

Wenn Sie eine Integration mit einem LLM-Anbieter nutzen, der von Braze über die Braze-Serviceleistungen bereitgestellt wird („von Braze bereitgestelltes LLM“), fungieren die Anbieter dieses von Braze bereitgestellten LLM als Unterauftragsverarbeiter von Braze, vorbehaltlich der Bestimmungen des Datenverarbeitungszusatzes (DPA) zwischen Ihnen und Braze. BrazeAI Operator<sup>TM</sup> verfügt über eine Integration mit OpenAI.

### Wie Daten mit OpenAI verwendet werden

Um KI-Ergebnisse über Braze AI-Features zu generieren, die OpenAI nutzen („Ergebnisse“), übermittelt Braze bestimmte Informationen („Eingaben“) an OpenAI. Die Eingabe umfasst Ihre Eingabeaufforderungen, die im Dashboard angezeigten Inhalte und die für Ihre Anfragen relevanten Daten des Workspaces. Gemäß [den Verpflichtungen der API-Plattform von OpenAI](https://openai.com/enterprise-privacy/) werden Daten, die über Braze an die API von OpenAI gesendet werden, nicht zum Trainieren oder Verbessern von OpenAI-Modellen verwendet. Zwischen Ihnen und Braze ist der Output Ihre geistige Eigenschaft. Braze erhebt keine Ansprüche auf das Urheberrecht an solchen Ausgaben. Braze übernimmt keinerlei Gewährleistung in Bezug auf KI-generierte Inhalte, einschließlich der Ausgabe.

## Nächste Schritte

- [Überprüfung von Maßnahmen]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/): Erfahren Sie, wie Sie die vom Operator vorgeschlagenen Änderungen überprüfen und genehmigen können.
- [Fehlerbehebung]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/): Häufige Probleme und Lösungen
