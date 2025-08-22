# Banners

> With Banners, you can create personalized messaging for your users, all while extending the reach of your other channels, such as email or push notifications. You can embed Banners directly in your app or website, which lets you engage with users through an experience that feels natural.

![An example Banner rendered on a device.]({% image_buster /assets/img/banners/sample_banner.png %})

## Prerequisites

Banners are available as part of your Message Credits entitlements. If you're not on our flexible Message Credits model, Banners are available as an add-on feature. Reach out to your Braze customer success manager for more information.

## Why use Banners?

Banners allow marketing and product teams to personalize app or website content dynamically, reflecting real-time user eligibility and behavior. They persistently display messages inline, providing non-intrusive, contextually relevant experiences that update automatically at the start of each user session.

After Banners are integrated into an app or website, marketers can design and launch Banners using a simple drag-and-drop editor, eliminating the need for ongoing developer assistance, reducing complexity, and improving efficiency.

| Use case | Explanation |
| --- | --- |
| Announcements | Keep announcements like upcoming events or policy changes at the forefront of your app experience. |
| Personalizing offers | Show personalized promotions and incentives based on each user’s browsing history, cart content, subscription tier, and loyalty status. |
| Targeting new user engagement | Guide new users through onboarding flows and account setup. |
| Sales and promotions | Highlight featured content, trending products, and ongoing brand campaigns persistently and directly on your homepage without disrupting the user experience. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Features

Features for Banners include:

- **Easy content building:** Create and preview your Banner using a visual, drag-and-drop editor with support for images, text, buttons, email capture forms, custom code, and more.
- **Flexible placements:** Define multiple locations within your application or website where Banners can appear, enabling precise targeting to specific contexts or user experiences.
- **Dynamic personalization:** Banners dynamically refresh with every new user session, ensuring content stays current and personalized using Braze’s built-in personalization tools and Liquid logic.
- **Native prioritization:** Set the display priority for when multiple Banners target the same placement, ensuring the right message reaches users at the right time.
- **Custom HTML support:** Incorporate custom HTML blocks for advanced customization or seamless integration with your existing web styles.

## About Banners {#about-banners}

### Placement IDs {#placement-id}

Banner placements are specific locations in your app or website [you create with the Braze SDK]({{site.baseurl}}/developer_guide/banners/creating_placements/) that designate where Banners can appear.

Common locations include the top of your homepage, product detail pages, and checkout flows. After placements are created, Banners can be [assigned in your Banner campaign]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/).

Additionally, Banner placements are unique to each workspace and can only be used across 10 campaigns within a single workspace. Placements within each workspace must be given a unique ID, which you'll assign when creating a placement in Braze.

{% alert important %}
Avoid modifying placement IDs after launching a Banner campaign.
{% endalert %}

### Banner priority {#priority}

When multiple campaigns reference the same placement ID, Banners are displayed in order of priority: high, medium, or low. By default, newly created Banners are set to medium, but you can [manually set the priority]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/#set-priority) when you create or edit your Banner campaign. 

If multiple Banners are set to the same priority, the newest Banner that user is eligible for is displayed first.

### Placement requests {#requests}

{% multi_lang_include banners/placement_requests.md %}

### Message delivery

Banner messages are delivered to your app or website as HTML content, typically rendered inside an iframe. This ensures that your Banners will render consistently across devices, and helps you keep their styles and scripts separate from the rest of your code.

Iframes allow for dynamic and personalized content updates that don't require changes to your codebase. Each iframe retrieves and displays the HTML for each user session using campaign targeting and personalization logic.

### Dimensions and sizing

Here's what you need to know about Banner dimensions and sizing:

- While the composer allows you to preview Banners in different dimensions, that information isn't saved or sent to the SDK.
- The HTML will take up the full width of the container it's rendered in.
- We recommend making a fixed dimension element and testing those dimensions in composer.

## Limitations

Each workspace can support up to 200 active Banner campaigns. If this limit is reached, you'll need to [archive or deactivate]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) an existing campaign before creating a new one.

Additionally, Banner messages do not support the following features:

- Canvas integration
- API-triggered and action-based campaigns
- Connected Content
- Promotional codes
- User-controlled dismissals
- `catalog_items` using the [`:rerender` tag]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/#using-liquid)

{% alert tip %}
Want to help prioritize what's next? Contact [banners-feedback@braze.com](mailto:banners-feedback@braze.com).
{% endalert %}

## Next steps

Now that you know about Banners, you're ready for the next steps:

1. [Creating Banner placements in your app or website]({{site.baseurl}}/developer_guide/banners/creating_placements/)
2. [Creating Banner campaigns in Braze]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/)
3. [Tutorial: Displaying a Banner by Placement ID]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
