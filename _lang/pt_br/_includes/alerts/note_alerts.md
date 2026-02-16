{% if include.alert == 'Content Cards frequency capping' %}

{% alert note %}
A limitação de frequência não se aplica aos Cartões de Conteúdo.
{% endalert %}

{% endif %}

{% if include.alert == 'Custom Attributes time attribute' %}

{% alert note %}
Uma string de data como "12-1-2021" ou "12/1/2021" será convertida em um objeto datetime e tratada como um [atributo de tempo]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% endif %}

{% if include.alert == 'Manage custom data storage' %}

{% alert note %}
Todos os dados do perfil do usuário (eventos personalizados, atributos personalizados, dados personalizados) são armazenados enquanto esses perfis estiverem ativos.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment profiles first app use' %}

{% alert note %}
O Braze não gera perfis para os usuários até que eles tenham usado o aplicativo pela primeira vez, portanto, não é possível fazer o direcionamento para usuários que ainda não abriram o aplicativo.
{% endalert %}

{% endif %}
