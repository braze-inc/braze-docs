---
nav_title: API Partner Integration
alias: /api_partner_integration/
hidden: true
---

# API partner integration

> Learn about our requirements for API partner integrations, such as the syntax for `User-Agent` headers.

## User-Agent headers

All partners are required to include a `User-Agent` header which clearly identifies the source of the traffic. This enables our shared customers to see partner traffic in Braze’s API usage reporting, and enables Braze engineers to identify integrations which are not following best practices. Partners should generally only use a single user agent for all their traffic.

To ensure you're clearly identified as a partner, your `User-Agent` header must use the following format (which is similar to the [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#page-46) standard):

```bash
User-Agent: partner-OrganizationName-ProductName/ProductVersion
```

Replace the following:

| Placeholder | Description |
|-------------|-------------|
| `OrganizationName` | The name of your organization formatted in Pascal case. |
| `ProductName` | The name of the your product formatted in Pascal case. |
| `ProductVersion` | The version number of your product. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For example, a correct user agent for Snowflake Cloud Data Ingestion would be:

```bash
User-Agent: partner-Snowflake-CloudDataIngestion/179
```

Whereas this is an incorrect user agent because it doesn't clearly identify the source of the traffic:

```bash
User-Agent: axios/1.4.0
``` 
