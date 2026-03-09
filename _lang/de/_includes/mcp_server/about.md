# Der Braze MCP-Server

> Erfahren Sie mehr über den Braze MCP-Server, eine sichere, schreibgeschützte Verbindung, über die KI-Tools wie Claude und Cursor auf nicht PII-bezogene Braze-Daten zugreifen können, um Fragen zu beantworten, Trends zu analysieren und Insights zu gewinnen, ohne die Daten zu verändern.

{% multi_lang_include mcp_server/beta_alert.md %}

## Was ist das Model Context Protocol (MCP)?

​Das Model Context Protocol (MCP) ist ein Standard, der es KI-Agenten ermöglicht, sich mit Daten aus einer anderen Plattform zu verbinden und mit diesen zu arbeiten. Es besteht aus zwei Hauptteilen:

- **MCP-Client:** Die Anwendung, in der der KI-Agent ausgeführt wird, wie beispielsweise Cursor oder Claude.
- **MCP-Server:** Ein Dienst, der von einer anderen Plattform wie Braze bereitgestellt wird und festlegt, welche Tools die KI verwenden und auf welche Daten sie zugreifen kann.

## Informationen zum Braze MCP-Server

Nach der Einrichtung des Braze MCP-Servers können Sie KI-Tools wie Agenten, Assistenten und{% if include.section == "user" %} Chatbots direkt mit Braze verbinden, sodass diese aggregierte Daten wie{{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %} Canvas- und {{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}KampagnenAnalytics, angepasste Attribute, Segmente und mehr lesen können. Der Braze MCP-Server eignet sich hervorragend für:

- Entwicklung von KI-gestützten Tools, die den Kontext von Braze erfordern.
- CRM-Ingenieure erstellen mehrstufige Arbeitsabläufe für Agenten.
- Technische Marketer, die mit Abfragen in natürlicher Sprache experimentieren.

Der Braze MCP-Server unterstützt 38 schreibgeschützte Endpunkte, die keine Daten aus Braze-Nutzerprofilen zurückgeben. Sie haben die Möglichkeit, nur einige dieser Endpunkte Ihrem Braze-API-Schlüssel zuzuweisen, um den Zugriff auf Daten für einen Agenten weiter einzuschränken.

{% alert warning %}
Bitte weisen Sie Ihrem API-Schlüssel keine Berechtigungen zu, die **nicht** schreibgeschützt sind. Agenten könnten versuchen, Daten in Braze zu schreiben oder zu löschen, was zu unbeabsichtigten Konsequenzen führen könnte.
{% endalert %}

## Anwendungsbeispiel

Sie können mit Braze über natürliche Sprache interagieren, indem Sie Tools wie Claude oder Cursor verwenden. Weitere Beispiele und bewährte Verfahren finden Sie unter [Verwendung des Braze MCP-Servers]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
![„Welche Braze-Funktionen stehen mir zur Verfügung?“ – diese Frage wird in Claude gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![Die Frage „Welche Braze-Funktionen stehen mir zur Verfügung?“ wird in Cursor gestellt und beantwortet.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Häufig gestellte Fragen (FAQ) {#faq}

### Welche MCP-Clients werden unterstützt?

Nur [Claude](https://claude.ai/) und [Cursor](https://cursor.com/) werden offiziell unterstützt. Sie benötigen ein Konto für einen dieser Clients, um den Braze MCP-Server nutzen zu können.

### Auf welche Braze-Daten hat mein MCP-Client Zugriff?

MCP-Clients können ausschließlich auf schreibgeschützte Endpunkte zugreifen, die nicht für den Abruf von PII vorgesehen sind. Sie dürfen keine Daten in Braze manipulieren.

### Ist es möglich, dass mein MCP-Client Braze-Daten manipuliert?

Nein. Der MCP-Server stellt nur Tools zur Verfügung, die nicht pII-Daten verarbeiten.

### Ist es möglich, einen MCP-Server eines Drittanbieters für Braze zu verwenden?

Die Verwendung eines MCP-Servers eines Drittanbieters für Braze-Daten wird nicht empfohlen. Bitte verwenden Sie ausschließlich den offiziellen Braze MCP-Server, der auf [PyPi](https://pypi.org/project/braze-mcp-server/) gehostet wird.

### Warum bietet der Braze MCP-Server keinen PII- oder Schreibzugriff an?

Um Daten zu schützen und gleichzeitig Innovationen zu ermöglichen, ist der Server auf Endpunkte beschränkt, die schreibgeschützt sind und in der Regel keine PII zurückgeben. Dies verringert das Risiko und unterstützt gleichzeitig wertvolle Anwendungsfälle.

### Darf ich meine API-Schlüssel wiederverwenden?

Nein. Sie müssen einen neuen API-Schlüssel für Ihren MCP-Client erstellen. Bitte beachten Sie, dass Sie Ihren KI-Tools nur Zugriff auf Daten gewähren sollten, mit denen Sie einverstanden sind, und vermeiden Sie erweiterte Berechtigungen.

### Wird der Braze MCP-Server lokal oder remote gehostet?

Der Braze MCP-Server wird lokal gehostet.

### Warum listet Cursor ausschließlich Funktionen auf?

Bitte überprüfen Sie, ob Sie sich im Abfrage-Modus oder im Agenten-Modus befinden. Um den MCP-Server nutzen zu können, müssen Sie sich im Agent-Modus befinden.

### Was soll ich tun, wenn der Agent eine Antwort zurückgibt, die mir unkorrekt erscheint?

Bei der Arbeit mit Tools wie Cursor empfiehlt es sich, das verwendete Modell zu ändern. Wenn Sie beispielsweise die automatische Einstellung verwenden, empfehlen wir, auf ein bestimmtes Modell umzustellen und zu ermitteln, welches Modell die beste Performance für Ihre Anwendungsfälle bietet. Sie können auch versuchen, einen neuen Chat zu starten und die Eingabeaufforderung erneut auszuführen. 

Sollten die Probleme persistent sein, bitten wir Sie, uns eine E-Mail an [mcp-product@](mailto:mcp-product@braze.com) zu senden[braze.com,](mailto:mcp-product@braze.com) um uns darüber zu informieren. Wenn möglich, fügen Sie bitte ein Video hinzu und erweitern Sie die Anruffunktionen, damit wir sehen können, welche Anrufe der Agent getätigt hat.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
