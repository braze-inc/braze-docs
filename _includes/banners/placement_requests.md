When you [create placements in your app or website]({{site.baseurl}}/developer_guide/banners/creating_placements/#requestBannersRefresh), you'll request placements from Braze to display Banner messages to your users.

During a single user session, you can request a maximum of 10 placements. For each one you request, Braze will return the highest-priority Banner a user is eligible for. If you request more than 10 placements in a single session, only the first 10 will be returned&#8212;any additional requests will return an error.

For example, if have a homepage-promo, a cart-abandonment, and a seasonal-offer placement in your app, you can request all three within a single user session.