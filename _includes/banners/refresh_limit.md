The number of times you can refresh placements during a session depends on your SDK version:

{% tabs local %}
{% tab multiple refreshes %}
These minimum SDK versions use a token bucket system for refreshing placements: up to 5 requests per session, with 1 request replenished every 180 seconds.

{% sdk_min_versions web:6.1.0 swift:13.1.0 android:38.0.0 %}
{% endtab %}

{% tab one refresh %}
Older SDK versions allow only one refresh per session; additional calls are ignored.

{% sdk_min_versions web:5.8.1 swift:11.3.0 android:33.1.0 reactnative:14.0.0 flutter:13.0.0 %}
{% endtab %}
{% endtabs %}