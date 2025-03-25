1. Allez dans **Modèles** > **Blocs de contenu**. Cliquez sur <i class="fas fa-plus"></i> **Create Content Block (Créer un bloc de contenu)** et sélectionnez **Drag-and-drop Content Block (Glisser-déposer un bloc de contenu)**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), cette page est située dans **Engagement** > **Modèles et médias** > **Bibliothèque de blocs de contenu**.
{% endalert %}

{% if include.location == "dnd" %}

{:start="2"}
2\. Glissez-déposez les [blocs de l'éditeur]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) pour créer un bloc de contenu par glisser-déposer.
3\. Glissez-déposez un bloc de format de l'onglet **Rangs** dans l'éditeur pour créer la mise en page de votre bloc de contenu. <br><br> ![]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4\. Ajoutez des blocs de contenu à glisser-déposer selon vos besoins pour créer vos campagnes d'e-mail.
5\. Après avoir créé votre bloc de contenu, cliquez sur **Terminé**.
6\. Donnez un nom à votre bloc de contenu. Ce nom s'affichera automatiquement dans l'**étiquette Liquid du bloc de contenu**.
7) (facultatif) Ajoutez une description.
8\. Cliquez sur **Lancer le bloc de contenu**.

{% elsif include.location == "html" %}

{:start="2"}
2\. Saisissez votre HTML dans l'onglet **HTML**, ou créez votre bloc de contenu dans l'onglet **Classique**. <br><br> ![]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
4\. Après avoir créé votre bloc de contenu, cliquez sur **Terminé**.
5\. Saisissez un nom pour votre bloc de contenu. Ce nom s'affichera automatiquement dans l'**étiquette Liquid du bloc de contenu**.
6\. (facultatif) Ajoutez une description.
7\. Cliquez sur **Lancer le bloc de contenu**.

{% endif %}