---
nav_title: API partner integration
alias: /api_partner_integration/
hidden: true
---

# API partner integration

> Learn about the requirements for partner API integrations, such as the syntax for `User-Agent` headers.

{% alert important %}
Previously, partners were required to add their name to the partner field in their API Requests. This formatting is no longer supported and a `User-Agent` header is now required.
{% endalert %}

## User agents

You are required to include a `User-Agent` header that clearly identifies the source of the traffic. This enables our shared customers to see partner traffic in Braze’s API usage reporting, and enables Braze engineers to identify integrations that are not following best practices. Generally, you should only use a single user agent for all of your traffic.

### Syntax

Your `User-Agent` header must adhere to the following format (which is similar to the [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#page-46) standard):

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

### Examples

For example, the following would be a correct user agent for Snowflake's Cloud Data Ingestion:

```bash
User-Agent: partner-Snowflake-CloudDataIngestion/179
```

Whereas this would be incorrect because it doesn't clearly identify the source of the traffic:

```bash
User-Agent: axios/1.4.0
``` 
