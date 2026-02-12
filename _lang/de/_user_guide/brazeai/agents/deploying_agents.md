---
nav_title: Agenten bereitstellen
article_title: Angepasste Agenten bereitstellen
description: "Lernen Sie, wie Sie angepasste Agenten in Braze einsetzen können, nachdem Sie sie erstellt haben."
alias: /deploying-agents/
---

# Angepasste Agenten bereitstellen

> Erfahren Sie, wie Sie angepasste Agenten in Canvas-Schritten oder Katalogfeldern verwenden können, nachdem Sie sie erstellt haben. Eine Einführung finden Sie unter [Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/). 

{% alert important %}
Braze-Agenten befinden sich derzeit in der Beta-Phase. Wenn Sie Hilfe benötigen, wenden Sie sich an Ihren Customer-Success-Manager:in.
{% endalert %}

## Agentennutzung

Im Abschnitt **Agentennutzung** Ihres Agenten können Sie referenzieren und navigieren, wo der Agent in Katalogen und Canvase aktiv verwendet wird.

![Abschnitt Agentennutzung, der zwei aktive Agenten und einen inaktiven Agenten für Canvase anzeigt.]( {% image_buster /assets/img/ai_agent/agent_usage.png %} )

## Agenten in Canvas  

Sie können Agenten als Schritte auf einer Reise einsetzen, um Nachrichten zu personalisieren oder Entscheidungen in Echtzeit zu treffen. Detaillierte Einrichtungsschritte finden Sie unter [Agent Step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/).

### Anwendungsfälle

| Anwendungsfall | Beschreibung |
| --- | --- |
| Lead Scoring und Qualifizierung | Verwenden Sie einen Agentenschritt, um eingehende Leads auf einer Skala zu bewerten (z.B. 1-10). Leiten Sie Nutzer:innen mit einer Punktzahl oberhalb eines Schwellenwerts in Nurture-Pfade weiter, während Sie Leads mit geringer Eignung disqualifizieren. |
| Dynamische Personalisierung von Nachrichten | Lassen Sie einen Agenten Betreffzeilen, Produktempfehlungen oder Nachrichten auf der Grundlage von Nutzer:innen-Attributen oder aktuellem Verhalten erstellen. Die Antwort kann direkt in einen Schritt der Nachricht eingefügt werden. |
| Umgang mit Kunden:in | Geben Sie Kommentare von Kund:innen an einen Agenten weiter, um die Stimmung zu analysieren und einfühlsame Nachrichten zu erstellen. Für hochwertige Nutzer:innen könnte der Agent die Antwort eskalieren oder Vergünstigungen anbieten. |
| Intelligentes Routing | Verwenden Sie Agentenausgaben (boolesch oder numerisch), um Nutzer:innen in verschiedene Canvas-Pfade aufzuteilen. Klassifizieren Sie beispielsweise Nutzer:innen als "gefährdet" oder "gesund" und passen Sie die Kadenz des Messagings entsprechend an. |
| Auswertung von Umfragen oder Antworten | Lassen Sie einen Agenten Antworten auf Umfragen mit offenem Ende oder Freitextfelder analysieren und strukturierte Werte zurückgeben (z. B. zur Kategorisierung von Absichten oder Bedürfnissen), die nachgelagerte Pfade steuern. |
| Mehrstufige Argumentation | Konfigurieren Sie einen Agenten so, dass er Kontextfelder kombiniert und komplexe Entscheidungen trifft, wie z.B. die Empfehlung der nächstbesten Aktion (E-Mail, SMS oder persönliche Ansprache) auf der Grundlage mehrerer Nutzer:innen-Attribute. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Agenten in Katalogen  

Sie können einen Agenten auf Katalogfelder anwenden, so dass er automatisch Werte für jede Zeile erzeugt oder berechnet. Der Agent wird auch bei neuen Zeilen ausgeführt, die dem Katalog in Zukunft hinzugefügt werden. 

### Anwendungsfälle

| Anwendungsfall | Beschreibung |
| --- | --- |
| Produktbeschreibungen generieren | Erstellen Sie automatisch kurze Marketingtexte für neue Katalogeinträge, indem Sie z.B. aus strukturierten Produktdaten wie Name, Kategorie und Features eine einprägsame Beschreibung generieren. |
| Anreicherung der Attribute von Produkten | Ergänzen Sie fehlende Werte wie Farbfamilie, Stil oder Saison anhand eines Produktnamens und der Details. Wenn ein Produkt zum Beispiel "Laguna Polarized Sunglasses" heißt, könnte der Agent den Stil als "Sport" und die Farbfamilie als "Blau" zuordnen. |
| Abgeleitete Felder berechnen | Verwenden Sie vorhandene Felder, um neue Daten zu generieren, z.B. einen "Fit Score" auf der Grundlage von Attributen oder einen "Popularitäts-Tag" aus Verkäufen und Bewertungen. |
| Artikel kategorisieren oder taggen | Weisen Sie Tags für die Empfehlungslogik zu, damit Personalisierungsmodelle Produkte effektiver segmentieren können. Kennzeichnen Sie Produkte zum Beispiel als "Outdoor", "Festival-tauglich" oder "Premium". |
| Inhalte lokalisieren | Übersetzen Sie den Katalogtext für globale Kampagnen in eine andere Sprache, oder passen Sie Ton und Länge für regionalspezifische Kanäle an. Übersetzen Sie zum Beispiel "Classic Clubmaster Sonnenbrille" ins Spanische als "Gafas de sol Classic Clubmaster" oder kürzen Sie Beschreibungen für SMS Kampagnen. |
| Fassen Sie Bewertungen oder Feedback zusammen | Fassen Sie die Stimmung oder das Feedback in einem neuen Feld zusammen, indem Sie z.B. Stimmungswerte wie Positiv, Neutral oder Negativ vergeben oder eine kurze Textzusammenfassung wie "Die meisten Kund:in erwähnen die gute Passform, bemängeln aber den langsamen Versand." erstellen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Schritte

