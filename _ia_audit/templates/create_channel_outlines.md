# Per-channel outlines: "Create a {{Channel}}" articles

> Maps existing article content to the standardized template structure.
> For the template itself, see [create_channel_template.md](create_channel_template.md).
>
> **Legend**
>
> - **Keep** = Content stays in the channel article (channel-specific)
> - **Move to editor ref** = Content moves to the relevant editor reference article
> - **Remove** = Content is general campaign/Canvas creation; handled elsewhere
> - Source file paths are relative to `_docs/_user_guide/message_building_by_channel/`

---

## 1. Create a Banner

**Source:** [`banners/create.md`](../../_docs/_user_guide/message_building_by_channel/banners/create.md)
**Editor:** Drag-and-drop (general)

### Prerequisites

| Requirement | Description |
|---|---|
| Campaign or Canvas | Create before composing your Banner. |
| Placements | Development team must [set up placements]({{site.baseurl}}/developer_guide/banners/creating_placements/) in your app or website. |

### Channel-specific settings outside composition

#### Placements

Keep the existing content about placements being unique app/site locations and selecting a placement for the campaign. Include the `multi_lang_include` for placement selection.

#### Priority

Keep. Explain the three priority levels (high, medium, low) and how Banners sharing a placement are ordered.

| Subsection | Content |
|---|---|
| **Campaign** | In the Schedule Delivery step, set a Message Priority or use the drag-and-drop priority sorter to define exact priority. |
| **Canvas** | Priority is set in the Message step configuration. |

#### Expiration

Keep. Banners last indefinitely by default.

| Subsection | Content |
|---|---|
| **Campaign** | Select **End Time** and specify an end date and time. |
| **Canvas** | Set an expiration as a duration after the step is available or at a specific date and time. |

### Composition

Intro: Compose your Banner by starting with a blank template, a Braze banner template, or a saved banner template. Link to the drag-and-drop (general) editor reference for step-by-step editing instructions.

#### Content

Keep the template selection options (blank, Braze template, saved template) and the image of the template chooser.

#### Style

Brief list of available elements, then link to editor reference:

- Tile
- Paragraph
- Button
- Image
- Link
- Spacer
- Custom Code
- Phone Capture
- Email Capture

Keep the note about customizing background properties, border settings through the **Styles** panel. Move detailed block-by-block editing instructions to the editor reference.

#### On-click behavior

Keep all existing content:

- Navigate deeper into app or redirect to another webpage
- Log a custom attribute or event
- **Overriding click events** alert: element-level on-click overrides Banner-level on-click

### Channel-specific settings inside composition

#### Custom properties

Keep all existing content:

- Description of structured metadata (strings, JSON objects)
- Use cases: third-party analytics, conditional logic, banner behavior control
- Navigation: **Settings** > **Properties** > **Add property**
- Property fields table (Property type, Property key, Value)
- Images of properties UI

### Next steps

Standard cross-references to campaign/Canvas setup, delivery, and testing docs.

### Content removed (handled elsewhere)

| Removed section | Destination |
|---|---|
| Step 2: Choose where to build your message (Campaign/Canvas tabs) | [Campaign basics]({{site.baseurl}}/user_guide/engagement_tools/campaigns/campaign_basics/) / [Create a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) |
| Step 4: Build the remainder (audience, conversions) | [Schedule your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) / Canvas delivery settings |
| Step 5: Test your message | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |
| Step 6: Review and deploy | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |

---

## 2. Create a Content Card

**Source:** [`content_cards/create.md`](../../_docs/_user_guide/message_building_by_channel/content_cards/create.md)
**Editor:** Traditional composer

### Prerequisites

| Requirement | Description |
|---|---|
| Campaign or Canvas | Create before composing your Content Card. |

### Channel-specific settings outside composition

#### Card types

Keep the card type selection and table:

- **Classic** -- Straightforward layout with bolded title, message text, optional left-aligned image
- **Captioned Image** -- Content with copy and attention-grabbing image
- **Image Only** -- Space for images, GIFs, and other non-text content

Include the existing images and link to [Creative Details]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/).

#### Expiration

Keep. Content Cards expire after up to 30 days. Include:

