---
nav_title: Configurações de estilo global de e-mail
article_title: Configurações de estilo global de e-mail
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "Este artigo de referência cobre como definir configurações de estilo de e-mail global no editor de arrastar e soltar para suas campanhas e canvas."
tool: 
  - Campaigns
  - Canvas
---

# Configurações de estilo de e-mail global

> Com as configurações de estilo global, você pode personalizar a aparência de suas campanhas de e-mail e canvas. Você pode adicionar e personalizar um tema padrão para o seu editor de arrastar e soltar. Isso inclui editar seus estilos para títulos de e-mail, texto, botões e mais. Usar uma combinação dessas configurações pode ajudar a criar uma aparência consistente em seu envio de mensagens de e-mail.

Para editar suas configurações de estilo global, acessar **Configurações** > **Preferências de e-mail** > **Preferências de e-mail de arrastar e soltar**. Depois de editar os estilos no editor de e-mail de arrastar e soltar, clique em **Salvar**. Para personalizar ainda mais suas campanhas de e-mail e canvas, confira como você pode incorporar blocos de editor de arrastar e soltar][8].

![][1]

{% alert note %}
As atualizações feitas nas configurações de estilo global serão aplicadas a todas as futuras campanhas de e-mail e canvas.
{% endalert %} 

## Estilização básica 

Para **Estilo Básico**, você pode definir as cores de fundo padrão do seu e-mail e conteúdo para suas campanhas de e-mail e canvas. Você também pode selecionar uma fonte padrão, adicionar uma fonte personalizada e editar as cores dos links.

![Opções básicas de estilo que incluem opções para editar o e-mail e as cores de fundo do conteúdo, o nome da fonte padrão e a cor padrão do link.][2] 

## Fonte personalizada

Com fontes personalizadas, você pode adicionar manualmente uma fonte da web para consistência de marca em várias plataformas de e-mail. Você pode adicionar uma fonte personalizada por seção. 

Antes de adicionar uma fonte personalizada, verifique se o arquivo de fonte personalizada atende aos seguintes requisitos:

- CORS deve ser habilitado no servidor que fornece o arquivo de fonte personalizada. Isso geralmente é gerenciado pela sua equipe de TI. 
  - O arquivo de fonte personalizado deve ter o cabeçalho: `Access-Control-Allow-Origin: *`
- A URL do arquivo deve apontar para um arquivo CSS (não WOFF, OTF, etc.)
- O nome da fonte personalizada deve corresponder ao nome da face da fonte no arquivo CSS

Para adicionar uma fonte personalizada:

1. Clique em **Adicionar uma fonte personalizada** abaixo do **Nome da Fonte Padrão** da seção de estilo.
2. Para o campo **Nome da Fonte**, insira o mesmo nome da fonte que aparece no seu arquivo de fonte personalizado. Certifique-se de que o nome esteja capitalizado e espaçado corretamente. 
3. Digite a URL correspondente para o campo **URL da Fonte**.
4. Verifique se a prévia mostra sua fonte personalizada antes de salvar. 
5. Clique **Salvar** para usar a fonte personalizada como sua fonte de e-mail padrão. 

{% alert important %}
O Gmail não suporta fontes personalizadas, então sua fonte personalizada pode ser exibida como uma fonte padrão do sistema. Para outras plataformas de e-mail, verifique se sua fonte personalizada é exibida corretamente antes de enviar seu envio de mensagens de e-mail.
{% endalert %}

Esteja ciente de que o fornecedor de fontes personalizadas pode coletar dados pessoais de seus destinatários. Você deve revisar as políticas do seu provedor de fontes antes de usar.

Para usar fontes personalizadas alternativas em suas campanhas de e-mail, você tem a opção de criar um [modelo de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) ou [Blocos de Conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/). Certifique-se de verificar se a sua escolha de fonte ainda é segura para a web e suportada nas suas plataformas de e-mail. 

### fonte de fallback

Fontes fallback são usadas para o título, cabeçalho e texto do corpo quando sua escolha de fonte padrão não é suportada pelo provedor de caixa de entrada ou sistema operacional. Por padrão, a Braze define automaticamente Arial como fonte de fallback quando as configurações de estilo global são salvas. Você também tem a opção de adicionar serif ou sans serif como opções para sua família de fontes padrão.

