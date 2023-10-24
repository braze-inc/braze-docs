---
nav_title: SmarterSends
article_title: SmarterSends - A Distributed Marketing Platform
page_order: 1

description: "The fastest way to enable your distributed marketing team to create, schedule, and deploy marketing campaigns using the power of Braze"
alias: /partners/smartersends/

page_type: partner
search_tag: Partner
hidden: true
layout: dev_guide
---

# SmarterSends

> [SmarterSends][2] is the fastest way to enable your distributed marketing team to create, schedule, and deploy marketing campaigns using the power of Braze. 
> * Empower hundreds or thousands of users to create and send campaigns.
> * Enforce brand and legal compliance with total control over the content, look and feel and underlying data used within your distributed campaigns.
> * Combine the power of Braze with the hyper-localized content owned by your distributed users to elevate your marketing campaigns and increase ROI.
> * It only takes 15 minutes to setup and integrate with your Braze instance

## Prerequisites

SmarterSends can be integrated with your Braze workspace in 15 minutes or less. Below you will find a list of requirements needed to get started. Additional documentation is available to walk you through the integration, configuration and customization of your SmarterSends instance.
<br/><br/>


| Requirement           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Partner account       | A SmarterSends account is required to take advantage of this partnership. Sign up for a [free 30-day free trial][2] at any time.                                                                                                                                                                                                                                                                                                                               |
| Braze REST API key    | A Braze REST API key with `users.track`, `users.export.ids`, `messages.schedule.create`, `messages.schedule.update`, `messages.schedule.delete`, `sends.id.create`, `segments.list`, `segments.data_series`, `segments.details`, `sends.data_series` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. Be sure to whitelist the SmarterSends IP address, _available in your instance,_ for additional security |
| Braze REST endpoint   | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance.                                                                                                                                                                                                                                                                                                                                                                      |
| Braze API Campaign ID | The Braze API Campaign ID is the unique identifier for all campaigns sent through SmarterSends. This can be created in the Braze dashboard at **Messaging** > **Campaigns**.                                                                                                                                                                                                                                                                                    |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can create an API key at **Developer Console** > **API Settings**.
{% endalert %}

## Use cases

Distributed marketing, also known as local store marketing or multi-location marketing, involves creating and executing marketing campaigns across multiple channels and locations. It is the empowering of non-marketers, to create, schedule and deploy brand compliant marketing messages, using a simple-to-master platform.

The top five benefits of distributed marketing include:

1) **Increased Reach:** By utilizing multiple channels and locations, distributed marketing enables you to reach a wider audience and target customers in different locations, resulting in increased brand exposure. [Read the Case Study][3]

2) **Targeted Messaging:** Different channels and locations may require different messaging to resonate with the local audience. Distributed marketing allows for tailored messaging, resulting in more effective communication and engagement with customers. [Read the Case Study][4]

3) **Improved Brand Consistency:** By using a distributed marketing approach, you can ensure that your brand messaging and image is consistent across all channels and locations, which is important for building a strong and recognizable brand. [Read the Case Study][5]

2) **Better Insights:** Distributed marketing allows for the collection of data from various channels and locations, providing valuable insights into customer behavior and preferences, which can be used to refine marketing strategies and tactics both on the local and global levels. [Read the Case Study][6]

3) **Increased Efficiency:** By leveraging the strengths of different channels and locations, distributed marketing can result in more efficient use of resources, such as time and money, while still achieving the desired marketing goals. [Read the Case Study][7]

## Integration

Below we'll walk you through the process of integrating your SmarterSends instance with your Braze workspace.  You can get this done in 15 minutes or less.

The items you'll need to create within your Braze workspace include:
* A Rest API Key with the correct permissions applied
* An Application ID
* An API Campaign with message variants for each Group you'll setup within SmarterSends
In order to start the integration process, go ahead and log into both your Braze workspace and your SmarterSends instance. We'll start in your Braze workspace.

### Step 1: Create a Rest API Key
   * In the side navigation click Settings then click API Keys.
   * Click Create New API Key
   * Name the API Key "SmarterSends" so you can identify the purpose of the key.
   * Select the following permissions for this key to allow SmarterSends to interact with your Braze workspace:
     * users.track
     * users.export.ids
     * messages.schedule.create
     * messages.schedule.update
     * messages.schedule.delete
     * sends.id.create
     * segments.list
     * segments.data_series
     * segments.details
     * sends.data_series
   * And add the SmarterSends IP address to the Whitelist IP
   * Click Save API Key
   * Copy the provided API key and paste into the Braze Email Service Provider settings within SmarterSends

### Create or Copy and Existing Application ID
   * In the side navigation of your Braze workspace click Settings and click App Settings
   * You can choose to set up a new application or use the application id from an existing application within your workspace.
   * The application id is labeled API Key in your Application Settings view
   * Copy this and paste it into the App ID field within SmarterSends

### Create an API Campaign
   * The API Campaign allows tracking metrics for all SmarterSends mailings within Braze and enables SmarterSends to trigger these API based campaigns.
   * In the side navigation click Messages and click Campaigns.
   * Click Create Campaign and select API Campaigns
   * We suggest naming this campaign SmarterSends Campaign.
   * You can now copy the Campaign ID found on this page into the Campaign ID field within SmarterSends.
   * You need to add at least one Message to the Braze API Campaign to track metrics against. Click Add Message and select Email. You can name the message group within Braze and then copy the Message Variation ID to the Message Variant ID within SmarterSends. This default message id will be used if you choose not to create a message id for each group within SmarterSends.
   * We do suggest that a Message Variant ID is created for each Group you will create within SmarterSends. This will allow you to view metrics for each groups sends separately within your Braze workspace. This can be very beneficial to identify trends across groups when building reports within your Braze workspace.
   * For each Group you create within SmarterSends, add a Message variant to your API Campaign within Braze and copy the Message Variant ID to the Group's Message Variant ID field within SmarterSends.


## Customization

Defining the attributes and custom attributes your distributed users can use for both personalization and in group restrictions.

Define the segments your distributed users can use to target their campaigns based on the segments you create within your Braze workspace

Each SmarterSends instance is fully customizable with your brand's logo colors and custom domain name, creating a familiar environment for your distributed users to log into.



[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://smartersends.com
[3]: https://smartersends.com/blog/make-sharing-distributable-content-simple
[4]: https://smartersends.com/blog/consolidate-disparate-systems
[5]: https://smartersends.com/blog/empower-non-technical-users
[6]: https://smartersends.com/blog/harnessing-the-power-of-local-store-marketing
[7]: https://smartersends.com/blog/scale-your-workflow