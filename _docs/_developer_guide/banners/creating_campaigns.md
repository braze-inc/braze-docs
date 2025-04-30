---
nav_title: Creating Campaigns
article_title: Creating Banner campaigns
alias: "/create_banner/"
description: "This reference article covers how to create and send Banners using Braze campaigns."
page_order: 2
---

# Creating Banner campaigns

> Learn how to create Banners when you build a campaign in Braze. For more general information, see [About Banners]({{site.baseurl}}/developer_guide/banners/).

{% alert important %}
Banners are currently in early access. Contact your Braze account manager if you’re interested in participating in this early access.
{% endalert %}

## Prerequisites {#prerequisite-determine-placement}

These are the minimum SDK versions to start using Banners:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Creating a Banner campaign

{% multi_lang_include banner_cards/creating_placements.md %}

### Step 2: Create a campaign

1. Go to **Messaging** > **Campaigns** and select **Create Campaign**.
2. Select **Banner**.
3. Name your campaign something clear and meaningful.
4. Add teams and tags as needed. Tags make your campaigns easier to find and build reports out of. For example, when using the Report Builder, you can filter by the relevant tags.
5. Select the placement you previously created to associate it with your campaign.
6. Add variants as needed. You can choose a different message type and layout for each one. For more information on variants, refer to [Multivariate and A/B testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

### Step 2: Compose a message

To compose your Banner, select **Edit message**. Here, you can style the Banner and define on-click behavior.

#### Step 2.1: Style the Banner {#styles}

You can drag and drop blocks and rows into the canvas area to start building your message. To customize your message's background properties, border settings, and more, select **Styles**. If you only want to customize the style for a specific block or row, select it to make changes.

![Style panel of the Banner composer.]({% image_buster /assets/img/banner_cards/banner_card_styles.png %})

#### Step 2.2: Define on-click behavior

When a customer clicks a link in the Banner, you can choose to navigate them deeper into your app or redirect them to another webpage. Additionally, you can choose to [log a custom attribute or event]({{site.baseurl}}/developer_guide/analytics/), which will update your customer’s profile with custom data when they click the Banner.

### Step 3: Set Banner priority {#set-priority}

When multiple campaigns reference the same placement ID, Banners are displayed in order of priority level. By default, newly created Banners are set to medium, but you can manually set the priority to high, medium, or low. If multiple Banners share the same priority level, the newest Banner will be displayed first.

To set the priority for a Banner:

1. Select **Priority sorter**.
2. Drag and drop the campaigns to order them with the correct priority.
3. Select **Apply sort**.

### Step 3: Finish building the campaign

Finish building your campaign by completing the following:

| Option                    | Description |
|---------------------------|-------------|
| **Campaign Duration** | Choose a start date and time for your Banner campaign. By default, Banners last indefinitely. You can change this by selecting **End Time** and specifying an end date and time. |
| **Targeted Users** | Target users by choosing segments or filters to narrow down your audience. You’ll automatically be given a snapshot of the approximate segment population. Exact segment membership is calculated just before the message is sent. |
| **Conversion Events** | Track how often users perform specific actions after receiving a campaign. You can define conversion events with up to a 30-day window to count the action as a conversion. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Step 4: Test and launch

After building your campaign, test and review it to make sure your campaign works as expected. When you’re ready, launch your Banner campaign!
