---
nav_title: Configurações globais de estilo de e-mail
article_title: Configurações globais de estilo de e-mail
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "Este artigo de referência aborda como definir configurações globais de estilo de e-mail no editor de arrastar e soltar para suas campanhas e Canvases."
tool: 
  - Campaigns
  - Canvas
---

# Configurações de estilo global de e-mail

> Com as configurações de estilo global, você pode personalizar a aparência de suas campanhas de e-mail e Canvases. Você pode adicionar e personalizar um tema padrão para seu editor de arrastar e soltar. Isso inclui a edição de seus estilos para títulos de e-mail, texto, botões e muito mais. O uso de uma combinação dessas configurações pode ajudar a criar uma aparência consistente em suas mensagens de e-mail.

Para editar suas configurações de estilo global, vá para **Configurações** > **Preferências de e-mail** > **Preferências de e-mail do tipo arrastar e soltar**. Após editar os estilos no editor de e-mail do tipo arrastar e soltar, selecione **Salvar**. Para personalizar ainda mais suas campanhas de e-mail e Canvases, veja como você pode incorporar [blocos de editor de arrastar e soltar]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks).

Seção Email Global Style Settings (Configurações de estilo global de e-mail) na guia Drag-And-Drop Email Editor Settings (Configurações do editor de e-mail com arrastar e soltar).]({% image_buster /assets/img_archive/dnd_global_style_settings.png %})

{% alert note %}
As atualizações feitas nas configurações de estilo global serão aplicadas a todas as futuras campanhas de e-mail e Canvases.
{% endalert %} 

## Estilo básico 

No **Basic Styling**, você pode definir as cores de fundo padrão do e-mail e do conteúdo para suas campanhas de e-mail e Canvases. Você também pode selecionar uma fonte padrão, adicionar uma fonte personalizada e editar as cores dos links.

Opções básicas de estilo que incluem opções para editar as cores de fundo do e-mail e do conteúdo, o nome da fonte padrão e a cor padrão do link.]({% image_buster /assets/img_archive/dnd_basic_styling.png %}) 

## Fonte personalizada

Com as fontes personalizadas, você pode adicionar manualmente uma fonte da Web para manter a consistência da marca em várias plataformas de e-mail. É possível adicionar uma fonte personalizada para cada seção de estilo.

### Requisitos

Antes de adicionar uma fonte personalizada, verifique se o arquivo de fonte personalizada atende aos seguintes requisitos:

- O CORS deve estar ativado no servidor que fornece o arquivo de fonte personalizado. Isso geralmente é gerenciado pela sua equipe de TI. 
  - O arquivo de fonte personalizada deve ter o cabeçalho: `Access-Control-Allow-Origin: *`
- O URL do arquivo deve apontar para um arquivo CSS (não WOFF ou OTF).
- O nome da fonte personalizada deve corresponder ao nome da face da fonte no arquivo CSS.

Observe que o provedor de fontes personalizadas pode coletar dados pessoais de seus destinatários. Você deve analisar as políticas do seu provedor de fontes antes de usá-las.

### Adição de uma fonte personalizada

Para adicionar uma fonte personalizada, faça o seguinte:

1. Na seção **Default Font Name (Nome da fonte padrão** ) de **Basic Styling (Estilo básico**), selecione **Add a custom font (Adicionar uma fonte personalizada**).
2. No campo **Font Name (Nome da fonte** ), digite o mesmo nome de fonte que aparece no arquivo de origem da fonte personalizada. Certifique-se de que esse nome esteja em letras maiúsculas e com espaçamento correto.
3. Digite o URL correspondente no campo **Font URL (URL da fonte** ).
4. Verifique se a visualização mostra sua fonte personalizada.
5. Selecione **Salvar** para usar a fonte personalizada como fonte padrão do e-mail. 

{% alert important %}
O Gmail não oferece suporte a fontes personalizadas, portanto, sua fonte personalizada pode ser exibida como uma fonte padrão do sistema. Para outras plataformas de e-mail, verifique se a fonte personalizada é exibida corretamente antes de enviar a mensagem de e-mail.
{% endalert %}

Para usar outras fontes personalizadas em suas campanhas de e-mail, você pode criar um [modelo de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) ou [blocos de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/) que inclua a fonte personalizada. Por exemplo, você pode criar um modelo de e-mail específico projetado com fontes personalizadas e festivas, adaptadas ao tema da sua venda. Certifique-se de verificar se a fonte escolhida ainda é segura para a Web e compatível com suas plataformas de e-mail.

### Fonte alternativa

