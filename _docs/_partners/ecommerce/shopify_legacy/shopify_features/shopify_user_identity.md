---
nav_title: Shopify User Identity Management
article_title: "Shopify User Identity Management"
description: "This reference article outlines the Shopify user identity management feature."
page_type: partner
search_tag: Partner
alias: "/shopify_user_identity/"
page_order: 3
---

# Shopify user identity management

> Braze will receive signals from your Shopify customers through their on-site behaviors and by listening to Shopify webhooks that you configured as part of your integration. For non-headless Shopify sites, Braze will assist with reconciling users from the checkout page. For headless Shopify sites, refer to our integration guidance on how to [reconcile users from checkout]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#headless-checkout).

{% multi_lang_include alerts/important_alerts.md alert='Shopify deprecation' %}

## Capturing information for user profiles 

### Shopify user tracking

If your store visitors are guests (that is, anonymous), Braze will capture the `device_id` for those particular customers’ sessions. After you set up user reconciliation for Shopify forms during your [implementation of the Web SDK]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk), customer emails will be added to anonymous user profiles whenever customers enter their information into a form. 

When store visitors enter their email into a Shopify newsletter or email capture form, Braze will receive a Shopify webhook event to create the user profile. Braze then merges this user profile with the anonymous user profile tracked by the Web SDK and assigns the Shopify customer ID as the user alias on the user profile. 

As customers progress to checkout and provide other identifiable information, like phone numbers, Braze must capture the relevant user data from Shopify webhooks and merge it with the anonymous user with the `device_id`.
- If you implemented the Web SDK via Shopify ScriptTag, on a non-headless Shopify site, or via Google Tag Manager, Braze will automatically ensure that the user data from the checkout page and the session data from the anonymous user profile are merged to the user alias profile with the assigned Shopify customer ID.
- If you have implemented the Web SDK on a Shopify headless site, you must ensure that user data submitted within the checkout page is appropriately assigned to the correct user profile through either the Web SDK or API. For more information, check out [Implementing the Web SDK directly onto your headless Shopify site]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#headless-site).

As customers continue the checkout process, Braze checks if their entered email address, phone number, or Shopify customer ID matches an existing user profile. If there is a match, Braze syncs the Shopify user data to that profile.

If the email address or phone number is associated with multiple identified user profiles, Braze syncs the Shopify data to the profile with the most recent activity.

If Braze does not find a match for the email address or phone number, Braze creates a new user profile with the supported Shopify data.

### When Shopify customers sync with Braze

Braze updates existing user profiles or creates new ones for leads, sign-ups, and account registrations captured in your Shopify store. You can collect user profile data from the following methods in Shopify and more:
- Customer creates an account
- Customer email address or phone number is collected in a Shopify capture form
- Customer email address is collected from a newsletter form
- Customer email address or phone number is collected through a third-party tool that is connected to Shopify, such as EcomSend

Braze will first attempt to map the supported Shopify data to any existing user profiles using the customer’s email address or phone number. 

To prevent duplicate user profiles, it is critical you review the user reconciliation for Shopify Forms instructions for the method you used to [implement the Web SDK on your Shopify website]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk).

## User profile merging 

{% alert note %}
The default Shopify integration provides tooling to assist with merging your anonymous user profile and the Shopify alias profile. If you are implementing the integration to a headless Shopify site, review [Implementing the Web SDK directly onto your headless Shopify site]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=headless%20shopify%20site#supported-features) to confirm you are properly reconciling your users. <br><br> If you encounter duplicate user profiles, you can use our [bulk merging tool]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging/) to help streamline your data.
{% endalert %}

Braze merges the fields from the anonymous user profile to the identified user profile when we find a match with one of the following:
- Shopify customer ID
- Email
- Phone number

Braze merges the following fields from the anonymous user profile to the identified user profile:
- First name
- Last name
- Email
- Gender
- Date of birth
- Phone number
- Time zone
- Home city
- Country
- Language
- Custom attributes
    - Custom event and purchase event data (excluding event properties, count, and first date and last date timestamps)
    - Custom event and purchase event properties for “X times in Y days” segmentation (where X<=50 and Y<=30)
- Push tokens
- Message history
- Any of the following fields found on the anonymous user profile or the identified user profile, such as custom event, purchase event count, and first date and last date timestamps
    - These merged fields will update “for X events in Y days” filters. For purchase events, these filters include “number of purchases in Y days” and “money spent in last Y days”.

{% alert important %}
Session data is not yet supported as part of the merging process.
{% endalert %}

## Syncing Shopify subscribers

During the Shopify setup process, Braze provides flexible controls to sync your customer email addresses and SMS opt-in states to the subscription groups and subscription states on Braze user profiles. 

### Collecting email or SMS subscribers

During your setup of the Shopify store in Braze, you will have the option to sync your email and SMS subscribers from Shopify into Braze. 

#### Collect email subscribers

To enable email subscriber collection, turn on the feature within your Shopify setup. We recommend that you assign at least one Braze [subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups), such as Shopify email subscribers. Braze will add your email subscribers to the specified subscription groups so that they are included in your audience targeting when you send a message. 

![]({% image_buster /assets/img/Shopify/collect_email.png %})

When enabled, Braze will sync updates to your Shopify email subscribers and updates to their email subscription states in real-time. If you don't enable the override option, your Shopify customers will either be subscribed or unsubscribed from the subscription group associated with your Shopify store.

If you enable the override option, Braze will update the global subscription state on the user profile. This means that if your customers are marked as unsubscribed in Shopify, Braze will mark the global subscription state as unsubscribed on the user profile and unsubscribe the customer from all available email subscription groups. As a result, no messages will be sent to users who were globally unsubscribed from email.

#### Collect SMS subscribers

To collect SMS subscribers from Shopify, you must create [SMS subscription groups]({{site.baseurl}}/sms_rcs_subscription_groups/) as part of your [SMS setup]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/sms_setup/sms_sending/). 

When you are ready to collect your Shopify SMS subscribers, enable SMS subscriber collection by turning it on within the Shopify setup page. You must select at least one SMS subscription group so that you can appropriately target and send SMS messages. 

![]({% image_buster /assets/img/Shopify/collect_sms.png %})

When enabled, Braze will sync updates to your Shopify SMS subscribers and their SMS subscription states in real-time. If you don't enable the override option, your Shopify customers will either be subscribed or unsubscribed from the subscription group associated with your Shopify store.

SMS subscribers don't have global subscription states, so you don't need to consider them when using an override option. A user can only be unsubscribed or subscribed to an SMS subscription group.

#### Legacy custom attributes

Legacy Shopify customers may have the old method of collecting email and SMS subscribers via the `shopify_accepts_marketing` and `shopify_sms_consent` custom attributes. If you save the settings above with override enabled, Braze will remove the custom attributes on the user profiles and sync those values over to their respective email subscription group and SMS subscription group.

If you have existing campaigns or Canvases using these legacy custom attributes, remove those attributes and confirm the campaigns or Canvases are using the appropriate subscription state, group, or both.
