User IDs should be set for each of your users. These should be unchanging and accessible when a user opens the app. Naming your user IDs correctly from the start is one of the most **crucial** steps when setting up user IDs. We strongly suggest using the Braze standard of UUIDs and GUIDs (detailed below). We also strongly recommend providing this identifier as it will allow you to:

- Track your users across devices and platforms, improving the quality of your behavioral and demographic data.
- Import data about your users using our [user data API][1].
- Target specific users with our [messaging API][2] for both general and transactional messages.

{% alert note %}
If such an identifier is not available, Braze will assign a unique identifier to your users, but you will lack the capabilities listed for user IDs. You should avoid setting user IDs for users for whom you lack a unique identifier that is tied to them as an individual. Passing a device identifier offers no benefit versus the automatic anonymous user tracking Braze offers by default.
{% endalert %}

{% alert warning %}
If you want to include an identifiable value as your user ID, for additional security, we **strongly recommend** adding our [SDK authentication]({{site.baseurl}}/developer_guide/authentication/) feature to prevent user impersonation.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/
