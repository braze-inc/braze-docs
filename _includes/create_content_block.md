1. Go to **Templates** > **Content Blocks**. Click <i class="fas fa-plus"></i> **Create Content Block** and select **Drag-and-drop Content Block**.

{% if include.location == "dnd" %}

{:start="2"}
2. Drag and drop the [editor blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) to build a drag-and-drop Content Block. 
3. Drag and drop a format block from the **Rows** tab into the editor to create the layout of your Content Block. <br><br> ![]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. Add drag-and-drop Content Blocks as needed to build out your email campaigns.
5. After creating your Content Block, click **Done**.
6. Give your Content Block a name. This name will auto-populate as part of the **Content Block Liquid Tag**.
7. (optional) Add a description.
8. Click **Launch Content Block**.

{% elsif include.location == "html" %}

{:start="2"}
2. Enter your HTML in the **HTML** tab, or build your Content Block in the **Classic** tab. <br><br> ![]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
4. After creating your Content Block, click **Done**.
5. Enter a name for your Content Block. This name will auto-populate as part of the **Content Block Liquid Tag**.
6. (optional) Add a description.
7. Click **Launch Content Block**.

{% endif %}