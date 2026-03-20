---
nav_title: Agenten erstellen
article_title: Angepasste Agenten erstellen
description: "Erfahren Sie, wie Sie Agenten erstellen, was Sie vor dem Start vorbereiten müssen und wie Sie diese für Messaging, Entscheidungsfindung und Datenmanagement einsetzen können."
page_order: 1
alias: /creating-agents/
---

# Angepasste Agenten erstellen

> Erfahren Sie, wie Sie angepasste Agenten erstellen, was Sie vor dem Start vorbereiten müssen und wie Sie diese für Messaging, Entscheidungsfindung und Datenmanagement einsetzen können. Weitere allgemeine Informationen finden Sie unter [Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents).

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

- [Berechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) für den Zugriff auf die **Agent Console** in Ihrem Workspace. Wenden Sie sich an Ihre Braze-Administratoren, falls diese Option nicht angezeigt wird.  
- Berechtigung zum Erstellen und Bearbeiten von angepassten KI-Agenten.
- Einen [KI-Modellanbieter]({{site.baseurl}}/partners/ai_model_providers), der mit Braze integriert ist.
- Eine Idee davon, was der Agent erreichen soll. Braze-Agenten können die folgenden Aktionen unterstützen:  
   - **Messaging:** Generieren Sie Betreffzeilen, Überschriften, Produkttexte oder andere Inhalte.  
   - **Entscheidungsfindung:** Leiten Sie Nutzer:innen in Canvas basierend auf Verhalten, Präferenzen oder angepassten Attributen weiter.  
   - **Datenverwaltung:** Berechnen Sie Werte, ergänzen Sie Katalogeinträge oder aktualisieren Sie Profilfelder.  

## Funktionsweise

Wenn Sie einen Agenten erstellen, definieren Sie dessen Zweck und legen Leitplanken für sein Verhalten fest. Nach der Live-Schaltung kann der Agent in Braze eingesetzt werden, um personalisierte Texte zu generieren, Entscheidungen in Realtime zu treffen oder Katalogfelder zu aktualisieren. Sie können einen Agenten jederzeit über das Dashboard pausieren oder aktualisieren.

Die folgenden Anwendungsfälle veranschaulichen einige Möglichkeiten, angepasste Agenten zu nutzen.

| Anwendungsfall | Beschreibung |
| --- | --- |
| Bearbeitung von Kundenfeedback | Leiten Sie das Feedback der Nutzer:innen an einen Agenten weiter, um die Stimmung zu analysieren und einfühlsame Follow-up-Nachrichten zu generieren. Bei besonders wertvollen Nutzer:innen kann der Agent die Antwort eskalieren oder Vergünstigungen hinzufügen. |
| Inhalte lokalisieren | Übersetzen Sie Katalogtexte für globale Kampagnen in andere Sprachen oder passen Sie Tonfall und Länge für regionsspezifische Kanäle an. Übersetzen Sie beispielsweise „Classic Clubmaster Sunglasses" ins Spanische als „Gafas de sol Classic Clubmaster" oder kürzen Sie Beschreibungen für SMS-Kampagnen. |
| Bewertungen oder Feedback zusammenfassen | Fassen Sie die Stimmung oder das Feedback in einem neuen Feld zusammen, beispielsweise durch die Vergabe von Stimmungsbewertungen wie „Positiv", „Neutral" oder „Negativ" oder durch die Erstellung einer kurzen Textzusammenfassung wie „Die meisten Kund:innen erwähnen die hervorragende Passform, bemerken jedoch den langsamen Versand." |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Einen Agenten erstellen

### 1. Schritt: Agententyp auswählen

Um Ihren angepassten Agenten zu erstellen:

1. Gehen Sie im Braze-Dashboard zu **Agent Console** > **Agent Management**.  
2. Wählen Sie **Agent erstellen** aus.
3. Wählen Sie, ob Sie einen Canvas-Agenten oder einen Katalog-Agenten erstellen möchten.

