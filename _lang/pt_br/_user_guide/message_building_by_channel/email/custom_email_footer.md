---
nav_title: Rodapé de e-mail personalizado
article_title: Rodapé de e-mail personalizado
page_order: 6.5
description: "Este artigo descreve como configurar um rodapé de e-mail personalizado em todo o espaço de trabalho."
channel:
  - email

---

# Rodapé de e-mail personalizado

> Você pode definir um rodapé de e-mail personalizado em todo o espaço de trabalho, que pode ser modelado em cada e-mail usando o atributo {% raw %}`{{${email_footer}}}`{% endraw %} Liquid.

Ao usar rodapés de e-mail personalizados, você não precisa mais criar um novo rodapé para cada modelo de e-mail ou campanha de e-mail que usar. As alterações feitas em seu rodapé personalizado serão refletidas em todas as campanhas de e-mail novas e existentes. Lembre-se de que a conformidade com a [Lei CAN-SPAM de 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) exige que você inclua um endereço físico da sua empresa e um link de cancelamento de assinatura em seus e-mails.

{% alert warning %}
É sua responsabilidade garantir que o rodapé personalizado atenda aos requisitos mencionados acima.
{% endalert %}

## Criando seu rodapé personalizado

Para criar ou editar seu rodapé personalizado, faça o seguinte:

1. Vá para **Configurações** > **Preferências de e-mail**.
2. Vá para a seção **Custom Footer (Rodapé personalizado** ) e ative os rodapés personalizados.
3. Edite o rodapé na seção **Compor**.
4. Enviar uma mensagem de teste. 

\![Um exemplo de um rodapé personalizado.]({% image_buster /assets/img_archive/custom_footer.png %})

O rodapé padrão usa o atributo {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} e nosso endereço físico para correspondência. Se você estiver usando esse padrão, certifique-se de selecionar **<other>** para o **protocolo**.

{% alert important %}
Para estar em conformidade com as normas da CAN-SPAM, seu rodapé personalizado deve incluir {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}. Você não poderá salvar um rodapé personalizado sem esse atributo.
{% endalert %}

\![Valores de protocolo e URL necessários para o rodapé personalizado.]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## Rodapés sem links de cancelamento de assinatura

Tenha muito cuidado ao usar um modelo com o rodapé personalizado {% raw %}`{{${email_footer}}}`, mas sem a tag de link de cancelamento de inscrição `{{${set_user_to_unsubscribed_url}}}`{% endraw %}. Um aviso será exibido, mas você poderá optar por enviar um e-mail com ou sem um link de cancelamento de assinatura.

Aqui está um aviso no compositor de e-mail:

\![Exemplo de e-mail composto sem um rodapé.]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

Aqui está um aviso no compositor da campanha:

\![Composição da campanha sem rodapé.]({% image_buster /assets/img_archive/no_footer_test.png %})

### Adição de um link de cancelamento de assinatura personalizado

Para adicionar um link de cancelamento de assinatura personalizado, você pode alterar o link de cancelamento de assinatura no rodapé personalizado de {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} para um link para o seu próprio site com um parâmetro de consulta que inclua o ID do usuário. Um exemplo é:
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Em seguida, chame o [ponto de extremidade`/email/status` ]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) para atualizar o status da assinatura do usuário. Para obter mais detalhes, consulte nossa documentação sobre [como alterar o status da assinatura de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

Em seguida, salve esse novo link. A tag padrão de cancelamento de inscrição do Braze {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} deve estar no rodapé. Isso significa que você precisa incluir o link padrão "ocultando-o" ao colocar a tag em um comentário ou em uma tag `<div>` oculta.

## Práticas recomendadas

Sugerimos as seguintes práticas recomendadas ao criar e usar rodapés personalizados.

### Personalização com atributos

Ao criar um rodapé personalizado, a Braze sugere o uso de [atributos para personalização]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/). O conjunto completo de atributos padrão e personalizados está disponível, mas aqui estão alguns que podem ser úteis:

| Atributo | Etiqueta |
| --------- | --- |
| Endereço de e-mail do usuário | {% raw %}`{{${email_address}}}`{% endraw %} |
| URL de cancelamento de inscrição personalizado do usuário | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>Essa tag substitui a tag anterior {% raw %}`{{${unsubscribe_url}}}`{% endraw %}. Em vez disso, recomendamos que você use a nova tag {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}. |
| URL de opt-in personalizado do usuário | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| URL de assinatura personalizada do usuário | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| URL do Centro de Preferências Braze personalizado do usuário | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Incluindo um link de cancelamento de assinatura e um link de adesão

{% raw  %}
Como prática recomendada, a Braze recomenda incluir um link de cancelamento de inscrição (como ``{{${set_user_to_unsubscribed_url}}}``) e um link de adesão (como ``{{${set_user_to_opted_in_url}}}``) em seu rodapé personalizado. Dessa forma, os usuários poderão cancelar a assinatura ou optar por participar, e você poderá coletar passivamente dados de participação para uma parte de seus usuários.
{% endraw %}

### Definição de rodapés personalizados para e-mails de texto simples

Você também pode optar por definir um rodapé personalizado para e-mails de texto simples na guia **Páginas e rodapés de assinatura** na página **Preferências de e-mail**, que segue as mesmas regras do rodapé personalizado para e-mails em HTML. 

Se você não incluir um rodapé em texto simples, o Braze criará automaticamente um a partir do rodapé em HTML. Quando os rodapés personalizados estiverem de acordo com suas preferências, selecione **Save (Salvar**).

\![E-mail com a opção Definir rodapé de texto simples personalizado selecionada.]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

