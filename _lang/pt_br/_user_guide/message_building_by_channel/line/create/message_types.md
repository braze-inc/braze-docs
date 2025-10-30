---
nav_title: Tipos de mensagem
article_title: Tipos de mensagens LINE
page_order: 0
description: "Este artigo aborda os diferentes tipos de mensagens LINE."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/message_types/
---

# Tipos de mensagens LINE

> Este artigo aborda os tipos de mensagem do LINE que você pode compor, incluindo aspectos e limitações.

Ao compor uma mensagem do LINE, você pode arrastar e soltar tipos de mensagens no compositor e personalizá-las.

Painel de tipos de mensagem com tipos de mensagem para arrastar para o editor de composição, incluindo texto, imagem, mensagem avançada e mensagem baseada em cartão.]({% image_buster /assets/img/line/line_message_types.png %}){: style="max-width:40%;"}

## Texto

Uma mensagem de texto do LINE pode conter até 5.000 caracteres e incluir emojis e personalização do Liquid.

Os casos de uso incluem:
- Anuncie uma promoção por tempo limitado para estoque de liquidação
- Envie felicitações de aniversário personalizadas com cartões promocionais exclusivos
- Compartilhe atualizações rápidas sobre os próximos eventos

\![Uma mensagem de texto lembrando o usuário de não se esquecer da festa da Black Friday e do potencial de economizar até 80% antes da meia-noite.]({% image_buster /assets/img/line/line_text_message.png %}){: style="max-width:40%;"}

## Imagem

Uma mensagem de imagem LINE pode ser adicionada por meio da [biblioteca de mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/), de um URL ou do Liquid. Essas imagens são autônomas e não contêm links clicáveis.

Os casos de uso incluem:
- Mostre um destino de férias para inspirar os usuários a procurar comprar passagens aéreas
- Destaque as promoções de fim de estação para incentivar os usuários a estocar as roupas de inverno do próximo ano com ótimas ofertas
- Inicie uma contagem regressiva visual para uma venda anual em toda a loja

\![Uma mensagem de imagem promovendo a venda de uma torradeira.]({% image_buster /assets/img/line/line_image_message.png %}){: style="max-width:40%;"}

### Imagem do URL

Use imagens de URL para casos de uso que incorporem:
- Imagens dinâmicas Liquid, incluindo o Liquid no atributo de origem da imagem. Por exemplo, você pode inserir {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} como o URL da imagem para incluir o primeiro nome de um usuário na imagem
- [Conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), extraindo imagens diretamente de seu servidor da Web ou de APIs acessíveis ao público
- [Crie catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/) acessando imagens de arquivos CSV importados e pontos de extremidade de API

| **Especificações** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| Comprimento do URL do arquivo de imagem | Máximo de 2.000 caracteres  |
| Formato da imagem          | PNG, JPEG             |
| Tamanho do arquivo     |  Máximo de 10 MB |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Mensagens ricas (mapa de imagens)

Uma mensagem LINE rich é uma imagem que contém um ou mais links que são abertos ao selecionar áreas específicas na imagem. Selecione um modelo de mensagem avançada para escolher como os links serão mapeados na imagem.

Os casos de uso incluem:
- Exibir uma grade de bolsas recém-chegadas com links para a respectiva página de produto de cada bolsa
- Apresentar um menu interativo que inicia um pedido combinado ao selecionar um item
- Disponha várias promoções para os usuários escolherem selecionando um quadrado da grade

Uma mensagem rica em seis quadrados com a foto de uma grade em preto e branco na qual os usuários podem tocar para receber uma oferta aleatória.]({% image_buster /assets/img/line/line_rich_message.png %})

### Mapa de imagens 

| **Especificações** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| Comprimento do URL do arquivo de imagem | Máximo de 2.000 caracteres  |
| Formato da imagem          | PNG (pode ser transparente), JPEG             |
| Relação de aspecto          | 1:1 (largura:altura)
| Tamanho do arquivo     |  Máximo de 10 MB |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link URI 

| **Especificações** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| Contagem de caracteres      | 1.000 no máximo |
| Esquemas              | HTTP, HTTPS, LINE, tel |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Texto 

Uma mensagem com rich text pode conter até 400 caracteres.

## Baseado em cartão (carrossel)

Uma mensagem baseada em cartão do LINE permite que os usuários percorram várias mensagens, como um carrossel, e tomem medidas em relação às mensagens mais relevantes para eles, selecionando um cartão ou os botões de um cartão.

Os casos de uso incluem:
- Exibir promoções para itens específicos do menu
- Destaque para as jaquetas mais vendidas desta temporada
- Apresentar uma amostra de ferramentas e utensílios de cozinha que estão incluídos em um kit

Uma mensagem baseada em cartões com pelo menos dois cartões que promovem sanduíches no editor de composição.]({% image_buster /assets/img/line/line_card_message.png %})

### Mensagem

| **Especificações** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| Colunas                  | 10 máximo |
| Relação de aspecto             | Retângulo: 1.51:1 <br> Quadrado: 1:1  |
| Título                    | Máximo de 40 caracteres
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


### Imagem

| **Especificações** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| URL da imagem                 | Máximo de 2.000 caracteres |
| Formato da imagem              | JPEG ou PNG |
| Largura                     | 1.024 pixels  |
| Tamanho do arquivo                 | 1 MB |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


### Texto

| **Especificações** | **Propriedades recomendadas** |
|-------------------------|----------------------------|
| Personagens              | 120 no máximo (sem imagem ou título) <br> 60 no máximo (mensagem com uma imagem ou título)  |
| Ações                 | 3 máximo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


