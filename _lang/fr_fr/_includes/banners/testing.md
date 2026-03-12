{% if include.page == "testing" %}Lorsque [vous rédigez votre message pour la bannière]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#compose-a-banner), veuillez {% elsif include.page == "campaigns" %}sélectionner «{% endif %} **Aperçu** » pour prévisualiser votre bannière ou envoyer un message test.

![Onglet Aperçu du compositeur de bannières.]({% image_buster /assets/img/banners/select_preview.png %}){: style="max-width:50%;"}

Veuillez noter que votre aperçu peut différer du rendu final sur l'appareil d'un utilisateur en raison des différences entre les matériels.

Pour envoyer un message test, veuillez ajouter un groupe de test de contenu ou un ou plusieurs utilisateurs individuels en tant que **destinataires du test**, puis sélectionnez **Envoyer le test**. Vous pourrez visualiser votre message test sur l'appareil pendant 5 minutes maximum. Vous pouvez ensuite sélectionner **Copier le lien d'aperçu** pour générer et copier un lien d'aperçu partageable qui montre à quoi ressemblera la bannière pour un utilisateur aléatoire. Le lien durera sept jours avant de devoir être régénéré.

![Onglet Aperçu du compositeur de bannières.]({% image_buster /assets/img/banners/preview_banner.png %})

Lorsque vous examinez votre bannière test, veuillez vérifier les éléments suivants :

- Votre campagne publicitaire est-elle affectée à un emplacement ?
- Les images et les médias s'affichent-ils et fonctionnent-ils comme prévu sur les types d'appareils et les tailles d'écran que vous ciblez ?
- Vos liens et boutons dirigent-ils correctement les utilisateurs vers les pages souhaitées ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous pris en compte une valeur d’attribut par défaut si le Liquid ne renvoie aucune information ?
- Votre texte est-il clair, concis et correct ?