### 2. Schritt: Details einrichten

Richten Sie anschließend die Details für Ihren Agenten ein:

1. Geben Sie einen Namen und eine Beschreibung ein, damit Ihr Team den Zweck versteht.
2. (optional) Fügen Sie Tags hinzu, um Ihren Agenten zu filtern.
3. Wählen Sie das [Modell]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) aus, das Ihr Agent verwenden soll.
4. Wenn Sie nicht das **Braze Auto**-Modell verwenden, wählen Sie die [Denkstufe]({{site.baseurl}}/user_guide/brazeai/agents/reference/#thinking-levels) des Modells aus. Sie können zwischen minimal, niedrig, mittel oder hoch wählen. Wir empfehlen, mit **Minimal** zu beginnen, die Antworten Ihres Agenten zu testen und diese bei Bedarf anzupassen.
5. Legen Sie ein tägliches Ausführungslimit fest. Standardmäßig ist dieser Wert auf 250.000 eingestellt, kann jedoch auf 1.000.000 erhöht werden. Wenn Sie das Limit über 1.000.000 hinaus erhöhen möchten, wenden Sie sich an Ihren Customer-Success-Manager, um mehr zu erfahren.

![Agent-Console-Oberfläche zum Erstellen eines angepassten Agenten in Braze. Der Bildschirm zeigt Felder zur Eingabe des Agentennamens und der Beschreibung, zur Auswahl eines Modells und zur Festlegung eines täglichen Ausführungslimits.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### 3. Schritt: Anweisungen verfassen {#agent-instructions}

Geben Sie dem Agenten Anweisungen. Wir empfehlen, Anweisungen dafür aufzunehmen, wie der Agent in unerwarteten oder unklaren Szenarien vorgehen soll. Dadurch wird das Risiko minimiert, dass Verwirrung beim Agenten zu Fehlern führt. Anstatt beispielsweise den Agenten nur nach „positiven" oder „negativen" Stimmungswerten zu fragen, bitten Sie ihn, „unsicher" zurückzugeben, wenn er sich nicht entscheiden kann.

Lesen Sie den Abschnitt [Anweisungen verfassen]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) für bewährte Verfahren und [Beispiele]({{site.baseurl}}/user_guide/brazeai/agents/reference/#examples) für Anregungen, wie Sie Ihren Agenten anweisen können.

{% alert tip %}
Für Canvas-Agenten können Sie Liquid in Ihren Anweisungen verwenden, um auf Nutzerattribute wie Vor- und Nachname oder angepasste Attribute zu referenzieren. Jede Liquid-Variable in den Agentenanweisungen wird automatisch an den Agentenschritt übergeben, wenn eine Nutzer:in den Schritt betritt.
{% endalert %}

#### Schritt 3.1: Ressourcen hinzufügen

Wählen Sie **Ressourcen hinzufügen** aus, um festzulegen, worauf Ihr Agent zugreifen kann. Dies beinhaltet:

- [Katalogfelder]({{site.baseurl}}/user_guide/brazeai/agents/reference/#catalogs-and-fields): Gewähren Sie dem Agenten Zugriff auf Ihre Katalogdaten für genauere Antworten.
- [Segmentzugehörigkeit]({{site.baseurl}}/user_guide/brazeai/agents/reference/#segment-membership-context): Ermöglichen Sie dem Agenten, Antworten basierend auf der Segmentzugehörigkeit der Nutzer:innen zu personalisieren. Sie können bis zu fünf Segmente auswählen.
- [Markenrichtlinien]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines): Referenzieren Sie die Richtlinien zur Markenstimme und zum Stil, die der Agent befolgen soll. Wenn Sie beispielsweise möchten, dass Ihr Agent SMS-Texte erstellt, um Nutzer:innen zur Anmeldung für eine Fitnessstudio-Mitgliedschaft zu motivieren, können Sie dieses Feld verwenden, um Ihre vordefinierte, motivierende Richtlinie zu referenzieren.
- [Gesamter Canvas-Kontext]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables): Analysieren Sie alle Canvas-Kontextdaten für eine Nutzer:in, wenn dieser Agent aufgerufen wird, einschließlich aller Variablen, die nicht im Abschnitt **Anweisungen** referenziert werden.

#### Schritt 3.2: Optionale Einstellungen hinzufügen

In den **optionalen Einstellungen** können Sie die [Temperatur]({{site.baseurl}}/user_guide/brazeai/agents/reference/#temperature) der vom Agenten generierten Texte anpassen. Eine höhere Temperatur ermöglicht es dem Agenten, die bereitgestellten Informationen kreativer zu nutzen.

### 4. Schritt: Ausgabe auswählen {#select-output}

Im Abschnitt **Ausgabe** können Sie die Ausgabe des Agenten anhand von Basisschemata oder erweiterten Schemata organisieren und definieren.

Um optimale Ergebnisse zu erzielen, stellen Sie sicher, dass die Angaben im Abschnitt **Ausgabe** mit den Agentenanweisungen übereinstimmen, die Sie in [Schritt 3](#agent-instructions) eingegeben haben. Wenn Sie beispielsweise in den Agentenanweisungen angegeben haben, dass Sie ein Objekt mit zwei Strings wünschen, stellen Sie sicher, dass Sie im Abschnitt **Ausgabe** ein Objekt mit zwei Strings angeben. Wenn Ihre Agentenanweisungen nicht mit der festgelegten Ausgabe übereinstimmen, kann der Agent verwirrt werden, eine Zeitüberschreitung verursachen oder unerwünschte Ausgaben generieren.

#### Grundlegende Schemata

Basisschemata sind eine einfache Ausgabe, die ein Agent zurückgibt. Dies kann ein String, eine Zahl, ein Boolescher Wert, ein String-Array oder ein Array von Zahlen sein.

Wenn Sie beispielsweise anhand einer einfachen Feedback-Umfrage die Zufriedenheit Ihrer Kund:innen nach Erhalt eines Produkts ermitteln möchten, können Sie **Zahl** als Basisschema auswählen, um das Ausgabeformat zu strukturieren.

{% alert important %}
Arrays sind nur für Canvas-Agenten verfügbar, nicht für Katalog-Agenten.
{% endalert %}

![Agent Console mit ausgewählter Zahl als grundlegendem Schema.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

#### Erweiterte Schemata

Zu den erweiterten Schemaoptionen gehören die manuelle Strukturierung von Feldern oder die Verwendung von JSON.

- **Felder:** Eine No-Code-Methode zur Durchsetzung einer Agentenausgabe, die Sie konsistent verwenden können.
- **JSON:** Ein Code-Ansatz zur Erstellung eines präzisen Ausgabeformats, bei dem Sie Variablen und Objekte innerhalb des JSON-Schemas verschachteln können. Nur für Canvas-Agenten verfügbar, nicht für Katalog-Agenten.

Wir empfehlen die Verwendung erweiterter Schemata, wenn der Agent eine Datenstruktur mit mehreren strukturiert definierten Werten zurückgeben soll, anstatt eine Ausgabe mit einem einzelnen Wert. Dadurch kann die Ausgabe besser als konsistente Kontextvariable formatiert werden.

Beispielsweise können Sie innerhalb eines Agenten ein Ausgabeformat verwenden, das dazu dient, für eine Nutzer:in auf Grundlage eines eingereichten Formulars einen Musterreiseplan zu erstellen. Das Ausgabeformat ermöglicht es Ihnen festzulegen, dass jede Antwort des Agenten mit Werten für `tripStartDate`, `tripEndDate` und `destination` zurückkommen soll. Jeder dieser Werte kann aus Kontextvariablen extrahiert und zur Personalisierung mithilfe von Liquid in einen Nachrichtenschritt eingefügt werden.

{% tabs %}
{% tab Fields %}

Wenn Sie die Antworten einer einfachen Feedback-Umfrage formatieren möchten, um zu ermitteln, wie wahrscheinlich es ist, dass die Befragten die neueste Eissorte Ihres Restaurants weiterempfehlen, können Sie die folgenden Felder einrichten, um das Ausgabeformat zu strukturieren:

| Feldname | Wert |
| --- | --- |
| **likelihood_score** | Zahl |
| **explanation** | String |
| **confidence_score** | Zahl |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Agent Console mit drei Ausgabefeldern für Wahrscheinlichkeitswert, Erklärung und Konfidenzwert.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON schema %}

Wenn Sie Nutzerfeedback zu den jüngsten Erfahrungen in Ihrer Restaurantkette sammeln möchten, können Sie **JSON Schema** als Ausgabeformat auswählen und das folgende JSON einfügen, um ein Datenobjekt zurückzugeben, das eine Stimmungsvariable und eine Begründungsvariable enthält.

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

### 5. Schritt: Agenten testen und erstellen

Der **Vorschaubereich** ist eine Instanz des Agenten, die als nebeneinander angeordnetes Panel innerhalb der Konfiguration angezeigt wird. Sie können ihn verwenden, um den Agenten zu testen, während Sie ihn erstellen oder aktualisieren, und ihn auf ähnliche Weise wie Endnutzer:innen zu erleben. Dieser Schritt hilft Ihnen zu bestätigen, dass er sich wie erwartet verhält, und gibt Ihnen die Möglichkeit, vor der Live-Schaltung Feinabstimmungen vorzunehmen.

1. Geben Sie im Feld **Agent testen** Beispielkundendaten oder Kundenantworten ein – alles, was reale Szenarien widerspiegelt, mit denen Ihr Agent konfrontiert sein wird.
2. Zeigen Sie eine Vorschau der Antwort des Agenten für eine zufällige Nutzer:in, eine bestehende Nutzer:in oder eine angepasste Nutzer:in an.
3. Wählen Sie **Antwort simulieren** aus. Der Agent führt die Konfiguration aus und zeigt seine Antwort an.

{% alert note %}
Testläufe werden auf Ihr tägliches Ausführungslimit angerechnet.
{% endalert %}

![Agent Console mit dem Vorschaubereich zum Testen eines angepassten Agenten. Die Oberfläche zeigt ein Feld für Beispieleingaben mit Beispielkundendaten, einen Button „Test ausführen" und einen Antwortbereich, in dem die Ausgabe des Agenten angezeigt wird.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Überprüfen Sie die Ausgabe mit kritischem Blick. Berücksichtigen Sie die folgenden Fragen:

- Entspricht der Text dem Markenimage?
- Leitet die Entscheidungslogik die Kund:innen wie beabsichtigt weiter?
- Sind die berechneten Werte korrekt?

Wenn etwas nicht stimmt, aktualisieren Sie die Konfiguration des Agenten und testen Sie erneut. Führen Sie einige unterschiedliche Eingaben durch, um zu beobachten, wie sich der Agent an verschiedene Szenarien anpasst, insbesondere an Randfälle wie fehlende Daten oder ungültige Antworten.

{% alert tip %}
Vermeiden Sie es, dem Agenten genau mitzuteilen, was er nicht tun soll. LLMs können diesen Inhalt dennoch generieren, wenn Sie ihn in den Anweisungen erwähnen.
{% endalert %}

### 6. Schritt: Ihren Agenten verwenden

Ihr Agent ist nun einsatzbereit! Weitere Informationen finden Sie unter [Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

## Verwandte Artikel  

- [Referenz für Agenten]({{site.baseurl}}/user_guide/brazeai/agents/reference/)