---
nav_title: Glissement vers le haut
article_title: Faire glisser les messages dans l'application
page_order: 2
channel:
  - messages intégrés à l'application
tool:
  - Médias
description: "Cet article de référence couvre les exigences de message et de conception des messages glissants dans l'application."
---

# Faire glisser les messages dans l'application

Nos slideups apparaissent généralement en haut ou en bas de l'écran de l'application (vous pouvez le définir lorsque vous créez votre message). Ils sont parfaits pour avertir vos utilisateurs des nouvelles conditions de service, des cookies et d'autres extraits d'informations. Elles ne sont pas discrètes et permettent à vos utilisateurs finaux de continuer à interagir avec votre application pendant que le message s'affiche.

!\[Slideup Specs\]\[2a\]{: style="max-width: 459px; border: none;"}

## Comportement de l'image et de la copie

Les messages de glissement peuvent contenir jusqu'à trois lignes de copie avant de tronquer avec des ellipses. Les images dans les diapositives ne seront jamais recadrées ou coupées - elles seront toujours réduites pour tenir dans le conteneur d'image 50X50.

- __Toutes les images doivent être inférieures à 5 Mo.__
- Nous n'acceptons que les types de fichiers `PNG`, `JPG`, et `GIF`.
- Nous recommandons que vos images soient de 500 Ko.

{% alert tip %} Créez des actifs en toute confiance! Nos modèles d'images de messages intégrés et nos surcouches de zone sécurisées sont conçus pour jouer avec des appareils de toutes tailles. [Télécharger le ZIP des modèles de design]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Mise en page  | Taille de l'actif                                                         | Notes                                                                                                |
| ------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Image + Texte | Rapport d'aspect 1:1<br>Hi-Res 150 x 150px<br> Min. 50 x 50px | Les images de différents ratios d'aspect s'insèrent dans un conteneur d'image carré, sans recadrage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Vous devriez __toujours__ [prévisualiser et tester vos messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) sur une variété de périphériques pour vous assurer que les zones les plus importantes de votre image et message apparaissent comme prévu.
[2a]: {% image_buster /assets/img/slideup-spec.png %} [2b]: {% image_buster /assets/img/slideup-Large viewport.png %}

### Ecrans plus grands

Sur une tablette ou un navigateur de bureau, un message glissant dans l'application s'assied dans le coin de l'écran de l'application comme indiqué ci-dessous (sauf indication contraire lors de la création du message dans l'application).

!\[Slideup Viewport\]\[2b\]{: style="max-width: 800px; border: none;"}
