# Banners

> With Banners, you can create personalized messaging for your users, all while extending the reach of your other channels, such as email or push notifications. You can embed Banners directly in your app or website, which lets you engage with users through an experience that feels natural.

## Prerequisites

Banners are available as part of your Message Credits entitlements. If you're not on our flexible Message Credits model, Banners are available as an add-on feature. Reach out to your Braze customer success manager for more information.

## Why use Banners?

Banners allow marketing and product teams to personalize app or website content dynamically, reflecting real-time user eligibility and behavior. They persistently display messages inline, providing non-intrusive, contextually relevant experiences that update automatically at the start of each user session.

Once Banners are integrated into an app or website, marketers can design and launch Banners using a simple drag-and-drop editor, eliminating the need for ongoing developer assistance, reducing complexity, and improving efficiency.

| Use case | Explanation |
| --- | --- |
| Announcements | Keep announcements like upcoming events or policy changes at the forefront of your app experience. |
| Personalizing offers | Show personalized promotions and incentives based on each user’s browsing history, cart content, subscription tier, and loyalty status. |
| Targeting new user engagement | Guide new users through onboarding flows and account setup. |
| Sales and promotions | Highlight featured content, trending products, and ongoing brand campaigns persistently and directly on your homepage without disrupting the user experience. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## How it works 

Banners are inline, embedded messages integrated into your app or website experience. Because they're delivered as dynamically generated HTML content, Banners are tailored to your design and layout. To choose where and how they're displayed in your app or website, you'll rely on **Placements** and **Prioritization**.

### Placements {#placement-id}

Placements are specific locations within your app or website where Banners can appear. Each placement acts as a container or slot designated by your developers during the initial integration. Common examples include the top of your homepage, product detail pages, and checkout flows. After placements are configured, marketers can assign a banner directly to these areas.

### Prioritization

Prioritization controls the order in which multiple Banners compete for the same placement. When more than one Banner qualifies for a given placement and audience segment, prioritization ensures that the most relevant message is displayed first. Priorities are easily adjustable when creating a Banner or when editing a placement.

## Features

Features for Banners include:

- **Easy content building:** Create and preview your Banner using a visual, drag-and-drop editor with support for images, text, buttons, email capture forms, custom code, and more.
- **Flexible placements:** Define multiple locations within your application or website where Banners can appear, enabling precise targeting to specific contexts or user experiences.
- **Dynamic personalization:** Banners dynamically refresh with every new user session, ensuring content stays current and personalized using Braze’s built-in personalization tools and Liquid logic.
- **Native prioritization:** Set the display priority for when multiple Banners target the same placement, ensuring the right message reaches users at the right time.
- **Custom HTML support:** Incorporate custom HTML blocks for advanced customization or seamless integration with your existing web styles.

## Integrating Banners

Your developers can create Banner placements for the Braze SDK. For more details on how to integrate with Banners, refer to the [Creating Banner placements]({{site.baseurl}}/developer_guide/banners/creating_placements).
