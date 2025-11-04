---
nav_title: Integration overview
article_title: Integration Overview
page_order: 2
description: "This article provides a basic overview of the onboarding process."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}Getting started: Integration overview

> This article provides a basic overview of the onboarding process.

![A venn diagram of four circles - discovery, integrate, quality assurance and maintain - centered around "time to value."]({% image_buster /assets/img/getting-started/getting-started-integrate-flower.png %}){: style="max-width:50%;float:right;margin-left:15px;border:none;"} 

As a technical resource, you'll empower your team by integrating Braze into your tech stack. Onboarding is broadly split up into four steps:
* [Discovery and planning](#discovery): Work with your team to align on scope, plan a structure for data and campaigns, and create an appropriate workspace structure. 
* [Integration](#integration): Execute on your plan by integrating the SDK and API, enabling messaging channels, and setting up data import and export. 
* [Quality Assurance](#qa): Confirm that the loop of data and messaging between the Braze platform and your app or site is working as expected.
* [Maintenance](#maintenance): After you've passed off Braze to your marketing team, you'll continue to make sure everything continues to run smoothly.

<br>
{% alert tip %}
We recognize that every organization has its distinct needs, and Braze is built to cater to a diverse range of customization options that can be tailored to your specific requirements. Integration times will vary based on your use case. 
{% endalert %}

## Discovery and planning {#discovery}

During this phase, you will work with your team to scope onboarding tasks and ensure all stakeholders are aligned on a common goal. 

Your team will perform end-to-end planning of your use cases to make sure everything can be built as expected, with the correct data available to do so. This phase includes your project lead, CRM lead, front and back-end engineering, product owners, and marketers. 

The discovery and planning phase takes, on average, about six weeks. Engineering leads can expect to spend 2-4 hours a week during this phase. Developers working with the product can expect to spend 10-20 hours a week on Braze during the discovery and planning phase. 

{% alert tip %}
During your company's onboarding period, Braze will host technical overview sessions. We strongly recommend that engineers attend these sessions. Technical overview sessions provide you an opportunity to have conversations about the scalability of the platform architecture and see practical examples of how companies of your size have previously been successful with similar use cases.
{% endalert %}

![Icons for different channels, such as email, shopping cart, images, geolocation, and so on.]({% image_buster /assets/img/getting-started/data-graphic-2.png %}){: style="max-width:40%;float:right;margin-left:15px;"} 

### Campaign planning

Your CRM team will plan out the messaging use cases that you'll launch in the near future. This includes the:
* [Channel]({{site.baseurl}}/user_guide/message_building_by_channel) (for example, push notifications or in-app messages)
* [Delivery method]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types) (for example, scheduled delivery or action-based delivery)
* [Target audience]({{site.baseurl}}/user_guide/engagement_tools/segments)
* [Success metrics]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)

For example, a new customer campaign might be: an email sent daily at 10 am to a segment of customers who logged their first session yesterday. The conversion event (the success metric) is logging a session.

<br>
{% alert important %}
Integration cannot begin until the campaign planning step is complete. This step will determine what parts and pieces of Braze need to be configured during the integration phase.
{% endalert %}

### Creating data requirements

Then, your CRM team should define what data is required to launch the campaigns they have planned, creating data requirements. 

Many common types of user attributes, such as name, email, date of birth, country, and similar are automatically tracked after the Braze SDK is integrated. Other types of data will need to be defined as custom data.

As a developer, you'll work with your team to define what additional, custom data makes sense to track. Your custom data will impact how your user base will be classified and segmented. You will set up an event taxonomy across your growth stack, structuring your data so that it is compatible with your systems as it moves in and out of Braze.

{% alert tip %}
Keep data nomenclature consistent across tools. For example, your data warehouse may record "purchase limited time offer" in a particular way. You will need to decide if a custom event in Braze is needed to match this format.
{% endalert %}

Learn more about [automatically collected data and custom data]({{site.baseurl}}/developer_guide/analytics/).

### Customizations planning

Talk to your marketers about their desired customizations. For example, do you want to implement the default Braze Content Cards? Do you want to slightly tweak their look and feel to match your brand guidelines? Do you want to develop an entirely new UI for a component and have Braze track its analytics? Different levels of customization require different levels of scope.

### Getting dashboard access

The Braze dashboard is our web UI interface. Marketers will use the dashboard to do their job and create content. Developers use the dashboard to manage settings for integrating apps, such as API keys and push notification credentials.

Your team administrator should add you (and all other team members who need access to Braze) as users on your dashboard.

### Workspaces and API keys

Your team administrator will also create different [workspaces]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/). Workspaces group your data—users, segments, API keys—into one location. As a best practice, we suggest only putting different versions of the same or very similar apps together under one workspace. 

Importantly, workspaces provide API keys for multiple platforms (such as iOS and Android). You'll use the correlated API keys to associate SDK data with a particular workspace. Navigate to your workspaces to access the API key for each of your apps. Make sure each API key has the correct permissions to perform the work you've scoped. See the [API provisioning article]({{site.baseurl}}/api/basics/#rest-api-key) for details.

{% alert important %}
It's important that you set up different environments for development and production. Setting up a test environment will prevent you from spending actual money during onboarding and QA. To create a testing environment, set up a testing workspace and be sure to use its API key so that you aren't populating your production workspace with test data.
{% endalert %}  

## Integration {#integration}

![Abstract pyramid graphic representing the flow of information from a data source to a user device.]({% image_buster /assets/img/getting-started/data-graphic.png %}){: style="max-width:45%;float:right;margin-left:15px;"} 

Braze supports iOS apps, Android apps, web apps, and more. You can also opt to use a cross-platform wrapper SDK, like React Native or Unity. We typically see customers integrate in anywhere from 1-6 weeks. Many customers have integrated Braze with just one engineer, depending on their breadth of technical skills and bandwidth. It's entirely dependent on your specific integration scope and how much time your team dedicates to the Braze project. 

You'll need developers who are familiar with:
* Working in your app or site's native layer
* Creating processes to hit our REST API
* Integration testing 
* JSON web token authentication
* General data management skills
* Settings up DNS records

### CDP integration partners

Many customers use Braze onboarding as an opportunity to also integrate with a customer data platform (CDP) as an integration partner. Braze provides data tracking and analytics, while a CDP can provide additional data routing and orchestration. Braze offers seamless integration with many CDPs, such as [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle/) and [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment/). 

If you are performing side-by-side integration with a CDP, you will map the calls from your CDP's SDK to the Braze SDK. Essentially, you will:
* Map identifying calls to `changeUser` ([Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)/), [web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)) and set attributes.
* Map data flush calls to `requestImmediateDataFlush` ([Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-immediate-data-flush.html?query=abstract%20fun%20requestImmediateDataFlush()), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/requestimmediatedataflush()), [web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestimmediatedataflush)).
* Log custom events or purchases.

