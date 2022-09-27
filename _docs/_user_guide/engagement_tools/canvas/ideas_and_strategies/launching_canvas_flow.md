---
nav_title: Launching with Canvas Flow
article_title: Launching with Canvas Flow
page_order: 3
description: "This reference article covers how to prepare and test a Canvas built with Canvas Flow before launch."
page_type: reference
tool: Canvas
---

# Launching with Canvas Flow

> This reference article covers how to prepare and test a Canvas built using Canvas Flow before launch. This includes identifying importnat Canvas checkpoints such as Canvas entry conditions, audience summaries, and user segments.

## Canvas entry

### Race conditions

To enter your Canvas, users must be in the **Entry Audience** before the entry schedule occurs (whether that be scheduled at a specific time, or triggered by action-based or API-triggered event). Note that users who qualify for your entry audience after will not enter for Canvases that are action-based, API-triggered, or one-time-send Canvases.

### Delivery times

By setting a Canvas delivery time in real time, this can lead to increasing engagement and conversion rates. Take note of which delivery time you've set for your Canvas. To increase engagement and conversion rates, it's best to have Canvases trigger in real time as opposed to a scheduled, recurring basis.

## Segment users

Before oversaturating your Canvas Flow user journey with components, consider how you might keep a user journey simple. Use the simplified view in the Canvas editor to get a better idea of how your user journey branches. 

There are four main components you can use to segment your users in a simple, effective manner:

* Audience Paths
* Decision Split
* Action Paths
* Experiement Paths

Use the Action Paths step to segment users within the Canvas based on custom attributes, custom events, and previous message engagement data from user profiles.

The Decision Split step creates a point in your user journey where you can evaluate your users with a polar question to determine which path to send the user to, depending on their answer.

Actions Paths focus on segmenting users based on real-time behaviors such as custom events, purcahse events, and custom attribute changes.

Similar to Action Paths, you can leverage Experiment Paths steps in your Canvas to test multiple Canvas paths against each other, along with a control group. This tracks path performance, allowing you to make informed decisions when building your Canvas journey. 


## Testing before launch

