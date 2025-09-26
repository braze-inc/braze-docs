---
nav_title: "Grupos de inscrições"
article_title: Grupos de inscrições de SMS e RCS
page_order: 1
description: "Este artigo de referência aborda grupos de inscrições, estados de inscrições e o processo de configuração de grupos de inscrições para canais SMS, MMS e RCS."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS
  
---

# Grupos de inscrições de SMS e RCS

> Os grupos de inscrições são a base para o envio de mensagens SMS, MMS e RCS pelo Braze. Um grupo de inscrições é uma coleção de [entidades de envio]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) (como remetentes verificados por RCS, códigos curtos de SMS, códigos longos de SMS ou IDs alfanuméricos de remetente de SMS) que são usados para um tipo específico de finalidade de envio de mensagens. Por exemplo, se uma marca planeja enviar mensagens SMS transacionais e promocionais, dois grupos de inscrições com pools separados de números de telefone para envio precisarão ser configurados no dashboard do Braze.

## Estados do grupo de inscrições

Há dois estados de inscrição para usuários de SMS e RCS: `subscribed` e `unsubscribed`. O estado da inscrição de um usuário reside no nível do grupo de inscrições e não é compartilhado entre grupos de inscrições, o que significa que um usuário pode ser `subscribed` em um grupo de inscrições transacional, mas `unsubscribed` em um promocional. Para as marcas, essa separação de estados garante que elas possam continuar a enviar mensagens SMS e RCS relevantes para seus usuários.

| Status | Definição |
| --------- | ---------- |
| Inscreveu-se | O usuário confirmou explicitamente que deseja receber SMS e RCS de um grupo de inscrições específico. Um usuário pode se inscrever tendo seu estado de inscrição atualizado por meio da API de inscrição do Braze ou enviando uma mensagem de texto com uma resposta de palavra-chave de aceitação. Um usuário deve estar inscrito em um grupo de inscrições de SMS ou RCS para receber SMS, RCS ou ambos. |
| Cancelou inscrição | O usuário fez a aceitação explícita do envio de mensagens do seu grupo de inscrições de SMS e RCS e dos números de telefone de envio dentro do grupo de inscrições. Eles podem cancelar a inscrição enviando uma mensagem de texto com uma palavra-chave de aceitação ou uma marca pode cancelar a inscrição de usuários por meio da [API de inscrição do Braze]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/). Os usuários que cancelarem a inscrição de um grupo de inscrições de SMS e RCS não receberão mais SMS ou RCS do envio de números de telefone que pertencem ao grupo de inscrições.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Definição do estado de um usuário

Quando um número de telefone é atualizado em um perfil de usuário, o novo número de telefone herda o status do grupo de inscrições do usuário. Se o número de telefone for atualizado para um número que já existe no Braze, o status da inscrição desse número de telefone existente será herdado.

Por exemplo, se o usuário A tiver um número de telefone inscrito em vários grupos de inscrições e esse número de telefone for adicionado ao usuário B, o usuário B será inscrito nos mesmos grupos de inscrições. Para evitar que um usuário herde as inscrições existentes, você pode redefinir os grupos de inscrições do número antigo por meio da Braze REST API sempre que um usuário alterar seu número. Se vários usuários compartilharem esse número de telefone, todos eles terão a inscrição cancelada.

Para definir o estado do grupo de inscrições de um usuário, use um dos seguintes métodos:

- **API REST:** Os perfis de usuário podem ser definidos programaticamente pelo ponto de extremidade [`/subscription/status/set`] ({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) usando a Braze REST API.
- **Integração de SDK** Os usuários podem ser adicionados a um grupo de inscrições para e-mail ou SMS e RCS usando o método `addToSubscriptionGroup` para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Tratada automaticamente na aceitação/exclusão do usuário:** Quando os usuários enviam uma mensagem de texto com uma [palavra-chave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/) padrão de aceitação ou não aceitação, o Braze define e atualiza automaticamente o estado da inscrição dos usuários.
- **Importação de usuário**: Os usuários podem ser adicionados a grupos de inscrições para e-mail ou SMS e RCS por meio da **importação de usuários**. Ao atualizar o status do grupo de inscrições, você deve ter estas duas colunas em seu CSV: `subscription_group_id` e `subscription_state`. Para saber mais, consulte [Importação de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status).

### Verificação do grupo de um usuário

Para verificar o grupo de inscrições de um usuário, use um dos seguintes métodos:

- **Perfil do usuário:** Os perfis de usuários individuais podem ser acessados por meio do dashboard do Braze, selecionando **User Search** na barra lateral. Aqui, é possível procurar perfis de usuários por endereço de e-mail, número de telefone ou ID de usuário externo. Dentro de um perfil de usuário, na guia Engajamento, é possível visualizar os grupos de inscrições de SMS e RCS de um usuário. 
- **API REST:** O grupo de inscrições de perfis de usuários individuais pode ser visualizado pelo [endpoint Listar grupos de inscrições do]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) usuário ou pelo [endpoint Listar status do grupo de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) usando a Braze REST API. 

## Envio de mensagens com um grupo de inscrições

