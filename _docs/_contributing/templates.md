---
nav_title: Templates
article: Templates
page_order: 8
---

# Templates

> You can use these templates to create a [page]({{site.baseurl}}/contributing/content_management/pages/) or [section]({{site.baseurl}}/contributing/content_management/sections/). Follow the HTML comments (noted as `<!-- COMMENT -->`) above each section in your template to learn more about that section.

{% alert important %}
HTML comments aren't rendered when [you]({{site.baseurl}}/contributing/generating_a_preview/) or [Vercel]({{site.baseurl}}/contributing/your_first_contribution/?tab=github#step-4-review-your-work) generate a site preview, so you can leave them in while writing. However, be sure to remove all HTML comments before publishing.
{% endalert %}

## Available templates

### Basic

The basic template is used for...

{% details See template %}
{% raw %}
`````markdown
---
nav_title: NAV_TITLE
article_title: ARTICLE_TITLE
description: "SHORT_DESCRIPTION."
---

<!-- The title of your page, used to render the in-page title. -->

# ARTICLE_TITLE

<!-- A description of your page containing an overview of what will be covered. Note that the description starts with the '>' character. -->

> DESCRIPTION.

<!-- An optional section used to contextualize the topic at a high-level. -->

OPTIONAL_CONTEXT.

## Prerequisites

<!-- The prerequisites for this task. If no prerequisites are required, you can remove this section. -->

Before you start, you'll need to complete the following:

- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE

<!-- An example section. You may add subsections, images, and links as needed. -->

## SECTION_TITLE

CONTENT.

<!-- An example section with subsections. You may add addtional subsections, images, and links as needed. -->

## SECTION_TITLE

### Step 1: ACTION_TO_COMPLETE

CONTENT.

### Step 2: ACTION_TO_COMPLETE

CONTENT.
`````
{% endraw %}
{% enddetails %}

### Technology partner

The technology partner template is used for...

{% details See template %}
{% raw %}
`````markdown
---
nav_title: NAV_TITLE
article_title: ARTICLE_TITLE
description: "SHORT_DESCRIPTION."
alias: /partners/your_partner_name/
page_type: partner
search_tag: Partner
layout: dev_guide
---

<!-- In most cases, the ARTICLE_TITLE will be your company name. If your tool requires several seperate pages on Braze Docs, you can add a relevant page descriptor to your title, such as "MyCompany Analytics." -->

# ARTICLE_TITLE

<!-- A description of your page containing an introduction to your company, a link to your main site, and a consice overview of this integration. Note that the description starts with the '>' character. -->

> DESCRIPTION.

<!-- A section covering the relationship between your company and Braze. Explain how Braze and your company partner together to tighten the bond between the Braze user and their customer. -->

CONTENT.

## Prerequisites

<!-- Most partner integrations require the following prerequisites. You can add additional prerequisites as needed. -->

Before you start, you'll need the following:

| Prerequisite          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| A [Partner] account   | A [Partner] account is required to take advantage of this partnership.                                                                     |
| A Braze REST API key  | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance.                                                 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can create an API key at **Developer Console** > **API Settings**.
{% endalert %}

## Use cases

<!-- An optional section used to outline the typical or atypical use cases for this integration. -->

CONTENT.

## Integrating TOOL_NAME

<! -- Create step-by-step instructions for integrating your tool with Braze. It's important to be concise and only outline the minimum neccesary steps. If you need to outline different integrations steps (such a side-by-side, server-to-server, or basic integration), consider creating multiple subsections. -->

CONTENT.

### Step 1: ACTION_TO_COMPLETE

CONTENT.

### Step 2: ACTION_TO_COMPLETE

CONTENT.

### Step 3: ACTION_TO_COMPLETE

CONTENT.

{% details Webhook formatting %}
```
### Step 2: Create a [Partner] webhook in Braze
To create a [Partner] webhook template to use in future campaigns or Canvases, navigate to the **Templates & Media** section in the Braze platform. If you would like to create a one-off [Partner] webhook campaign or use an existing template, select **Webhook** in Braze when creating a new campaign.
Once you have selected the [Partner] webhook template, you should see the following:
- **Webhook URL**: [Partner Webhook URL]
- **Request Body**: Raw Text
#### Request headers and method
[Partner] requires an `HTTP Header` for authorization. The following will already be included within the template as key-value pairs.
- **HTTP Method**: POST
- **Request Header**:
    - **Authorization**: Bearer [PARTNER_AUTHORIZATION_HEADER]
    - **Content-Type**: application/json
#### Request body
Include code of your webhook request body.
### Step 3: Preview your request
Preview your request in the **Preview** panel or navigate to the `Test` tab, where you can select a random user, an existing user or customize your own to test your webhook.
{% alert important %}
Remember to save your template before leaving the page! <br>Updated webhook templates can be found in the **Saved Webhook Templates** list when creating a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}
```
{% enddetails %}

## Customizing [tool name]

Customization is an **optional** section. Here, you could outline specific ways to customize your integration between the two partners.

## Using [tool name] with Braze

This section should describe how to use the integration in Braze. Let users know how to access the data (if any) provided to Braze through the integration and how to leverage it in Braze messaging.

### Step 1: ACTION_TO_COMPLETE

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

### Step 2: ACTION_TO_COMPLETE

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
`````
{% endraw %}
{% enddetails %}

### Release notes

The release notes template is used for...

{% details See template %}
{% raw %}
`````markdown
---
nav_title: Release Notes
page_order: 2
page_type: reference
description: "This article contains a template for release notes."
permalink: /contributing/templates/release_notes/

noindex: true
---

# [Month Day, Year] release

## [Section 1]

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

## [Section 2]

### Ipsum

{% multi_lang_include release_type.md release="Early access" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

### Dolor

{% multi_lang_include release_type.md release="General availability" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

### Sit amet

{% multi_lang_include release_type.md release="Beta" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

### Consectetur

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

## [Section 3]

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.

## [Section 4]

### Adipiscing

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

## [Section 5]

### Elit

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

#### Sed do eiusmod tempor

{% multi_lang_include release_type.md release="General availability" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

## [Section 6]

### Laboris

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

## New Braze partnerships

### Incididunt - Canvas Audience Sync

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

### Ut labore - Dynamic content

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

## SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [Example](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - More details on this example
- [Other example](https://github.com/braze-inc/braze-react-native-sdk/blob/8.3.0/CHANGELOG.md)
- [Other example](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
`````
{% endraw %}
{% enddetails %}
