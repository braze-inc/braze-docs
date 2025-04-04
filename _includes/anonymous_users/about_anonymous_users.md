After you [integrate the Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/), users who launch your app for the first time will be considered "anonymous" until you call the `changeUser` method and assign them an `external_id`. Once assigned, you can't make them anonymous again. However, if they uninstall and reinstall your app, they will become anonymous again until `changeUser` is called.

If a previously-identified user starts a session on a new device, all of their anonymous activity will automatically sync to their existing profile after you call `changeUser` on that device using their `external_id`. This includes any attributes, events, or history collected during the session on the new device.

{% if include.section == "user_guide" %}
{% alert tip %}
For a full walkthrough, see [Setting User IDs]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/).
{% endalert %}
{% endif %}