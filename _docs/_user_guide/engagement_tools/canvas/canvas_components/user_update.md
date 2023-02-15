---
nav_title: User Update 
article_title: User Update 
alias: "/user_update/"
page_order: 6
page_type: reference
description: "This reference article covers the User Update component and how to use them in your Canvases."
tool: Canvas
---

# User Update 

![][1]{: style="float:right;max-width:45%;margin-left:15px;"}

The User Update component allows you to update a user's attributes, events, and purchases in a JSON composer, so there's no need to include sensitive information like API keys.

With User Update, updates don't count towards your users or track per minute rate limit. Instead, these updates are batched so Braze can process them more efficiently than a Braze-to-Braze webhook. Note that this component does consume [data points]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/).

Users will only advance to downstream Canvas steps after the relevant user updates have been completed. If your downstream messaging relies on the user updates that you're making, you can ensure that these updates have been completed prior to when the messages send.

## Create a User Update

Drag and drop the component from the sidebar, or click the <i class="fas fa-plus-circle"></i> plus button at the bottom of the variant or step and select **User Update**. 

There are three options that allow you to update existing, add new, or remove user profile information. All combined, the User Update steps in an app group can update up to 200,000 user profiles per minute.

### Update custom attribute

To add or update a custom attribute, select an attribute name from your list of attributes and enter the key value.

![][4]{: style="max-width:90%;"}

### Remove custom attribute

To remove a custom attribute, select an attribute name using the dropdown. You can switch to the advanced JSON composer to further edit. 

![][5]{: style="max-width:90%;"}

### Advanced JSON composer

Add an attribute, event, or purchase JSON object up to 65,536 characters to the JSON composer. A user's [global subscription]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) and [subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) state can also be set.

![][2]{: style="max-width:90%;"}

Using the advanced composer, you can also preview and test that the user profile is updated with the changes with the **Preview and test** tab. You can either select a random user or search for a specific user. Then, after sending a test to a user, view the user profile using the generated link.

![][6]{: style="max-width:90%;"}

#### Limitations

You don't need to include sensitive data like your API key while using the JSON composer as this is automatically provided by the platform. As such, the following fields are unneeded and should not be used in the JSON composer:
* External user ID
* API key
* Braze cluster URL
* Fields related to push token imports

## Use case

For example, if we want a group of users to be promoted to loyalty members, select **Loyalty Member** as the attribute name, and select `True` as the corresponding key value. So, the users who enter this User Update step will have their VIP Member attribute updated to `True`.

![][3]{: style="max-width:90%;"}

## Personalization features

To store the property of the trigger event for a Canvas as an attribute, use the personalization modal to extract and store the Canvas entry property. This component also supports the following personalization features: 
* [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [Entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/)
* Liquid logic (including [aborting messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/))
* Multiple attribute or event updates per object


[1]: {% image_buster /assets/img_archive/canvas_user_update_step.png %} 
[2]: {% image_buster /assets/img_archive/canvas_user_update_composer.png %} 
[3]: {% image_buster /assets/img_archive/canvas_user_update_example.png %} 
[4]: {% image_buster /assets/img_archive/canvas_user_update_update.png %} 
[5]: {% image_buster /assets/img_archive/canvas_user_update_remove.png %} 
[6]: {% image_buster /assets/img_archive/canvas_user_update_test_preview.png %} 
