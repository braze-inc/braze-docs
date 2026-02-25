# "Create a {{Channel}}" article template

> Reusable structural template for all messaging channel "Create a..." articles.
> Each article covers **channel-specific configuration only**. General content lives elsewhere:
>
> - Campaign setup → Campaign creation docs
> - Canvas setup → Canvas creation docs
> - Editor-specific instructions → Editor reference articles (drag-and-drop email, drag-and-drop general, HTML email, traditional composers)
> - Audience, delivery, conversion steps → Campaign and Canvas creation docs

---

## Frontmatter

```yaml
---
nav_title: "Create a {{Channel}}"
article_title: "Create a {{Channel}}"
page_order: {{integer}}
description: "Learn how to configure and compose {{Channel}} messages in Braze."
tool:
  - Campaigns
  - Canvas
  # For transactional email, remove Canvas (API-triggered only).
channel:
  - {{channel_slug}}
---
```

---

## Article body

````markdown
# Create a {{Channel}}

> {{1-3 sentence intro. State what this article covers and link to the channel's
> "About" page for general information.}}


## Prerequisites

Before you start, make sure you have the following:

| Requirement | Description |
|---|---|
| Campaign or Canvas | A [campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/campaign_basics/) or [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/). |
| {{Channel-specific requirement}} | {{Description of any channel-specific prerequisite, such as SDK setup, placements, subscription groups, approved templates, or partner configuration.}} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


<!-- ============================================================
     CHANNEL-SPECIFIC SETTINGS OUTSIDE COMPOSITION
     ============================================================
     One or more H2 sections for settings that exist independent of
     the message editor. These vary by channel. Examples:

     - Banners: Placements, Priority, Expiration
     - Content Cards: Card types, Expiration
     - Email: Editing experience (DnD vs. HTML), Sending information, Subject line and preheader
     - In-app messages: Editing experience (DnD vs. traditional), Delivery platforms, Message types
     - Push: Push platforms, Notification type
     - Webhook: Webhook URL, HTTP method, Request headers
     - WhatsApp: Message type (template vs. response)
     - SMS/MMS/RCS: Subscription group

     Use descriptive H2 headings (not numbered steps).
     Where Campaign and Canvas behavior diverges, use H3 subsections:

     ### Campaign
     ...
     ### Canvas
     ...

     Only include these subsections when there is a meaningful difference.

     For steps that live in campaign/Canvas docs, cross-reference the
     specific child page:
     - Delivery/scheduling → Schedule your campaign / Canvas delivery settings
     - Audience/targeting → Campaign basics / Canvas targeting
     - Conversions → Campaign basics / Canvas conversions
     ============================================================ -->

## {{Setting name}}

{{Description of the setting and how to configure it.}}

### Campaign

{{Campaign-specific behavior, if different.}}

### Canvas

{{Canvas-specific behavior, if different.}}


## Composition

<!-- When a single article covers multiple message types with distinct
     composition flows (e.g., SMS vs. MMS vs. RCS, or template vs. response
     messages), use {% tabs %} to organize the content within this section.
     Don't nest tabs. -->

{{1-2 sentence intro. Cross-reference the relevant editor reference article.}}

For details on using the {{editor name}} editor, see [{{Editor reference title}}]({{site.baseurl}}/...).

### Content

{{Brief description of what content elements this channel supports.
List available blocks, message types, or content fields.
Link to the editor reference for step-by-step instructions.}}

### Style

{{Brief list of available style elements or design options for this channel.
Link to the editor reference for full details on using them.}}

Banners support the following elements:

- {{Element 1}}
- {{Element 2}}
- ...

For details on styling your message, see [{{Editor reference title}}]({{site.baseurl}}/...).

### {{Interactions heading}}

<!-- Use the heading that fits the channel:
     - "On-click behavior" for Banners, Content Cards, in-app messages
     - "Actions" for push notifications
     - "Call-to-action types" for WhatsApp
     - "Suggested replies and actions" for RCS
     - Omit entirely if the channel has no interactive elements (e.g., basic SMS) -->

{{Description of how users interact with the message and what actions
are available. Include tables for action types where applicable:}}

| Action | Description |
|---|---|
| {{Action name}} | {{What happens when the user takes this action.}} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


