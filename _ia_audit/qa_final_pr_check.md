# Final QA check — User Guide IA PR

> **Branch:** qa-round2-user-guide-ia  
> **Date:** 2025-03-11  
> **Per:** braze-docs-migration skill (Step 6 Verify + Step 7 QA)

---

## Summary

| Check | Status | Notes |
|-------|--------|--------|
| Stale path references (old IA in links) | **Fail** | Multiple files still use `engagement_tools/`, `message_building_by_channel/`, `data_and_analytics/`, `administrative/`. See table below. |
| Broken anchor links | **Fixed** | `the_braze_dashboard.md`: `#adding-favorite-workspaces` → `#favorite-workspaces`. |
| Broken-link script (fblinks) | **Skipped** | `node_modules` missing. Run `yarn install` then `./bdocs fblinks` before merge. |
| Build + redirect test | **Manual** | Build locally, spot-check pages, test 2–3 old URLs; use `./bdocs lredirects` if needed. |

---

## 1. Stale path references (update to canonical paths)

In-doc links should use the **new** user_guide IA paths. The following still use old path segments. Update each to the canonical path (or add a redirect and still prefer canonical in-doc links).

**Canonical mapping (old → new):**

- `message_building_by_channel/sms_mms_rcs/` → `channels/sms_mms_and_rcs/`
- `data_and_analytics/analytics/` → `analytics/` (e.g. `analytics/reports/`, home dashboard under analytics if present)
- `data_and_analytics/user_data_collection/user_import` → `data/` (confirm exact path: e.g. `data/distribution/` or audience/user data)
- `data_and_analytics/export_braze_data/` → `data/distribution/export_braze_data/`
- `data_and_analytics/braze_currents/` → `data/braze_currents/` or per redirect list
- `data_and_analytics/custom_data/` → `data/activation/` (e.g. `data/activation/attributes/`, `managing_custom_data/`)
- `engagement_tools/campaigns/` → `messaging/campaigns/`
- `engagement_tools/canvas/` → `messaging/canvas/`
- `engagement_tools/segments/` → `audience/segments/`
- `engagement_tools/messaging_fundamentals/` → `messaging/messaging_fundamentals/`
- `engagement_tools/campaigns/testing_and_more/` → `messaging/campaigns/` (e.g. `messaging/campaigns/` + rate-limiting, multivariate_testing per nav)
- `engagement_tools/testing/` → `messaging/ab_testing/` (or per redirect)
- `administrative/access_braze/sdk_endpoints/` → `administer/personal/sdk_endpoints/`
- `administrative/app_settings/` → `administer/global/workspace_settings/` (e.g. message_activity_log_tab, email_settings)

**Files and suggested fixes:**