- Setting a specific expiration date or days until expiry (up to 30 days)
- All variants share identical expiration dates
- Tip about Banners for content lasting longer than 30 days

### Composition

Intro: Compose your Content Card in the **Compose** tab. Content varies based on the card type selected. Link to the traditional composer editor reference.

#### Content

Keep from existing article:

- **Language** -- Add Languages button, Liquid insertion, right-to-left messages reference
- **Title and message** -- Custom copy, not available for Image Only cards
- **Image** -- Add Image or provide URL, media library, 2 KB total payload limit

#### On-click behavior

Keep the full on-click behavior section:

- Redirect to Web URL
- Deep Link into App
- Log Custom Event
- Log Custom Attribute

Include the SDK minimum versions note (`{% sdk_min_versions %}`).

#### Pin to top

Keep the existing pinning content:

- Pinned cards appear at top of feed
- User can't dismiss pinned cards
- Can't retroactively update pinned option after send

### Channel-specific settings inside composition

#### Key-value pairs

Keep. Link to key-value pairs documentation. Describe use for creating card categories, multiple Content Card feeds, and custom sort orders.

### Things to know

Keep the full "Things to know" section. This is channel-specific reference material with H3 sub-sections:

- **Payload and feed limitations** (2 KB payload limit, 250 card feed limit)
- **Re-eligibility for Content Cards** (re-eligibility calculation, 30-day expiration interaction)
- **Managing live Content Cards** (updating launched cards, removing/expiring cards)

### Next steps

Standard cross-references to campaign/Canvas setup, delivery, and testing docs.

### Content removed (handled elsewhere)

| Removed section | Destination |
|---|---|
| Step 1: Choose where to build your message | [Campaign basics]({{site.baseurl}}/user_guide/engagement_tools/campaigns/campaign_basics/) / [Create a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) |
| Step 5: Build the remainder (delivery, audience, conversions) | [Schedule your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) / Canvas delivery settings |
| Step 6: Review and deploy | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |

---

## 3. Create an email

**Sources:**
- [`email/html_editor/creating_an_email_campaign.md`](../../_docs/_user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign.md)
- [`email/drag_and_drop/overview.md`](../../_docs/_user_guide/message_building_by_channel/email/drag_and_drop/overview.md)

**Editors:** Drag-and-drop (email), HTML email

### Prerequisites

| Requirement | Description |
|---|---|
| Campaign or Canvas | Create before composing your email. |

### Channel-specific settings outside composition

#### Editing experience

Keep. Choosing between the drag-and-drop editor and HTML editor. Link to each editor reference for details on using the chosen editor.

#### Sending information

Keep from Step 3a. This is email-specific configuration:

- **From Display Name + Address** -- Select or customize
- **Reply-To Address** -- Select or customize
- **BCC Address** -- Make email visible to this address
- **Subject line** -- Required
- **Preheader** -- Optional, with whitespace tip

#### Inline CSS

Keep the toggle to turn on inline CSS (from **Sending Settings** > **Advanced**).

### Composition

Intro: Compose your email using the drag-and-drop editor or HTML editor. Link to both editor reference articles for step-by-step instructions.

#### Content

Brief note that content creation depends on the chosen editor. Link to:

- Drag-and-drop (email) editor reference
- HTML email editor reference

Keep the note about HTML, classic, plaintext, and AMP tabs. Keep the "Regenerate from HTML" plaintext sync behavior.

#### Style

Brief note that styling depends on the chosen editor. Link to editor references.

### Channel-specific settings inside composition

#### Email headers

Keep from Step 3a > Advanced. This is email-specific:

- Adding custom headers (key-value pairs)
- Reserved fields table (BCC, CC, Content-Transfer-Encoding, Content-Type, DKIM-Signature, From, MIME-Version, Received, Reply-To, Subject, To, x-sg-eid, x-sg-id)

#### Email extras

Keep from Step 3a > Advanced:

- Send additional data to other email service providers
- Key-value pairs must not exceed 1 KB
- Not published to Currents or Snowflake (use `message_extras` Liquid filter instead)

### Email validation errors

Use a specific H2 heading (not "Things to know") since this section covers a single focused topic. Keep the list of errors the editor catches:

- From Display Name and Header not specified together
- Invalid From and Reply-To addresses
- Duplicate Header keys
- Liquid syntax problems
- Bodies larger than 400 KB
- Blank Body or Subject
- No unsubscribe link
- Non-allowlisted sending address

### Next steps

Standard cross-references to campaign/Canvas setup, delivery, and testing docs.

### Content removed (handled elsewhere)

| Removed section | Destination |
|---|---|
| Step 1: Choose where to build your message | [Campaign basics]({{site.baseurl}}/user_guide/engagement_tools/campaigns/campaign_basics/) / [Create a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) |
| Step 3b: Preview and test your message | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |
| Step 4: Build the remainder (delivery, audience, conversions) | [Schedule your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) / Canvas delivery settings |
| Step 5: Review and deploy | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |
| Detailed editor instructions (drag-and-drop blocks, HTML editing) | Editor reference articles |

---

## 4. Create a transactional email

**Source:** [`email/transactional_message_api_campaign.md`](../../_docs/_user_guide/message_building_by_channel/email/transactional_message_api_campaign.md)
**Editors:** Drag-and-drop (email), HTML email

### Prerequisites

| Requirement | Description |
|---|---|
| Transactional Email add-on | Contact your Braze customer success manager or open a support ticket. |

Note: This channel uses a simplified creation flow -- no delivery schedule, no target audiences, no conversion events.

### Channel-specific settings outside composition

#### API campaign setup

Keep. Core configuration:

- Creating a Transactional Email campaign type
- Noting the `campaign_id` for use with the `/transactional/v1/campaigns/{campaign_id}/send` endpoint
- Simplified flow explanation (no scheduling, no audience targeting, no conversions)

#### Disallowed Liquid tags

Keep. `Connected Content` and `Promotion Code` tags are unavailable:

- `Connected Content` makes outbound API requests that can add latency
- `Promotion Code` requires additional processing to evaluate availability

### Composition

Brief intro. Link to email editor references for composing the email body.

#### Content

Compose using a template or from scratch. Same editor options as standard email.

### Channel-specific settings inside composition

#### One-click list-unsubscribe

Keep. Defaults to **Use workspace default**. Braze doesn't add one-click unsubscribe by default for transactional emails.

### Next steps

Transactional email uses a simplified flow. The Next steps section should link to the [Transactional Email endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) for API triggering, rather than the standard campaign/Canvas setup links.

### Content removed (handled elsewhere)

| Removed section | Destination |
|---|---|
| General campaign creation steps | [Campaign basics]({{site.baseurl}}/user_guide/engagement_tools/campaigns/campaign_basics/) |
| Editor instructions | Editor reference articles |

---

## 5. Create an in-app message

**Sources:**
- [`in-app_messages/traditional/create.md`](../../_docs/_user_guide/message_building_by_channel/in-app_messages/traditional/create.md)
- [`in-app_messages/drag_and_drop/create.md`](../../_docs/_user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create.md)

**Editors:** Drag-and-drop (general), Traditional composer

### Prerequisites

| Requirement | Description |
|---|---|
| Campaign or Canvas | Create before composing your in-app message. |
| SDK requirements (drag-and-drop) | Minimum SDK versions for drag-and-drop: Swift 5.13.0+, Android 26.0.0+, Web 4.9.0+. Additional requirements for web (`allowUserSuppliedJavascript`). |

### Channel-specific settings outside composition

#### Delivery platforms

Keep. Platform selection table:

| Platform | Message Delivery |
|---|---|
| Mobile Apps | iOS and Android SDKs |
| Web Browsers | Web SDK |
| Both Mobile Apps and Web Browsers | iOS, Android, and Web SDKs |

#### Message types

Keep the full message types section. This is core to the channel:

**Standard types** (accepted by both mobile and web):

- **Fullscreen** -- Image and Text, Image Only. Enforced device orientation.
- **Modal** -- Text (with optional image), Image Only.
- **Slideup** -- Minimal screen coverage.

**Advanced types:**

- Custom HTML Message
- Email Capture Form
- Web Modal with CSS (Web SDK only)

#### Message close

Keep:

- Dismiss Automatically (set seconds)
- Wait for User Swipe or Touch

#### Slideup position (slideup type only)

Keep: From Bottom of App Screen or From Top of App Screen.

