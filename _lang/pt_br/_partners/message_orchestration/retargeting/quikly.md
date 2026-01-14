---
nav_title: Quikly
article_title: Quikly
description: "Este artigo de referência descreve a parceria entre a Braze e a Quickly, uma plataforma de marketing de urgência. Com essa parceria, você pode acelerar as conversões em eventos dentro de uma jornada do cliente da Braze."
alias: /partners/quikly/
page_type: partner
search_tag: Partner

---

# Quikly

> [A Quikly](https://www.quikly.com), uma plataforma de marketing de urgência, utiliza a psicologia para motivar os consumidores, de modo que as marcas possam aumentar imediatamente a resposta em torno de suas principais iniciativas de marketing.

_Essa integração é mantida pela Quikly._

## Sobre a integração

A parceria Braze e Quikly permite que você acelere as conversões em eventos dentro de uma jornada do cliente da Braze. A Quikly faz isso usando a psicologia da urgência para motivar os consumidores de forma divertida e instantânea. Por exemplo, as marcas podem usar o Quikly para adquirir imediatamente novos assinantes de e-mail e SMS diretamente no Braze ou para motivar outros objetivos importantes de marketing, como baixar seu app para mobile.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Quikly | É necessário ter uma conta de parceiro da marca [Quikly](https://www.quikly.com) para aproveitar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com as permissões `users.track`, `subscription.status.set`, `users.export.ids` e `subscription.status.get`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá da URL do Braze para sua instância. |
| Chave de API da Quikly (opcional) | Uma chave de API da Quikly fornecida por seu gerente de sucesso do cliente (somente webhook). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

A Quikly permite que as marcas acelerem a aquisição por e-mail ou SMS e motiva os assinantes a fornecer dados primários diretamente na Braze. Você também pode usar a Braze para direcionar os clientes perdidos com uma ativação da Quikly que reativará e reterá esse público. Além disso, os profissionais de marketing podem usar essa integração para incentivar eventos específicos da jornada do cliente com estruturas de recompensas exclusivas. 

Por exemplo:
 - Crie antecipação e engajamento ao longo dos dias à medida que os consumidores aceitam a chance de ganhar recompensas incríveis com o [Quikly Hype](https://www.quikly.com/urgency-marketing/platform/product-overview/hype). Os dados primários são automaticamente enviados por push para a Braze.
 - Acelere a aquisição de novos assinantes de envio de e-mail e SMS usando ofertas exclusivas e em tempo real com base na velocidade de resposta do consumidor, na classificação em relação a outros, aleatoriamente ou antes que o tempo ou as quantidades se esgotem com o [Quikly Swap](https://www.quikly.com/urgency-marketing/platform/product-overview/swap).
 - Motive etapas específicas da jornada do cliente com estruturas de recompensas exclusivas usando webhooks.
 - Aplique atributos ou eventos personalizados ao perfil do usuário ao participar de uma ativação do Quikly.

## Integração

Abaixo estão descritas quatro integrações diferentes: aquisição de e-mail, aquisição de SMS, atributos personalizados e webhooks. A integração escolhida dependerá de sua ativação do Quikly e do caso de uso.

{% tabs %}
{% tab Aquisição de e-mail %}

### Aquisição de e-mail

Se suas ativações do Quikly coletarem dados de perfil ou endereços de e-mail de clientes, a única etapa necessária é fornecer ao Quikly sua chave de API REST e o ponto de extremidade. A Quikly configurará sua conta de marca para passar esses dados para a Braze. Se houver atributos do usuário adicionais que gostaria de incluir, mencione isso ao fornecer as credenciais da API à Quikly.

Aqui está um esboço de como a Quikly executa esse fluxo de trabalho.
1. Ao participar de uma ativação da Quikly, a Quikly agenda uma pesquisa de usuário usando a [API de exportação]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para ver se existe um usuário com um determinado `email_address`.
2. Registre ou atualize o usuário.
  - Se o usuário existir:
    - Não crie um novo perfil.
    - Se desejar, o Quikly pode registrar um atributo personalizado no perfil do usuário para indicar que o usuário participou da ativação.
  - Se o usuário não existir:
    - A Quikly cria um perfil somente de alias por meio do [ponto de extremidade]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) do Braze [`/users/track`, definindo o e-mail do usuário como o alias do usuário para fazer referência a esse usuário no futuro (já que o usuário não terá um ID externo).]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
    - Se desejar, a Quikly pode registrar eventos personalizados para indicar que esse perfil participou da ativação da Quikly.

{% details /users/track request %}

#### Cabeçalhos da solicitação
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Corpo da solicitação
```
{
  "attributes": [{
    "_update_existing_only": false,
    "user_alias:": {
      "alias_name": "email@example.com",
      "alias_label: "email"
    },
    "email": "email@example.com"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab Aquisição de SMS %}

### Inscrições para SMS

As ativações da Quikly podem coletar números de telefones celulares diretamente dos clientes e iniciar uma nova inscrição por SMS. Para ativar essa integração, forneça ao gerente de sucesso do cliente da Quikly o `subscription_group_id`. É possível acessar o site `subscription_group_id` de um grupo de inscrições navegando até a página **Grupo de inscrições**.

O Quikly realizará uma pesquisa de inscrição usando o número de telefone do cliente e o creditará automaticamente na ativação se já existir uma inscrição por SMS. Caso contrário, uma nova inscrição será iniciada e, depois que o status da inscrição for verificado, o cliente receberá o crédito.

Aqui está o fluxo de trabalho completo quando um cliente fornece seu número de celular e consentimento por meio da Quikly:
1. A Quikly realiza uma pesquisa de inscrição usando o [status do grupo de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) para ver se um determinado `phone` está inscrito em um `subscription_group_id`. Se houver uma inscrição, credite o usuário na ativação da Quikly. Nenhuma ação adicional é necessária.
2. O Quikly realiza uma pesquisa de usuário usando o [ponto de extremidade Exportar perfil de usuário por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para ver se existe um perfil de usuário com um determinado `email_address`. Se não houver nenhum usuário, crie um perfil somente de alias por meio do [ponto de extremidade]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) do Braze [`/users/track`, definindo o e-mail do usuário como o alias do usuário para fazer referência a esse usuário no futuro (já que o usuário não terá um ID externo).]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
3. Atualize o status da inscrição usando o [endpoint "Atualizar status do grupo de inscrições do usuário"]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

Para dar suporte aos fluxos de trabalho de inscrição por SMS de aceitação dupla existentes, a Quikly pode enviar um evento personalizado para o Braze em vez do fluxo de trabalho acima. Nesse caso, em vez de atualizar o status da inscrição diretamente, o [evento personalizado dispara o processo de dupla aceitação]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/), e o status da inscrição é monitorado periodicamente para verificar se o usuário fez a aceitação total antes de creditá-lo na ativação da Quikly.

{% alert important %}
O Braze aconselha que, ao criar novos usuários por meio do endpoint `/users/track`, deve haver uma postergação de cerca de 2 minutos antes de adicionar usuários ao grupo de inscrições relevante para dar tempo ao Braze de criar completamente o perfil do usuário.
{% endalert %}

{% details Solicitação detalhada /subscription/status/set  %}
#### Cabeçalhos da solicitação
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Corpo da solicitação
```
{
  "subscription_group_id": "the-id-of-the-subscription-group",
    "subscription_status": "subscribed",
    "phone": "+13135551212"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab Atributos personalizados %}
### Atributos personalizados

Dependendo da sua implementação da Braze, você pode querer que os eventos dentro da ativação da Quikly passem em cascata pela Braze para processamento adicional. Por exemplo, você pode querer aplicar um atributo personalizado de usuário com base no nível ou incentivo alcançado na ativação do Quikly, permitindo que você exiba o cartão de conteúdo relevante quando eles abrirem o app ou registrarem o site. A Quikly trabalhará diretamente com você para implementar essas integrações.

{% endtab %}
{% tab Webhooks %}
### Webhooks
Use webhooks para disparar incentivos para eventos específicos na jornada do cliente. Por exemplo, se você tiver um evento Braze para quando um usuário registrar de usuários de eventos em seu app, ativar notificações push baseadas em localização ou usar o localizador de sua loja, poderá usar um webhook para disparar uma oferta personalizada para esse usuário com base na configuração de uma ativação específica da Quikly. Exemplos de táticas incluem recompensas com uma oferta personalizada para o primeiro número X de usuários que realizarem uma ação (como o registro no seu app) ou uma oferta que diminui de valor à medida que o tempo passa para motivar uma resposta imediata.

### Criar um webhook da Quikly no Braze

Para criar um modelo de webhook da Quikly para futuras campanhas ou Canvas, navegue até **Modelos** > **Modelos de webhook** na plataforma Braze. 

Se quiser criar uma campanha única de webhook da Quikly ou usar um modelo existente, selecione **Webhook** no Braze ao criar uma nova campanha.

Selecione **Modelo em branco** e digite o seguinte para o URL do webhook e o corpo da solicitação:
- **URL do webhook**: https://api.quikly.com/webhook/braze
- **Corpo da solicitação**: Pares de chave/valor JSON

#### Cabeçalhos de solicitação e método

O Quikly exige um `HTTP Header` para autorização.

- **Método HTTP**: POST
- **Cabeçalho da solicitação**:
  - **Autorização**: Portador [PARTNER_AUTHORIZATION_HEADER]
  - **Content-Type**: application/json

#### Corpo da solicitação

Selecione ***JSON key/value pairs*** (Pares de chave/valor JSON) e adicione os seguintes pares:
{% raw %}
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}
```
{% endraw %}

### veja uma prévia da sua solicitação

Pré-visualize a solicitação no painel **Preview (Pré-visualização** ) ou navegue até a guia `Test`, onde é possível selecionar um usuário aleatório, um usuário existente ou personalizar o seu próprio usuário para testar o webhook.

{% alert important %}
Lembre-se de salvar seu modelo antes de sair da página! <br>Os modelos de webhook atualizados podem ser encontrados na lista **Modelos de webhook salvos** ao criar uma nova [campanha de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

{% endtab %}
{% endtabs %}

## Suporte
Entre em contato com o gerente de sucesso do cliente da Quikly se tiver alguma dúvida.


