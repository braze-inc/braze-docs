---
nav_title: Most Recent
page_order: 0
---

# Most Recent Braze Release Notes

_Braze releases information on it’s product updates on a monthly cadence. For more information on any of the updates listed in this section, reach out to your account manager or to [open a support ticket][support]. You can also check out [our SDK Changelogs]({{ site.baseurl }}/developer_guide/platform_integration_guides/sdk_changelogs/) to see more information on our monthly releases, updates, and improvements._


## September 2019

{% alert update %}
New September updates!
{% endalert %}

### Braze App within OneLogin

Customers will be able to simply search and select Braze within [OneLogin]({{ site.baseurl }}/user_guide/administrative/access_braze/single_sign_on/onelogin/) for SP or IdP Initiated login. This means that customers will not have to add a custom application within OneLogin. As a result, this should pre-populate certain settings like attributes which we have seen come up since launching SAML SSO.

### Rokt Calendar Partnership

[Rokt Calendar]({{ site.baseurl }}/partners/technology_partners/channel_extensions/calendar/rokt_calendar) provides Braze customers the ability to align their personalized marketing initiatives and extend personalized content to the end user's calendar. Thus, making it a more seamless experience for the end user and further develops stickiness with our customers' services. Customers will be able to...

- Send a calendar invite via Braze platform to 'save the date' and extend our communication
- Update an existing invite if the contents of the event has changed.

### Passkit Partnership

With [Passkit]({{ site.baseurl }}/partners/technology_partners/additional_channels/mobile_wallet/passkit/), Braze customers will be able to expand their customer engagement to mobile wallet. They will be able to personalized wallet campaigns while using Braze's powerful segmentation and orchestrate alongside channels like push, in-app messages, and more.

### Dispatch ID Value Return via Messaging Endpoints

A message's `dispatch_id` will be included in the following Messaging endpoint responses:

