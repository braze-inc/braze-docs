---
nav_title: "Grupos de inscrição de SMS"
article_title: Grupos de inscrição de SMS
page_order: 4
description: "Este artigo de referência aborda os grupos de inscrições de SMS, os estados das inscrições e o processo de configuração do grupo de inscrições."
page_type: reference
channel:
  - SMS
  
---

# Grupos de inscrições de SMS

> Os grupos de inscrições são a base para o envio de SMS e MMS pelo Braze. Um grupo de inscrições é uma coleção de [envio de números de telefone][2] (como códigos curtos, códigos longos e/ou IDs de remetente alfanuméricos) que são usados para um tipo específico de finalidade de envio de mensagens. Por exemplo, se uma marca planeja enviar mensagens SMS transacionais e promocionais, dois grupos de inscrições com pools separados de números de telefone para envio precisarão ser configurados no dashboard do Braze.

## Estados de inscrição de SMS

Há dois estados de inscrição para usuários de SMS: `subscribed` e `unsubscribed`. O estado de inscrição de um usuário não é compartilhado entre grupos de inscrições, o que significa que um usuário pode ser `subscribed` em um grupo de inscrições transacionais, mas `unsubscribed` em um grupo promocional. Para as marcas, essa separação de estados garante que elas possam continuar a enviar mensagens SMS relevantes para seus usuários.

| Status | Definição |
| --------- | ---------- |
| Inscreveu-se | O usuário confirmou explicitamente que deseja receber SMS de um grupo de inscrições específico. Um usuário pode se inscrever tendo seu estado de inscrição atualizado por meio da API de inscrição do Braze ou enviando uma mensagem de texto com uma resposta de palavra-chave de aceitação. Um usuário deve estar inscrito em um grupo de inscrições de SMS para receber um SMS. |
| Cancelou inscrição | O usuário fez a aceitação explícita do envio de mensagens do seu grupo de inscrições de SMS e dos números de telefone de envio dentro do grupo de inscrições. Eles podem cancelar a inscrição enviando uma mensagem de texto com uma palavra-chave de aceitação ou uma marca pode cancelar a inscrição de usuários por meio da [API de inscrição da Braze][4]. Os usuários que cancelarem a inscrição em um grupo de inscrições de SMS não receberão mais SMS de números de telefone pertencentes ao grupo de inscrições.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Como os grupos de inscrições de SMS dos usuários são definidos 

- **Rest API:** Os perfis de usuário podem ser definidos programaticamente pelo endpoint [`/subscription/status/set`][4] usando a REST API da Braze.
- **Integração de SDK** Os usuários podem ser adicionados a um grupo de inscrições para e-mail ou SMS usando o método `addToSubscriptionGroup` para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web][11].
- **Tratada automaticamente na aceitação/exclusão do usuário:** Quando os usuários enviam uma mensagem de texto com a opção de aceitação ou aceitação [palavra-chave][7]], a Braze define e atualiza automaticamente o estado da inscrição dos usuários.
- **Importação de usuário**: Os usuários podem ser adicionados a grupos de inscrições para e-mail ou SMS por meio da **importação de usuários**. Ao atualizar o status do grupo de inscrições, você deve ter estas duas colunas em seu CSV: `subscription_group_id` e `subscription_state`. Para saber mais, consulte [Importação de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status).

Quando um número de telefone é atualizado em um perfil de usuário, o novo número de telefone herda o status do grupo de inscrições do usuário. Se o número de telefone for atualizado para um número que já existe no Braze, o status da inscrição desse número de telefone existente será herdado.

Por exemplo, se o usuário A tiver um número de telefone inscrito em vários grupos de inscrições e esse número de telefone for adicionado ao usuário B, o usuário B será inscrito nos mesmos grupos de inscrições. Para evitar que um usuário herde as inscrições existentes, é possível redefinir os grupos de inscrições do número antigo via API REST sempre que um usuário alterar seu número. Se vários usuários compartilharem esse número de telefone, todos eles terão a inscrição cancelada.

### Como verificar o grupo de inscrições de SMS de um usuário

- **Perfil do usuário:** Os perfis de usuários individuais podem ser acessados por meio do dashboard da Braze, selecionando User Search na barra lateral. Aqui, é possível procurar perfis de usuários por endereço de e-mail, número de telefone ou ID de usuário externo. Em um perfil de usuário, na guia Engajamento, é possível visualizar os grupos de inscrições de SMS de um usuário. 
- **Rest API:** O grupo de inscrições de perfis de usuários individuais pode ser visualizado pelo [endpoint Listar grupos de inscrições do usuário][9] ou [endpoint Listar status de grupos de inscrições do usuário][8] usando a REST API da Braze. 

## Envio com um grupo de inscrições

Para lançar uma campanha de SMS por meio do Braze, um grupo de inscrições deve ser selecionado no menu suspenso, conforme mostrado na imagem a seguir. Depois de selecionado, um filtro de público será adicionado automaticamente à sua campanha ou Canva, garantindo que apenas os usuários `subscribed` do grupo de inscrições selecionado estejam no público-alvo. Para aderir às diretrizes e à conformidade internacional [de telecomunicações][3]], o Braze nunca enviará SMS a usuários que não tenham se inscrito no grupo de inscrições selecionado.  

![Criador de SMS com o menu suspenso do grupo de inscrições aberto e "Serviço de envio de mensagens A para SMS" destacado pelo usuário.][6]

## Processo de configuração

Durante seu processo de integração de SMS, um gerente de integração do Braze configurará grupos de inscrições para sua conta dashboard. Eles trabalharão com você para determinar quantos grupos de inscrições você precisa e adicionarão os números de telefone de envio apropriados aos seus grupos de inscrições. Os prazos para a configuração de um grupo de inscrições dependerão do tipo de números de telefone que você está adicionando. Por exemplo, os aplicativos de código curto podem levar de 8 a 12 semanas, enquanto os códigos longos podem ser configurados em um dia. Se tiver dúvidas sobre a configuração do dashboard do Braze, entre em contato com o representante do Braze para obter suporte.  

## Capacitação do grupo de inscrições MMS

Para enviar uma mensagem MMS, pelo menos um número em seu grupo de inscrições precisa estar ativado para enviar MMS. Isso é indicado por uma tag localizada ao lado do grupo de inscrições. 

![Grupo de inscrições com "Serviço de envio de mensagens A para SMS" destacado. A entrada é prefixada com a tag "MMS".][10]{: style="max-width:40%"}


[1]: {% image_buster /assets/img/sms/multi_country_subgroups.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/
[4]: {{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[6]: {% image_buster /assets/img/sms/sms_subgroup_select.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[10]: {% image_buster /assets/img/sms/mms_sub_group_tag.png %}
Daqui a [11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
