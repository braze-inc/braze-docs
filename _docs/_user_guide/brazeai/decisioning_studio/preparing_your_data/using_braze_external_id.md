---
nav_title: Using Braze External ID
article_title: Using Braze External ID as your unit of identity
page_order: 4
page_type: reference
description: "This reference article explains why Decisioning Studio uses Braze External ID as the unit of customer identity and what happens if a different identifier structure is used."
---

# Using Braze External ID

> Decisioning Studio requires a single, stable customer identifier that is consistent across all data assets. The recommendation is to use **Braze External ID** as that identifier. This article explains why, and what risks arise when other identifier structures are used instead.

## The recommendation: use Braze External ID

Decisioning Studio operates exclusively using the Braze External ID as its unit of customer identity. All data assets—customer profiles, features, activations, engagements, conversions—should reference the Braze External ID as the primary customer identifier.

This is not just a technical requirement; it is a deliberate design choice that protects the reliability of the model's training and recommendations.

## Why other identifier structures create problems

### The dual-identity challenge

Many organizations maintain two different customer identifier systems:

- **A warehouse or system-of-record ID** (sometimes called a "canonical ID" or "physical ID"): the source of truth for metrics like lifetime value, returns, and loyalty. Lives in your data warehouse or ERP.
- **A platform ID**: the identifier used by tools like Braze, typically tied to an email address, device token, or similar activation channel.

The temptation is to use the warehouse ID for building customer features (since that's where the data lives) and the Braze ID for activation (since that's what Braze uses). But this requires a translation layer between the two systems—and that translation layer introduces fragility.

### The risk: identity drift

Even if the mapping between your warehouse ID and your Braze ID is currently one-to-many (one physical customer maps to multiple Braze profiles), that mapping can destabilize over time into many-to-many. If a single warehouse ID gets reassigned to different customers over time, or if the same Braze profile becomes associated with multiple warehouse IDs, the result is **identity drift**.

Identity drift causes:

- **Model training failures:** If the customer the model thought it was recommending to is actually a different person, the training signal is corrupted.
- **Reporting inaccuracies:** Metrics become unmeaningful when the underlying identity mapping is unstable.
- **Attribution errors:** Conversions get matched to the wrong recommendations.

## Why Braze External ID addresses these risks

### 1. Activation-ready by design

Recommendations generated against a Braze External ID can be injected directly into messages via Liquid or Connected Content without any ID translation step. Eliminating the translation layer removes a significant source of operational complexity and failure.

### 2. Isolated from upstream changes

By operating on the Braze External ID, Decisioning Studio is insulated from changes in your upstream systems. If your internal warehouse ID changes due to a system migration, a data quality fix, or an ERP update, the Braze External ID—and everything associated with it—remains stable.

### 3. Clean channel separation

In Braze, a user profile corresponds to a reachable communication channel. If a customer registers two email addresses, they have two distinct Braze profiles with two distinct Braze External IDs. Decisioning Studio treats these as two separate entities, which has an important benefit: recommendations and event history for one email are not contaminated by activity associated with the other.

This prevents what might be called "context creep"—the recommendation engine would not, for example, mix work-related purchasing behavior into recommendations sent to a personal email account.

## Multi-entity considerations

### Multi-store or hierarchical businesses

For businesses that operate multiple storefronts or sub-brands (for example, a franchisor with many franchisees), the concept of "customer" can be ambiguous. A customer who shops across multiple locations may have separate records at each location but should be treated as one person for recommendation purposes.

If your business has this structure, discuss with your Decisioning Studio team how to model the customer hierarchy before finalizing your identifier strategy.

### B2C identity fragmentation

A single physical person can accumulate multiple Braze profiles over time—for example, by registering with different email addresses or logging in on different devices before account merge. Decisioning Studio treats each Braze External ID as a distinct customer.

This is by design: each profile represents a distinct activation channel. However, it does mean that the quality of your recommendations depends on the quality of your Braze identity resolution. If your Braze implementation does not reliably merge duplicate profiles, some customers may receive lower-quality personalization because their history is fragmented across multiple profiles.
