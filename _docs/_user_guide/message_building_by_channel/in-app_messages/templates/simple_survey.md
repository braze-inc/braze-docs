---
nav_title: Simple Survey
platform: Message_Building_and_Personalization
subplatform: In-App Messages
page_order: 1.5
hidden: true
description: "Collect user attributes, insights, and preferences to power your campaign strategy using new In-App Message Surveys."
---
<br>
{% alert important %}
This feature is in a closed _Early Access_ period. To request access, please submit your feedback in our [Product Portal](https://dashboard.braze.com/resources/roadmap).
{% endalert %}

# Simple Survey In-App Message

Use the new **Simple Survey** In-App Message template to collect user attributes, insights, and preferences that power your campaign strategy.

For example, ask users how they'd like to use your app, learn more about their personal preferences, or even ask about their satisfaction with a particular feature.

![examples]({% image_buster /assets/img/iam/iam-survey.png %})

## SDK Requirements {#supported-sdk-versions}

This in-app message will only be delivered to devices that use at least the [SDK versions]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) below:

{% sdk_min_versions web:2.5.0 android:8.0.0 ios:3.23.0 %}

## Creating a Survey {#create}

When creating an [in-app message][1], select **Simple Survey** for your **Message Type**.

![Simple Survey Message Type]({% image_buster /assets/img/iam/survey-message-type.png %}){: style="max-width:80%"}

This survey template is supported for both mobile apps and web browsers. Remember to check that your SDKs are on the [minimum versions](#supported-sdk-versions) required for this feature.

### Step 1: Add Your Survey Question

To get started building your survey, add your question to the survey **Header** field. If desired, you can add an optional **Body** message that will appear below your survey question.

![Simple Survey Question]({% image_buster /assets/img/iam/iam-survey2.png %})

{% alert tip %} These fields can include both Liquid and emojis, so get fancy! {% endalert %}

### Step 2: Choose Between Single or Multiple-choice {#single-multiple-choice}

Use the Single vs. Multiple Choice option to control whether a user can select only one choice or multiple choices. You can add up to 12 choices in a survey.

![Single Multiple Choice]({% image_buster /assets/img/iam/single-multiple-choice.png %}){: style="max-width:70%"}

{% alert tip %} Your **Helper text** will automatically update when you switch between **Single-choice selection** and **Multiple-choice selection** to let users know how many options they can select. {% endalert %}

### Step 3: Collect Custom Attributes {#custom-attributes}

Select **Log attributes upon submission** to collect attributes based on the user's submission. You can use this option to create new segments and retargeting campaigns. For example, in a satisfaction survey, you could send a follow-up email to all users who were not happy.

![Custom Attributes]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:70%"}

To add a Custom Attribute to each choice, select an existing attribute name from the dropdown, and the value to set when this choice is submitted. You can create a new Custom Attribute in your [Settings Page][5].

For example, in a notification preferences survey, you might make each choice a boolean (true/false) attribute to allow users to select which topics they're interested in. If a user checks the "Promotions" option, that will update their [User Profile][3] with the Custom Attribute `Promotions_Topic = true`. If they leave the option unchecked, that same attribute will instead be marked as `false`.

![Choice Custom Attributes]({% image_buster /assets/img/iam/iam-survey3.png %}){: style="max-width:70%"}

You can then create a segment for users with `Promotions_Topic = true` to make sure that only users interested in your promotions will receive the relevant campaigns.

{% alert important %} When Custom Attribute collection is enabled, choices that share the same Custom Attribute Name will be combined into an Array.{% endalert %}

### Step 4: Choose Submission Behavior

Once a user submits their response, you can optionally show a confirmation page, or simply close the message.

A confirmation page is a great place to thank users for their time or provide additional information. You can customize the Call To Action on this page to guide users to another page of your app or website.

Edit your button text and on-click behavior in the **Submit Button** section at the bottom of the **Survey** tab:

![Confirmation Option]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:70%"}

If you elect to add a confirmation page, switch to the **Confirmation Page** tab to customize your message:

![Confirmation Page]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:70%"}

If you want to guide users to another page of your app or website, change the button’s **On-click behavior**.

### Step 5: Stylize Your Message (Optional) {#styling}

You can customize the font and accent color of the message using the **Color Theme** picker.

![Color Theme Picker]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analyze Results {#analytics}

Once your campaign has launched, you can analyze results in real-time to see the breakdown of each selected choice. If you've enabled [Custom Attribute collection](#custom-attributes), you'll also be able to create new segments or follow-up campaigns for users who have submitted the survey.

{% alert note %}
Deleted survey choices will still appear in analytics, but will not be shown as a choice to new users.
{% endalert %}

![Analytics]({% image_buster /assets/img/iam/iam-survey-analytics.png %}){: style="max-width:90%"}

Check out [Reporting & Analytics][4] for a breakdown of your campaign metrics.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[3]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
