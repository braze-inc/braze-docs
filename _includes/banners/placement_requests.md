When you [create placements in your app or website]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), your app sends a request to Braze to fetch Banner messages for each placement.  

- You can request up to **10 placements per refresh request**.  
- For each placement, Braze returns the **highest-priority Banner** the user is eligible to receive.  
- If more than 10 placements are requested in a refresh, only the first 10 are returned; the rest are dropped.  

For example, an app might request three placements in a refresh request: `homepage_promo`, `cart_abandonment`, and `seasonal_offer`. Each request returns the most relevant Banner for that placement.

#### Rate limiting for refresh requests

For users on older SDK versions (prior to Swift 13.1.0, Android 38.0.0, Web 6.1.0, React Native 17.0.0 and Flutter 15.0.0), **only one refresh request is permitted per user session**.

For users on newer minimum SDK versions—Swift 13.1.0+, Android 38.0.0+, Web 6.1.0+, React Native 17.0.0+, and Flutter 15.0.0+—refresh requests are controlled by a token bucket algorithm to prevent excessive polling:

* Each user session begins with **5 refresh tokens**.
* Tokens refill at a rate of **1 token every 180 seconds (3 minutes)**.

Each call to `requestBannersRefresh` consumes one token. If you attempt a refresh when no tokens are available, the request will be dropped until a token refills. This mechanism is important for mid-session, event-triggered updates. To implement dynamic updates (e.g., after a user completes an action on the same page), call the refresh method after the custom event is logged, but be mindful of the necessary delay for Braze to ingest and process the event before the user qualifies for a different Banner campaign.
