# Support Case Analysis Output — L7D 02/12/2026

## Summary

- **Total unique cases analyzed**: 1,817
- **CSV file**: `SUPPORT_CASE_EXPORT_L7D_02122026.csv`
- **Analysis date**: 2026-02-12

### Triage Breakdown

| Category | Count |
|---|---|
| Docs Gap | 898 |
| Bug/Product | 364 |
| Support-Only | 139 |
| Edge Case | 8 |
| Other (no docs action) | 408 |

### Top Topic Clusters (by case volume)

| Topic | Cases | Docs Action |
|---|---|---|
| eCommerce events | 46 | Add FAQ section to ecommerce_events.md |
| Canvas throttle/rate limiting | 51 | Add FAQ entry to rate-limiting.md |
| Machine opens / auto-unsubscribe | 17 | Add FAQ entry to email/faq.md |
| Custom attribute data types | 13 | Add FAQ entry to managing_custom_data.md |

---

## Per-Ticket Analysis (Actionable Items)

### Case: 500VP00000pxtRKYAY
- **Category**: Docs Gap (New Feature)
- **Question**: Where can I view product-level purchase data with eCommerce recommended events? Why can't I segment by specific product?
- **Resolution**: eCommerce recommended events currently show high-level summary only (total spend). Product-level detail is viewed in user profiles under the Transactions tab. To segment by specific product, use Segment Extensions with nested event property filtering.
- **Verified behavior**: The ecommerce_events.md page does not have an FAQ section addressing this common question.
- **Target Doc**: `_docs/_user_guide/data/activation/custom_data/recommended_events/ecommerce_events.md`
- **Suggested Change**: Add FAQ section covering product-level data visibility, segmentation by product, and migration from legacy purchase events

### Case: 500VP00000qPrBFYA0
- **Category**: Docs Gap (New Feature)
- **Question**: Purchase events vs eCommerce events — how does deprecation affect Products page and "Purchased Specific Product" filters? No public documentation exists for the Products page or its relationship to segmentation.
- **Resolution**: The Products page is distinct from Shopify-synced catalogs and drives segmentation dropdowns. eCommerce events are the replacement for legacy purchase events.
- **Verified behavior**: The ecommerce_events.md page has a deprecation alert but doesn't detail migration path or Products page.
- **Target Doc**: `_docs/_user_guide/data/activation/custom_data/recommended_events/ecommerce_events.md`
- **Suggested Change**: Add FAQ entries about migration from purchase events and Products page discoverability

### Case: 500VP00000njKGAYA2
- **Category**: Docs Gap (New Feature)
- **Question**: Can I customize parameters in eCommerce order placed events (e.g., add purchase channel, store info)?
- **Resolution**: This is expected behavior — order tags and custom parameters are not currently supported in ecommerce events. Customers must continue sending legacy custom purchase events for proprietary data.
- **Verified behavior**: Confirmed via support resolution that custom order-level parameters are not supported.
- **Target Doc**: `_docs/_user_guide/data/activation/custom_data/recommended_events/ecommerce_events.md`
- **Suggested Change**: Add FAQ entry clarifying customization limitations of eCommerce events

### Case: 500VP00000qJUu7YAG
- **Category**: Docs Gap
- **Question**: Can I create a segment of users who browsed product pages in the last 30 days using ecommerce.product_viewed?
- **Resolution**: The Segment Builder only allows filtering by count of times the event was performed. For time-window filtering, use Segment Extensions which allow filtering by specific custom event in a time window plus nested property filtering.
- **Verified behavior**: The ecommerce use cases page mentions Segment Extensions but doesn't provide explicit guidance for this common use case.
- **Target Doc**: `_docs/_user_guide/data/activation/custom_data/recommended_events/ecommerce_events.md`
- **Suggested Change**: Add FAQ entry about segmentation by product_viewed in time window

### Case: 500VP00000q8WeIYAU
- **Category**: Docs Gap
- **Question**: When is external_id required vs not required for eCommerce recommended events (SDK vs API)?
- **Resolution**: Via REST API (`/users/track`), each request must include a user identifier (external_id, braze_id, user_alias, email, or phone). Via SDK, the SDK logs against the currently identified user (set via changeUser), so no explicit ID is needed per event call.
- **Verified behavior**: The ecommerce_events.md page shows API payload examples with external_id but doesn't explicitly explain when it's required.
- **Target Doc**: `_docs/_user_guide/data/activation/custom_data/recommended_events/ecommerce_events.md`
- **Suggested Change**: Add FAQ entry about identity handling for SDK vs API

