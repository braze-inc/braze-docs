Após a [integração do SDK do Braze]({{site.baseurl}}/developer_guide/sdk_integration/), os usuários que iniciarem seu app pela primeira vez serão considerados "anônimos" até que você chame o método `changeUser` e atribua a eles um `external_id`. Uma vez atribuídas, não é possível torná-las anônimas novamente. No entanto, se o usuário desinstalar e reinstalar o app, ele se tornará anônimo novamente até que `changeUser` seja chamado.

Se um usuário previamente identificado iniciar uma sessão em um novo dispositivo, todas as suas atividades anônimas serão automaticamente sincronizadas com o perfil existente depois que você ligar para `changeUser` nesse dispositivo usando o endereço `external_id`. Isso inclui quaisquer atribuições, eventos ou histórico coletados durante a sessão no novo dispositivo.

{% if include.section == "user_guide" %}
{% alert tip %}
Para obter um passo a passo completo, consulte [Definição de IDs de usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/).
{% endalert %}
{% endif %}