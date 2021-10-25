---
nav_title: Integration
article_title: Onboarding Integration Overview
page_order: 1
page_type: reference
description: "This reference article briefly covers the integration steps required from your engineers or developers."

---

# Integration

Integrating with Braze is a worth-while process. But you're smart. you're __here__. Clearly you already know that!

But what you probably don't know was that you and your engineers or developers are about to go on a journey together that requires technical expertise, strategic planning, and consistent communication that will help you coordinate between the two!

{% alert note %} Please note that this doesn't count for email. Check that out in the [Email Set Up Guide]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/).{% endalert %}

## The technical side of the integration process

You may find yourself thinking "My engineers are magical! They can do anything, so I usually just leave them to it!" And they probably are and probably can! But there's no reason why you shouldn't know what they're doing behind the scenes. In fact, it would help the entire process if you knew when to jump in with information and what to look for when they say "Can you send me the API Key and API Endpoint?".

"So what are they doing when they integrate Braze with my app or site?"

Glad you asked!

### Step 1: They implement the Braze SDK

The Braze SDK (Software Development Kit) is how we send and get information to and from your app or site. Your engineers are, essentially, tying our apps together. To do this, they need a few pieces of key information:

* [The API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/api_settings_tab/)
* [Your Endpoint]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)
  * Braze no longer gives out custom endpoints so please use the [predefined SDK endpoints]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). If you have been given a pre-exisiting custom endpoint, here you can find the set up steps involved for [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-5-optional-custom-endpoint-setup), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/), and [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#initializing-the-sdk) integration.

You can either give this information to them directly, or you can give them access to Braze by creating an account for them.

{% alert warning %}
Please ensure that you and your engineer don't unknowingly or unintentionally change the company's credentials in Braze, as this could cause issues during the implementation process or lock one or more of you out of your accounts.
{% endalert %}

### Step 2: They implement your desired messaging channels

Braze has many options for getting in touch with your customers/users, and each requires its own set up or tweaking to work the way you want. This is where communication with your engineers becomes critical.

Be sure to tell your engineers which channels you want to use to ensure that implementation is done efficiently and in proper order.

| Channel | Details |
|---|---|
| In-App Messages | Requires SDK implementation as well as these channel-specific steps. |
| News Feed | This works upon proper implementation and is SDK required. |
| Push | Requires SDK implementation to provide proper handling around messaging credentials and push tokens. |
| Email | This is an entirely different process. Check that out in [our Email Setup section]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/). |
{: .reset-td-br-1 .reset-td-br-2}

### Step 3: They set up your data

Braze isn't a one-trick pony. This isn't about just sending emails or sending push. This is about creating personalized customer journeys that are unique for every user/customer. The customer journeys are based on their actions within your app or site and you get to define what those are! However, what good is that definition if you can't track, record, compile, and act on them. That's your engineer's next task - ensure that actions taken within your app or site are picked up by Braze.

So, what do you need to do to get them this information?

1. Work with your marketing team to define campaigns, goals, attributes, and events that you need to track. Define those use cases, share them with your teams.
2. Define your Custom Data Requirements (Attributes, Events, etc.).
3. From there, discuss [how that data should be tracked]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) (triggered through the SDK, etc.).
4. Define how many [App Groups]({{site.baseurl}}/user_guide/administrative/app_settings/app_group_management/) you need. They'll need to know how to [test and configure]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/) these.

Once you discover all of this information, share it with your engineer. They'll take that information and implement your [Custom Data]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/pre-populating_custom_data/). You might even need to [import some users]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/). You should also be aware of [event naming conventions]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

### Step 4: They customize based on what you want

If you want things like API-Triggered launching and Connected Content, discuss that with both your Braze contact and your engineers to ensure that you'll be able to get data that lives outside of your app and Braze into your messages.

### Step 5: You both QA your implementation

Work together with your engineer to make sure everything is working. Send [test messages]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_push_notifications/), use our [test apps for Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sample_apps/) and [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/sample_apps/), check every box before you start sending!

We even have specific instructions for [testing your Android or FireOS integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/test_your_basic_integration/#test-your-basic-integration) and testing [push for iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/testing/).

## After implementation

Keep in mind that the Implementation Finish Line isn't also the green light to send a million messages at once! Sending a million push might break your app if every customer clicks the same link at once - we recommend discussing what your capacity of your internal set up is for handling requests from Braze before clicking that _Send_ button. Then, you can set your [rate limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting) based on that.

Now that you're more familiar with the integration process, check out the next article for [suggestions on where to go next]({{site.baseurl}}/user_guide/onboarding_with_braze/learning_to_use_braze/)!

After you're comfortable using Braze, consider becoming a Braze Firebrand! With Braze Firebrands, our customer engagement community, we're building a community of movers and shakers using Braze to modernize their customer experience and marketing. Interested in learning more? [Join now](https://brazefirebrands.splashthat.com/).
