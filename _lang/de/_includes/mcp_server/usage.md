# Verwendung des Braze MCP-Servers

> Erfahren Sie, wie Sie mit Ihren Braze-Daten mithilfe von Tools wie Claude und Cursor in natürlicher Sprache interagieren können. Weitere allgemeine Informationen finden Sie unter [Braze MCP-Server]{% if include.section == "user" %}.{{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/mcp_server/){% endif %}

{% multi_lang_include mcp_server/beta_alert.md %}

## Voraussetzungen

Bevor Sie dieses Feature nutzen können, müssen Sie den Braze MCP-Server einrichten{% if include.section == "user" %}.{{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}

## Bewährte Praktiken

Wenn Sie den Braze MCP-Server über natürliche Sprachtools wie Claude und Cursor verwenden, beachten Sie bitte die folgenden Hinweise, um optimale Ergebnisse zu erzielen:

- LLMs können Fehler machen, daher sollten Sie ihre Antworten stets überprüfen.
- Für die Analyse der Daten ist es wichtig, den benötigten Zeitbereich genau zu definieren. Kürzere Entfernungen liefern häufig genauere Ergebnisse.
- Bitte verwenden Sie [die](https://www.braze.com/resources/articles/glossary) genaue [Braze-Terminologie,](https://www.braze.com/resources/articles/glossary) damit Ihr LLM die richtige Funktion aufruft.
- Sollten die Ergebnisse unvollständig erscheinen, bitten Sie Ihren LLM, fortzufahren oder tiefer zu recherchieren.
- Bitte probieren Sie kreative Anregungen aus. Je nach Ihrem MCP-Client können Sie möglicherweise CSV-Dateien oder andere nützliche Dateien exportieren.

## Anwendungsbeispiele

Nach der Einrichtung des Braze MCP-Servers können Sie über Tools wie Claude oder Cursor in natürlicher Sprache mit{% if include.section == "user" %} Braze interagieren.{{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %} Hier sind einige Beispiele für den Einstieg:

### Welche Funktionen stehen mir in Braze zur Verfügung?

{% tabs %}
{% tab Claude %}
![„Welche Braze-Funktionen stehen mir zur Verfügung?“ – diese Frage wird in Claude gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![Die Frage „Welche Braze-Funktionen stehen mir zur Verfügung?“ wird in Cursor gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

### Erhalten Sie detaillierte Informationen zu einer Canvas-ID.

{% tabs %}
{% tab Claude %}
![Die Frage „Details zu einer Canvas-ID abrufen“ wird in Claude gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![„Details zu einer Canvas-ID abrufen“ wird in Cursor abgefragt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

### Bitte zeigen Sie mir meine letzten Canvases.

{% tabs %}
{% tab Claude %}
![Die Frage „Meine aktuellen Canvases anzeigen“ wird in Claude gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![Die Frage „Meine aktuellen Canvases anzeigen“ wurde in Cursor gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}
