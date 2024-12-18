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

> Os blocos de conteúdo usados exclusivamente no editor de arrastar e soltar são semelhantes em funcionalidade aos [blocos de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) usados em diferentes canais. Eles são um local centralizado para armazenar informações que podem ser consultadas em várias campanhas de envio de e-mail. Isso pode incluir o agrupamento de cabeçalhos de e-mail, chamadas promocionais e muito mais, tudo em uma linha reutilizável.

{% alert note %}
Os blocos de conteúdo do tipo arrastar e soltar só estão disponíveis para uso em campanhas de e-mail e mensagens de e-mail no Canva.
{% endalert %}

## Criação de um bloco de conteúdo

Para criar um bloco de conteúdo, faça o seguinte:

{% multi_lang_include create_content_block.md local="dnd" %}

{% alert important %}
Cada bloco de conteúdo de arrastar e soltar é limitado a uma linha. No entanto, você pode usar blocos do editor de arrastar e soltar para criar e personalizar o bloco de conteúdo de acordo com seu envio de mensagens por e-mail.
{% endalert %}

## Uso de um bloco de conteúdo

Há duas maneiras de adicionar o bloco de conteúdo ao seu e-mail: usando o editor ou usando o Liquid.

### Usando o editor para adicionar um bloco de conteúdo

Para adicionar um bloco de conteúdo no editor, faça o seguinte:

1. Acesse a guia **Rows (Linhas)** no editor e selecione **Content Blocks (Blocos de conteúdo**). 
2. Arraste e solte seu bloco de conteúdo no editor de e-mail. 

Depois que o bloco de conteúdo for adicionado ao editor de e-mail por meio de arrastar e soltar, você poderá fazer edições no bloco de conteúdo que não afetarão o bloco de conteúdo original criado em **Modelos e mídias.** Isso ocorre porque os blocos de conteúdo adicionados por meio de arrastar e soltar não estão vinculados ao bloco de conteúdo original. Para visualizar as alterações feitas no bloco de conteúdo original, arraste-o para o editor de e-mail novamente. 

O desalinhamento no editor de arrastar e soltar pode ocorrer quando vários blocos de conteúdo são adicionados a um único bloco de linha. Tente usar blocos de linhas separados para manter o alinhamento de seu conteúdo no nível da linha.

### Usando o Liquid para adicionar um bloco de conteúdo

Para adicionar um bloco de conteúdo usando o Liquid, faça o seguinte:

1. Acesse sua campanha de e-mail e selecione **Editar corpo do e-mail**. 
2. Clique em <i class="fas fa-plus"></i> **Personalization**.
3. Localize a guia **Add Personalization (Adicionar personalização** ) e selecione **Content Blocks (Blocos de conteúdo** ) no menu suspenso **Personalization Type (Tipo de personalização** ).
4. Selecione o nome de seu bloco de conteúdo no campo **Atribuição**. O campo Snippet Liquid será preenchido com a Liquid tag do bloco de conteúdo. 
5. Copie e cole o snippet Liquid em um bloco do editor de texto. <br>![A guia Add Personalization com opções.][2]{: style="max-width:30%;"}

Ao fazer a prévia do envio de mensagens por e-mail, o snippet do Liquid será exibido como o bloco de conteúdo do editor de arrastar e soltar. 

{% alert important %}
Quando um bloco de conteúdo é adicionado ao editor de e-mail com o Liquid, esse bloco de conteúdo é vinculado ao bloco de conteúdo original criado em **Modelos e mídias.** Isso significa que o bloco de conteúdo será atualizado para refletir quaisquer alterações no modelo original do bloco de conteúdo.
{% endalert %}

## Atualização de blocos de conteúdo

Para atualizar um Content Block existente, você pode editar o Content Block original na página **Content Blocks** ou copiar o HTML da mensagem original para a nova. As atualizações em um modelo de bloco de conteúdo serão atualizadas em todas as mensagens de e-mail em que o bloco de conteúdo for adicionado via Liquid.

Para arquivar um bloco de conteúdo, acesse **Modelos** > **Blocos de conteúdo**, selecione o ícone de reticências verticais <i class="fas fa-ellipsis-vertical"></i> para o bloco de conteúdo e clique em **Arquivar**. Quando você arquivar um bloco de conteúdo, suas mensagens ainda incluirão o conteúdo do bloco arquivado. No entanto, os blocos de conteúdo arquivados são somente leitura, portanto, desarquive o bloco de conteúdo antes de editá-lo. 

[2]: {% image_buster /assets/img_archive/dnd_content_block_personalization.png %}
