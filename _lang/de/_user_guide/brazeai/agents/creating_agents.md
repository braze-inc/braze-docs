---
nav_title: Agenten erstellen
article_title: Angepasste Agenten erstellen
description: "Erfahren Sie, wie Sie Agenten erstellen, was Sie vor dem Start vorbereiten müssen und wie Sie diese für Messaging, Entscheidungsfindung und Datenmanagement einsetzen können."
page_order: 1
alias: /creating-agents/
---

# Angepasste Agenten erstellen

> Erfahren Sie, wie Sie benutzerdefinierte Agenten erstellen, was Sie vor dem Start vorbereiten müssen und wie Sie diese für Messaging, Entscheidungsfindung und Datenmanagement einsetzen können. Für weitere allgemeine Informationen, siehe [Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents).

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

- [Berechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) für den Zugriff auf die **Agent-Konsole** in Ihrem Workspace. Bitte wenden Sie sich an Ihre Braze-Administratoren, falls diese Option nicht angezeigt wird.  
- Berechtigung zum Erstellen und Bearbeiten von benutzerdefinierten KI-Agenten.
- Eine Idee davon, was Sie vom Makler erwarten. Braze-Agenten können die folgenden Aktionen unterstützen:  
   - **Messaging:** Erstellen Sie Betreffzeilen, Überschriften, Produktbeschreibungen oder andere Inhalte.  
   - **Entscheidungsfindung:** Leiten Sie Nutzer:innen in Canvas basierend auf ihrem Verhalten, ihren Präferenzen oder angepassten Attributen weiter.  
   - **Datenverwaltung:** Berechnen Sie Werte, ergänzen Sie Katalogeinträge oder aktualisieren Sie Profilfelder.  

## Funktionsweise

Wenn Sie einen Agenten erstellen, definieren Sie dessen Zweck und legen Sie Richtlinien für dessen Verhalten fest. Nach der Live-Schaltung kann der Agent in Braze eingesetzt werden, um personalisierte Texte zu generieren, Entscheidungen in Realtime zu treffen oder Katalogfelder zu Updateen. Sie können einen Agenten jederzeit über das Dashboard pausieren oder ein Update durchführen.

Die folgenden Anwendungsfälle veranschaulichen einige Möglichkeiten, wie angepasste Agenten genutzt werden können.

| Anwendungsfall | Beschreibung |
| --- | --- |
| Bearbeitung von Kundenfeedback | Leiten Sie das Feedback der Nutzer:innen an einen Mitarbeiter weiter, um die Stimmung zu analysieren und einfühlsame Follow-up-Nachrichten zu erstellen. Bei besonders wertvollen Nutzer:innen kann der Mitarbeiter die Antwort eskalieren oder Vergünstigungen hinzufügen. |
| Lokalisierung der Inhalte | Übersetzen Sie Katalogtexte für globale Kampagnen in andere Sprachen oder passen Sie Tonfall und Länge für regionsspezifische Kanäle an. Bitte übersetzen Sie beispielsweise „Classic Clubmaster Sunglasses“ ins Spanische mit „Gafas de sol Classic Clubmaster“ oder kürzen Sie Beschreibungen für SMS-Kampagnen. |
| Zusammenfassung von Bewertungen oder Feedback | Fassen Sie die Stimmung oder das Feedback in einem neuen Feld zusammen, beispielsweise durch die Vergabe von Stimmungsbewertungen wie „Positiv“, „Neutral“ oder „Negativ“ oder durch die Erstellung einer kurzen Textzusammenfassung wie „Die meisten Kund:innen erwähnen die hervorragende Passform, bemerken jedoch den langsamen Versand.“ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Einen Agenten erstellen

### Schritt 1: Bitte wählen Sie einen Agententyp aus.

Um Ihren angepassten Agenten zu erstellen:

1. Bitte gehen Sie im Braze-Dashboard zu **„Agent Console“** > **„Agent Management**“.  
2. Auswählen **„Agent erstellen**“.
3. Bitte wählen Sie, ob Sie einen Canvas-Agenten oder einen Katalog-Agenten erstellen möchten.

