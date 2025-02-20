---
nav_title: Anonymous users
article_title: Getting Started&#58; Anonymous Users
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

When a user first uses Braze on a device, they are considered "anonymous". This user will remain anonymous until an `external_id` is assigned to that user's profile by a `changeuser` method ([web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69), [Android](https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-)), and then will become known. Once an anonymous user becomes known, they can't reverted to an anonymous user, but uninstalling and reinstalling an app will generate a new anonymous user ID for that user. 

### When users are identified on new devices

If a user is identified on a device where they **have never** been identified before, all their previous activity on that device as an anonymous user will be saved and linked to their newly identified profile. This means that all their attributes, events, and history will be attributed to them, even though they were anonymous at the time.

### When users are identified on old devices

If a user is identified on a device where they **have been** identified before, any previous activity that was already sent to the server from the anonymous user on that device will become "orphaned". In other words, that activity won't be linked to any future users. These "orphaned" users aren't included in user counts and won't receive any messages. This is because their activity isn't associated with an identified user, so there's no way to attribute their actions to a specific user.

## Assigning user aliases

Anonymous users don’t have `external_ids`, but you can assign anonymous user profiles with an alternative identifier: [user aliases]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#user-aliases). This allows you to take the same actions on an anonymous user profile as if they were identified by `external_ids`. For example, you can use the Braze API to log events and attributes associated with anonymous users, and target those users in your messaging with the segmentation filter [External User ID is blank]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#external-user-id).

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
