# Der Braze MCP Server

> Erfahren Sie mehr über den Braze MCP Server, eine sichere, schreibgeschützte Verbindung, über die KI-Tools wie Claude und Cursor auf nicht PII-geschützte Daten von Braze zugreifen können, um Fragen zu beantworten, Trends zu analysieren und Insights zu liefern, ohne die Daten zu verändern.

{% multi_lang_include mcp_server/beta_alert.md %}

## Was ist das Model Context Protocol (MCP)?

​Das Model Context Protocol (MCP) ist ein Standard, mit dem KI-Agenten eine Verbindung zu Daten einer anderen Plattform herstellen und mit diesen arbeiten können. Sie besteht aus zwei Hauptteilen:

- **MCP Client:** Die Anwendung, in der der KI-Agent läuft, z. B. Cursor oder Claude.
- **MCP Server:** Ein Dienst, der von einer anderen Plattform wie Braze bereitgestellt wird und definiert, welche Tools die KI verwenden kann und auf welche Daten sie zugreifen kann.

## Über den Braze MCP Server

Nach der [Einrichtung des Braze MCP-Servers]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, können Sie KI-Tools wie Agenten, Assistenten und Chatbots direkt mit Braze verbinden, was es ihnen erlaubt, aggregierte Daten wie Canvas- und Kampagnen-Analytics, angepasste Attribute, Segmente und mehr zu lesen. Der Braze MCP Server ist ideal für:

- Aufbau von KI-gestützten Tools, die Braze-Kontext benötigen.
- CRM-Ingenieure, die mehrstufige Arbeitsabläufe für Agenten erstellen.
- Technische Marketer, die mit natürlichsprachlichen Abfragen experimentieren.

Der Braze MCP Server unterstützt 38 schreibgeschützte Endpunkte, die keine Daten aus Nutzer:innen-Profilen zurückgeben. Sie können Ihrem Braze API-Schlüssel nur einige dieser Endpunkte zuweisen, um die Daten, auf die ein Agent zugreifen kann, weiter einzuschränken.

{% alert warning %}
Weisen Sie Ihrem API-Schlüssel keine Berechtigungen zu, die **nicht** schreibgeschützt sind. Agenten können versuchen, Daten in Braze zu schreiben oder zu löschen, was zu unbeabsichtigten Konsequenzen führen kann.
{% endalert %}

## Beispiel für die Verwendung

Sie können mit Braze über natürliche Sprache interagieren, indem Sie Tools wie Claude oder Cursor verwenden. Weitere Beispiele und bewährte Verfahren finden Sie unter [Verwendung des Braze MCP Servers]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "Entwickler:in" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
![Die Frage 'Welche Braze-Funktionen stehen mir zur Verfügung?' wird in Claude gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![Die Frage 'Welche Funktionen sind in Braze verfügbar?' wird in Cursor gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Häufig gestellte Fragen (FAQ) {#faq}

### Welche MCP-Clients werden unterstützt?

Derzeit werden nur [Claude](https://claude.ai/) und [Cursor](https://cursor.com/) offiziell unterstützt. Sie benötigen ein Konto für einen dieser Clients, um den Braze MCP Server zu verwenden.

### Auf welche Daten von Braze kann mein MCP Client zugreifen?

MCP-Clients können nur auf schreibgeschützte Endpunkte zugreifen, die nicht für den Abruf von PII ausgelegt sind. Sie können Daten in Braze nicht manipulieren.

### Kann mein MCP Client Braze Daten manipulieren?

Nein. Der MCP Server stellt nur Tools zur Verfügung, die Daten verarbeiten, die nicht PII sind und nur gelesen werden können.

### Kann ich einen MCP-Server eines Drittanbieters für Braze verwenden?

Die Verwendung eines MCP-Servers eines Drittanbieters für Braze-Daten wird nicht empfohlen. Verwenden Sie nur den offiziellen Braze MCP Server, der auf [PyPi](https://pypi.org/project/braze-mcp-server/) gehostet wird.

### Warum bietet der Braze MCP Server keinen PII- oder Schreibzugriff?

Um Daten zu schützen und gleichzeitig Innovationen zu ermöglichen, haben wir den Server so konzipiert, dass er auf Endpunkte beschränkt ist, die nur lesen können und normalerweise keine PII zurückgeben. Dies reduziert das Risiko und unterstützt gleichzeitig wertvolle Anwendungsfälle.

### Kann ich meine API-Schlüssel wiederverwenden?

Nein. Sie müssen einen neuen API-Schlüssel für Ihren MCP Client erstellen. Denken Sie daran, Ihren KI-Tools nur Zugriff auf das zu gewähren, womit Sie sich wohl fühlen, und vermeiden Sie erhöhte Berechtigungen.

### Wird der Braze MCP Server lokal oder aus der Ferne gehostet?

Derzeit wird der Braze MCP Server lokal gehostet.

### Warum listet Cursor nur Funktionen auf?

Prüfen Sie, ob Sie sich im Fragemodus oder im Agentenmodus befinden. Um den MCP Server zu verwenden, müssen Sie sich im Agentenmodus befinden.

### Was mache ich, wenn der Agent eine falsche Antwort gibt?

Wenn Sie mit Werkzeugen wie Cursor arbeiten, können Sie versuchen, das verwendete Modell zu ändern. Wenn Sie z.B. die Einstellung Auto gewählt haben, versuchen Sie, ein bestimmtes Modell zu wählen und experimentieren Sie, um herauszufinden, welches Modell für Ihren Anwendungsfall am besten geeignet ist. Sie können auch versuchen, einen neuen Chat zu starten und die Aufforderung erneut zu versuchen. 

Sollten die Probleme persistent sein, können Sie uns eine E-Mail an [mcp-product@braze.com](mailto:mcp-product@braze.com) schicken. Wenn möglich, fügen Sie ein Video ein und erweitern Sie die Anruffunktionen, damit wir sehen können, welche Anrufe der Agent versucht hat.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
