---
nav_title: Reporting
article_title: In-App Message Reporting
page_order: 5
description: "This reference article covers in-app message reporting and analytics including campaign details, message performance, and historical performance."
channel:
  - in-app messages
tool:
  - Reports

---

# In-app message reporting {#iam-reporting}

> This reference article covers in-app message reporting and analytics including campaign details, message performance, and historical performance.

{% multi_lang_include analytics/campaign_analytics.md channel="in-app message" %}

### Discrepancies between control groups and variants

When an in-app message campaign has a 50-50 variant split, sometimes the control group will have a slightly higher percentage than the variant (such as 51% for the control group and 49% for the variant). This discrepancy is caused by a difference in rendering time.

In-app messages may require some time to render if they contain images, Connected Content, and other features, or if they're rendering in regions with slower internet speeds. It's possible for a user to trigger an in-app message, be assigned to a variant, but then end their session before the in-app message renders on their device—resulting in the impression not getting logged. In contrast, the control group doesn't require any rendering. The user only needs to perform the trigger to log an impression.

