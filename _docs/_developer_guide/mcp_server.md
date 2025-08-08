---
nav_title: Braze MCP server
article_title: About Braze MCP server
description: "Connect AI tools like Claude and Cursor to Braze for read-only access to workspace data using the MCP protocol."
page_order: 2.8
alias: /mcp_server/
---

# Braze MCP server

> Learn about Braze MCP server, so you can connect Braze to AI tools like Claude and Cursor for read-only access to your workspace.

{% multi_lang_include mcp_server/beta_alert.md %}

## What is an MCP server?

​​MCP (Model Context Protocol) is a protocol that assists AI clients (like Cursor, VS Code, or Claude) in interacting with products like Braze.

An MCP server defines what tools an AI client has access to.  Clients (like an agent in Cursor or Claude Desktop) can then understand context about Braze, what it can do (like get data about campaign performance), and how to do it (use the /campaigns/details endpoint).

## About the Braze MCP server

The Braze MCP server connects AI tools directly to Braze. This gives AI agents, assistants, and chatbots the ability to read aggregated Braze data like Canvas analytics, Campaign analytics, custom attributes, segments, and more. All through natural language interactions.

Braze’s MCP server interfaces with 38 endpoints that are all read-only and are designed not to return Personally Identifiable Information (PII).  Your agents will have access to these tools.  Keep in mind that you can scope access down further by adjusting API key scopes. Note that if you use an API Key with broader scopes than read-only, your agents may be able to perform other actions in Braze - including writing or deleting data. This may result in unintended outcomes.

- Use this if you are building agentic tools at your company and want to give those tools context into Braze.
- Use this if you’re an engineer on a CRM team and want to build out multi-step agentic workflows.
- Use this if you’re a more technical marketer and want to experiment with natural language queries to Braze context in your day to day workflow.

## Use cases

By setting up your MCP client with Braze’s MCP server, your LLM can answer questions about your Braze workspace.  Below are a few examples:

| Use Case | Example Prompt | What the MCP server Does |
|----------|----------------|--------------------------|
| Getting details on your recent Canvases/Campaigns | Can you show me my recent canvases? | Calls `get_canvas_list` and displays canvases with IDs, names, and last edited dates. |
| Assistance in custom attribute clean-up projects | I’m working on a custom attribute clean up project. Can you review my custom attributes and create a report for me with suggested next steps? | Retrieves all custom attribute names from Braze, analyzes them, and generates a report of common trends with suggestions and best practices. |
| Analyzing performance data | How did my campaigns perform yesterday? | Determines which campaigns were active yesterday, retrieves analytics for each, and compiles a performance report highlighting trends. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Frequently Asked Questions (FAQ) {#faq}

### What data can MCP clients access through Braze’s MCP server?

MCP clients can only access read-only endpoints that are not built to retrieve PII. They cannot manipulate data in Braze.

### Can LLMs manipulate Braze data?

No. The MCP server only exposes tools that handle non-PII, read-only data.

### Can I use another MCP server from GitHub?

This isn't recommend. Only the Braze MCP server is officially supported.

### Why doesn’t Braze’s MCP server offer PII or write access?

To protect data while still enabling innovation, the server is limited to non-PII, read-only tools. This reduces risk while supporting valuable use cases.

### Can I reuse my API keys?

No. You'll need to create a new API key for your MCP client. Remember to only give your AI tools access to what you’re comfortable with, and avoid elevated permissions.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
