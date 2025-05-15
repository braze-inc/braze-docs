---
nav_title: About Banners
article_title: About Banners
page_order: 0
description: "This reference article provides an overview of the Braze Banner channel and common use cases."
channel:
  - banners
---

# About Banners

> With Banners, you can create personalized messaging for your users, all while extending the reach of your other channels, such as email or push notifications. You can embed Banners directly in your app or website, which lets you engage with users through an experience that feels natural.

Banners are available as part of your Message Credits entitlements. If you're not on our flexible Message Credits model, Banners are available as an add-on feature. Reach out to your Braze customer success manager for more information.

## Why use Banners?

Banners allow marketing and product teams to personalize app or website content dynamically, reflecting real-time user eligibility and behavior. They persistently display messages inline, providing non-intrusive, contextually relevant experiences that update automatically at the start of each user session.

Once Banners are integrated into an app or website, marketers can design and launch Banners using a simple drag-and-drop editor, eliminating the need for ongoing developer assistance, reducing complexity, and improving efficiency.

Because they never expire and are personalized every time a user starts a new session, they’re great for:

- Highlighting featured content, trending products, or promotions
- Notifying users about upcoming events or important dates
- Promoting loyalty programs and personalized offers
- Guiding users through onboarding flows and account setup
- Upselling or cross-selling complementary products
- Seasonal or ongoing brand campaigns

### Features

Key features for Banners include:

- **Easy content building:** Drag rows and editor blocks to structure your Banner, including images, text, buttons, email capture forms, and custom HTML.
- **Real-time preview:** Instantly preview your Banners on different device views or using custom dimensions, ensuring a seamless user experience on mobile and desktop.
- **Dynamic personalization:** Utilize Braze’s built-in personalization options and Liquid logic, refreshing dynamically for each user’s session.
- **Native prioritization:** Easily set the display priority for multiple Banners targeting the same placement, ensuring the right message reaches users at the right time.
- **Custom HTML support:** Add custom HTML blocks when advanced customization or integration with existing web styles is required.

## How it works 

Banners are inline, embedded messages integrated into your app or website experience. Delivered as dynamically generated HTML content, Banners allow flexible rendering tailored to your design and layout.

They use two key components to designate where and how they display in your app or website:

### Placement {#placement-id}

Placements are specific locations within your app or website where Banners can appear. Each placement acts as a container or slot designated by your developers during the initial integration. Common examples include the top of your homepage, product detail pages, checkout flows, or custom positions tailored to your app or website. After placements are configured, marketers can assign a banner directly to these areas

### Prioritization

Prioritization controls the order in which multiple Banners compete for the same placement. When more than one Banner qualifies for a given placement and audience segment, prioritization ensures that the most relevant message is displayed first. Priorities are easily adjustable when creating a Banner.

## Use cases

| Use case | Explanation |
| --- | --- |
| Announcements | Keep relevant announcements like policy changes at the forefront of your app experience. |
| Personalizing offers | Show tailored promotions based on each user’s browsing history, cart content, subscription tier, and loyalty status. |
| Targeting new user engagement | Guide onboarding or account setup by walking new users through important setup steps. |
| Sales and promotions | Promote complementary products persistently and directly on your homepage. Or, keep your time-sensitive promotions visible and actionable, without being disruptive. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrating Banners

Your developers can create Banner placements for the Braze SDK. For more details on how to integrate with Banners, refer to the [Creating Banner placements]({{site.baseurl}}/developer_guide/banners/creating_placements).

## Frequently asked questions

### How are Banners sent to my app and website?

Banners are sent as HTML.

### Can Banners be implemented in an existing (traditional) Content Card feed, or do Banners need their own code container? Should they be incorporated with an existing Content Card feed?

Banners are different from Content Cards, meaning you can’t use Banners and Content Cards in the same feed. To replace existing Content Card feeds with Banners, you’ll need to use a new integration.
