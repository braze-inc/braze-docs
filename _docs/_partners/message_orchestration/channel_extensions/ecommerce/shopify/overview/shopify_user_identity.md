---
nav_title: Shopify User Identity Management
article_title: "Shopify user identity management"
description: "This reference article outlines the Shopify user identity management feature."
page_type: partner
search_tag: Partner
page_order: 3
---

# Shopify user identity management

> Use the Web SDK integration to track sessions for your Shopify customers. 

## Capturing information for user profiles 

### Shopify user tracking

If your store visitors are guests (that is, anonymous), Braze will capture the `device_id` for those particular customers’ sessions. After you set up user reconciliation for Shopify forms during your [implementation of the Web SDK](), customer emails will be added to anonymous user profiles whenever customers enter their information into a form. 

When store visitors enter their email into a newsletter or email capture form, Braze will receive a Shopify webhook event to create the user profile. Braze then merges this user profile with the anonymous user profile tracked by the Web SDK and assigns the Shopify customer ID as the user alias on the user profile. 

As customers progress to checkout and provide other identifiable information, like phone numbers, Braze must capture the relevant user data from Shopify webhooks and merge it with the anonymous user with the `device_id`.
- If you implemented the Web SDK via Shopify ScriptTag, on a non-headless Shopify site, or via Google Tag Manager, Braze will automatically ensure that the user data from the checkout page and the session data from the anonymous user profile are merged to the user alias profile with the assigned Shopify customer ID.
- If you have implemented the Web SDK on a Shopify headless site, you must ensure that user data submitted within the checkout page is appropriately assigned to the correct user profile through either the Web SDK or API. For more information, check out [Implementing the Web SDK directly onto your Shopify site’s `theme.liquid`]().

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

To prevent duplicate user profiles, it is critical you review the user reconciliation for Shopify Forms instructions for the method you used to [implement the Web SDK on your Shopify website]().

## User profile merging 

{% alert note %}
The default Shopify integration provides tooling to assist with merging your anonymous user profile and the Shopify alias profile. If you are [implementing the integration to a headless Shopify site](), review Implementing the Web SDK directly onto your headless Shopify site to confirm you are properly reconciling your users. 
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

During the **Collect Email of SMS Subscribers** step, select whether you want to collect email and SMS opt-ins from your Shopify store to sync to Braze.

IMAGE

#### Collect email subscribers

If selected, Braze will update the global email subscription state on the profile to `subscribed` so you can send emails to your users. You can also optionally add one or more [subscription groups]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups) to automatically assign email subscribers to when they opt-in.

IMAGE

#### Collect SMS subscribers

If selected, Braze will update the selected [SMS subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) on the profile to `subscribed` so you can send messages to your users. If you are collecting SMS opt-ins, you must select one subscription group. If no subscription group exists, or you would like to create a new subscription group, contact your Braze customer success manager for support.

If there is an existing global subscription state on a user profile within Braze that’s different from Shopify, we recommend you turn on **Override existing global subscription state for users**. This will override the Braze state to check if it matches with Shopify.

{% alert important %}
If you do not override global subscription states, existing user states may not match those found in Shopify. This can lead to unreceived and unintended messages.
{% endalert %}

#### Legacy custom attributes

Legacy Shopify customers may have the old method of collecting email and SMS subscribers via the `shopify_accepts_marketing` and `shopify_sms_consent` custom attributes. If you save the settings above with override enabled, Braze will remove the custom attributes on the user profiles and sync those values over to their respective email subscription group and SMS subscription group.

If you have existing campaigns or Canvases using these legacy custom attributes, remove those attributes and confirm the campaigns or Canvases are using the appropriate subscription state, group, or both.