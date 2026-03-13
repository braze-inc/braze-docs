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

If Content Cards are displayed correctly in your app but you are consistently not receiving any analytics (unique recipients, impressions, clicks, and so on), it is likely an SDK integration issue.

- **Custom Content Card views (Android, iOS):** If you are using a custom Content Card view, you must implement the logging of impressions and clicks manually within your application. The default Braze UI logs these automatically; custom implementations require explicit calls to the appropriate logging methods. See [Log analytics]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) for your platform.
- **Web:** Ensure that the Braze Web SDK is loaded and that you are calling the methods that log impressions and clicks when cards are displayed or clicked. Check the browser console for errors and verify that card data is being received.
- **General:** Confirm that the user is identified (not anonymous) when cards are displayed and that the SDK is initialized before requesting or displaying cards.
