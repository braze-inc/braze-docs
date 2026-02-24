# Comprehensive Assessment: Days 2-4

> **Context:** Day 1 (Administer + Data) is already done as PR #12255. Days 2-4 cover the remaining structural migration. Content work is deferred to Jira tickets for writers.
>
> **Guiding principle:** Restructure now if the section is coherent with existing content alone. Defer if it would create empty shells that only make sense once new content exists.

---

## Day 2 — Audience + Analytics (38 pages)

### Do now: 31 moves + 3 landing stubs

#### Moves — Audience (9 pages + child pages)

All of these exist today and are just changing location:

| Page | Current location |
|------|-----------------|
| Segments | `engagement_tools/segments.md` + all children |
| Global control group | `engagement_tools/testing/global_control_group.md` |
| Suppression lists | `engagement_tools/segments/suppression_lists.md` |
| User profiles | `engagement_tools/segments/user_profiles.md` + children |
| Import users | `data/unification/user_data/import_users.md` |
| Merge duplicate users | `engagement_tools/segments/user_profiles/duplicate_users.md` |
| Delete users | `data/unification/user_data/delete_users.md` |
| Preference center | `message_building_by_channel/email/preference_center.md` + children |
| Locations and geofences | `engagement_tools/locations_and_geofences.md` + children |

#### Moves — Analytics (~22 pages)

Nearly the entire Analytics section is an internal reshuffle — pages moving within `analytics/`:

| Page | Current location |
|------|-----------------|
| Dashboards landing | `analytics/dashboard.md` |
| Dashboard Builder | `analytics/reporting/dashboard_builder.md` → moves under Dashboards |
| Home, API usage, Channel performance, Conversions, Deliverability Center | `analytics/dashboard/` children (stay put) |
| Reports landing | `analytics/reporting.md` |
| Configure reporting, Engagement reports, Campaign analytics, Canvas analytics, Report Builder, Retention reports, Funnel reports, Revenue report, Global control group report | `analytics/reporting/` children (stay put) |
| Query Builder | `analytics/query_builder.md` → moves under Reports |
| Tracking landing + 4 children | `analytics/tracking/` (stays put) |

#### Landing stubs (3)

| Stub | Why it works now |
|------|-----------------|
| **Audience** (top-level) | 9 real pages moving underneath it |
| **Manage users** | Import, Merge, and Delete users all exist |
| **Subscription preferences** | Preference center exists; Subscription status and Groups are deferred |

### Defer to Jira: 5 items

| Page | Why defer |
|------|-----------|
| **Your audience** | Truly new article — "jumping off points for audience/user management." No existing equivalent |
| **Subscription status** | Content exists scattered in `managing_user_subscriptions.md` but needs extraction into a standalone page |
| **Subscription groups** | Content spread across email and SMS subscription docs — needs consolidation into a channel-agnostic page |
| **Use case: Segment with nested custom attributes** | Requires extracting the Segmentation section (lines 268-381) from `nested_custom_attribute_support.md` into a new article |
| **Metrics glossary merge** | Blocked on PM confirmation — combines Report metrics glossary with Email analytics glossary |

### Day 2 verdict

**Very comfortable.** 31 moves + 3 stubs. Audience pulls from 4 source directories, but each pull is just 1-3 pages. Analytics is almost entirely an internal reshuffle. Five deferred items become Jira tickets.

---

## Day 3 — Messaging (93 pages)

### Do now: 69 moves + 8 landing stubs + 3 deferred reworks

#### Moves (69 pages)

From three source directories:

- **`engagement_tools/`** — Campaigns, Canvas, Landing pages, Feature flags, Testing (→ A/B testing), Messaging fundamentals, Templates and media
- **`message_building_by_channel/`** — Editor pages (Email DnD, Email HTML, Image specs)
- **`personalization_and_dynamic_content/`** — Liquid, Connected Content, Promotion codes, Key-value pairs, Canvas entry properties, Context variables

#### Landing stubs (8)

| Stub | Why it works now |
|------|-----------------|
| **Messaging** (top-level) | All subsections below it have real content |
| **A/B testing** | All children exist under `engagement_tools/testing/` — just regrouping |
| **Reusable content** | Content Blocks and Product Blocks both exist |
| **Design and edit** | Email DnD tree, Email HTML tree, and Image specs are movable (3 of 5 children). The general DnD overview and Traditional composers don't exist yet — all 4 editor articles have consolidation rewrites as separate Jira tickets |
| **Personalize** | Liquid, Connected Content, and all Sources children (except User profile fields) exist |
| **Sources** | 6 of 7 children exist (REST API, Catalog, Promotion codes, Canvas entry properties, Context variables, Key-value pairs) |
| **Liquid reference** | Restructure of existing `liquid.md` + its children — content is there |
| **Connected content reference** | Restructure of existing `connected_content.md` + its children — content is there |

#### Existing pages moved with deferred content rework (3)

