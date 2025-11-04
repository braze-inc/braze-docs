---
nav_title: "Grupos de assinatura"
article_title: Grupos de assinatura de SMS e RCS
page_order: 1
description: "Este artigo de referência aborda grupos de assinatura, estados de assinatura e o processo de configuração de grupos de assinatura para canais SMS, MMS e RCS."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS
  
---

# Grupos de assinatura de SMS e RCS

> Os grupos de assinatura são a base para o envio de mensagens SMS, MMS e RCS pelo Braze. Um grupo de assinatura é uma coleção de [entidades de envio]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) (como remetentes verificados pelo RCS, códigos curtos de SMS, códigos longos de SMS ou IDs alfanuméricos de remetente de SMS) que são usados para um tipo específico de finalidade de mensagem. Por exemplo, se uma marca tiver planos de enviar mensagens SMS transacionais e promocionais, será necessário configurar dois grupos de assinatura com conjuntos separados de números de telefone de envio no painel do Braze.

## Estados do grupo de assinaturas

Há dois estados de assinatura para usuários de SMS e RCS: `subscribed` e `unsubscribed`. O estado da assinatura de um usuário reside no nível do grupo de assinatura e não é compartilhado entre grupos de assinatura, o que significa que um usuário pode ser `subscribed` em um grupo de assinatura transacional, mas `unsubscribed` em um grupo promocional. Para as marcas, essa separação de estados garante que elas possam continuar a enviar mensagens SMS e RCS relevantes para seus usuários.

| Estado | Definição |
| --------- | ---------- |
| Assinatura | O usuário confirmou explicitamente que deseja receber SMS e RCS de um grupo de assinatura específico. Um usuário pode se inscrever tendo seu estado de assinatura atualizado por meio da API de assinatura do Braze ou enviando uma mensagem de texto com uma resposta de palavra-chave de aceitação. Um usuário deve estar inscrito em um grupo de assinatura de SMS ou RCS para receber SMS, RCS ou ambos. |
| Cancelamento da inscrição | O usuário optou explicitamente por não receber mensagens do seu grupo de assinatura de SMS e RCS e dos números de telefone de envio dentro do grupo de assinatura. Eles podem cancelar a assinatura enviando uma mensagem de texto com uma palavra-chave de recusa ou uma marca pode cancelar a assinatura dos usuários por meio da [API de assinatura do Braze]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/). Os usuários que cancelarem a assinatura de um grupo de assinatura de SMS e RCS não receberão mais SMS ou RCS do envio de números de telefone que pertençam ao grupo de assinatura.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Definição do estado de um usuário

Quando um número de telefone é atualizado em um perfil de usuário, o novo número de telefone herda o status do grupo de assinatura do usuário. Se o número de telefone for atualizado para um número que já existe no Braze, o status de assinatura desse número de telefone existente será herdado.

Por exemplo, se o usuário A tiver um número de telefone inscrito em vários grupos de assinatura e esse número de telefone for adicionado ao usuário B, o usuário B será inscrito nos mesmos grupos de assinatura. Para evitar que um usuário herde as assinaturas existentes, você pode redefinir os grupos de assinatura do número antigo por meio da Braze REST API sempre que um usuário alterar seu número. Se vários usuários compartilharem esse número de telefone, todos eles terão a inscrição cancelada.

Para definir o estado do grupo de assinatura de um usuário, use um dos métodos a seguir:

