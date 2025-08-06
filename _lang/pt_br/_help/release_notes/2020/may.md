---
nav_title: Maio
page_order: 8
noindex: true
page_type: update
description: "Este artigo contém notas de versão de maio de 2020."
---
# Maio de 2020

## Google Tag Manager

Foram adicionados documentação e exemplos de como implantar e gerenciar o SDK do Braze para Android usando o [Google Tag Manager]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android).

## Novo ponto de extremidade da API de envio de e-mail de lista de proibições

Agora você pode colocar endereços de e-mail [em uma lista de proibições]({{site.baseurl}}/api/endpoints/email/post_blacklist/) por meio da API do Braze. A inclusão de um endereço de e-mail na lista de proibições cancelará a inscrição do usuário no e-mail e o marcará como hard bounce.

## Alteração da chave de API para endpoints da API da Braze

A partir de maio de 2020, a Braze mudou a forma como lemos as chaves de API para torná-las mais seguras. Agora, as chaves de API devem ser passadas como um cabeçalho de solicitação. Os exemplos podem ser encontrados nas páginas de endpoints individuais em **Solicitação de exemplo**, bem como na **Explicação da chave de API**.

A Braze continuará a oferecer suporte ao `api_key` que está sendo transmitido por meio do corpo da solicitação e dos parâmetros de URL, mas acabará sendo descontinuado (TBD). **Atualize suas chamadas de API adequadamente.** Essas alterações foram atualizadas no [Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro).
{% details Explicação da chave de API %}
{% tabs %}
{% tab Solicitação GET %}
Este exemplo usa o ponto de extremidade `/email/hard_bounces`.

**Antes: Chave de API no corpo da solicitação**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?api_key={YOUR_REST_API_KEY}&start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
```
**Agora: Chave de API no cabeçalho**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endtab %}
{% tab Solicitação POST %}
Este exemplo usa o ponto de extremidade `/user/track`.

**Antes: Chave de API no corpo da solicitação**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--data-raw '{
	"api_key": YOUR-API-KEY-HERE ,
	"attributes": [ 
 	{
 	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
**Agora: Chave de API no cabeçalho**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
	"attributes": [ 
 	{
	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
{% endtab %}
{% endtabs %}
{% enddetails %}


