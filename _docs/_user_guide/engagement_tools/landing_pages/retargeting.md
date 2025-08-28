---
nav_title: Retargeting users
article_title: Retargeting Users through a Landing Page
description: "Learn how to retarget users who've submitted a form through a landing page."
page_order: 3
---

# Retargeting users through a landing page

> Learn how to retarget users who've submitted a form through a landing page by creating a dedicated segment or triggering a message when the form is submitted.

## Prerequisites

Before you start, you'll need to create a [landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/).

## Retargeting users

Braze automatically tracks when a user submits a landing page form. You can view the total number of submissions for a form under [landing page analytics]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#viewing-analytics). However, for user-specific retargeting, you'll need to retarget users through your landing page form using one of the following methods:

- **Using a segment:** You can create a new segment to automatically identify users who have or haven't submitted a landing page form.
- **Using a message trigger:** You can set up a message trigger to automatically message users or enter them into a Canvas after they submit the form.

{% tabs local %}
{% tab Using a segment %}
When you [create a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), under "Retargeting" group, choose **Submitted form on Landing Page**.

![Segment creation with the Filter Group selected as "Submitted Form on Landing Page".]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

From here, you can segment users based on whether they have or haven't submitted a landing page form for your landing page.
{% endtab %}

{% tab Using a message trigger %}
When you choose your delivery option for your [campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) or [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/), select **Action Based Delivery**, then **Submitted Landing Page form**.

All users who submit a form through this landing page form will either be messaged through the chosen messaging channel or entered into the chosen Canvas.

![Landing page trigger action in messaging.]({% image_buster /assets/img/landing_pages/trigger.png %})

{% alert note %}
The action-based delivery option for landing pages isn't available for in-app messages. To target users who have submitted a form on a landing page with an in-app message, select the **Submitted Form on Landing Page** filter in the **Targeting Options** of your campaign.
{% endalert %}

{% endtab %}
{% endtabs %}
