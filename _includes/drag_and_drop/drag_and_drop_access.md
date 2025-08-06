{% if include.variable_name == "dnd editors" %}

{% alert important %}
To gain access to the drag-and-drop editor, contact your IT administrator to verify that your firewall has `*.bz-rndr.com` allowlisted.
{% endalert %}

{% elsif include.variable_name == "email html editor" %}

{% alert important %}
To gain access to the HTML editor, contact your IT administrator to verify that your firewall has `*.bz-rndr.com` allowlisted.
{% endalert %}

{% endif %}