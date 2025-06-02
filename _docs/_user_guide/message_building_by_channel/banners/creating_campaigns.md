---
nav_title: Creating Campaigns
article_title: Creating Banner campaigns in Braze
page_order: 1
description: "This reference article covers how to create, compose, configure and send Banners using Braze campaigns."
tool:
  - Campaigns
channel:
  - banners
---

# Creating Banner campaigns

> Learn how to create Banners when you build a campaign in Braze. For more general information, see [About Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners).

## Prerequisites

Before you can launch your Banner campaign, your development team will need to [set up placements in your app or website]({{site.baseurl}}/developer_guide/banners/creating_placements/). You can still draft your Banner campaign in the meantime&#8212;you just won't be able to launch the campaign.

## Creating a Banner campaign

{% multi_lang_include banners/creating_placements.md section="user" %}

### Step 2: Create a campaign

1. Go to **Messaging** > **Campaigns** and select **Create Campaign**.
2. Select **Banner**.
3. Name your campaign something clear and meaningful.
4. Add teams and tags as needed. Tags make your campaigns easier to find and build reports out of. For example, when using the Report Builder, you can filter by the relevant tags.
5. Select the placement you previously created to associate it with your campaign.
6. Add variants as needed. You can choose a different message type and layout for each one. For more information on variants, refer to [Multivariate and A/B testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).

### Step 3: Compose a Banner {#compose-a-banner}

To compose your Banner, select **Edit message**. Here, you can create the Banner and define on-click behavior. 

#### Step 3.1: Style the Banner

You can drag and drop blocks and rows into the canvas area to start building your message.

To customize your message's background properties, border settings, and more, select **Styles**. If you only want to customize the style for a specific block or row, select it to make changes.

![Style panel of the Banner composer.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Step 3.2: Define on-click behavior

When a user clicks a link in the Banner, you can choose to navigate them deeper into your app or redirect them to another webpage. Additionally, you can choose to [log a custom attribute or event]({{site.baseurl}}/developer_guide/analytics/), which will update your user's profile with custom data when they click the Banner.

{% alert important %}
{::nomarkdown}
On-click behavior can be overridden if a specific element (such as a button, link, or image, of the Banner) has its own on-click behavior. For example, given the following on-click behaviors:<br><br><ul><li>A Banner has an on-click behavior that redirects to a website's homepage.</li><li>An image in the Banner has an on-click behavior that redirects to a website's product page.</li></ul>If a user clicks the image, they'll be redirected to the product page. However, clicking the surrounding area in the Banner will redirect them to the homepage.
{:/}
{% endalert %}

### Step 4: Set campaign duration

Choose a start date and time for your Banner campaign. By default, Banners last indefinitely. You can change this by selecting **End Time** and specifying an end date and time.

### Step 5: Set Banner priority (optional)

[Banner priority]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) determines the order in which Banners are displayed if they share the same placement. To manually set the priority:

1. Select **Set exact priority**.
2. Drag and drop the campaigns to order them with the correct priority.
3. Select **Apply Sort**.

{% alert tip %}
If you have multiple Banner campaigns using the same placement ID, we recommend using the drag-and-drop priority sorter to define the exact priority.
{% endalert %}

### Step 6: Test your message (optional)

{% multi_lang_include banners/testing.md page="campaigns" %}

### Step 7: Finish building the campaign

Finish building your campaign by completing the following:

| Option | Description |
| --- | --- |
| **Targeted Users** | Target users by choosing segments or filters to narrow down your audience. You’ll automatically be given a snapshot of the approximate segment population. Exact segment membership is calculated just before the message is sent. |
| **Conversion Events** | Track how often users perform specific actions after receiving a campaign. You can define conversion events with up to a 30-day window to count the action as a conversion. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Step 8: Launch your campaign

After you're finished building and testing your Banner campaign, you're ready to launch!
