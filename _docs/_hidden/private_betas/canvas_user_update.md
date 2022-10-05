---
nav_title: User Update 
article_title: User Update 
permalink: "/user_update/"
hidden: true
page_type: reference
description: "This reference article covers the User Update component and how to use them in your Canvases."
tool: Canvas
---

# User Update 

![][1]{: style="float:right;max-width:45%;margin-left:15px;"}

The User Update component allows you to update a user’s attributes, events, and purchases in a JSON composer, so there's no need to include sensitive information like API keys.

With User Update, updates don't count towards your users or track per minute rate limit. Instead, these updates are batched so Braze can process them more efficiently than a Braze-to-Braze webhook. Note that this component does consume [data points]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/).

Users will only advance to downstream Canvas steps after the relevant user updates have been completed. If your downstream messaging relies on the user updates that you're making, you can ensure that these updates have been completed prior to when the messages send.

{% alert important %}
User Update is currently in early access and only supported in Canvas Flow. Contact your Braze account manager if you are interested in participating in this early access. <br><br>Braze will begin to deprecate Braze-to-Braze webhooks that target the `/users/track` endpoint once this feature is generally available. We'll let you know about the full deprecation process and timeline when the User Update component is released so that you have the time and support from Braze to make the switch.
{% endalert %}

## Create a User Update

Drag and drop the component from the sidebar, or click the <i class="fas fa-plus-circle"></i> plus button at the bottom of the variant or step and select **User Update**. 

There are three options that allow you to update existing, add new, or remove user profile information. If you switch between actions, this will clear any existing inputs. This component will update up to 50,000 user profiles per minute.

### Update user attribute

To update a user attribute, select an attribute name from your list of existing attributes and key value using the dropdowns.

### Remove user attribute

To remove a user attribute, select an attribute name using the dropdown.

### Advanced JSON composed 

Then, add an attribute, event, or purchase JSON object to the JSON composer. You can add up to 65,536 characters to the JSON composer.

![][2] 

#### Limitations

Do not include any of the following information in the JSON composer:
* External user ID
* API key
* Braze cluster URL
* Fields related to push token imports

As an example, users who receive the following User Update step will have the VIP Member attribute set to `true`.

![][3]

## Personalization features

User Update also supports the following personalization features: 
* [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [Entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/)
* Liquid logic (including [Aborting Messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/))
* Multiple attribute or event updates per object


[1]: {% image_buster /assets/img_archive/canvas_user_update_step.png %} 
[2]: {% image_buster /assets/img_archive/canvas_user_update_composer.png %} 
[3]: {% image_buster /assets/img_archive/canvas_user_update_example.png %} 
