{% if include.location == "dnd" %}

1. Allez dans **Modèles** > **Blocs de contenu**. Sélectionnez <i class="fas fa-plus"></i> **Create Content Block (Créer un bloc de contenu)** et sélectionnez **Drag-and-drop Content Block (Glisser-déposer un bloc de contenu)**.
2. Glissez-déposez les [blocs de l'éditeur]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) pour créer un bloc de contenu par glisser-déposer. 
3. Glissez-déposez un bloc de format de l'onglet **Rangs** dans l'éditeur pour créer la mise en page de votre bloc de contenu. <br><br> ![Compositeur de blocs de contenu par glisser-déposer.]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. Ajoutez des blocs de contenu à glisser-déposer selon vos besoins pour créer vos campagnes d'e-mail.
5. Après avoir créé votre bloc de contenu, sélectionnez **Terminé**.
6. Donnez un nom à votre bloc de contenu. Ce nom s'affichera automatiquement dans l'**étiquette Liquid du bloc de contenu**.
7. (Facultatif) Ajoutez une description.
8. Sélectionnez l'onglet **Aperçu** pour visualiser l'apparence de votre bloc de contenu. Sélectionnez éventuellement **Copier le lien de prévisualisation** pour générer et copier un lien de prévisualisation partageable qui montre à quoi ressemblera l'e-mail pour un utilisateur aléatoire. Le lien durera sept jours avant de devoir être régénéré.<br><br> ![Onglet "Aperçu" pour le compositeur de blocs de contenu à glisser-déposer.]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. Sélectionnez **Lancer le bloc de contenu**.

{% elsif include.location == "html" %}

1. Allez dans **Modèles** > **Blocs de contenu**. Sélectionnez <i class="fas fa-plus"></i> **Create Content Block (Créer un bloc de contenu)** et sélectionnez **HTML Content Block (Bloc de contenu HTML)**.
2. Saisissez votre HTML dans l'onglet **HTML**, ou créez votre bloc de contenu dans l'onglet **Classique**. <br><br> ![Compositeur de blocs de contenu HTML]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
4. Après avoir créé votre bloc de contenu, sélectionnez **Terminé**.
5. Saisissez un nom pour votre bloc de contenu. Ce nom s'affichera automatiquement dans l'**étiquette Liquid du bloc de contenu**.
6. (Facultatif) Ajoutez une description.
7. Sélectionnez l'onglet **Aperçu** pour visualiser l'apparence de votre bloc de contenu. Sélectionnez éventuellement **Copier le lien de prévisualisation** pour générer et copier un lien de prévisualisation partageable qui montre à quoi ressemblera l'e-mail pour un utilisateur aléatoire. Le lien durera sept jours avant de devoir être régénéré.<br><br> ![Onglet "Aperçu" pour le compositeur de blocs de contenu HTML.]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
8. Sélectionnez **Lancer le bloc de contenu**.

{% endif %}