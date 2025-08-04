No painel da Braze, acesse **Configurações de Dados** > **Transformação de Dados**.

Selecione **Criar Transformação** para nomear sua transformação, em seguida escolha sua experiência de edição.

![Detalhes da transformação com a opção de escolher "Usar um modelo" ou "Começar do zero" para sua experiência de edição.]({% image_buster /assets/img/data_transformation/data_transformation10.png %}){: style="max-width:80%;"}

Selecione **Usar um modelo** para navegar por uma biblioteca de modelos, incluindo casos de uso de Transformação de Dados. Ou, selecione **Começar do zero** para carregar um modelo de código padrão. 

Se você está começando do zero, escolha um destino para sua transformação. Você ainda pode inserir um modelo de código da biblioteca de modelos.

{% details Mais sobre destinos %}
* **POST: Rastrear usuários:** Transforma webhooks de uma plataforma de origem em atualizações de perfil de usuário, como atributos, eventos ou compras.
* **PUT: Atualizar vários itens do catálogo:** Transforma webhooks de uma plataforma de origem em atualizações de itens do catálogo.
* **DELETE: Excluir vários itens do catálogo:** Transforma webhooks de uma plataforma de origem em exclusões de itens do catálogo.
* **PATCH: Editar vários itens do catálogo:** Transforma webhooks de uma plataforma de origem em edições de itens de catálogo.
* **POST: Envie mensagens imediatamente via API Only:** Transforma webhooks de uma plataforma de origem para enviar mensagens imediatas a usuários designados.
{% enddetails %}

{% alert note %}
Quer solicitar modelos adicionais ou destinos? Considere deixar [feedback do produto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% endalert %}

Após criar sua transformação, você verá a visão detalhada da transformação. Aqui, você pode visualizar o webhook mais recente recebido para esta transformação em **Detalhes do webhook** e um espaço para escrever seu código de transformação em **Código de transformação**.

{% if include.location == "typeform" %}

![Um exemplo de detalhes de webhook e código de transformação.]({% image_buster /assets/img/typeform/data_transformation_typeform.png %})

{% endif %}

Capture seu **Webhook URL** para uso na próxima etapa.
