---
nav_title: API Partner Integration
alias: /api_partner_integration/
hidden: true
---

# API partner integration

Alloys ISV partners are required to add their partner name to the `partner` field in their API Requests, allowing Braze to track API partner usage such as incoming requests from partners. Reference the following [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint structure when developing your implementation.

## Partner request body

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object),
   "partner" : (required, string)
}
```