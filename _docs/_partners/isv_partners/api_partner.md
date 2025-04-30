---
nav_title: API Partner Integration
alias: /api_partner_integration/
hidden: true
---

# API partner integration
## User Agents

All partners are required to include a User-Agent header which clearly identifies the source of the traffic. This enables our shared customers to see partner traffic in Braze’s API usage reporting, and enables Braze engineers to identify integrations which are not following best practices. Partners should generally only use a single user agent for all their traffic.

User agents should follow the following format which clearly identifies the partner, similar to [RFC 7231] (https://datatracker.ietf.org/doc/html/rfc7231#page-46):

```User-Agent: partner-<partner name>-<partner product> / <version>```

For example, Snowflake Cloud Data Ingestion’s user agent could be:

```User-Agent: partner-Snowflake-CloudDataIngestion/179``` 

An example of an unacceptable User-Agent header would be:

```User-Agent: axios/1.4.0``` 

This user agent is unacceptable because it does not clearly identify the source of the traffic.
