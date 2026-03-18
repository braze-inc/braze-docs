---
nav_title: Log analytics
article_title: Log Analytics 
page_order: 1
description: "This article covers how to manually log clicks, events, and analytics for your customized Content Cards."
toc_headers: "h2"

---

# Log analytics

{% multi_lang_include developer_guide/_shared/logging_analytics/content_cards.md %}

## Missing Content Cards analytics

If Content Cards are displayed correctly in your app but you consistently do not receive any analytics (unique recipients, impressions, clicks, and so on), it is likely an SDK integration issue.

- **Custom Content Card views (Android, iOS, Web):** The default Braze UI logs impressions and clicks automatically on all platforms. If you are using a custom Content Card view or implementation, you must call the appropriate logging methods explicitly within your application. See [Log analytics]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) for your platform. For custom Web implementations specifically, ensure the Braze Web SDK is loaded, check the browser console for errors, and verify that card data is being received.
- **SDK initialization and user identification:** Ensure the SDK is fully initialized before displaying cards. Events are silently dropped (not queued) if the SDK is uninitialized, in delayed initialization mode, or GDPR-disabled. The SDK does log analytics for anonymous users, but dashboard metrics like "unique recipients" require a resolved user identity, so call changeUser before cards are displayed where possible.
