# User Guide IA — Step 6 & 7 QA report

> **Branch:** qa-round2-user-guide-ia (from git status)  
> **Scope:** Full user_guide (entirety of user_guide as requested)  
> **Date:** 2025-03-11

---

## Step 6: Verify — Stale references and orphan links

### 6.1 Stale path segments (old IA paths still in content)

Content and links should use **canonical** paths. The following path segments are from the old IA and appear in `_docs/` and/or `_lang/`. Update them to the new paths (see redirect list or migration tracker for targets).

#### In `_docs/` (English)

| Old path segment | Example file(s) | New path (canonical) |
|------------------|-----------------|----------------------|
| `engagement_tools/` | `channels/webhooks/create_a_webhook.md`, `analytics/`, `messaging/canvas/create_a_canvas/create_a_canvas.md`, `messaging/ab_testing/faq.md`, `channels/line/line_setup.md`, `channels/sms_mms_and_rcs/` | `messaging/`, `channels/`, `audience/segments/`, `messaging/canvas/` as appropriate |
| `message_building_by_channel/` | `analytics/tracking/influenced_opens.md`, `analytics/dashboards/channel_performance.md`, `messaging/messaging_fundamentals/know_before_you_send.md` | `channels/` (e.g. `channels/push/`, `channels/email/`) |
| `personalization_and_dynamic_content/` | `channels/webhooks/create_a_webhook.md`, `messaging/landing_pages/personalize_landing_pages.md` | `messaging/design_and_edit/personalize/` |
| `onboarding_with_braze/` | `messaging/messaging_fundamentals/know_before_you_send.md` (email_setup/ip_warming) | Use `channels/email/email_setup/ip_warming/` or equivalent |
| `administrative/` | Many: `channels/webhooks/create_a_webhook.md`, `channels/*/create_a_*.md`, `messaging/messaging_fundamentals/sending_test_messages.md`, `_api/endpoints/export.md`, etc. | `administer/` (e.g. `administer/global/workspace_settings/`, `administer/global/user_management/`) — map per redirect list |
| `engagement_tools/campaigns/testing_and_more/sending_test_messages` | `messaging/messaging_fundamentals/accessibility.md` | `messaging/messaging_fundamentals/sending_test_messages/` (with `?tab=` when channel-specific) |
| `test_campaigns/sending_test_messages` | `messaging/design_and_edit/media_library/image_specifications.md` | `messaging/messaging_fundamentals/sending_test_messages/` |
| `engagement_tools/canvas/get_started/` | `messaging/canvas/canvas_components/experiment_step.md` | `messaging/canvas/` or `messaging/canvas/ideas_and_strategies/` (get_started dissolved) |

**Release notes and other _docs:**  
`_docs/_releases/home.md`, `_docs/_releases/2025/11_11_25.md`, `_docs/_releases/2025/2_4_25.md`, `_docs/_releases/2025/1_7_25.md`, `_docs/_releases/2024/11_12_24.md`, `_docs/_releases/2019/october.md`, and `_docs/_developer_guide/banners/placements.md` contain `engagement_tools/` or `canvas/get_started/` or `testing_and_more/sending_test_messages` links. Prefer canonical paths; historical release text can stay with a note that redirects cover old URLs.

#### In `_lang/` (translations)

- **pt_br:** Multiple files under `_lang/pt_br/_user_guide/` and `_lang/pt_br/_releases/home.md` use `engagement_tools/`, `message_building_by_channel/`, `personalization_and_dynamic_content/`, `administrative/`.
- **ko, fr_fr, es:** Similar patterns in `_releases/home.md`, `_releases/2025/11_11_25.md`, and some `_user_guide` files (e.g. `message_building_by_channel/sms_mms_rcs/link_shortening.md`, `brazeai/operator.md`).

Per migration skill, `_lang/` mirrors are often handled separately; coordinate with localization. For QA alignment, consider at least fixing the same segment renames in the main locale files you touch.

---

### 6.2 Orphan / deleted paths (links to pages that no longer exist)