Para lançar uma campanha de SMS ou RCS por meio do Braze, selecione um grupo de inscrições no menu suspenso **SMS/MMS/RCS Variantes**. Depois de selecionado, um filtro de público será adicionado automaticamente à sua campanha ou Canva, garantindo que apenas os usuários `subscribed` do grupo de inscrições selecionado estejam no público-alvo.

{% alert important %}
Em conformidade com as [diretrizes e]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) a conformidade internacional [de telecomunicações]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/), o Braze nunca enviará SMS ou RCS a usuários que não tenham se inscrito no grupo de inscrições selecionado.  
{% endalert %}

![Criador de SMS com o menu suspenso do grupo de inscrições aberto e "Serviço de envio de mensagens A para SMS" destacado pelo usuário.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Ativação de grupos de inscrições

Para ativar os grupos de inscrições para SMS, MMS ou RCS, consulte o seguinte:

{% tabs local %}
{% tab SMS %}
Durante seu processo de integração de SMS, um gerente de integração do Braze configurará grupos de inscrições para sua conta dashboard. Eles trabalharão com você para determinar quantos grupos de inscrições você precisa e adicionarão os números de telefone de envio apropriados aos seus grupos de inscrições. Os prazos para a configuração de um grupo de inscrições dependerão do tipo de números de telefone que você está adicionando. Por exemplo, os aplicativos de código curto podem levar de 8 a 12 semanas, enquanto os códigos longos podem ser configurados em um dia. Se tiver dúvidas sobre a configuração do dashboard do Braze, entre em contato com o representante do Braze para obter suporte.  
{% endtab %}

{% tab MMS %}
Para enviar uma mensagem MMS, pelo menos um número em seu grupo de inscrições precisa estar ativado para enviar MMS. Isso é indicado por uma tag localizada ao lado do grupo de inscrições. 

![Grupo de inscrições com "Serviço de envio de mensagens A para SMS" destacado. A entrada é prefixada com a tag "MMS".]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Um remetente verificado pelo RCS deve estar presente em seu grupo de inscrições para que você possa enviar uma mensagem RCS. 

Há duas maneiras de adicionar um remetente verificado por RCS:
- Adicione-o a um grupo de inscrições existente
- Criar um novo grupo de inscrições RCS
A escolha depende muito dos casos de uso do RCS em que você está interessado. 

Dependendo da sua integração, o Braze pode adicionar remetentes verificados por RCS aos seus grupos de inscrições de SMS existentes ou configurar novos grupos de inscrições para você. Em qualquer um dos casos, o gerente de sucesso do cliente o orientará a fazer um upgrade eficiente e sem interrupções do tráfego de SMS.
{% endtab %}
{% endtabs %}

## Migração do tráfego de SMS para o RCS

Se tiver grupos de inscrições separados para SMS e RCS, poderá migrar usuários do SMS para o RCS usando uma etapa do Canva. 

A Braze recomenda que você teste o envio do RCS para volumes menores de usuários inicialmente e migre mais usuários para o grupo de inscrições do RCS ao longo do tempo. Por exemplo, se você tiver 1.000.000 de usuários inscritos em um grupo de inscrições de SMS, isso poderia ser feito primeiro migrando todos os usuários para o novo grupo de inscrições e, em seguida, segmentando um público menor de 50.000 a 100.000 (5-10%) para testar as mensagens RCS.

### Etapa 1: Crie uma tela e preencha o cronograma de entrada

Crie uma tela e dê a ela um nome facilmente identificável (como "SMS-RCS Subscription Group User Transfer"). Em seguida, agende a campanha quando for conveniente para você.

### Etapa 2: Defina seu público

Defina seu público usando um dos seguintes métodos. Em seguida, vá para a etapa **Send Settings (Configurações de envio** ) e selecione **Users who are subscribed or opted-in (Usuários inscritos ou com aceitação**).

| Método                          | Descrição                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Criar um segmento**         | Crie um segmento que inclua todos os usuários em um grupo de inscrições ou um subconjunto usando filtros de segmentação (e.g., um 5-10% aleatório). Os segmentos são atualizados antes de cada envio para refletir sua base de usuários atual.        |
| **Aplicar filtros de campanha ou do Canva** | Refine o público na etapa do **público-alvo** de sua campanha ou Canva. Ajuste as opções de direcionamento sem sair da página para maior flexibilidade.                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Etapa 3: Configurar uma etapa de atualização de usuário

Adicione uma etapa de atualização do usuário ao seu Canva. Na etapa, abra o **Advanced JSON Editor** e insira o seguinte (para o campo de identificador de usuário exclusivo, recomendamos usar o campo `braze_id` ):

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

!["Objeto de atualização do usuário" que contém o código JSON mencionado anteriormente.]({% image_buster /assets/img/sms/user_update_object.png %})

### Etapa 4: Teste a tela

É altamente recomendável [testar seu Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) para confirmar que ele funciona conforme o esperado antes de enviá-lo para seu público mais amplo.

### Etapa 5: Inicie seu canva

Depois de testar o Canva com sucesso, lance-o para o seu subconjunto de usuários!

Para confirmar que seus usuários foram migrados com sucesso, recomendamos verificar alguns perfis de usuários individuais que foram atualizados. Na guia **Engajamento**, procure **Configurações de contato** e role a tela para ver os grupos de inscrições nos quais o usuário está inscrito. O botão de alternância do grupo de inscrições RCS agora deve estar ativado.
