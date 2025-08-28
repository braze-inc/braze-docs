{% if include.location == "dnd" %}

1. Acessar **Modelos** > **Blocos de Conteúdo**. Selecione <i class="fas fa-plus"></i> **Criar Bloco de Conteúdo** e selecione **Arrastar e soltar Bloco de Conteúdo**.
2. Arraste e solte os [blocos de editor]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) para construir um bloco de conteúdo arrastável. 
3. Arraste e solte um bloco de formato da guia **Rows** no editor para criar o layout do seu bloco de conteúdo. <br><br> ![Arrastar e soltar compositor de Bloco de Conteúdo.]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. Adicione blocos de conteúdo de arrastar e soltar conforme necessário para criar suas campanhas de e-mail.
5. Após criar seu Bloco de Conteúdo, selecione **Concluído**.
6. Dê um nome ao seu bloco de conteúdo. Este nome será preenchido automaticamente como parte do **bloco de conteúdo Liquid tag**.
7. (Opcional) Adicione uma descrição.
8. Selecione a guia **Prévia** para ver como seu Bloco de Conteúdo aparecerá. Opcionalmente, selecione **Copiar link de prévia** para gerar e copiar um link de prévia compartilhável que mostra como o e-mail ficará para um usuário aleatório. O link durará sete dias antes de precisar ser regenerado.<br><br> ![ guia "Prévia" para o compositor de Bloco de Conteúdo arrastar e soltar.]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. Selecione **Lançar Bloco de Conteúdo**.

{% elsif include.location == "html" %}

1. Acessar **Modelos** > **Blocos de Conteúdo**. Selecione <i class="fas fa-plus"></i> **Criar Bloco de Conteúdo** e selecione **Bloco de Conteúdo HTML**.
2. Insira seu HTML na guia **HTML**, ou construa seu bloco de conteúdo na guia **Classic**. <br><br> ![ compositor de Bloco de Conteúdo HTML]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
4. Após criar seu Bloco de Conteúdo, selecione **Concluído**.
5. Digite um nome para o seu bloco de conteúdo. Este nome será preenchido automaticamente como parte do **bloco de conteúdo Liquid tag**.
6. (Opcional) Adicione uma descrição.
7. Selecione a guia **Prévia** para ver como seu Bloco de Conteúdo aparecerá. Opcionalmente, selecione **Copiar link de prévia** para gerar e copiar um link de prévia compartilhável que mostra como o e-mail ficará para um usuário aleatório. O link durará sete dias antes de precisar ser regenerado.<br><br> ![ guia "Prévia" para o compositor de Bloco de Conteúdo HTML.]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
8. Selecione **Lançar Bloco de Conteúdo**.

{% endif %}