As fontes alternativas são usadas para o título, o cabeçalho e o corpo do texto quando a fonte padrão escolhida não é compatível com o provedor da caixa de entrada ou com o sistema operacional. Por padrão, o Braze define automaticamente a Arial como uma fonte alternativa quando as configurações de estilo global são salvas. Você também tem a opção de adicionar serifa ou sans serifa como opções para a família de fontes padrão.

\![Um exemplo de "Arial" como uma fonte alternativa com "Sans-serif" como a família de fontes.]({% image_buster /assets/img_archive/dnd_fallbacks.png %})

Você pode adicionar até 17 fontes alternativas. A primeira fonte alternativa selecionada será a primeira a ser tentada. A fonte alternativa será aplicada somente a modelos recém-criados, campanhas de e-mail e componentes do Canvas. A fonte de fallback não é definida automaticamente para mensagens que foram criadas antes de a fonte de fallback ser especificada. É altamente recomendável selecionar fontes alternativas que sejam semelhantes às suas mensagens de e-mail para manter a consistência em toda a sua marca.

## Estilo do título

Aqui, você pode ajustar os estilos dos títulos dos e-mails editando o tamanho da fonte, a cor da fonte e o alinhamento do texto. Isso se aplica ao cabeçalho principal e ao cabeçalho secundário. 

\![Title Configurações de estilo para um cabeçalho principal e um cabeçalho secundário alinhados ao centro.]({% image_buster /assets/img_archive/dnd_title_styling.png %})

Opcionalmente, você pode substituir o estilo padrão do tema do editor de arrastar e soltar. Selecione **Override default style (Substituir estilo padrão** ) para aplicar o estilo de título de sua escolha. Isso pode incluir a configuração de uma fonte e de uma cor de link diferentes.

## Estilo de parágrafo

Para definir um estilo de parágrafo padrão, vá para **Paragraph Styling (Estilo de parágrafo**), digite o **Font Size (Tamanho da fonte**) e selecione **Font Color (Cor da fonte** ) para escolher uma cor de fonte. Você também pode ajustar o estilo do bloco para o corpo do texto editando os valores **Padding Top**, **Padding Right**, **Padding Bottom** e **Padding Left**. Isso se aplicará ao espaçamento em todas as quatro áreas ao redor do bloco de parágrafos.

\![Configurações de estilo de parágrafo para texto com fonte 14pt.]({% image_buster /assets/img_archive/dnd_paragraph_styling.png %})

## Estilo de lista

Ao adicionar listas às suas mensagens, a seção **List Styling (Estilo de lista** ) cria consistência na forma como as listas são estilizadas. Isso inclui detalhes como: 

- Tamanho da fonte
- Cor da fonte
- Peso da fonte
- Altura da linha
- Alinhamento
- Direção do texto
- Espaçamento entre letras
- Espaçamento entre itens da lista
- Recuo do item da lista
- Tipo de lista
- Tipo de estilo de lista

Você pode definir o **tipo de lista** como numerado ou com marcadores. O **tipo de estilo de lista** oferece personalização adicional para o estilo de suas listas. Por exemplo, você pode definir que os tipos de lista sejam sempre com marcadores e que cada marcador seja um quadrado.  

\![Configurações de estilo de lista para uma lista com marcadores.]({% image_buster /assets/img_archive/dnd_list_styling.png %})

## Estilo do botão

Na seção **Button Styling (Estilo do botão** ), é possível editar os seguintes estilos padrão para o botão:
- Cor de fundo
- Tamanho da fonte
- Cor da fonte
- Raio da borda
- Cor da borda
- Peso da borda
- Preenchimento de botões

\![Configurações de estilo de botão para um botão retangular com fundo azul.]({% image_buster /assets/img_archive/dnd_button_styling.png %})

Como em todas as outras seções de estilo, é possível ajustar o estilo do bloco editando os valores de **Padding Top**, **Padding Right**, **Padding Bottom** e **Padding Left**.

## Largura do modelo de e-mail

Usando a largura do modelo de e-mail, você pode ajustar e definir uma largura para manter a consistência em suas campanhas de e-mail. 

\![Largura do modelo de e-mail definida como 600px.]({% image_buster /assets/img_archive/dnd_email_template_width.png %})

## Largura do bloco de conteúdo

Essa configuração será a pré-configurada para todos os blocos de conteúdo futuros. Os blocos de conteúdo existentes não serão atualizados. Você pode definir que todos os blocos de conteúdo sejam definidos como 100%, respeitando a largura em que um bloco de conteúdo é inserido, ou definir um valor de pixel específico.

Recomendamos combinar a largura do Content Block com a largura do modelo de e-mail.

\![Largura do bloco de conteúdo definida como 600px.]({% image_buster /assets/img_archive/dnd_content_block_width_update.png %})