Example integrations between the Braze SDK and your CDP of choice might be available, depending on which platform you've chosen. See our [list of CDP technology partners]({{site.baseurl}}/partners/data_and_analytics/) for more information. 

### Braze SDK integration

The Braze SDK provides two critical pieces of functionality: it collects and syncs user data into a consolidated user profile, and powers messaging channels such as push notifications, in-app messages, and Content Cards. 

{% alert tip %} 
When fully integrated with your app or site, the Braze SDK offers a completely-realized level of marketing sophistication. If you defer integrating the Braze SDK, some of the functionality described in the documentation will not be available.
{% endalert %}

During SDK implementation, you will:

* Write SDK integration code for each platform you want to support.
* Activate the messaging channels for each platform, ensuring that the Braze SDK tracks the data from your interactions with your customers across email, SMS, push notifications, and other channels.
* Create any planned UI component customizations (for example, custom Content Cards). For completely custom content, you will need to log analytics since the SDK's automatic data collection won't be aware of your new components. You can pattern this implementation on our default components.

### Using the Braze API

You will use our REST API for different tasks at different points throughout your time using Braze. The Braze API is useful for:

1. Importing historical data; and
2. Continuous updates that aren’t triggered in Braze. For example, a user profile upgrades to VIP without them logging into an app, so the API needs to communicate this info to Braze.

Get started with the [Braze API]({{site.baseurl}}/api/basics).

{% alert important %}
While using the API, ensure you batch your requests and only send delta values. Braze re-writes every attribute that is sent. Do not update any custom attribute if its value has not changed.
{% endalert %}

### Setting up product analytics

Braze is all about data. Data in Braze is stored on the user profile. 

Data points are a structure by which you ensure you're capturing the right data for your marketers, not just "any" data you can possibly vacuum up. Familiarize yourself with [data points]({{site.baseurl}}/user_guide/data/data_points/).

### Migrating legacy user data

You can use the Braze [`/users/track endpoint`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to migrate historical data that was recorded outside of Braze. Examples of commonly imported data include push tokens and past purchases. This endpoint can be used for one-off imports or regular batch updates. 

You can also import users and update customer attribute values through a one-time [CSV upload]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#importing-a-csv) to the dashboard. Uploading CSVs can be helpful for marketers, while our REST API allows for greater flexibility.

### Setting up session tracking

The Braze SDK generates "open session" and "close session" data points. The Braze SDK also flushes data at regular intervals. Refer to these links for session tracking default values, all of which can be customized ([Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web)).

### Tracking custom events, attributes, and purchase events

Coordinate with your team to set up your planned data schema, including custom events, user attributes, and purchase events. Your [custom data scheme]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) will be entered using the dashboard and must match exactly what you implement during SDK integration.

