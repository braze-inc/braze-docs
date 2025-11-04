---
nav_title: "Grupos de assinatura"
article_title: Grupos de assinatura do WhatsApp
page_order: 1
description: "Este artigo descreve os grupos de assinatura do WhatsApp, quais estados de assinatura são oferecidos e como os grupos de assinatura são definidos."
page_type: reference
alias: /whatsapp_subscription_groups/
channel:
  - WhatsApp
 
---

# Grupos de assinatura

> Os grupos de assinatura do WhatsApp são criados após a integração do WhatsApp com seu aplicativo por meio do **Technology Partner Portal**.

## Estados de assinatura do WhatsApp

Há dois estados de assinatura para usuários do WhatsApp: `subscribed` e `unsubscribed`.

| Estado | Definição |
| --- | --- |
| Assinatura | O usuário confirmou explicitamente que deseja receber mensagens do WhatsApp de uma empresa específica. Os usuários podem se inscrever tendo seu estado de assinatura atualizado por meio da API de assinatura do Braze ou implantando uma estratégia de opt-in, de acordo com as diretrizes do WhatsApp. |
| Cancelamento da inscrição | O usuário não deu consentimento explícito para o opt-in ou seu status de opt-in foi explicitamente removido. <br><br> Os usuários que cancelarem a assinatura de um grupo de assinatura do WhatsApp não receberão mais mensagens do WhatsApp do envio de números de telefone que pertencem ao grupo de assinatura. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Configuração dos grupos de assinatura do WhatsApp dos usuários

- **API de descanso:** Os perfis de usuário podem ser definidos de forma programática pelo [endpoint`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) usando a Braze REST API.
- **SDK da Web:** Os usuários podem ser adicionados a um grupo de assinatura de e-mail, SMS ou WhatsApp usando o método `addToSubscriptionGroup` para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Importação do usuário**: Os usuários podem ser adicionados a grupos de assinatura de e-mail ou SMS por meio da opção **Importar usuários**. Ao atualizar o status do grupo de assinaturas, você deve ter estas duas colunas em seu CSV: `subscription_group_id` e `subscription_state`. Consulte [Importação do usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) para obter mais informações.

### Verificação do grupo de assinatura do WhatsApp de um usuário

- **Perfil do usuário:** Os perfis de usuários individuais podem ser acessados no painel do Braze em **Audience** > **Search Users**. Aqui, você pode procurar perfis de usuários por endereço de e-mail, número de telefone ou ID de usuário externo. Quando estiver dentro de um perfil de usuário, na guia **Envolvimento**, você poderá visualizar o grupo de assinatura do WhatsApp de um usuário e seu status.

- **API de descanso:** O grupo de assinatura de perfis de usuários individuais pode ser visualizado pelo [ponto de extremidade Listar grupos de assinatura do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) ou pelo [ponto de extremidade Listar status do grupo de assinatura do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) usando a API REST do Braze. 

## Processo de ativação e desativação do WhatsApp

Atualmente, os usuários podem se inscrever e [optar por participar ou não das]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/) mensagens do WhatsApp de várias maneiras, incluindo [SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), por meio de um site, um tópico do WhatsApp, telefone ou pessoalmente. Observe que os opt-ins são obrigatórios.

No momento, não há suporte para palavras-chave opt-in para o canal do WhatsApp, portanto, caberá a você manter uma lista de usuários. O WhatsApp tem uma abordagem retrospectiva para opt-ins e limites de taxa, em que, se os usuários começarem a denunciar ou bloquear você, seu limite de taxa será reduzido. 

## Atualização do status de assinatura de um usuário em um WhatsApp Canvas {#update-subscription-status}

Independentemente dos métodos de opt-in e opt-out usados, é possível atualizar o status da assinatura dos perfis de usuário com um dos seguintes métodos de atualização:

- Crie um [webhook Braze-to-Braze]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know) que atualize o status da assinatura por meio da API REST, como no exemplo a seguir:

\![Compositor de webhook com uma mensagem usando o método POST.]({% image_buster /assets/img/whatsapp/whatsapp118.png %}){: style="max-width:90%;"}

Para evitar condições de corrida, qualquer mensagem de acompanhamento após o webhook deve estar contida em um segundo Canvas que seja acionado por resultados do primeiro Canvas (por exemplo, um usuário entrou em uma variação do Canvas e está em um grupo de assinatura do WhatsApp).

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

Etapa de atualização do usuário com uma etapa do Advanced JSON Editor.]({% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}){: style="max-width:90%;"}

{% alert note %}
As atualizações do status da assinatura de um usuário podem levar até 60 segundos.
{% endalert %}

