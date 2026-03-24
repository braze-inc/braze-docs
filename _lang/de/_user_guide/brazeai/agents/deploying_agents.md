---
nav_title: Agenten bereitstellen
article_title: Angepasste Agenten bereitstellen
description: "Erfahren Sie, wie Sie angepasste Agenten in Braze einsetzen können, nachdem Sie diese erstellt haben."
alias: /deploying-agents/
page_order: 2
---

# Angepasste Agenten bereitstellen

> Erfahren Sie, wie Sie angepasste Agenten in Canvas-Schritten oder Katalogfeldern einsetzen können, nachdem Sie diese erstellt haben. Für eine Einführung, sehen Sie [bitte Braze Agents.]({{site.baseurl}}/user_guide/brazeai/agents/)

## Agenten in Canvas  

Sie können Agenten als Schritte in einem Prozess einsetzen, um Nachrichten zu personalisieren oder Entscheidungen in Realtime zu unterstützen. Detaillierte Schritte zur Einrichtung werden in der Referenz zum [Agent-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/) referenziert.

### Anwendungsfälle

| Anwendungsfall | Beschreibung |
| --- | --- |
| Lead-Bewertung und -Qualifizierung | Verwenden Sie einen Agentenschritt, um eingehende Leads auf einer Skala (z. B. 1-10) zu bewerten. Leiten Sie Nutzer:innen mit einer Punktzahl über einem bestimmten Schwellenwert in Nurture-Pfade weiter und disqualifizieren Sie gleichzeitig Leads mit geringer Eignung. |
| Dynamische Nachrichtenpersonalisierung | Lassen Sie einen Agenten Betreffzeilen, Produktempfehlungen oder Nachrichtentexte auf Grundlage von Nutzerattributen oder aktuellen Verhaltensweisen generieren. Die Antwort kann direkt in einen Schritt für Nachrichten eingefügt werden. |
| Bearbeitung von Kundenfeedback | Leiten Sie Kundenkommentare an einen Mitarbeiter weiter, um die Stimmung zu analysieren und einfühlsame Follow-up-Nachrichten zu erstellen. Bei besonders wertvollen Nutzer:innen kann der Mitarbeiter die Antwort eskalieren oder Vergünstigungen hinzufügen. |
| Intelligentes Routing | Verwenden Sie Agent-Ausgaben (boolesch oder numerisch), um Nutzer:innen in verschiedene Canvas-Pfade aufzuteilen. Beispielsweise können Nutzer:innen als „gefährdet“ oder „gesund“ klassifiziert und die Häufigkeit des Messaging-Verkehrs entsprechend angepasst werden. |
| Umfrage oder Interpretation der Antworten | Lassen Sie einen Agenten offene Antworten auf Umfragen oder Freitextfelder analysieren und strukturierte Werte zurückgeben (z. B. Kategorisierung von Absichten oder Bedürfnissen), die nachgelagerte Pfade steuern. |
| Mehrstufige Argumentation | Konfigurieren Sie einen Agenten, um Kontextfelder zu kombinieren und komplexe Entscheidungen zu treffen, wie beispielsweise die Empfehlung der nächstbesten Maßnahme (E-Mail, SMS oder persönliche Kontaktaufnahme) auf der Grundlage mehrerer Attribute der Nutzer:innen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Vertreter in Katalogen  

Sie können einen Agenten auf Katalogfelder anwenden, sodass er automatisch Werte für jede Zeile generiert oder berechnet. Der Agent wird auch für neue Zeilen ausgeführt, die in Zukunft zum Katalog hinzugefügt werden. 

### Anwendungsfälle

