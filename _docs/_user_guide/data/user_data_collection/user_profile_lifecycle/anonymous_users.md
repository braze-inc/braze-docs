---
nav_title: Anonymous users
article_title: Anonymous Users
page_order: 0
page_type: reference
description: "This article provides an overview of anonymous users and user aliases, outlining their significance and how they can be leveraged in your messages."

---

# Anonymous users

> Users who visit your website or application without logging in, like a guest visitor, are recognized as anonymous users. These users don't have `external_ids`, which are used to update user profiles with the Braze API, but they still have [data points]({{site.baseurl}}/user_guide/data/data_points/) assigned to them and can be targeted in your segments.

When an anonymous user visits your website or application, the Braze SDK creates and assigns them to an “anonymous” user profile. While the user browses, the SDK automatically captures data for their anonymous user profile, such as usage information, device information, and more if you’ve set up custom attributes and custom events.

You can do the following with captured anonymous users:

- Message users before they log in
- Collect a user’s profile before they log in, so you don’t miss out on relevant data
- Encourage profile completion with a message when a user only partially completes their profile
- Complete a user’s profile when they log in, so that you can cancel messaging on other platforms (such as not sending a “free shipping on 1st app order” message when the user already has made app orders)
- Engage with users who show an intent to exit by encouraging them to create a profile, checkout their cart, or take another action

## How it works

After you [integrate the Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/), users who launch your app for the first time will be considered "anonymous" until you call the `changeUser` method and assign them an `external_id` through the Braze SDK. For a full walkthrough, see [Setting User IDs]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/).

Once a user is assigned an `external_id`, you can't revert them to an anonymous user&#8212;however, by uninstalling and reinstalling your app they'll be considered anonymous again until `changeUser` is called.


If a previously-identified user starts a session on a new device, all of their "anonymous" activity will automatically sync to their existing profile after you call `changeUser` on that device. This includes any attributes, events, or history collected during the session on the new device.

## Assigning user aliases

Although anonymous users don’t have `external_ids`, you can assign them a [user alias]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#user-aliases) instead. You should assign a user alias when you want to add other identifiers to the user but don't know what their `external_id` is (for example, they aren't logged in). With user aliases, you also can:

- Use the Braze API to log events and attributes associated with anonymous users
- Use the [External User ID is blank]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#external-user-id) segmentation filter to target anonymous users in your messaging

For more information, see [Braze SDK: Setting a user alias]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).

## Merging anonymous users  

Sometimes anonymous user profiles are duplicates that have the same phone number or email address as other user profiles. One of the duplicates may even be an identified user profile. These duplicates can be merged into one user profile by using the [POST: Merge Users endpoint]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) or one of the merge tools on the Braze platform, such as [rules-based merging]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging).

## Use cases

### Target anonymous users in your segment

Because anonymous users don't have an `external_id`, you can target them in bulk by using the segmentation filter **External User ID is blank**. For further accuracy, you can add a custom attribute to the anonymous users you want to target and filter for that.

Let's say you assign the custom attribute "is_lead_profile" to each anonymous user profile. You could target these profiles with one or both of these filters:

- **External User ID is blank**
- "is_lead_profile" **is true**

![Segment filters for a blank external user ID and a true "is_lead_profile" custom attribute.][1]

### Capture checkout data from an anonymous user

You can capture checkout data from an anonymous user (or guest visitor) by creating a user aliased profile during the checkout process. When an anonymous user checks out by using a web capture form, have an API call trigger to create a user aliased profile and log a purchase event. You'll then be able to update the created user profile through the Braze API.

Here is an example payload that will generate when the web capture form is submitted:

{% raw %}
```json
{
    "purchase":[
        {
            "user_alias": {"alias_name": "Joedoe", "alias_label": "full_name"},
            "app_id": "11dk3k9d-2183-3948-k02b-kw3938109k12od",
            "product_id": "jacket",
            "currency": "USD",
            "price": 80.00,
            "time": "2025-01-05T19:20:30+01:00",
            "properties": {
                "color": "brown",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Small",
                "brand": "Natural Essence"
            }
        }
    ]
}
```
{% endraw %}

[1]: {% image_buster /assets/img/getting_started/anonymous_users.png %}
