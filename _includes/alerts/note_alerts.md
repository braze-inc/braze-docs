{% if include.alert == 'Content Cards frequency capping' %}

{% alert note %}
Frequency capping doesn't apply to Content Cards.
{% endalert %}

{% endif %}

{% if include.alert == 'Custom Attributes time attribute' %}

{% alert note %}
A date string such as "12-1-2021" or "12/1/2021" will be converted to a datetime object and treated as a [time attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% endif %}

{% if include.alert == 'Manage custom data storage' %}

{% alert note %}
All user profile data (custom events, custom attributes, custom data) is stored as long as those profiles are active.
{% endalert %}

{% endif %}