| Anwendungsfall | Beschreibung |
| --- | --- |
| Produktbeschreibungen erstellen | Erstellen Sie automatisch kurze Marketingtexte für neue Katalogeinträge, indem Sie beispielsweise aus strukturierten Produktdaten wie Name, Kategorie und Features eine ansprechende Beschreibung generieren. |
| Produkteigenschaften anreichern | Bitte ergänzen Sie fehlende Angaben wie Farbfamilie, Stil oder Saison anhand des Produktnamens und der Produktdetails. Wenn ein Produkt beispielsweise den Namen „Laguna Polarized Sunglasses“ trägt, könnte der Mitarbeiter den Stil als „Sport“ und die Farbfamilie als „Blau“ zuordnen. |
| Abgeleitete Felder berechnen | Verwenden Sie vorhandene Felder, um neue Daten zu generieren, wie beispielsweise einen „Fit-Score“ basierend auf Attributen oder einen „Beliebtheits-Tag“ aus Verkaufszahlen und Bewertungszahlen. |
| Artikel kategorisieren oder mit Tags versehen | Weisen Sie Tags für die Empfehlungslogik zu, damit Personalisierungsmodelle Produkte effektiver segmentieren können. Beispielsweise können Sie Produkte mit „Outdoor“, „festivaltauglich“ oder „Premium“ mit Tags kennzeichnen. |
| Lokalisierung der Inhalte | Übersetzen Sie Katalogtexte für globale Kampagnen in andere Sprachen oder passen Sie Tonfall und Länge für regionsspezifische Kanäle an. Bitte übersetzen Sie beispielsweise „Classic Clubmaster Sunglasses“ ins Spanische mit „Gafas de sol Classic Clubmaster“ oder kürzen Sie Beschreibungen für SMS-Kampagnen. |
| Zusammenfassung von Bewertungen oder Feedback | Fassen Sie die Stimmung oder das Feedback in einem neuen Feld zusammen, beispielsweise durch die Vergabe von Stimmungsbewertungen wie „Positiv“, „Neutral“ oder „Negativ“ oder durch die Erstellung einer kurzen Textzusammenfassung wie „Die meisten Kund:innen erwähnen die hervorragende Passform, bemerken jedoch den langsamen Versand.“ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Schritte