<!-- ============================================================
     CHANNEL-SPECIFIC SETTINGS INSIDE COMPOSITION
     ============================================================
     One or more H2 sections for settings accessible within the
     composer that are unique to this channel. Examples:

     - Banners: Custom properties
     - Content Cards: Key-value pairs, Pinning
     - Email: Email headers, Email extras
     - In-app messages: Key-value pairs, iOS device options
     - Push: Platform-specific options (sounds, badges, channels)
     - Transactional email: One-click list-unsubscribe

     Omit this section entirely if the channel has no such settings.
     ============================================================ -->

## {{Setting name}}

{{Description and configuration instructions.}}


<!-- ============================================================
     THINGS TO KNOW (OPTIONAL)
     ============================================================
     Include channel-specific reference material that doesn't fit
     into the configuration or composition sections above. Examples:

     - Content Cards: Payload/feed limitations, re-eligibility, managing live cards
     - Email: Validation errors
     - In-app messages: Active campaign limits, local time delivery
     - Webhooks: Errors/retry logic/timeouts, IP allowlisting
     - WhatsApp: Supported features tables

     Use "Things to know" as the default heading. Use a more specific
     H2 only when the section covers a single focused topic (e.g.,
     "Email validation errors").
     Omit this section entirely if the channel has no supplementary notes.
     ============================================================ -->

## Things to know

{{Reference material that doesn't fit into the sections above. Use H3
sub-sections to organize multiple topics.}}


## Next steps

After composing your {{Channel}} message, continue setting up your
[campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) or
[Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/):

- [Delivery and entry types]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/delivery_types/)
- [Send test messages]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) (campaigns) or [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) (Canvas)
````

---

## Structural rules

1. **No numbered steps.** Use descriptive H2/H3 headings.
2. **Campaign/Canvas subsections only where behavior diverges.** Don't repeat shared instructions under both headings.
3. **Cross-reference, don't duplicate.** Link to the editor reference article for editor-specific details. Link to the specific campaign child page (Campaign basics, Schedule your campaign, Test campaigns, or Manage campaigns) or Canvas creation docs for audience, delivery, and conversion steps.
4. **Style section lists elements briefly.** Enumerate the available blocks or style options for the channel, then link to the editor reference for how to use them.
5. **Interactions heading varies by channel.** Choose the heading that best describes the channel's interactive behavior (see comment in template).
6. **Alerts sparingly.** Use `{% alert %}` tags for early-access notices, deprecation warnings, or SDK version requirements. Don't stack two alerts in a row. Place early-access and beta notices immediately after the intro paragraph. Place SDK version requirements inline with the setting they apply to.
7. **Tables for structured data.** Use tables (with `{: .reset-td-br-1 ... }` classes) for prerequisites, action types, property fields, and specification lists.
8. **Images with alt text.** Use `{% image_buster %}` tags. Alt text should be descriptive, plain language, sentence case.
9. **Use tabs for parallel message types within one article.** When a single article covers multiple message types with distinct composition flows (e.g., SMS vs. MMS vs. RCS, or template vs. response messages), use `{% tabs %}` to organize the content. Don't nest tabs.
10. **"Things to know" is the default heading for supplementary reference material.** Use a more specific H2 only when the section covers a single focused topic (e.g., "Email validation errors"). If mixing topics, use "Things to know" with H3 sub-sections.

## Editor reference mapping

Each channel maps to one or more editor reference articles:

| Channel | Editor type | Editor reference article |
|---|---|---|
| Banner | Drag-and-drop (general) | _TBD_ |
| Content Card | Traditional composer | _TBD_ |
| Email | Drag-and-drop (email) **or** HTML email | _TBD_ (two articles) |
| Transactional email | Drag-and-drop (email) **or** HTML email | _TBD_ (two articles) |
| In-app message | Drag-and-drop (general) **or** Traditional composer | _TBD_ (two articles) |
| LINE | Traditional composer | _TBD_ |
| Webhook | Traditional composer | _TBD_ |
| Push notification | Traditional composer | _TBD_ |
| WhatsApp | Traditional composer | _TBD_ |
| SMS, MMS, RCS | Traditional composer | _TBD_ |
