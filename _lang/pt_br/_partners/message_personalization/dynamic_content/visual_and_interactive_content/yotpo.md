---
nav_title: Yotpo
article_title: Yotpo
alias: /partners/yotpo/
description: "Este artigo de referência descreve a parceria entre Braze e Yotpo, uma plataforma de marketing eCommerce líder que ajuda milhares de marcas inovadoras a acelerar o crescimento direto ao consumidor."
page_type: partner
search_tag: Partner
---

# Yotpo

> [Yotpo](https://www.yotpo.com/), a principal plataforma de marketing eCommerce, ajuda milhares de marcas inovadoras a acelerar o crescimento direto ao consumidor. A abordagem de plataforma única do Yotpo integra soluções baseadas em dados para avaliações, fidelidade, marketing por SMS e muito mais, capacitando as marcas a criar experiências mais inteligentes e de maior conversão para os clientes.

_Esta integração é mantida pela Yotpo._

## Sobre a integração

Com a integração do Braze e do Yotpo, é possível extrair e exibir dinamicamente classificações com estrelas, principais avaliações e conteúdo visual gerado pelo usuário (UGC) sobre produtos em e-mails e outros canais de comunicação no Braze. Também é possível incluir dados de fidelidade no nível do cliente em e-mails e outros métodos de comunicação para criar uma interação mais personalizada, aumentando as vendas e a fidelidade.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Yotpo | É necessário ter uma conta no Yotpo para aproveitar essa parceria. |
| Chave de API de avaliações do Yotpo | Esta API será implementada no snippet de código do conteúdo conectado.<br><br>Para saber mais, consulte como [encontrar sua chave do app Yotpo e a chave secreta](https://support.yotpo.com/en/article/finding-your-yotpo-app-key-and-secret-key). |
| Chave de API de fidelidade do Yotpo | Esta chave de API e o GUID serão implementados no snippet de código do conteúdo conectado.<br><br>Para saber mais, consulte como [encontrar sua chave de API e GUID de fidelidade e indicação](https://support.yotpo.com/en/article/finding-your-loyalty-referrals-api-key-and-guid)|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Antes de continuar, confirme se o ID do produto Yotpo é igual ao `product_id` que será extraído dinamicamente da Braze. Isso é obrigatório para que a integração funcione. 

Para encontrar seu ID de produto Yotpo, execute as etapas a seguir:

1. Acesse o site de sua loja.
2. Abra a página do produto.
3. Clique com o botão direito do mouse e selecione **Inspect (Inspecionar**).
4. Pressione <kbd>Control</kbd> + <kbd>F</kbd> e procure por `yotpo-main` no código. A variável `data-product ID` e seu valor aparecem na div da Yotpo.

![Inspecione e procure por yotpo-main para encontrar a variável data-product ID]({% image_buster /assets/img/yotpo/image1.png %})

## Integração

Para integrar a Yotpo e a Braze, execute as etapas a seguir:

1. Acesse seu dashboard do Braze.
2. Na página **Campanhas**, clique em **Criar campanha** e selecione **E-mail**.
3. Selecione seu modelo preferido.
4. Clique em **Editar corpo do e-mail** e adicione o respectivo snippet do [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) para seu caso de uso:
    - [Exibir a classificação por estrelas e o número de avaliações de um produto](#star-review-count)
    - [Exibir uma avaliação recente de um produto com 5 estrelas](#five-star-review)
    - [Exibir conteúdo visual gerado por usuários por produto](#visual-ugc)
    - [Exibir o saldo de fidelidade de um cliente em um e-mail](#loyalty-balance)

### Exibir a classificação por estrelas e o número de avaliações de um produto {#star-review-count}

Use esse snippet para fornecer a pontuação média pública e o número total de avaliações de um produto incluído no e-mail:

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/products/<YOTPO-API-KEY>/{{event_properties.${product_id}}}/bottomline :save result %}      

{% if {{result.response.bottomline.average_score}} != 0 %}

The average rating for this product is:

{{result.response.bottomline.average_score}}/5, based on {{result.response.bottomline.total_reviews}} reviews.

{% else %}                    
{% endif %}
```
{% endraw %}

Substitua `<YOTPO-API-KEY>` por sua chave de API de avaliações do Yotpo. `product_id` será extraído dinamicamente da Braze. Para que a integração funcione, o `product_id` no Braze deve corresponder ao ID do produto no Yotpo (normalmente o ID do produto pai do eCommerce).

![Substitua YOTPO-API-KEY pela sua chave de API do Yotpo Reviews]({% image_buster /assets/img/yotpo/image2.png %})

### Exibir uma avaliação recente de um produto com 5 estrelas {#five-star-review}

Use esse snippet para fornecer uma das principais avaliações (publicadas) de um produto específico que está incluído no e-mail:

{% raw %}
```liquid
{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/products/{{event_properties.${product_id}}}/reviews.json?per_page=50&star=5&sort=votes_up :save result %}

{% if {{result.response.reviews[0].score}} == 5 %}

Recent 5 Star Review for this product:

{{result.response.reviews[0].content}}

{% else %}              
{% endif %}
```
{% endraw %}

Substitua `<YOTPO-API-KEY>` por sua chave de API de avaliações do Yotpo. `product_id` será extraído dinamicamente da Braze. Para que a integração funcione, o `product_id` no Braze deve corresponder ao ID do produto no Yotpo (normalmente o ID do produto pai do eCommerce).

Veja a seguir a aparência do snippet em seu editor de e-mail:

![Exemplo de editor de e-mail mostrando um trecho para as últimas avaliações de 5 estrelas]({% image_buster /assets/img/yotpo/image3.png %})

### Exibir conteúdo visual gerado por usuários por produto {#visual-ugc}

Use esse snippet para recuperar imagens do Yotpo marcadas e publicadas e adicioná-las a seus e-mails em vez da imagem de estoque ou como uma galeria adicional:

{% raw %}
```liquid

{% connected_content https://api.yotpo.com/v1/widget/<YOTPO-API-KEY>/albums/product/{{event_properties.${product_id}}}?per_page=1 :save result %}

{% if {{result.response.images[0].tagged_products[0].image_url}} != null %}

The Visual content of the product: 

<img src="{{result.response.images[0].tagged_products[0].image_url}}" border="0" width="200" height="200" alt="" />

{% else %}

Image return NULL

{% endif %}
```
{% endraw %}

Substitua `<YOTPO-API-KEY>` por sua chave de API de avaliações do Yotpo. `product_id` será extraído dinamicamente da Braze. Para que a integração funcione, o `product_id` no Braze deve corresponder ao ID do produto no Yotpo (normalmente o ID do produto pai do eCommerce).

O snippet ficará assim:

![Exemplo de editor de e-mail mostrando um trecho de imagens publicadas no Yotpo]({% image_buster /assets/img/yotpo/image4.png %})

### Exibir o saldo de fidelidade de um cliente em um e-mail {#loyalty-balance}

Use esse snippet para recuperar o saldo de pontos de fidelidade de um cliente e usá-lo em seu envio de mensagens por e-mail:

{% raw %}
```liquid
{% connected_content 

https://loyalty.yotpo.com/api/v2/customers?customer_email=**{{${email_address}}}**
:method get
:headers {
    "x-guid": "<YOTPO-LOYALTY-GUID>",
    "x-api-key": "<YOTPO-LOYALTY-API-KEY>"
        }
:content_type application/json
:save publication
%}

You have {{publication.points_balance}} points

Only {{publication.vip_tier_upgrade_requirements.points_needed}} more points to become part of our VIP Tier!
```
{% endraw %}

Substitua `<YOTPO-LOYALTY-GUID>` e `<YOTPO-LOYALTY-API-KEY>` por suas credenciais de fidelidade do Yotpo. `email_address` é extraído dinamicamente da Braze. Para que a integração funcione, o e-mail deve ser o endereço de e-mail do cliente que está recebendo o e-mail.

O snippet ficará assim:

![Exemplo de editor de e-mail mostrando um trecho do saldo de fidelidade do cliente]({% image_buster /assets/img/yotpo/image5.png %})

## Perguntas frequentes {#faq}

#### E se eu não tiver uma avaliação 5 estrelas?

Se você não tiver nenhuma avaliação 5 estrelas (por exemplo, se a resposta do endpoint retornar NULL para a avaliação 5 estrelas), nenhum conteúdo será exibido.

#### E se eu não tiver uma imagem publicada para um produto?

Se você não tiver nenhuma imagem para um produto (por exemplo, se a resposta do ponto de extremidade retornar NULL para a imagem do produto), nenhum conteúdo será exibido.

#### Posso personalizar a aparência ou extrair outros campos de dados do Yotpo?

Sim! Para descobrir outros pontos de dados e opções de personalização disponíveis, consulte [Fazer uma chamada de API]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/). Talvez você precise da ajuda de um desenvolvedor de front-end para fazer isso.

{% alert note %}
O Yotpo não oferece suporte a requisitos personalizados além do que está descrito neste guia.
{% endalert %}