{% alert tip %}
User IDs, called `external_id`s in Braze, should be set for all known users. These should be unchanging and accessible when a user opens the app, allowing you to track your users across devices and platforms. See the [User lifecycle]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) article for best practices.
{% endalert %}

### Other tools

Based on your use case, there may be other tools you need to set up. For example, you might need to configure a tool like [geofences]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences/) to realize your user stories. We have found that customers who have the ability to set up these additional tools after completing the essential integration steps are most successful.

## Quality assurance {#qa}
As you execute your integration, you'll provide quality assurance to make sure everything you're setting up is working as expected. This QA falls into two general categories: data ingestion and message channels.

{% alert important %}
Make sure your production and testing environments are set up before beginning QA.
{% endalert %}

| **QA data ingestion**  | **QA messaging**                                              |
|---------------------------|---------------------------------------------------------------|
| You'll perform quality assurance on the way data is ingested, stored, and exported. | You'll make sure that your messages are being sent correctly to your users and everything looks excellent. |
| Run tests to confirm data is stored properly. | Create segments of users. |
| Confirm session data is correctly attributed to the intended workspace within Braze. | Launch campaigns and Canvases successfully. |
| Confirm session starts and ends are being recorded. | Confirm the correct campaigns are being shown to the correct user segments. |
| Confirm user attribute information is correctly recorded against user profiles. | Confirm that push tokens are correctly being registered. |
| Test that custom data is being correctly recorded against user profiles. | Confirm that push tokens are correctly removed. |
| Create anonymous user profiles. | Test that push campaigns are correctly sending to devices and engagement is logged. |
| Confirm that anonymous user profiles become known user profiles when the `changeUser()` method is called. | Test that in-app messages are delivered and metrics logged. |
|                           | Test that Content Cards are delivered and metrics logged. |
|                           | Facilitate Connected Content (for example, AccuWeather). |
|                           | Confirm all message channel integrations are working together properly. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
While performing QA on your SDK integration, use the [SDK Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging) to get troubleshoot issues without turning on verbose logging for your app.
{% endalert %}

### Passing Braze off to marketers

Once you have integrated your platform or site, you will want to involve your Marketing team to pass ownership of the platform to them. This process looks different at every company, but might include the following:

* Composing complex [Liquid logic]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid#about-liquid)
* Help facilitating [email IP warming]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)
* Making sure other stakeholders understand the kind of data being tracked

### Develop for the future

Have you ever inherited a codebase and had no clue what the initial developer was thinking? Worse, have you ever written code, understood it completely, and then felt completely baffled when you came back to it a year later? 

When onboarding Braze, the collective decisions you make concerning data, user profiles, what integrations were and were not in scope, how customizations are supposed to work, and more, will feel fresh in your mind and therefore obvious. When your team wants to expand Braze or when other technical resources are assigned to your Braze project, this information will be obscure.

Create a resource to cement the information you learned during your technical overview sessions. This resource will help reduce the time to onboard new developers who join your team (or serve as a reminder to yourself when you need to expand your current Braze implementation). 

## Maintenance {#maintenance}

After handoff to your marketers, you will continue to serve as a resource for maintenance. You will pay attention to iOS and Android updates that might impact the Braze SDK and make sure that your third-party vendors are up to date. 

You will track updates to the Braze platform via the Braze [GitHub](https://github.com/braze-inc/). Occasionally, your administrator will receive emails about urgent updates and bug fixes directly from Braze, as well. 

## SDK rate limits 

### Monthly Active Users CY 24-25 

For customers who have purchased Monthly Active Users - CY 24-25, Braze enforces server-side rate limits on API requests used by our SDKs to update sessions, user attributes, events, and other user profile data. This is to ensure platform stability and to maintain fast, reliable service. 

* Hourly rate limits are set according to the expected SDK traffic on your account, which may correspond to the number of monthly active users (MAU) you have purchased, industry, seasonality, or other factors. When the hourly rate limit is reached, Braze will throttle requests until the next hour.
* All rate limited requests are automatically retried by the SDK.
* SDK requests correlate with the amount of custom data collected in your implementation. If you're consistently near or at your hourly rate limit, consider:
    * Reviewing your SDK integration to reduce excessive data collection.
    * Blocklisting custom data that isn't essential for your marketing use cases.
* Burst rate limits are short-lived rate limits that apply when a high volume of requests arrive in a very short period (that is, within seconds). You don't need to take action when burst limits occur, and the SDK will retry shortly after.

### Finding your rate limits

To find current limits based on expected SDK throughput, go to **Settings** > **APIs and Identifiers** > **API and SDK limits**.

For historical usage, go to **Settings** > **APIs and Identifiers** > **API and SDK dashboard**.

### Changes and support

Braze may modify rate limits to protect system stability or allow for increased data throughput on your account. Contact Braze Support or your customer success manager for questions or concerns regarding rate limits and how they impact your business.