### Composition

Intro: Compose your in-app message in the **Compose** tab. Link to the relevant editor reference (drag-and-drop general or traditional composer).

#### Content

Keep from existing articles:

- **Language** -- Add Languages, Liquid insertion
- **Image** -- Upload Image, Pick a Badge, Font Awesome, media library
- **Header and body** -- Custom copy with HTML capabilities, Liquid personalization
- **Buttons** -- Up to two buttons, custom text and color, Terms of Service link for email capture

#### Style

Keep the style options table:

- Color Profile (from templates gallery)
- Text Alignment (left, center, right)
- Header, Text, Buttons, Button Border, Background Color, Screen Overlay, Chevron/Close -- all HEX color codes with opacity

Link to editor reference for detailed styling instructions.

#### On-click behavior

Keep the full on-click behavior table:

| Action | Description |
|---|---|
| Redirect to Web URL | Open a non-native web page. |
| Deep Link into App | Deep link into an existing screen. |
| Close Message | Closes the currently active message. |
| Log Custom Event | Trigger a custom event. |
| Log Custom Attribute | Set a custom attribute. |
| Request Push Permission | Show native push permission prompt. |

Include SDK minimum versions.

### Channel-specific settings inside composition

#### Key-value pairs

Keep. Send extra custom fields to user devices.

#### iOS device options

Keep. Restrict to iOS devices only.

### Things to know

Keep with H3 sub-sections:

- **Active in-app message campaign limits** -- 200 active action-based IAM campaigns per workspace
- **Local time delivery evaluation** -- Device-side evaluation of campaign start/end times

### Next steps

Standard cross-references to campaign/Canvas setup, delivery, and testing docs.

### Content removed (handled elsewhere)

| Removed section | Destination |
|---|---|
| Step 1: Choose where to build your message | [Campaign basics]({{site.baseurl}}/user_guide/engagement_tools/campaigns/campaign_basics/) / [Create a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) |
| Step 7: Build the remainder (triggers, priority, audience, conversions) | [Schedule your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) / Canvas delivery settings |
| Step 8: Review and deploy | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |
| Drag-and-drop editor specifics (blocks, rows, templates, multi-page flows) | Drag-and-drop (general) editor reference |
| HTML and assets (Custom code type) | Traditional composer editor reference |

---

## 6. Create a LINE message

**Source:** [`line/create.md`](../../_docs/_user_guide/message_building_by_channel/line/create.md)
**Editor:** Traditional composer

### Prerequisites

| Requirement | Description |
|---|---|
| Campaign or Canvas | Create before composing your LINE message. |
| LINE channel setup | Read the LINE overview, acknowledge policies, and [set up your LINE connection]({{site.baseurl}}/user_guide/message_building_by_channel/line/line_setup/). |

### Channel-specific settings outside composition

#### Message Credits

Keep the note that sending LINE messages draws from your account's Message Credits.

### Composition

Intro: Compose your LINE message using personalization as needed. LINE allows up to five message bubbles per message. Link to the traditional composer editor reference.

#### Content

Keep:

- **Message bubbles** -- Up to five per message, with layouts: text, image, rich, or card-based
- **Liquid and Connected Content** -- Use for personalization
- **Right-to-left messages** -- Link to best practices
- **Dynamic image URL** alert

#### Style

Not applicable for LINE. The traditional composer for LINE does not have a separate style panel.

### Channel-specific settings inside composition

None.

### Next steps

Standard cross-references to campaign/Canvas setup, delivery, and testing docs.

### Content removed (handled elsewhere)

| Removed section | Destination |
|---|---|
| Step 1: Choose where to build your message | [Campaign basics]({{site.baseurl}}/user_guide/engagement_tools/campaigns/campaign_basics/) / [Create a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) |
| Step 3: Preview and test your message | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |
| Step 4: Build the remainder (delivery, audience, conversions) | [Schedule your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) / Canvas delivery settings |
| Step 5: Review and deploy | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |

---

## 7. Create a webhook

**Source:** [`webhooks/creating_a_webhook.md`](../../_docs/_user_guide/message_building_by_channel/webhooks/creating_a_webhook.md)
**Editor:** Traditional composer

### Prerequisites

