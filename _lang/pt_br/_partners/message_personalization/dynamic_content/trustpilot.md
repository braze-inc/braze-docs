---
nav_title: Trustpilot
article_title: Trustpilot
description: "Esta página aborda como integrar a Trustpilot ao Braze, enviar convites para avaliações e personalizar mensagens com insights sobre avaliações de produtos."
alias: /partners/trustpilot/
page_type: partner
search_tag: Partner
---

# Trustpilot

> [A Trustpilot](https://www.trustpilot.com/) é uma plataforma de avaliação on-line que ativa o compartilhamento de feedback dos clientes e permite que você gerencie e responda às avaliações.

Esta página fornece um guia passo a passo para:

* Criação de convites para avaliações usando a API de criação de convites da Trustpilot  
* Envio de mensagens personalizadas com análises de produtos por meio da API de análises de produtos da Trustpilot

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Pré-requisito | Descrição |
| --- | --- |
| Uma conta na Trustpilot | Você precisa de uma conta da Trustpilot com acesso à API da Trustpilot. |
| Uma chave de autenticação da Trustpilot | Você precisará configurar uma chave de API e solicitar um token de acesso. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Integração

### Etapa 1: Obtenha suas credenciais da API da Trustpilot

1. [Faça o registro na Trustpilot](https://app.contentful.com/login) com suas credenciais.  
2. Crie ou recupere a chave e o segredo da API no dashboard da Trustpilot acessando **Integrações** > **Desenvolvedores** > **APIs**. Se você ainda não tiver uma chave de API, crie uma nova:  
   1. Acesse **Nome do aplicativo** > **Criar aplicativo**  
   2. Copie sua chave e segredo de API, que serão usados para autenticar suas solicitações de Connected Content.

## Envio de convites para avaliações da Trustpilot

### Etapa 1: Configurar uma campanha de webhook do Braze 

Configure uma campanha de webhook do Braze baseada em ação para disparar as APIs da Trustpilot para enviar convites de avaliação por e-mail aos usuários. Por exemplo, você pode enviar um convite para avaliação depois que um usuário fizer um pedido com os seguintes detalhes do webhook:
   * [URL do webhook](https://developers.trustpilot.com/invitation-api?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..#create-invitation(s)): `https://invitations-api.trustpilot.com/v1/private/business-units/{businessUnitId}/email-invitations`  
   * Método: POST  
   * Adicione as informações relevantes do cliente como pares de valores-chave

### Etapa 2: Recuperar o token de acesso

1. Use [o Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) para fazer uma solicitação ao [ponto de extremidade de autenticação da Trustpilot](https://documentation-apidocumentation.trustpilot.com/authentication?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..) para recuperar o token de acesso.
2. Use o tipo de concessão **client_credentials** e insira sua chave de API e segredo em uma tag Connected Content para recuperar um token. A solicitação de Connected Content pode ser inserida no cabeçalho da solicitação. O Connected Content pode ter a seguinte aparência:
  
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
3\. Adicione o token de acesso ao cabeçalho da solicitação de sua campanha de webhook.

{% alert tip %}
Consulte a [documentação da Trustpilot](https://support.trustpilot.com/hc/en-us/community/posts/11947443933074-Braze-Trustpilot-Setup-Instructions-for-triggering-API-invites) para obter instruções mais detalhadas.
{% endalert %}

## Personalização de mensagens com insights sobre avaliações de produtos

Em sua campanha no Braze, faça uma chamada de Connected Content para solicitar dados do [endpoint Get product reviews summary](https://developers.trustpilot.com/product-reviews-api#get-product-reviews-summary) da Trustpilot ({% raw %}`https://api.trustpilot.com/v1/product-reviews/business-units/{businessUnitId}`{% endraw %}). Esse método recupera revisões de produtos para SKUs específicos da unidade de negócios. O exemplo a seguir especifica a SKU específica do produto e filtra as avaliações de cinco estrelas.

{% raw %}
```liquid
{% connected_content https://api.trustpilot.com/v1/product-reviews/business-units/66ea0530xxxxxx/reviews?sku={{event_properties.${item_sku}}}&stars=5
   :method get
   :headers {"apikey": "xxxxx"}
   :content_type application/json :save result %}
```
{% endraw %}

![Conteúdo conectado no e-mail usando o Liquid para extrair informações.]({% image_buster /assets/img/trustpilot_connected_content_example.png %}){:style="max-width:38%;"}

A solicitação do Connected Content retornará as avaliações do produto.

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
2\. Use a sintaxe Liquid para inserir o conteúdo relevante em sua mensagem. Por exemplo, para extrair o conteúdo da análise do produto, use a Liquid tag {% raw %}`{{result.productReviews[0].content}}`{% endraw %}.

![Envio de e-mail personalizado com uma avaliação de um caminhão de brinquedo que o usuário deixou em seu carrinho.]({% image_buster /assets/img/trustpilot_personalized_email.png %}){:style="max-width:38%;"}