---
nav_title: Modal
article_title: Messages modaux dans l'application
page_order: 1
channel:
  - messages intégrés à l'application
tool:
  - Médias
description: "Cet article de référence couvre les exigences de message et de conception des messages modaux dans l'application."
---

# Messages modaux dans l'application

Les modales apparaissent au centre de l'écran de l'appareil avec une superposition d'écran qui l'aide à se démarquer de votre application en arrière-plan. Celles-ci sont parfaites pour suggérer à votre utilisateur de profiter d'une vente ou d'un don.

!\[Modal Specs\]\[1a\]{: style="max-width: 801px; border: none;"}

## Comportement de l'image et de la copie

Les messages modaux intégrés à l'application sont conçus pour s'adapter à l'appareil au meilleur rapport de remplissage possible tout en restant fidèle à la taille et aux ratios de l'image de votre choix ou copie de votre message.

- __Toutes les images doivent être inférieures à 5 Mo.__
- Nous n'acceptons que les types de fichiers `PNG`, `JPG`, et `GIF`.
- Nous recommandons que vos images soient de 500 Ko.

{% alert tip %} Créez des actifs en toute confiance! Nos modèles d'images de messages intégrés et nos surcouches de zone sécurisées sont conçus pour jouer avec des appareils de toutes tailles. [Télécharger le ZIP des modèles de design]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Mise en page     | Taille de l'actif                                                                                      | Notes                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Image + Texte    | Rapport d'aspect 29:10<br>Hi-Res 1450 x 500px<br> Min. 725 x 250px                         | Les images hautes ou étroites se réduisent et sont centrées horizontalement. Les grandes images seront coupées sur les bords gauche et droite. |
| Image uniquement | Presque n'importe quel ratio d'aspect<br>Hi-Res jusqu'à 1200 x 2000px<br> Min. 600 x 600px | Le message va être redimensionné pour correspondre aux images de la plupart des proportions de la taille.                                      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Vous devriez __toujours__ [prévisualiser et tester vos messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) sur une variété de périphériques pour vous assurer que les zones les plus importantes de votre image et message apparaissent comme prévu.

### Génial

Braze prend en charge l'utilisation de [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) pour les icônes de messages modaux dans l'application.

## Ecrans plus grands

Sur une tablette ou un navigateur de bureau, un message modal dans l'application restera au centre de l'écran de l'application, comme indiqué ci-dessous.

!\[Modal Viewport\]\[1b\]{: style="max-width: 800px; border: none;"}
[1a]: {% image_buster /assets/img/modal-spec.png %} [1b]: {% image_buster /assets/img/modal-Large viewport.png %}


