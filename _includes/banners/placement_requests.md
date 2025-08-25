When you [create placements in your app or website]({{site.baseurl}}/developer_guide/banners/creating_placements/#requestBannersRefresh), your app sends a request to Braze to fetch Banner messages for each placement.  

- You can request up to **10 placements per user session**.  
- For each placement, Braze returns the **highest-priority Banner** the user is eligible to receive.  
- If more than 10 placements are requested in a session, only the first 10 are returned; the rest are dropped.  

For example, an app might request three placements during a single session: `homepage_promo`, `cart_abandonment`, and `seasonal_offer`. Each request returns the most relevant Banner for that placement.
