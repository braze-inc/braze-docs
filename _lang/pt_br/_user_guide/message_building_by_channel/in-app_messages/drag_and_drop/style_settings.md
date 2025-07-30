---
nav_title: Configurações de estilo
article_title: "Configurações de estilo de mensagem no app"
description: "Este artigo de referência aborda as opções de estilo disponíveis ao criar uma mensagem no app com o editor de arrastar e soltar."
page_order: 3
---

# Configurações de estilo de mensagem no app

> A experiência de edição de arrastar e soltar é dividida em duas seções: **Compilação** e **Pré-visualização e Teste**. Este artigo aborda o que você precisa saber para trabalhar na guia **Build** do editor e pressupõe que você já tenha [criado uma mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/).

![Guia "Estilos de mensagens".]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

## Estilos em nível de mensagens

É possível definir determinados estilos a serem aplicados em todos os blocos relevantes da mensagem no app na guia **Estilos de mensagem**. Por exemplo, talvez você queira personalizar a fonte de todo o texto ou a cor de todos os links da sua mensagem.

Os estilos desta seção são usados em toda a mensagem, exceto quando são substituídos por um bloco específico. Se a sua mensagem tiver [várias páginas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page), você também poderá substituir os estilos no nível da mensagem para páginas individuais, exceto para o tipo de exibição e a largura máxima. Se você tentar aplicar os estilos de nível de página e de nível de mensagem, o estilo de nível de página substituirá o estilo de nível de mensagem.

Para facilitar a experiência de design, recomendamos configurar os estilos no nível da mensagem antes de personalizar os estilos no nível do bloco.

Para retornar à guia **Message Styles (Estilos de mensagens** ) a qualquer momento:

- Clique no botão X de fechar nas propriedades individuais do bloco
- Selecione o contêiner da mensagem, o botão X de fechamento da mensagem ou o plano de fundo do editor

### Fontes personalizadas

Aceitamos os seguintes tipos de arquivos para fontes: `.ttf`, `.woff`, `.otf`, e `.woff2`. Para saber mais, consulte [Arquivos de ativos]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages#asset-files).

Você pode adicionar várias variações de uma família de fontes, pois algumas opções de estilo podem não estar disponíveis para fontes personalizadas. Atualmente, não oferecemos suporte à adição de fontes via URL.

Para adicionar uma fonte personalizada:

1. Acesse a seção **Content (Conteúdo** ) na guia **Message styles (Estilos de mensagens** ).
2. Clique em **Adicionar fonte personalizada**.
3. Faça upload de sua fonte usando a biblioteca de mídia. 

{% alert note %}
A fonte em nível de mensagem será aplicada somente à mensagem atual e a quaisquer mensagens duplicadas, mas não a modelos futuros.
{% endalert %}

## Componentes de mensagens

![Um GIF mostrando uma mensagem promocional no app sendo criada.]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

O editor de arrastar e soltar usa dois componentes principais para criar mensagens no app: **linhas** e **blocos**. Todos os blocos devem ser colocados em uma fileira.

### Linhas

As linhas são unidades estruturais que definem a composição horizontal de uma seção da mensagem usando células.

![Linhas que você pode adicionar em sua mensagem no app.]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

Quando uma linha é selecionada, é possível adicionar ou remover o número de colunas necessárias na seção **Personalização de colunas** para colocar diferentes elementos de conteúdo lado a lado. 

Você também pode deslizar para ajustar o tamanho das colunas existentes.

![Ajuste de colunas da seção "Personalização de colunas".]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

Como prática recomendada, formate suas propriedades de linha e coluna antes de formatar qualquer bloco dentro das linhas. Há muitos lugares onde você pode ajustar o espaçamento e o alinhamento, portanto, começar pela base facilita a edição à medida que você avança.

### Blocos

Os blocos representam diferentes tipos de conteúdo que podem ser usados em sua mensagem. Arraste uma dentro de um segmento de linha existente e ela se ajustará automaticamente à largura da célula.

