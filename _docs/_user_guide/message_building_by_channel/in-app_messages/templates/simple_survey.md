---
nav_title: Simple Survey
platform: Message_Building_and_Personalization
subplatform: In-App Messages
page_order: 9
description: "Collect custom user attributes and power retargeting campaigns using an In-App Message Survey Template."
---

# Simple Survey In-App Message

Collect custom user attributes and power retargeting campaigns using an In-App Message Survey Template.

{% alert important %}
This feature is in *Early Access*. Ask your Braze account team to request access!
{% endalert %}


<hr>

## SDK Requirements {#supported-sdk-versions}

To use this feature, your apps will need to be on at least the following SDK versions:

{% sdk_min_versions web:2.5.0 android:8.0.0 ios:3.23.0 %}

{% alert warning %}
Because this message type can only be received by certain newer SDK versions, users that are on unsupported SDK versions will not receive the message. <br><br>

Did you know you can segment app versions _above_ these SDK requirements? [Learn More]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).
{% endalert %}

## Examples {#examples}

<style>
.swiper-container .swiper-description p {
    font-size: 1.7rem;
}
</style>
{% gallery %}
 {{site.baseurl}}/assets/img/iam/iam-survey.png <br><br> Collect User Preferences as Custom Attributes
 {{site.baseurl}}/assets/img/iam/iam-survey.png <br><br> Gather Customers Satisfaction and Feedback
 {{site.baseurl}}/assets/img/iam/iam-survey.png <br><br> Promote New Features and Trigger Promotions
{% endgallery %}


## Creating A New Survey Message {#create}

Create a new Survey message by selecting the Simple Survey option in your message's Template Type option.

![Simple Survey Message Type]({% image_buster /assets/img/iam/survey-message-type.png %}){: style="max-width:700px"}

This Survey template is supported on mobile, web, or both mobile + web. Remember to be sure that your SDKs are on the [minimum versions](#supported-sdk-versions) required for this feature.

### Options {#options}

#### Single vs. Multiple Choice {#single-multiple-choice}

Use the Single vs. Multiple Choice option to control the number of choices a user can select; one, or multiple.

When Custom Attribute collection is enabled, the Multiple Choice option will set each choice's designated custom attribute. Be sure to use a unique Custom Attribute name for each choice to prevent choices from overwriting each other.

![Single Multiple Choice]({% image_buster /assets/img/iam/single-multiple-choice.png %}){: style="max-width:700px"}

### Collecting Custom Attributes

![Color Theme Picker]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:700px"}

### Showing A Confirmation Page

![Confirmation Option]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:700px"}

![Confirmation Page]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:700px"}

### Styling Your Message

![Color Theme Picker]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:700px"}

## Analyzing Results

![Analytics]({% image_buster /assets/img/iam/analytics.png %}){: style="max-width:700px"}

## Retargeting Using Custom Attributes
