{% if include.location == "dnd" %}

1. Acessar **Modelos** > **Blocos de Conteúdo**. Selecione <i class="fas fa-plus"></i> **Create Content Block** e selecione **Drag-and-drop Content Block**.
2. Arraste e solte os [blocos de editor]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) para construir um bloco de conteúdo arrastável. 
3. Arraste e solte um bloco de formato da guia **Rows** no editor para criar o layout do seu bloco de conteúdo. <br><br> ![Criador de blocos de conteúdo do tipo arrastar e soltar.]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. Adicione blocos de conteúdo de arrastar e soltar conforme necessário para criar suas campanhas de e-mail.
5. Depois de criar seu bloco de conteúdo, selecione **Done (Concluído**).
6. Dê um nome ao seu bloco de conteúdo. Este nome será preenchido automaticamente como parte do **bloco de conteúdo Liquid tag**.
7. (Opcional) Adicione uma descrição.
8. Selecione a guia **Preview (Pré-visualização** ) para ver como seu bloco de conteúdo aparecerá. Opcionalmente, selecione **Copiar link de visualização** para gerar e copiar um link de visualização compartilhável que mostre como será o e-mail para um usuário aleatório. O link terá duração de sete dias antes de precisar ser regenerado.<br><br> ![Guia "Pré-visualização" para o criador de blocos de conteúdo de arrastar e soltar.]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. Selecione **Launch Content Block (Iniciar bloco de conteúdo**).

{% elsif include.location == "html" %}

1. Acessar **Modelos** > **Blocos de Conteúdo**. Selecione <i class="fas fa-plus"></i> **Create Content Block** e selecione **HTML Content Block**.
2. Insira seu HTML na guia **HTML**, ou construa seu bloco de conteúdo na guia **Classic**. <br><br> ![Criador do bloco de conteúdo HTML]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
4. Depois de criar seu bloco de conteúdo, selecione **Done (Concluído**).
5. Digite um nome para o seu bloco de conteúdo. Este nome será preenchido automaticamente como parte do **bloco de conteúdo Liquid tag**.
6. (Opcional) Adicione uma descrição.
7. Selecione a guia **Preview (Pré-visualização** ) para ver como seu bloco de conteúdo aparecerá. Opcionalmente, selecione **Copiar link de visualização** para gerar e copiar um link de visualização compartilhável que mostre como será o e-mail para um usuário aleatório. O link terá duração de sete dias antes de precisar ser regenerado.<br><br> ![Guia "Pré-visualização" do criador do bloco de conteúdo HTML.]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
8. Selecione **Launch Content Block (Iniciar bloco de conteúdo**).

{% endif %}