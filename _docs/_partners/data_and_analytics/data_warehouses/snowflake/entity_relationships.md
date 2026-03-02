---
nav_title: "Entity relationships"
article_title: Entity Relationships for Snowflake and Braze
page_order: 10
search_tag: Partner
---

# Entity relationships for Snowflake and Braze

> These are the list of entity relationships between Snowflake and Braze for each messaging channel.

{% alert important %}
The entity relationship diagrams are meant to highlight the shared fields and relationships across tables. They are not meant to be a complete representation of each table's schema. For a full list of fields, refer to the individual table schemas.
{% endalert %}

{% sdktabs %}
{% sdktab Content Cards %}
{% multi_lang_include snowflake_users_messages/contentcard.md %}
{% endsdktab %}

{% sdktab Email %}
{% multi_lang_include snowflake_users_messages/email.md %}
{% endsdktab %}

{% sdktab Feature Flags %}
{% multi_lang_include snowflake_users_messages/featureflag.md %}
{% endsdktab %}

{% sdktab In-App Messages %}
{% multi_lang_include snowflake_users_messages/inappmessage.md %}
{% endsdktab %}

{% sdktab Push Notifications %}
{% multi_lang_include snowflake_users_messages/pushnotification.md %}
{% endsdktab %}

{% sdktab SMS %}
{% multi_lang_include snowflake_users_messages/sms.md %}
{% endsdktab %}

{% sdktab Webhook %}
{% multi_lang_include snowflake_users_messages/webhook.md %}
{% endsdktab %}

{% sdktab WhatsApp %}
{% multi_lang_include snowflake_users_messages/whatsapp.md %}
{% endsdktab %}
{% endsdktabs %}