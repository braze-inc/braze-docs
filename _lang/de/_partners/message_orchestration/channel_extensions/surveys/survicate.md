---
nav_title: Survicate
article_title: Survicate
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Survicate, einer Plattform für Kundenfeedback, die Ihnen hilft, Kundeneinblicke über mehrere Kanäle und während der gesamten User Journey zu sammeln, zu analysieren und zu nutzen."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

![Ein Beispiel dafür, wie eine eingebettete HTML-Umfrage (erste Frage) in einer Braze-E-Mail aussehen könnte.][2]{: style="float:right;max-width:40%;border:0; margin-left:8px;"}

> [Survicate][1] ist eine Plattform für Kundenfeedback, die Ihnen hilft, Kundeneinblicke über mehrere Kanäle und während der gesamten User Journey zu sammeln, zu analysieren und zu nutzen.  

Mit der Integration von Braze und Survicate können Sie Umfragen direkt in Ihre Braze-E-Mails einbetten, um die Antwortraten zu erhöhen. Umfrageantworten werden automatisch mit Braze-Benutzerprofilen als benutzerdefinierte Attribute oder Ereignisse synchronisiert. Einblicke in Echtzeit machen es einfach, das Feedback zusammen mit den Kundendaten zu verfolgen und zu analysieren und gezielte Nachfassaktionen zu erstellen.

## Anwendungsfälle

Braze und Survicate arbeiten zusammen, um eine Reihe von Feedback-Anwendungsfällen abzudecken, die Ihnen helfen, verwertbare Erkenntnisse zu sammeln und das Kundenerlebnis zu verbessern:

- Messen Sie die Kundenzufriedenheit (wie CSAT, NPS oder CES)
- Sammeln Sie Produkt-Feedback
- Führen Sie Benutzer- oder Marktforschung durch
- Sammeln Sie Erkenntnisse in kritischen Phasen der Customer Journey
- Lösen Sie personalisierte Workflows aus und automatisieren Sie Folgekampagnen auf der Grundlage von Kundenfeedback.

## Hauptmerkmale der Integration

Die Integration von Survicate und Braze bietet einen Datenabgleich in Echtzeit, so dass die aktuellsten Informationen aus Survicate-Umfragen sofort in Braze verfügbar sind. Auf der Grundlage der Umfrageantworten können Sie diese Daten nutzen, um zeitnahe, personalisierte Maßnahmen zu ergreifen.

- **Senden Sie Umfrageantworten als benutzerdefinierte Benutzerattribute an Braze**: Reichern Sie Braze-Benutzerprofile mit Daten aus Umfrageantworten an.
- **Lösen Sie benutzerdefinierte Ereignisse in Braze aus**: Nutzen Sie Ereignisse, die auf Umfrageantworten basieren, um bestimmte Gruppen anzusprechen oder Folgekampagnen zu initiieren.
- **Erstellen Sie detaillierte Segmente**: Erstellen Sie Braze-Segmente mit Daten aus Survicate-Umfragen, um Ihre Ansprache weiter zu personalisieren.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Survicate-Konto | Sie benötigen ein Survicate-Konto, um diese Integration zu aktivieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie Ihre Umfrage in Survicate

1. Wählen Sie in Ihrem Survicate-Panel die Option **Neue Umfrage erstellen**.
2. Wählen Sie Ihren Umfragekanal: E-Mail**, Link, Website, produktinterne Umfragen und Umfragen über eine mobile App** sind möglich. 
3. Entwerfen Sie Ihre Umfrage von Grund auf neu, verwenden Sie den AI Survey Creator oder wählen Sie aus über 100 fertigen Vorlagen.

![Vier Optionen für die Erstellung einer Umfrage: von Grund auf neu beginnen, eine Vorlage verwenden, KI-unterstützte Erstellung und Fragen importieren.][4]

### Schritt 2: Identifizieren Sie die Befragten automatisch mit Braze-E-Mails

1. Nachdem Ihre Umfrage fertig ist, gehen Sie auf die Registerkarte **Konfigurieren**.
2. Wählen Sie für *Befragte identifizieren mit* die Option **Hartlöten**. Dadurch werden die Antworten automatisch mit Ihren Braze-Kundenprofilen verknüpft, so dass Sie in Ihrer Umfrage nicht mehr nach den Kontaktdaten fragen müssen.

![Braze wird als Befragter ausgewählt.][5]

### Schritt 3: Verbinden Sie die Integration

1. Suchen Sie dann auf der **Registerkarte Verbinden** nach Braze und wählen Sie Zur Integration **verbinden**. 
2. Geben Sie Ihren Braze-Konto-Workspace-API-Schlüssel und die Braze-Instanz-URL ein.

![Felder zur Eingabe des Arbeitsbereich-API-Schlüssels und der Braze-Instanz-URL.][3]

### Schritt 4: Teilen Sie Ihre Umfrage

1. Wählen Sie dann auf der Registerkarte **Teilen**, wo Sie Ihre Umfrage platzieren möchten. Die Optionen umfassen:
- **Direkter Link**: Kopieren Sie den Link, um ihn in Braze als Schaltfläche oder Hyperlink zu verwenden.
- **Die erste Frage einbetten**: Kopieren Sie den HTML-Code, um die erste Umfragefrage direkt in eine Braze-E-Mail einzubetten.
- **Starten Sie eine Umfrage auf Ihrer Website oder in einem Produkt**: Installieren Sie den Tracking-Code einmal und schalten Sie die Umfragen direkt über das Survicate-Panel live.

### Schritt 5: Fügen Sie die Umfrage zu Ihrer Braze E-Mail-Kampagne hinzu

1. In Braze fügen Sie den Umfragelink oder den HTML-Code in den Inhalt Ihrer E-Mail-Kampagne ein.
2. Beginnen Sie mit dem Sammeln von Feedback und verfolgen Sie die Antworten direkt in Survicate.


[1]: https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter
[2]:  {% image_buster /assets/img/survicate/survicate_asset_1.png %}
[3]:  {% image_buster /assets/img/survicate/image1.png %}
[4]:  {% image_buster /assets/img/survicate/survicate_asset_3.png %}
[5]:  {% image_buster /assets/img/survicate/survicate_asset_2.png %}
