---
nav_title: Agenten erstellen
article_title: Angepasste Agenten erstellen
description: "Erfahren Sie, wie Sie Agenten erstellen, was Sie vorbereiten müssen und wie Sie sie in den Bereichen Messaging, Entscheidungsfindung und Datenverwaltung einsetzen können."
page_order: 1
alias: /creating-agents/
---

# Angepasste Agenten erstellen

> Erfahren Sie, wie Sie angepasste Agenten erstellen, was Sie vorbereiten müssen und wie Sie sie in den Bereichen Messaging, Entscheidungsfindung und Daten-Management einsetzen können. Weitere allgemeine Informationen finden Sie unter [Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents). 

{% alert important %}
Braze-Agenten befinden sich derzeit in der Beta-Phase. Wenn Sie Hilfe benötigen, wenden Sie sich an Ihren Customer-Success-Manager:in.
{% endalert %}

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

- Zugriff auf die **Agentenkonsole** in Ihrem Workspace. Wenden Sie sich an Ihre Braze-Administratoren, wenn Sie diese Option nicht sehen.  
- Berechtigung zum Erstellen und Bearbeiten angepasster KI-Agenten. 
- Eine Idee, was Sie mit dem Agenten bezwecken möchten. Braze Agents können die folgenden Aktionen unterstützen:  
   - **Messaging:** Generieren Sie Betreffzeilen, Überschriften, produktinterne Texte oder andere Inhalte.  
   - **Entscheidungsfindung:** Leiten Sie Nutzer:innen in Canvas auf der Grundlage von Verhalten, Vorlieben oder angepassten Attributen weiter.  
   - **Datenverwaltung:** Berechnen Sie Werte, reichern Sie Katalogeinträge an oder aktualisieren Sie Profilfelder.  

## Funktionsweise

Wenn Sie einen Agenten erstellen, definieren Sie seinen Zweck und setzen Leitplanken für sein Verhalten. Nach der Inbetriebnahme kann der Agent in Braze eingesetzt werden, um personalisierte Texte zu erstellen, Entscheidungen in Echtzeit zu treffen oder Katalogfelder zu aktualisieren. Sie können einen Agenten jederzeit über das Dashboard pausieren oder aktualisieren.

Die folgenden Anwendungsfälle zeigen einige Möglichkeiten, wie Sie angepasste Agenten nutzen können.

| Anwendungsfall | Beschreibung |
| --- | --- |
| Umgang mit Kunden:in | Geben Sie das Feedback der Nutzer:innen an einen Agenten weiter, um die Stimmung zu analysieren und einfühlsame Nachrichten zu erstellen. Für hochwertige Nutzer:innen könnte der Agent die Antwort eskalieren oder Vergünstigungen anbieten. |
| Inhalte lokalisieren | Übersetzen Sie den Katalogtext für globale Kampagnen in eine andere Sprache, oder passen Sie Ton und Länge für regionalspezifische Kanäle an. Übersetzen Sie zum Beispiel "Classic Clubmaster Sonnenbrille" ins Spanische als "Gafas de sol Classic Clubmaster" oder kürzen Sie Beschreibungen für SMS Kampagnen. |
| Fassen Sie Bewertungen oder Feedback zusammen | Fassen Sie die Stimmung oder das Feedback in einem neuen Feld zusammen, indem Sie z.B. Stimmungswerte wie Positiv, Neutral oder Negativ vergeben oder eine kurze Textzusammenfassung wie "Die meisten Kund:in erwähnen die gute Passform, bemängeln aber den langsamen Versand." erstellen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Einen Agenten erstellen

### Schritt 1: Details einrichten

Um Ihren angepassten Agenten zu erstellen:

