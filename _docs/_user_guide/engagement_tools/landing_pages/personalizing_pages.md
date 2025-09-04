---
nav_title: Personalizing Landing Pages
article_title: Personalizing Landing Pages
description: "This article covers how to personalize Braze landing pages with the drag-and-drop editor."
page_order: 4
---

# Personalizing Landing Pages

> Liquid personalization for landing pages is only available on the Pro tier of Landing Pages. Currently, Connected Content and Promo Codes are not supported via liquid personalization in landing pages.

## How to Personalize Pages

Within the Drag and Drop editor, you can insert liquid personalization both within the editor and in the page or block settings in the right-hand panel. For detailed instructions on implementing liquid, please reference our [liquid documentation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid-1).

## Previewing & Testing Personalized Pages

When previewing a landing page within the editor, you can view the page as a random user, an existing user, or a custom user.

However, when previewing the landing page from the datatable or the Landing Page details page, you will only be able to view it as a random user.

## Personalization Considerations on Landing Pages

To maintain optimal performance for your end users, please note the following size limits:

- When saving a landing page, if the size exceeds **500KB**, you may receive a warning message indicating that the page has exceeded our size limits, which may prevent it from being published.
- When rendering with liquid personalization, the total size must not exceed **1MB**; otherwise, the page may be automatically unpublished by Braze.

If your page violates these size limits, you will be notified via email that it may be unpublished if it continues to exceed the limit. Once the threshold is reached, the page will automatically be unpublished, and you will receive a notification.

### How to Avoid Unpublishing

To prevent your page from violating size limits or experiencing slow load times, avoid using liquid personalization that:

- Continuously loops through or references large data sets
- Relies on extensive mathematical or conditional logic within the liquid block

## Fallback Pages

If your end users attempt to access a page that has been unpublished due to any of the following reasons, they will see a message indicating that the page cannot currently be loaded:

- Complex or broken liquid causing long render times
- User network issues
- Page unpublished due to exceeding the maximum size limit

