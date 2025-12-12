---
nav_title: SmarterSends
article_title: SmarterSends
description: "This reference article outlines the partnership between Braze and SmarterSends, an easy-to-use interface designed for non-marketers to create, schedule, and deploy brand compliant emails campaigns."
alias: /partners/smartersends/
page_type: partner
search_tag: Partner
---

# SmarterSends

> [SmarterSends](https://smartersends.com) drives personalization with marketing campaigns that businesses can create, schedule, and deploy to enforce brand and legal compliance with control over the content and data used. 

_This integration is maintained by SmarterSends._

## About the integration

The Braze and SmarterSends partnership allows you to combine the power of Braze with the hyper-localized content owned by your distributed users to elevate your marketing campaigns.

## Prerequisites

| Requirement | Description |
| --- | --- |
| SmarterSends account | A [SmarterSends account](https://smartersends.com) is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with these permissions: {::nomarkdown}<ul><li><code>users.track</code></li><li><code>users.export.ids</code></li><li><code>messages.schedule.create</code></li><li><code>messages.schedule.update</code></li> <li><code>messages.schedule.delete</code></li><li><code>sends.id.create</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>sends.data_series</code></li></ul>{:/} This can be created in the Braze dashboard from **Settings** > **API Keys**. For additional security, allowlist the SmarterSends IP address (available in your instance). |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
| Braze API campaign ID | The [Braze API campaign ID]({{site.baseurl}}/api/api_campaigns/) is the unique identifier for all campaigns sent through SmarterSends. This can be created in the Braze dashboard at **Messaging** > **Campaigns**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

With the Braze and SmarterSends integration, you can take advantage of distributed marketing by creating and executing marketing campaigns across multiple channels and locations. These advantages include:

1. **Increased reach:** Using multiple channels and locations to reach a wider audience and target customers in different locations, resulting in increased brand exposure.
2. **Targeted messaging:** Tailoring messaging across channels and locations to resonate with local audiences for more effective communication and engagement with customers. 
3. **Improved brand consistency:** Aligning your brand messaging and image across all channels and locations, which is important for building a strong and recognizable brand.
4. **Better insights:** Collecting data from various channels and locations, providing valuable insights into customer behavior and preferences, which can be used to refine marketing strategies and tactics both on the local and global levels.
5. **Increased efficiency:** Leveraging the strengths of different channels and locations, which can result in more efficient use of resources while still achieving the desired marketing goals. 

## Integration

### Step 1: Create a REST API key

1. In Braze, go to **Settings** > **API Keys** and click **Create New API Key**.
2. Enter a name for the API key.
3. Select the following permissions for this key to allow SmarterSends to interact with your Braze workspace.
- `users.track`
- `users.export.ids`
- `messages.schedule.create`
- `messages.schedule.update`
- `messages.schedule.delete`
- `sends.id.create`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `sends.data_series`
4. Add the SmarterSends IP address to the **Whislist IPs** section.
5. Click **Save API Key**.
6. Copy and paste the API key with the appropriate permissions to the **Braze Email Service Provider** settings in SmarterSends.

### Step 2: Create or copy an application ID

1. In your Braze workspace, go to **Settings** > **App Settings**. 
2. Set up a new app or use the application ID from an existing application within your workspace. Note the application ID is labeled as the **API Key**. 
3. Copy and paste this ID into the **App ID** field in SmarterSends.

### Step 3: Create an API campaign

An API campaign allows tracking metrics for all SmarterSends mail within Braze and enables SmarterSends to trigger these API-based campaigns.

1. In Braze, [create an API campaign]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign).
2. Click **Email** under **Select Message Channel** to add a messaging channel to begin tracking metrics.
3. Next, copy and paste the campaign ID from Braze to the **Campaign ID** field in SmarterSends. 
4. Copy and paste the message variation ID from Braze to the **Message Variant ID** field in SmarterSends. This will be the default message ID used if you decide not to create a message ID for each group in SmarterSends.
5. For each group you create in SmarterSends, add a message variant to your API campaign in Braze. Then, copy the message variant ID to the group's message variant ID in SmarterSends.

{% alert tip %}
Create a message variant ID for each group you create in SmarterSends to view metrics for each group's sends separately in your Braze workspace. This can be helpful to identify trends across groups when building reports in Braze.
{% endalert %}

## Customization

Each SmarterSends instance is fully customizable with your brand's logo colors and custom domain name, creating a familiar environment. Additionally, for further personalization, you can define the attributes and custom attributes to target users in campaigns based on the segments within your Braze workspace.