- [`/campaigns/trigger/send`]({{ site.baseurl }}/api/endpoints/messaging/#sending-messages-via-api-triggered-delivery)
- [`/campaigns/trigger/schedule`]({{ site.baseurl }}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/messages/send`]({{ site.baseurl }}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/messages/schedule`]({{ site.baseurl }}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/canvases/trigger/send`]({{ site.baseurl }}/api/endpoints/messaging/#canvas)
- [`/canvases/trigger/schedule`]({{ site.baseurl }}/api/endpoints/messaging/#api-triggered-canvases)

This way, customers who use transactional messaging can trace the call back through Currents.

### Canvas Changelogs

Did you even wonder more about the details of who is working on a Canvas in your account? Wonder no more! You can now access Canvas Changelogs.

![Canvas Changelogs]({% image_buster /assets/img/canvas-changelogs.gif %})


## August 2019

### Campaign Details in Reports

Your Campaign performance report will now list your campaign's details so you don't have to go back through your campaign to see which Delivery, Audience, or Conversion settings you chose while setting up your report.

![Campaign Details]({% image_buster /assets/img/campaign_details_update.png %})

### New Email Content Block API Endpoints

You can now manage ([create]({{ site.baseurl }}/api/endpoints/email_templates/#create-content-block), [list available]({{ site.baseurl }}/api/endpoints/email_templates/#list-available-content-blocks), [get information]({{ site.baseurl }}/api/endpoints/email_templates/#see-content-block-information)) your Email Content Blocks via API!

{% alert update %}
This feature is temporarily in limited availability. Please reach out to your Braze account manager for more information.
{% endalert %}

### Custom Email Unsubscribe Landing Page Update

The default [custom Email Unsubscribe page]({{ site.baseurl }}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-unsubscribe-landing-page) has been updated with a sleek, more modern look.

### iOS SDK - Notched Phone Support Improvement

Improved support for in-app messages on “notched” devices (for example, iPhone X, Pixel 3XL). Full-screen messages now expand to fill the entire screen of any phone, while covering the status bar.

You won't see many updates in the Docs reflecting this change just yet - but they're on the way!


## July 2019

{% alert update %}
Braze had two (you read that right - **two**) product release cycles this month! The latest release is noted at the top, the earlier one [starts further down this page](#earlier-this-month)!
{% endalert %}

### SAML/SSO

[Single Sign On (SSO)]({{ site.baseurl }}/user_guide/administrative/access_braze/single_sign_on/) provides companies a secure and centralized way of controlling access to the Braze dashboard. In short, a single set of credentials can be use to access different applications, including Braze.

In addition to [Google Sign-In using OAuth 2.0 support](https://developers.google.com/identity/protocols/OAuth2), companies would like SSO with Security Assertion Markup Language (SAML) support. This enables them to seamlessly integrate with large identity providers (IdPs), including [Azure Active Directory]({{ site.baseurl }}/user_guide/administrative/access_braze/single_sign_on/azure_ad/) and [Okta]({{ site.baseurl }}/user_guide/administrative/access_braze/single_sign_on/okta/), which support the latest industry standards (SAML 2.0).

Braze supports:
- [OneLogin]({{ site.baseurl }}/user_guide/administrative/access_braze/single_sign_on/onelogin/)
- [Azure Active Directory]({{ site.baseurl }}/user_guide/administrative/access_braze/single_sign_on/azure_ad/)
- [Okta]({{ site.baseurl }}/user_guide/administrative/access_braze/single_sign_on/okta/)

### Adjust Event API Key Shows

We have updated Adjust's partner page to make this API key accessible to customers.

![Adjust API Key]({% image_buster /assets/img/adjust_eventapikey.png %})

### New Partners

Some new partners have joined our Alloys program and have been added to our Docs! Say hello to...
- [FiveTran]({{ site.baseurl }}/partners/fivetran/)
- [Talon.One]({{ site.baseurl }}/partners/talonone/)
- [Voucherify]({{ site.baseurl }}/partners/voucherify/)

### Campaign Details Improvement

Expanded Campaign details are now shown in the ... wait for it ... Campaign Details section of the Campaign Page!

![Campaign Details]({% image_buster /assets/img/campaign_details.png %})

### Show Only Mine in Segments & Canvas

The "Only Show Mine" check filter on the Campaigns page has proven to be wildly popular! As a result, we're also adding this option to the Canvas and Segment lists!

### Advancement Behavior
You can now choose [when a user advances]({{ site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) from one Canvas step to the next - options are "Message Sent" and "Entire Audience After Delay".

![Advancement Behavior]({% image_buster /assets/img/advancement_behavior_rn.png %})

### In-App Messages in Canvas

[In-app messages are now available to use with Canvas!]({{ site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/) Add a Canvas step and browse available channels to add an in-app message.

![In-App Messages in Canvas]({% image_buster /assets/img/iam-in-canvas.png %})

## Earlier This Month
---

### User Profile Image Removal

We are removing the user profile pictures displayed in Braze User Profiles and User Searches.

### Connected Content in Content Cards

You can now use [Connected Content]({{ site.baseurl }}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) strings and functionality in [Content Cards]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/overview/).

Connected Content calls to external servers will happen when a Card is actually sent, __not__ when the Card is viewed by the User. Similar to Email, dynamic content will be calculated and determined at sending time, rather than when a Card is actually viewed.

### Null 'Reply-To' Address

Customers can now set a `null` value for an email messages's "Reply-To" address from the Email Settings page in Braze or using [the API]({{ site.baseurl }}/api/endpoints/messaging/#email-object-specification).  When used, replies will be sent to the listed "From" address.  You can now personalize the "From" address field as `dan@emailaddress.com` and your customers will have the ability to reply directly back to Dan.

To set a `null` value for an email messages's "Reply-To" address from Braze, go to `Manage App Group` in the navigation, then the `Email Settings` tab. Scroll to the `Outbound Email Settings` section, and select `Exclude “Reply-To” and send replies to “From”` as the default address.

![Email Settings Reply-To]({% image_buster /assets/img/null_reply-to.png %})

### Campaign Comparisons

Look at [multiple campaigns at one time to compare their relative performance]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/comparing_campaigns/), side-by-side in Braze - in one window!

### Template Dispatch ID into Messages with Liquid

{% alert update %}
Behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{ site.baseurl }}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

If you want to track the dispatch of a message from within the message (in a URL, for example), you can template in the `dispatch_id`. You can find the formatting for this in our list of Supported Personalization Tags, under [Canvas Attributes]({{ site.baseurl }}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

This behaves just like `api_id`, in that since the `api_id` isn't available at Campaign creation, it is templated in as a placeholder and will preview as `dispatch_id_for_unsent_campaign`. The id is generated before the message is sent, and will be included in as send time.

{% alert warning %}
Liquid templating of `dispatch_id_for_unsent_campaign` does not work with in-app messages, since in-app messages don't have a `dispatch_id`.
{% endalert %}

### "Show Only Mine" Setting Persists

The "Show Only Mine" filter on the Campaign grid will remain "on" any time you visit the Campaigns page.

### A/B Testing Updates

You can send a one-time [A/B test]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/) with up to eight variants (and optional control) to a user-specified percentage of a Campaign's audience, and then send the best variant to the remaining audience at a pre-scheduled time.





[support]: {{ site.baseurl }}/support_contact/
[CCFeed]: {% image_buster /assets/img/cc-feed.png %}
[cbm]: {% image_buster /assets/img/created_by_me2.png %}
[plat_p]: {% image_buster /assets/img/iam_platforms.gif %}
