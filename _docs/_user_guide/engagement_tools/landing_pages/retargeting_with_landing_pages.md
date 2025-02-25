---
nav_title: Retargeting with Landing Pages
article_title: Retargeting with Landing Pages
guide_top_header: "Retargeting with Landing Pages"
description: "This article contains resources on how to retarget users with Braze landing pages."
alias: /landing_pages/retargeting
---

# Retargeting with landing pages

> Learn how to create segments of users who have submitted a landing page form and how to trigger messages when a landing page form is submitted. 

Braze will automatically track when a user submits a landing page form. The total count of these form submissions will be shown in your [landing page analytics]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#viewing-analytics). For more user specific breakdowns of form submissions, you have the option to create a [segment](#segmentation) based on whether a user has or has not submitted a landing page form. You can also [trigger messages](#retargeting-with-landing-pages) when users submit landing page forms. 

## Segmentation

When [creating a segment]({{site.baseurl}}/docs/user_guide/engagement_tools/segments/creating_a_segment/), under the "Retargeting" group, select **Submitted form on Landing Page** as a filter. 

From here, you have the ability to segment users based on whether they have or have not submitted a landing page form for a specific landing page. 

![Segment creation with the Filter Group selected as "Submitted Form on Landing Page"]({% image_buster /assets/img/landing_pages/segmentation_selected.png %})

## Triggering messages on landing page submissions

Select **Action Based Delivery** when selecting your delivery option. and select **Submitted Landing Page form** to trigger a message or Canvas based on a landing page submisssion.

![Landing page trigger action in messaging]({% image_buster /assets/img/landing_pages/trigger.png %})

All users who submit this form will then be messaged on the eligible messaging channel or entered into the Canvas. 