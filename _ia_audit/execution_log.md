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

## Day 3 — Messaging

**Status:** Not started

**Estimate:** 93 pages, 11 stubs

---

## Day 4 — Channels

**Status:** Not started

**Estimate:** 132 pages, 11 stubs

---

## Days 5–8 — QA, merge, Jira tickets

**Status:** Not started
