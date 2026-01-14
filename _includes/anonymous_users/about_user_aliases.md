Although anonymous users don’t have `external_ids`, you can assign them a [user alias]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#user-aliases) instead. You should assign a user alias when you want to add other identifiers to the user but don't know what their `external_id` is (for example, they aren't logged in). With user aliases, you also can:

- Use the Braze API to log events and attributes associated with anonymous users
- Use the [External User ID is blank]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#external-user-id) segmentation filter to target anonymous users in your messaging

{% if include.section == "user_guide" %}
{% alert tip %}
For a full walkthrough, see [Braze SDK: Setting a user alias]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).
{% endalert %}
{% endif %}