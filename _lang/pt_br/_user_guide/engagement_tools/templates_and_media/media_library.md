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

Você pode encontrar a **Biblioteca de Mídia** em **Modelos**.

Você pode usar a **Biblioteca de Mídia** para:

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

![Página da Biblioteca de Mídia que inclui uma seção "Fazer Upload para a Biblioteca" para arrastar e soltar ou fazer upload de arquivos. Há também uma lista de conteúdo enviado na biblioteca de mídia.][1]

{% alert tip %} Para mais ajuda com a biblioteca de mídias, confira nosso [FAQ de Modelos e Mídias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Detalhes da imagem

Na biblioteca de mídia, é possível ver o tipo de ativo, o tamanho, as dimensões, o URL, a data em que foi adicionado à biblioteca e outras informações. 

### Usando a biblioteca de mídia versus um CDN

Usar a biblioteca de mídia proporciona melhor cache e performance para mensagens no app. Todos os ativos da biblioteca de mídia encontrados em uma mensagem no app serão pré-carregados para exibição mais rápida e estarão disponíveis para exibição offline. Além disso, a biblioteca de mídia é integrada com os compositores do Braze, permitindo que os profissionais de marketing selecionem ou taguem imagens em vez de copiar e colar URLs de imagens.

## Especificações da imagem

Todas as imagens carregadas na biblioteca de mídia devem ter menos de 5 MB. Os tipos de arquivos compatíveis são PNG, JPEG, GIF e SVG. Para recomendações específicas de imagens por canal de envio de mensagens, consulte as seguintes seções.

### Cartões de conteúdo

{% multi_lang_include image_specs.md variable_name='content cards' %}

### E-mail

{% multi_lang_include image_specs.md variable_name="email"  %}

### Mensagem no app

{% multi_lang_include image_specs.md variable_name="in-app messages"  %}

Para saber mais, consulte os detalhes criativos da [mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Push

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

##### Mais recursos

- [Push imagem e especificações de texto]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)

### Vídeo

Por enquanto, os vídeos feitos upload para a biblioteca de mídia só podem ser usados em mensagens do WhatsApp. Para saber mais, consulte [Criação de uma mensagem do Whatsapp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

{% alert important %}
A adição de vídeos às mensagens do WhatsApp está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Acessando a biblioteca de mídia a partir de um criador de mensagem

A biblioteca de mídia atua como o local centralizado do seu dashboard para ativos, pois todas as imagens são carregadas diretamente para ela. Isso permite que você reutilize imagens em diferentes envios de mensagens.

![Duas maneiras comuns de acessar a biblioteca de mídia dependendo do criador de mensagem. Um mostra o editor de arrastar e soltar de e-mail com o título "Imagens e GIFs" e um botão para "Adicionar da Biblioteca de Mídia". O outro mostra os editores padrão, como push e mensagens in-app, com o título "Mídia" e um botão para "Adicionar Imagem".][1.5]{: style="border:none"}

## Gerar uma imagem usando IA {#generate-ai}

Você pode gerar imagens para sua biblioteca de mídia usando o [DALL-E 3](https://openai.com/index/dall-e-3/), um sistema de IA da OpenAI, um provedor terceirizado do Braze. Este sistema pode criar imagens e arte realistas a partir de uma descrição em linguagem natural. Cada solicitação gera quatro variações do seu prompt, e sua empresa pode gerar imagens 10 vezes por dia. Este total se aplica a todos os usuários da sua empresa.

1. Na biblioteca de mídia, selecione <i class="fas fa-wand-magic-sparkles"></i> **Gerador de Imagens de IA**.
2. Digite uma descrição da imagem que você deseja gerar, com até 300 caracteres. Quanto mais detalhada a descrição, melhor será o seu resultado. Esse recurso só suporta entrada de texto - não é possível fazer upload de uma imagem como referência.
3. Selecione **Gerar Imagens**. Pode levar cerca de um minuto para as imagens serem geradas.
4. Selecionar <i class="fas fa-download" title="Add image to Media Library (Adicionar imagem à biblioteca de mídia)"></i> nas imagens que deseja adicionar à sua biblioteca de mídia.

![Gerador de imagens de IA modal na biblioteca de mídia.][6]{: style="max-width:75%"}

Entre você e a Braze, todas as imagens geradas com o DALL-E 3 são de sua propriedade intelectual. A Braze não ajuizará nenhuma ação de titularidade de direitos autorais em relação a tais imagens nem apresenta garantias de nenhuma natureza em relação a qualquer conteúdo ou imagem gerada por IA.

Para gerar imagens, o Braze enviará sua consulta à plataforma API da OpenAI. Todas as consultas enviadas para a OpenAI pela Braze são anonimizadas, o que significa que a OpenAI não será capaz de identificar de quem a consulta foi enviada, a menos que você inclua informações exclusivamente identificáveis na entrada que você fornecer. Conforme detalhado em [Compromissos da Plataforma API da OpenAI](https://openai.com/policies/api-data-usage-policies), os dados enviados para a API da OpenAI via Braze não são usados para treinar ou melhorar seus modelos e serão excluídos após 30 dias. Certifique-se de aderir às políticas da OpenAI relevantes para você, que podem incluir [a Política de Uso](https://openai.com/policies/usage-policies) e a [Política de Compartilhamento e Publicação](https://openai.com/policies/sharing-publication-policy). A Braze não oferece nenhuma garantia de qualquer tipo com relação a qualquer conteúdo gerado por IA. 


[1]: {% image_buster /assets/img_archive/media_library_main.png %}
[1,5]: {% image_buster /assets/img_archive/media_library_composers.png %}
[2]: {% image_buster /assets/img_archive/media_library_crop1.png %}
[3]: {% image_buster /assets/img_archive/media_library_crop2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
Daqui a [5]: https://imageoptim.com/mac
[6]: {% image_buster /assets/img_archive/media_library_dalle.png %}
