1. Gehen Sie zu **Vorlagen** > **Inhaltsblöcke**. Klicken Sie auf <i class="fas fa-plus"></i> **Inhaltsblock erstellen** und wählen Sie **Inhaltsblock ziehen und ablegen**.

{% if include.location == "dnd" %}

{:start="2"}
2\. Ziehen Sie die [Editorblöcke]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) per Drag-and-Drop, um einen Content-Block zu erstellen.
3\. Ziehen Sie einen Formatblock von der Registerkarte **Zeilen** in den Editor, um das Layout Ihres Inhaltsblocks zu erstellen. <br><br> ![]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4\. Fügen Sie bei Bedarf Content-Blöcke per Drag-and-Drop hinzu, um Ihre E-Mail-Kampagnen zu erstellen.
5\. Nachdem Sie Ihren Inhaltsblock erstellt haben, klicken Sie auf **Fertig**.
6\. Geben Sie Ihrem Inhaltsblock einen Namen. Dieser Name wird als Teil des **Content Block Liquid Tag** automatisch ausgefüllt.
7\. (optional) Fügen Sie eine Beschreibung hinzu.
8\. Klicken Sie auf **Inhaltsblock starten**.

{% elsif include.location == "html" %}

{:start="2"}
2\. Geben Sie Ihren HTML-Code auf der Registerkarte **HTML** ein, oder erstellen Sie Ihren Inhaltsblock auf der Registerkarte **Klassisch**. <br><br> ![]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
4\. Nachdem Sie Ihren Inhaltsblock erstellt haben, klicken Sie auf **Fertig**.
5\. Geben Sie einen Namen für Ihren Inhaltsblock ein. Dieser Name wird als Teil des **Content Block Liquid Tag** automatisch ausgefüllt.
6\. (optional) Fügen Sie eine Beschreibung hinzu.
7\. Klicken Sie auf **Inhaltsblock starten**.

{% endif %}