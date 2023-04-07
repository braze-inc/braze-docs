---
nav_title: Modal
article_title: Messages In-App modaux
page_order: 1
channel:
  - messages In-App
tool:
  - Media
description: "Le présent article de référence aborde les exigences de conception des messages In-App modaux."

---

# Messages In-App modaux

Les modaux apparaissent au centre de l’écran de l’appareil avec une incrustation le démarquant de votre application en arrière-plan. Ils sont parfaits pour suggérer plus ou moins subtilement à votre utilisateur de profiter d’une vente ou d’un concours.

![Deux messages In-App modaux, côte à côte, indiquant les recommandations en matière d’image et de texte. Voir les sections suivantes pour plus de détails.][1a]{: style="max-width: 801px; border: none;"}

## Comportement d’image et de texte

Les messages In-App modaux sont conçus pour s’adapter le mieux possible aux proportions de l’appareil, tout en restant fidèle à la taille et aux rapports de l’image ou du texte de votre choix pour votre message.

- Toutes les images doivent être inférieures à 5 Mo.
- Nous acceptons uniquement les types de fichiers PNG, JPG et GIF.
- Nous recommandons que la taille de vos images soit de 500 ko.

{% alert tip %} Créez des ressources en toute confiance ! Nos modèles d’image de messages In-App et d’incrustations de zone sécurisée sont conçus pour s’adapter à des appareils de toutes tailles. [Télécharger le ZIP de modèles de conception]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Disposition | Taille de la ressource | Remarques |
|--- | --- | ------ |
| Image + Texte | 2Format 9:10<br>Haute-Res 1450 x 500 px<br> Min. 725 x 250 px | Les images hautes ou étroites sont réduites et centrées horizontalement. Les images larges seront rognées sur les bords gauche et droit. |
| Image uniquement | Presque n’importe quel format<br>Haute-Res jusqu’à 1200 x 2000 px<br> Min. 600 x 600 px | Le message sera redimensionné pour s’adapter à la plupart des formats d’image. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Vous devez toujours [prévisualiser et tester vos messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) sur divers appareils pour s’assurer que les parties les plus importantes de votre image et de votre message s’affichent comme prévu.

### Font Awesome

Braze prend en charge [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) pour les icônes de message In-App modal.

## Écrans plus grands

Sur une tablette ou un navigateur de bureau, un message In-App modal s’affiche toujours au centre de l’écran de l’application, comme illustré dans la capture d’écran suivante.

![Message In-App modal tel qu’il apparaîtrait sur un grand écran. Comme sur les téléphones, les messages s’affichent au centre de l’écran.][1b]{: style="max-width: 800px; border: none;"}

[1a]: {% image_buster /assets/img/modal-spec.png %}
[1b]: {% image_buster /assets/img/modal-large-viewport.png %}


