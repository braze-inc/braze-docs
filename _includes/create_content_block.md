{% if include.location == "dnd" %}

1. Go to **Templates** > **Content Blocks**. Select <i class="fas fa-plus"></i> **Create Content Block** and select **Drag-and-drop Content Block**.
2. Drag and drop the [editor blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) to build a drag-and-drop Content Block. 
3. Drag and drop a format block from the **Rows** tab into the editor to create the layout of your Content Block. <br><br> ![Drag-and-drop Content Block composer.]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. Add drag-and-drop Content Blocks as needed to build out your email campaigns.
5. After creating your Content Block, select **Done**.
6. Give your Content Block a name. This name will auto-populate as part of the **Content Block Liquid Tag**.
7. (Optional) Add a description.
8. Select the **Preview** tab to view how your Content Block will appear. Optionally select **Copy preview link** to generate and copy a shareable preview link that shows what the email will look like for a random user. The link will last for seven days before it needs to be regenerated.<br><br> !["Preview" tab for the drag-and-drop Content Block composer.]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. Select **Launch Content Block**.

{% elsif include.location == "html" %}

1. Go to **Templates** > **Content Blocks**. Select <i class="fas fa-plus"></i> **Create Content Block** and select **HTML Content Block**.
2. Enter your HTML in the **HTML** tab, or build your Content Block in the **Classic** tab. <br><br> ![HTML Content Block composer]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
4. After creating your Content Block, select **Done**.
5. Enter a name for your Content Block. This name will auto-populate as part of the **Content Block Liquid Tag**.
6. (Optional) Add a description.
7. Select the **Preview** tab to view how your Content Block will appear. Optionally select **Copy preview link** to generate and copy a shareable preview link that shows what the email will look like for a random user. The link will last for seven days before it needs to be regenerated.<br><br> !["Preview" tab for the HTML Content Block composer.]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
8. Select **Launch Content Block**.

{% endif %}