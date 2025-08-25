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

#### Step 3.2: Define on-click behavior (optional)

When a user clicks a link in the Banner, you can choose to navigate them deeper into your app or redirect them to another webpage. Additionally, you can choose to [log a custom attribute or event]({{site.baseurl}}/developer_guide/analytics/), which will update your user's profile with custom data when they click the Banner.

{% alert important %}
{::nomarkdown}
On-click behavior can be overridden if a specific element (such as a button, link, or image, of the Banner) has its own on-click behavior. For example, given the following on-click behaviors:<br><ul><li>A Banner has an on-click behavior that redirects to a website's homepage.</li><li>An image in the Banner has an on-click behavior that redirects to a website's product page.</li></ul>If a user clicks the image, they'll be redirected to the product page. However, clicking the surrounding area in the Banner will redirect them to the homepage.
{:/}
{% endalert %}

#### Step 3.3: Add custom properties (optional) {#custom-properties}

{% alert important %}
Custom properties for Banners are currently in early access. Contact your Braze account manager if you're interested in participating
{% endalert %}

You can add custom properties to a Banner to attach structured metadata, such as strings or JSON objects. These properties don’t affect how the Banner is displayed but can be [accessed through the Braze SDK]({{site.baseurl}}/developer_guide/banners/managing_placements/#accessing-properties) to modify your app’s behavior or appearance. For example, you could:

- Change layout or styling based on a property like `color` or `expanded`.
- Use metadata such as a `timestamp` or JSON object to trigger custom behavior.
- Detect control variants and decide whether to hide a container or show alternate content.

To add a custom property, select **Settings** > **Properties** > **Add property**.

![The properties page showing the option to add the first custom property to a Banner campaign.]({% image_buster /assets/img/banners/add_property.png %})

For each property you'd like to add, fill out the following:

| Field | Description | Example |
|-------|-------------|---------|
| Property type | The data type for the property. Supported types include string, boolean, number, timestamp, image URL, and JSON object. | String |
| Property key | The unique identifier for the property. This key is used in the SDK to access the property. | `color` |
| Value | The value assigned to the property. Must match the selected property type. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

When you're finished, select **Done**.

![The properties page with a string property with a key of color and value of #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

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

1. In **Target Audiences**, choose segments or filters to narrow down your audience. You’ll automatically be given a preview of the approximate segment population. Exact segment membership is calculated just before the message is sent.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2. In **Assign Conversions**, track how often users perform specific actions after receiving a campaign by defining conversion events with up to a 30-day window to count the action as a conversion.

### Step 8: Launch your campaign

After you're finished building and testing your Banner campaign, you're ready to launch!
