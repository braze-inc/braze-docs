---
nav_title: Personalizing landing pages
article_title: Personalizing landing pages
description: "This article covers how to personalize Braze landing pages with the drag-and-drop editor."
page_order: 4
---

# Personalizing landing pages

> Use Liquid personalization in landing pages to dynamically tailor the content with user profile data. For example, you can personalize headlines based on different user attributes without managing multiple static landing pages.

{% alert important %}
Liquid personalization for landing pages is only available on the Pro tier of landing pages. Currently, [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content), [multi-language]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings), and [promotion codes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes) are not supported with Liquid personalization in landing pages.
{% endalert %}

## Inserting Liquid

In the drag-and-drop editor, you can insert Liquid personalization both in the editor and in the page or block settings in the right-hand panel. For instructions on implementing Liquid, check out our dedicated [Liquid documentation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid-1).

![Landing page editor with Liquid personalization added.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## Previewing and testing

When previewing a landing page in the editor, you can view the page as a random user, an existing user, or a custom user.

However, when previewing the landing page from the data table or the **Landing Page details** page, you'll only be able to view it as a random user.

## Personalization considerations

To maintain optimal performance with personalized landing pages, note the following size limits:

- **Saving a landing page:** If the size exceeds 500&nbsp;KB, you may receive a warning message indicating that the page has exceeded our size limits, which may prevent it from being published.
- **Rendering with Liquid personalization:** The total size must not exceed 1&nbsp;MB. Otherwise, the page may be automatically unpublished by Braze.

### Avoid unpublishing landing pages

If your page exceeds these size limits, you'll receive an email that it may be unpublished if it continues to exceed the limit. When the threshold is reached, the page will be automatically unpublished, and you'll receive a notification.

To prevent your page from exceeding size limits or experiencing slow load times, make sure to use Liquid personalization that:

- Doesn't continuously loops through or references large data sets.
- Doesn't rely on extensive mathematical or conditional logic within the Liquid block.

### Use Liquid for identified and anonymous users 

Liquid can customize the landing page experience for both identified and anonymous visitors.

- **Identified users:** Link to the landing page from a Braze message and include the [landing page Liquid tag]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users/#using-landing-page-liquid-tags). This associates the user with their Braze profile and personalizes the page experience.
- **Anonymous visitors:** Use Liquid for contextual, non–profile-based content, such as a random number or a time-of-day greeting.

## Fallback pages

If your users attempt to access a page that has been unpublished, they'll see a message indicating that the page cannot currently be loaded. Reasons that a page has been unpublished include:

- Complex or broken Liquid, which can cause long render times
- User network issues
- Exceeding the maximum landing page size limits
