---
nav_title: Reporting
article_title:  Email Reporting
page_order: 20
description: "This reference article covers the different components of email reporting and where it can be found in the dashboard."
tool:
  - Reports
channel:
  - email

---

# Email reporting

> This article covers the different components of your email reporting and where it can be found in the dashboard.

## Troubleshooting

### Bounced emails

- **554 5.7.1 [internal] recipient address was suppressed due to customer policy** — Try another address, re-engage on another channel, or—for your own test addresses only—remove the address from the suppression list (avoid removing real user suppressions; that can hurt reputation).
- **Mailbox full / invalid account** — Often a list-quality signal. Prioritize users who recently opened or clicked (for example last 30–60 days) while you clean inactive or bad addresses.

### Invalid domains

Errors like `unable to get mx info` often mean many targets use bad domains (for example typos). Segment, export, correct, and re-import those profiles.

### Throttled IPs

If a recipient server throttles your IP, reduce volume to that domain, improve engagement, and work with deliverability support if throttling persists.

{% multi_lang_include analytics/campaign_analytics.md channel="email" %}