### Case: 500VP00000oFkHAYA0
- **Category**: Docs Gap
- **Question**: Why can't I access nested `products` properties (like product_id) when setting up AI Recommendations with ecommerce.order_placed?
- **Resolution**: The AI Recommendations property dropdown only shows top-level properties. Nested array properties like `products` are not accessible via dot notation in this context. This is a known limitation.
- **Verified behavior**: Confirmed — nested array properties within ecommerce events are not surfaced in AI Recommendation setup dropdowns.
- **Target Doc**: `_docs/_user_guide/data/activation/custom_data/recommended_events/ecommerce_events.md`
- **Suggested Change**: Add FAQ entry about nested property limitations with AI Recommendations

### Case: 500VP00000qCPCoYAO
- **Category**: Docs Gap
- **Question**: If I change a send throttle on an active Canvas, does it apply to users already in the Canvas?
- **Resolution**: Yes, the new rate limit applies to users already in the Canvas, but only for their next Canvas step. Users already enqueued for a message step will be sent at the original throttle. The updated throttle only takes effect on future step processing.
- **Verified behavior**: Confirmed via support resolution.
- **Target Doc**: `_docs/_user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting.md`
- **Suggested Change**: Add FAQ entry clarifying how mid-flight throttle changes affect in-progress Canvas users

### Case: 500VP00000q5kKTYAY
- **Category**: Docs Gap
- **Question**: How do I prevent email security software (like Barracuda, Proofpoint) from auto-unsubscribing users by scanning link URLs?
- **Resolution**: Some corporate email security software pre-fetches or scans all URLs in emails, including unsubscribe links, causing unintended unsubscribes. Braze identifies these as machine-triggered via the one-click list-unsubscribe header. Customers should work with their recipients' IT to whitelist Braze domains, or use preference center URLs instead of direct unsubscribe links.
- **Verified behavior**: Multiple cases confirm this is a recurring issue with corporate email security scanning.
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/email/faq.md`
- **Suggested Change**: Add FAQ entry about security software causing auto-unsubscribes

### Case: 500VP00000qHEANYA4
- **Category**: Docs Gap
- **Question**: Why has the machine open percentage dropped significantly with no segmentation changes?
- **Resolution**: Machine open rates can fluctuate based on email provider behavior (e.g., Apple Mail Privacy Protection). These rates are not consistent and can vary over time. Unique opens and Other Opens are more reliable metrics for measuring true engagement.
- **Verified behavior**: Machine opens documentation exists but doesn't address fluctuation expectations.
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/email/faq.md`
- **Suggested Change**: Add FAQ entry about machine open rate fluctuations

### Case: 500VP00000ndH7EYAU
- **Category**: Docs Gap
- **Question**: Custom attribute detected as number in dev but string in production. How do I change the data type? Do I need to recreate and resend?
- **Resolution**: Braze auto-detects data types based on the first value received. You can force the data type in Data Settings > Custom Attributes by selecting the desired type from the dropdown. However, data ingested before the type change remains stored as the old type and may not be segmentable. A warning will appear on affected user profiles.
- **Verified behavior**: Documented in managing_custom_data.md under "Forcing data type comparisons" but lacks a clear FAQ entry.
- **Target Doc**: `_docs/_user_guide/data/activation/custom_data/managing_custom_data.md`
- **Suggested Change**: Add FAQ section with common questions about data type detection, mismatches across environments, and best practices

---

## Consolidated Updates

### Update 1: ecommerce_events.md — Add FAQ Section
**Priority**: HIGH (46 cases)
**Target**: `_docs/_user_guide/data/activation/custom_data/recommended_events/ecommerce_events.md`
**Cases**: 500VP00000pxtRKYAY, 500VP00000qPrBFYA0, 500VP00000njKGAYA2, 500VP00000qJUu7YAG, 500VP00000q8WeIYAU, 500VP00000oFkHAYA0, 500VP00000fwDi5YAE, 500VP00000qFeLoYAK, 500VP00000pfDwqYAE, 500VP00000q7oLZYAY

### Update 2: email/faq.md — Add Machine Opens and Auto-Unsubscribe FAQ Entries
**Priority**: HIGH (17 cases)
**Target**: `_docs/_user_guide/message_building_by_channel/email/faq.md`
**Cases**: 500VP00000q5kKTYAY, 500VP00000q2BavYAE, 500VP00000qHEANYA4, 500VP00000p5edlYAA, 500VP00000pMuRFYA0

### Update 3: rate-limiting.md — Add Canvas Throttle Change FAQ
**Priority**: MEDIUM (51 cases about rate limiting; specific throttle change question)
**Target**: `_docs/_user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting.md`
**Cases**: 500VP00000qCPCoYAO, 500VP00000qGJlXYAW, 500VP00000qPBGtYAO

### Update 4: managing_custom_data.md — Add FAQ Section for Data Type Issues
**Priority**: MEDIUM (13 cases)
**Target**: `_docs/_user_guide/data/activation/custom_data/managing_custom_data.md`
**Cases**: 500VP00000ndH7EYAU, 500VP00000q2FHyYAM, 500VP00000p4r5EYAQ, 500VP00000qDOL8YAO, 500VP00000q2HTSYA2

