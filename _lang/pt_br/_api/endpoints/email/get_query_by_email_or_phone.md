---
nav_title: "OBTER: Estado da inscrição na lista com endereço de e-mail ou número de telefone"
article_title: "OBTER: Estado da inscrição na lista com endereço de e-mail ou número de telefone"
search_tag: Endpoint
page_order: 2
hidden: true
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes sobre o estado da inscrição na lista com um endereço de e-mail ou número de telefone no endpoint do Braze."

---
{% api %}
# Estado da inscrição na lista com um endereço de e-mail ou número de telefone
{% apimethod get %}
/users/subscription
{% endapimethod %}

> Use esse ponto de extremidade para retornar o valor do estado da inscrição com base em um endereço de e-mail ou número de telefone.

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `email` | Sim | String | O endereço de e-mail do usuário (deve incluir pelo menos um endereço e no máximo 50 endereços). |
| `phone` | Sim | String | O número de telefone do usuário (deve incluir pelo menos um número de telefone e no máximo 50 números de telefone). Recomendamos fornecer isso no formato E.164. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação
```
curl --location --request GET 'https://rest.iad-01.braze.com/users/subscriptions?phone=+12123355555&email=example%40braze.com' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Resposta

As entradas são listadas em ordem decrescente.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "emails": [
    {
      "email": "example@braze.com",
      "email_subscribe": {
        "email_subscription_event_date": "2019-11-20T19:58:04.825Z",
        "email_subscription_state": "Subscribed"
      },
      "subscription_group": [
        {
          "subscription_group_id": "5f5536d2a76e0f4e323a1234",
          "subscription_group_event_date": "2021-03-11T21:29:22.347Z",
          "subscription_group_state": "Unsubscribed"
        }
      ],
      "hard_bounced_at": null,
      "spam_at": null
    }
  ],
	"phone": [{
		"phone": "+12123355555",
		"subscription_group": [{
			"subscription_group_id": "3f5536d2a76e0f4e323a5555",
			"subscription_group_state": "Subsscribed",
			"subscription_group_event_date": "2021-03-11T21:29:22.347Z"
		}]
	}],
	"message": "success"
}
```

{% endapi %}
