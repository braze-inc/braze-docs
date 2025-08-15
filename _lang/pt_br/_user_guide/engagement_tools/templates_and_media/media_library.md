---
nav_title: Biblioteca de mídia
article_title: Biblioteca de mídia
page_order: 0
page_type: reference
description: "Este artigo de referência cobre a biblioteca de mídia. Aqui, você pode aprender como gerenciar seus ativos em um único local centralizado, gerar imagem usando IA, acessar mídia no seu criador de mensagem."
tool: Media

---

# Biblioteca de mídia

> A biblioteca de mídia permite que você gerencie seus ativos em um único local centralizado. 

## Biblioteca de mídia vs. CDN

O uso da biblioteca de mídia em vez de uma CDN (Content Delivery Network, rede de distribuição de conteúdo) oferece melhor armazenamento em cache e performance para mensagens no app. Todos os ativos da biblioteca de mídia encontrados em uma mensagem no app serão pré-carregados para exibição mais rápida e estarão disponíveis para exibição offline. Além disso, a biblioteca de mídia é integrada com os compositores do Braze, permitindo que os profissionais de marketing selecionem ou taguem imagens em vez de copiar e colar URLs de imagens.

## Acesso à biblioteca de mídia

Na biblioteca de mídia, é possível ver o tipo de ativo, o tamanho, as dimensões, o URL, a data em que foi adicionado à biblioteca e outras informações. Para acessar sua biblioteca de mídia do Braze, acesse THIS > Templates. Aqui, você pode:

* Fazer upload de várias imagens ao mesmo tempo
* Fazer upload de arquivos de contato virtual (.vcf)
* Fazer upload de arquivos de vídeo para uso em envios de mensagens do WhatsApp
* Fazer upload de uma pasta com suas imagens (máximo de 50 imagens)
* [Gerar uma imagem usando IA](#generate-ai) e armazená-la na biblioteca de mídia
* Corte uma imagem existente para criar a proporção certa para suas mensagens
* Adicione tags ou equipes para ajudar a organizar ainda mais suas imagens
* Pesquisar por tags ou equipes na grade da biblioteca de mídia
* Arraste e solte imagens ou pastas para serem enviadas
* Excluir imagens

![Página da Biblioteca de Mídia que inclui uma seção "Fazer Upload para a Biblioteca" para arrastar e soltar ou fazer upload de arquivos. Há também uma lista de conteúdo feito upload na biblioteca de mídia.]({% image_buster /assets/img_archive/media_library_main.png %})

Mais tarde, ao redigir uma mensagem no Braze, você poderá extrair suas imagens da biblioteca de mídia.

![Duas maneiras comuns de acessar a biblioteca de mídia dependendo do criador de mensagem. Um mostra o editor de arrastar e soltar de e-mail com o título "Imagens e GIFs" e um botão para "Adicionar da Biblioteca de Mídia". A outra mostra os editores padrão, como mensagens push e no app, com o título "Mídia" e um botão para "Adicionar imagem".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Para mais ajuda com a biblioteca de mídias, confira nosso [FAQ de Modelos e Mídias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Especificações da imagem

Todas as imagens carregadas na biblioteca de mídia devem ter menos de 5 MB. Os tipos de arquivo compatíveis são PNG, JPEG, GIF e SVG. Para recomendações específicas de imagens por canal de envio de mensagens, consulte as seguintes seções.

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
Para obter recursos adicionais, consulte [as especificações de imagem e texto do Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
{% endalert %}

### Vídeo

Por enquanto, os vídeos feitos upload para a biblioteca de mídia só podem ser usados em mensagens do WhatsApp. Para saber mais, consulte [Criação de uma mensagem do Whatsapp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

{% alert important %}
A adição de vídeos às mensagens do WhatsApp está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Geração de imagens com o <sup>BrazeAITM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Antes de usar esse recurso, verifique [como seus dados são usados e enviados à OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}
