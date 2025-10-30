# Verwendung des Braze MCP Servers

> Lernen Sie, wie Sie mit Hilfe von Tools wie Claude und Cursor über natürliche Sprache mit Ihren Daten in Braze interagieren können. Weitere allgemeine Informationen finden Sie unter [Braze MCP Server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "Entwickler:in" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Voraussetzungen

Bevor Sie dieses Feature nutzen können, müssen Sie [den Braze MCP Server einrichten]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "Entwickler:in" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Bewährte Praktiken

Wenn Sie den Braze MCP Server über natürlichsprachliche Tools wie Claude und Cursor verwenden, sollten Sie die folgenden Tipps beachten, um die besten Ergebnisse zu erzielen:

- LLMs können Fehler machen, daher sollten Sie ihre Antworten immer doppelt überprüfen.
- Für die Datenanalyse sollten Sie sich über den Zeitraum im Klaren sein, den Sie benötigen. Kürzere Reichweiten liefern oft genauere Ergebnisse.
- Verwenden Sie die genaue [Terminologie von Braze](https://www.braze.com/resources/articles/glossary), damit Ihr LLM die richtige Funktion aufruft.
- Wenn die Ergebnisse unvollständig erscheinen, fordern Sie Ihren LLM auf, fortzufahren oder tiefer zu graben.
- Versuchen Sie es mit kreativen Impulsen! Je nach MCP-Client können Sie eine CSV-Datei oder andere nützliche Dateien exportieren.

## Beispiele für den Gebrauch

Nach der [Einrichtung des Braze MCP Servers]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "Entwickler:in" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, können Sie mit Hilfe von Tools wie Claude oder Cursor über natürliche Sprache mit Braze interagieren. Hier sind einige Beispiele für den Anfang:

### Welche Braze-Funktionen stehen mir zur Verfügung?

{% tabs %}
{% tab Claude %}
![Die Frage 'Welche Braze-Funktionen stehen mir zur Verfügung?' wird in Claude gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![Die Frage 'Welche Funktionen sind in Braze verfügbar?' wird in Cursor gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

### Details zu einer Canvas ID abrufen

{% tabs %}
{% tab Claude %}
!['Details zu einer Canvas ID abrufen' wird in Claude gefragt und beantwortet.]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['Details zu einer Canvas ID abrufen' wird in Cursor gefragt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

### Meine letzten Canvases anzeigen

{% tabs %}
{% tab Claude %}
!['Zeige meine letzten Canvases' wird in Claude gefragt und beantwortet.]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['Zeige meine letzten Canvases' wird in Cursor gefragt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}
