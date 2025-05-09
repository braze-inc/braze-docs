{% if include.variable_name == "dnd editors" %}

{% alert important %}
To access to the drag-and-drop editor, contact your IT administrator to verify that your firewall has `.bz-rndr.com` allowlisted.
{% endalert %}

{% elsif include.variable_name == "email html editor" %}

{% alert important %}
To access to the WYSIWYG (what you see is what you get) editor, contact your IT administrator to verify that your firewall has `.bz-rndr.com` allowlisted.
{% endalert %}

{% endif %}