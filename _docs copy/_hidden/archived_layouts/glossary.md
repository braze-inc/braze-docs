---
nav_title: Glossary
article_title: Glossary layout
page_order: 0
noindex: true
---

# Example layout: Glossary

> The glossary layout is in YAML. It requires several components and parameters. Glossary layouts are good for localized searchable content, like dictionaries and specific categories of content.

## Required Components

1. YAML Open and Closing notation. In other words, `---` before the content, and `---` after. 
2. Quotes around certain parameter content. (Header parameters, text parameters, content with hyphens or other special characters.)
3. Glossary Tags notation (These are filter tags)

## Required Parameters

|Parameter | Content Type | Details |
|---|---|---|
|`page_order`| numerical | Order the page within the section. This order will reflect in the left-hand navigation. |
| `nav-title`| Alphanumeric | Title that will appear in the left-hand navigation. |
|`layout`| Alphanumeric - No spaces | Select a layout from the [layout section](https://github.com/Appboy/braze-docs/tree/develop/_layouts) of the documentation. | 
|`glossary_top_header` | Alphanumeric | Requires double quotes. Title appears at the top of the page. |
|`glossary_top_text`| String, Alphanumeric | Describe your glossary page. This will appear above the search bar and filters (if you choose to have them.) This is essentially written in HTML, so you can use ```<br> to create linebreaks. | 
|`glossary_tag_name` | Single Word, Alphanumeric | Name your filters. These will appear in checkboxes below the search bar as well as in the data below. | 
|`glossary_filter_text`| String, Alphanumeric | Describe your filters. Usually used to instruct. | 
|`glossary_tags`| More YAML plus content. | Format as shown below: <br> glossary_tags: <br>  - name: Content Cards <br>  - name: Email | 
| `glossaries`| More YAML plus content. | See [Glossaries Parameters](#glossaries-parameters) below. |

### Glossaries Parameters

|Parameter | Content Type | Details |
|---|---|---|
|`name`| Alphanumeric | Name your glossary item.| 
|`description`| String, Alphanumeric | Describe your glossary item. | 
|`calculation`| String | (optional) Describe how your glossary item is calculated (usually used when describing data or metrics. | 
|`tags`| Alphanumeric | Should match what is listed as a `name` under `glossary_tags`. List as many as applicable. Writing `All` will include the item in all filters.|

## Example

```
---
page_order: 0
nav_title: Report Metrics Glossary
layout: glossary_page
glossary_top_header: "Report Metrics Glossary"
glossary_top_text: "These are terms you'll find in your reports in your Braze account. Search for the metrics you need, or filter by channel. <br>  <br> This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account."

glossary_tag_name: Channels
glossary_filter_text: "Select Channels below to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Content Cards
  - name: Email
  - name: In-App Message
  - name: News Feed
  - name: Web Push
  - name: iOS Push
  - name: Android Push
  - name: Webhook

glossaries:
  - name: Variation
    description: Variation of a campaign, differing as defined by the creator.
    calculation: Count
    tags:
      - All
  - name: Audience
    description: Percentage of users who received a particular message. This number is received from Braze.
    calculation: (Number of Recipients in Variant) / (Unique Recipients)
    tags:
      - All
  - name: Unique Recipients
    description: Exact number of users who received a particular message. This number is received from Braze.
    calculation: Count
    tags:
      - Email
      - Web Push
      - iOS Push
      - Android Push
      - In-App Message
      - News Feed
  - name: Total Impressions
    description: The number of users whose devices reported that the in-app message has been delivered (if a user receives a message twice, they will be counted twice). This number is a sum of number of impression events that Braze receives from the SDKs.
    calculation: Count
    tags:
      - In-App Message
      - News Feed
      - Content Cards
---
```
