---
nav_title: Mit einem LLM entwickeln
article_title: Bauen mit einem LLM
page_order: 4
description: "Erfahren Sie, wie Sie KI-Codierungsassistenten mit Braze-Dokumentation einsetzen können, um Ihren SDK-Integrations-Workflow zu beschleunigen."
platform:
  - Web
  - React Native
---

# Bauen mit einem LLM

> Nutzen Sie KI-Codierungsassistenten, um Ihren Braze-Integrations-Workflow zu beschleunigen. Verbinden Sie Ihre IDE über Context7 mit dem Braze Docs MCP-Server und erhalten Sie präzise, aktuelle SDK-Anleitungen direkt in Ihrer Entwicklungsumgebung.

KI-Codierungsassistenten können Ihnen beim Schreiben von Integrationscode, bei der Fehlerbehebung und beim Erkunden der Features des Braze SDK behilflich sein – jedoch nur, wenn sie über den richtigen Kontext verfügen. Der Braze Docs MCP-Server ermöglicht Ihrem KI-Assistenten direkten Zugriff auf die Braze-Dokumentation, sodass er präzise Snippets generieren und technische Fragen auf Grundlage der neuesten SDK-Referenzen beantworten kann.

## Verbindung mit dem Braze Docs MCP herstellen

[Context7](https://context7.com/braze-inc/braze-docs) fungiert als Schnittstelle zwischen Ihrem KI-Assistenten und der Braze-Dokumentationsbibliothek. Durch Hinzufügen von Context7 zur MCP-Konfiguration Ihrer IDE kann Ihr KI-Assistent die gesamte Braze-Dokumentation abfragen und bei Bedarf relevante SDK-Referenzen, Code-Beispiele und Integrationsanleitungen abrufen.

### Einrichtung von Context7

Um Ihren KI-Assistenten über Context7 mit dem Braze Docs MCP zu verbinden, fügen Sie bitte die folgende Konfiguration zur Datei Ihrer`mcp.json` IDE hinzu.

{% tabs %}
{% tab Cursor %}
Bitte gehen Sie in [Cursor](https://cursor.com/) zu **„Einstellungen“** > **„Tools und Integrationen“** > **„MCP-Tools“** > **„Benutzerdefiniertes MCP hinzufügen**“ und fügen Sie anschließend das folgende Snippet hinzu:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

Bitte speichern Sie die Konfiguration und starten Sie Cursor neu. Ihr KI-Assistent kann nun über Context7 auf die Braze-Dokumentation zugreifen, wenn Sie dies in Ihre `use context7`Eingabeaufforderungen einfügen.
{% endtab %}

{% tab Claude %}
Öffnen Sie in Claude Desktop **„Einstellungen“** > **„Entwickler:in“** > **„Konfiguration bearbeiten**“ und fügen Sie Folgendes zu Ihrer`claude_desktop_config.json`Datei hinzu:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

Bitte speichern Sie die Konfiguration und starten Sie Claude Desktop neu.
{% endtab %}

{% tab VS Code %}
Fügen Sie Folgendes zu Ihrer VS `settings.json``.vscode/mcp.json`Code-Datei hinzu:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

Bitte speichern Sie die Konfiguration und starten Sie VS Code neu.
{% endtab %}
{% endtabs %}

{% alert note %}
Context7 unterscheidet sich vom [Braze MCP-Server]({{site.baseurl}}/developer_guide/mcp_server/). Context7 gewährt Ihrem KI-Assistenten Zugriff auf **die Braze-Dokumentation**, während der Braze MCP-Server Lesezugriff auf **Ihre Braze-Workspace-Daten** (wie Kampagnen, Segmente und Analytics) ermöglicht. Sie können beide zusammen verwenden, um eine umfassendere KI-gestützte Entwicklungserfahrung zu erzielen.
{% endalert %}

## Schreibanregungen für die Entwicklung des Braze SDK

Nachdem Sie Context7 eingerichtet haben, fügen Sie bitte`use context7` in Ihre Eingabeaufforderungen ein, um Ihrem KI-Assistenten mitzuteilen, dass er die Braze-Dokumentation als Kontext heranziehen soll. Die folgenden Beispiele veranschaulichen, wie Sie effektive Eingabeaufforderungen für gängige SDK-Aufgaben erstellen können.

### React Native SDK

Diese Anweisungen veranschaulichen gängige Aufgaben der Integration für das [Braze React Native SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/).

#### Initialisierung des SDK

```text
Using the Braze React Native SDK, show me how to initialize the SDK 
in my App.tsx with an API key and custom endpoint. Include the 
configuration for automatic session tracking. Use context7.
```

#### Protokollierung angepasster Events mit Eigenschaften

```text
I need to track user activity in my React Native app using the Braze 
React Native SDK. Show me how to log a custom event called 
"ProductViewed" with properties for product_id, category, and price. 
Use context7.
```

#### Push-Benachrichtigungen einrichten

```text
Using the Braze React Native SDK, walk me through requesting push 
notification permissions on both iOS and Android 13+. Include the 
code for registering the push token with Braze. Use context7.
```

#### Umgang mit In-App-Nachrichten

```text
Show me how to subscribe to in-app messages using the Braze React 
Native SDK, including how to log impressions and button clicks 
programmatically. Use context7.
```

### Web SDK

Diese Anweisungen veranschaulichen gängige Aufgaben der Integration für das [Braze-Internet-SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/).

#### Initialisierung des SDK

```text
Using the Braze Web SDK, show me how to initialize the SDK with 
braze.initialize(), including the API key, base URL, and options 
for enabling logging and automatic in-app message display. 
Use context7.
```

#### Tracking von angepassten Events und Käufen

```text
Using the Braze Web SDK, create a JavaScript module that logs a 
custom event called "VideoPlayed" with properties for video_id, 
duration_seconds, and completion_percentage. Also show how to log 
a purchase with product ID, price, currency code, and quantity. 
Use context7.
```

#### Registrierung für Web-Push-Benachrichtigungen

```text
Using the Braze Web SDK, provide the HTML and JavaScript needed to 
register a user for web push notifications after they click a 
"Subscribe to updates" button. Include the service worker setup. 
Use context7.
```

#### Verwaltung von Benutzerattributen

```text
Using the Braze Web SDK, show me how to set standard user attributes 
(first name, email, country) and custom user attributes (favorite_genre, 
subscription_tier) for the current user. Use context7.
```

## Einfache Text-Dokumentation

Sie können auf die Dokumentation des Braze Developer Guide als reine Textdateien zugreifen, die für KI-Tools und LLMs optimiert sind. Diese Dateien enthalten die Braze-Dokumentation in einem Format, das KI-Assistenten ohne den Aufwand der HTML-Rendering-Verarbeitung analysieren und verstehen können.

| Datei | Beschreibung |
|------|-------------|
| [llms.txt](https://www.braze.com/docs/developer_guide/llms.txt) | Ein Verzeichnis der Braze-Dokumentationsseiten für Entwickler:innen mit Titeln und Beschreibungen. Bitte nutzen Sie dies als Ausgangspunkt, um die verfügbare Dokumentation zu entdecken. |
| [llms-full.txt](https://www.braze.com/docs/developer_guide/llms-full.txt) | Die vollständige Braze-Dokumentation für Entwickler:innen in einer einzigen Textdatei, formatiert für die Verwendung mit LLM. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Diese Dateien entsprechen dem[llms.txt](https://llmstxt.org/)[Standard](https://llmstxt.org/), einer sich entwickelnden Konvention, um Dokumentationen für KI-Tools zugänglich zu machen. Sie können diese Dateien direkt in Ihren Eingabeaufforderungen referenzieren oder ihren Inhalt zur Kontextualisierung in ein LLM einfügen.