{% alert tip %}
Antes de adicionar blocos, configure [estilos no nível da mensagem](#set-message-level-styles) para o contêiner da mensagem, a fonte, as cores e qualquer outra coisa que queira personalizar. Em seguida, você pode personalizar blocos individuais conforme necessário. O **botão Fechar** permanecerá na seção superior da sua mensagem para que os usuários sempre tenham a opção de dispensar a mensagem.
{% endalert %}

![Arraste e solte caixas para selecionar.]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

Cada bloco tem suas configurações, como o controle granular do preenchimento. O painel do lado direito muda automaticamente para um painel de estilo para o elemento de conteúdo selecionado. Para saber mais, consulte [Propriedades do bloco do editor]({{site.baseurl}}/editor_blocks_dnd_iam/).

Ao criar sua mensagem no app, você pode selecionar uma visualização para celular, tablet ou desktop na barra de ferramentas para fazer uma prévia de como sua mensagem no app será exibida para seus grupos de usuários. Isso garantirá que seu conteúdo seja responsivo e que você possa fazer os ajustes necessários ao longo do processo.

#### Texto do intervalo

{% multi_lang_include span_text.md %}

## Detalhes criativos

### Tela cheia em telas maiores {#fullscreen}

Em um tablet ou navegador de desktop, uma mensagem no app em tela cheia ficará no centro da tela do aplicativo. Quaisquer edições na largura máxima da mensagem em tela cheia só se aplicarão a dispositivos tablet e desktop. 

![Exemplo de mensagem no app em tela inteira.]({% image_buster /assets/img_archive/dnd_iam_fullscreen_example.png %}){: style="border:none"}

### Adição de uma imagem de fundo

Você pode adicionar uma imagem ao plano de fundo de sua mensagem na guia **Estilos de mensagem**. 

1. Na área da tela, selecione o contêiner de plano de fundo. Esta é a seção de rolagem da sua mensagem.
2. Na guia **Estilos de mensagens**, ative **Imagem de fundo**.
3. Adicione uma imagem da sua biblioteca de mídia ou insira o URL onde a imagem está hospedada.

{% alert tip %}
Se estiver tendo problemas para selecionar um determinado bloco, você pode usar a seta para cima na barra de ferramentas em linha do bloco para mover o foco para cada bloco pai.
{% endalert %}

### Adição de Liquid

![Ícone para adicionar personalização Liquid.]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

Para adicionar [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) à sua mensagem no app, selecione <i class="fa-solid fa-circle-plus"></i> **Add Personalization** na barra de ferramentas do editor. Aqui, você pode adicionar vários tipos de personalização, como atributos padrão, atributos de dispositivo, atributos personalizados e muito mais.

Em seguida, pegue o snippet do Liquid gerado e insira-o em sua mensagem. Depois de projetar e criar sua mensagem no app, acesse **Preview & Test (Visualizar e testar** ) para fazer a prévia da mensagem.

### Usando o copywriter de IA

Quando um bloco de texto for selecionado em sua mensagem no app, clique em <i class="fa-solid fa-wand-magic-sparkles" title="Redator IA"></i> na barra de ferramentas do bloco para iniciar o [assistente de Copywriting com IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). O Assistente de Copywriting de IA passa um breve nome ou descrição do produto para a ferramenta de geração de cópia GPT3 da OpenAI para gerar uma cópia de marketing semelhante à humana para seu envio de mensagens.

{% alert tip %}
Você pode economizar alguns cliques destacando o texto dentro do bloco antes de clicar no ícone. O texto destacado será adicionado à ferramenta, e uma cópia será gerada imediatamente.
{% endalert %}

![GIF do redator de IA.]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### Redefinição de estilos para o padrão

As propriedades que você alterou em relação ao estilo padrão são marcadas com um ponto laranja. Para redefinir uma propriedade específica para seu estilo padrão, passe o mouse sobre o campo e selecione **Redefinir para o padrão**.

![Ponto laranja que redefine o tamanho do texto para seu tamanho padrão.]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

Você também pode redefinir todos os estilos de um elemento selecionado selecionando o botão <i class="fas fa-paintbrush" title="Botão Copiar ou colar estilos"></i> ao lado do nome do painel de propriedades e selecionando **Redefinir para os estilos padrão**.

### Copiar e colar estilos

Depois de fazer alterações no estilo de um elemento, você pode copiar e colar esses estilos em outro elemento. Ao colar estilos, somente as propriedades relevantes para esse elemento são aplicadas.

![Menu suspenso com opção de copiar estilos.]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. Com o elemento selecionado, selecione <i class="fas fa-paintbrush" title="Copiar ou colar estilos"></i> ao lado do nome do painel de propriedades (por exemplo, se você tiver um botão selecionado, ao lado de "Propriedades do botão").
2. Clique em **Copiar estilos** e selecione o elemento ao qual você deseja aplicar o estilo copiado.
3. Selecionar <i class="fas fa-paintbrush" title="Copiar ou colar estilos"></i> novamente e selecione **Colar estilos**.

#### Atalhos de teclado

Você também pode usar atalhos de teclado para copiar e colar estilos:

| Ação       | Mac                                            | Windows                                           |
| ------------ | ---------------------------------------------- | ------------------------------------------------- |
| Copiar estilos  | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> |
| Colar estilos | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
