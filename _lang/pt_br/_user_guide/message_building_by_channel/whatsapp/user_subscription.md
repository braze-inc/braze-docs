---
nav_title: "Grupos de inscrições"
article_title: Grupos de inscrições de WhatsApp
page_order: 1
description: "Este artigo descreve os grupos de inscrições do WhatsApp, quais estados de inscrição são oferecidos e como os grupos de inscrições são definidos."
page_type: reference
channel:
  - WhatsApp
 
---

# Grupos de inscrições

> Os grupos de inscrições do WhatsApp são criados após a integração do WhatsApp com seu app por meio do **Technology Partner Portal**.

## Estados da inscrição no WhatsApp

Há dois estados de inscrição para usuários do WhatsApp: `subscribed` e `unsubscribed`.

| Status | Definição |
| --- | --- |
| Inscreveu-se | O usuário confirmou explicitamente que deseja receber mensagens do WhatsApp de uma empresa específica. Os usuários podem se inscrever tendo seu estado de inscrição atualizado por meio da API de inscrição do Braze ou implantando uma estratégia de aceitação, de acordo com as diretrizes do WhatsApp. |
| Cancelou inscrição | O usuário não deu consentimento explícito para aceitação ou seu status de aceitação foi explicitamente removido. <br><br> Os usuários que cancelarem a inscrição em um grupo de inscrições do WhatsApp não receberão mais mensagens do WhatsApp do envio de números de telefone que pertencem ao grupo de inscrições. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Configuração dos grupos de inscrições do WhatsApp dos usuários

- **API de descanso:** Os perfis de usuário podem ser definidos programaticamente pelo [endpoint`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) usando a Braze REST API.
- **SDK da Web:** Os usuários podem ser adicionados a um grupo de inscrições para e-mail, SMS ou WhatsApp usando o método `addToSubscriptionGroup` para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Importação de usuário**: Os usuários podem ser adicionados a grupos de inscrições para e-mail ou SMS por meio da **importação de usuários**. Ao atualizar o status do grupo de inscrições, você deve ter estas duas colunas em seu CSV: `subscription_group_id` e `subscription_state`. Para saber mais, consulte [Importação de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status).

### Verificação do grupo de inscrições do WhatsApp de um usuário

- **Perfil do usuário:** Os perfis de usuários individuais podem ser acessados no dashboard do Braze em **Público** > **Pesquisar usuários**. Aqui, é possível procurar perfis de usuários por endereço de e-mail, número de telefone ou ID de usuário externo. Quando estiver dentro de um perfil de usuário, na guia **Engajamento**, você poderá ver o grupo de inscrições do WhatsApp de um usuário e seu status.

- **API de descanso:** O grupo de inscrições de perfis de usuários individuais pode ser visualizado pelo [endpoint Listar grupos de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) ou pelo [endpoint Listar status do grupo de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) usando a API REST do Braze. 

## Processo de aceitação e recusa do WhatsApp

Atualmente, os usuários podem se inscrever e [optar pela aceitação e recusa]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/) ao envio de mensagens do WhatsApp de várias maneiras, incluindo [SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), através de um site, um thread do WhatsApp, telefone ou pessoalmente. Observe que a aceitação é obrigatória.

No momento, não há suporte para palavras-chave de aceitação para o canal do WhatsApp, portanto, caberá a você manter uma lista de usuários. O WhatsApp tem uma abordagem retrospectiva para aceitação e limites de frequência, ou seja, se os usuários começarem a denunciar ou bloquear você, seu limite de frequência será reduzido. 

## Atualização do status da inscrição de um usuário em um WhatsApp Canva {#update-subscription-status}

Independentemente dos métodos de aceitação e de exclusão usados, é possível atualizar o status da inscrição dos perfis de usuário com um dos seguintes métodos de atualização:

- Crie um [webhook Braze-to-Braze]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know) que atualize o status da inscrição via API REST, como no exemplo a seguir:

![Criador de webhook com uma mensagem usando o método POST.]({% image_buster /assets/img/whatsapp/whatsapp118.png %}){: style="max-width:90%;"}

Para evitar condições de corrida, qualquer envio de mensagens de acompanhamento após o webhook deve estar contido em um segundo Canvas que seja disparado por resultados do primeiro Canvas (como um usuário que tenha entrado em uma variação do Canvas e esteja em um grupo de inscrições do WhatsApp).

- Use o editor JSON avançado para atualizar o perfil do usuário com o seguinte modelo: 

	```json
	{
	  "attributes": [
	  {
	  	"subscription_groups": [{
	  	  "subscription_group_id": "subscription_group_identifier_1",
	  	  "subscription_state": "unsubscribed"
	  	   },
	  	   {
	  	     "subscription_group_id": "subscription_group_identifier_2",
	  	     "subscription_state": "subscribed"
	  	     },
	  	     {
	  	       "subscription_group_id": "subscription_group_identifier_3",
	  	       "subscription_state": "subscribed"
	  	    }
	  	  ]
	  	}
	  ]
	}
	```

![Etapa de atualização do usuário com uma etapa do Advanced JSON Editor.]({% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}){: style="max-width:90%;"}

{% alert note %}
As atualizações do status da inscrição de um usuário podem levar até 60 segundos.
{% endalert %}

