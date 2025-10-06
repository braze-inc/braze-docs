---
nav_title: "Simple survey"
article_title: Simple Survey In-App Message
page_order: 1.5
page_type: reference
description: "This reference article covers how to collect user attributes, insights, and preferences to power your campaign strategy using the in-app message surveys."
channel:
  - in-app messages
tool:
  - Templates
---

# Simple survey

> Use the **Simple Survey** in-app message template to collect user attributes, insights, and preferences that power your campaign strategy. 

For example, ask users how they'd like to use your app, learn more about their personal preferences, or even ask about their satisfaction with a particular feature.

![Three simple survey messages: notification preferences, dietary preferences, and a customer satisfaction survey. The selected options in the surveys correspond to custom attributes that will be logged for that user.]({% image_buster /assets/img/iam/iam-survey.png %})

## SDK requirements {#supported-sdk-versions}

This in-app message will only be delivered to devices that support [Flex CSS](https://caniuse.com/flexbox), and must have at least the following [SDK versions]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions). 

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
To enable HTML in-app messages through the Web SDK, you must supply the `allowUserSuppliedJavascript` initialization option to Braze.
{% endalert %}

## Creating a survey {#create}

When creating an [in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/), select **Simple Survey** for your **Message Type**.

This survey template is supported for both mobile apps and web browsers. Remember to check that your SDKs are on the [minimum SDK versions](#supported-sdk-versions) required for this feature.

### Step 1: Add your survey question

To get started building your survey, add your question to the survey **Header** field. If desired, you can add an optional **Body** message that will appear under your survey question.

![Compose tab of the simple survey editor, with fields for a header, optional body, and optional helper text.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:90%"}

{% alert tip %} 
These fields can include both Liquid and emojis, so get fancy! 
{% endalert %}

### Step 2: Configure choices {#single-multiple-choice}

You can add up to 12 choices in a survey.

Select either **Single-choice selection** or **Multiple-choice selection**. The **Helper text** will automatically update when you switch between the two options to let users know how many choices they can select. 

Then, determine if you will [collect custom attributes](#custom-attributes) or [log responses only](#no-attributes).

![Choices dropdown with "Log attributes upon submission" selected.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### Collect custom attributes {#custom-attributes}

Select **Log attributes upon submission** to collect attributes based on the user's submission. You can use this option to create new segments and retargeting campaigns. For example, in a [satisfaction survey](#user-satisfaction), you could send a follow-up email to all users who were not happy.

To add a custom attribute to each choice, select a custom attribute name from the dropdown menu (or create a new one), and then enter the value to set when this choice is submitted. You can also create a new custom attribute in your [Settings Page]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/).

The data type of your custom attributes matters depending on how you've set up your survey.

- **Multiple-choice selection:** The data type of the custom attribute must be an array. If the custom attribute is set to a different data type, responses will not be logged.
- **Single-choice selection:** The data type of the custom attribute _must not_ be an array. Responses will not be logged if the attribute is an array.

{% alert important %} 
When custom attribute collection is enabled, choices that share the same custom attribute name will be combined into an array.
{% endalert %}

##### Example 

For example, in a [notification preferences survey](#notification-preferences), you might make each choice a boolean (true/false) attribute to allow users to select which topics they're interested in. If a user checks the "Promotions" choice, that will update their [user profile]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) with the custom attribute `Promotions Topic` set to `true`. If they leave the choice unchecked, that same attribute will remain unchanged.

You can then use the `Custom Attribute` filter to create a segment for users with the custom attribute `Promotions Topic` `is` `true` to make sure that only users interested in your promotions will receive the relevant campaigns.

#### Logging responses only {#no-attributes}

Alternatively, you can choose to **Log responses only (no attributes)**. When this option is selected, survey responses are logged as button clicks, but custom attributes are not logged to a user's profile. This means you can still view the click metrics for each survey option (see [Analytics](#analytics)), but that choice won't be reflected on their user profile.

These click metrics are not available for retargeting.

### Step 4: Choose submission behavior

Once a user submits their response, you can optionally show a confirmation page, or simply close the message.

A confirmation page is a great place to thank users for their time or provide additional information. You can customize the call-to-action on this page to guide users to another page of your app or website.

Edit your button text and on-click behavior in the **Submit Button** section at the bottom of the **Survey** tab:

![On-click behavior set to "Submit responses and display confirmation page".]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

If you elect to add a confirmation page, switch to the **Confirmation Page** tab to customize your message:

![Confirmation Page tab of the simple survey editor. The available fields are header, optional body, button text, and button on-click behavior.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:90%"}

If you want to guide users to another page of your app or website, change the button's **On-click behavior**.

### Step 5: Stylize your message (optional) {#styling}

You can customize the font color and accent color of the message using the **Color Theme** picker.

![Compose tab of the simple survey editor with the Color Theme picker expanded after a user has clicked on the color palette.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analyze results {#analytics}

Once your campaign has launched, you can analyze results in real-time to see the breakdown of each selected choice. If you've enabled [custom attribute collection](#custom-attributes), you'll also be able to create new segments or follow-up campaigns for users who have submitted the survey.

{% alert note %}
Deleted survey choices will still appear in analytics but will not be shown as a choice to new users.
{% endalert %}

You can find your survey performance metrics by expanding the **Results** dropdown for a specific variant in the **In-App Message Performance** section of the analytics. Here’s a breakdown of what you’ll see:

- **Survey engagement** shows how users interacted with the survey overall, including total submissions, dismissals, and clicks within the message body.
- **Survey results** display a breakdown of how many users selected each response option, along with the percentage of total submissions each choice represents.
- **Confirmation page metrics** (if enabled) include how many users viewed the confirmation screen, clicked its button, or dismissed it without interacting.

For definitions of survey metrics, refer to the [Report Metrics Glossary]({{site.baseurl}}/user_guide/data/report_metrics/) and filter by "In-App Message".

Check out [In-app message reporting]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) for a breakdown of your campaign metrics.

### Currents {#currents}

Selected choices will automatically flow through to Currents, under the [**In-App Message Click Events**]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe) `button_id` field. Each choice will be sent with its universally unique identifier (UUID).

## Use cases

{% tabs %}
{% tab User satisfaction %}

### User satisfaction

**Goal:** Measure customer satisfaction and send win-back campaigns to users who left low scores.

To set this up, use a single-choice selection survey with five options ranging from “😡 Very Dissatisfied” to “😍 Very Satisfied.” Each choice is mapped to the custom attribute `customer_satisfaction`, with a numeric value from 1 to 5—where 1 indicates the least satisfied and 5 the most satisfied.

| Choice                                | Attribute              | Value |
|---------------------------------------|------------------------|-------|
| 😡 Very Dissatisfied                  | `customer_satisfaction` | 1     |
| 😟 Dissatisfied                       | `customer_satisfaction` | 2     |
| 🙂 Neither Satisfied nor Dissatisfied | `customer_satisfaction` | 3     |
| 😊 Satisfied                          | `customer_satisfaction` | 4     |
| 😍 Very Satisfied                     | `customer_satisfaction` | 5     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

When a user submits the survey, their selected value is logged as a custom attribute. You can then build follow-up campaigns using audience filters. For example, target win-back messages to users whose `customer_satisfaction` attribute is 1 or 2.

{% endtab %}
{% tab Notification preferences %}

### Notification preferences

**Goal:** Let users opt into specific types of notifications.

To set this up, use a multiple-choice selection survey where each choice represents a notification topic. Instead of assigning the same attribute with different values, each choice maps to a distinct boolean attribute that reflects the user’s interest in that topic. If a user selects a choice, the corresponding attribute is set to `true`. If left unselected, the attribute remains unchanged.

| Choice             | Attribute              | Value  |
|--------------------|------------------------|--------|
| Product Updates    | `wants_product_updates`| `true` |
| Promotions         | `wants_promotions`     | `true` |
| Event Invites      | `wants_event_invites`  | `true` |
| Surveys & Feedback | `wants_surveys`        | `true` |
| Tips & Tutorials   | `wants_tips`           | `true` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Identify customer goals %}

### Identify customer goals

**Goal:** Identify top reasons why users visit your app.

To set this up, use a single-choice selection survey with each option representing a common goal or intent. Each choice is mapped to the custom attribute `product_goal` with a value corresponding to the selected user intent.

| Choice                     | Attribute       | Value     |
|----------------------------|------------------|-----------|
| Checking status            | `product_goal`   | `status`  |
| Upgrading my account       | `product_goal`   | `upgrade` |
| Scheduling an appointment  | `product_goal`   | `schedule`|
| Customer support           | `product_goal`   | `support` |
| Just Browsing              | `product_goal`   | `browse`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

When a user submits the survey, the selected value is logged as a custom attribute on their profile. You can then use this data to personalize future experiences or segment users based on their primary goal.

{% endtab %}
{% tab Improve conversion rates %}

### Improve conversion rates

**Goal:** Understand why customers aren’t upgrading or purchasing.

To set this up, use a single-choice selection survey with each option representing a common barrier to upgrading. Each choice is mapped to the custom attribute `upgrade_reason` with a corresponding value that reflects the user's selection.

| Choice              | Attribute        | Value       |
|---------------------|------------------|-------------|
| Too Expensive       | `upgrade_reason` | `expensive` |
| Not Valuable        | `upgrade_reason` | `value`     |
| Difficult To Use    | `upgrade_reason` | `difficult` |
| Using a Competitor  | `upgrade_reason` | `competitor`|
| Other Reason        | `upgrade_reason` | `other`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

When a user submits the survey, the selected value is saved to their profile. You can then target these users with campaigns tailored to their specific objection, like discount offers or usability improvements.

{% endtab %}
{% tab Favorite features %}

### Favorite features

**Goal:** Understand which features customers enjoy using.

To set this up, use a multiple-choice selection survey where each option represents a feature of your app. Each choice is mapped to the custom attribute `favorite_features`, and when the user submits the survey, the attribute is set to an array of the selected values.

| Choice            | Attribute          | Value        |
|-------------------|--------------------|--------------|
| Bookmarks         | `favorite_features`| `bookmarks`  |
| Mobile App        | `favorite_features`| `mobile`     |
| Sharing Posts     | `favorite_features`| `sharing`    |
| Customer Support  | `favorite_features`| `support`    |
| Customization     | `favorite_features`| `custom`     |
| Price / Value     | `favorite_features`| `value`      |
| Community         | `favorite_features`| `community`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Because this survey uses multiple-choice selection, the user's profile will be updated with a list of all selected feature values.

{% endtab %}
{% endtabs %}