1. Gehen Sie im Braze-Dashboard zu **Agentenkonsole** > **Agent Management**.  
2. Wählen Sie **Agent erstellen**.
3. Geben Sie einen Namen und eine Beschreibung ein, damit Ihr Team seinen Zweck versteht.
4. (optional) Fügen Sie Tags hinzu, um Ihren Agenten zu filtern.
5. Wählen Sie den Interaktionsstandort aus, d.h. den Standort, an dem der Agent eingesetzt wird. Beachten Sie, dass die Interaktionsseite nicht mehr aktualisiert werden kann, nachdem ein Agent erstellt wurde.
6. Wählen Sie das [Modell]({{site.baseurl}}/docs/user_guide/brazeai/agents/reference/#models), das Ihr Agent verwenden wird.

![Schnittstelle der Agentenkonsole zur Erstellung eines angepassten Agenten in Braze. Der Bildschirm enthält Felder zur Eingabe des Agentennamens und der Beschreibung sowie zum Auswählen eines Modells.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:85%;"}

### Schritt 2: Schreiben Sie die Anweisungen

Geben Sie dem Agenten Anweisungen. Schauen Sie in der [Referenz des Agents]({{site.baseurl}}/user_guide/brazeai/agents/reference/) nach.

{% alert tip %}
Sie können Liquid in Ihren Anweisungen verwenden, um Nutzer:innen-Attribute, wie z.B. ihren Vor- und Nachnamen, oder angepasste Attribute zu referenzieren.
{% endalert %}

#### Schritt 2.1: Kontext hinzufügen

Wählen Sie **Kontext hinzufügen**, um auszuwählen, was Ihr Agent referenzieren kann. Dies beinhaltet:

- [Katalogfelder]({{site.baseurl}}/user_guide/brazeai/agents/reference/#catalogs-and-fields): Stellen Sie Katalogfelder bereit, auf die der Agent referenzieren kann.
- [Segmentzugehörigkeit]({{site.baseurl}}/user_guide/brazeai/agents/reference/#segment-membership-context): Berücksichtigen Sie bei der Personalisierung von Nachrichten die Mitgliedschaft eines Nutzers:innen in einem Segment. Sie können bis zu drei Segmente auswählen.
- [Markenrichtlinien]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines): Referenzieren Sie die Markenstimme und die Stilrichtlinien, die der Agent befolgen muss. Wenn Sie beispielsweise möchten, dass Ihr Agent SMS-Texte erstellt, um Nutzer:innen zur Registrierung für eine Mitgliedschaft im Fitnessstudio zu ermutigen, können Sie in diesem Feld Ihre vordefinierte fettgedruckte, motivierende Richtlinie referenzieren.
- [Canvas-Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables): Analysieren Sie alle Canvas-Kontextvariablen für einen Nutzer:innen, wenn dieser Agent aufgerufen wird.

#### Schritt 2.2: Optionale Einstellungen hinzufügen

In den **optionalen Einstellungen** können Sie die [Temperatur]({{site.baseurl}}/user_guide/brazeai/agents/reference/#temperature) der vom Agenten erstellten Kopie anpassen. Eine höhere Temperatur erlaubt es dem Agenten, die bereitgestellten Informationen kreativer zu nutzen.

Sie können auch das tägliche Ausführungslimit für Ihren Agenten festlegen. Standardmäßig ist dieser Wert auf 50.000 eingestellt, kann aber auf 100.000 erhöht werden. Wenn Sie daran interessiert sind, das Limit über 100.000 zu erhöhen, wenden Sie sich an Ihren Customer-Success-Manager, um mehr zu erfahren.

### Schritt 3: Wählen Sie die Ausgabe aus

Im Bereich **Ausgabe** können Sie die Ausgabe des Agenten nach Basisschemata oder vorgebrachten Schemata organisieren und definieren.

#### Grundlegende Schemata

Basisschemata sind eine einfache Ausgabe, die ein Agent zurückgibt. Dies kann ein String, eine Zahl, ein Boolean, ein String-Array oder ein Zahlen-Array sein.

Nehmen wir an, Sie möchten Nutzer:innen in einer einfachen Umfrage nach ihrer Zufriedenheit mit einem Produkt befragen. Sie können **Nummer** als Basisschema auswählen, um das Ausgabeformat zu strukturieren.

{% alert important %}
Arrays sind nur für Canvas-Agenten verfügbar, nicht für Katalog-Agenten.
{% endalert %}

![Agentenkonsole mit ausgewählter Nummer als Basisschema.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

#### Fortgeschrittene Schemata

Zu den vorgebrachten Schemaoptionen gehören die manuelle Strukturierung von Feldern oder die Verwendung von JSON.

- **Felder:** Ein Code-freier Weg, um eine Agentenausgabe zu erzwingen, die Sie konsistent verwenden können. 
- **JSON:** Ein Code-Ansatz zur Erstellung eines präzisen Ausgabeformats, bei dem Sie Variablen und Objekte innerhalb des JSON-Schemas verschachteln können.

{% tabs %}
{% tab Fields %}

Nehmen wir an, Sie möchten die Antworten auf eine einfache Umfrage formatieren, um festzustellen, wie wahrscheinlich es ist, dass die Befragten die neueste Eissorte Ihres Restaurants weiterempfehlen. Sie können die folgenden Felder einrichten, um das Ausgabeformat zu strukturieren:

| Feldname | Wert
| --- | --- |
| **likelihood_score** | Zahl |
| **Erklärung** | Text |
| **confidence_score** | Zahl |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Agentenkonsole mit drei Ausgabefeldern für Wahrscheinlichkeitswert, Erklärung und Vertrauenswert.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON schema %}

Nehmen wir an, Sie möchten das Feedback der Nutzer:innen zu ihrem letzten Restaurantbesuch in Ihrer Restaurantkette sammeln. Sie könnten **JSON Schema** als Ausgabeformat auswählen und das folgende JSON einfügen, um ein Datenobjekt zurückzugeben, das eine Sentiment-Variable und eine Argumentationsvariable enthält.

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

{% endtab %}
{% endtabs %}

### Schritt 4: Testen und erstellen Sie den Agenten

Das **Vorschau-Fenster** ist eine Instanz des Agenten, die in der Konfigurationsumgebung als Panel nebeneinander angezeigt wird. Damit können Sie den Agenten testen, während Sie ihn erstellen oder Updates vornehmen, um ihn ähnlich wie die Nutzer:innen zu erleben. Dieser Schritt hilft Ihnen zu bestätigen, dass sich das System so verhält, wie Sie es erwarten, und gibt Ihnen die Möglichkeit zur Feinabstimmung, bevor es live geht.

1. Geben Sie in das Feld **Testen Sie Ihren Agenten** Beispiel-Kundendaten oder Kundenantworten ein - alles, was reale Szenarien widerspiegelt, die Ihr Agent bearbeiten wird.
2. Vorschau auf die Antwort des Agenten für einen zufälligen, bestehenden oder angepassten Nutzer:innen.
3. Wählen Sie **Antwort simulieren**. Der Agent wird auf der Grundlage Ihrer Konfiguration ausgeführt und zeigt seine Antwort an. Testläufe werden auf Ihr tägliches Ausführungslimit angerechnet.

![Agenten-Konsole mit dem Vorschau-Fenster zum Testen eines angepassten Agenten. Die Schnittstelle zeigt ein Beispieleingabefeld mit beispielhaften Kundendaten, einen Button Test ausführen und einen Antwortbereich, in dem die Ausgabe des Agenten erscheint.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Prüfen Sie die Ausgabe mit einem kritischen Auge. Überlegen Sie sich die folgenden Fragen:

- Ist der Text markengerecht?
- Leitet die Entscheidungslogik die Kund:in wie vorgesehen weiter?
- Sind die berechneten Werte korrekt?

Wenn Sie das Gefühl haben, dass etwas nicht stimmt, aktualisieren Sie die Konfiguration des Agenten und testen Sie erneut. Führen Sie einige verschiedene Eingaben durch, um zu sehen, wie sich der Agent an verschiedene Szenarien anpasst, insbesondere an Grenzfälle wie keine Daten oder ungültige Antworten.

### Schritt 5: Verwenden und überwachen Sie Ihren Agenten

Ihr Agent ist jetzt einsatzbereit! Einzelheiten finden Sie unter [Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

Im Tab **Protokolle** Ihres Agenten können Sie die tatsächlichen Agentenaufrufe überwachen, die in Ihren Canvase und Katalogen erfolgen. Sie können nach Informationen wie dem Datumsbereich, dem Ergebnis (Erfolg oder Misserfolg) oder dem Standort des Anrufers filtern.

![Protokolle für einen Agenten Story Teller, aus denen hervorgeht, wann und wo der Agent angerufen wurde.]({% image_buster /assets/img/ai_agent/agent_activity_logs.png %})

Wählen Sie **Ansicht** für einen bestimmten Agentenaufruf, um die Eingabe, die Ausgabe und die Nutzer:innen zu sehen.

![Protokolle für einen Agenten Story Teller. Das Panel "Details" zeigt die Eingabeaufforderung, die Ausgabeantwort und die zugehörige Nutzer:in an.]({% image_buster /assets/img/ai_agent/agent_logs.png %})
