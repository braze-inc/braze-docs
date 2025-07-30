---
nav_title: Tipos de mensagens
article_title: Tipos de Mensagem LINE
page_order: 0
description: "Este artigo cobre os diferentes tipos de mensagens LINE."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/message_types/
---

# Tipos de mensagem LINE

> Este artigo cobre os tipos de mensagem LINE que você pode compor, incluindo aspectos e limitações.

Quando você compõe uma mensagem LINE, pode arrastar e soltar tipos de mensagem no criador e, em seguida, personalizá-los.

![Painel de tipos de mensagem com tipos de mensagem para arrastar para o editor de criador, incluindo texto, imagem, mensagem rica e mensagem baseada em cartão.]({% image_buster /assets/img/line/line_message_types.png %}){: style="max-width:40%;"}

## Texto

Uma mensagem de texto LINE pode conter até 5.000 caracteres e incluir emojis e personalização Liquid.

Os casos de uso incluem:
- Anuncie uma promoção por tempo limitado para estoque de liquidação
- Envie cumprimentos de aniversário personalizados com cartões de promoção exclusivos
- Compartilhe atualizações rápidas sobre eventos futuros

![Uma mensagem de texto lembrando o usuário de não esquecer de uma festa de Black Friday e a possibilidade de economizar até 80% antes da meia-noite.]({% image_buster /assets/img/line/line_text_message.png %}){: style="max-width:40%;"}

## Imagem

Uma mensagem de imagem LINE pode ser adicionada através da [biblioteca de mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/), uma URL ou Liquid. Estas imagens são independentes e não contêm links clicáveis.

Os casos de uso incluem:
- Apresente um destino de férias para inspirar os usuários a considerarem a compra de passagens aéreas.
- Destaque as promoções de fim de temporada para incentivar os usuários a estocar roupas de inverno do próximo ano com ótimas ofertas.
- Inicie uma contagem regressiva visual para uma venda anual em toda a loja

![Uma mensagem de imagem promovendo uma venda de torradeiras.]({% image_buster /assets/img/line/line_image_message.png %}){: style="max-width:40%;"}

### URL da imagem

Use imagens de URL para casos de uso que incorporam:
- Imagens dinâmicas Liquid, incluindo o Liquid no seu atributo de fonte de imagem. Por exemplo, você pode inserir {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} como a URL da imagem para incluir o primeiro nome de um usuário na imagem
- [Conteúdo Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) puxando imagens diretamente do seu servidor web ou APIs acessíveis publicamente
- [Braze catalogs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) acessando imagens de arquivos CSV importados e pontos de extremidade da API

| **Especificações** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| Comprimento da URL do arquivo de imagem | 2.000 caracteres no máximo  |
| Formato de imagem          | PNG, JPEG             |
| Tamanho do arquivo     |  10 MB máximo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Mensagens ricas (mapa de imagem)

Uma mensagem rica de LINE é uma imagem que contém um ou mais links que são abertos ao selecionar áreas específicas na imagem. Selecione um modelo de mensagem rico para escolher como os links são mapeados na imagem.

Os casos de uso incluem:
- Exibir uma grade de bolsas recém-chegadas com links para a página de produto de cada bolsa
- Apresente um menu interativo que inicia um pedido em combo ao selecionar um item
- Apresente várias promoções para os usuários escolherem selecionando um quadrado da grade

![Uma mensagem rica de seis quadrados com uma foto de uma grade em preto e branco que os usuários podem tocar para receber uma oferta aleatória.]({% image_buster /assets/img/line/line_rich_message.png %})

### Mapa da imagem 

| **Especificações** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| Comprimento da URL do arquivo de imagem | 2.000 caracteres no máximo  |
| Formato de imagem          | PNG (pode ser transparente), JPEG             |
| Proporção          | 1:1 (largura:altura)
| Tamanho do arquivo     |  10 MB máximo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### link URI 

| **Especificações** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| Contagem de caracteres      | 1.000 máximo |
| Esquemas              | HTTP, HTTPS, LINE, tel |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Texto 

Uma mensagem rica em texto pode conter até 400 caracteres.

## Cartão-baseado (carrossel)

Uma mensagem baseada em cartão do LINE permite que os usuários rolem por várias mensagens, como um carrossel, e tomem ações nas mensagens mais relevantes para eles selecionando um cartão ou os botões de um cartão.

Os casos de uso incluem:
- Exibir promoções para itens de menu específicos
- Destaque os casacos mais vendidos desta temporada
- Apresentar uma amostra de ferramentas e gadgets de cozinha que estão incluídos em um kit

![Uma mensagem baseada em cartão com pelo menos dois cartões que promovem sanduíches no editor de criador.]({% image_buster /assets/img/line/line_card_message.png %})

### Mensagem

| **Especificações** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| Colunas                  | 10 máximo |
| Proporção             | Retângulo: 1,51:1 <br> Quadrado 1:1  |
| Título                    | 40 caracteres no máximo
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


### Imagem

| **Especificações** | **Propriedades recomendadas** |
|--------------------------|----------------------------|
| URL de imagem                 | 2.000 caracteres no máximo |
| Formato de imagem              | JPEG ou PNG |
| Largura                     | 1.024 pixels  |
| Tamanho do arquivo                 | 1 MB |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


### Texto

| **Especificações** | **Propriedades recomendadas** |
|-------------------------|----------------------------|
| Personagens              | 120 máximo (sem imagem ou título) <br> 60 máximo (mensagem com uma imagem ou título)  |
| Ações                 | 3 máximo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