### Schritt 2: Einrichtungsdetails

Bitte richten Sie anschließend die Details für Ihren Agenten ein:

1. Bitte geben Sie einen Namen und eine Beschreibung ein, damit Ihr Team den Zweck versteht.
2. (optional) Fügen Sie Tags hinzu, um Ihren Agenten zu filtern.
3. Bitte wählen Sie das [Modell]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) aus, das Ihr Agent verwenden soll.
4. Bitte wählen Sie die Denkebene des Modells aus. Sie können zwischen minimal, niedrig, mittel oder hoch wählen. Wir empfehlen, mit **„Minimal“** zu beginnen, die Antworten Ihres Agenten zu testen und diese bei Bedarf anzupassen.

![Agentenkonsole-Schnittstelle zum Erstellen eines benutzerdefinierten Agenten in Braze. Der Bildschirm zeigt Felder zur Eingabe des Agentennamens und der Beschreibung sowie zum Auswählen eines Modells an.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### Schritt 3: Bitte die Anweisungen verfassen. {#agent-instructions}

Bitte geben Sie dem Agenten Anweisungen. Wir empfehlen, Anweisungen für den Agenten aufzunehmen, wie er in unerwarteten oder unklaren Situationen vorgehen soll. Dadurch wird das Risiko minimiert, dass Verwirrung bei den Mitarbeitern zu Fehlern führt. Anstatt beispielsweise den Agenten nur nach „positiven“ oder „negativen“ Stimmungswerten zu fragen, bitten Sie ihn, „unsicher“ zurückzugeben, wenn er sich nicht entscheiden kann.

Refernzieren Sie die [Schreibanweisungen]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) für bewährte Verfahren und [Beispiele,]({{site.baseurl}}/user_guide/brazeai/agents/reference/#examples) um Anregungen zu erhalten, wie Sie Ihren Agenten anweisen können.

{% alert tip %}
Für Canvas-Agenten können Sie Liquid in Ihren Anweisungen verwenden, um auf Benutzerattribute wie den Vornamen und den Nachnamen oder angepasste Attribute zu referenzieren. Jede Liquid-Variable in den Agentenanweisungen wird automatisch an den Agentenschritt übergeben, wenn eine Nutzer:in den Schritt aufruft.
{% endalert %}

#### Schritt 3.1: Kontext hinzufügen

Auswählen **„Kontext hinzufügen”,** um festzulegen, worauf Ihr Agent referenzieren kann. Dies beinhaltet:

- [Katalogfelder]({{site.baseurl}}/user_guide/brazeai/agents/reference/#catalogs-and-fields): Bitte gewähren Sie dem Mitarbeiter Zugriff auf Ihre Katalogdaten, um genauere Antworten zu erhalten.
- [Segmentzugehörigkeit]({{site.baseurl}}/user_guide/brazeai/agents/reference/#segment-membership-context): Bitte gestatten Sie dem Agenten, Antworten entsprechend der Segmentzugehörigkeit der Nutzer:innen individuell zu personalisieren. Sie können bis zu fünf Segmente auswählen.
- [Markenrichtlinien]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines): Refernzieren Sie die Richtlinien zur Markenstimme und zum Stil, die der Agent befolgen soll. Wenn Sie beispielsweise möchten, dass Ihr Agent einen SMS-Text erstellt, um Nutzer:innen zur Registrierung für eine Fitnessstudio-Mitgliedschaft zu motivieren, können Sie dieses Feld verwenden, um Ihre vordefinierte, motivierende Richtlinie zu referenzieren.
- [Gesamter Canvas-Kontext]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables): Analysieren Sie alle Canvas-Kontextdaten für einen Nutzer:in, wenn dieser Agent aufgerufen wird, einschließlich aller Variablen, die nicht im Abschnitt **„Anweisungen“** referenziert sind.

#### Schritt 3.2: Optionale Einstellungen hinzufügen

In den **optionalen Einstellungen** können Sie die [Temperatur]({{site.baseurl}}/user_guide/brazeai/agents/reference/#temperature) der vom Agenten erstellten Kopie anpassen. Eine höhere Temperatur macht es dem Agenten zulässig, die bereitgestellten Informationen kreativer zu nutzen.

Sie können auch das tägliche Ausführungslimit für Ihren Agenten festlegen. Standardmäßig ist dieser Wert auf 250.000 eingestellt, kann jedoch auf 1.000.000 erhöht werden. Sollten Sie daran interessiert sein, das Limit über 1.000.000 hinaus zu erhöhen, wenden Sie sich bitte an Ihren Customer-Success-Manager, um weitere Informationen zu erhalten.

### Schritt 4: Bitte wählen Sie die Ausgabe aus. {#select-output}

Im Abschnitt **„Ausgabe**“ können Sie die Ausgabe des Agenten anhand von Basisschemata oder erweiterten Schemata organisieren und definieren.

Um optimale Ergebnisse zu erzielen, stellen Sie bitte sicher, dass die Angaben im Abschnitt **„Ausgabe“** mit den Anweisungen für Agenten übereinstimmen, die Sie in [Schritt 3](#agent-instructions) eingegeben haben. Wenn Sie beispielsweise in den Anweisungen für den Agenten angegeben haben, dass Sie ein Objekt mit zwei Strings wünschen, stellen Sie sicher, dass Sie im Abschnitt **„Ausgabe“** ein Objekt mit zwei Strings angeben. Sollten Ihre Anweisungen an den Agenten nicht mit dem von Ihnen festgelegten Ergebnis übereinstimmen, kann dies zu Verwirrung beim Agenten führen, eine Zeitüberschreitung verursachen oder unerwünschte Ergebnisse hervorrufen.

#### Grundlegende Schemata

Basisschemata sind eine einfache Ausgabe, die ein Agent zurückgibt. Dies kann ein String, eine Zahl, ein Boolescher Wert, ein String-Array oder ein Array von Zahlen sein.

Wenn Sie beispielsweise anhand einer einfachen Feedback-Umfrage die Zufriedenheit Ihrer Kund:innen nach Erhalt eines Produkts ermitteln möchten, können Sie **„Zahl“** als Basisschema auswählen, um das Ausgabeformat zu strukturieren.

{% alert important %}
Arrays sind nur für Canvas-Agenten verfügbar, nicht für Katalog-Agenten.
{% endalert %}

![Agentenkonsole mit ausgewählter Nummer als grundlegendem Schema.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

#### Erweiterte Schemata

Zu den erweiterten Schemaoptionen gehören die manuelle Strukturierung von Feldern oder die Verwendung von JSON.

- **Felder:** Eine No-Code-Methode zur Durchsetzung einer Agentenausgabe, die Sie konsistent anwenden können.
- **JSON:** Ein Code-Ansatz zur Erstellung eines präzisen Ausgabeformats, bei dem Sie Variablen und Objekte innerhalb des JSON-Schemas verschachteln können. Nur für Canvas-Agenten verfügbar, nicht für Katalog-Agenten.

Wir empfehlen die Verwendung erweiterter Schemata, wenn Sie möchten, dass der Agent eine Datenstruktur mit mehreren Werten zurückgibt, die in einer strukturierten Weise definiert sind, anstatt eine Ausgabe mit einem einzigen Wert. Dadurch ist es zulässig, die Ausgabe besser als konsistente Kontextvariable formatiert zu haben.

Beispielsweise können Sie innerhalb eines Agenten ein Ausgabeformat verwenden, das dazu dient, für einen Nutzer:in auf Grundlage eines von ihm eingereichten Formulars einen Musterreiseplan zu erstellen. Das Ausgabeformat ermöglicht es Ihnen festzulegen, dass jede Antwort des Agenten mit Werten für `tripStartDate`,`tripEndDate`  und  zurückkommen`destination` soll. Jeder dieser Werte kann aus Kontextvariablen extrahiert und zur Personalisierung mithilfe von Liquid in einen Nachrichtenschritt eingefügt werden.

{% tabs %}
{% tab Fields %}

Wenn Sie die Antworten einer einfachen Feedback-Umfrage formatieren möchten, um zu ermitteln, wie wahrscheinlich es ist, dass die Befragten die neueste Eissorte Ihres Restaurants weiterempfehlen, können Sie die folgenden Felder einrichten, um das Ausgabeformat zu strukturieren:

| Feldname | Wert |
| --- | --- |
| **likelihood_score** | Zahl |
| **Erklärung** | String |
| **confidence_score** | Zahl |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Agentenkonsole mit drei Ausgabefeldern für Wahrscheinlichkeitswert, Erklärung und Konfidenzwert.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON schema %}

Wenn Sie Nutzer-Feedback zu den jüngsten Erfahrungen in Ihrer Restaurantkette sammeln möchten, können Sie **JSON Schema** als Ausgabeformat auswählen und das folgende JSON einfügen, um ein Datenobjekt zurückzugeben, das eine Stimmungsvariable und eine Begründungsvariable enthält.

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

### Schritt 5: Den Agenten testen und erstellen

Der **Vorschaubereich** ist eine Instanz des Agenten, die als nebeneinander angeordnetes Panel innerhalb der Konfiguration angezeigt wird. Sie können es verwenden, um den Agenten zu testen, während Sie ihn erstellen oder Updates für ihn durchführen, um ihn auf ähnliche Weise wie Endnutzer:innen zu erleben. Dieser Schritt ermöglicht es Ihnen, zu überprüfen, ob alles wie erwartet funktioniert, und bietet Ihnen die Möglichkeit, vor der Live-Schaltung noch Feinabstimmungen vorzunehmen.

1. Geben Sie im Feld **„Agent testen**“ Beispielkundendaten oder Kundenantworten ein – alles, was reale Szenarien widerspiegelt, mit denen Ihr Agent konfrontiert sein wird.
2. Zeigen Sie eine Vorschau der Antwort des Agenten für einen zufälligen Nutzer, einen bestehenden Nutzer oder einen angepassten Nutzer an.
3. Bitte wählen Sie **„Antwort simulieren**“. Der Agent führt die von Ihnen festgelegten Konfigurationen aus und zeigt die entsprechenden Ergebnisse an. Testläufe werden auf Ihr tägliches Ausführungslimit angerechnet.

![Agentenkonsole mit dem Fenster der Vorschau zum Testen eines angepassten Agenten. Die Schnittstelle zeigt ein Feld „Beispeleingaben“ mit Beispielkundendaten, einen Button „Test ausführen“ und einen Antwortbereich, in dem die Ausgabe des Agenten angezeigt wird.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Bitte überprüfen Sie die Ergebnisse kritisch. Bitte berücksichtigen Sie die folgenden Fragen:

- Entspricht der Text dem Markenimage?
- Leitet die Entscheidungslogik die Kund:innen wie beabsichtigt weiter?
- Sind die berechneten Werte korrekt?

Sollte etwas nicht korrekt funktionieren, führen Sie ein Update der Konfiguration des Agenten durch und führen Sie den Test erneut durch. Führen Sie einige unterschiedliche Eingaben durch, um zu beobachten, wie sich der Agent an verschiedene Szenarien anpasst, insbesondere an Randfälle wie fehlende Daten oder ungültige Antworten.

{% alert tip %}
Bitte vermeiden Sie es, dem Agenten genau mitzuteilen, was Sie nicht möchten, dass er tut. LLMs können diesen Inhalt dennoch generieren, wenn Sie dies in den Anweisungen erwähnen.
{% endalert %}

### Schritt 6: Bitte wenden Sie sich an Ihren Vertreter.

Ihr Agent ist nun einsatzbereit. Weitere Informationen referenzieren Sie unter [Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

## Ähnliche Artikel  

- [Referenz für Vertreter]({{site.baseurl}}/user_guide/brazeai/agents/reference/)
