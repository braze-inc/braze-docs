# The Braze MCP server

> Learn about the Braze MCP server, a secure, read-only connection that lets AI tools like Claude and Cursor access non-PII Braze data to answer questions, analyze trends, and provide insights without altering data.

{% multi_lang_include mcp_server/beta_alert.md %}

## What is Model Context Protocol (MCP)?

​​Model Context Protocol, or MCP, is a standard that lets AI agents connect to and work with data from another platform. It has two main parts:

- **MCP client:** The application where the AI agent runs, such as Cursor or Claude.
- **MCP server:** A service provided by another platform, like Braze, that defines which tools the AI can use and what data it can access.

## About the Braze MCP server

After [setting up the Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, you can connect AI tools like agents, assistants, and chatbots directly to Braze, allowing them to read aggregated data such as Canvas and Campaign analytics, custom attributes, segments, and more. The Braze MCP server is great for:

- Building AI-powered tools that need Braze context.
- CRM engineers creating multi-step agent workflows.
- Technical marketers experimenting with natural language queries.

The Braze MCP server supports 38 read-only endpoints that do not return data from Braze user profiles. You can choose to assign only some of these endpoints to your Braze API key to further restrict which data an agent can access.

{% alert warning %}
Do not assign permissions to your API key that are **not** read-only. Agents may try to write or delete data in Braze, which could cause unintended consequences.
{% endalert %}

## Usage example

You can interact with Braze through natural language using tools like Claude or Cursor. For other examples and best practices, see [Using the Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
!['What are my available Braze functions?' being asked and answered in Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['What are my available Braze functions' being asked and answered in Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Frequently Asked Questions (FAQ) {#faq}

### Which MCP clients are supported?

Only [Claude](https://claude.ai/) and [Cursor](https://cursor.com/) are officially supported. You must have an account for one of these clients to use the Braze MCP server.

### What Braze data can my MCP client access?

MCP clients can only access read-only endpoints that are not built to retrieve PII. They cannot manipulate data in Braze.

### Can my MCP client manipulate Braze data?

No. The MCP server only exposes tools that handle non-PII, read-only data.

### Can I use a third-party MCP server for Braze?

Using a third-party MCP server for Braze data is not recommended. Only use the official Braze MCP server hosted on [PyPi](https://pypi.org/project/braze-mcp-server/).

### Why doesn’t the Braze MCP server offer PII or write access?

To protect data while still enabling innovation, the server is limited to endpoints that are read-only and do not typically return PII. This reduces risk while supporting valuable use cases.

### Can I reuse my API keys?

No. You'll need to create a new API key for your MCP client. Remember to only give your AI tools access to what you’re comfortable with, and avoid elevated permissions.

### Is the Braze MCP server hosted locally or remotely?

The Braze MCP server is hosted locally.

### Why is Cursor only listing functions?

Check if you're in ask mode or agent mode. To use the MCP server, you need to be in agent mode.

### What do I do when the agent returns an answer that looks incorrect?

When working with tools like Cursor, you may want to try changing the model used. For example, if you have it set to auto, try changing it to a specific model and experiment to find which model performs best for your use case. You can also try starting a new chat and retrying the prompt. 

If issues persist, you can email us at [mcp-product@braze.com](mailto:mcp-product@braze.com) to let us know. If possible, include a video and expand the call functions so we can see what calls the agent attempted.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
