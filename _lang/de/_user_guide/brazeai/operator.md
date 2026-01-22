---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 0.7
alias: /operator/
description: "Dieser referenzierte Artikel behandelt BrazeAI Operator, einen KI-gestützten Assistenten, der in das Braze-Dashboard integriert ist."
---

# <sup>BrazeAITM</sup> Operator

> <sup>BrazeAITM</sup> Operator ist ein KI-gestützter Assistent, der in das Braze-Dashboard integriert ist. Operator hilft Ihnen, Antworten zu finden, Fehlerbehebungen vorzunehmen und Best Practices zu erlernen, ohne Ihren Arbeitsablauf zu verlassen.

{% alert important %}
<sup>BrazeAITM</sup> Operator befindet sich derzeit in einer privaten Beta-Phase mit eingeschränkter Funktionalität. Wenn Sie Hilfe benötigen, wenden Sie sich an Ihren Customer-Success-Manager:in.
{% endalert %}

## Über Operator

Operator ist Ihr eingebauter KI-Assistent im Braze-Dashboard. Es hilft Ihnen, schneller voranzukommen, indem es Fragen beantwortet, nächste Schritte vorschlägt und Sie durch Aufgaben führt - und das alles, ohne Ihren Arbeitsablauf zu verlassen.

Während der Beta-Phase unterstützt Operator nur den **Fragemodus**. Sie können:

