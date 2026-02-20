{% if include.alert == 'User profile external_id' %}

{% alert warning %}
Don't assign an `external_id` to a user profile before you can uniquely identify them. After you identify a user, you can't revert them to anonymous.
<br><br>
An `external_id` can be updated using the [`/users/external_ids/rename` endpoint]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/). However, any attempt to set a different `external_id` during a user's session will create a new user profile with the new `external_id` associated with it. No data will be passed between the two profiles.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment Currents multiple connectors' %}

{% alert warning %}
If you intend to create more than one of the same Currents connectors (for example, two message engagement event connectors), they must be in different workspaces. Because the Braze Segment Currents integration cannot isolate events by different apps in a single workspace, failure to do this will lead to unnecessary data deduping and lost data.
{% endalert %}

{% endif %}

{% if include.alert == 'Canvas race condition audience trigger' %}

{% alert warning %}
Avoid configuring an action-based campaign or Canvas with the same trigger as the audience filter (such as a changed attribute or performed a custom event). A [race condition]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions) may occur in which the user is not in the audience at the time they perform the trigger event, which means they won't receive the campaign or enter the Canvas.
{% endalert %}

{% endif %}