- **API de descanso:** Os perfis de usuário podem ser definidos programaticamente pelo endpoint [\`/subscription/status/set\`]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) usando a Braze REST API.
- **Integração do SDK** Os usuários podem ser adicionados a um grupo de assinatura de e-mail ou SMS e RCS usando o método `addToSubscriptionGroup` para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Tratada automaticamente quando o usuário opta por entrar ou sair:** Quando os usuários enviam uma mensagem de texto com uma [palavra-chave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/) padrão de inclusão ou exclusão, o Braze define e atualiza automaticamente o estado da assinatura dos usuários.
- **Importação do usuário**: Os usuários podem ser adicionados a grupos de assinatura de e-mail ou SMS e RCS por meio da **opção Importar usuários**. Ao atualizar o status do grupo de assinaturas, você deve ter estas duas colunas em seu CSV: `subscription_group_id` e `subscription_state`. Consulte [Importação do usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) para obter mais informações.

### Verificação do grupo de um usuário

Para verificar o grupo de assinatura de um usuário, use um dos métodos a seguir:

- **Perfil do usuário:** Os perfis de usuários individuais podem ser acessados por meio do painel de controle do Braze, selecionando **Pesquisa de usuários** na barra lateral. Aqui, você pode procurar perfis de usuários por endereço de e-mail, número de telefone ou ID de usuário externo. Em um perfil de usuário, na guia Envolvimento, você pode visualizar os grupos de assinatura de SMS e RCS de um usuário. 
- **API de descanso:** O grupo de assinatura de perfis de usuários individuais pode ser visualizado pelo [ponto de extremidade Listar grupos de assinatura do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) ou pelo [ponto de extremidade Listar status do grupo de assinatura do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) usando a Braze REST API. 

## Envio de mensagens com um grupo de assinaturas

Para lançar uma campanha de SMS ou RCS por meio do Braze, selecione um grupo de assinatura no menu suspenso **Variantes de SMS/MMS/RCS**. Depois de selecionado, um filtro de público-alvo será adicionado automaticamente à sua campanha ou Canvas, garantindo que apenas os usuários `subscribed` do grupo de assinatura selecionado estejam no público-alvo.

{% alert important %}
Em conformidade com as [diretrizes e]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) a conformidade internacional [de telecomunicações]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/), o Braze nunca enviará SMS ou RCS a usuários que não tenham se inscrito no grupo de assinatura selecionado.  
{% endalert %}

\![SMS composer with the subscription group dropdown open and "Messaging Service A for SMS" highlighted by the user.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Ativação de grupos de assinatura

Para ativar grupos de assinatura para SMS, MMS ou RCS, consulte o seguinte:

{% tabs local %}
{% tab SMS %}
Durante o processo de integração de SMS, um gerente de integração do Braze definirá grupos de assinatura para sua conta do painel. Eles trabalharão com você para determinar quantos grupos de assinatura você precisa e adicionarão os números de telefone de envio apropriados aos seus grupos de assinatura. Os prazos para a configuração de um grupo de assinaturas dependerão do tipo de números de telefone que você está adicionando. Por exemplo, os aplicativos de código curto podem levar de 8 a 12 semanas, enquanto os códigos longos podem ser configurados em um dia. Se tiver dúvidas sobre a configuração do painel de controle da Braze, entre em contato com o representante da Braze para obter suporte.  
{% endtab %}

{% tab MMS %}
Para enviar uma mensagem MMS, pelo menos um número em seu grupo de assinaturas deve estar habilitado para enviar MMS. Isso é indicado por uma tag localizada ao lado do grupo de assinaturas. 

Grupo de assinatura com "Serviço de mensagens A para SMS" destacado. A entrada é prefixada com a tag "MMS".]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Um remetente verificado pelo RCS deve estar presente em seu grupo de assinaturas para que você possa enviar uma mensagem RCS. 

Há duas maneiras de adicionar um remetente verificado por RCS:
- Adicione-o a um grupo de assinaturas existente
- Criar um novo grupo de assinatura RCS
A escolha depende muito dos casos de uso do RCS nos quais você está interessado. 

Dependendo da sua integração, o Braze pode adicionar remetentes verificados por RCS aos seus grupos de assinatura de SMS existentes ou configurar novos grupos de assinatura para você. Em qualquer um dos casos, o gerente de sucesso do cliente o orientará em um upgrade de tráfego de SMS eficiente e sem interrupções.
{% endtab %}
{% endtabs %}

## Migração do tráfego de SMS para o RCS

Se você tiver grupos de assinatura SMS e RCS separados, poderá migrar usuários do SMS para o RCS usando o Canvas em uma única etapa. 

A Braze recomenda que você teste o envio de RCS para volumes menores de usuários inicialmente e migre mais usuários para o grupo de assinatura RCS ao longo do tempo. Por exemplo, se você tiver 1.000.000 de usuários inscritos em um grupo de assinaturas de SMS, isso poderia ser feito primeiro migrando todos os usuários para o novo grupo de assinaturas e, em seguida, segmentando um público menor de 50.000 a 100.000 (5-10%) para testar as mensagens RCS.

### Etapa 1: Crie um Canvas e preencha o cronograma de entrada

Crie um Canvas e dê a ele um nome facilmente identificável (por exemplo, "SMS-RCS Subscription Group User Transfer"). Em seguida, agende a campanha quando for conveniente para você.

### Etapa 2: Defina seu público-alvo

Defina seu público-alvo usando um dos métodos a seguir. Em seguida, vá para a etapa **Send Settings (Configurações de envio** ) e selecione **Users who are subscribed or opted-in (Usuários que estão inscritos ou optaram por participar**).

| Método                          | Descrição                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Criar um segmento**         | Crie um segmento que inclua todos os usuários em um grupo de assinatura ou um subconjunto usando filtros de segmentação (e.g., 5-10% aleatórios). Os segmentos são atualizados antes de cada envio para refletir sua base de usuários atual.        |
| **Aplicar filtros de campanha ou de tela** | Refine o público-alvo na etapa **Público-alvo** de sua campanha ou Canvas. Ajuste as opções de direcionamento sem sair da página para maior flexibilidade.                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Etapa 3: Configurar uma etapa de atualização de usuário

Adicione uma etapa de atualização do usuário ao seu Canvas. Na etapa, abra o **Advanced JSON Editor** e insira o seguinte (para o campo de identificador de usuário exclusivo, recomendamos usar o campo `braze_id` ):

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

\!["Objeto de atualização do usuário" que contém o código JSON mencionado anteriormente.]({% image_buster /assets/img/sms/user_update_object.png %})

### Etapa 4: Teste o Canvas

É altamente recomendável [testar seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) para confirmar se ele funciona conforme o esperado antes de enviá-lo para seu público mais amplo.

### Etapa 5: Inicie seu Canvas

Depois de testar o Canvas com sucesso, lance-o para o seu subconjunto de usuários!

Para confirmar que seus usuários foram migrados com sucesso, recomendamos verificar alguns perfis de usuários individuais que foram atualizados. Na guia **Envolvimento**, procure **Configurações de contato** e role a tela para ver os grupos de assinatura nos quais o usuário está inscrito. O botão de alternância do grupo de assinatura RCS deve estar ativado.
