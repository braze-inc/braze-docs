---
nav_title: User Update 
article_title: User Update 
alias: "/user_update/"
page_order: 6
page_type: reference
description: "This reference article covers the User Update component and how to use it in your Canvases."
tool: Canvas
---

# User Update 

![][1]{: style="float:right;max-width:45%;margin-left:15px;"}

The User Update component allows you to update a user's attributes, events, and purchases in a JSON composer, so there's no need to include sensitive information like API keys.

With User Update, updates don't count towards your users or track per minute rate limit. Instead, these updates are batched so Braze can process them more efficiently than a Braze-to-Braze webhook. Note that this component does consume [data points]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/).

Users will only advance to the next Canvas steps after the relevant user updates have been completed. If your subsequent messaging relies on the user updates that you're making, you can ensure that these updates have been completed prior to when the messages send.

## Create a User Update

Drag and drop the component from the sidebar, or click the <i class="fas fa-plus-circle"></i> plus button at the bottom of the variant or step and select **User Update**. 

There are three options that allow you to update existing, add new, or remove user profile information. All combined, the User Update steps in an app group can update up to 200,000 user profiles per minute.

{% alert tip %}
You can also test the changes made with this component by searching for a user and applying the change to them. This will update the user.
{% endalert %}

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

## Use cases

### Set Canvas entry property as an attribute

You can use the user update step to persist a `canvas_entry_property`.  Let’s say you have an event that triggers when an item is added to a cart. You can store the ID of the most recent item added to cart and use that for a remarketing campaign. Use the personalization feature to retrieve a Canvas entry property and store it in an attribute.

![][8]{: style="max-width:90%;"}

#### Personalization

To store the property of the trigger event for a Canvas as an attribute, use the personalization modal to extract and store the Canvas entry property. User Update also supports the following personalization features: 
* [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [Entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/)
* Liquid logic (including [aborting messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/))
* Multiple attribute or event updates per object

### Increment numbers

This component can also be used to track the number of times a user has performed an event in increment and decrement numbers. For example, you could track the number of classes that a user has taken in a week. Using this component, the class count can reset at the start of the week and begin tracking again. 

![][7]{: style="max-width:90%;"}

### Add to arrays

You can add or remove items from an array, and remove an item. For example, you could use this step to add to or remove items from a wishlist.

![][9]{: style="max-width:90%;"}

[1]: {% image_buster /assets/img_archive/canvas_user_update_step.png %} 
[2]: {% image_buster /assets/img_archive/canvas_user_update_composer.png %} 
[3]: {% image_buster /assets/img_archive/canvas_user_update_example.png %} 
[4]: {% image_buster /assets/img_archive/canvas_user_update_update.png %} 
[5]: {% image_buster /assets/img_archive/canvas_user_update_remove.png %} 
[6]: {% image_buster /assets/img_archive/canvas_user_update_test_preview.png %} 
[7]: {% image_buster /assets/img_archive/canvas_user_update_increment.png %} 
[8]: {% image_buster /assets/img_archive/canvas_user_update_cep.png %} 
[9]: {% image_buster /assets/img_archive/canvas_user_update_wishlist.png %} 