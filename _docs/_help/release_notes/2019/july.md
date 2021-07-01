---
nav_title: July
page_order: 6
no_index: true
page_type: update
description: "This article contains release notes for July 2019."
---

# July 2019

{% alert update %}
Braze had two (you read that right - **two**) product release cycles this month! The latest release is noted at the top, the earlier one [starts further down this page](#earlier-this-month)!
{% endalert %}

## SAML/SSO

[Single Sign On (SSO)]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/) provides companies a secure and centralized way of controlling access to the Braze dashboard. In short, a single set of credentials can be use to access different applications, including Braze.

In addition to [Google Sign-In using OAuth 2.0 support](https://developers.google.com/identity/protocols/OAuth2), companies would like SSO with Security Assertion Markup Language (SAML) support. This enables them to seamlessly integrate with large identity providers (IdPs), including [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/azure_ad/) and [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/), which support the latest industry standards (SAML 2.0).

Braze supports:
- [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)
- [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/azure_ad/)
- [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)

## Adjust Event API Key Shows

We have updated Adjust's partner page to make this API key accessible to customers.

![Adjust API Key]({% image_buster /assets/img/adjust_eventapikey.png %})

## New Partners

Some new partners have joined our Alloys program and have been added to our Docs! Say hello to...
- [FiveTran]({{site.baseurl}}/partners/fivetran/)
- [Talon.One]({{site.baseurl}}/partners/talonone/)
- [Voucherify]({{site.baseurl}}/partners/voucherify/)

## Campaign Details Improvement

Expanded Campaign details are now shown in the ... wait for it ... Campaign Details section of the Campaign Page!

![Campaign Details]({% image_buster /assets/img/campaign_details.png %})

## Show Only Mine in Segments & Canvas

The "Only Show Mine" check filter on the Campaigns page has proven to be wildly popular! As a result, we're also adding this option to the Canvas and Segment lists!

### Advancement Behavior
You can now choose [when a user advances]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) from one Canvas step to the next - options are "Message Sent" and "Entire Audience After Delay".

![Advancement Behavior]({% image_buster /assets/img/advancement_behavior_rn.png %})

### In-App Messages in Canvas

[In-app messages are now available to use with Canvas!]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/) Add a Canvas step and browse available channels to add an in-app message.

![In-App Messages in Canvas]({% image_buster /assets/img/iam-in-canvas.png %})

# Earlier This Month
---

## User Profile Image Removal

We are removing the user profile pictures displayed in Braze User Profiles and User Searches.

## Connected Content in Content Cards

You can now use [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) strings and functionality in [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/).

Connected Content calls to external servers will happen when a Card is actually sent, __not__ when the Card is viewed by the User. Similar to Email, dynamic content will be calculated and determined at sending time, rather than when a Card is actually viewed.

## Null 'Reply-To' Address

Customers can now set a `null` value for an email messages's "Reply-To" address from the Email Settings page in Braze or using [the API]({{site.baseurl}}/api/endpoints/messaging/#email-object-specification).  When used, replies will be sent to the listed "From" address.  You can now personalize the "From" address field as `dan@emailaddress.com` and your customers will have the ability to reply directly back to Dan.

To set a `null` value for an email messages's "Reply-To" address from Braze, go to `Manage Settings` in the navigation, then the `Email Settings` tab. Scroll to the `Outbound Email Settings` section, and select `Exclude “Reply-To” and send replies to “From”` as the default address.

![Email Settings Reply-To]({% image_buster /assets/img/null_reply-to.png %})

## Campaign Comparisons

Look at [multiple campaigns at one time to compare their relative performance]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/comparing_campaigns/), side-by-side in Braze - in one window!

## Template Dispatch ID into Messages with Liquid

{% alert update %}
Behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

If you want to track the dispatch of a message from within the message (in a URL, for example), you can template in the `dispatch_id`. You can find the formatting for this in our list of Supported Personalization Tags, under [Canvas Attributes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

This behaves just like `api_id`, in that since the `api_id` isn't available at Campaign creation, it is templated in as a placeholder and will preview as `dispatch_id_for_unsent_campaign`. The id is generated before the message is sent, and will be included in as send time.

{% alert warning %}
Liquid templating of `dispatch_id_for_unsent_campaign` does not work with in-app messages, since in-app messages don't have a `dispatch_id`.
{% endalert %}

## "Show Only Mine" Setting Persists

The "Show Only Mine" filter on the Campaign grid will remain "on" any time you visit the Campaigns page.

## A/B Testing Updates

You can send a one-time [A/B test]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/) with up to eight variants (and optional control) to a user-specified percentage of a Campaign's audience, and then send the best variant to the remaining audience at a pre-scheduled time.
