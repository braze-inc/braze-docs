# QA session: Testing redirects and in-article links

> **Context:** Thread with Adam, Rachel, Zair. Decision: remove channel "Testing" nav redirects; link to "Send test messages" from create/preview content. Channel `testing.md` files are already deleted on this branch.

**Actionable in this QA session only:** redirect list updates and fixing wrong in-article links. Not in scope: adding new "Preview and test" sections, or standalone channel testing pages (defer).

---

## 1. Redirect list updates (`assets/js/broken_redirect_list.js`)

**Problem:** Current entries send `message_building_by_channel/X/testing` → `channels/X/testing`. Channel testing pages are deleted, so those targets 404. Bookmarks or old links to `channels/X/testing` also 404.

**Actions:**

### 1a. Update existing channel-testing redirects (10 pairs)

Change the **destination** from `channels/.../testing` to `messaging_fundamentals/sending_test_messages` with the correct `?tab=` so users land on the right channel tab.

| Current target (broken) | New target (with tab) |
|-------------------------|------------------------|
| `/docs/user_guide/channels/banners/testing/` | `/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=banners` |
| `/docs/user_guide/channels/content_cards/testing/` | `/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=content%20card` |
| `/docs/user_guide/channels/email/testing/` | `/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=email` |
| `/docs/user_guide/channels/in_app_messages/testing/` | `/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=in-app%20message` |
| `/docs/user_guide/channels/line/testing/` | `/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=line` |
| `/docs/user_guide/channels/push/testing/` | `/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=push` |
| `/docs/user_guide/channels/sms_mms_and_rcs/testing/` | `/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=sms%2Fmms%20and%20rcs` |
| `/docs/user_guide/channels/webhooks/testing/` | `/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=webhook` |
| `/docs/user_guide/channels/whatsapp/testing/` | `/docs/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=whatsapp` |

**Implementation:** In `broken_redirect_list.js`, find the 10 lines where the value is `'/docs/user_guide/channels/.../testing'` or `'.../testing/'` (banners, content_cards, email, in_app_messages, line, push, sms_mms_and_rcs, webhooks, whatsapp). Replace the RHS with the new target from the table. Note: `sms_mms_rcs` in message_building_by_channel maps to channel `sms_mms_and_rcs`; use tab `sms%2Fmms%20and%20rcs`.

### 1b. Add redirects from `channels/*/testing` to fundamentals (new entries)

Anyone with a bookmark or link to e.g. `/docs/user_guide/channels/content_cards/testing/` currently gets 404. Add one pair per channel (with and without trailing slash if the script expects both):

- `channels/banners/testing` and `.../testing/` → fundamentals with `?tab=banners`
- `channels/content_cards/testing` and `.../testing/` → fundamentals with `?tab=content%20card`
- Same for: email, in_app_messages, line, push, sms_mms_and_rcs, webhooks, whatsapp

Place these near the other channel testing redirects in the file. Follow existing style (with/without trailing slash as in the current message_building_by_channel entries).

---

## 2. Fix wrong in-article links to sending test messages

Replace old paths with `{{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/` and add `?tab=<channel>` where the link is channel-specific.

### 2a. In-app messages (old path: engagement_tools or test_campaigns)

| File | Current link / path | New link |
|------|----------------------|----------|
| `_docs/_user_guide/channels/in_app_messages/message_types.md` | `/docs/user_guide/messaging/campaigns/test_campaigns/sending_test_messages/` (in guide_top_text) | `{{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=in-app%20message` (use Liquid; page uses raw `<a href=`) |
| `_docs/_user_guide/channels/in_app_messages/traditional.md` | `engagement_tools/campaigns/testing_and_more/sending_test_messages` (line ~290) | `messaging/messaging_fundamentals/sending_test_messages` with `?tab=in-app%20message` |
| `_docs/_user_guide/channels/in_app_messages/traditional.md` | same (line ~399) | same |
| `_docs/_user_guide/channels/in_app_messages/message_types/slideup.md` | `engagement_tools/campaigns/testing_and_more/sending_test_messages` | `messaging/messaging_fundamentals/sending_test_messages` with `?tab=in-app%20message` |
| `_docs/_user_guide/channels/in_app_messages/message_types/fullscreen.md` | same | same |
| `_docs/_user_guide/channels/in_app_messages/best_practices/prep_guide.md` | same (Testing link) | same |

Use `{{site.baseurl}}/user_guide/...` for all. Tab param: `?tab=in-app%20message`.

### 2b. Best practices landing pages (wrong path: developer_guide/in_app_messages)

| File | Current link | New link |
|------|--------------|----------|
| `_docs/_user_guide/channels/content_cards/best_practices.md` | `link: /docs/developer_guide/in_app_messages/sending_test_messages/` | `link: /docs/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=content%20card` |
| `_docs/_user_guide/channels/email/best_practices.md` | `link: /docs/developer_guide/in_app_messages/sending_test_messages/` | `link: /docs/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=email` |

---

## 3. Verification (before calling QA done)

- [x] Redirect list: all 10 existing channel-testing redirect targets updated; new `channels/*/testing` entries added (with/without trailing slash per existing pattern).
- [x] In-app: 6 files updated (message_types.md, traditional.md x2, slideup.md, fullscreen.md, prep_guide.md).
- [x] Best practices: 2 files updated (content_cards, email).
- [x] No remaining references to `engagement_tools/campaigns/testing_and_more/sending_test_messages` or `test_campaigns/sending_test_messages` in channel docs (except in redirect list LHS).
- [ ] Optional: run `./bdocs redirects <base_url>` if available; spot-check 2–3 old channel testing URLs and one message_building_by_channel testing URL.

---

## Out of scope for this session

- Adding new "Preview and test" sections or links where they don’t exist.
- Creating standalone channel testing pages (Zair’s idea); defer.
- Changes under `_lang/` (translations); handle separately.
