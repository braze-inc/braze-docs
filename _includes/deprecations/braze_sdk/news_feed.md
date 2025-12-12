{% if include.status == 'Deprecated' %}

{% alert important %}
News Feed and relevant tags and methods are deprecated. We recommend using our [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/) messaging channel instead&#8212;it's more flexible, customizable, and reliable.
{% endalert %}

{% else %}

{% alert important %}
News Feed is being deprecated. We recommend migrating to our Content Cards messaging channel instead&#8212;it's more flexible, customizable, and reliable. To get started, check out [Migrating from News Feed]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

{% endif %}