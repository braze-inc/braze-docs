---
nav_title: Searching Your Braze Dashboard
article_title: Searching Your Braze Dashboard
page_order: 0.5
page_type: reference
description: "Learn about global search in Braze."
---

# Searching your Braze dashboard

You can use the search bar to find your work and other information within your Braze dashboard. The search bar is at the top of your Braze dashboard. Click the search bar, or press <kbd>Ctrl</kbd>&nbsp;+&nbsp;<kbd>K</kbd> on Windows or <kbd>⌘</kbd>&nbsp;+&nbsp;<kbd>K</kbd> on a Mac to jump directly to the search bar.

![][3]

## What can you search for?

You can search for the following items and actions:

- Campaign names
- Canvas names
- Content Blocks
- Segment names
- Email template names
- [Pages within Braze](#find-pages-that-have-been-renamed)

{% alert tip %}
To search for exact text, put your search term in quotations (""). For example, searching for [“all users”] will return all items that contain the exact phrase “all users” in their name.
{% endalert %}

## Key features

### Keyboard shortcuts

Navigate through search results effortlessly with keyboard shortcuts:

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2), {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| Action                      | Keyboard shortcut                                                             |
| --------------------------- | ----------------------------------------------------------------------------- |
| Open the search menu        | {::nomarkdown} <ul> <li> Mac: <kbd>⌘</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> <li>Windows: <kbd>Ctrl</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> </ul> {:/}  |
| Move between search results | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| Select a search result      | <kbd>Enter</kbd>    |
| Close the search menu       | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Content type and status tags

Each search result is paired with tags that indicate the result's content type (page, campaign, Canvas, segment, email template) and status (active, archived, stopped, etc.).

### Access recently opened content

You can revisit recently accessed content from the search menu. The search interface displays your recently opened results below the search bar, including items interacted with throughout the entire Braze platform. This lets you return to previously viewed pages, campaigns, Canvases, segments, or email templates so you can pick up right where you left off with fewer clicks.

![][1]

### Find pages that have been renamed

The search understands synonyms for pages that have been renamed in our [updated navigation]({{site.baseurl}}/navigation). For example, it will find "Data Export" when you search for "Currents", as that page has been renamed.

<!---

### Quick create campaigns

Search for channels to see quick create options among your top 10 results. For example, searching for "email" shows "Create Email Campaign" or "Create Transactional Email Campaign".

![][2]

--->

### Filter for active and draft content

You can include active and draft content in your search results by selecting **Show active and draft only**. By default, the toggle is on, and all content, including archived, is shown.

![The "Show active and draft only" toggle.][4]

### Search for emojis

Do you use emojis when naming your work in Braze? Search for them! You can use emojis as search queries. 😎


[1]: {% image_buster /assets/img/global_search/global_search.png %}
[2]: {% image_buster /assets/img/global_search/search_create_campaign.png %}
[3]: {% image_buster /assets/img/global_search/global_search2.png %}
[4]: {% image_buster /assets/img/global_search/show_active_draft.png %}
