---
nav_title: Trustpilot
article_title: Trustpilot
description: "Esta página cobre como integrar o Trustpilot com o Braze, enviar convites para avaliações e personalizar mensagens com insights de avaliações de produtos."
alias: /partners/trustpilot/
page_type: partner
search_tag: Partner
---

# Trustpilot

> [Trustpilot](https://www.trustpilot.com/) é uma plataforma de avaliações online que permite que os clientes compartilhem feedback e permite que você gerencie e responda a avaliações.

Esta página fornece um guia passo a passo para:

* Criar convites para avaliações usando a API de Criação de Convite do Trustpilot  
* Personalizar mensagens com avaliações de produtos através da API de Avaliações de Produtos do Trustpilot

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Pré-requisito | Descrição |
| --- | --- |
| Uma conta do Trustpilot | Você precisa de uma conta do Trustpilot com acesso à API do Trustpilot. |
| Uma chave de autenticação do Trustpilot | Você precisará configurar uma chave de API e solicitar um token de acesso. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Integração

### Etapa 1: Obtenha suas credenciais da API do Trustpilot

1. [Faça login no Trustpilot](https://app.contentful.com/login) com suas credenciais.  
2. Crie ou recupere a chave e o segredo da API no painel do Trustpilot acessando **Integrações** > **Desenvolvedores** > **APIs**. Se você ainda não tiver uma chave de API, crie uma nova:  
   1. Acesse **Nome da Aplicação** > **Criar Aplicação**  
   2. Copie sua chave de API e segredo, que serão usados para autenticar suas solicitações de Conteúdo Conectado.

## Enviando convites para avaliações do Trustpilot

### Etapa 1: Configure uma campanha de webhook do Braze 

Configure uma campanha de webhook do Braze baseada em ações para acionar as APIs do Trustpilot para enviar convites de avaliação por e-mail aos usuários. Por exemplo, você pode enviar um convite para avaliação após um usuário fazer um pedido com os seguintes detalhes do webhook:
   * [URL do webhook](https://developers.trustpilot.com/invitation-api?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..#create-invitation(s)): `https://invitations-api.trustpilot.com/v1/private/business-units/{businessUnitId}/email-invitations`  
   * Método: POST  
   * Adicione as informações relevantes do cliente como pares chave-valor

### Etapa 2: Recuperar o token de acesso

1. Use [Conteúdo Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) para fazer uma solicitação ao [Ponto de Autenticação do Trustpilot](https://documentation-apidocumentation.trustpilot.com/authentication?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..) para recuperar o Token de Acesso.
2. Use o tipo de concessão **client_credentials** e insira sua chave de API e segredo em uma tag de Conteúdo Conectado para recuperar um token. A solicitação de Conteúdo Conectado pode ser inserida no cabeçalho da solicitação. O Conteúdo Conectado pode parecer assim:
  
{% raw %}

```liquid
{% connected_content 
https://api.trustpilot.com/v1/oauth/oauth-business-users-for-applications/accesstoken
:method post
:headers {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic {{'API_KEY:API_SECRET' | base64_encode}}" }
:body grant_type=client_credentials
:save token
:retry
:cache_max_age 3600 %}

{{token.access_token}}

```

{% endraw %}

{: start="3"}
3\. Adicione o token de acesso ao cabeçalho da solicitação da sua campanha de webhook.

{% alert tip %}
Consulte [a documentação do Trustpilot](https://support.trustpilot.com/hc/en-us/community/posts/11947443933074-Braze-Trustpilot-Setup-Instructions-for-triggering-API-invites) para obter instruções mais detalhadas.
{% endalert %}

## Personalizando mensagens com insights de avaliações de produtos

Na sua campanha Braze, faça uma chamada de Conteúdo Conectado para solicitar dados do [Ponto de resumo de avaliações de produtos do Trustpilot](https://developers.trustpilot.com/product-reviews-api#get-product-reviews-summary) ({% raw %}`https://api.trustpilot.com/v1/product-reviews/business-units/{businessUnitId}`{% endraw %}). Este método recupera avaliações de produtos para SKUs específicos da unidade de negócios. O seguinte exemplo especifica o SKU do produto específico e filtra por avaliações de cinco estrelas.

{% raw %}
```liquid
{% connected_content https://api.trustpilot.com/v1/product-reviews/business-units/66ea0530xxxxxx/reviews?sku={{event_properties.${item_sku}}}&stars=5
   :method get
   :headers {"apikey": "xxxxx"}
   :content_type application/json :save result %}
```
{% endraw %}

![Conteúdo Conectado em e-mail usando Liquid para puxar informações.]({% image_buster /assets/img/trustpilot_connected_content_example.png %}){:style="max-width:38%;"}

A solicitação de Conteúdo Conectado retornará as avaliações de produtos.

{% raw %}
```liquid
  {
   "productReviews": [
       {
           "id": "670d5810ba62e6b31de97de9",
           "createdAt": "2024-10-14T17:42:40.286Z",
           "stars": 5,
           "content": "Such a great toy truck, my kids really enjoy it! ",
           "consumer": {
               "id": "6176xxxx",
               "displayName": "Kevin Bob"
           },
           "language": "en",
           "attributeRatings": [],
           "attachments": [],
           "firstCompanyComment": null
       }
   ],
   "links": []
 ```
{% endraw %}

{: start="2"}
2\. Use a sintaxe Liquid para puxar o conteúdo relevante para sua mensagem. Por exemplo, para puxar o conteúdo da avaliação do produto, use a tag Liquid {% raw %}`{{result.productReviews[0].content}}`{% endraw %}.

![E-mail personalizado com uma avaliação de um caminhão de brinquedo que o usuário deixou no carrinho.]({% image_buster /assets/img/trustpilot_personalized_email.png %}){:style="max-width:38%;"}