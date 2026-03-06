---
nav_title: Erste Schritte
article_title: Erste Schritte mit BrazeAI Operator<sup>TM</sup>
page_order: 1
description: "Erfahren Sie, wie Sie auf BrazeAI Operator<sup>TM</sup> zugreifen und ihn nutzen – Brazes KI-Assistent im Dashboard – inkl. Funktionen und Best Practices."
---

# Erste Schritte mit BrazeAI Operator

> Erfahren Sie, wie Sie auf BrazeAI Operator<sup>TM</sup> zugreifen und ihn nutzen – Ihren KI-Assistenten im Dashboard – inkl. Funktionen und Best Practices.

## Operator öffnen

Öffnen Sie Operator von jeder Seite im Braze-Dashboard aus.

1. Wählen Sie **BrazeAI Operator<sup>TM</sup>** neben Ihrem Benutzerprofil.

![Das BrazeAI-Operator-Symbol neben einem Benutzerprofil.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2. Das Operator-Chat-Panel öffnet sich auf der rechten Seite des Bildschirms.

![Das Operator-Chat-Panel.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximieren Sie das Panel für bessere Lesbarkeit oder minimieren Sie es, um Operator beim Arbeiten verfügbar zu halten.
{% endalert %}

## Operator nutzen

Beschreiben Sie in natürlicher Sprache, was Sie erreichen möchten. Die Eingaben können von einfachen Fragen bis zu komplexen Anfragen reichen:

- **Einfach:** Warum wird mein Liquid nicht gerendert?
- **Komplex:** Wie kann ich das `abort_message`-Tag meiner Nachricht so einrichten, dass es das Benutzerattribut enthält, das den Abbruch ausgelöst hat?

Operator kann Schritt-für-Schritt-Anleitungen, Links zur Braze-Dokumentation und verständliche Erklärungen liefern. Klare und konkrete Fragen führen zu hilfreicheren Antworten. Operator nutzt [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2), das starke Argumentation bietet und sich für komplexe, mehrstufige Aufgaben eignet.

## Best Practices

Behandeln Sie Operator wie ein Gespräch, nicht wie eine Suchmaschine. Kurze, natürliche Eingaben funktionieren am besten.

- **Seien Sie konkret:** Statt „Erzähl mir von Canvas“ fragen Sie z. B. „Wie nutze ich Aktionspfade in Canvas?“.
- **Stellen Sie Rückfragen:** Wenn die erste Antwort Ihren Bedarf nicht deckt, fragen Sie nach oder bitten Sie um Details.
- **Nutzen Sie den seitenabhängigen Kontext:** Operator erkennt, wo Sie sich in Braze befinden. Öffnen Sie Operator auf der passenden Seite für die genauesten Ergebnisse.

## Ihr Erlebnis anpassen

### Markenrichtlinien anwenden

Fügen Sie Markenrichtlinien als Kontext zu Operator-Anfragen hinzu, damit Antworten zu Stimme, Ton und Persönlichkeit Ihrer Marke passen. Operator nutzt die in Ihrem Workspace konfigurierten Markenrichtlinien, was für einheitliche Ansprache sorgt, wenn er Texte vorschlägt oder Funktionen erklärt.

Um Markenrichtlinien einzurichten, gehen Sie zu **Einstellungen** > **Markenrichtlinien**. Weitere Informationen finden Sie unter [Markenrichtlinien]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

![Auswahl der Markenrichtlinien im Operator-Chat-Panel.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Seitenabhängigen Kontext nutzen

Operator erkennt automatisch Ihren Standort in Braze und passt Antworten daran an. Wenn Sie z. B. Operator beim Erstellen eines Canvas öffnen, kann er passende Schritte vorschlagen oder Canvas-Funktionen erklären, ohne dass Sie Ihren Arbeitsstand beschreiben müssen.

So können Sie kürzere, natürlichere Fragen stellen wie „Wie füge ich eine Verzögerung ein?“ statt „Wie füge ich einen Verzögerungsschritt in einen Canvas-Workflow ein?“.

## Mit Operator-Antworten arbeiten

### Mit vorgeschlagenen Eingaben starten

Beim Öffnen von Operator erscheinen Vorschläge basierend auf häufigen Aufgaben und Ihrer aktuellen Seite. Wählen Sie einen zum schnellen Einstieg oder tippen Sie Ihre eigene Frage.

### Nachvollziehen, wie Operator denkt

Operator zeigt seine Überlegungen in ausklappbaren Bereichen mit der Bezeichnung **Reasoned**. Öffnen Sie die Dropdown-Liste, um diese Bereiche zu erweitern und zu sehen, wie Operator zu einer Antwort gelangt ist.

![Die eingeklappte „Reasoned“-Dropdown-Liste in einer Operator-Antwort.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Mit Operator Aktionen ausführen

Operator kann Änderungen direkt im Braze-Dashboard vorschlagen und ausführen, z. B. Formularfelder ausfüllen, Einstellungen anpassen oder Inhalte erzeugen. Jede vorgeschlagene Änderung wird als Aktionskarte zur Prüfung und Freigabe angezeigt. Mehr dazu unter [Aktionen prüfen]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/).

## Ihre Sitzung verwalten

### Eine Antwort beenden

Während Operator eine Antwort erzeugt, wird die Schaltfläche **Senden** zu **Stopp**. Wählen Sie **Stopp**, um die Antwort vorzeitig zu beenden, wenn Sie die Frage umformulieren möchten oder die Antwort in die falsche Richtung geht.

### Verlauf löschen

Um neu zu starten oder sensible Informationen aus dem Gespräch zu entfernen, wählen Sie **Chatverlauf löschen**. Dadurch wird der aktuelle Inhalt gelöscht und der Gesprächskontext zurückgesetzt.

### Feedback geben

Nutzen Sie die Daumen-hoch- oder Daumen-runter-Schaltflächen unter jeder Antwort für schnelles Feedback. Ihr Feedback hilft, die Antworten von Operator zu verbessern.

## Nächste Schritte

- [Aktionen prüfen]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/) – So prüfen und genehmigen Sie von Operator vorgeschlagene Änderungen
- [Fehlerbehebung]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/) – Häufige Probleme und Lösungen
