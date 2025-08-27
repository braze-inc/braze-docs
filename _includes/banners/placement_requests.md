When you [create placements in your app or website]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), your app sends a request to Braze to fetch Banner messages for each placement.  

- You can request up to **10 placements per refresh request** by default. If more than 10 placements are requested, only the first 10 are returned; the rest are dropped.  
- For each placement, Braze returns the **highest-priority Banner** the user is eligible to receive.

Refresh linits depend on the SDK version your app is using:
- For SDK versions Android 38.0.0, Swift 13.1.0 and Web 6.1.0, placements refreshes use a token bucket algorithm. This allows multiple refreshes in a session within the defined limits (a bucket size of 5 requests with a refill rate of one per 180 seconds).
- For older SDK versions, placement refreshes are limited to once per session. Additional refresh calls in the same session are ignored.

{% alert important %}
Check which SDK version your app is running to ensure you understand the applicable refresh limits.
{% endalert %}
