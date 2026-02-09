---
nav_title: "Grupos de inscrições"
article_title: Grupos de Inscrição SMS e RCS
page_order: 1
description: "Este artigo de referência cobre grupos de inscrição, estados de inscrição e o processo de configuração de grupos de inscrição para canais SMS, MMS e RCS."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS
  
---

# Grupos de inscrição SMS e RCS

> Os grupos de inscrição são a base para o envio de mensagens SMS, MMS e RCS através do Braze. Um grupo de inscrição é uma coleção de [entidades de envio]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) (como remetentes verificados por RCS, códigos curtos SMS, códigos longos SMS ou IDs de remetente alfanuméricos SMS) que são usados para um tipo específico de propósito de envio de mensagens. Por exemplo, se uma marca planeja enviar mensagens SMS transacionais e promocionais, dois grupos de inscrições com pools separados de números de telefone para envio precisarão ser configurados no dashboard do Braze.

## Estados de grupos de inscrição

Existem dois estados de inscrição para usuários SMS e RCS: `subscribed` e `unsubscribed`. O estado de inscrição de um usuário reside no nível do grupo de inscrição e não é compartilhado entre grupos de inscrição, o que significa que um usuário pode estar `subscribed` em um grupo de inscrição transacional, mas `unsubscribed` em um promocional. Para as marcas, essa separação de estados garante que elas possam continuar a enviar mensagens SMS e RCS relevantes para seus usuários.

| Status | Definição |
| --------- | ---------- |
| Inscreveu-se | O usuário confirmou explicitamente que deseja receber SMS e RCS de um grupo de inscrição específico. Um usuário pode se inscrever tendo seu estado de inscrição atualizado por meio da API de inscrição do Braze ou enviando uma mensagem de texto com uma resposta de palavra-chave de aceitação. Um usuário deve estar inscrito em um grupo de inscrição SMS ou RCS para receber SMS, RCS ou ambos. |
| Cancelou inscrição | O usuário optou explicitamente por não receber mensagens do seu grupo de inscrição SMS e RCS e dos números de telefone de envio dentro do grupo de inscrição. Eles podem cancelar a inscrição enviando uma mensagem de texto com uma palavra-chave de aceitação ou uma marca pode cancelar a inscrição de usuários por meio da [API de inscrição da Braze]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/). Usuários que cancelaram a inscrição de um grupo de inscrição SMS e RCS não receberão mais SMS ou RCS de números de telefone de envio que pertencem ao grupo de inscrição.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Definindo o estado de um usuário

Quando um número de telefone é atualizado em um perfil de usuário, o novo número de telefone herda o status do grupo de inscrições do usuário. Se o número de telefone for atualizado para um número que já existe no Braze, o status da inscrição desse número de telefone existente será herdado.

Por exemplo, se o usuário A tiver um número de telefone inscrito em vários grupos de inscrições e esse número de telefone for adicionado ao usuário B, o usuário B será inscrito nos mesmos grupos de inscrições. Para evitar que um usuário herde as inscrições existentes, você pode redefinir os grupos de inscrição do número antigo através da API REST do Braze sempre que um usuário mudar seu número. Se vários usuários compartilharem esse número de telefone, todos eles terão a inscrição cancelada.

Para definir o estado do grupo de inscrição de um usuário, use um dos seguintes métodos:

- **API REST:** Os perfis de usuário podem ser definidos programaticamente pelo endpoint [\`/subscription/status/set\`]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) usando a API REST do Braze.
- **Integração de SDK** Usuários podem ser adicionados a um grupo de inscrição de e-mail ou SMS e RCS usando o método `addToSubscriptionGroup` para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Tratada automaticamente na aceitação/exclusão do usuário:** Ao os usuários enviarem um opt-in ou opt-out padrão [palavra-chave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/), o Braze define e atualiza automaticamente o estado de inscrição dos usuários.
- **Importação de usuário**: Usuários podem ser adicionados a grupos de inscrição de e-mail ou SMS e RCS através de **Importar Usuários**. Ao atualizar o status do grupo de inscrições, você deve ter estas duas colunas em seu CSV: `subscription_group_id` e `subscription_state`. Para saber mais, consulte [Importação de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status).

### Verificando o grupo de um usuário

Para verificar o grupo de inscrição de um usuário, use um dos seguintes métodos:

- **Perfil do usuário:** Perfis de usuários individuais podem ser acessados através do dashboard do Braze selecionando **Pesquisa de Usuário** na barra lateral. Aqui, é possível procurar perfis de usuários por endereço de e-mail, número de telefone ou ID de usuário externo. Quando dentro de um perfil de usuário, na guia de Engajamento, você pode visualizar os grupos de inscrição de SMS e RCS de um usuário. 
- **API REST:** O grupo de inscrições de perfis de usuários individuais pode ser visualizado pelo [endpoint Listar grupos de inscrições do]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) usuário ou pelo [endpoint Listar status do grupo de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) usando a Braze REST API. 

## Enviando mensagens com um grupo de inscrição

Para lançar uma campanha de SMS ou RCS através do Braze, selecione um grupo de inscrição no menu suspenso **Variações de SMS/MMS/RCS**. Depois de selecionado, um filtro de público será adicionado automaticamente à sua campanha ou Canva, garantindo que apenas os usuários `subscribed` do grupo de inscrições selecionado estejam no público-alvo.

{% alert important %}
Em conformidade com as [normas e diretrizes de telecomunicações internacionais]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/), o Braze nunca enviará SMS ou RCS para usuários que não se inscreveram no grupo de inscrição selecionado.  
{% endalert %}

![Criador de SMS com o menu suspenso do grupo de inscrições aberto e "Serviço de envio de mensagens A para SMS" destacado pelo usuário.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Ativando grupos de inscrição

Para ativar grupos de inscrição para SMS, MMS ou RCS, consulte o seguinte:

{% tabs local %}
{% tab SMS %}
Durante seu processo de integração de SMS, um gerente de integração do Braze configurará grupos de inscrições para sua conta dashboard. Eles trabalharão com você para determinar quantos grupos de inscrições você precisa e adicionarão os números de telefone de envio apropriados aos seus grupos de inscrições. Os prazos para a configuração de um grupo de inscrições dependerão do tipo de números de telefone que você está adicionando. Por exemplo, os aplicativos de código curto podem levar de 8 a 12 semanas, enquanto os códigos longos podem ser configurados em um dia. Se você tiver dúvidas sobre a configuração do seu dashboard do Braze, entre em contato com seu representante do Braze para suporte.  
{% endtab %}

{% tab MMS %}
Para enviar uma mensagem MMS, pelo menos um número em seu grupo de inscrições precisa estar ativado para enviar MMS. Isso é indicado por uma tag localizada ao lado do grupo de inscrições. 

![Grupo de inscrições com "Serviço de envio de mensagens A para SMS" destacado. A entrada é prefixada com a tag "MMS".]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Um remetente verificado de RCS deve estar presente dentro do seu grupo de inscrição antes que você possa enviar uma mensagem RCS. 

Existem duas maneiras de adicionar um remetente verificado de RCS:
- Adicione-o a um grupo de inscrição existente
- Crie um novo grupo de inscrição de RCS
A escolha depende em grande parte dos casos de uso de RCS que você está interessado. 

Dependendo da sua integração, o Braze pode adicionar remetentes verificados de RCS aos seus grupos de inscrição de SMS existentes ou configurar novos grupos de inscrição para você. Em qualquer um dos casos, seu gerente de sucesso do cliente irá guiá-lo através de uma atualização de tráfego de SMS tranquila e eficiente.
{% endtab %}
{% endtabs %}

## Migrando tráfego de SMS para RCS

Se você tiver grupos de inscrição de SMS e RCS separados, pode migrar usuários de SMS para RCS usando um Canvas de uma etapa. 

O Braze recomenda que você teste o envio de RCS para volumes menores de usuários inicialmente e migre mais usuários para o grupo de inscrição de RCS ao longo do tempo. Por exemplo, se você tiver 1.000.000 de usuários inscritos em um grupo de inscrições por SMS, isso poderia parecer primeiro migrar todos os usuários para o novo grupo de inscrições e, em seguida, segmentar um público menor de 50.000 a 100.000 (5-10%) para testar as mensagens RCS.

### Etapa 1: Crie um Canva e preencha o Cronograma de Entrada

Crie um Canva e nomeie-o de forma que seja facilmente identificável (como "Transferência de Usuários do Grupo de Inscrições SMS-RCS"). Em seguida, agende a campanha sempre que for conveniente para você.

### Etapa 2: Defina seu público

Defina seu público usando um dos seguintes métodos. Em seguida, acesse a etapa **Configurações de Envio** e selecione **Usuários que estão inscritos ou optaram por participar**.

| Método                          | Descrição                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Criar um segmento**         | Construa um segmento que inclua todos os usuários em um grupo de inscrições ou um subconjunto usando filtros de segmentação (como 5-10% aleatórios). Os segmentos são atualizados antes de cada envio para refletir sua base de usuários atual.        |
| **Aplicar filtros de campanha ou Canva** | Refine o público na etapa **Público-Alvo** da sua campanha ou Canva. Ajuste as opções de direcionamento sem sair da página para maior flexibilidade.                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Etapa 3: Configure uma etapa de Atualização de Usuário

Adicione uma Etapa de Atualização de Usuário ao seu Canva. Na etapa, abra o **Editor JSON Avançado** e insira o seguinte (para o campo de identificador único do usuário, recomendamos usar o campo `braze_id`):

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

!["Objeto de Atualização de Usuário" que contém o código JSON mencionado anteriormente.]({% image_buster /assets/img/sms/user_update_object.png %})

### Etapa 4: Teste o Canva

Recomendamos fortemente [testar seu Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) para confirmar que funciona como esperado antes de enviá-lo ao seu público mais amplo.

### Etapa 5: Inicie seu canva

Depois de ter testado com sucesso seu Canva, vá em frente e lance-o para seu subconjunto de usuários!

Para confirmar que seus usuários foram migrados com sucesso, recomendamos verificar alguns perfis de usuários individuais que foram atualizados. Na guia **engajamento**, procure por **Configurações de Contato** e role para ver os grupos de inscrições aos quais o usuário está inscrito. O interruptor do grupo de inscrições RCS deve estar ativado agora.
