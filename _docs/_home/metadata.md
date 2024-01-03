---
nav_title: Metadata 
page_order: 5
noindex: true
---

# Metadata

> These are the supported metadata keys you can add to your page's YAML front matter.

The top of every markdown page should begin with a section of YAML to define the page.

```html
---
nav_title: "Docs Metadata"
page_order: 0

description: "This page walks through the options for adding metadata to Docs pages. We optimize our search based on page type and other bits of metadata. This is a great resource for contributors via our GitHub page."
page_type: reference
tool: 
  - docs
  - dashboard
---
```

Sometimes, you may find that a content tag for a page could be categorized with multiple values (as in, an article might talk about both Canvas and campaigns, or cover a custom integration for both Android and iOS).

You can format that like this:

```yaml
key:
  - string1
  - string2      
  - string3
```

## Metadata keys 

| YAML Content Tag | Description  | Required? | Accepts Multiple Values? | Data Type | Available Values |
| ----------------- | ----------- | --------- | ------------------------ | --------- | ---------------- |
| `nav_title` | This is the title of the article that will appear in the left navigation of the Docs site. Encapsulate in quotes. | Yes, unless page is `hidden`. | No. | String. | Any - the title of a page is up to you. We recommend less than 30 characters with spaces. |
| `page_order` | This is the order in which the article will appear in the left navigation of the Docs site. | Yes, unless page is hidden. | No. | Integer. | Any number (including multiple decimals) between `1` and `100`. You can use `1.1`, `1.2`, `1.3`, etc. to order pages, as well.|
| `hidden` | Notes whether or not the page will be visible in the left navigation bar. Setting this to `false` will cause the page not to appear in searches (both on-site or through online search providers). | No. | No. | Boolean. | You may choose between `true` and `false`. |
| `config_only` | Whether or not a page will act as a page or as a category in the left navigation panel. Defaults to `false`. | No. |  No. | Boolean. | You may choose between `true` and `false`. |
| `permalink` | Sets the page's url. For example: `permalink: /this_page_name/` will set the page's URL to `https://www.braze.com/docs/this_page_name/`. | No, unless page is `hidden`. | No. | String. | Any - this URL is up to you. Encapsulate in slashes (`/`). |
| `layout` | Sets specific features on the page that align with developed layouts. Defaults is a regular page. | No. | No. | String. | If you do not set this, it will default to a regular content page. You may choose between: `api_page`, `dev_guide`, `featured_video`, `featured`, `glossary_page`, `blank_config`, and `redirect`. There are others, but those are mostly for internal and config uses. |
| `hide_toc` | Determines whether the Table of Contents on the right side of the page is included or not. | No. | No. | Boolean. | You may choose between `true` and `false`. |
| `noindex` | Determines whether the article will show in Algolia and Google Searches. Defaults to `false` unless you have the `hidden` YAML tag set as `true`. | No. | No. | Boolean. | `true` or `false`. |
| `description` | Description of the page that will show in online searches. Encapsulate in quotes. | Yes. | No. | String. | Any - the page description of a page is up to you. We recommend less than 3 sentences. <br> <br> Template: `This {page_type} {lists, describes, walks you through} {topic or task} for {platform and/or channel} using {tool}.` Though the exact phrasing can vary, it must include at least the page type, what the page aims to do (as in, it will "walk you through how to perform noted task" or "teach you how to read a certain report" or "describe the requirements of a certain Partner integration". <br> <br> Example: `This glossary lists all of the terms you need to know while onboarding with Braze and preparing for the Integration Phase.` Or `This reference article describes the different kinds of Canvas Steps and how they affect iOS or Android push campaigns.` Or even `This solutions article will walk you through a custom integration.` |
| `page_type` | Type of page, determined by page templates. Inform formatting and content. | Yes. | No. | String. | See [Page Types](#page-types). |
| `platform` | Notes which platforms (iOS, Android, etc.) the article is associated with. | No, unless on a Dev Guide page.  | Multiple values can be used. | String. | Any of the platforms Braze integrates on: `iOS`, `Android`, `Web`, `API`, and any of the wrapper SDKs. |
| `channel` | Notes which messaging channels (push, in-app messages, etc.) the article is associated with. | No, unless the content mentions a specific channel or channels. | Multiple values can be used. | String. | Any of the messaging channels Braze sends to: `content cards`, `email`, `news feed`, `in-app messages`, `push`, `sms`, and `webhooks`.|
| `tool` | Notes which engagement tools (Canvas, campaigns, etc.) the article is associated with. | Yes. | Multiple values can be used. | String. | Any of the following Braze  tools: `dashboard`, `docs`, `canvas`, `campaigns`, `segments`, `templates`, `media`, `location`, `currents`, `reports`. |

