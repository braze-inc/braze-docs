---
nav_title: Simple Survey
platform: Message_Building_and_Personalization
subplatform: In-App Messages
page_order: 1.5
description: "Collect user attributes, insights, and preferences to power your campaign strategy using new In-App Message Surveys."
---

# Simple Survey In-App Message

Collect user attributes, insights, and preferences to power your campaign strategy using new In-App Message Surveys.

{% alert important %}
This feature is in *Early Access*. Ask your Braze account team to request access!
{% endalert %}

## SDK Requirements {#supported-sdk-versions}

This feature requires the following minimum SDK versions:

{% sdk_min_versions web:2.5.0 android:8.0.0 ios:3.23.0 %}

{% alert warning %}
Because this message type can only be received by certain newer SDK versions, users that are on unsupported SDK versions will not receive the message. <br><br>

Did you know you can segment app versions _above_ these SDK requirements? [Learn More]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).
{% endalert %}

![example]({% image_buster /assets/img/iam/iam-survey.png %})

* Collect User Preferences as Custom Attributes
* Gather Customers Satisfaction and Feedback
* Promote New Features and Trigger Promotions

## Creating a new Survey {#create}

Create a new Survey message by selecting the Simple Survey option in your message's Template Type option.

![Simple Survey Message Type]({% image_buster /assets/img/iam/survey-message-type.png %}){: style="max-width:700px"}

This Survey template is supported on mobile, web, or both mobile + web. Remember to be sure that your SDKs are on the [minimum versions](#supported-sdk-versions) required for this feature.

### Options {#options}

#### Single vs. Multiple Choice Survey {#single-multiple-choice}

Use the Single vs. Multiple Choice option to control whether a user can select only one choice, or multiple choices.

When Custom Attribute collection is enabled, the Multiple Choice option will set each choice's designated custom attribute. So, be sure to use a unique Custom Attribute name for each choice to prevent choices from overwriting each other.

![Single Multiple Choice]({% image_buster /assets/img/iam/single-multiple-choice.png %}){: style="max-width:700px"}

### Collect Custom Attributes

Enable Custom Attribute collection to collect attributes based on the user's submission. Use this option to create new segments and retargeting campaigns. For example, in a satisfaction survey, you could send a follow-up email to all users who were not happy.

![Custom Attributes]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:700px"}

### Showing A Confirmation Page

Once a user submits their response, you can optionally show a confirmation page or close the message.

Use a confirmation page to thank users or provide additional information, and set a click-through URL to other parts of your app or website.

![Confirmation Option]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:700px"}

![Confirmation Page]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:700px"}

### Styling Your Message

Customize the font and accent color of the message using the Color Theme picker.

![Color Theme Picker]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:700px"}

## Analyzing Results

Analyze results in real-time in your message's analytics report to see how many users selected each choice.

![Analytics]({% image_buster /assets/img/iam/analytics.png %}){: style="max-width:700px"}

 <!-- Retargeting Using Custom Attributes -->
