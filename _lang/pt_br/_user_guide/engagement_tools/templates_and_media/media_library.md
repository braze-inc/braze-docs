---
nav_title: Biblioteca de mídia
article_title: Biblioteca de mídia
page_order: 0
page_type: reference
description: "Este artigo de referência cobre a biblioteca de mídia. Aqui, você pode aprender a gerenciar seus ativos em um único local centralizado, gerar imagens usando IA, acessar mídias no seu criador de mensagens."
tool: Media

---

# Biblioteca de mídia

> A biblioteca de mídia permite que você gerencie seus ativos em um único local centralizado. 

## Biblioteca de mídia versus CDN

Usar a biblioteca de mídia em vez de uma Rede de Distribuição de Conteúdo (CDN) proporciona melhor cache e performance para mensagens no app. Todos os ativos da biblioteca de mídia encontrados em uma mensagem no app serão pré-carregados para exibição mais rápida e estarão disponíveis para exibição offline. Além disso, a biblioteca de mídia é integrada com os criadores da Braze, permitindo que os profissionais de marketing selecionem ou taguem imagens em vez de copiar e colar URLs de imagens.

## Acessando a biblioteca de mídia

Na biblioteca de mídia, você pode ver o tipo de ativo, tamanho, dimensões, URL, a data em que foi adicionado à biblioteca e outras informações. Para acessar sua biblioteca de mídia da Braze, acesse **Modelos** > **Biblioteca de mídia**. Aqui, você pode:

* Fazer upload de várias imagens ao mesmo tempo
* Fazer upload de arquivos de contato virtual (.vcf)
* Fazer upload de arquivos de vídeo para uso em mensagens do WhatsApp
* Fazer upload de uma pasta com suas imagens (até 50 imagens)
* [Gerar uma imagem usando IA](#generate-ai) e armazená-la na biblioteca de mídia
* Cortar uma imagem existente para criar a proporção certa para suas mensagens
* Adicionar tags ou equipes para ajudar a organizar ainda mais suas imagens
* Pesquisar por tags ou equipes na grade da biblioteca de mídia
* Arrastar e soltar imagens ou pastas para fazer upload
* Excluir imagens

![Página da Biblioteca de Mídia que inclui uma seção "Fazer Upload para a Biblioteca" para arrastar e soltar ou fazer upload de arquivos. Há também uma lista de conteúdo enviado na biblioteca de mídia.]({% image_buster /assets/img_archive/media_library_main.png %})

Mais tarde, ao redigir uma mensagem na Braze, você pode puxar suas imagens da biblioteca de mídia.

![Duas maneiras comuns de acessar a biblioteca de mídia dependendo do criador de mensagens. Uma mostra o editor de arrastar e soltar de e-mail com o título "Imagens e GIFs" e um botão para "Adicionar da Biblioteca de Mídia". A outra mostra os editores padrão, como push e mensagens no app, com o título "Mídia" e um botão para "Adicionar Imagem".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Para saber mais sobre a biblioteca de mídia, veja o [FAQ de modelos e mídias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Especificações de imagem

Todas as imagens carregadas na biblioteca de mídia devem ter menos de 5&nbsp;MB. Os tipos de arquivo suportados são PNG, JPEG, GIF, SVG e WebP. Para recomendações específicas de imagens por canal de envio de mensagens, consulte as seções a seguir.

{% alert important %}
GIFs com formas muito alongadas (por exemplo, 3000 x 2 pixels) ou 300 ou mais quadros podem falhar ao fazer upload, mesmo que o tamanho total do arquivo seja pequeno.
{% endalert %}

### Cartões de conteúdo

{% multi_lang_include image_specs.md variable_name='content cards' %}

### E-mail

{% multi_lang_include image_specs.md variable_name="email"  %}

### Mensagens no app

{% multi_lang_include image_specs.md variable_name="in-app messages"  %}

Para saber mais, consulte os [detalhes criativos de mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Push

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

#### Comprimentos de mensagem recomendados

Para melhores resultados, consulte as diretrizes de comprimento de mensagem a seguir ao criar mensagens push. Pode haver alguma variação dependendo da presença de uma imagem, do estado da notificação (iOS) e da configuração de exibição do dispositivo do usuário, bem como do tamanho do dispositivo.

| Tipo de mensagem | Comprimento recomendado (somente texto) | Comprimento recomendado (rich) |
| --- | --- | --- |
| Tela de bloqueio do iOS | 160 caracteres | 130 caracteres |
| Central de notificações do iOS | 160 caracteres | 130 caracteres |
| Alerta em banner do iOS | 80 caracteres | 65 caracteres |
| Tela de bloqueio do Android | 49 caracteres | N/A |
| Gaveta de notificações do Android | 597 caracteres | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

Para saber mais sobre contagem de caracteres no iOS, consulte as [diretrizes de contagem de caracteres do iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count).

#### Push para a web

{% tabs %}
{% tab Imagens %}

| Navegador | Tamanho de ícone recomendado |
| --- | --- |
| Chrome | 192 x 192 px ou maior |
| Firefox | 192 x 192 px ou maior |
| Safari | 192 x 192 px ou maior (configurável por campanha com Safari 16 no macOS 13+) |
| Opera | 192 x 192 px ou maior |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| Navegador | Plataforma | Tamanho de imagem grande |
| --- | --- | --- |
| Chrome | Android | Proporção 2:1 |
| Firefox | Android | N/A |
| Chrome | Windows | Proporção 2:1 |
| Edge | Windows | Proporção 2:1 |
| Firefox | Windows | N/A |
| Opera | Windows | Proporção 2:1 |
| Chrome | macOS | N/A |
| Safari | macOS | N/A |
| Firefox | macOS | N/A |
| Opera | macOS | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Texto %}

| Navegador | Plataforma | Comprimento máximo do título | Comprimento máximo do corpo |
| --- | --- | --- | --- |
| Chrome | Android | 35 | 50 |
| Firefox | Android | 35 | 50 |
| Chrome | Windows | 50 | 120 |
| Edge | Windows | 50 | 120 |
| Firefox | Windows | 54 | 200 |
| Opera | Windows | 50 | 120 |
| Chrome | macOS | 35 | 50 |
| Safari | macOS | 38 | 84 |
| Firefox | macOS | 38 | 42 |
| Opera | macOS | 38 | 42 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}

#### Exemplos de notificações por push

{% tabs %}
{% tab iOS %}

![Notificação por push do iOS com o texto: "Oi! Esta é uma notificação por push do iOS com uma imagem" com um emoji. Há uma pequena imagem ao lado do texto.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![Notificação por push do iOS expandida com o mesmo texto da mensagem anterior e uma imagem expandida antes do texto.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Android %}

![Notificação por push do Android com uma imagem grande abaixo do texto da mensagem.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Notificações com imagens grandes são exibidas melhor ao usar uma imagem de pelo menos 600 x 300 pixels.
{% endalert %}

{% endtab %}
{% endtabs %}

### Vídeo

Vídeos enviados para a biblioteca de mídia só podem ser usados em mensagens do WhatsApp. Para saber mais, consulte [Criando uma mensagem do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

## Gerando imagens com BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Antes de usar este recurso, revise [como seus dados são usados e enviados para a OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}