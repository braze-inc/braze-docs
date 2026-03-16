{% if include.alert == 'User profile external_id' %}

{% alert warning %}
Não atribua um `external_id` a um perfil de usuário antes de poder identificá-lo exclusivamente. Depois de identificar um usuário, não é possível revertê-lo para anônimo.
<br><br>
Um `external_id` pode ser atualizado usando o [`/users/external_ids/rename` endpoint]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/). No entanto, qualquer tentativa de definir um `external_id` diferente durante a sessão de um usuário criará um novo perfil de usuário com o novo `external_id` associado a ele. Nenhum dado será transmitido entre os dois perfis.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment Currents multiple connectors' %}

{% alert warning %}
Se você pretende criar mais de um dos mesmos conectores Currents (por exemplo, dois conectores de eventos de engajamento com mensagens), eles devem estar em espaços de trabalho diferentes. Como a integração do Braze Segment Currents não pode isolar eventos de diferentes apps em um único espaço de trabalho, se isso não for feito, haverá desduplicação de dados desnecessários e perda de dados.
{% endalert %}

{% endif %}

{% if include.alert == 'Canvas race condition audience trigger' %}

{% alert warning %}
Evite configurar uma campanha baseada em ação ou o Canva com o mesmo disparo do filtro de público (como um atributo alterado ou a realização de um evento personalizado). Uma [condição de corrida]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions) pode ocorrer em que o usuário não está no público no momento em que realiza o evento de gatilho, o que significa que ele não receberá a campanha ou entrará no canva.
{% endalert %}

{% endif %}
