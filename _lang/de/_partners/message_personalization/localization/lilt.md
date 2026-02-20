---
nav_title: LILT
article_title: LILT
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und LILT."
alias: /partners/lilt/
page_type: partner
search_tag: Partner
---

# LILT

> [LILT](https://lilt.com/) ist die komplette KI-Lösung für die Übersetzung und Inhaltserstellung in Unternehmen. Mit KI-Agenten und vollautomatisierten Workflows ermöglicht LILT globalen Unternehmen die Skalierung und Optimierung ihres Inhalts-, Produkt-, Kommunikations- und Supportbetriebs.

_Diese Integration wird von LILT gepflegt._

## Über diese Integration

Der LILT Braze Connector ermöglicht die Übersetzung von HTML-Templates für E-Mails mit KI-Geschwindigkeit und in Unternehmensqualität. Fragen Sie eine markengerechte Sofortübersetzung oder eine qualitätsgesicherte verifizierte Übersetzung an und erhalten Sie mehrsprachige E-Mail-Inhalte von LILT direkt in Braze. 

## Anwendungsfälle

Die Integration von LILT Braze automatisiert und beschleunigt den Übersetzungsprozess und ermöglicht es globalen Marketing Teams, ihre mehrsprachigen Kampagnen schnell und mit Markenkonsistenz einzuführen.

### Rationalisierter globaler Start von Kampagnen

Führen Sie Marketing Kampagnen in mehreren Regionen gleichzeitig ein, ohne dass es zu Verzögerungen durch manuelle Übersetzungsübergaben kommt.

- **Szenario:** Ihr Unternehmen bringt ein neues Produkt in 10 Ländern auf den Markt.
- **Lösung:** Ihr Marketing Team stellt das englische Template für E-Mails in Braze fertig, versieht es mit Tags ( `LILT: Ready`), und der LILT Connector zieht den Inhalt automatisch ab. Domänenspezifische Linguisten überprüfen die KI-Übersetzungsaufforderungen in der LILT-Plattform zur Qualitätssicherung, und der Konnektor pusht die übersetzten Versionen zurück nach Braze.
- **Profitieren Sie davon:** Verkürzt die Markteinführungszeit Ihrer globalen Kampagnen von Tagen auf Stunden, so dass alle Kund:innen die Ankündigung eines neuen Produkts zum optimalen Zeitpunkt erhalten können.

### Sofortige markengerechte Lokalisierung

Nutzen Sie die KI von LILT für sofortige, markengerechte Übersetzungen für zeitkritische Kommunikation.

- **Szenario:** Sie müssen sofort E-Mails für einen Flash-Sale, ein zeitlich begrenztes Angebot oder eine dringende Unterbrechung des Dienstes in fünf geografischen Märkten versenden.
- **Lösung:** Sie taggen die E-Mail Template mit `LILT: Instant`. LILT nutzt seine KI und die für Ihr Unternehmen spezifischen linguistischen Ressourcen (wie Terminologie und Stilrichtlinien), um innerhalb von Minuten eine hochwertige, markenkonsistente Übersetzung zu erstellen.
- **Profitieren Sie davon:** Zulässig ist eine hyperresponsive Kommunikation in Realtime, ohne dass die Stimme der Marke oder die Qualität beeinträchtigt wird, was für zeitkritisches Marketing entscheidend ist.

## Voraussetzungen

| Voraussetzung       | Beschreibung |                        
|-----------------------|-----------------|
| Ein LILT-Konto   | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein LILT-Konto.  |
| Ein Braze REST API-Schlüssel  | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen:<br>- `templates.email.create`<br>- `templates.email.update`<br>- `templates.email.info`<br>- `templates.email.list`<br>- `templates.translations.source.get`<br>- `templates.translations.update`<br>- `templates.translations.get`<br>- `templates.translations.all.get`. <br><br> Erstellen Sie diesen Schlüssel im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. |
| Ein Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.  |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}


## Integration

### Schritt 1: Konfigurieren Sie den LILT Braze Konnektor

1. Melden Sie sich bei LILT an und gehen Sie dann zu **Verbinden** > **Neuer Konnektor** > **Braze**.
	
![Lötbarer Konnektor in LILT.]({% image_buster /assets/img/lilt/image_1_select_connector.png %})

{: start="2"}
2\. Wählen Sie den gewünschten Lokalisierungs-Workflow für Ihre Braze-Inhalte aus.

![Lötarbeiten in LILT.]({% image_buster /assets/img/lilt/image_2_select_workflow.png %})	

{: start="3"}
3\. Geben Sie die erforderlichen Konfigurationsdetails ein und überprüfen Sie sie:
- Ihr Braze API-Schlüssel
- Braze REST Endpunkt

![Vollständige API-Zugangsdaten.]({% image_buster /assets/img/lilt/image_3_api_creds.png %})	

{: start="4"}
4\. Wählen Sie **Überprüfen**, um die Einrichtung zu testen. Nachdem die Verbindung bestätigt wurde, speichern Sie die Konfiguration.

### Schritt 2: Bereiten Sie Ihren Braze Workspace vor

1. Aktivieren Sie die Mehrsprachigkeit in den Einstellungen Ihres Braze Workspace.

![Lokalisierung in Braze einrichten.]({% image_buster /assets/img/lilt/image_4_lilt_locales.png %})	

{: start="2"}
2\. Erstellen Sie in Braze die folgenden Tags für Ihren LILT-Workflow: 
- `LILT: Ready`
- `LILT: In progress`
- `LILT: Sent to LILT`
- `LILT: Delivered`
- `LILT: Needs Attention`
- `LILT: Instant`

![Richten Sie LILT-Tags in Braze ein.]({% image_buster /assets/img/lilt/image_5_lilt_tags.png %})	

{: start="3"}
### Schritt 3: Senden Sie Inhalte zur Übersetzung an LILT 

1. Nachdem Sie den LILT Braze Connector eingerichtet haben, verwenden Sie Liquid-Tags für die Übersetzung in Ihren E-Mail Templates, um die zu übersetzenden Inhalte zu identifizieren. 
- Beispiel:  {% raw %}`{% translation id_0 %}`Hallo, `{{first_name}}!{% endtranslation %}`{% endraw %}
2. Starten Sie die Übersetzung, indem Sie den Tag des Templates aktualisieren, um den gewünschten Arbeitsablauf anzugeben: 
- Wählen Sie `LILT: Ready` für eine überprüfte Übersetzung
- Wählen Sie `LILT: Instant` für markengerechte Sofortübersetzung
3. Der LILT Braze Connector wird zu dem von Ihnen festgelegten Zeitpunkt ausgeführt, um die getaggten Inhalte in LILT zu übernehmen. Verfolgen Sie den Übersetzungsfortschritt, denn die Tags für die Inhalte werden in Braze automatisch aktualisiert und spiegeln den Stand Ihres Projekts wider. 
	
![Braze E-Mail Template mit Tags für die Übersetzung.]({% image_buster /assets/img/lilt/image_6_braze_template.png %})	