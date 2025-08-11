---
nav_title: Braze MCP server
article_title: About Braze MCP server
description: "Connect AI tools like Claude and Cursor to Braze for read-only access to workspace data using the MCP protocol."
page_order: 2.8
alias: /mcp/
---

# Braze MCP server

> Learn about Braze MCP server, so you can connect Braze to AI tools like Claude and Cursor for read-only access to your workspace.

{% multi_lang_include mcp_server/beta_alert.md %}

## What is Model Context Protocol (MCP)?

​​Model Context Protocol, or MCP, is a standard that lets AI agents connect to and work with data from another platform. It has two main parts:

- **MCP client:** The application where the AI agent runs, such as Cursor or Claude.
- **MCP server:** A service provided by another platform, like Braze, that defines which tools the AI can use and what data it can access.

## About Braze MCP server

The Braze MCP server connects AI tools like agents, assistants, and chatbots directly to Braze, allowing them to read aggregated data such as Canvas and Campaign analytics, custom attributes, segments, and more. Braze MCP server is great for:

- Building AI-powered tools that need Braze context.
- CRM engineers creating multi-step agent workflows.
- Technical marketers experimenting with natural language queries.

Braze MCP server supports up to 38 read-only endpoints that do not return Personally Identifiable Information (PII) data. You can limit which endpoints you assign to your Braze API key to restrict what the agent can access.

{% alert warning %}
Do not assign permissions to your API key that are **not** read-only. Agents may try to write or delete data in Braze, which could cause unintended consequences.
{% endalert %}

## Usage examples

After you [set up your Braze MCP server]({{site.baseurl}}/developer_guide/mcp_server/setup/), your AI client can answer questions about your Braze workspace using natural language. Here are a few ways you might use it:

| Example | Prompt | What the MCP server Does |
|---------|--------|--------------------------|
| Viewing recent Canvases or Campaigns | Can you show me my recent canvases? | Calls `get_canvas_list` and returns canvas IDs, names, and last edited dates. |
| Cleaning up custom attributes | I’m working on a custom attribute clean-up project. Can you review my custom attributes and create a report for me with suggested next steps? | Pulls all custom attribute names from Braze, analyzes them, and provides a report with trends, suggestions, and best practices. |
| Reviewing performance data | How did my campaigns perform yesterday? | Identifies campaigns active yesterday, retrieves analytics for each, and summarizes key performance trends. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert tip %}
For more examples and use cases, see [Using Braze MCP server]({{site.baseurl}}/developer_guide/mcp_server/usage/).
{% endalert %}

## Frequently Asked Questions (FAQ) {#faq}

### Which MCP clients are supported?

Currently, only [Claude](https://claude.ai/) and [Cursor](https://cursor.com/) are supported. You'll need an account for one of these clients to use Braze MCP server.

### What Braze data can my MCP client access?

MCP clients can only access read-only endpoints that are not built to retrieve PII. They cannot manipulate data in Braze.

### Can my MCP client manipulate Braze data?

No. The MCP server only exposes tools that handle non-PII, read-only data.

### Can I use a third-party Braze MCP server?

Using a third-party Braze MCP servers is not recommend. Only use the official Braze MCP server hosted on [PyPi](https://pypi.org/project/braze-mcp-server/).

### Why doesn’t Braze MCP server offer PII or write access?

To protect data while still enabling innovation, the server is limited to non-PII, read-only tools. This reduces risk while supporting valuable use cases.

### Can I reuse my API keys?

No. You'll need to create a new API key for your MCP client. Remember to only give your AI tools access to what you’re comfortable with, and avoid elevated permissions.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