![][11]

Você pode adicionar até 17 fallback fontes. A primeira fonte de fallback selecionada será a primeira tentativa. A fonte de fallback será aplicada apenas para novos modelos criados, campanhas de e-mail e componentes do canva. A fonte de fallback não é configurada automaticamente para mensagens que foram criadas antes que a fonte de fallback fosse especificada. Recomendamos fortemente selecionar fontes fallback que sejam semelhantes ao envio de mensagens de e-mail para manter a consistência da sua marca.

## Estilização de título

Aqui, você pode ajustar os estilos dos títulos do seu e-mail editando o tamanho da fonte, a cor da fonte e o alinhamento do texto. Isso se aplica ao cabeçalho principal e ao cabeçalho secundário. 

![][9]

Opcionalmente, você pode substituir o estilo padrão do tema do seu editor de arrastar e soltar. Clique em **Substituir estilo padrão** para aplicar sua escolha de estilo de título. Isso pode incluir a definição de uma fonte e cor de link diferentes.

## Estilo de parágrafo

Para definir um estilo de parágrafo padrão, acessar o **Estilo de Parágrafo**, insira o **Tamanho da Fonte** e selecione **Cor da Fonte** para escolher uma cor de fonte. Você também pode ajustar o estilo do bloco para o texto do corpo editando os valores de **Espaçamento Superior**, **Espaçamento Direito**, **Espaçamento Inferior** e **Espaçamento Esquerdo**. Isso se aplicará ao espaçamento em todas as quatro áreas ao redor do bloco de parágrafo.

![][7]

## Estilização de lista

Ao adicionar listas ao seu envio de mensagens, a seção **Estilo de Lista** cria consistência em como suas listas são estilizadas. Isso inclui detalhes como: 

- Tamanho da fonte
- Cor da fonte
- Peso da fonte
- Altura da linha
- Alinhamento
- Direção do texto
- Espaçamento entre as letras
- Espaçamento entre itens da lista
- Recuo do item da lista
- Tipo de lista
- Tipo de estilo de lista

Você pode definir o **Tipo de Lista** como numerado ou com marcadores. O **Tipo de Estilo de Lista** fornece personalização adicional para o estilo de suas listas. Por exemplo, você pode definir os tipos de lista para serem sempre com marcadores e para cada marcador ser um quadrado.  

![][10]

## Estilização de botões

Na seção **Estilo do Botão**, você pode editar os seguintes estilos padrão para o botão:
- Cor de fundo
- Tamanho da fonte
- Cor da fonte
- Raio da borda
- Cor da borda
- Peso da borda
- Preenchimento do botão

![][12]

Como em todas as outras seções de estilo, você pode ajustar o estilo do bloco editando os valores de **Espaçamento Superior**, **Espaçamento Direito**, **Espaçamento Inferior** e **Espaçamento Esquerdo**.

## Largura do modelo de e-mail

Usando a largura do modelo de e-mail, você pode ajustar e definir uma largura para consistência em suas campanhas de e-mail. 

![][13]

## Largura do bloco de conteúdo

Você também pode definir a largura do bloco de conteúdo no editor de arrastar e soltar de e-mail. Recomendamos combinar a largura do bloco de conteúdo com a largura do modelo de e-mail.

![][14]


[1]: {% image_buster /assets/img_archive/dnd_global_style_settings.png %}
[2]: {% image_buster /assets/img_archive/dnd_basic_styling.png %}
[3]: {% image_buster /assets/img_archive/dnd_custom_font.png %}
[5]: {% image_buster /assets/img_archive/dnd_button_styling.png %}
[6]: {% image_buster /assets/img_archive/dnd_heading_styling.png %}
[7]: {% image_buster /assets/img_archive/dnd_paragraph_styling.png %}
[9]: {% image_buster /assets/img_archive/dnd_title_styling.png %}
[10]: {% image_buster /assets/img_archive/dnd_list_styling.png %}
[11]: {% image_buster /assets/img_archive/dnd_fallbacks.png %}
[12]: {% image_buster /assets/img_archive/dnd_button_styling.png %}
[13]: {% image_buster /assets/img_archive/dnd_email_template_width.png %}
[14]: {% image_buster /assets/img_archive/dnd_content_block_width.png %}
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks
