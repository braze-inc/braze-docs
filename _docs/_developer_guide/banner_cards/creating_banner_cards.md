---
nav_title: Creating Banner Cards
article_title: Creating Banner Cards
alias: "/create_banner_card/"
description: "This reference article covers how to create and send Banner Cards using Braze campaigns."
hidden: true
page_type: reference
---

# Creating Banner Cards

> Learn how to create Banner Cards in Braze when you build campaigns.

{% alert important %}
Banner Cards are currently in early access. Contact your Braze account manager if you’re interested in participating in this early access.
{% endalert %}

## About Banner Cards

Similar to [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/), Banner Cards are embedded directly in your app or website so that you can engage users with an experience that feels natural. They’re a quick and seamless solution to create personalized messaging for your users all while extending the reach of other channels (such as email or push notifications). 

Banner Cards are great for:

- Highlighting featured content
- Notifying users about upcoming events
- Sharing updates on loyalty programs

Because Banner Cards personalize each time a user starts a new session and can be configured to never expire, they’re a helpful tool to add to your engagement strategy.

## Prerequisites

Before you can create Banner Cards, you'll need to [create Banner Card placements](https://braze.com/docs/developer_guide/banner_cards/creating_placements) in your app.

## Creating a Banner Card

### Step 1: Create your campaign

To create a new campaign in Braze:

1. Go to **Messaging** > **Campaigns** and select **Create Campaign**.
2. Select **Banner Card**.
3. Name your campaign something clear and meaningful.
4. Add teams and tags as needed. Tags make your campaigns easier to find and build reports out of. For example, when using the Report Builder, you can filter by the relevant tags.
5. Select a [placement](#prerequisite-determine-placement) to associate with your campaign. This is where the Banner Card will appear in your app or site.
6. Add and name as many variants as you like for your campaign. You can choose different message types and layouts for each added variant. For more information on variants, refer to [Multivariate and A/B testing](https://braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing/).

### Step 2: Compose a Banner Card

To edit the details of your message’s content:

1. Select **Edit message**. The composer will open.
2. Choose a row style that fits your message. Drag and drop a row into the canvas area.
3. Drag and drop blocks into the row to build your message.
4. Define the [style](#styles) of your message.

#### Styles

Select **Style** to adjust the settings to apply to all blocks in the message.

![Style panel of the Banner Card composer.]({% image_buster /assets/img/banner_cards/banner_card_styles.png %})

Here, you can provide custom styling such as background properties, border settings, and defaults to your Banner Cards. Styles applied here can be overridden for a specific block or row. To override styles, select the specific block or row to view its properties and make changes.

#### On-click behavior

When your customer clicks on a link in the Banner Card, you can either navigate them deeper into your app or redirect them to another webpage.

You can also choose to log a custom attribute or custom event. This will update your customer’s profile with custom data when they click the Banner Card.

### Step 3: Build the remainder of your campaign

Next, build the remainder of your campaign. Refer to the next sections for more details on how to best use our tools to build Banner Cards.

#### Choose a campaign duration

Select the start date and time for the Banner Card campaign. 

By default, Banner Cards last indefinitely. You can change this by selecting **End Time** and specifying an end date and time.

#### Choose users to target

Next, target users by choosing segments or filters to narrow down your audience. You’ll automatically be given a snapshot of what that approximate segment population looks like right now. Keep in mind that exact segment membership is always calculated just before the message is sent.

#### Choose conversion events

Braze allows you to track how often users perform specific actions, and conversion events, after receiving a campaign. You can allow up to a 30-day window during which a conversion will be counted if the user takes the specified action.

### Step 4: Test and deploy

After building your campaign, test and review it to make sure your campaign works as expected. Then, you’re ready to launch your Banner Card campaign!

## Setting Banner Card prioritization

If two Banner Card campaigns share the same placement, priority determines which one appears first. Higher-priority messages will be shown before lower-priority ones.

You can choose between the following Banner Card priorities:

- Low priority (shown after other messages)
- Medium priority
- High priority (shown before other messages)

By default, the Banner Card priority is set to medium, with the most recently created Banner Cards having the highest relative property.

The high, medium, and low options are buckets, and as such multiple messages could have the same selected priority. To set priorities in these buckets, do the following:

1. Select **Priority sorter**.
2. Drag and drop the campaigns to order them with the correct priority.
3. Select **Apply sort**.

## Things to know

### Expiration

By default, Banner Cards do not have an expiration date, but you can add an optional end date.

### Placement management

Placements are unique per workspace, and each placement can be used in up to 10 campaigns.

Placement IDs must be unique to a workspace, and should not be edited after launch. Work with your developer team to define this ID, because they will need to use it during the integration. 

### Analytics

The following table defines key Banner Card metrics. For a full list of metrics, definitions, and calculations, refer to our [Report Metrics Glossary](https://braze.com/docs/user_guide/data_and_analytics/report_metrics/).

| Metric | Definition |
| --- | --- |
| [Total Impressions](https://braze.com/docs/user_guide/data_and_analytics/report_metrics#total-impressions) | _Total Impressions_ is the number of times the message has been loaded and appears on a user’s screen, regardless of prior interaction (for example, if a user is shown a message twice, they will be counted twice). |
| [Unique Impressions](https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#unique-impressions) | _Unique Impressions_ is the total number of users who received and viewed a given message in a day. Each user is only counted once. |
| [Total Clicks](https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#total-clicks) | _Total Clicks_ is the total number (and percentage) of users who clicked within the delivered message, regardless of whether the same user clicks multiple times. |
| [Unique Clicks](https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#unique-clicks) | _Unique Clicks_ is the distinct number of recipients who have clicked within a message at least once and is measured by [dispatch_id](https://braze.com/docs/help/help_articles/data/dispatch_id/). Each user is only counted once. |
| [Primary Conversions](https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#primary-conversions-a-or-primary-conversion-event) | _Primary Conversions (A) or Primary Conversion Event_ is the number of times a defined event occurred after interacting with or viewing a received message from a Braze campaign. This defined event is determined by you when building the campaign. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
