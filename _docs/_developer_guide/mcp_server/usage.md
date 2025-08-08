---
nav_title: Using Braze MCP server
article_title: Using Braze MCP server
description: "Learn how to interact with Braze data through the MCP server using natural language in tools like Claude and Cursor, plus recommended best practices."
page_order: 1.2
---

# Using Braze MCP server

> Learn how to interact with your Braze data through our MCP server using natural language in tools like Claude and Cursor.

## Prerequisites

Before you can use this feature, you'll need to [set up the Braze MCP server]({{site.baseurl}}/developer_guide/mcp_server/setup).

## Using Braze MCP server with agents

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

## Best practices

- LLMs aren’t perfect and can get things wrong.  Be sure to always double check responses.
- If you’re looking to analyze data, be specific about the window of time you want.  Smaller time ranges generally yield more accurate responses.
- Be specific with Braze terminology, that ensures that your LLM uses the correct function.  
  - Examples:  Specify active or draft.  Specify if you’re looking for canvases or campaigns.
- If you’re noticing that you’re not seeing all the data you’re looking for, you may have to prompt the LLM to continue to explore further.
- Depending on your MCP client, you could even ask your LLM to create you a CSV file or other artifacts.  Experiment with this!
