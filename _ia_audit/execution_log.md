# IA Migration Execution Log

> Tracks actual vs. estimated work for each day of Phase 1: "The Big Move" (Feb 23 – Mar 4).
>
> Reference: [IA Migration Execution Plan](https://docs.google.com/document/d/...) | [PR #12255](https://github.com/braze-inc/braze-docs/pull/12255)

---

## Day 1 — Administer + Data (Feb 23)

**Status:** Complete — PR #12255 open for review

### Estimated vs. actual

| | Estimated | Actual |
|--|-----------|--------|
| **Administer** | 40 pages, 4 stubs | 38 renames + 7 new files + 5 deletes = **50 file operations** |
| **Data** | 49 pages | 16 renames + 9 new files + 8 deletes + ~30 content edits = **63 file operations** |
| **Total files changed** | ~89 pages | **135 files** (54 renames, 16 new, 13 deletions, 52 content edits, 50+ redirects) |
| **Net lines** | — | 1,654 added, 2,657 removed |

### What went beyond the estimate

The original scope assumed structural moves and 4 landing page stubs. The actual work included significant content work that was done alongside the structural migration rather than deferred to Jira tickets:

- **Article splits:** Tags (split from Administer into Data > Activation), Data types (extracted from Custom attributes), Custom event properties (extracted from Custom events)
- **Article merges:** Troubleshooting into Accessing your account, Opening CSV reports in Excel into FAQs, Export revenue data into Revenue report
- **New articles:** Blocklist custom data, Custom events report (moved from Data > Distribution to Analytics > Reports and restructured), Managing custom data (rewritten to cover both events and attributes)
- **Landing page rewrites:** Data landing page (integrated content from deleted `braze_data_platform.md`), Attributes overview (new content covering standard + custom), Events overview (new content mentioning recommended events), Data Activation description (cohesive paragraph)
- **Content quality pass:** Copilot-assisted review for voice, tone, title casing, and cross-references (3 additional commits: #12256, #12259, #12260, #12261)
- **Misc fixes:** Renamed `manage_braze_users.md` to `manage_company_users.md`, removed outdated navigation alert

### What was intentionally deferred

- **Site-wide cross-reference updates:** Originally included (~170 files), then reverted. Will be handled in a final QA pass (Phase 3) after all IA restructuring is complete.

### Jira ticket impact

All 6 Jira tickets originally scoped for Administer and Data content work were completed as part of the Day 1 automation:

| Ticket | Title | Status |
|--------|-------|--------|
| BD-XXXX | Accessing your account (merge) | Done in PR |
| BD-XXXX | Attributes overview (new article) | Done in PR |
| BD-XXXX | Data types (new article) | Done in PR |
| BD-XXXX | Manage custom data (new article) | Done in PR |
| BD-XXXX | Blocklist custom data (new article) | Done in PR |
| BD-XXXX | Events landing page (rewrite) | Done in PR |

### Key lessons

1. **Content work surfaced during structural migration.** When you move files, you naturally see opportunities to split, merge, and improve content. Doing this alongside the structural work is more efficient than a separate pass, but it expands the scope of each day.
2. **Cross-reference updates should be deferred.** Updating 170+ files across the entire site for each workstream creates unnecessary churn. Better to batch these as a single QA pass at the end.
3. **Copilot-assisted quality passes add value but add commits.** Three additional PRs (#12256, #12259, #12260) improved content quality (parallelism between articles, voice/tone, cross-links) but extended the day.
4. **Plan for ~1.5x the estimated file operations.** The 89-page estimate became 135 files in practice. Factor this into Days 2–4.

---

## Day 2 — Audience + Analytics (Feb 24)

**Status:** Complete — PR [#12272](https://github.com/braze-inc/braze-docs/pull/12272) open for review

### Estimated vs. actual

| | Estimated | Actual |
|--|-----------|--------|
| **Audience** | ~16 pages from tracker | 31 files (3 new stubs + 28 moved from 4 source directories) |
| **Analytics** | ~22 pages from tracker | 28 files (renames + cross-section moves) |
| **Total files changed** | 38 pages, 5 stubs | **66 files** (58 renames, 3 new stubs, 1 redirect file, 4 _ia_audit files) |
| **Redirects** | — | 59 new entries + 81 existing destinations updated |

### What happened

- **Audience section created from scratch.** Pulled pages from `engagement_tools/segments/`, `engagement_tools/locations_and_geofences/`, `data/unification/user_data/`, `message_building_by_channel/email/preference_center/`, and `analytics/reporting/`.
- **Analytics reshuffle.** Renamed `dashboard/` → `dashboards/` and `reporting/` → `reports/`. Moved Dashboard Builder and Query Builder into their new parent sections. Renamed 4 dashboard files and 2 tracking files.
- **Day 1 gap fixed.** `viewing_and_understanding_segment_data.md` was supposed to move to `data/distribution/export_braze_data/segment_data.md` in Day 1 but was missed. Handled here.
- **3 tracker corrections identified.** Rows 140, 141, 143 had stale source paths that were corrected during execution.

### Deferred to Jira (5 items)

1. Your audience (new article)
2. Subscription status (content extraction)
3. Subscription groups (content consolidation)
4. Use case: Segment with nested custom attributes (content extraction)
5. Metrics glossary merge (blocked on PM)

---

## Day 3 — Messaging (Feb 25–26)

**Status:** Complete — PR [#12290](https://github.com/braze-inc/braze-docs/pull/12290) open for review

### Estimated vs. actual

| | Estimated | Actual |
|--|-----------|--------|
| **Scope** | 93 pages, 11 stubs | 179 renames + 10 new files + 12 deletes + 3 content edits = **204 file operations** |
| **Source sections** | `engagement_tools/`, `personalization_and_dynamic_content/`, partial `message_building_by_channel/` | Same + cross-section template consolidation |
| **Redirects** | — | +549 lines added, −175 lines removed in `broken_redirect_list.js` |
| **Net lines** | — | 564 added, 602 removed across `_docs/` |

### What happened

**Eight new subsections created under Messaging:**
1. **Messaging fundamentals** (17 files) — moved from `engagement_tools/messaging_fundamentals/` with renames (`delivery_types` → `delivery_and_entry_types`, `about_statuses` → `statuses`). Pulled in `frequency_capping` and `rate_limiting` from other locations.
2. **Campaigns** (33 files) — restructured during move: flattened `campaign_basics`, renamed `delivery_types` → `schedule_your_campaign`, `managing_campaigns` → `manage_campaigns`, `testing_and_more` → `test_campaigns`.
3. **Canvas** (58 files) — bulk moved as-is from `engagement_tools/canvas/`.
4. **Design and edit** — `editor_blocks` from messaging fundamentals, **Media library** (with Image specifications and FAQ nested under it).
5. **Content** — new parent section containing Personalize (30+ files from `personalization_and_dynamic_content/`), Templates (consolidated from 4 source locations), Content Blocks (merged two articles into one canonical), Product Blocks.
6. **A/B testing** (9 files) — assembled from `engagement_tools/testing/`, conceptual content integrated into landing page, new `variant_distribution.md` concept article.
7. **Feature flags** (5 files) — extracted from `canvas_components/`, children from `engagement_tools/feature_flags/`.
8. **Landing pages** (7 files) — moved from `engagement_tools/landing_pages/` with renames.

**Two top-level sections fully removed:**
- `engagement_tools/` — all content migrated to `messaging/`
- `personalization_and_dynamic_content/` — all content moved to `messaging/content/personalize/`

**Cross-section template consolidation:**
- Email templates moved from `message_building_by_channel/email/templates/`
- In-app message templates moved from `message_building_by_channel/in-app_messages/drag_and_drop/templates/`
- Webhook templates moved from `message_building_by_channel/webhooks/webhook_template`
- Canvas templates moved from `messaging/canvas/create_a_canvas/canvas_templates/`
- Content Block library merged with DnD Content Blocks into single canonical article

**Content quality work:**
- Removed duplicative image specs from media library, consolidated into dedicated child article
- Fixed broken Intelligent Selection link on A/B testing landing page
- Resolved 11 pre-existing redirect chains
- Fixed ~50 stale internal links across landing pages and key articles

### What was intentionally deferred

- **~230 bulk-moved file internal links:** Files moved from `engagement_tools/` still contain old-path internal links that resolve through redirects. Full cross-reference update deferred to Phase 3 QA pass.

### Deferred to Jira (6 items)

1. Priority sorter (new article)
2. Campaigns landing page rewrite
3. Drag-and-drop editor (new article)
4. Email drag-and-drop editor (new article)
5. Email HTML editor (new article)
6. Traditional composers (new article)

### Key lessons

1. **Template consolidation is the most complex work.** Moving templates from 4 different source locations (email, in-app, webhooks, Canvas) into a single Templates section required careful sequencing, multiple redirect updates, and landing page rewrites.
2. **Content merges require careful diffing.** Merging Content Block library and DnD Content Blocks into one canonical article required section-by-section comparison to avoid losing content. Always compare against production before finalizing.
3. **Media library and image specs had hidden duplication.** The media library article contained a full copy of channel-by-channel image specs. Deduplicating and linking to a canonical article was the right call.
4. **Landing page tile links are the most critical links to fix.** Stale links in article body text resolve through redirects, but stale tile links on landing pages break primary navigation. These should be prioritized in QA.
5. **1.5x multiplier from Day 1 held true.** The 93-page estimate became 204 file operations—about 2.2x. The additional complexity came from cross-section template consolidation and content merges that weren't in the original scope.

---

## Day 4 — Channels (Feb 27)

**Status:** Complete — branch `phase4-channels` ready for PR

### Estimated vs. actual

| | Estimated | Actual |
|--|-----------|--------|
| **Scope** | 132 pages, 11 stubs | 160 renames + 8 new stubs + 1 delete + 127 link fixes + 426 redirect lines = **218 files changed** |
| **Source section** | `message_building_by_channel/` | Same — fully emptied |
| **Target sections** | `channels/` + `channels/transactional_email/` | Same |
| **Redirects** | — | +426 new redirect lines, ~120 existing chain targets updated |
| **Net lines** | — | 1,432 added, 854 removed |

### What happened

**Nine channel sections created under Channels:**
1. **Banners** (5 files) — clean 1:1 move with `create` → `create_a_banner`, `analytics` → `reporting` renames.
2. **Content Cards** (9 files) — `create` → `create_a_content_card` rename, page_order updates.
3. **Webhooks** (6 files) — `creating_a_webhook` → `create_a_webhook`, two use case renames.
4. **LINE** (10 files) — `line_users/` restructured to `message_users/`, old landing page deleted, `messaging_users.md` promoted to section landing.
5. **In-app messages** (26 files) — `in-app_messages` (hyphen) → `in_app_messages` (underscore). `creative_details/` children moved to `message_types/`. `traditional/customize/` children split between `customize/` and `message_types/`. DnD and traditional editor trees preserved.
6. **Push** (30 files) — new `push_setup/` (token lifecycle + subscription states), new `platform_specific_resources/` (iOS/Android/Web), `creating_a_push_message` → `create_a_push_message`, `advanced_push_options/` children flattened into `create_a_push_message/`.
7. **Email** (43 files) — new `customize/` section (global styles, footer, AMP, universal links), `apple_mail/` moved under `best_practices/`, `reporting_and_analytics` renamed to `reporting`, transactional email extracted to own top-level section.
8. **SMS/MMS/RCS** (38 files) — `sms_mms_rcs` → `sms_mms_and_rcs`, new `message_setup/` section, new `message_features_and_optimization/` section (link shortening, keywords, retargeting, bot filtering), `segments` → `billing_calculator`, `campaign_analytics` → `reporting`.
9. **WhatsApp** (32 files) — `overview/` → `whatsapp_setup/`, new `whatsapp_phone_numbers/` section, new `message_features_and_optimization/` section, `whatsapp_campaign/` children distributed across create + features sections, message processing paths renamed for clarity.

**One top-level section fully removed:**
- `message_building_by_channel/` — all 160+ files migrated, landing page deleted, directory empty.

**One new top-level section created:**
- `transactional_email/` — extracted from `email/transactional_message_api_campaign/` with 2 child articles.

**8 landing page stubs created:**
- `channels.md` (top-level with tiles for all 10 subsections)
- `transactional_email.md`
- `push/push_setup.md`
- `push/platform_specific_resources.md`
- `email/customize.md`
- `sms_mms_and_rcs/message_features_and_optimization.md`
- `whatsapp/message_features_and_optimization.md`
- `whatsapp/whatsapp_setup/whatsapp_phone_numbers.md`

**Internal link fixes:**
- 127 files updated with ~449 stale link replacements (all `message_building_by_channel/` → `channels/` within moved files)
- Zero remaining references to old paths in `channels/` directory

**Redirect chain collapse:**
- ~120 existing redirect targets updated from `message_building_by_channel/` to `channels/` to prevent multi-hop chains

### Deferred to Jira (9 items)

1. Live notifications (new article — marketer-facing iOS Live Activities overview)
2. Message types landing (IAM) — new tile layout for "All editors" vs "Traditional only"
3. Email landing content merge — fold Email services into landing
4. Email FAQ merge — fold Duplicate emails into FAQ
5. Push landing rewrite — integrate Types of push as table
6. Create a push message update — content refresh per proposal annotation
7. Push Troubleshooting merge — combine Common push error messages
8. LINE Message users restructure — reorganize child pages
9. Webhooks Lead scoring — may need webhook-specific article

### Key lessons

1. **Batchable moves go fast.** Day 4 had the highest page count (132→160) but lowest conceptual complexity. The repetitive channel-by-channel pattern allowed parallel execution across all 9 channels.
2. **Directory renames compound link fixes.** The `in-app_messages` hyphen-to-underscore and `sms_mms_rcs` → `sms_mms_and_rcs` renames required fixing every internal cross-reference, not just within those sections but across all channels that link to them.
3. **Landing page stubs needed for subsection navigation.** The CSV identified 2 formal stubs, but 6 additional subsection landing pages were required for newly created directory structures (push_setup, platform_specific_resources, customize, message_features_and_optimization, whatsapp_phone_numbers).
4. **Chain collapse is critical at this scale.** With 281 existing redirects pointing to `message_building_by_channel/`, failing to collapse chains would have created 281 two-hop redirects on top of the new ones.

---

## Day 4 follow-up — Email section reorder + Jira item #4 (Feb 27)

**Status:** Complete — on branch `phase4-channels`

### What happened

**Email nav reorder:** Updated `page_order` frontmatter in 9 of 11 email landing pages (`email_setup.md` and `testing.md` were already correct). New order:

1. Email setup (1)
2. Drag-and-drop editor (2)
3. HTML editor (3)
4. Customize (4)
5. Subscriptions (5)
6. Testing (6)
7. Inbox Vision (7) — will be nested under "Create email" once writers create that article
8. Reporting (8)
9. Use cases (9)
10. Best practices (10)
11. FAQ (11)

**Jira item #4 — Email FAQ merge (Duplicate emails):**
- Folded `best_practices/duplicate_emails.md` content into `faq.md`: expanded the existing deduplication FAQ entry with subscription-state propagation details (up to 100 profiles) and time zone triggered-campaign example; added new FAQ entry for subscription state inheritance when email address changes.
- Deleted `best_practices/duplicate_emails.md`.
- Removed "Manage Email Subscriptions" tile from `best_practices.md` landing page.
- Added redirect: `channels/email/best_practices/duplicate_emails/` → `channels/email/faq/`.
- Collapsed 2 existing redirect chains (`message_building_by_channel/email/best_practices/managing_email_subscriptions/` and `message_building_by_channel/email/best_practices/duplicate_emails/`) to point directly to FAQ.

**Email reporting directory fix:**
- Moved `reporting_and_analytics/email_reporting.md` and `reporting_and_analytics/analytics_glossary.md` into `reporting/` to match the `reporting.md` landing page (Jekyll requires directory name to match landing page filename).
- Removed empty `reporting_and_analytics/` directory.
- Updated 5 internal links in `faq.md`, `email.md`, `mpp.md`, and `creating_an_email_campaign.md`.
- Updated 10 redirect targets in `broken_redirect_list.js` from `reporting_and_analytics/` to `reporting/`.
- Added 5 new redirects for old `channels/email/reporting_and_analytics/` paths.

### Files changed

- 9 page_order updates (email landing pages)
- 1 content merge (`faq.md`)
- 1 tile removal (`best_practices.md`)
- 1 file deleted (`duplicate_emails.md`)
- 2 files moved (`reporting_and_analytics/` → `reporting/`)
- 5 internal link fixes
- ~20 redirect entries added or updated in `broken_redirect_list.js`

### Remaining Jira items from Day 4

Items 1–3 and 5–9 from the Day 4 deferred list are still open.

---

## Day 4 follow-up — In-app messages section reorder (Feb 27)

**Status:** Complete — on branch `phase4-channels`

### What happened

**In-app messages nav reorder:** Updated `page_order` frontmatter for 6 top-level pages and 1 customize child page. New order:

1. Drag-and-drop editor (1)
2. Traditional editor (2)
3. Message types (3) — new landing page
4. Customize (4)
5. Testing (5)
6. Reporting (6)
7. Best practices (7)
8. FAQ (8)

**New "Message types" landing page:** Created `message_types.md` with two tile sections matching the wireframe: "Available in all editors" (Fullscreen, Modal) and "Traditional editor only" (Slideup, Custom HTML, Email capture form, Simple survey). Serves as landing for the existing `message_types/` directory.

**"Creative details" converted to redirect:** Replaced `creative_details.md` content with `layout: redirect` pointing to `message_types/`. Added `hidden: true` to remove from nav.

**File moves:**
- `create_an_in_app_message.md` → `drag_and_drop/create_an_in_app_message.md` (child of DnD editor)
- `ios_app_rating_prompt.md` → `best_practices/ios_app_rating_prompt.md` (child of Best practices)

**Landing page updates:**
- `customize.md`: Updated `guide_featured_list` to show 4 actual child pages (Style settings, Dark mode themes, Color profiles and CSS templates, Video in custom HTML). Removed Custom HTML and Email capture form tiles (now under Message types).
- `best_practices.md`: Added iOS rating prompt tile.
- `traditional.md`: Removed broken tiles for `traditional/customize/` and `traditional/dark-mode/` (those pages don't exist); kept only the Create tile.

**Internal link fixes:** Updated 8 stale links across 4 files:
- `prep_guide.md`: `creative_details/fullscreen/` → `message_types/fullscreen/`
- `traditional/create.md`: 4 references from `creative_details/` → `message_types/`
- `custom_html.md`: `creative_details/` → `message_types/`
- `style_settings.md`: 2 references from `create_an_in_app_message` → `drag_and_drop/create_an_in_app_message`
- `drag_and_drop.md`: tile link updated for moved create page

**Redirects:** 12 new entries in `broken_redirect_list.js` + 5 existing chain targets collapsed:
- 6 entries for `creative_details/{fullscreen,modal,slideup}` → `message_types/`
- 2 entries for `create_an_in_app_message` → `drag_and_drop/create_an_in_app_message`
- 2 entries for `ios_app_rating_prompt` → `best_practices/ios_app_rating_prompt`
- Collapsed 3 existing chains (`creative_details` landing, `ios_app_rating_prompt`, DnD `create`) to point to final destinations
- Updated 1 anchor redirect (`#content-guidelines`) to point to `message_types/`

### Customize child page order

- Style settings (1)
- Dark mode themes (2)
- Color profiles and CSS templates (3)
- Video in custom HTML (4)

### Files changed

- 6 page_order updates (top-level in-app messages pages)
- 1 page_order update (customize/style_settings.md)
- 1 new file (message_types.md landing page)
- 1 file converted to redirect (creative_details.md)
- 2 files moved (create_an_in_app_message.md, ios_app_rating_prompt.md)
- 3 landing page updates (customize.md, best_practices.md, traditional.md)
- 4 files with internal link fixes
- ~17 redirect entries added or updated in broken_redirect_list.js

### Jira items resolved

- Item #2 from Day 4 deferred list: "Message types landing (IAM) — new tile layout for 'All editors' vs 'Traditional only'"

---

## Days 5–8 — QA, merge, Jira tickets

**Status:** Not started