![Ein Agent-Schritt in einem Katalogfeld.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Um einen Agenten zu Ihrem Katalogfeld hinzuzufügen:

1. Fügen Sie in Ihrem Katalog ein neues Feld hinzu.  
2. Wählen Sie **KI-Agent anwenden**.
3. Weisen Sie diesem Feld einen Agenten zu.  
4. Wählen Sie aus, welche Spalten als Eingabe übergeben werden sollen. Wenn Sie keine auswählen, hat der Agent Zugriff auf alle Spalten des Katalogs.  
5. Legen Sie fest, ob der Agent die Felder neu berechnen soll, wenn Katalogzeilen aktualisiert werden. Wenn Sie diese Option nicht auswählen, wird der Agent nur einmal pro Zeile ausgeführt.
6. Wählen Sie **Felder hinzufügen** aus, um den Agenten einzusetzen und die Kostenschätzungen zu überprüfen. Das Modal **Kostenschätzung** zeigt an, wie oft der Agent für diesen Katalog ausgeführt wird, was ungefähr der Gesamtzahl der Zeilen entspricht. Um fortzufahren, wählen Sie **Bestätigen**.

### Wie Katalogagenten laufen  

Nach dem Start wird der Agent ausgeführt und wertet jede Zeile aus, wobei er die ausgewählten Spalten in seinen Kontext aufnimmt, um eine Ausgabe zu erzeugen. Agenten werden auf allen neuen Zeilen ausgeführt, die nach der Verteilung des Agenten hinzugefügt werden. Wenn Sie **Neu berechnen bei Update von Katalogzeilen** ausgewählt haben, werden alle Werte für dieses Feld aktualisiert, wenn sich bestehende Quellfelder ändern.

Sie können die Felder in Ihrem Katalog, die Agenten verwenden, aktualisieren und bearbeiten. Um einen Agenten aus einer Spalte zu entfernen, deaktivieren Sie die Option **KI-Agent anwenden**. Dadurch wird die Spalte in eine nicht-agentische Spalte umgewandelt und die Felder behalten die letzten Werte, die der Agent bei der letzten Ausführung auf den Katalog angewendet hat.

Zirkuläre Referenzen in Katalogen werden nicht unterstützt, d.h. das folgende Szenario kann nicht auftreten:

- Agentenspalte 1 verwendet Agentenspalte 2 als Eingabe
- Agentenspalte 2 verwendet Agentenspalte 1 als Eingabe

![Die Option zum Auswählen von "KI-Agent anwenden" für ein Katalogfeld.]({% image_buster /assets/img/ai_agent/edit_agent_column.png %}){: style="max-width:80%;"}

{% alert note %}
Während der Beta-Phase sind die Katalogagenten auf die Verarbeitung von Eingabewerten bis zu 25 KB pro Zeile beschränkt.
{% endalert %}

#### Definieren Sie Antwortfelder

Wenn Ihr Agent [Felder]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#fields) als Ausgabeformat verwendet, können Sie das entsprechende Feld aus dem Agenten für **Antwortfeld** auswählen, um es im Katalogfeld zu verwenden. 

Nehmen wir an, Sie haben einen Agenten, der einem Katalog Produktbeschreibungen hinzufügt und das Ausgabeformat mit den folgenden Feldern strukturiert:

| Feldname | Wert |
| --- | --- |
| **Beschreibung** | Text |
| **confidence_score_out_of_ten** | Zahl |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Sie können ein Feld namens **product_description** zu einem Katalog hinzufügen und **Beschreibung** als **Antwortfeld** auswählen, um die Spalte mit den Beschreibungen des Agenten zu füllen.

![Ein Feld "product_description", auf das der Agent "Descriptor" angewendet wurde. Die Ausgabe "Beschreibung" ist als Antwortfeld ausgewählt.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

Sie können die vom Agenten erstellte Zelle auch manuell überschreiben, indem Sie **Artikel bearbeiten** auswählen und die vom Agenten erstellte Beschreibung mit Ihren Änderungen aktualisieren. Um Ihre Bearbeitungen wieder auf die vom Agenten generierte Beschreibung zurückzusetzen, wählen Sie das Aktualisierungssymbol in der Zelle aus.

### Fehlerbehandlung in Katalogen  

- Fehlgeschlagene Katalogaufrufe werden nicht wiederholt.
- Wenn der API-Aufruf an den Foundational Model Provider einen Fehler zurückgibt, z.B. einen ungültigen API-Schlüssel oder einen Rate-Limits-Fehler, wird der Feldwert nicht aktualisiert.
- In den Protokollen des Agenten können Sie Details zu fehlgeschlagenen Läufen nachlesen.
