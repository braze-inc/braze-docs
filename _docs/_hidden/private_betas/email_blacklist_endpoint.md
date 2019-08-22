---
nav_title: Email Blacklist
page_order: 3
search_rank: 2
---
# Email Blacklist

User email addresses can be blacklisted via Braze using a RESTful API.

## Braze Instance Endpoints

Instance  | REST Endpoint
-----------|-----------------------------------------
US-01 | `https://rest.iad-01.braze.com/email/blacklist`
US-02 | `https://rest.iad-02.braze.com/email/blacklist`
US-03 | `https://rest.iad-03.braze.com/email/blacklist`
US-04 | `https://rest.iad-04.braze.com/email/blacklist`
US-06 | `https://rest.iad-06.braze.com/email/blacklist`
EU-01 | `https://rest.fra-01.braze.eu/email/blacklist`

## Blacklisting Email Addresses

Blacklisting an email address will unsubscribe the user from email and mark them as hard bounced.

```json
POST https://YOUR_REST_API_URL/email/blacklist
Content-Type: application/json
```

| Parameter | Required | Data Type | Description |
| ---------------------| --------------- |
| `api_key` | Yes | String | see App Group REST API Key in Parameter Definitions |
| `email` | Yes | String or Array | String email address to blacklist, or an Array of up to 50 email addresses to blacklist. |

### Example Email Blacklist CURL

```
curl -X POST -H "Content-Type: application/json" -d '{"api_key":"YOUR_APP_GROUP_REST_API_KEY","email":["EMAIL_TO_BLACKLIST_1","EMAIL_TO_BLACKLIST_2"]}' https://YOUR_REST_API_URL/email/blacklist
```