- **Channel testing pages:** `channels/*/testing` and `message_building_by_channel/*/testing` are deleted. Redirects in `broken_redirect_list.js` send them to `messaging/messaging_fundamentals/sending_test_messages/?tab=...`. Any **in-article** link that still points at `channels/.../testing` or old test_campaigns/testing_and_more URLs should be updated to `messaging/messaging_fundamentals/sending_test_messages/` with the appropriate `?tab=` (see `_ia_audit/qa_testing_redirects_plan.md`).
- **Canvas get_started:** Subsection dissolved; content moved to `canvas_basics.md`, `ideas_and_strategies/canvas_outlines.md`, etc. Links to `engagement_tools/canvas/get_started/...` or `canvas/get_started/...` should point to the new canonical pages (e.g. `messaging/canvas/`, `messaging/canvas/ideas_and_strategies/`).
- **Redirect list inconsistency:** In `broken_redirect_list.js`, line 798 sends `engagement_tools/campaigns/testing_and_more/sending_test_messages/` to `developer_guide/platform_wide/sending_test_messages/`. The canonical user_guide page is `messaging/messaging_fundamentals/sending_test_messages/`. Consider updating that redirect target so old bookmarks land on the user guide page. Line 3290 points to `messaging/campaigns/testing_and_more/sending_test_messages/#send-test-messages` — confirm that path exists; if not, point to `messaging/messaging_fundamentals/sending_test_messages/` with the correct anchor.

---

### 6.3 Redirect list (channel testing)

Channel testing redirects in `broken_redirect_list.js` are correctly pointing to `messaging/messaging_fundamentals/sending_test_messages/?tab=...` for both `message_building_by_channel/*/testing` and `channels/*/testing`. No change needed for those entries.

---

## Step 7: QA checklist

Run these manually (and optionally add to your release/QA runbook):

- [ ] **Build locally**  
  - Run the site (e.g. `bundle exec jekyll serve` or project default).  
  - Confirm the user_guide section loads in navigation and no build errors for user_guide pages.

- [ ] **Spot-check 3–5 moved/renamed pages**  
  - Examples: `messaging/messaging_fundamentals/sending_test_messages`, `messaging/canvas/canvas_basics`, `messaging/governance`, `administer/global/workspace_settings`, a channel “Create a…” page.  
  - Confirm they render and that in-page links (especially to other user_guide pages) work.

- [ ] **Test redirects**  
  - Old URLs (with trailing slash): e.g.  
    - `/docs/user_guide/channels/email/testing/` → `.../sending_test_messages/?tab=email`  
    - `/docs/user_guide/engagement_tools/canvas/get_started/` (if you have a redirect)  
    - `/docs/user_guide/administrative/access_braze/braze_instances/` → `.../administer/personal/sdk_endpoints/`  
  - At least one `?tab=` destination (e.g. webhook, email) to confirm query-string targets work.

- [ ] **Broken-link check**  
  - Run `yarn install` (or `npm install`) if needed, then `./bdocs fblinks` to find broken links across the site.  
  - Focus on “Create a…”, landing, and “Know before you send”–style pages in user_guide for links to deleted or renamed paths.

- [ ] **Redirect tooling**  
  - The migration skill references `./bdocs redirects <base_url>`. This repo’s `./bdocs help` does not list a `redirects` subcommand. Available: `lredirects` (list old URLs in branch), `mredirects` (make redirects for renamed files). Use `./bdocs lredirects` to list old URLs; run it when needed to validate redirect coverage.

---

## Summary

| Step | Status | Action |
|------|--------|--------|
| **6.1 Stale references** | Resolved | Replaced old path segments (`engagement_tools`, `message_building_by_channel`, `personalization_and_dynamic_content`, `onboarding_with_braze`, `administrative`, and wrong test/sending_test_messages paths) with canonical paths in `_docs/`. `_lang/` left for localization. |
| **6.2 Orphan links** | Resolved | Updated in-article links; fixed redirect targets (lines 798, 3290). |
| **6.3 Channel testing redirects** | Pass | Redirect entries for channel testing point to `sending_test_messages/?tab=...`. |
| **7 QA** | Pending | Build, spot-check pages, test redirects, run fblinks; use `./bdocs lredirects` where applicable. |

Once Step 7 is executed, the branch will align with the migration skill’s QA expectations for the user_guide.