| Requirement | Description |
|---|---|
| Campaign or Canvas | Create before building your webhook. |

### Channel-specific settings outside composition

#### Webhook URL

Keep all existing content:

- The URL/HTTP endpoint where information is sent
- Vendor-provided URL or internal systems URL
- Standard ports only (80 for HTTP, 443 for HTTPS)
- Personalizing URLs with Liquid (include default values)

#### HTTP method

Keep. Method varies by endpoint; POST is most common.

#### Request headers

Keep from Step 3:

- Adding headers in the **Compose** section
- Common headers: `Content-Type` (application/json, application/x-www-form-urlencoded) and `Authorization` (Bearer, Basic)
- Reserved/system headers

### Composition

Intro: Build your webhook from scratch, from an existing template, or from a Braze template. Link to the traditional composer editor reference.

#### Content

Keep the request body content:

- **JSON key-value pairs** -- For endpoints expecting JSON format. Personalize with Liquid.
- **Raw text** -- For any body format (XML, URL-encoded, etc.). Supports Liquid and internationalization.
- **Language/internationalization** -- Supported in URL and request body. Add Languages button.

### Channel-specific settings inside composition

None.

### Things to know

Keep with H3 sub-sections:

- **Errors, retry logic, and timeouts** -- Error types, response codes table (20x, 30x, 408, 429, 4XX, 5XX), retry behavior, 90-second timeout
- **IP allowlisting** -- Braze IP addresses for webhook requests, instructions for allowlisting
- **Using webhooks with Braze partners** -- Links to partner integrations

### Next steps

Standard cross-references to campaign/Canvas setup, delivery, and testing docs.

### Content removed (handled elsewhere)

| Removed section | Destination |
|---|---|
| Step 1: Choose where to build your message | [Campaign basics]({{site.baseurl}}/user_guide/engagement_tools/campaigns/campaign_basics/) / [Create a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) |
| Step 4: Test send your message | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |
| Step 5: Build the remainder (delivery, audience, conversions) | [Schedule your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) / Canvas delivery settings |
| Step 6: Review and deploy | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |

---

## 8. Create a push notification

**Source:** [`push/creating_a_push_message.md`](../../_docs/_user_guide/message_building_by_channel/push/creating_a_push_message.md)
**Editor:** Traditional composer

### Prerequisites

| Requirement | Description |
|---|---|
| Campaign or Canvas | Create before composing your push notification. |

### Channel-specific settings outside composition

#### Push platforms

Keep the full platform selection section:

- Choose platform and device combinations to limit delivery
- Quick push vs. multichannel vs. Canvas differences table
- Quick push campaign limitations (no push action buttons, notification channels, TTL, display priority, sounds)

#### Notification type

Keep (iOS and Android):

- Standard push
- Push stories (link to dedicated article)
- Inline image (Android only)
- Rich notifications links (iOS and Android)

#### Sending options

Keep:

- Send to all devices vs. most recently used device
- iOS device filtering (iPad only or iPhone/iPod only)

### Composition

Intro: Compose your push notification in the **Compose** tab. Content varies based on notification type. Link to the traditional composer editor reference.

#### Content

Keep from existing article:

- **Notification channel or group** (iOS and Android) -- Link to platform-specific notification options
- **Language** -- Add Languages, right-to-left messages
- **Title and body** -- Plain text, Liquid personalization. Android requires a title (or single space for silent push).
- **Image** -- App icon as default, rich notifications for additional media

#### On-click behavior

Keep:

- Open app, redirect to web URL, deep link
- Button prompts: Accept/Decline, Yes/No, Confirm/Cancel, More

### Channel-specific settings inside composition

#### Platform-specific options

These settings are unique to push and vary by platform. Content from the existing article references platform-specific notification option pages:

**iOS:**
- Sounds
- Badges
- Interruption level
- Relevance score

**Android:**
- Notification channels and groups
- Priority / display priority
- Sounds
- Visibility
- Time-to-live (TTL)

Link to [iOS Notification Options]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/) and [Android Notification Options]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_options/) for full details.

### Next steps

Standard cross-references to campaign/Canvas setup, delivery, and testing docs.

### Content removed (handled elsewhere)

