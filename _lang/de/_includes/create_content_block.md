{% if include.location == "dnd" %}

1. Gehen Sie zu **Vorlagen** > **Inhaltsblöcke**. Wählen Sie <i class="fas fa-plus"></i> **Content-Block erstellen** und wählen Sie **Content-Block per Drag-and-Drop** aus.
2. Ziehen Sie die [Editorblöcke]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) per Drag-and-Drop, um einen Content-Block zu erstellen. 
3. Ziehen Sie einen Formatblock von der Registerkarte **Zeilen** in den Editor, um das Layout Ihres Inhaltsblocks zu erstellen. <br><br> ![Content-Block Komponist per Drag-and-Drop.]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. Fügen Sie bei Bedarf Content-Blöcke per Drag-and-Drop hinzu, um Ihre E-Mail-Kampagnen zu erstellen.
5. Nachdem Sie Ihren Content-Block erstellt haben, wählen Sie **Fertig**.
6. Geben Sie Ihrem Inhaltsblock einen Namen. Dieser Name wird als Teil des **Content Block Liquid Tag** automatisch ausgefüllt.
7. (Optional) Fügen Sie eine Beschreibung hinzu.
8. Wählen Sie den Tab **Vorschau**, um zu sehen, wie Ihr Content-Block aussehen wird. Wählen Sie optional **Vorschau-Link kopieren** aus, um einen Vorschau-Link zu generieren und zu kopieren, der zeigt, wie die E-Mail für einen zufälligen Nutzer:innen aussehen wird. Der Link bleibt sieben Tage lang bestehen, bevor er erneuert werden muss.<br><br> ![Tab "Vorschau" für den Content-Block-Composer per Drag-and-Drop.]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. Wählen Sie **Content-Block starten**.

{% elsif include.location == "html" %}

1. Gehen Sie zu **Vorlagen** > **Inhaltsblöcke**. Wählen Sie <i class="fas fa-plus"></i> **Content-Block erstellen** und wählen Sie **HTML Content-Block**.
2. Geben Sie Ihren HTML-Code auf der Registerkarte **HTML** ein, oder erstellen Sie Ihren Inhaltsblock auf der Registerkarte **Klassisch**. <br><br> ![HTML Content-Block Komponist]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
4. Nachdem Sie Ihren Content-Block erstellt haben, wählen Sie **Fertig**.
5. Geben Sie einen Namen für Ihren Inhaltsblock ein. Dieser Name wird als Teil des **Content Block Liquid Tag** automatisch ausgefüllt.
6. (Optional) Fügen Sie eine Beschreibung hinzu.
7. Wählen Sie den Tab **Vorschau**, um zu sehen, wie Ihr Content-Block aussehen wird. Wählen Sie optional **Vorschau-Link kopieren** aus, um einen Vorschau-Link zu generieren und zu kopieren, der zeigt, wie die E-Mail für einen zufälligen Nutzer:innen aussehen wird. Der Link bleibt sieben Tage lang bestehen, bevor er erneuert werden muss.<br><br> ![Tab "Vorschau" für den HTML Content-Block Composer.]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
8. Wählen Sie **Content-Block starten**.

{% endif %}