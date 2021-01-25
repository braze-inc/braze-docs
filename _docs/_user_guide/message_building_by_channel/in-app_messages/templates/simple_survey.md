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

<style>
#sdk-versions .sdk-versions--chip {
    word-break: normal;
    tab-size: 4;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    box-sizing: inherit;
    margin: 0;
    align-items: center;
    cursor: default;
    display: inline-flex;
    line-height: 20px;
    max-width: 100%;
    outline: none;
    overflow: hidden;
    position: relative;
    text-decoration: none;
    transition-duration: .28s;
    transition-property: box-shadow,opacity;
    transition-timing-function: cubic-bezier(.4,0,.2,1);
    vertical-align: middle;
    white-space: nowrap;
    color: rgba(0,0,0,.87);
    border-radius: 16px;
    font-size: 14px;
    height: 32px;
    border: none !important;
    padding: 6px 17px !important;
}
</style>

## SDK Requirements {#supported-sdk-versions}

This template requires upgrading to the following Braze SDK versions:

<div id="sdk-versions" style="margin-bottom:30px">
    <a href="/developer_guide/platform_integration_guides/web/changelog/#250" class="sdk-versions--chip" style="background:#50c5d4">Web: 2.5.0+</a>
    <a href="/developer_guide/platform_integration_guides/ios/changelog/#3230" class="sdk-versions--chip" style="background:#ed9494">iOS: 3.23.0+</a>
    <a href="/developer_guide/platform_integration_guides/android/changelog/#800" class="sdk-versions--chip" style="background:#ff9449">Android: 8.0.0+</a>
</div>

{% alert warning %}
Because this message type can only be received by certain newer SDK versions, users that are on unsupported SDK versions will not receive the message. <br><br>

Consider adopting this new message type once a significant portion of your user base is reachable, or target only those users whose app version is _above_ the requirements. [Learn More]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)
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



