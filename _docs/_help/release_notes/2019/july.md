---
nav_title: July
page_order: 6
noindex: true
page_type: update
description: "This article contains release notes for July 2019."
---

# July 2019

{% alert update %}
Braze had two (you read that right - **two**) product release cycles this month! The latest release is noted at the top, the earlier one [starts further down this page](#earlier-this-month)!
{% endalert %}

## SAML/SSO

[Single sign-on]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/) (SSO) provides companies a secure and centralized way of controlling access to the Braze dashboard. In short, a single set of credentials can be use to access different applications, including Braze.

In addition to [Google Sign-In using OAuth 2.0 support](https://developers.google.com/identity/protocols/OAuth2), companies would like SSO with Security Assertion Markup Language (SAML) support. This enables them to seamlessly integrate with large identity providers (IdPs), including [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/) and [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/), which support the latest industry standards (SAML 2.0).

Braze supports:
- [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)
- [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
- [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)

## Adjust event API key shows

We have updated Adjust's partner page to make this API key accessible to customers.

## New Partners

Some new partners have joined our Alloys program and have been added to our Docs! Say hello to:
- [FiveTran]({{site.baseurl}}/partners/fivetran/)
- [Talon.One]({{site.baseurl}}/partners/talonone/)
- [Voucherify]({{site.baseurl}}/partners/voucherify/)

## Campaign details improvement

Expanded campaign details are now shown in the ...wait for it...**Campaign Details** section of the **Campaign** Page!

## Show only mine in segments & Canvas

The "Only Show Mine" check filter on the **Campaigns** page has proven to be wildly popular. As a result, we're also adding this option to the Canvas and Segment lists!

### Advancement behavior

You can now choose [when a user advances]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) from one Canvas step to the next. These options include "Message Sent" and "Entire Audience After Delay".

### In-app messages in Canvas

[In-app messages]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) are now available in Canvas! Add a Canvas step and browse the available channels to add an in-app message.

# Earlier this month

## User profile image removal

We are removing the user profile pictures displayed in Braze user profiles and user searches.

## Connected Content in Content Cards

You can now use [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) strings and functionality in [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/).

Connected Content calls to external servers will happen when a Card is actually sent, not when the Card is viewed by the User. Similar to Email, dynamic content will be calculated and determined at sending time, rather than when a Card is actually viewed.

## Null "reply-to" address

Customers can now set a `null` value for an email message's "reply-to" address from the **Email Settings** page in Braze or using the [API]({{site.baseurl}}/api/endpoints/messaging/#email-object-specification).  When used, replies will be sent to the listed "From" address.  You can now personalize the "From" address field as `dan@emailaddress.com`, and your customers will have the ability to reply directly back to Dan.

To set a `null` value for an email message's "reply-to-" address from Braze, go to **Manage Settings** in the navigation, then the **Email Settings** tab. Scroll to the **Outbound Email Settings** section, and select **Exclude "Reply-To" and send replies to "From"** as the default address.

## Campaign comparisons

Look at [multiple campaigns at one time to compare their relative performance]({{site.baseurl}}/report_builder/), side-by-side in Braze - in one window!

## Template dispatch ID into messages with Liquid

{% alert note %}
Behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for entry steps, which can be scheduled) as triggered events, even when they are "scheduled". Learn more about [`dispatch_id` behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/) in Canvases and campaigns.
{% endalert %}

If you want to track the dispatch of a message from within the message (in a URL, for example), you can template in the `dispatch_id`. You can find the formatting for this in our list of supported personalization tags, under [Canvas Attributes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

This behaves just like `api_id`, in that since the `api_id` isn't available at campaign creation, it is templated in as a placeholder and will preview as `dispatch_id_for_unsent_campaign`. The ID is generated before the message is sent, and will be included in as send time.

{% alert warning %}
Liquid templating of `dispatch_id_for_unsent_campaign` does not work with in-app messages, since in-app messages don't have a `dispatch_id`.
{% endalert %}

## "Show Only Mine" setting persists

The "Show Only Mine" filter on the campaign grid will remain on any time you visit the **Campaigns** page.

## A/B testing updates

You can send a one-time [A/B test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) with up to eight variants (and optional control) to a user-specified percentage of a campaign's audience, and then send the best variant to the remaining audience at a pre-scheduled time.
