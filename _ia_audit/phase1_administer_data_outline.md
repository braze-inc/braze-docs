# Phase 1: Administer and Data — Evaluation & Outline

> **Branch:** `phase1-administer-data`
>
> **Status:** Migration complete (administer structure per tracker). Old administrative folder removed.
>
> **Source of truth:** User Guide IA Migration Tracker FY27 (CSV) — not the biweekly deck.
>
> **Target:** Administer splits into **Personal** (access, dashboard, language, portal, support) and **Global** (user management, SSO, workspaces, workspace settings, admin settings, billing, privacy). Full restructure per tracker.

---

## Administer

### Current structure
- **Path:** `_docs/_user_guide/administrative/`
- **Nav title:** "Administrative"
- **Subsections:**
  - `access_braze/` — Access Your Account, SSO, Language, SDK endpoints, Dashboard, Support, Troubleshooting, Portal
  - `app_settings/` — Workspaces, API Keys, Message Activity Log, Event User Log, Internal Groups, Tags, Email Preferences, Push settings, multi-language settings, brand guidelines, subscription/usage (billing), exports log, company settings (contact info, security, notification prefs, automated provisioning)
  - `privacy/` — Spam regulations, managing consent

### Target structure (from migration tracker)
- **Path:** `_docs/_user_guide/administer/`
- **Subsections:** Personal (new landing), Global (new landing)
- **Personal:** access_braze content → `administer/personal/` (accessing account, dashboard, language, portal, support)
- **Global:** app_settings + privacy + SSO → `administer/global/` (user management, workspace settings, company settings, billing, privacy)

### Work required

| Task | Scope | Notes |
|------|-------|-------|
| **1. Rename folder** | `administrative` → `administer` | All files under `_docs/_user_guide/administrative/` move to `_docs/_user_guide/administer/` |
| **2. Update nav_title** | All landing pages | `Administrative` → `Administer` in `administrative.md`; verify child pages |
| **3. Add redirects** | Every moved path | `user_guide/administrative/*` → `user_guide/administer/*` (path preserved below `/administrative/`) |
| **4. Update internal links** | ~150+ files | Replace `/user_guide/administrative/` with `/user_guide/administer/` across `_docs`, `_api`, `_partners`, `_developer_guide`, `_releases`, `_help`, `_lang` |
| **5. Fix broken link in app_settings** | 1 file | `app_settings.md` links to `/user_guide/data/field_level_encryption/` — correct path is `/user_guide/data/infrastructure/field_level_encryption/` |

### Files to move (English only — `_lang` mirrors)
- `administrative.md` → `administer.md`
- `administrative/access_braze.md` + 10 children
- `administrative/app_settings.md` + ~25 children (including admin_settings, manage_your_braze_users, email_settings)
- `administrative/privacy.md` + 2 children

---

## Data

### Current structure
- **Path:** `_docs/_user_guide/data/`
- **Nav title:** "Data"
- **Subsections:**
  - `unification/` — CDI/Cloud Ingestion, Data Transformation, User data, Formula
  - `activation/` — Custom data (events, attributes), Catalogs, Report metrics glossary
  - `distribution/` — Currents, Export Braze data
  - `infrastructure/` — Data centers, Field-level encryption, Data points
  - `technology_partners.md` — Links to `/partners/`

### Target structure
- **Path:** `_docs/_user_guide/data/` (unchanged)
- **Scope:** Unification (CDI, transforms), Activation (events, attributes, catalogs), Distribution (Currents, exports). Infrastructure stays (data centers, FLE, data points). Technology Partners stays as outbound link.

### Work required

| Task | Scope | Notes |
|------|-------|-------|
| **1. Verify nav titles** | Landing pages | "Data" already correct. Confirm `data.md`, `unification.md`, `activation.md`, `distribution.md` titles match target |
| **2. Reorder or regroup (if any)** | Optional | Current structure already matches. No folder renames needed |
| **3. Update internal links** | Only if paths change | Data paths unchanged → no link updates for Data itself. May need to update links *to* Data if any reference old Administer paths |
| **4. Fix any stale links** | Audit | Links from Administer → Data (e.g. field_level_encryption) — verify correct |

### Assessment
**Data = minimal or no changes.** Structure already aligns with target. Focus is on Administer; Data is included in phase 1 as a "verify and document" pass.

---

## Execution order

1. **Administer**
   - Create redirect mappings (old URL → new URL) for all `administrative/*` paths
   - Move `administrative/` → `administer/` (or create new structure and delete old)
   - Update `nav_title` in `administer.md` and any child landing pages
   - Fix `app_settings.md` field_level_encryption link
   - Run find-and-replace: `/user_guide/administrative/` → `/user_guide/administer/` across repo (excluding redirect definitions)
   - Add redirects to Braze redirect config (location TBD — check existing redirect setup)

2. **Data**
   - Spot-check landing pages for nav_title, guide_top_header
   - Confirm no structural changes needed
   - Document "no changes" in phase 1 log

3. **QA**
   - Build site locally, verify Administer section loads
   - Verify redirects work for old `administrative` URLs
   - Broken link scan for `administrative` and `administer`

---

## Redirect format

Redirects live in `assets/js/broken_redirect_list.js`:

```javascript
validurls['/docs/user_guide/administrative'] = '/docs/user_guide/administer';
validurls['/docs/user_guide/administrative/access_braze'] = '/docs/user_guide/administer/access_braze';
// ... one entry per moved path, preserving path below /administrative/
```

Add entries for every `administrative/*` path that moves to `administer/*`. Run `./bdocs redirects <base_url>` to test.

---

## Source
**Use the migration tracker CSV** for the complete Administer mapping. Rows 16–56 define Administer (Personal, Global, and all moves/renames).
