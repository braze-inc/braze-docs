{% if include.page == "testing" %}Lors de la [composition de votre message Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#compose-a-banner), sélectionnez{% elsif include.page == "campaigns" %}Select{% endif %} **Preview** pour prévisualiser votre Banner ou envoyer un message test.

![Onglet Aperçu du compositeur de bannières.]({% image_buster /assets/img/banners/select_preview.png %}){: style="max-width:50%;"}

Gardez à l'esprit que votre aperçu peut ne pas être identique au rendu final sur l'appareil d'un utilisateur en raison des différences entre les matériels.

Pour envoyer un message de test, ajoutez un groupe de test de contenu ou un ou plusieurs utilisateurs individuels en tant que **destinataires du test**, puis sélectionnez **Envoyer le test.** Vous pourrez consulter votre message de test sur l'appareil pendant 5 minutes maximum. Vous pouvez ensuite sélectionner **Copier le lien de prévisualisation** pour générer et copier un lien de prévisualisation partageable qui montre à quoi ressemblera la bannière pour un utilisateur aléatoire. Le lien durera sept jours avant de devoir être régénéré.

![Onglet Aperçu du compositeur de bannières.]({% image_buster /assets/img/banners/preview_banner.png %})

En examinant votre bannière de test, vérifiez les points suivants :

- Votre campagne Banner est-elle assignée à un placement ?
- Les images et les médias s'affichent-ils et agissent-ils comme prévu sur les types d'appareils et les tailles d'écran que vous avez ciblés ?
- Vos liens et boutons dirigent-ils l'utilisateur vers l'endroit où il doit se rendre ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous pris en compte une valeur d’attribut par défaut si le Liquid ne renvoie aucune information ?
- Votre texte est-il clair, concis et correct ?
