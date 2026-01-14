---
nav_title: Biblioteca de mídia
article_title: Biblioteca de mídia
page_order: 0
page_type: reference
description: "Este artigo de referência aborda a biblioteca de mídia. Aqui, você pode aprender a gerenciar seus ativos em um único local centralizado, gerar imagens usando IA e acessar a mídia em seu compositor de mensagens."
tool: Media

---

# Biblioteca de mídia

> A biblioteca de mídia permite que você gerencie seus ativos em um único local centralizado. 

## Biblioteca de mídia vs. CDN

O uso da biblioteca de mídia em vez de uma CDN (Content Delivery Network) proporciona melhor armazenamento em cache e desempenho para mensagens no aplicativo. Todos os ativos da biblioteca de mídia encontrados em uma mensagem in-app serão armazenados em cache para uma exibição mais rápida e estarão disponíveis para exibição off-line. Além disso, a biblioteca de mídia é integrada aos compositores do Braze, permitindo que os profissionais de marketing selecionem ou marquem imagens em vez de copiar e colar URLs de imagens.

## Acesso à biblioteca de mídia

Na biblioteca de mídia, você pode ver o tipo de ativo, o tamanho, as dimensões, o URL, a data em que foi adicionado à biblioteca e outras informações. Para acessar sua biblioteca de mídia do Braze, vá para THIS > **Templates**. Aqui, você pode:

* Faça upload de várias imagens de uma só vez
* Carregar arquivos de contatos virtuais (.vcf)
* Carregar arquivos de vídeo para uso em mensagens do WhatsApp
* Faça upload de uma pasta com suas imagens (máximo de 50 imagens)
* [Gerar uma imagem usando IA](#generate-ai) e armazená-la na biblioteca de mídia
* Recorte uma imagem existente para criar a proporção correta para suas mensagens
* Adicione tags ou equipes para ajudar a organizar melhor suas imagens
* Pesquise por tags ou equipes na grade da biblioteca de mídia
* Arraste e solte as imagens ou pastas a serem carregadas
* Excluir imagens

Página Media Library que inclui uma seção "Upload To Library" para arrastar e soltar ou fazer upload de arquivos. Há também uma lista de conteúdo carregado na biblioteca de mídia.]({% image_buster /assets/img_archive/media_library_main.png %})

Mais tarde, ao redigir uma mensagem no Braze, você poderá extrair suas imagens da biblioteca de mídia.

\![Duas maneiras comuns de acessar a biblioteca de mídia, dependendo do compositor da mensagem. Uma mostra o Editor de arrastar e soltar do e-mail com o título "Imagens e GIFs" e um botão para "Adicionar da biblioteca de mídia". A outra mostra os editores padrão, como mensagens push e no aplicativo, com o título "Mídia" e um botão para "Adicionar imagem".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Para obter mais ajuda com a biblioteca de mídia, consulte as [Perguntas frequentes sobre modelos & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Especificações da imagem

Todas as imagens carregadas na biblioteca de mídia devem ter menos de 5 MB. Os tipos de arquivos compatíveis são PNG, JPEG, GIF e SVG. Para obter recomendações específicas de imagens por canal de mensagens, consulte as seções a seguir.

### Cartões de conteúdo

{% multi_lang_include image_specs.md variable_name='content cards' %}

### E-mail

{% multi_lang_include image_specs.md variable_name="email"  %}

### Mensagens no aplicativo

{% multi_lang_include image_specs.md variable_name="in-app messages"  %}

Para obter mais informações, consulte [Detalhes de criação de mensagens in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Empurrar

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

{% alert note %}
Para obter recursos adicionais, consulte [as especificações de imagem e texto do Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
{% endalert %}

### Vídeo

Por enquanto, os vídeos carregados na biblioteca de mídia só podem ser usados em mensagens do WhatsApp. Para obter mais informações, consulte [Criação de uma mensagem do Whatsapp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

## Geração de imagens com o <sup>BrazeAITM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Antes de usar esse recurso, verifique [como seus dados são usados e enviados à OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}
