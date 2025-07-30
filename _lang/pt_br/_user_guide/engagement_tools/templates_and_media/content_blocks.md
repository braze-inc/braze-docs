---
nav_title: Biblioteca de blocos de conteúdo
article_title: Biblioteca de blocos de conteúdo
page_order: 1
page_type: reference
description: "Este artigo de referência explica como usar a Biblioteca de Blocos de Conteúdo para gerenciar seu conteúdo reutilizável e entre canais em um único local centralizado."
tool: 
  - Templates
  - Media

---

# Biblioteca de blocos de conteúdo

> A Biblioteca de Blocos de Conteúdo permite gerenciar seu conteúdo reutilizável e entre canais em um único local centralizado.

Com os blocos de conteúdo, você pode:

- Crie uma aparência consistente para suas campanhas de e-mail usando-os como cabeçalhos e rodapés.
- Distribua os mesmos códigos de oferta em diferentes canais.
- Crie ativos predefinidos que podem ser usados para criar mensagens com informações e ativos consistentes.
- Copiar corpos inteiros de mensagens para outras mensagens.

## Criar um bloco de conteúdo

Há dois tipos de editores usados para criar um bloco de conteúdo: o clássico e o de arrastar e soltar. Esses dois tipos de editores correspondem ao tipo de bloco de conteúdo: HTML e arrastar e soltar. Você também pode criar e gerenciar seus blocos de conteúdo [usando a API]({{site.baseurl}}/api/endpoints/templates/).

{% tabs %}
{% tab Arrastar e soltar %}

{% multi_lang_include create_content_block.md local="dnd" %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include create_content_block.md local="html" %}

{% endtab %}
{% endtabs %}

### Especificações do bloco de conteúdo

| Atributo do bloco de conteúdo | Especificações |
|---|---|
| Nome | Campo obrigatório com um máximo de 100 caracteres. Ele não pode ser renomeado depois que o bloco de conteúdo tiver sido salvo. Além disso, você não pode nomear um novo bloco de conteúdo com o mesmo nome de um bloco de conteúdo anterior, mesmo que o anterior tenha sido arquivado. |
| Descrição | (opcional) Máximo de 250 caracteres. Descreva o bloco de conteúdo para que outros usuários do Braze saibam para que serve e onde é usado. |
| Tamanho do conteúdo | Máximo de 50 KB. |
| Posicionamento | Os blocos de conteúdo não podem ser usados em um rodapé de e-mail. |
| Criação | Editor de HTML ou editor de arrastar e soltar. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Ao criar blocos de conteúdo, pode ser útil visualizar o HTML e o Liquid adicionando quebras de linha. Se essas quebras de linha forem deixadas durante o envio, você corre o risco de ter espaços estranhos que podem afetar a forma como o bloco será renderizado. Para evitar isso, use a tag **Capture** em seu bloco junto com o filtro **| strip**.
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Uso de blocos de conteúdo

Depois de criar seu bloco de conteúdo, você pode inseri-lo em suas mensagens seguindo estas etapas: 

1. Copie a **Liquid Tag** do **bloco de conteúdo** da seção **Detalhes do bloco de conteúdo** ).
2. Insira a tag Content Block Liquid na mensagem. Você também pode começar a digitar o Liquid e fazer com que a tag seja preenchida automaticamente.

### Coisas para saber

- O uso de blocos de conteúdo HTML em e-mails de arrastar e soltar **ou** de blocos de conteúdo de arrastar e soltar em e-mails HTML pode resultar em problemas inesperados de renderização. Isso ocorre porque o editor de arrastar e soltar gera HTML e CSS que renderizam dinamicamente o conteúdo, enquanto o editor de HTML é mais estático.
- As propriedades do evento Canvas só são compatíveis com um Canvas. Se você fizer referência a um bloco de conteúdo com propriedades de entrada de tela em uma campanha, ele não será preenchido.

### Atualização e cópia de blocos de conteúdo

Se você optar por atualizar um bloco de conteúdo, ele será atualizado em todas as mensagens em que o bloco de conteúdo for usado se for inserido via Liquid. Se o bloco de conteúdo for importado usando o menu suspenso **Blocos de conteúdo** em **Linhas** no editor de arrastar e soltar, ele não será atualizado em todas as mensagens.