![Ein Agentenschritt in einem Katalogfeld.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Um einen Agenten zu Ihrem Katalogfeld hinzuzufügen:

1. Bitte fügen Sie in Ihrem Katalog ein neues Feld hinzu.  
2. Auswählen Sie **„KI-Agent anwenden**“.
3. Bitte weisen Sie diesem Feld einen Mitarbeiter zu.  
4. Bitte wählen Sie aus, welche Spalten als Eingabe übergeben werden sollen. Wenn keine ausgewählt sind, hat der Agent Zugriff auf alle Spalten im Katalog.  
5. Entscheiden Sie, ob der Agent Felder neu berechnen soll, wenn Updates an den Katalog vorgenommen werden. Wenn Sie diese Option nicht auswählen, wird der Agent nur einmal pro Zeile ausgeführt.
6. Wählen Sie **„Felder hinzufügen“,** um den Agenten bereitzustellen und die Kostenschätzungen zu überprüfen. Das Modal **„Kostenvoranschlag“** zeigt an, wie oft der Agent diesen Katalog ausführen wird, was in etwa der Gesamtzahl der Zeilen entspricht. Um fortzufahren, wählen Sie **bitte „Bestätigen**“.

### Wie Katalogagenten funktionieren  

Nach dem Start führt der Agent jede Zeile aus und wertet sie aus, wobei er die ausgewählten Spalten in seinen Kontext einbezieht, um eine Ausgabe zu erzeugen. Agenten werden auf allen neuen Zeilen ausgeführt, die nach der Bereitstellung des Agenten hinzugefügt werden. Wenn Sie **„Bei Aktualisierung der Katalogzeilen neu berechnen“** ausgewählt haben, werden alle Werte für dieses Feld aktualisiert, wenn sich vorhandene Quellfelder ändern.

Sie können die Felder in Ihrem Katalog, die Agenten verwenden, aktualisieren und bearbeiten. Um einen Agenten aus einer Spalte zu entfernen, deaktivieren Sie bitte die Option **„KI-Agent anwenden**“. Dadurch wird die Spalte wieder in eine nicht-agentische Spalte zurückgesetzt, und die Felder behalten die letzten Werte bei, die der Agent bei seiner letzten Ausführung im Katalog angewendet hat.

Zirkuläre Referenzen in Katalogen werden nicht unterstützt, was bedeutet, dass das folgende Szenario nicht auftreten kann:

- Agentische Spalte 1 verwendet die agentialische Spalte 2 als Eingabe.
- Agentische Spalte 2 verwendet die agentialische Spalte 1 als Eingabe.

![Die Option, „KI-Agent anwenden“ für ein Katalogfeld auszuwählen.]({% image_buster /assets/img/ai_agent/edit_agent_column.png %}){: style="max-width:80%;"}

{% alert note %}
Katalogagenten können nur Eingabewerte von bis zu 25 KB pro Zeile verarbeiten.
{% endalert %}

#### Antwortfelder definieren

Wenn Ihr Agent [Felder]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/?tab=fields#advanced-schemas) als Ausgabeformat verwendet, können Sie das entsprechende Feld aus dem Agenten für **das Antwortfeld** auswählen, das im Katalogfeld verwendet werden soll. 

Angenommen, Sie verfügen über einen Agenten, der Produktbeschreibungen zu einem Katalog mit den folgenden Feldern hinzufügt, um das Ausgabeformat zu strukturieren:

| Feldname | Wert |
| --- | --- |
| **Beschreibung** | Text |
| **confidence_score_out_of_ten** | Zahl |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Sie können ein Feld mit dem Namen**product_description**  zu einem Katalog hinzufügen und **„Beschreibung”** als Antwort**feld** auswählen, um die Spalte mit den Beschreibungen des Agenten zu füllen.

![Ein Feld, auf"product_description" das der Agent „Descriptor“ angewendet wurde. Die Ausgabe „description“ wird als Antwortfeld ausgewählt.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

Sie können die vom Agenten generierte Zelle auch manuell überschreiben, indem Sie **„Artikel bearbeiten“** auswählen und die vom Agenten generierte Beschreibung mit Ihren Änderungen aktualisieren. Um zur vom Agenten generierten Beschreibung zurückzukehren, wählen Sie bitte das Aktualisierungssymbol in der Zelle aus.

### Fehlerbehandlung in Katalogen  

- Fehlgeschlagene Katalogaufrufe werden nicht wiederholt.
- Wenn der API-Aufruf an den Basismodellanbieter einen Fehler zurückgibt, beispielsweise einen ungültigen API-Schlüssel oder einen Fehler bei den Rate-Limits, wird der Feldwert nicht aktualisiert.
- Sie können die Protokolle des Agenten überprüfen, um Details zu fehlgeschlagenen Ausführungen zu erhalten.

## Bitte überwachen Sie Ihren Agenten.

Im Abschnitt **„Verwendung“** Ihres Agenten können Sie referenzieren und zu den Stellen navigieren, an denen der Agent in Katalogen und Canvases aktiv verwendet wird.

![Der Abschnitt „Agentenverwendung“ zeigt zwei aktive Agenten und einen inaktiven Agenten für Canvase an.]({% image_buster /assets/img/ai_agent/agent_usage.png %})

Im Abschnitt **„Protokolle“** Ihres Agenten können Sie die tatsächlichen Anrufe Ihrer Agenten überwachen, die in Ihren Canvases und Katalogen stattfinden. Sie können nach Informationen wie dem Datumsbereich, dem Ergebnis (Erfolg oder Misserfolg) oder dem Standort des Anrufs filtern. Sie können auch **„CSV exportieren“** auswählen, um nur die auf der aktuellen Seite angezeigten Protokolle zu exportieren.

{% alert tip %}
Sie können auch Fehler bezüglich des täglichen Aufruflimits im Nachrichtenaktivitätsprotokoll überwachen.
{% endalert %}

![Protokolle für einen Agenten-KI-Sentiment-Score.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

Auswählen Sie **„Ansicht“** für einen bestimmten Agentenanruf, um die Eingabe, Ausgabe und ID des Nutzers oder der Nutzerin anzuzeigen.

![Das Panel für einen Agenten mit dem Namen „Random Sports Assignment“, das die Eingabeaufforderung, die Ausgabeantwort und eine zugehörige ID eines Nutzers anzeigt.]({% image_buster /assets/img/ai_agent/agent_logs_view.png %})

### Verwenden Sie Currents

Sie können diese Currents-Ereignisse auch verwenden, um auf die Kafka-Datensatzschemata zuzugreifen:

- Vom Agenten ausgeführte Ereignisse
- Toolaufrufereignisse

Weitere Informationen zum Thema [Engagement]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) im Zusammenhang [mit Nachrichten]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) finden Sie [im Glossar]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) [zu Ereignissen]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) im Zusammenhang mit Nachrichten.

## Ähnliche Artikel  

- [Referenz für Vertreter]({{site.baseurl}}/user_guide/brazeai/agents/reference/)