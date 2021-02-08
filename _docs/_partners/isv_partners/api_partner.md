---
nav_title: API Partner Integration
alias: /currents_connector/
hidden: true
---

# API Partner Integration

Certified ISV partners are required to add their partner name to the partner field in their API implementation. Please see the following /users/track endpoint structure for an example request.

## Partner Request Body

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "attributes" : (optional, array of Attributes Object),
   "events" : (optional, array of Event Object),
   "purchases" : (optional, array of Purchase Object),
   "partner" : (optional, string)
}
```