| Removed section | Destination |
|---|---|
| Step 1: Choose where to build your message (incl. quick push decision chart) | [Campaign basics]({{site.baseurl}}/user_guide/engagement_tools/campaigns/campaign_basics/) / [Create a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) |
| Step 5: Preview and test your message | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |
| Step 6: Build the remainder (delivery, audience, conversions) | [Schedule your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) / Canvas delivery settings |
| Step 7: Review and deploy | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |
| Multichannel campaigns with email and push | [Campaign basics]({{site.baseurl}}/user_guide/engagement_tools/campaigns/campaign_basics/) |

---

## 9. Create a WhatsApp message

**Source:** [`whatsapp/whatsapp_campaign/create.md`](../../_docs/_user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create.md)
**Editor:** Traditional composer

### Prerequisites

| Requirement | Description |
|---|---|
| Campaign or Canvas | Create before composing your WhatsApp message. |
| WhatsApp channel setup | Complete the [WhatsApp overview]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/): acknowledge policies, set up connection, build initial templates in Meta. |
| Approved message templates | For business-initiated conversations, create and get approval for [WhatsApp templates]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates). |

### Channel-specific settings outside composition

#### Message type

Keep. Two fundamental message types:

- **Template message** -- Business-initiated conversations using pre-approved Meta templates. Must be submitted for WhatsApp approval (up to 24 hours). Edits require reapproval.
- **Response message** -- Replies to inbound user messages within a 24-hour window. Built directly in Braze. Editable at any time.

#### Subscription group

Keep the note that selecting a subscription group is part of the WhatsApp message setup.

#### Languages (template messages)

Keep. Each template has an assigned language, requiring a separate campaign or Canvas step per language.

### Composition

Intro: Compose your WhatsApp message as a template message or response message. Link to the traditional composer editor reference.

#### Content

**Template messages:**
- Variables -- Replace blank spaces with Liquid or plain text
- Disabled text fields -- Part of the approved template, can't be edited in Braze
- Dynamic links -- CTA URLs with variables, link shortening and tracking
- Dynamic images -- Image URL support

**Response messages:**
Five available layouts:
- Quick Reply
- Text Message
- Media Message
- Call-to-action Button
- List Message

#### Call-to-action types

Keep the full CTA types table:

| CTA type | Details |
|---|---|
| Visit website | One button maximum (including variable parameters). |
| Call phone number | Templates only. One button maximum. |
| Custom quick reply buttons | Three buttons maximum. |
| Marketing opt-out button | Subscription status handling link. |
| Coupon code message templates | Templates only. Compatible with Liquid and Braze promotion codes. |
| CTA response messages | Response messages with a CTA button. |
| List response messages | Response messages with up to 10 options. |

### Channel-specific settings inside composition

None.

### Things to know

Use "Things to know" as the heading (multiple sub-topics):

- **Supported outbound message features** -- Feature table with file format and size specifications
- **Supported inbound message features** -- Feature table with supported formats

### Next steps

Standard cross-references to campaign/Canvas setup, delivery, and testing docs.

### Content removed (handled elsewhere)

| Removed section | Destination |
|---|---|
| Step 1: Choose where to build your message | [Campaign basics]({{site.baseurl}}/user_guide/engagement_tools/campaigns/campaign_basics/) / [Create a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) |
| Step 3: Preview and test your message | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |
| Step 4: Build the remainder (delivery, audience, conversions) | [Schedule your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) / Canvas delivery settings |
| Step 5: Review and deploy | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |

---

## 10. Create an SMS, MMS, or RCS message

**Sources:**
- [`sms_mms_rcs/sms/create.md`](../../_docs/_user_guide/message_building_by_channel/sms_mms_rcs/sms/create.md)
- [`sms_mms_rcs/mms/create.md`](../../_docs/_user_guide/message_building_by_channel/sms_mms_rcs/mms/create.md)
- [`sms_mms_rcs/rcs/create.md`](../../_docs/_user_guide/message_building_by_channel/sms_mms_rcs/rcs/create.md)

**Editor:** Traditional composer

### Prerequisites

| Requirement | Description |
|---|---|
| Campaign or Canvas | Create before composing your message. |
| Subscription group | An SMS/MMS/RCS-enabled [subscription group]({{site.baseurl}}/sms_rcs_subscription_groups/). For MMS, the subscription group must have MMS-enabled phone numbers. For RCS, the subscription group must have an RCS sender. |

