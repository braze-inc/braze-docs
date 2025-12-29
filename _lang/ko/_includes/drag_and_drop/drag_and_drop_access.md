{% if include.variable_name == "dnd editors" %}

{% alert important %}
드래그 앤 드롭 편집기에 액세스하려면 IT 관리자에게 문의하여 방화벽에 `*.bz-rndr.com` 허용 목록이 있는지 확인하세요.
{% endalert %}

{% elsif include.variable_name == "email html editor" %}

{% alert important %}
HTML 편집기에 액세스하려면 IT 관리자에게 문의하여 방화벽에 `*.bz-rndr.com` 허용 목록이 있는지 확인하세요.
{% endalert %}

{% endif %}