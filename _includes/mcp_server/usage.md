# Using Braze MCP server

> Learn how to interact with your Braze data using natural-language tools like Claude and Cursor. For more general information, see [Braze MCP server]({{site.baseurl}}/developer_guide/mcp_server/).

{% multi_lang_include mcp_server/beta_alert.md %}

{% multi_lang_include mcp_server/prerequisites.md %}

## Best practices

When using Braze MCP server through natural-language tools like Claude and Cursor, keep these tips in mind to get the best results:

- LLMs can make mistakes, so always be sure to double-check their answers.
- For data analysis, be clear about the time range you need. Shorter ranges often give more accurate results.
- Use exact [Braze terminology](https://www.braze.com/resources/articles/glossary) so your LLM calls the right function.
- If results seem incomplete, prompt your LLM to continue or dig deeper.
- Try creative prompts! Depending on your MCP client, you may be able to export a CSV or other useful files.

## Usage examples

After [setting up Braze MCP server]({{site.baseurl}}/developer_guide/mcp_server/setup/), you can use natural-language tools like Claude and Cursor to interact with your Braze data. Here's some examples to get you started: 

### What are my available Braze functions?

{% tabs %}
{% tab Claude %}
!['What are my available Braze functions?' being asked and answered in Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %})
{% endtab %}

{% tab Cursor %}
!['What are my available Braze functions' being asked and answered in Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

### Get details about a canvas ID

{% tabs %}
{% tab Claude %}
!['Get details about a canvas ID' being asked and answered in Claude.]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %})
{% endtab %}

{% tab Cursor %}
!['Get details about a canvas ID' being asked and answered in Cursor.]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

### Show my recent canvases

{% tabs %}
{% tab Claude %}
!['Show my recent canvases' being asked and answered in Claude.]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %})
{% endtab %}

{% tab Cursor %}
!['Show my recent canvases' being asked and answered in Cursor.]({% image_buster /assets/img/mcp_server/cursor/show_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}
