---
nav_title: Retargeting with Landing Pages
article_title: Retargeting with Landing Pages
guide_top_header: "Retargeting with Landing Pages"
description: "This article contains resources on how to retarget users with Braze landing pages."
alias: /landing_pages/retargeting
---

# Retargeting with Landing Pages

> Learn how to create segments of users who have submitted a landing page form and how to trigger messages on landing page form submission events. 

When creating a landing page, Braze will automatically track form submission events tied to each landing page. The aggregate count of these form submissions will be shown in your [Landing Page analytics]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/viewing-analytics). For more user specific breakdowns of form submissions, you have the option to create a segment based on whether a user has or has not submitted a landing page form. You can also trigger messages when users submit landing page forms. 

## Segmentation

When creating a segment, under the “Retargeting” group, select “Submitted form on Landing Page” as a filter. 

![The landing pages segmentation search]({% image_buster assets/img/landing_pages/segmentation.png %})

From here, you have the ability to segment users based on whether they have or have not submitted a landing page form for a specific landing page. 

![Landing pages segmentation filter selected] ({% image_buster assets/img/landing_pages/segmentation selected.png %})

## Triggering Messages on Landing Page Submissions

For action based delivery of other messaging channels when a user submits a landing page form, select “Action Based Delivery” when selecting your delivery option, select “Submitted Landing Page form” 

![Landing page trigger action in messaging]({% image_buster assets/img/landing_pages/trigger.png %})


All users who submit this form will then be messaged on the eligible messaging channel. 
