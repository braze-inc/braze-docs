---
nav_title: "DELETE: Excluir o estado da inscrição por endereço de e-mail ou número de telefone"
article_title: "DELETE: Excluir estado da inscrição por endereço de e-mail ou número de telefone"
search_tag: Endpoint
page_order: 0
hidden: true
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes sobre o endpoint da Braze \"Excluir estado da inscrição por endereço de e-mail ou número de telefone\"."

---

{% api %}
# Excluir o estado da inscrição por endereço de e-mail ou número de telefone
{% apimethod delete %}
/users/subscription
{% endapimethod %}

> Use esse ponto de extremidade para excluir o valor do estado da inscrição com base em um endereço de e-mail ou número de telefone.

## Parâmetros de solicitação

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `email` | Sim | String | O endereço de e-mail do usuário (deve incluir pelo menos um endereço e no máximo 50 endereços). |
| `phone` | Sim | String | O número de telefone do usuário (deve incluir pelo menos um número de telefone e no máximo 50 números de telefone). Recomendamos fornecer isso no formato E.164. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  {phone: "+12125551212"},
  {email: "dont.spam@me.com"},
  {phone: "+17185551212"}
}
```

## Resposta

```json
{
  "status": "The emails and/or phone numbers have been queued for deletion",
  "message": "success"
}
```

{% endapi %}