- Antworten aus der Braze Dokumentation erhalten
- Fehlerbehebung mit [seitenorientiertem Kontext](#page-aware-context)
- Lernangebote und Anleitung zum Onboarding

## Wie Sie Operator aufrufen

Sie können Operator von jeder Seite des Braze-Dashboards aus öffnen.  

1. Wählen Sie **<sup>BrazeAITM</sup> Operator**, neben Ihrem Nutzerprofil.

\![Das BrazeAI Operator Symbol neben einem Nutzerprofil.]({% image_buster /assets/img/operator/operator_profile.png %}){:style="max-width:60%"}

{: start="2"}
2\. Das Operator Chat Panel wird auf der rechten Seite des Bildschirms geöffnet.

\![Das Chat Panel für Operator.]({% image_buster /assets/img/operator/operator_panel.png %})

{% alert tip %}
Versuchen Sie, das Panel zu maximieren, um es besser lesen zu können, oder zu minimieren, damit Operator weiterhin verfügbar ist, während Sie weiterarbeiten.  
{% endalert %}

## Wie man mit Operator spricht

Verwenden Sie Eingabeaufforderungen, um mit dem Operator zu kommunizieren. Am besten sprechen Sie ganz natürlich, so wie Sie es mit einem Kollegen oder einem Freund tun würden. Ihre Eingabeaufforderungen können von einfachen Fragen bis hin zu komplexen Anfragen reichen:

- **Einfach:** Wie kann ich sicherstellen, dass Nutzer:innen keine E-Mails zum abgebrochenen Einkauf erhalten, während sie sich noch auf der Website befinden?
- **Komplex:** Wie kann ich das Attribut des Nutzers:innen, der den Abbruch verursacht hat, in den Tag `abort_message` meiner Nachricht aufnehmen?

Operator kann Schritt-für-Schritt-Anleitungen, Links zu Braze-Dokumenten und Erklärungen in einfacher Sprache bereitstellen. Je klarer und spezifischer Ihre Frage ist, desto nützlicher wird die Antwort sein. 

### Bewährte Praktiken

Betrachten Sie Operator als ein Gespräch, nicht als eine Suchmaschine. Kurze, natürliche Souffleure funktionieren in der Regel am besten.

- **Seien Sie konkret:** Versuchen Sie anstelle von "Erzählen Sie mir von Canvas" lieber "Wie verwende ich Aktions-Pfade in Canvas?".  
- **Verwenden Sie Nachfassaktionen:** Wenn die erste Antwort nicht das ist, was Sie brauchen, stellen Sie klärende Fragen. Der Operator kann die Antworten verfeinern.
- **Verlassen Sie sich auf den Kontext:** Operator weiß, auf welcher Seite Sie sich in Braze befinden. Öffnen Sie Operator, während Sie sich auf der Seite befinden, mit der Sie arbeiten, um die wichtigsten Ergebnisse zu erhalten.

## Features

Operator enthält während der Beta-Phase die folgenden Features:

### Seitenbezogener Kontext

Operator versteht die Seite, an der Sie gerade in Braze arbeiten, und kann die Antworten auf der Grundlage dieses Kontexts anpassen. Wenn Sie zum Beispiel Operator öffnen, während Sie ein Canvas erstellen, kann er Ihnen für das Canvas relevante Schritte vorschlagen oder Anleitungen geben, ohne dass Sie erklären müssen, wo Sie sich befinden. 

### Vorgeschlagene Souffleure

Wenn Sie Operator öffnen, sehen Sie ein paar Vorschläge, die Ihnen den Einstieg erleichtern. Wählen Sie eine aus, um loszulegen, oder geben Sie Ihre eigene Frage ein.

### Argumentation anzeigen

Operator zeigt seine Argumentationsschritte in zusammenklappbaren Abschnitten mit der Bezeichnung **Reasoned** an. Wählen Sie die Dropdown-Liste aus, um diese Abschnitte zu erweitern und zu sehen, wie Operator zu einer Antwort gekommen ist.

\![Dropdown für "Begründet" erweitert mit mehr Details zur Antwort des Operators.]({% image_buster /assets/img/operator/operator_reasoning.png %}){:style="max-width:60%"}

### Vorgeschlagene Aktionen

In einigen Fällen wird Operator die nächsten Schritte empfehlen und direkte Links zu den entsprechenden Seiten in Ihrem Braze-Dashboard bereitstellen. Wenn Sie beispielsweise nach den Absprungraten von E-Mails fragen, kann Operator Sie auf die Seite Ihres **Zustellbarkeits-Centers** verweisen. Diese Verknüpfungen helfen Ihnen, schneller zu handeln, ohne dass Sie manuell navigieren müssen.

### Erzeugung stoppen

Während der Operator eine Antwort generiert, wird der Button **Senden** zu einem **Stop** Button. Wenn Sie die Antwort vorzeitig beenden möchten, wählen Sie **Stopp**.

### Löschen des Chatverlaufs

Um Ihre Unterhaltung zurückzusetzen, wählen Sie **Chat-Verlauf löschen**. Dadurch wird der aktuelle Inhalt entfernt, so dass Sie neu beginnen können.

### Maximieren und Minimieren des Panels

Sie können den Button **Maximieren** verwenden, um Operator zur besseren Lesbarkeit zu erweitern, oder den Button **Minimieren**, um das Panel zu verstecken, während Sie in Braze weiterarbeiten.

### Feedback senden

Verwenden Sie die Buttons "Daumen hoch" oder "Daumen runter" am Ende jeder Antwort, um schnelles Feedback zu geben. Dies hilft, die Antworten von Operator zu verbessern.

## Fehlersuche

| Fehler | Fehlersuche |
| --- | --- |
| Keine Antwort | Versuchen Sie, die Seite zu aktualisieren und das Operator Panel erneut zu öffnen. |
| Off-Topic-Antworten | Formulieren Sie Ihre Frage etwas genauer um. Nennen Sie das Feature oder den Workflow, nach dem Sie fragen. |
| Fehlermeldungen | Wenn Operator keine Inhalte streamen kann, sehen Sie möglicherweise die Aufforderung "Erneut versuchen". Der Operator ist möglicherweise vorübergehend nicht verfügbar oder Ihre Verbindung wurde unterbrochen. Versuchen Sie es nach ein paar Minuten erneut. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Beschränkungen

Operator wurde entwickelt, um Ihnen bei der Navigation in Braze zu helfen und Ihre Arbeit effizienter zu gestalten, aber es gibt einige Stromgrenzen, die Sie beachten müssen:

### Kein Zugriff auf Ihre Daten

Während Operator auf den Kontext Ihrer Arbeit in Braze zugreifen kann, kann Operator die in Braze gespeicherten Daten Ihres Unternehmens weder abfragen noch Antworten liefern. Es **kann zum Beispiel nicht** auf Anfragen wie diese reagieren:

- "Geben Sie mir eine Liste aller meiner E-Mail Kampagnen vom letzten Jahr."
- "Zeigen Sie mir, welche Segmente im letzten Quartal das höchste Engagement hatten."
- "Analysieren Sie meine Canvas Performance und schlagen Sie Verbesserungen vor."

### Beta-Stabilität

Da es sich um eine private Beta-Version handelt, kann Operator gelegentlich Fehler, Unterbrechungen oder unvollständige Features aufweisen.

Wenn Sie sich nicht sicher sind, ob eine Frage unterstützt wird, versuchen Sie, sie so zu formulieren, dass Operator Ihnen bei der Navigation oder der Durchführung von Aktionen innerhalb des Braze-Dashboards helfen kann, anstatt Daten aus Analytics oder historischen Daten abzurufen.
