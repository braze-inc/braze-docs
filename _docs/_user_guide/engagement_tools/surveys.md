---
nav_title: Surveys
article_title: Braze surveys
description: "Learn how to create surveys in in-app messages and landing pages, review responses, and retarget users during closed beta."
hidden: true
---

# Braze surveys

> Braze surveys (closed beta) let you collect feedback in in-app messages and landing pages, then use responses for analysis and follow-up messaging.

{% alert important %}
Braze surveys are in closed beta. For beta feedback, email `surveys-feedback@braze.com`.
{% endalert %}

## Prerequisites

Before you start:

- Access to **Landing Pages** and/or **In-App Messages** in your Braze workspace
- Familiarity with [creating landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/)
- Familiarity with [creating drag-and-drop in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/)

## Creating a survey

During beta, surveys are built inside your existing message composition flow.

1. Go to **Messaging** and choose **Landing Pages**, or create an in-app message in a campaign or Canvas.
2. Create a new message.
3. Select **Survey** as your message type.

## Composing an in-app message survey

In-app message surveys start with two pages by default:

- **Page 1**, where consumers answer questions
- **Confirmation page**, where the survey is submitted

By default, buttons are linked to **Next page**. To change this behavior, update each button in the **Actions** panel.

_Image placeholder: In-app message survey page flow and action settings._

## Using survey form blocks

For shared styling and composition controls, refer to:

- [In-app message drag-and-drop editor blocks]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/)
- [Landing page form blocks]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#form-blocks)

You can add the following form blocks to surveys:

- Phone capture
- Email capture
- Radio button group
- Short text capture
- Long text capture
- Dropdown
- Single checkbox
- Checkbox group

### Long text capture

Long text capture is useful for qualitative feedback.

You can configure:

- Minimum and maximum character counts (up to `1000`)
- Whether to show character limits during composition
- Text area height (rows)
- Placeholder text

During beta, long text responses are available in reporting and exports, but they can't be logged as user profile custom attributes.

_Image placeholder: Long text capture block settings._

## Configuring required fields and attributes

For each form block, enter an **Identifier for Reporting** in the right-side settings panel. This identifier appears in survey reporting and CSV exports.

During beta:

- You can log most survey responses to user profile custom attributes.
- Long text responses can't be logged as custom attributes.
- If you choose not to log a response as a user attribute, you can't segment users by that response value.

_Image placeholder: Identifier for Reporting and attribute logging settings._

## Viewing reporting and analytics

After launch, review results in:

- The **Responses** tab for in-app message surveys
- The landing page analytics view for landing page surveys

Top-level analytics include:

- **All responses**: Total complete and incomplete responses
- **Completed**: Users who completed all required questions
- **Partially complete**: Users who submitted some data, but did not complete all required questions
- **Unique impressions**: Total page views

{% alert note %}
Landing page surveys do not track partially complete responses during beta.
{% endalert %}

You can also review per-question response breakdowns and export data as CSV.

_Image placeholder: Survey analytics overview and question-level breakdown._

## Retargeting and triggering

During beta, you can:

- Trigger campaigns and Canvases when a user completes a survey
- Segment users by survey completion status
- Segment users by survey responses that are logged as user attributes

Limitations during beta:

- You can't segment users by long text responses.
- Question-and-answer triggering that does not rely on logged user attributes is not available.

_Image placeholder: Trigger setup and segmentation filters for survey follow-up._