| File | Old path in link | Suggested canonical path |
|------|-------------------|--------------------------|
| `administer/global/user_management/internal_groups.md` | `message_building_by_channel/sms_mms_rcs/` | `channels/sms_mms_and_rcs/` |
| `administer/personal/the_braze_dashboard.md` | `data_and_analytics/analytics/home_dashboard/` | `analytics/` (find correct home dashboard path) |
| `administer/personal/the_braze_dashboard.md` | `engagement_tools/campaigns/...`, `engagement_tools/canvas/...`, `engagement_tools/segments/...` | `messaging/campaigns/`, `messaging/canvas/`, `audience/segments/` |
| `channels/whatsapp/faq.md` | `data_and_analytics/user_data_collection/user_import` | `data/` (user import path) |
| `channels/webhooks/use_case_create_a_braze_to_braze_webhook.md` | `engagement_tools/`, `administrative/access_braze/sdk_endpoints/`, `administrative/app_settings/message_activity_log_tab/` | `messaging/`, `administer/personal/sdk_endpoints/`, `administer/global/workspace_settings/` (message activity log) |
| `channels/push/best_practices.md` | `engagement_tools/messaging_fundamentals/` | `messaging/messaging_fundamentals/` |
| `channels/push/troubleshooting.md` | `engagement_tools/segments/`, `engagement_tools/campaigns/testing_and_more/`, `data_and_analytics/export_braze_data/`, `administrative/app_settings/` | `audience/segments/`, `messaging/campaigns/`, `data/distribution/export_braze_data/`, `administer/global/workspace_settings/` |
| `channels/line/reporting.md` | `engagement_tools/testing/` | `messaging/ab_testing/` (or correct conversion/conversion_correlation path) |
| `channels/line/line_setup.md` | `data_and_analytics/user_data_collection/user_import` | `data/` (user import) |
| `channels/in_app_messages/drag_and_drop.md` | `engagement_tools/canvas/`, `engagement_tools/messaging_fundamentals/` | `messaging/canvas/`, `messaging/messaging_fundamentals/` |
| `channels/email/faq.md` | `administrative/app_settings/email_settings/` | `administer/global/workspace_settings/` (email preferences) |
| `messaging/templates/.../post_purchase_feedback.md` | `data_and_analytics/custom_data/custom_attributes/` | `data/activation/attributes/` or `data/activation/managing_custom_data/` |
| `messaging/messaging_fundamentals/localization.md` | `data_and_analytics/braze_currents` | `data/braze_currents/` or `data/infrastructure/` (confirm) |
| `data/activation/attributes/array_of_objects.md` | `data_and_analytics/custom_data/custom_attributes/` | `data/activation/attributes/` (or nested path) |
| `data/distribution/export_braze_data/message_archiving.md` | `partners/data_and_analytics/cloud_storage/` | Keep if under `_partners/`; confirm path exists. |
| `partners/.../looker.md` | `user_guide/data_and_analytics/braze_currents/` | `user_guide/data/braze_currents/` or data distribution path |
| `privacy_portal.md` | `data_and_analytics/export_braze_data/message_archiving` | `data/distribution/export_braze_data/message_archiving` |
| `_hidden/other/support_contact.md` | `data_and_analytics/` | `data/` or `analytics/` per new IA |

Use the migration tracker or `broken_redirect_list.js` to confirm exact target paths where the new IA has different nesting.

---

## 2. Broken anchor link (fixed)

- **File:** `_docs/_user_guide/administer/personal/the_braze_dashboard.md`
- **Issue:** Link `[add favorite workspaces](#adding-favorite-workspaces)` pointed to a slug that doesn’t exist. The section heading is "Favorite workspaces", which generates `#favorite-workspaces`.
- **Fix applied:** Changed the link to `#favorite-workspaces`.

---

## 3. Step 7 QA — Run before merge

1. **Build locally**  
   `bundle exec jekyll serve` (or project default). Confirm user_guide nav and key pages build.

2. **Broken-link check**  
   `yarn install` then `./bdocs fblinks`. Triage any reported broken links (paths and anchors).

3. **Redirects**  
   Open 2–3 old URLs (e.g. `/docs/user_guide/engagement_tools/campaigns/`, `/docs/user_guide/administrative/access_braze/braze_instances/`) and confirm they redirect to the new canonical URLs.

4. **Spot-check**  
   Open "Create a campaign", "Create a Canvas", dashboard, and a channel "Create a…" page; confirm in-page and cross-page links work.

---

## 4. Redirect list — targets pointing at removed paths

Many entries in `broken_redirect_list.js` have **destinations** that still use `user_guide/administrative/` or `user_guide/data_and_analytics/`. The current repo has `administer/`, `analytics/`, and `data/` (no `administrative/` or `data_and_analytics/` under `_user_guide`). If those destination URLs are not themselves redirected, they will 404. Recommend:

- Grep for redirect **targets** that contain `user_guide/administrative/` or `user_guide/data_and_analytics/`.
- Either update those targets to the new canonical paths (e.g. `administer/`, `data/`, `analytics/`) or ensure a further redirect exists from the old path to the new one so the chain resolves.

This is a follow-up task; the main PR fix is updating in-doc links to canonical paths and running fblinks after `yarn install`.
