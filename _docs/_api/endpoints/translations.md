---
nav_title: Translations
article_title: Translation Endpoints
search_tag: Endpoint
page_order: 9
layout: dev_guide

description: "This landing page lists the Braze translation endpoints."
page_type: landing

guide_top_header: "Translation Endpoints"
guide_top_text: "Use the Braze translation endpoints to manage and update translations in your campaigns and Canvases."

guide_featured_title: "Campaign endpoints"
guide_featured_list:
  - name: "GET: View Translation for a Campaign"
    link: /docs/api/endpoints/translations/campaigns/get_translation_campaign/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Update Translation in a Campaign"
    link: /docs/api/endpoints/translations/campaigns/put_update_translation_campaign/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: View Campaign Default Source Translations"
    link: /docs/api/endpoints/translations/campaigns/get_source_campaign/
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title: "Canvas endpoints"
guide_menu_list:
  - name: "GET: View Translation for a Canvas"
    link: /docs/api/endpoints/translations/canvas/get_translation_canvas/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Update Translation in a Canvas"
    link: /docs/api/endpoints/translations/canvas/put_update_translation_canvas/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: View Canvas Default Source Translations"
    link: /docs/api/endpoints/translations/canvas/get_source_canvas/
    image: /assets/img/braze_icons/message-plus-square.svg

guide_menu_title2: "Email template endpoints"
guide_menu_list2:
  - name: "GET: View Email Template Default Source Translations"
    link: /docs/api/endpoints/translations/email_templates/get_view_source_template/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: View Specific Translation and Locale"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_locale_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: View All Translations and Locales"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT: Update Translations in an Email Template"
    link: /docs/api/endpoints/translations/email_templates/put_update_template/
    image: /assets/img/braze_icons/target-04.svg

---

{% alert important %}
The Braze translation endpoints are currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## How our translation endpoints work

Our translation endpoints work with [multi-language composition]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/), where a message can have different versions that can be rendered depending on the user receiving the message.

### Prerequisites

Before using these endpoints, you must [add your locales]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).

### How to test your translations

There are two ways you can validate translation support using the API and the Braze dashboard across campaigns, Canvases (including individual steps), and email templates:

- During composition (before launch)
- After launch (using post-launch drafts)

Before testing updating translations, you must:

1. [Add your locales]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).
2. Create a message and use translation tags where appropriate.
3. Save the message.
4. Select the locales to be included.
