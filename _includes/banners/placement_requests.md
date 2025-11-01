When you [create placements in your app or website]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), your app sends a request to Braze to fetch Banner messages for each placement.  

- You can request up to **10 placements per refresh request**.  
- For each placement, Braze returns the **highest-priority Banner** the user is eligible to receive.  
- If more than 10 placements are requested in a refresh, only the first 10 are returned; the rest are dropped.  

For example, an app might request three placements in a refresh request: `homepage_promo`, `cart_abandonment`, and `seasonal_offer`. Each request returns the most relevant Banner for that placement.
