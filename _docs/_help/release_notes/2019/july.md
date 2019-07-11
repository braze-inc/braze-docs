---
nav_title: July
page_order: 6
---

# July 2019

## User Profile Image Removal

We are removing the user profile pictures displayed in Braze User Profiles and User Searches.

## Connected Content in Content Cards

You can now use [Connected Content]({{ site.baseurl }}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) strings and functionality in [Content Cards]({{ site.baseurl }}/user_guide/message_building_by_channel/content_cards/overview/).

Connected Content calls to external servers will happen when a Card is actually sent, __not__ when the Card is viewed by the User. Similar to Email, dynamic content will be calculated and determined at sending time, rather than when a Card is actually viewed.

## Null 'Reply-To' Address

Customers can now set a `null` value for an email messages's "Reply-To" address from the Email Settings page in Braze or using [the API]({{ site.baseurl }}/api/endpoints/messaging/#email-object-specification).  When used, replies will be sent to the listed "From" address.  You can now personalize the "From" address field as `dan@emailaddress.com` and your customers will have the ability to reply directly back to Dan.

To set a `null` value for an email messages's "Reply-To" address from Braze, go to `Manage App Group` in the navigation, then the `Email Settings` tab. Scroll to the `Outbound Email Settings` section, and select `Exclude “Reply-To” and send replies to “From”` as the default address.

![Email Settings Reply-To]({% image_buster /assets/img/null_reply-to.png %})

## Campaign Comparisons

Look at [multiple campaigns at one time to compare their relative performance]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/comparing_campaigns/), side-by-side in Braze - in one window!

## Template Dispatch ID into Messages with Liquid

If you want to track the dispatch of a message from within the message (in a URL, for example), you can template in the `dispatch_id`. You can find the formatting for this in our list of Supported Personalization Tags, under [Canvas Attributes]({{ site.baseurl }}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

This behaves just like `api_id`, in that since the `api_id` isn't available at Campaign creation, it is templated in as a placeholder and will preview as `dispatch_id_for_unsent_campaign`. The id is generated before the message is sent, and will be included in as send time.

{% alert warning %}
Liquid templating of `dispatch_id_for_unsent_campaign` does not work with in-app messages, since in-app messages don't have a `dispatch_id`.
{% endalert %}

## "Show Only Mine" Setting Persists

The "Show Only Mine" filter on the Campaign grid will remain "on" any time you visit the Campaigns page.

## A/B Testing Updates

You can send a one-time [A/B test]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/) with up to eight variants (and optional control) to a user-specified percentage of a Campaign's audience, and then send the best variant to the remaining audience at a pre-scheduled time.
