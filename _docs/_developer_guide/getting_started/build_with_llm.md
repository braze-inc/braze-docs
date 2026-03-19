---
nav_title: Build with an LLM
article_title: Building with an LLM
page_order: 4
description: "Learn how to use AI coding assistants with Braze documentation to accelerate your SDK integration workflow."
platform:
  - Web
  - React Native
---

# Building with an LLM

> Use AI coding assistants to accelerate your Braze integration workflow. Connect your IDE to the Braze Docs MCP server through Context7 and get accurate, up-to-date SDK guidance directly in your development environment.

AI coding assistants can help you write integration code, troubleshoot issues, and explore Braze SDK features&#8212;but only if they have the right context. The Braze Docs MCP server provides your AI assistant with direct access to Braze documentation, so it can generate accurate code snippets and answer technical questions based on the latest SDK references.

## Connecting to the Braze Docs MCP

[Context7](https://context7.com/braze-inc/braze-docs) serves as the bridge between your AI assistant and the Braze documentation library. By adding Context7 to your IDE's MCP configuration, your AI assistant can query the full Braze documentation set and retrieve relevant SDK references, code examples, and integration guides on demand.

### Setting up Context7

To connect your AI assistant to the Braze Docs MCP through Context7, add the following configuration to your IDE's `mcp.json` file.

{% tabs %}
{% tab Cursor %}
In [Cursor](https://cursor.com/), go to **Settings** > **Tools and Integrations** > **MCP Tools** > **Add Custom MCP**, then add the following snippet:

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

Save the configuration and restart Cursor. Your AI assistant can now access Braze documentation through Context7 when you include `use context7` in your prompts.
{% endtab %}

{% tab Claude %}
In Claude Desktop, go to **Settings** > **Developer** > **Edit Config**, then add the following to your `claude_desktop_config.json` file:

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

Save the configuration and restart Claude Desktop.
{% endtab %}

{% tab VS Code %}
Add the following to your VS Code `settings.json` or `.vscode/mcp.json` file:

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

Save the configuration and restart VS Code.
{% endtab %}
{% endtabs %}

{% alert note %}
Context7 is different from the [Braze MCP server]({{site.baseurl}}/developer_guide/mcp_server/). Context7 provides your AI assistant with access to **Braze documentation**, while the Braze MCP server provides read-only access to **your Braze workspace data** (such as campaigns, segments, and analytics). You can use both together for a more complete AI-assisted development experience.
{% endalert %}

## Writing prompts for Braze SDK development

After you set up Context7, include `use context7` in your prompts to signal your AI assistant to pull in Braze documentation as context. The following examples show how to write effective prompts for common SDK tasks.

### React Native SDK

These prompts demonstrate common integration tasks for the [Braze React Native SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/).

#### Initializing the SDK

```text
Using the Braze React Native SDK, show me how to initialize the SDK 
in my App.tsx with an API key and custom endpoint. Include the 
configuration for automatic session tracking. Use context7.
```

#### Logging custom events with properties

```text
I need to track user activity in my React Native app using the Braze 
React Native SDK. Show me how to log a custom event called 
"ProductViewed" with properties for product_id, category, and price. 
Use context7.
```

#### Setting up push notifications

```text
Using the Braze React Native SDK, walk me through requesting push 
notification permissions on both iOS and Android 13+. Include the 
code for registering the push token with Braze. Use context7.
```

#### Handling in-app messages

```text
Show me how to subscribe to in-app messages using the Braze React 
Native SDK, including how to log impressions and button clicks 
programmatically. Use context7.
```

### Web SDK

These prompts demonstrate common integration tasks for the [Braze Web SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/).

#### Initializing the SDK

```text
Using the Braze Web SDK, show me how to initialize the SDK with 
braze.initialize(), including the API key, base URL, and options 
for enabling logging and automatic in-app message display. 
Use context7.
```

#### Tracking custom events and purchases

```text
Using the Braze Web SDK, create a JavaScript module that logs a 
custom event called "VideoPlayed" with properties for video_id, 
duration_seconds, and completion_percentage. Also show how to log 
a purchase with product ID, price, currency code, and quantity. 
Use context7.
```

#### Registering for web push

```text
Using the Braze Web SDK, provide the HTML and JavaScript needed to 
register a user for web push notifications after they click a 
"Subscribe to updates" button. Include the service worker setup. 
Use context7.
```

#### Managing user attributes

```text
Using the Braze Web SDK, show me how to set standard user attributes 
(first name, email, country) and custom user attributes (favorite_genre, 
subscription_tier) for the current user. Use context7.
```

## Plain text documentation

You can access the Braze Developer Guide documentation as plain text files optimized for AI tools and LLMs. These files provide Braze documentation in a format that AI assistants can parse and understand without the overhead of HTML rendering.

| File | Description |
|------|-------------|
| [llms.txt](https://www.braze.com/docs/developer_guide/llms.txt) | An index of Braze developer documentation pages with titles and descriptions. Use this as a starting point for discovering available documentation. |
| [llms-full.txt](https://www.braze.com/docs/developer_guide/llms-full.txt) | The complete Braze developer documentation in a single plain text file, formatted for LLM consumption. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

These files follow the [llms.txt standard](https://llmstxt.org/), an emerging convention for making documentation accessible to AI tools. You can reference these files directly in your prompts or paste their contents into an LLM for context.
