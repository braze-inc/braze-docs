---
nav_title: Cloudinary
article_title: Cloudinary
description: "Este artigo de referência descreve a parceria entre a Braze e a cloudinary."
alias: /partners/cloudinary/
page_type: partner
search_tag: Partner
---

# Cloudinary

> [O Cloudinary](https://www.cloudinary.com?utm_source=braze_partner_page) é uma plataforma de imagem e vídeo usada para gerenciar, editar, otimizar e fornecer imagens e vídeos em escala para qualquer campanha em todos os canais e jornadas de clientes. Quando integrado e ativado, o gerenciamento de mídia do Cloudinary possibilita o fornecimento de ativos dinâmicos, contextuais e personalizados para suas campanhas e Canvas do Braze. 

## Sobre essa integração

A conexão do Cloudinary ao Braze dá às marcas acesso à mídia visual armazenada no Cloudinary Assets para uso nos canais de envio de mensagens do Braze. Com os links dinâmicos do Cloudinary, é possível selecionar e personalizar imagens e vídeos em tempo real com base nos atributos do usuário do Braze. Juntos, a Cloudinary e a Braze oferecem suporte à criação de campanhas personalizadas e visualmente ricas que contam a story de cada produto e proporcionam experiências únicas em escala.

Esta página descreve quatro métodos de integração possíveis, mas não exaustivos, entre o Cloudinary e o Braze. Esses métodos de integração dependem principalmente da modificação de links de ativos copiados manualmente da biblioteca de mídia do Cloudinary. 

{% alert important %}
Métodos de integração mais avançados, incluindo o uso do [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) para chamar a [API de administração](https://cloudinary.com/documentation/admin_api#banner) do Cloudinary, são possíveis, mas a abordagem varia de acordo com o cliente. Entre em contato com o gerente de sucesso do cliente da Cloudinary e da Braze para obter orientação.
{% endalert %}

## Pré-requisitos

| Solicitações     | Descrição |                        
|-----------------------|-----------------|
| Conta do Cloudinary  | É necessário ter uma [conta no Cloudinary](https://cloudinary.com/users/register_free?utm_source=braze+docs+page) para aproveitar essa parceria  |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Métodos de integração

{% alert tip %}
Alguns desses métodos de integração usam as `f_auto` e `q_auto` Cloudinary Transformations, que oferecem uma personalização mais profunda do comportamento e da aparência dos ativos [de imagem](https://cloudinary.com/documentation/image_transformations#banner) e [vídeo](https://cloudinary.com/documentation/video_manipulation_and_delivery#banner). Para saber mais sobre como modificar um link de ativo do Cloudinary para incluir transformações, consulte [Estrutura de URL de transformação](https://cloudinary.com/documentation/image_transformations#transformation_url_structure).
{% endalert %}

{% tabs %}
{% tab Cloudinary DAM %}

## Selecione os ativos da campanha por meio do Cloudinary DAM

A maneira mais direta de usar imagens e vídeos diretamente do DAM do Cloudinary em suas campanhas e telas do Braze é extrair o URL da página de **ativos** da biblioteca de mídia do Cloudinary.

![Uma exibição de grade da biblioteca de ativos de imagem do Cloudinary, com o canto superior direito de uma das imagens destacado, mostrando uma dica de ferramenta "Copiar URL".]({% image_buster /assets/img/cloudinary/one.png %})

### Configuração de imagens e GIFs

1. Copie o URL da imagem ou do GIF do DAM no Cloudinary acessando **Ativos** > **Biblioteca de mídia** > **Ativos** > **Copiar URL**.
2. Crie a tag de imagem em HTML e, em seguida, adicione `f_auto,q_auto` ao URL copiado para otimizar a imagem ou o GIF.

#### Exemplo de URL de imagem

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/v1678993440/f_auto,q_auto/cld-sample.jpg" alt="Summer Campaign">
</img>
```
{% endraw %}

### Configuração de vídeos

1. Copie o link da imagem ou do GIF do DAM no Cloudinary acessando **Ativos** > **Biblioteca de mídia** > **Ativos** > **Copiar URL**.
2. Crie a tag de vídeo em HTML e, em seguida, adicione `f_auto,q_auto` ao URL copiado para otimizar automaticamente o formato e a qualidade do vídeo.

#### Exemplo de URL de vídeo

{% raw %}
```bash
<video class="video" autoplay muted playsinline controls>
  <source src="https://res.cloudinary.com/demo/video/upload/v1651840278/f_auto,q_auto/samples/cld-sample-video.mp4">
</video>
```
{% endraw %}

Consulte o [vídeo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/video/) para obter considerações específicas sobre Android e iOS. 

{% endtab %}
{% tab Convert videoes into GIFs %}

## Converta vídeos em GIFs para envio de e-mail

Use o `f_auto:animated` [Cloudinary Transformation](https://cloudinary.com/documentation/image_transformations/) para converter automaticamente ativos de vídeo em GIFs. Isso é particularmente valioso se estiver usando o canal de e-mail do Braze, pois os GIFs são otimizados para reduzir as cargas úteis de e-mail, que, se forem muito altas, podem causar problemas de entregabilidade. 

### Configuração da conversão

1. Copie o URL do vídeo do Cloudinary DAM.
2. Crie a tag de imagem e adicione `f_auto:animated,fl_lossy` para reduzir o tamanho do GIF e escolha o melhor formato de animação para o cliente.
3. Adicione `c_scale,w_nnn` para corresponder à largura desejada do GIF no layout do e-mail.
4. Adicione `e_loop` para repetir a animação.

#### Exemplo de URL de GIF

{% raw %}
```
https://res.cloudinary.com/demo/video/upload/c_scale,w_500,e_loop/f_auto:animated,fl_lossy/samples/cld-sample-video.gif
```
{% endraw %}

{% endtab %}
{% tab Target attributes %}

## Selecione dinamicamente os ativos da campanha com base nos atributos de direcionamento

Esse método de integração ativa a personalização dinâmica da mídia, selecionando de forma inteligente o melhor ativo para cada usuário com base em suas atribuições em tempo real. 

Se você incluir tags Liquid como parâmetros em um link Cloudinary em uma mensagem de campanha do Braze, quando a mensagem for enviada, as atribuições associadas do Braze substituirão dinamicamente as tags Liquid. Podem ser dados específicos do usuário, como idioma ou nível de cliente. O Cloudinary usará essas atribuições para determinar qual ativo de campanha é mais adequado para esse usuário e retornará automaticamente a imagem ou o vídeo correto. Isso faz com que os destinatários recebam apenas ativos que sejam contextualmente relevantes e aprovados pela marca.

### Como funciona?

O Cloudinary organiza os ativos da campanha usando [tags](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#tags) e [metadados estruturados (SMD)](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#structured_metadata) para torná-los pesquisáveis. 

Cada ativo de campanha é agrupado em uma tag de campanha (por exemplo, `spring_launch`) e enriquecido com campos de metadados estruturados que correspondem a atribuições Braze como `language=en` ou `tier=gold`. Quando o Braze chama o link do Cloudinary, uma [função personalizada](https://cloudinary.com/documentation/custom_functions#javascript_filters) processa os atributos recebidos, procura o ativo com tags e metadados correspondentes e, em seguida, retorna a correspondência mais adequada. 

Se uma correspondência exata não for encontrada, a função seleciona automaticamente uma opção fallback ou "next best" para continuidade em cada experiência. Quando o ativo é selecionado, a camada de transformação do Cloudinary (por exemplo, `f_auto` ou `q_auto`) otimiza a mídia para entrega. Essa combinação de tag, metadados e funções personalizadas oferece aos desenvolvedores uma maneira flexível e orientada por API para automatizar o fornecimento personalizado de ativos.

{% alert tip %}
Consulte o [repositório`braze-personalization` GitHub](https://github.com/cloudinary-devs/braze-personalization) da Cloudinary para obter instruções sobre como criar e aplicar funções personalizadas e um exemplo de função personalizada para seleção de ativos e opções de fallback para uma determinada campanha. Para obter mais orientações, entre em contato com a equipe de suporte do Cloudinary.
{% endalert %}

### Pré-requisitos

Para ativar a seleção dinâmica de ativos, o Cloudinary deve ser capaz de retornar um conjunto de ativos com base em tags e metadados. Se o tipo de entrega da lista for restrito, o Cloudinary não poderá fornecer a lista dinâmica necessária para a seleção personalizada de ativos nas campanhas do Braze.
- Liberar o tipo de entrega de lista: Abra as Configurações de segurança em seu Console do Cloudinary e desmarque o item da lista de recursos em Tipos de imagem restritos.

### Configuração de seleção dinâmica

1. Configure a tag e os metadados dos ativos no Cloudinary.
2. Faça upload de sua função personalizada para o Cloudinary DAM.
3. Crie o URL do Cloudinary para a tag desejada.
4. Usando o URL da tag como base, adicione tags Liquid de imagem dinâmica para incorporar os atributos do Braze e a função personalizada.

#### Exemplo de URL

Este exemplo presume que os ativos no Cloudinary têm dois campos SMD definidos ("localização" e "público") preenchidos com os valores esperados correspondentes às atribuições do Braze. Além disso, os ativos necessários para a campanha receberam a tag "samples", e a função personalizada `segmentedBanner.js` foi feita upload na conta do Cloudinary. 

{% raw %}
```bash

// Use the appropriate Braze attributes.
{% assign audience = {{custom_attribute.${sample_audience_identifier}}} %} 
{% assign locale = {{${language}}}%} 

// The URL for the "samples" tag used in the campaign is https://papish.cloudinary.us/image/list/v1690000000/samples.json, which is the base for the dynamic image URL.
<img src="https://papish.cloudinary.us/image/list/f_auto,q_auto/$locale_#{locale}/$audience_!{audience}!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/campaigns/samples.json" alt="Banner"> 
```
{% endraw %}

##### URLs de saída

- URL de saída para usuários com público `internal` e localização `en`: 
```
https://papish.cloudinary.us/image/list/f_auto,q_auto/$locale_!en!/$audience_!Internal!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- URL de saída para usuários com público `external` e localização `es`: 
```
https://papish.cloudinary.us/image/list/$locale_!es!/$audience_!External!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- URL da imagem fallback: 
```
https://papish.cloudinary.us/image/list/$locale_!unknown!/$audience_!unknown!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```

{% endtab %}
{% tab Personalized image generation %}

## Geração de imagens personalizadas

[As transformações de sobreposição de texto](https://cloudinary.com/documentation/accessible_media_visual_audio_clarity#text_overlays_on_images_and_videos/) do Cloudinary usam dados de usuários do Braze diretamente em um ativo do Cloudinary. 

O exemplo a seguir demonstra como a Transformação `l_text` pode ser usada para inserir o nome de um usuário em um ativo. É possível obter uma personalização adicional usando as Liquid tags ao desenvolver campanhas e Canvas para determinar o texto que deve preencher os parâmetros do site `l_text`.

Para obter mais orientações sobre como os parâmetros de transformação podem ser usados para projetar um ativo, entre em contato com a equipe de suporte do Cloudinary.

### Exemplo `l_text` Transformação

{% raw %}
```bash
{% assign first_name = {{${first_name}}}%} 
{% assign second_name = {{${last_name}}}%} 

<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20{{first_name}}%20{{second_name}}%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

#### Exemplo de URL de saída

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20John%20Smith%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

![Uma igreja branca com telhado azul e vista para o mar. Na parte superior esquerda da imagem, as palavras "John Smith" são impostas em um grande retângulo escuro e aberto.]({% image_buster /assets/img/cloudinary/two.png %})

```
{% endtab %}
{% endtabs %}
