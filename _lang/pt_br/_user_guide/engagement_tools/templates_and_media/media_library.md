---
nav_title: Biblioteca de mídia
article_title: Biblioteca de mídia
page_order: 0
page_type: reference
description: "Este artigo de referência cobre a biblioteca de mídia. Aqui, você pode aprender a gerenciar seus ativos em um único local centralizado, gerar imagens usando IA, acessar mídias no seu criador de mensagem."
tool: Media

---

# Biblioteca de mídia

> A biblioteca de mídia permite que você gerencie seus ativos em um único local centralizado. 

## Biblioteca de mídia versus CDN

Usar a biblioteca de mídia em vez de uma Rede de Distribuição de Conteúdo (CDN) proporciona melhor cache e performance para mensagens no app. Todos os ativos da biblioteca de mídia encontrados em uma mensagem no app serão pré-carregados para exibição mais rápida e estarão disponíveis para exibição offline. Além disso, a biblioteca de mídia é integrada com os compositores do Braze, permitindo que os profissionais de marketing selecionem ou taguem imagens em vez de copiar e colar URLs de imagens.

## Acessando a biblioteca de mídia

Dentro da biblioteca de mídia, você pode ver o tipo de ativo, tamanho, dimensões, URL, a data em que foi adicionado à biblioteca e outras informações. Para acessar sua biblioteca de mídia Braze, vá para **Templates** > **Media Library**. Aqui, você pode:

* Fazer upload de várias imagens ao mesmo tempo
* Fazer upload de arquivos de contato virtual (.vcf)
* Fazer upload de arquivos de vídeo para uso em mensagens do WhatsApp
* Fazer upload de uma pasta com suas imagens (até 50 imagens)
* [Gerar uma imagem usando IA](#generate-ai) e armazená-la na biblioteca de mídia
* Corte uma imagem existente para criar a proporção certa para suas mensagens
* Adicione tags ou equipes para ajudar a organizar ainda mais suas imagens
* Pesquisar por tags ou equipes na grade da biblioteca de mídia
* Arraste e solte imagens ou pastas para serem enviadas
* Excluir imagens

![Página da Biblioteca de Mídia que inclui uma seção "Fazer Upload para a Biblioteca" para arrastar e soltar ou fazer upload de arquivos. Há também uma lista de conteúdo enviado na biblioteca de mídia.]({% image_buster /assets/img_archive/media_library_main.png %})

Mais tarde, ao redigir uma mensagem no Braze, você pode puxar suas imagens da biblioteca de mídia.

![Duas maneiras comuns de acessar a biblioteca de mídia dependendo do criador de mensagem. Um mostra o editor de arrastar e soltar de e-mail com o título "Imagens e GIFs" e um botão para "Adicionar da Biblioteca de Mídia". O outro mostra os editores padrão, como push e mensagens no app, com o título "Mídia" e um botão para "Adicionar Imagem".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Para saber mais sobre a biblioteca de mídia, veja o [Templates & FAQ de Mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Especificações da imagem

Todas as imagens carregadas na biblioteca de mídia devem ter menos de 5 MB. Os tipos de arquivo suportados são PNG, JPEG, GIF, SVG e WebP. Para recomendações específicas de imagens por canal de envio de mensagens, consulte as seguintes seções.

{% alert important %}
GIFs com formas muito alongadas (por exemplo, 3000 x 2 pixels) ou 300 ou mais quadros podem falhar ao fazer upload, mesmo que o tamanho total do arquivo seja pequeno.
{% endalert %}

### Cartões de conteúdo

{% multi_lang_include image_specs.md variable_name='content cards' %}

### E-mail

{% multi_lang_include image_specs.md variable_name="email"  %}

### Mensagem no app

{% multi_lang_include image_specs.md variable_name="in-app messages"  %}

Para saber mais, consulte os detalhes criativos da [mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Push

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

{% alert note %}
Para recursos adicionais, veja [Especificações de imagem e texto para Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
{% endalert %}

### Vídeo

Vídeos enviados para a biblioteca de mídia só podem ser usados em mensagens do WhatsApp. Para mais informações, consulte [Criando uma mensagem do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

## Gerando imagens com BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Antes de usar este recurso, revise [como seus dados são usados e enviados para a OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}