Se quiser atualizar um bloco de conteúdo para uma única mensagem ou fazer uma cópia para usar em outras mensagens, é possível copiar o HTML da mensagem original para a nova mensagem ou editar o bloco de conteúdo original (ele já deve ter sido usado em uma mensagem) e salvá-lo. Você receberá um aviso que permitirá salvá-lo como um novo bloco de conteúdo.

Depois de fazer edições em um bloco de conteúdo, você pode salvar e iniciar o bloco de conteúdo atualizado selecionando **Lançar bloco de conteúdo**. Ou, você pode selecionar **Mais** > **Duplicar**para criar uma duplicata do seu bloco de conteúdo.

![Um bloco de conteúdo que diz "Welcome to our newsletter" (Bem-vindo ao nosso boletim informativo).]({% image_buster /assets/img/copy-content-block.png %})

Você também pode [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) um bloco de conteúdo. Isso cria uma cópia de rascunho do bloco de conteúdo.

### Pré-visualização de blocos de conteúdo

Depois de adicionar um bloco de conteúdo em uma campanha ou canvas ativo, é possível fazer uma prévia desse bloco de conteúdo na biblioteca de blocos de conteúdo passando o mouse sobre o bloco de conteúdo e selecionando o ícone <i class="fa fa-eye preview-icon"></i> **Preview**. 

Essa prévia inclui informações sobre o bloco de conteúdo, como quem o criou, tags, data de criação, data da última edição, descrição, tipo de editor, contagem de inclusão com detalhes e uma prévia real do bloco de conteúdo.

![Uma prévia de um bloco de conteúdo "Workout_Promo" para ciclismo e dança que tem seis inclusões.]({% image_buster /assets/img/preview_tab_content_block.png %}){: style="max-width:60%;"} 

### Aninhamento de blocos de conteúdo

Os blocos de conteúdo podem ser aninhados, mas apenas uma vez. Você pode aninhar o Bloco de conteúdo A no Bloco de conteúdo B, mas não poderá aninhar o Bloco de conteúdo B no Bloco de conteúdo C.

{% alert warning %}
Nada impedirá você de aninhar um terceiro nível de bloco de conteúdo, mas você não verá a expansão do conteúdo em aninhamentos além do segundo. O conteúdo e o snippet Liquid são removidos da mensagem.
{% endalert %}

Além disso, os blocos de conteúdo não podem ser usados em um rodapé de e-mail, embora os rodapés de e-mail possam ser usados em blocos de conteúdo.

### Arquivamento de blocos de conteúdo

![Menu suspenso Configurações expandido que mostra três opções: Arquivar, Duplicar e Copiar para o espaço de trabalho.]({% image_buster /assets/img/template_archive_cog.png %}){: style="max-width:20%;float:right;margin-left:15px;" }

Quando terminar de usar um bloco de conteúdo, você poderá arquivá-lo na página [Modelos e mídias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/). Os blocos de conteúdo arquivados são somente leitura, portanto, desarquive o bloco de conteúdo antes de editá-lo. Os blocos de conteúdo não podem ser arquivados se forem usados em alguma mensagem.

#### Melhores práticas

- Quando seu bloco for usado apenas em alguns e-mails, recomendamos arquivar o bloco desatualizado e atualizar suas mensagens ao vivo com um bloco mais recente que não tenha sido arquivado.
- Quando seu bloco tiver apenas um erro de digitação ou precisar de uma pequena alteração, não recomendamos arquivar o bloco. Em vez disso, atualize o bloco e comece a enviar!
- Quando seu bloco for usado em mais mensagens do que você pode gerenciar razoavelmente com a primeira sugestão desta lista, recomendamos remover todo o conteúdo do bloco e arquivá-lo. Isso garantirá que nenhuma informação desatualizada seja incluída em qualquer e-mail recém-enviado.
- Se você arquivar acidentalmente um bloco de conteúdo, poderá desarquivá-lo.

![Painel Blocos de conteúdo salvos em que o menu suspenso de configurações para "Test_32" é expandido para mostrar três opções: Desarquivar, duplicar e copiar para o espaço de trabalho]({% image_buster /assets/img/unarchive-content-block.png %})

