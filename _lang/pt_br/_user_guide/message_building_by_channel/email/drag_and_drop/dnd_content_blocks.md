---
nav_title: Blocos de conteúdo
article_title: Blocos de conteúdo do editor de arrastar e soltar
alias: "/dnd/content_blocks/"
channel: email
page_order: 2
description: "Este artigo de referência aborda como criar e usar blocos de conteúdo no editor de arrastar e soltar."
tool: Media

---

# Blocos de conteúdo do editor de arrastar e soltar

> Os blocos de conteúdo usados exclusivamente no editor de arrastar e soltar são semelhantes em funcionalidade aos [blocos de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) usados em diferentes canais. Eles são um local centralizado para armazenar informações que podem ser consultadas em várias campanhas de e-mail. Isso pode incluir o agrupamento de cabeçalhos de e-mail, chamadas promocionais e muito mais, tudo em uma linha reutilizável.

{% alert note %}
Os blocos de conteúdo do tipo arrastar e soltar só estão disponíveis para uso em campanhas de e-mail e mensagens de e-mail no Canvas.
{% endalert %}

## Criação de um bloco de conteúdo

Para criar um Content Block, faça o seguinte:

{% multi_lang_include create_content_block.md location="dnd" %}

{% alert important %}
Cada Content Block de arrastar e soltar é limitado a uma linha. No entanto, você pode usar blocos do editor de arrastar e soltar para criar e personalizar o Content Block de acordo com suas mensagens de e-mail.
{% endalert %}

## Uso de um bloco de conteúdo

Há duas maneiras de adicionar o Content Block ao seu e-mail: usando o editor ou usando o Liquid.

### Usar o editor para adicionar um bloco de conteúdo

Para adicionar um Content Block no editor, faça o seguinte:

1. Vá para a guia **Rows (Linhas)** no editor e selecione **Content Blocks (Blocos de conteúdo**). 
2. Arraste e solte seu bloco de conteúdo no editor de e-mail. 
3. (Opcional) Ajuste a largura de seu Content Block selecionando o botão no menu de navegação. A largura padrão é 100% quando não especificada nas configurações globais de estilo do seu e-mail; caso contrário, as configurações globais serão respeitadas. <br><br>\![Uma seta de dois lados com uma opção para editar a largura.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }<br><br>

Depois de adicionar o Content Block ao editor de e-mail, você pode fazer edições no Content Block que não afetarão o Content Block original que você criou em **Templates & Media**. Isso ocorre porque os blocos de conteúdo adicionados por arrastar e soltar não são vinculados ao bloco de conteúdo original. Para visualizar as alterações feitas no Content Block original, arraste-o novamente para o editor de e-mail. 

O desalinhamento no editor de arrastar e soltar pode ocorrer quando vários blocos de conteúdo são adicionados a um único bloco de linha. Tente usar blocos de linhas separados para manter o alinhamento do conteúdo no nível da linha.

### Uso do Liquid para adicionar um bloco de conteúdo

Para adicionar um Content Block usando o Liquid, faça o seguinte:

1. Vá para sua campanha de e-mail e selecione **Edit Email Body (Editar corpo do e-mail**). 
2. Clique em <i class="fas fa-plus"></i> **Personalization**.
3. Localize a guia **Add Personalization (Adicionar personalização** ) e selecione **Content Blocks (Blocos de conteúdo** ) no menu suspenso **Personalization Type (Tipo de personalização** ).
4. Selecione o nome de seu Content Block no campo **Attribute (Atributo** ). O campo Liquid snippet será preenchido com sua Content Block Liquid Tag. 
5. Copie e cole o snippet do Liquid em um bloco do editor de texto. <br>\![A guia Add Personalization com opções.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

Quando você visualizar a mensagem de e-mail, o snippet do Liquid será exibido como o Content Block do editor de arrastar e soltar. 

{% alert important %}
Quando um bloco de conteúdo é adicionado ao editor de e-mail com o Liquid, esse bloco de conteúdo é vinculado ao bloco de conteúdo original criado em **Templates & Media**. Isso significa que o Content Block será atualizado para refletir quaisquer alterações no modelo original do Content Block.
{% endalert %}

## Atualização de blocos de conteúdo

Para atualizar um Content Block existente, você pode editar o Content Block original na página **Content Blocks** ou copiar o HTML da mensagem original para a nova. As atualizações em um modelo de Content Block serão atualizadas em todas as mensagens de e-mail em que o Content Block for adicionado via Liquid.

Para arquivar um bloco de conteúdo, acesse **Modelos** > **Blocos de conteúdo**, selecione o ícone de reticências verticais <i class="fas fa-ellipsis-vertical"></i> para o bloco de conteúdo e clique em **Arquivar**. Quando você arquivar um Content Block, suas mensagens ainda incluirão o conteúdo do bloco arquivado. No entanto, os blocos de conteúdo arquivados são somente leitura, portanto, desarquive o bloco de conteúdo antes de editá-lo. 

