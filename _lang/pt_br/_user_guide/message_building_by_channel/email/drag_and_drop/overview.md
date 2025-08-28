---
nav_title: Criação de um e-mail
article_title: Criação de um e-mail com o recurso arrastar e soltar
alias: "/dnd/overview/"
channel: email
page_order: 0
description: "Este artigo aborda como configurar e usar corretamente o editor de arrastar e soltar para mensagens de e-mail."
tool:
- Campaigns
- Canvas
---

# Criação de um e-mail com o recurso de arrastar e soltar

> Usando o editor de arrastar e soltar, você pode criar mensagens de e-mail totalmente personalizadas para campanhas ou Canvas, tudo sem usar HTML para criar o corpo do e-mail.

## Sobre o editor

O editor de arrastar e soltar usa [Content](#content) e [Rows](#rows) como os dois principais componentes para simplificar seu fluxo de trabalho, sem uso adicional de HTML.

<table style="width: 100%; table-layout: fixed;">
    <tr>
        <th style="width: 50%;">Conteúdo</th>
        <th style="width: 50%;">Linhas</th>
    </tr>
    <tr>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_content.png %}" alt="A guia &quot;Rows&quot; (Linhas) que inclui diferentes combinações estruturais para o layout de seu e-mail." style="max-width: 100%; height: auto;">
        </td>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_rows.png %}" alt="A guia &quot;Content&quot; (Conteúdo), que inclui blocos básicos, mídia e avançados" style="max-width: 100%; height: auto;">
        </td>
    </tr>
</table>
{: .reset-td-br-1 role="presentation"}

### Conteúdo

**O conteúdo** inclui uma série de blocos que representam diferentes tipos de conteúdo que podem ser usados em sua mensagem. Elas são organizadas em três categorias: básica, mídia e avançada. 

{% tabs %}
{% tab Básico %}

Os blocos básicos são a base de seu e-mail. Usando esses blocos, você pode adicionar qualquer um dos seguintes elementos ao corpo do e-mail:

- Título
- Parágrafo
- Lista
- Botão
- Divisor
- Espaçador

{% endtab %}
{% tab Mídia %}

Com os blocos de conteúdo, é possível adicionar diferentes conteúdos visuais, como imagens, vídeos, ícones e links de redes sociais e ícones personalizáveis.

{% endtab %}
{% tab Avançado %}

Embora o editor de arrastar e soltar simplifique seu fluxo de trabalho com esses blocos, também é possível usar blocos avançados para inserir HTML ou adicionar um menu ao corpo do e-mail. Observe que o uso de seu próprio HTML pode afetar a forma como a mensagem é renderizada.

{% endtab %}
{% endtabs %}

### Linhas

**As linhas** são unidades estruturais que definem a composição horizontal de uma seção da mensagem por meio de colunas. Você pode esvaziar as linhas ou [os blocos de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/). O uso de mais de uma coluna permite que você coloque diferentes elementos de conteúdo lado a lado. Dessa forma, você pode adicionar todos os elementos estruturais necessários à sua mensagem, independentemente do modelo selecionado no início.

#### Estilo dos cartões

**O estilo dos cartões** é uma propriedade de linha que permite adicionar espaçamento entre as colunas e arredondar seus cantos. Com a formatação em estilo de cartão, é possível criar layouts com maior engajamento visual para ajudar a destacar seu conteúdo mais importante, como novos recursos de produtos, depoimentos, ofertas especiais, atualizações de notícias e muito mais.

## Usando o editor de arrastar e soltar

Não tem certeza se sua mensagem de e-mail deve ser enviada usando uma campanha ou um Canva? As campanhas são melhores para campanhas de mensagens únicas e simples, enquanto as canvas são melhores para jornadas de usuários em várias etapas.

Depois de selecionar onde construir sua mensagem, vamos nos aprofundar nas etapas para criar um e-mail do tipo arrastar e soltar.

### Etapa 1: Selecione seu modelo

Depois de selecionar o editor de arrastar e soltar como sua experiência de edição, você pode optar por:

- Comece com um modelo em branco.
- Use um modelo de e-mail pré-desenhado do Braze para arrastar e soltar.
- Use um modelo de e-mail salvo do tipo arrastar e soltar.

{% alert note %}
Para usar um modelo de HTML personalizado existente ou modelos criados por terceiros, você deve recriar o modelo acessando **Modelos** > **Modelos de e-mail** e selecionando **Editor de arrastar e soltar** como sua experiência de edição.
{% endalert %}

Também é possível acessar todos os modelos na seção **Modelos**.

