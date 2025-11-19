{% if include.variable_name == "dnd editors" %}

{% alert important %}
Para obter acesso ao editor de arrastar e soltar, entre em contato com o administrador de TI para verificar se o firewall tem o endereço `*.bz-rndr.com` na lista de permissões.
{% endalert %}

{% elsif include.variable_name == "email html editor" %}

{% alert important %}
Para obter acesso ao editor de HTML, entre em contato com o administrador de TI para verificar se o firewall tem o endereço `*.bz-rndr.com` na lista de permissões.
{% endalert %}

{% endif %}