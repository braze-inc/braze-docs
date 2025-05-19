---
nav_title: Creating a Banner
article_title: Creating a Banner
page_order: 1
description: "This reference article covers how to create, compose, configure and send Banners using Braze campaigns."
tool:
  - Campaigns
channel:
  - banners
---

# Creating a Banner campaign

> This page covers how to create Banners when you build a campaign in Braze.

## Prerequisites

These are the minimum SDK versions to start using Banners:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Creating a Banner campaign

### Step 1: Create placements

If you haven’t already, you’ll need to create Banner placements in Braze that are used to define the locations in your app or site that can display Banners. To create a placement, go to **Settings** > **Banners Placements**, then select **Create placement**.

Give your placement a name and assign a Placement ID. Be sure you consult other teams before assigning an ID, as it’ll be used throughout the card’s lifecycle and shouldn’t be changed later. For more information, see Placement IDs.

### Step 2: Create a campaign

1. Go to **Messaging** > **Campaigns** and select **Create Campaign**.
2. Select **Banner**.
3. Name your campaign something clear and meaningful.
4. Add teams and tags as needed. Tags make your campaigns easier to find and build reports out of. For example, when using the Report Builder, you can filter by the relevant tags.
5. Select the placement you previously created to associate it with your campaign.
6. Add variants as needed. You can choose a different message type and layout for each one. For more information on variants, refer to [Multivariate and A/B testing].

### Step 3: Compose a Banner

To compose your Banner, select **Edit message**. Here, you can create the Banner and define on-click behavior. 

#### Step 3.1: Style the Banner

You can drag and drop blocks and rows into the canvas area to start building your message.

To customize your message's background properties, border settings, and more, select **Styles**. If you only want to customize the style for a specific block or row, select it to make changes.

![Style panel of the Banner composer.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Step 3.2: Define on-click behavior

When a user clicks a link in the Banner, you can choose to navigate them deeper into your app or redirect them to another webpage. Additionally, you can choose to [log a custom attribute or event]({{site.baseurl}}/developer_guide/analytics/), which will update your user's profile with custom data when they click the Banner.

{% alert important %}
{::nomarkdown}
On-click behavior can be overridden if a specific element (such as a button, link, or image, of the banner) has its own on-click behavior. For example, given the following on-click behaviors:<br><br><ul><li>A Banner has an on-click behavior that redirects to a website's homepage.</li><li>An image in the Banner has an on-click behavior that redirects to a website's product page.</li></ul>If a user clicks the image, they'll be redirected to the product page. However, clicking the surrounding area in the Banner will redirect them to the homepage.
{:/}
{% endalert %}

### Step 4: Set campaign duration

Choose a start date and time for your Banner campaign. By default, Banners last indefinitely. You can change this by selecting End Time and specifying an end date and time.

### Step 5: Set Banner priority

When multiple campaigns reference the same placement ID, Banners are displayed in order of priority level. By default, newly created Banners are set to medium. If multiple Banners share the same priority level, the newest Banner will be displayed first.

You can manually set the priority to high, medium, or low.

To manually set the priority for a Banner:

1. Select **Set exact priority**.
2. Drag and drop the campaigns to order them with the correct priority.
3. Select **Apply Sort**.

If you have multiple Banner campaigns using the same placement ID, we recommend using the drag-and-drop priority sorter to define the exact priority.

{% alert note %}
As you create more Banner campaigns, a new Banner's priority is set as the highest priority in the **Medium Priority** section of the exact priority sorter.
{% endalert %}

### Step 6: Finish building the campaign

Finish building your campaign by completing the following:

| Option | Description |
| --- | --- |
| **Targeted Users** | Target users by choosing segments or filters to narrow down your audience. You’ll automatically be given a snapshot of the approximate segment population. Exact segment membership is calculated just before the message is sent. |
| **Conversion Events** | Track how often users perform specific actions after receiving a campaign. You can define conversion events with up to a 30-day window to count the action as a conversion. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Step 7: Test and launch

After building your campaign, test and review it to make sure your campaign works as expected. When you’re ready, launch your Banner campaign!

## Frequently asked questions

### What are the dimensions of a Banner?

The HTML will take up the full width of the container it’s rendered in. To learn more about Banner specifications, see About Banners.

### Can I create multiple Banners using the same placement?

Only one Banner can be used for each placement ID. However, up to 10 Banners can be assigned to a placement.

### Can Banners be dismissed by a user?

No, users cannot manually dismiss Banners. However, you can control Banner visibility by managing user segment eligibility. When a user no longer meets the targeting criteria for a Banner campaign, they won't see it again on their next session.

For example, if you display a promotional Banner until a user makes a purchase, logging an event such as `purchase_completed` can remove that user from the targeted segment, effectively hiding the Banner in subsequent sessions.

### Can I export Banners campaign analytics using the Braze API?

Yes. You can use the [`/campaigns/data_series` endpoint]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) to get data on how many Banner campaigns were viewed, clicked, or converted.

### When are users segmented?

Users are segmented at the beginning of the session. If a campaign's targeted segments depend on custom attributes, custom events, or other targeting attributes, they must be present on the user at the beginning of the session. 

### How can I compose Banners to ensure the lowest latency?

The simpler the messaging in your Banner, the faster it will render. It’s best to test your Banner campaign against the expected latency for your use case. For example, be sure to test Liquid attributes like `catalog_items`.

### What Liquid tags are not supported?

The following Liquid tags aren’t supported: Connected Content, promotion codes, and catalog `:rerender` tags.

### How can click events be captured?

Click events are only captured if an on-click action is set on a `logClick` element and is called using the JS Bridge.