Depois de selecionar o modelo, você verá uma visão geral do e-mail em **Variantes de e-mail**, que inclui as informações de envio e o corpo do e-mail. 

Em seguida, selecione **Edit Email Body (Editar corpo do e-mail)** para começar a projetar a estrutura do e-mail no editor de arrastar e soltar. 

![A seção "Variantes de e-mail" com um exemplo de corpo de e-mail.]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### Etapa 2: Crie seu e-mail

A experiência de edição de arrastar e soltar é dividida em três seções: **Configurações de envio**, **Conteúdo** e **Prévia e teste**. A mágica de criar o corpo do e-mail acontece na seção **Conteúdo**. Antes de criar seu e-mail, é importante entender os principais componentes que orientam sua experiência de criação de e-mail. Se você precisar revisar, consulte [Sobre o editor](#about-the-editor).

Quando estiver pronto, use os blocos de conteúdo do tipo arrastar e soltar para criar seu e-mail.

1. Selecione o painel **Rows**. Arraste e solte as configurações de linha no editor principal. Isso mapeará o layout do conteúdo de seu e-mail.
- Note que as novas configurações devem ser arrastadas para a parte superior ou inferior de uma seção existente.
- Quando você seleciona uma configuração de linha, as configurações de **Propriedades da linha** são exibidas para personalização adicional das cores de fundo da linha, imagens e tamanhos de coluna personalizados.
2. Selecione o painel **Content (Conteúdo** ). Arraste e solte os blocos de conteúdo desejados nos componentes da linha.
- Você também pode arrastar qualquer um dos blocos de **conteúdo** para o editor principal. Isso cria uma linha para o bloco.
- Você pode refinar ainda mais o bloco selecionando-o e ajustando os campos em **Propriedades do conteúdo** e **Opções do bloco**. Isso inclui a edição do espaçamento entre letras, preenchimento, altura da linha e muito mais.

Consulte [Outras personalizações](#other-customizations) para ver outras maneiras de personalizar ainda mais seu e-mail de arrastar e soltar.

Ao criar seu e-mail, é possível alternar entre a visualização para desktop e para dispositivos móveis para fazer uma prévia de como será o envio de mensagens por e-mail para seus grupos de usuários. Isso verificará se o seu conteúdo é responsivo e você poderá fazer os ajustes necessários ao longo do processo.

{% alert tip %}
Precisa de ajuda para criar um texto incrível? Tente usar o [Assistente de Copywriting da IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Insira o nome ou a descrição de um produto, e a IA gerará uma cópia de marketing semelhante à humana para uso em seu envio de mensagens.

![Botão Copywriter, localizado no painel Content (Conteúdo) ao lado de Style Settings (Configurações de estilo) no editor de arrastar e soltar.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### Etapa 3: Adicione suas informações de envio

Depois de terminar de projetar e criar sua mensagem de e-mail, é hora de adicionar as informações de envio na seção **Configurações de envio**.

1. Em **Informações de envio**, selecione um e-mail como **Nome de exibição + Endereço de origem**. Você também pode personalizar isso selecionando **Personalizar a partir do nome de exibição + endereço**.
2. Selecione um e-mail como **endereço de resposta**. Você também pode personalizar essa opção selecionando **Personalizar endereço de resposta**.
3. Em seguida, selecione um e-mail como **endereço BCC** para tornar seu e-mail visível para esse endereço.
4. Adicione uma linha de assunto ao seu e-mail. Opcionalmente, você também pode adicionar um pré-cabeçalho e um espaço em branco após o pré-cabeçalho.

Uma prévia no painel direito será preenchida com as informações de envio que você adicionou. Essas informações também podem ser atualizadas em **Configurações** > **Preferências de e-mail** > **Configuração de envio de e-mail**.

#### Personalização do cabeçalho de seu e-mail (avançado)

Em **Configurações de envio**, é possível adicionar personalização para cabeçalhos de e-mail e extras de e-mail, o que permite enviar dados adicionais de volta a outros prestadores de serviço de e-mail. A personalização de um cabeçalho de e-mail, como a inclusão do nome do destinatário, também pode contribuir para a probabilidade de seu e-mail ser aberto.

{% alert note %}
A funcionalidade avançada aparecerá no criador da campanha ou do Canva. Na funcionalidade avançada, você pode modificar sua configuração de CSS em linha e inserir um cabeçalho ou pares de valores-chave adicionais (se configurados).
{% endalert %}

### Etapa 4: Teste seu e-mail

Depois de adicionar suas informações de envio, é hora de finalmente testar seu e-mail. 

Acesse a seção **Pré-visualização e teste**. Aqui, você tem a opção de fazer uma prévia do seu e-mail como usuário ou enviar uma mensagem de teste. Essa seção também inclui o [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/), que permite verificar se o seu e-mail foi renderizado corretamente em diferentes clientes móveis e da Web.

{% alert tip %}
Você também pode usar o botão de alternância de **visualização do modo escuro** no painel de prévia para visualizar o corpo do e-mail no modo escuro e ajustar o e-mail conforme necessário.
{% endalert %}

Como você pode visualizar três versões diferentes do mesmo e-mail no editor real, no Inbox Vision e como um e-mail de teste real, é importante alinhar os detalhes em todas as suas plataformas.

#### Pré-visualização e teste de envio
 
Na guia **Preview as a User (Visualizar como usuário** ), é possível selecionar os seguintes tipos de usuários para a prévia da mensagem.

- **Usuário aleatório:** O Braze selecionará aleatoriamente um usuário do banco de dados e fará a prévia do e-mail com base em suas atribuições ou informações do evento.
- **Selecione Usuário:** É possível selecionar um usuário específico com base em seu endereço de e-mail ou ID externo. O e-mail será pré-visualizado com base nas atribuições do usuário e nas informações do evento
- **Usuário personalizado:** Você pode personalizar um usuário. O Braze oferecerá entradas para todas as atribuições e eventos disponíveis. Você pode inserir qualquer informação que gostaria de ver no e-mail de prévia.

{% alert note %}
O usuário aleatório pode ou não fazer parte dos seus critérios de segmentação. A segmentação é selecionada posteriormente, portanto o Braze não tem conhecimento de seu público-alvo nesse momento.
{% endalert %}

Também é possível selecionar **Copiar link de visualização** para gerar e copiar um link de visualização compartilhável que mostre como será o e-mail para um usuário aleatório. O link terá duração de sete dias antes de precisar ser regenerado. 

Observe que as edições feitas em um modelo de e-mail não se refletirão em um link gerado anteriormente. Você precisará gerar uma nova prévia do link para ver as edições.

![Envio de e-mail com um botão para "Copiar link da prévia" e copiar o link gerado.]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### Use o Inbox Vision

O Inbox Vision permite que você visualize suas campanhas de e-mail a partir da perspectiva de clientes de e-mail e dispositivos móveis. Para testar sua mensagem de e-mail usando o Inbox Vision, selecione **Inbox Vision** na seção **Preview & Test** e selecione **Run Inbox Vision**.

{% alert tip %}
As imagens de fundo em envios de mensagens por e-mail podem, às vezes, causar linhas brancas ou desconexões entre as imagens, por isso é importante testar e verificar os detalhes da sua mensagem de e-mail.
{% endalert %}

Depois de usar o editor de arrastar e soltar para projetar e criar sua mensagem de e-mail, continue a [criar]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas) o restante de sua campanha ou Canvas.

{% details Sobre o mecanismo HTML atualizado %}
O mecanismo subjacente que produz HTML a partir do editor de arrastar e soltar foi otimizado e atualizado, resultando em benefícios relacionados à compactação e à renderização de arquivos HTML.

Nosso tamanho médio de pegada de dados HTML exportados foi reduzido, levando a um carregamento e renderização mais rápidos, redução do recorte móvel e redução do consumo de largura de banda.

A renderização de HTML foi aprimorada com base nas seguintes atualizações que minimizam o número de comentários condicionais e consultas de mídia CSS. Como resultado, os arquivos HTML são menores e codificados com mais eficiência.
- Migração de um design baseado em elementos do site `<div>` para uma base de código formatada padrão do site `<table>` 
- [Os blocos do editor]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) foram recodificados para maior concisão
- O código HTML final é compactado para remover os espaços em branco entre as tags
- Divisores transparentes são automaticamente convertidos em preenchimento de conteúdo
{% enddetails %}

## Outras personalizações

À medida que continuar criando e-mails do tipo arrastar e soltar, você poderá personalizar ainda mais o corpo de cada e-mail usando uma combinação desses detalhes criativos para capturar a atenção e o interesse do público em sua mensagem.

{% alert tip %}
Você pode criar um tema personalizado para o editor de arrastar e soltar usando [as configurações de estilo global]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/).
{% endalert %}

### Imagens com largura automática

As imagens adicionadas ao seu e-mail serão automaticamente definidas como **largura automática**. Para ajustar essa configuração, desative a opção **Largura automática** e ajuste a porcentagem de largura conforme necessário.

![Opção de largura automática na guia Conteúdo do editor de arrastar e soltar.]({% image_buster /assets/img/dnd/dnd1.png %})

### Camadas de cores

Usando camadas de cores, você pode alterar a cor do plano de fundo do e-mail, da área de conteúdo e de diferentes componentes de conteúdo. A ordem de cores da frente para trás é: cor do componente de conteúdo, cor de fundo da área de conteúdo e cor de fundo.

![Exemplo de camadas de cores no editor de arrastar e soltar.]({% image_buster /assets/img/dnd/dnd2.png %})

### Preenchimento de conteúdo

![Opções de bloco para o editor de arrastar e soltar.]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Para ajustar o preenchimento, role para baixo até **Block Options (Opções de bloco** ) e selecione **More Options (Mais opções**). É possível ajustar o preenchimento para que o e-mail tenha a aparência ideal.

### Histórico do conteúdo

É possível adicionar uma imagem de fundo à configuração da linha, o que permite incorporar mais design e conteúdo visual à sua campanha de e-mail.

### Adicionar personalização

![Opções para adicionar personalização ao editor de arrastar e soltar.]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

O Liquid básico é compatível com o editor de arrastar e soltar de e-mails. Para adicionar personalização ao seu e-mail:

1. Selecione **Personalização** na seção **Conteúdo**. 
2. Selecione o tipo de personalização. Isso inclui atributos padrão (standard), atributos de dispositivo, atributos personalizados e muito mais. 
3. Pesquise a atribuição a ser adicionada.
4. Copie o snippet do Liquid gerado e cole-o no corpo do e-mail.

A personalização Liquid não é compatível com blocos de imagens e campos do tipo link de botão. 

#### Imagens dinâmicas

Você pode optar por incluir imagens dinâmicas em seu envio de mensagens por e-mail, incluindo Liquid no atributo de origem da imagem. Por exemplo, em vez de uma imagem estática, é possível inserir {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} como URL da imagem para incluir o nome de um usuário na imagem. Isso ajuda a personalizar seus e-mails para cada usuário.

### Alterar a direção do texto

Ao ser o criador da mensagem, você pode alternar a direção do texto entre a esquerda para a direita e a direita para a esquerda selecionando o respectivo botão **Direção do texto**. Você pode usar essa opção ao criar mensagens em idiomas como árabe e hebraico.

![Menu do editor de arrastar e soltar de e-mail com botão para alternar o alinhamento do texto entre direita para esquerda e esquerda para direita.]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

A aparência final das mensagens da direita para a esquerda depende muito de como os prestadores de serviço as processam. Para obter práticas recomendadas sobre o envio de mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

### Adicionar atribuições HTML a links

![A seção "Attributes" com o atributo "clicktracking" desativado para um link.]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Ao usar links, botões, imagens e vídeos no editor de arrastar e soltar, selecione **Adicionar novo atributo** em **Atributos** na seção **Conteúdo** para anexar informações adicionais às tags de HTML nos e-mails. Isso pode ser especialmente útil para personalização, segmentação e estilização de mensagens.

Um caso de uso comum é inserir uma atribuição em sua tag âncora para desativar o rastreamento de cliques ao enviar pelo Braze.

* **SendGrid:** `clicktracking = "off"`
* **SparkPost:** `data-msys-clicktrack = "0"`

Outro caso de uso comum é sinalizar links específicos como links universais. Os links universais são links que redirecionam para o seu app, proporcionando aos seus usuários uma experiência integrada.

* **SendGrid:** `universal = "true"`
* **SparkPost:** `data-msys-sublink = "open-in-app"` (uma [subcamada personalizada](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths) deve ser configurada)

Para configurar links universais, consulte [Links universais e links de apps]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).

Como alternativa, você pode fazer a integração com um de nossos parceiros de atribuição, como a [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) ou [a AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/#email-deep-linking-and-click-tracking), para gerenciar links universais.

Por fim, estão disponíveis atribuições predefinidas para ajudar a tornar sua mensagem acessível. Saiba mais em nosso artigo dedicado [Building accessible messages in Braze]({{site.baseurl}}/help/accessibility).

### Definição de um idioma para envio de e-mail

Você pode definir a atribuição do idioma acessando a guia **Configurações** e selecionando o idioma desejado. Também é possível direcionar a atribuição do usuário {%raw%} `{{${language}}}` {%endraw%} se a mensagem for destinada a usuários com valores de idioma dinâmicos.

![Configuração do valor "Language" (Idioma) para um e-mail.]({% image_buster /assets/img/dnd/language_setting_dnd.png %})

