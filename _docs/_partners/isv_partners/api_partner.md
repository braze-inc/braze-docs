---
nav_title: API Partner Integration
alias: /api_partner_integration/
hidden: true
---

# API partner integration

## User Agents

All partners are required to include a User-Agent header which clearly identifies the source of the traffic. This enables our shared customers to see partner traffic in Braze’s API usage reporting, and enables Braze engineers to identify integrations which are not following best practices. Partners should generally only use a single user agent for all their traffic.

User agents should follow the following format which clearly identifies the partner, similar to [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#page-46):

```
User-Agent: partner-NAME-PRODUCT/VERSION
```

Replace the following:

| Placeholder | Description |
|-------------|-------------|
| `NAME` | The name of your organization in pascal case. |
| `PRODUCT` | The name of the specific product in pascal case. |
| `VERSION` | The version number of the product. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For example, a correct user agent for Snowflake Cloud Data Ingestion would be:

```
User-Agent: partner-Snowflake-CloudDataIngestion/179
```

Whereas this is an incorrect user agent because it doesn't clearly identify the source of the traffic:

```
User-Agent: axios/1.4.0
``` 
