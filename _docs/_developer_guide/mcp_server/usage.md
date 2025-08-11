---
nav_title: Using Braze MCP server
article_title: Using Braze MCP server
description: "Learn how to interact with your Braze data using natural-language tools like Claude and Cursor."
page_order: 1.2
---

# Using Braze MCP server

> Learn how to interact with your Braze data using natural-language tools like Claude and Cursor. For more general information, see [Braze MCP server]({{site.baseurl}}/developer_guide/mcp_server/).

{% multi_lang_include mcp_server/beta_alert.md %}

{% multi_lang_include mcp_server/prerequisites.md %}

## Best practices

- LLMs aren’t perfect and can get things wrong. Be sure to always double check responses.
- If you’re looking to analyze data, be specific about the window of time you want. Smaller time ranges generally yield more accurate responses.
- Be specific with Braze terminology, that ensures that your LLM uses the correct function.
- If you’re noticing that you’re not seeing all the data you’re looking for, you may have to prompt the LLM to continue to explore further.
- Depending on your MCP client, you could even ask your LLM to create you a CSV file or other artifacts. Experiment with this!

## Usage examples

Once installed and configured in Cursor / Claude, you can interact with your Braze data using natural language:

**"Show me my recent canvases"**

```
The agent will use the MCP server to call get_canvas_list and display your canvases with their IDs, names, and last edited dates.
```

**"Get details about canvas ID 401cc9b3-d9bf-4c73-ac9f-e9dca46d2a36"**

```
The agent will retrieve detailed canvas information including steps, variants, schedule type, and current status.
```

**"What are my available Braze API functions?"**

```
The agent will list all 38 available functions across campaigns, canvases, catalogs, events, KPIs, segments, purchases, sessions, SDK authentication, messages, CDI integrations, templates, and more.
```

{% multi_lang_include mcp_server/legal_disclaimer.md %}
