---
nav_title: User Update Step
article_title: User Update Step
permalink: "/user_update/"
hidden: true
page_type: reference
description: "This reference article covers the User Update Step and how to use them in your Canvases."
tool: Canvas
---

# User Update Step

![][1]{: style="float:right;max-width:45%;margin-left:15px;"}

The Canvas User Update Step allows you to update a user’s attributes, events, and purchases in a JSON composer, so there's no need to include sensitive information like API keys.

With the User Update Step, updates do not count towards your users or track per minute rate limit. Instead, updates are batched so Braze can process them more efficiently than a Braze-to-Braze webhook.

Users will only advance to downstream Canvas steps after the relevant user updates have been completed. If your downstream messaging relies on the user updates that you are making, you can ensure that these updates have been completed prior to when the messages send.

{% alert important %}
The Canvas User Update Step is currently in early access. Braze will begin to deprecate Braze-to-Braze webhooks once this feature is generally available. Contact your Braze account manager if you are interested in participating in the Canvas User Updates early access.
{% endalert %}

## Create a User Update Step

To create a User Update Step, add a step to your Canvas. Use the drop-down menu at the top of the new step to select `User Update Step`. Then, add an attribute, event, or purchase JSON object to the JSON composer.

![][2] 

{% alert note %}
Do not include any of the following information in the JSON composer:
* External user ID
* API key
* Braze cluster URL
* Fields related to push token imports
{% endalert %}

As an example, users who receive the following User Update Step will have the VIP Member attribute set to `true`.

![][3]

### Personalization Features

The User Update Step also supports the following personalization features: 
* [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [Entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) and [event properties]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)
* Liquid logic (including [Aborting Messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/))
* Multiple attribute or event updates per object


[1]: {% image_buster /assets/img_archive/canvas_user_update_step.png %} 
[2]: {% image_buster /assets/img_archive/canvas_user_update_composer.png %} 
[3]: {% image_buster /assets/img_archive/canvas_user_update_example.png %} 