| Page | Move now | Rework later |
|------|----------|--------------|
| **Campaigns landing** | Move to new location | Rewrite content (currently "Getting started with campaigns") |
| **Media library** | Move to new location | Remove image specs section, fold in FAQ content |
| **Rate limiting & Frequency capping** | Move combined page to Rate limiting slot | Split Frequency capping into its own page later |

### Defer to Jira: 13 items

#### New articles (7)

| Page | Parent section | Notes |
|------|---------------|-------|
| **Priority sorter** | Messaging fundamentals | No existing standalone page |
| **Custom templates** (IAM) | Templates > In-app message templates | One new leaf page |
| **Dashboard tools** | Personalize | New article explaining the Add Personalization modal |
| **Preview personalization** | Personalize | New article pulling from test message docs |
| **User profile fields** | Personalize > Sources | Sources section works with its other 6 children |
| **Actions and media URLs** | Personalize | New article on personalizing URLs with Liquid |
| **Frequency capping** (standalone) | Messaging fundamentals | Requires splitting content from combined Rate limiting page |

#### Content reworks (2)

| Page | Type |
|------|------|
| **Campaigns landing rewrite** | Rewrite existing content |
| **Media library rework** | Remove image specs section, fold FAQ |

#### Cross-channel content consolidation (4)

These four "Design and edit" articles each require reshuffling significant content from multiple existing articles without any information being lost. They fall into two subcategories based on what exists today.

**Restructure existing article trees (2)** — Content exists but must be reshaped into a centralized editor-reference format:

| Article | Source articles | Wireframe scope |
|---------|---------------|-----------------|
| **Email drag-and-drop editor** | `email/drag_and_drop/overview.md`, `dnd_email_style_settings.md`, `faq.md`, `dnd_content_blocks.md` | Sending Settings (Sending info, Advanced), Content (Design and Build tabs: Content, Rows, Settings), Editor toolbar (Preview sizes, Editing history, Undo, Redo), Other tools (Personalization, Languages, Copywriter), Editor area (expanded inline text editor with strikethrough, background color, superscript, etc.; block action toolbar; row action toolbar), Properties panel, Link Management, Link templates, Preview and Test (Dark mode preview, Inbox Vision), Global actions (Cancel, Done, Operator, Style settings) |
| **Email HTML editor** | `email/html_editor/creating_an_email_campaign.md`, `css_inline.md`, `gmail_promotions_tab.md`, `troubleshooting.md` | Sending Settings (Sending info, Advanced, CSS inline), Content (Design and Build tabs), Editor toolbar (Editor mode, Add Image, Preview, Quick line, Code editor), Other tools, Main body covering 4 edit modes (HTML Default, Classic WYSIWYG, AMP, Drag-and-drop), Audiences, Properties panel, Live preview, Global action toolbar, Link Management, Link templates, Email Promotion, Email preview, Preview and Test (Send test messages, Send test as preview, Inbox Vision), Global actions (Queue/File, Done, Operator) |

**Create new by cross-channel extraction (2)** — No dedicated article exists today; must be built by extracting shared content from multiple channel articles:

| Article | Source articles | Wireframe scope |
|---------|---------------|-----------------|
| **Drag-and-drop editor** (general) | IAM (`in-app_messages/drag_and_drop/create.md`), Banners (`banners/create.md`), Landing Pages (`landing_pages/creating_pages.md`), Preference Centers (`email/preference_center/dnd_preference_center.md`), shared editor blocks (`messaging_fundamentals/drag_and_drop_editor_blocks.md`) | Editor sections (Compose/Build, Settings, Preview and Test), Compose section (Pages for IAM/pref center only, Rows, Blocks, Form blocks for pref center only), Editor toolbar (Undo, Redo, Preview sizes, Edit canvas size for Banners only, Hide outlines, Personalization), Editor area (inline text editor, block action toolbar, row action toolbar), Properties panel, Settings (Accessibility/Languages, Properties for Banners only), Preview and Test (Random User, Select User, Custom User, Send test messages), Global actions (Cancel, Done, Operator). Important: this editor is different from the email DnD editor. |
| **Message composers** (Traditional) | Push (`push/creating_a_push_message.md`), Content Cards (`content_cards/create.md`), LINE (`line/create.md`), SMS/MMS/RCS (`sms_mms_rcs/*/create.md`), IAM traditional (`in-app_messages/traditional/create.md`), WhatsApp (`whatsapp/whatsapp_campaign/create.md`), Webhooks (`webhooks/creating_a_webhook.md`) | Channels list, Composer anatomy (annotated screenshot), Message type (comprehensive table mapping types to channels), Live preview, Composer tabs, Content section (with per-channel variations), Description, Settings tab (with table of settings and availability), Contact Card/Promotion, Test tab. The most complex of the four — spans 7+ channel "create" articles. |

### Day 3 verdict

**Tight but doable.** The hardest day — two source directories, deepest restructure, most stubs. Map the target directory tree first thing in the morning. The moves will go fast once the structure is clear.