### Channel-specific settings outside composition

#### Subscription group

Keep. Selecting a subscription group:

- Automatically adds a segmenting filter for subscribed users
- Only long codes and short codes in that subscription group are used for sending
- MMS requires an MMS-enabled subscription group
- RCS requires an RCS-enabled subscription group

#### Message type (RCS only)

Keep from RCS source. Choose between:

- **SMS/MMS** -- Standard text or multimedia message
- **RCS** -- Rich Communication Services message

Include the image of the message type selector.

#### SMS fallback (RCS only)

Keep. Braze strongly recommends that every RCS subscription group also includes at least one SMS code for fallback. Covers device incompatibility and incomplete carrier coverage.

### Composition

Intro: Compose your message in the traditional composer. The composition experience varies by message type. Link to the traditional composer editor reference.

Use `{% tabs %}` to organize content by message type:

#### SMS tab

**Content:**
- Text composition with Liquid, Connected Content, emojis
- Message segments and copy limits -- link to [SMS message segments]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/)
- Contact cards -- add business contact info; link to [Contact cards]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/)

**Tips:**
- Using Liquid (include default values)
- Generating AI copy
- Creating right-to-left messages

#### MMS tab

**Content:**
- Input PNG, JPEG, GIF, or VCF media from the media library or by URL
- One image per message
- Contact cards (vCard/VCF) -- programmatic or built-in generator

**Image specifications:**

| Specification | Recommended |
|---|---|
| Size | Up to 600 KB |
| File types | PNG, JPEG, GIF |

**Billing:** MMS billed at a different rate than SMS. Carriers that don't accept MMS will receive an image link instead (Twilio auto-conversion).

#### RCS tab

**Message types:**

**Text messages:**
- Up to 160 characters for basic (text-only) billing
- Up to 3,072 characters for rich (single) billing
- Suggested Replies (up to 5 buttons) -- pre-populated response options
- Suggested Actions (up to 5 buttons) -- initiate device actions (OpenURL)

**Media messages:**
- Everything available in text messages, plus:
- Image files (JPEG, PNG, GIF) via Media Library upload
- Video files (MP4, MPEG, M4V) via URL
- Document files (PDF) via URL

**File specifications:**

| File type | Specifications |
|---|---|
| All | Up to 100 MB, URL up to 2,048 characters |
| Image | JPG, JPEG, GIF |
| Video | H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Document | PDF |

**Considerations:** User experience varies by carrier, device hardware, and OS. RCS integrates more naturally with Android.

### Channel-specific settings inside composition

None.

### Next steps

Standard cross-references to campaign/Canvas setup, delivery, and testing docs.

### Content removed (handled elsewhere)

| Removed section | Destination |
|---|---|
| Step 1: Choose where to build your message (all three sources) | [Campaign basics]({{site.baseurl}}/user_guide/engagement_tools/campaigns/campaign_basics/) / [Create a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) |
| Step 3/4: Preview and test your message | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |
| Step 4/5: Build the remainder (delivery, audience, conversions) | [Schedule your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) / Canvas delivery settings |
| Step 5/6: Review and deploy | [Test campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) / [Test Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/) |

---

## Source file mapping summary

| New article | Existing source file(s) |
|---|---|
| Create a Banner | `banners/create.md` |
| Create a Content Card | `content_cards/create.md` |
| Create an email | `email/html_editor/creating_an_email_campaign.md` + `email/drag_and_drop/overview.md` |
| Create a transactional email | `email/transactional_message_api_campaign.md` |
| Create an in-app message | `in-app_messages/traditional/create.md` + `in-app_messages/drag_and_drop/create.md` |
| Create a LINE message | `line/create.md` |
| Create a webhook | `webhooks/creating_a_webhook.md` |
| Create a push notification | `push/creating_a_push_message.md` |
| Create a WhatsApp message | `whatsapp/whatsapp_campaign/create.md` |
| Create an SMS, MMS, or RCS message | `sms_mms_rcs/sms/create.md` + `sms_mms_rcs/mms/create.md` + `sms_mms_rcs/rcs/create.md` |
