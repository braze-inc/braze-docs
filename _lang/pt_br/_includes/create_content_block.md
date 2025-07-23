1. Acessar **Modelos** > **Blocos de Conteúdo**. Clique em <i class="fas fa-plus"></i> **Criar Bloco de Conteúdo** e selecione **Arrastar e soltar Bloco de Conteúdo**.

{% if include.location == "dnd" %}

{:start="2"}
2\. Arraste e solte os [blocos de editor]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) para construir um bloco de conteúdo arrastável.
3\. Arraste e solte um bloco de formato da guia **Rows** no editor para criar o layout do seu bloco de conteúdo. <br><br> ![]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4\. Adicione blocos de conteúdo de arrastar e soltar conforme necessário para criar suas campanhas de e-mail.
5\. Após criar seu bloco de conteúdo, clique em **Concluído**.
6\. Dê um nome ao seu bloco de conteúdo. Este nome será preenchido automaticamente como parte do **bloco de conteúdo Liquid tag**.
7\. (opcional) Adicione uma descrição.
8\. Clique em **Iniciar bloco de conteúdo**.

{% elsif include.location == "html" %}

{:start="2"}
2\. Insira seu HTML na guia **HTML**, ou construa seu bloco de conteúdo na guia **Classic**. <br><br> ![]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
4\. Após criar seu bloco de conteúdo, clique em **Concluído**.
5\. Digite um nome para o seu bloco de conteúdo. Este nome será preenchido automaticamente como parte do **bloco de conteúdo Liquid tag**.
6\. (opcional) Adicione uma descrição.
7\. Clique em **Iniciar bloco de conteúdo**.

{% endif %}