> **Day 3 / Day 4 dependency:** The 4 consolidation articles have a tight dependency with Day 4 (Channels). Creating them also requires updating the source channel articles — Push, Content Cards, LINE, SMS/MMS/RCS, IAM, WhatsApp, Webhooks, and Banners — to remove duplicated composer/editor content and cross-link to the new centralized articles instead. When writers pick up these Jira tickets post-migration, the channel article updates should be paired with the consolidation article in the same PR.

---

## Day 4 — Channels (132 pages)

### Do now: ~113 moves + 2 landing stubs + 6 deferred reworks

#### Moves (113 pages)

Nearly everything moves from `message_building_by_channel/` to `channels/`. The channel-level structure is largely preserved — children stay with their parents:

| Channel | Approx pages | Complexity |
|---------|-------------|------------|
| Banners | 4 | Low — clean 1:1 move |
| Content Cards | 7 | Low — clean 1:1 move |
| Email | ~30 | Medium — deep tree (setup, editors, templates, reporting, best practices) |
| In-app messages | ~15 | Medium — deep tree (traditional, DnD, creative details, reporting) |
| LINE | ~8 | Low |
| Push | ~20 | Medium — deep tree (iOS, Android, Web, advanced options, best practices) |
| SMS/MMS/RCS | ~15 | Medium — deep tree (setup, keywords, link shortening, user phone numbers) |
| Webhooks | 5 | Low |
| WhatsApp | ~15 | Medium — deep tree (setup, campaign, use cases, message processing) |

#### Landing stubs (2)

| Stub | Why it works now |
|------|-----------------|
| **Channels** (top-level) | All 9 channel sections land underneath with real content. The "In-product / Out-of-product" tile framing is new but the tiles link to existing pages |
| **Transactional email** | Both child pages (Create + Tracking) exist today under `email/`; just pulling them into their own section |

#### Existing pages moved with deferred content rework (6)

| Page | Move now | Rework later |
|------|----------|--------------|
| **Email landing** | Move the page | Add Email services content, remove source article |
| **Email FAQ** | Move the page | Fold in Duplicate emails, remove source article |
| **Push landing** | Move the page | Integrate Types of push as table |
| **Create a push message** | Move the page | Content update per proposal annotation |
| **Push Troubleshooting** | Move the page | Merge Common push error messages into this article |
| **LINE — Message users** | Move the page | Restructure child pages |

### Defer to Jira: 9 items

#### New articles (2)

| Page | Notes |
|------|-------|
| **Live notifications** | New marketer-facing overview of iOS Live Activities (developer docs exist, no marketer equivalent) |
| **Message types landing** (IAM) | New landing organizing message types into "All editors" vs "Traditional only" tiles |

#### Content merges and reworks (7)

| Page | Type |
|------|------|
| **Email landing content merge** | Merge Email services content into landing, remove source article |
| **Email FAQ merge** | Fold Duplicate emails into FAQ, remove source article |
| **Push landing rewrite** | Integrate Types of push as table |
| **Create a push message update** | Content update |
| **Push Troubleshooting merge** | Combine Common push error messages into this article |
| **LINE Message users restructure** | Reorganize child pages |
| **Webhooks Lead scoring** | Currently redirects to B2B lead scoring; may need webhook-specific article |

### Day 4 verdict

**High volume, low complexity.** The easiest day conceptually despite having the most pages. Almost everything is a directory-level move from `message_building_by_channel/X` to `channels/X` with the internal structure preserved. The pattern is repetitive and highly batchable. Only 2 stubs needed.

---

## Full picture across Days 1-4

### Structural work (ship in PRs)

| | Day 1 (done) | Day 2 | Day 3 | Day 4 | **Total** |
|--|-------------|-------|-------|-------|-----------|
| **Moves** | ~77 | 31 | 69 | 113 | **290** |
| **Landing stubs** | ~8 | 3 | 8 | 2 | **21** |
| **Pages moved with deferred rework** | — | 0 | 3 | 6 | **9** |
| **Scope** | **~85** | **34** | **80** | **121** | **320** |

### Content work (Jira tickets for writers)

| | Day 2 | Day 3 | Day 4 | **Total** |
|--|-------|-------|-------|-----------|
| **New articles** | 2 | 7 | 2 | **11** |
| **Content extractions/splits** | 2 | 0 | 0 | **2** |
| **Cross-channel consolidation** | 0 | 4 | 0 | **4** |
| **Merges/rewrites** | 1 | 2 | 7 | **10** |
| **Jira tickets** | **5** | **13** | **9** | **27** |

### What you ship in 8 days

**Days 1-4:** 4 PRs covering the entire User Guide restructure. Every existing page in its new home. 21 landing page stubs making the new navigation coherent. 9 pages moved to correct locations with content rework queued.

**Days 5-8:** QA each PR, merge to develop (smallest to largest: Administer+Data → Audience+Analytics → Messaging → Channels), create 27 Jira tickets for writers.

### What goes to Jira for writers

27 tickets total: 11 new articles, 2 content extractions, 4 cross-channel consolidations, 10 merges/rewrites. None of these block the structural migration — every section works without them. Writers can tackle these in any order once the PRs merge, though the 4 consolidation articles should be paired with updates to their source channel articles (see Day 3 dependency note).
