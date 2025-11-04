---
nav_title: Olo
article_title: Olo
description: "Este artigo descreve a parceria entre a Braze e a Olo, uma plataforma SaaS aberta líder para restaurantes que permite hospitalidade em cada ponto de contato."
alias: /partners/olo/
page_type: partner
search_tag: Partner
---

# Olo

> A [Olo](https://www.olo.com/) é uma plataforma SaaS aberta líder para restaurantes que permite hospitalidade em cada ponto de contato.

Ao integrar Olo e Braze, você pode:

- Atualize os perfis de usuário no Braze para mantê-los consistentes com os perfis de usuário do Olo
- Enviar a próxima melhor mensagem pela Braze com base nos eventos da Olo

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Olo | Uma conta Olo com acesso a webhooks é necessária para aproveitar esta parceria. Configure assinaturas de webhook através da [ferramenta de webhooks de autoatendimento](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) no dashboard da Olo. |
| Transformação de Dados Braze | Uma [URL de Transformação de Dados]({{site.baseurl}}/data_transformation/) é necessária para receber dados do Olo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Um webhook é uma maneira de Olo enviar informações acionadas por eventos para a Braze sobre os usuários e suas ações, incluindo eventos como Pedido Realizado, Convidado Optou Por Participar, Pedido Retirado e mais. O Webhook Olo entrega o evento para a Braze geralmente em segundos após a ação ser realizada.

## Aviso Legal

No Olo, você está limitado a um webhook por ambiente para cada marca aprovada, todos enviados para o mesmo **URL de Destino**. Marcas diferentes podem ter URLs diferentes, mas eventos da mesma marca devem compartilhar uma URL. No Braze, isso significa que você pode fazer apenas uma transformação para usar com Olo.

Para lidar com vários eventos Olo dentro desta única transformação, procure o cabeçalho `X-Olo-Event-Type` em cada webhook. Este cabeçalho permite processar condicionalmente diferentes eventos Olo.

## Integração

### Etapa 1: Configure a transformação de dados do Braze para aceitar o evento de teste do Olo {#step-1}

{% multi_lang_include create_transformation.md local="default" %}

### Etapa 2: Configurar webhooks Olo

Use a ferramenta de webhooks [self-service](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) no dashboard da Olo para configurar webhooks para enviar para sua Transformação de Dados.

1. Escolha quais eventos devem ser enviados para Braze
2. Configure a **URL de Destino**. Este será o URL de transformação de dados criado na [etapa 1](#step-1).

{% alert note %}
`OAuth` e o segredo compartilhado do cabeçalho `X-Olo-Signature` não são necessários para a transformação.
{% endalert %}

{:start="3"}
3\. Verifique se o webhook está configurado corretamente enviando um [Evento de Teste](https://developer.olo.com/docs/load/webhooks#operation/test) para sua Transformação de Dados. Somente os usuários do dashboard Olo com a [permissão de Ferramentas de Desenvolvedor](https://olosupport.zendesk.com/hc/en-us/articles/115001427843-Dashboard-Permissions) podem enviar Eventos de Teste.

Olo requer uma resposta bem-sucedida do webhook de Evento de Teste antes que você possa concluir o processo de configuração do webhook do Olo.

### Etapa 3: Escreva o código de transformação para aceitar seus eventos Olo escolhidos

Nesta etapa, você transformará a carga útil do webhook que será enviada da plataforma de origem para um valor de retorno do objeto JavaScript.

1. Envie uma solicitação para o seu URL de Transformação de Dados com uma carga útil de evento de amostra de um evento Olo que você pretende suportar. Consulte o [formato do corpo da solicitação](#request-body-format) para obter ajuda na formatação de sua solicitação.
2. Atualize sua Transformação de Dados e certifique-se de que você pode ver a carga útil do evento de amostra nos **Detalhes do Webhook**.
3. Atualize seu código de Transformação de Dados para suportar os eventos Olo escolhidos.
4. Clique em **Validar** para retornar uma prévia da saída do seu código e verificar se é uma solicitação `/users/track` aceitável.
5. Salve e ative sua Transformação de Dados.

#### Formato do corpo da solicitação

Este valor de retorno deve aderir ao formato do corpo da solicitação da Braze `/users/track`:

- O código de transformação é aceito na linguagem de programação JavaScript. Todo fluxo de controle JavaScript padrão, como a lógica if/else, é suportado.
- O código de transformação acessa o corpo da solicitação do webhook através da variável carga útil. Esta variável é um objeto populado pela análise do corpo da solicitação JSON.
- Qualquer recurso aceito em nosso `/users/track` endpoint é aceito, incluindo:
    - Objetos de atributos de usuário, objetos de eventos e objetos de compra
    - Atributos aninhados e propriedades de evento personalizado aninhadas
    - Atualizações do grupo de inscrições
    - Endereço de e-mail como um identificador

## Exemplos de Transformações de Dados para webhooks do Olo

Esta seção contém modelos de exemplo que podem ser usados como ponto de partida. Sinta-se à vontade para começar do zero ou excluir componentes específicos conforme achar necessário.

Em cada modelo, o código define uma variável, `brazecall` para construir uma solicitação de `/users/track`.

Depois que a solicitação `/users/track ` for atribuída a `brazecall`, você retornará explicitamente `brazecall` para criar uma saída.

### Transformação de evento único

Se você quiser suportar apenas um único evento da Olo, não precisará usar o cabeçalho `X-Olo-Event-Type` para criar condicionalmente a carga útil da solicitação `/users/track`. Por exemplo, registrar um evento de compra ou um evento personalizado no perfil do usuário quando um webhook de Pedido Realizado do Olo é enviado para a Braze.

### Registrando cada produto como uma compra

```javascript
// iterate through the items included within the order

const purchases = payload.items.map((item) => {
 return {
   external_id: payload.customer.customerId.toString(),
   product_id: item.productId.toString(),
   currency: 'USD',
   price: item.sellingPrice,
   time: new Date().toISOString(),
   quantity: item.quantity,
   properties: {
     customValues: item.customValues
   }
 };
});

// log a purchase per item in the order

let brazecall = {
 "purchases": purchases
};

return brazecall;
```

### Registrando um evento personalizado

```javascript
// log an event “Order Placed” to the profile that includes all items in the order as event properties.

let brazecall = { 
"events": [
   {
     "external_id": payload.customer.customerId.toString(),
     "_update_existing_only": false,
     "name": "Order Placed",
     "time": new Date().toISOString(),
     "properties": {
       "Delivery Method": payload.deliveryMethod,
       "Items": payload.items,
       "Total": payload.totals.total,
       "Location": payload.location.name
     }
   }
 ]
};

return brazecall;
```

## Transformação multi-evento

A Olo envia o tipo de evento no cabeçalho `X-Olo-Event-Type` de cada webhook. Para suportar vários eventos de webhook Olo dentro de uma única transformação, use lógica condicional para transformar a carga útil do webhook com base no valor deste tipo de cabeçalho.  

No exemplo de transformação abaixo, nosso JavaScript cria uma carga útil específica para os eventos de `UserSignedUp` e `OrderPlaced`. Além disso, uma condição `else` lida com uma carga útil para quaisquer eventos da Olo enviados para a Braze sem o cabeçalho X-Olo-Event-Type de `UserSignedUp` e `OrderPlaced`.

```javascript
// captures the value within the X-Olo-Event-Type header for use in the conditional logic

let event_type = headers["X-Olo-Event-Type"];

// defines a variable 'brazecall' that will hold the request payload for the /users/track request

let brazecall;

// if the X-Olo-Event-Type header is 'UserSignedUp', define a variable for the different subscription statuses that could be included within the Olo event payload

if (event_type == "UserSignedUp") {
	let emailSubscribe;
	let emailSubscriptionGroup;
	let smsSubscriptionGroup;


// determine if the user has opted into marketing emails


	if (payload.allowEmail) {
		emailSubscribe = "opted_in";
		emailSubscriptionGroup = "subscribed";
	} else {
		emailSubscribe = "unsubscribed";
		emailSubscriptionGroup = "unsubscribed";
	}


	// determine if the user has opted into SMS


	if (payload.allowMarketingSms) {
		smsSubscriptionGroup = "subscribed";
	} else {
		smsSubscriptionGroup = "unsubscribed";
	}

	// build the /users/track request and pass in the appropriate subscription statuses


	brazecall = {
		"attributes": [{
			"external_id": payload.id.toString(),
			"_update_existing_only": false,
			"email": payload.emailAddress,
			"first_name": payload.firstName,
			"last_name": payload.lastName,
			"email_subscribe": emailSubscribe,
			"phone": payload.contactNumber,
			"subscription_groups": [{
					"subscription_group_id": "57e5307f-9084-490d-9d6d-8244dc919a48",
					"subscription_state": emailSubscriptionGroup
				},
				{
					"subscription_group_id": "6440ba26-86ea-47db-a935-6647941dc78b",
					"subscription_state": smsSubscriptionGroup
				}
			]
		}]
	}; // if the X-Olo-Event-Type header is 'OrderPlaced', build the /users/track request to log an event to the user profile
} else if (event_type == "OrderPlaced") {
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": false,
			"name": "Order Placed",
			"time": new Date().toISOString(),
			"properties": {
				"Delivery Method": payload.deliveryMethod,
				"Items": payload.items,
				"Total": payload.totals.total,
				"Location": payload.location.name
			}
		}]
	};
} else { // if the X-Olo-Event-Type header is anything else, build the /users/track request to log an event to the user profile
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": true,
			"name": "Another Event",
			"time": new Date().toISOString()
		}]

	};
}

// return `brazecall` to create an output.

return brazecall;
```

### Etapa 4: Publique seu webhook Olo

Depois de ativar sua Transformação de Dados no Braze, use a [ferramenta de webhooks de autoatendimento](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) no dashboard do Olo para publicar seu webhook. Quando o webhook for publicado, a transformação de dados começará a receber mensagens de eventos do webhook da Olo.

## Coisas para saber

### Tentativas

Olo tentará novamente as chamadas de webhook que resultarem em um código de status de resposta HTTP de `429 - Too Many Requests` ou na faixa de `5xx` (por exemplo, devido a um tempo limite do gateway ou erro do servidor), até 50 vezes em um período de 24 horas antes de descartar a solicitação.

### Pelo menos uma entrega

Se uma chamada de webhook resultar em um código de status de resposta HTTP de `429 - Too Many Requests` ou na faixa de `5xx` (por exemplo, devido a tempo esgotado do gateway ou erro do servidor), a Olo tentará reenviar a mensagem até 50 vezes em um período de 24 horas antes de desistir.

Webhooks podem, portanto, ser recebidos várias vezes por um assinante. Cabe ao inscrito ignorar duplicatas verificando o cabeçalho `X-Olo-Message-Id`.


