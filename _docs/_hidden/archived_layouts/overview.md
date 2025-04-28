---
nav_title: Overview
page_order: 0
noindex: true
---

# Example layout: Overview

> The overview layout is good for creating a specific navigation option at the top of a page that allows users to click a button to travel to a specific part of a page or a completely other page.

Classic examples of the Selector Layout are [the SDK Changelogs](https://www.braze.com/docs/developer_guide/changelogs) page, or the [In-app Message Creative Details page](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/).

## Required Components

1. YAML Open and Closing notation. In other words, --- before the content, and --- after.
2. Quotes around certain parameter content. (Header parameters, text parameters, content with hyphens or other special characters.)
3. Glossary Tags notation (These are filter tags)

## Required Parameters

|Parameter | Content Type | Details |
|---|---|---|
|`page_order`| numerical | Order the page within the section. This order will reflect in the left-hand navigation. |
| `nav-title`| Alphanumeric | Title that will appear in the left-hand navigation. |
|`layout`| Alphanumeric - No spaces | Select a layout from the [layout section](https://github.com/Appboy/braze-docs/tree/develop/_layouts) of the documentation. | 
|`guide_top_header`|Alphanumeric | Title your page.|
|`guide_top_text`|Alphanumeric | Describe your page, this will go directly above the buttons and their title. Quotes required around content. |
|`guide_featured_title`| Alphanumeric | Title your cards. This will go directly above the buttons.
|`guide_featured_list`| More YAML, Alphanumeric | See [Guide Listing Format](#guide-listing-format) below. |

### Guide Listing Format

|Parameter | Content Type | Details |
|---|---|---|
|`name`| Alphanumeric | Name the box. |
| `link`| URL or Path | Link to where the box will go. Must contain full URL or (if an internal link) `/docs...`  |
|`image`| Path | Link to location of image. |

Format example:

```yaml
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
```

## Example

```yaml
---
nav_title: Creative Details
page_order: 4
layout: featured
guide_top_header: "Creative Details"
guide_top_text: "Get creative with our in-app messages! But you should know some of the guidelines, first! After all, you have to know those rules to break them! Check out the individual message type's Creative Specs or the global Creative Details below."

guide_featured_title: "Message Type Creative Specs"
guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Slideup
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#slideup
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: Full-Screen
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#full-screen
  image: /assets/img/braze_icons/expand-05.svg
---

# Creative Details {#general}

Braze in-app messages have both global and individual creative specifications. For more information on our more customizable in-app message types, go to our [Customize]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/) page.

{% alert important %}
  These details only apply to our most recent in-app message generation (Generation 3). If you are not using our newest generation of in-app messages, check out our [previous in-app message generations]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/) documentation.
{% endalert %}
```
