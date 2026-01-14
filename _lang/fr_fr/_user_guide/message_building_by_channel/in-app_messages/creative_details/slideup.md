---
nav_title: Contextuel
article_title: Messages in-app de Slideup
page_order: 2
channel:
  - in-app messages
tool:
  - Media
description: "Cet article de référence couvre les exigences en matière de message et de conception des messages in-app contextuels."

---

# Messages in-app contextuels

> Nos contextuels apparaissent généralement en haut ou en bas de l'écran de l'appli (vous pouvez régler cela lorsque vous créez votre message). Elles sont idéales pour alerter vos utilisateurs sur les nouvelles conditions de service, les cookies et d'autres extraits de code. Ces derniers sont non intrusifs et permettent à vos utilisateurs de continuer à interagir avec votre appli pendant que le message s'affiche.

Deux messages in-app, l'un apparaissant en haut de l'écran et l'autre en bas, détaillant l'image et les recommandations textuelles. Voir les sections suivantes pour plus de détails.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width: 40%; border: none;"}

## Comportement de l'image et de la copie

Les messages contextuels peuvent contenir jusqu'à trois lignes de texte avant d'être tronqués par des ellipses. Les images dans les contextuels ne seront jamais recadrées ou coupées - elles seront toujours mises à l'échelle pour tenir dans le conteneur d'image de 50 x 50 pixels.

- Toutes les images doivent être inférieures à 5 Mo.
- Nous n'acceptons que les fichiers de type PNG, JPEG et GIF.
- Nous recommandons que vos images aient une taille de 500 KB.

{% alert tip %} Créez des ressources en toute confiance ! Nos modèles d'images de messages in-app et nos superpositions de zones de sécurité sont conçus pour s'adapter aux appareils de toutes tailles. [Téléchargez les modèles de conception ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Mise en page | Taille des ressources | Notes |
|--- | --- | --- |
| Image + texte | Rapport hauteur/largeur 1:1<br>Haute résolution 150 x 150 px<br> Minimum 50 x 50 px | Les images de différents rapports hauteur/largeur tiendront dans un conteneur d'image carré, sans recadrage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Vous devriez toujours [prévisualiser et tester vos messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) sur une variété d'appareils pour vous assurer que les zones les plus importantes de votre image et de votre message apparaissent comme prévu. Notez que lors de la prévisualisation de votre message sur le compositeur, le rendu réel sur les appareils peut être différent.

## Appareils mobiles

Sur les appareils mobiles, les contextuels apparaissent en haut ou en bas de l'écran de l'appli. Vous pouvez le spécifier lorsque vous créez votre message. Les utilisateurs peuvent faire glisser le curseur pour fermer le contextuel, ou le toucher pour l'ouvrir si une action de clic est incluse. Si une action de clic est ajoutée au contextuel, un chevron ">" apparaît.

## Des écrans plus grands

{% tabs %}
{% tab Desktop %}

Sur un navigateur de bureau, un message in-app contextuel s'affichera dans le coin de l'écran comme le montre la capture d'écran suivante (sauf indication contraire lors de la création du message in-app). Les utilisateurs peuvent cliquer sur le bouton de fermeture "X" pour fermer le contextuel.

!message in-app contextuel tel qu'il apparaît sur un navigateur de bureau. Le message apparaît dans le coin inférieur droit de l'écran et n'occupe pas toute la largeur de l'écran.]({% image_buster /assets/img/slideup-large-viewport.png %}){: style="border: none;"}

{% endtab %}
{% tab Tablet %}

Sur une tablette, un message in-app contextuel apparaît en bas de l'écran. Comme sur les appareils mobiles, les utilisateurs peuvent faire glisser leur doigt pour fermer le contextuel, ou le toucher pour l'ouvrir si une action de clic est incluse. Si une action de clic est ajoutée au contextuel, un chevron ">" apparaît. Le bouton de fermeture "X" n'est pas affiché par défaut.

Un message in-app contextuel tel qu'il apparaît sur l'écran d'une tablette. Le message apparaît en bas au milieu de l'écran et n'occupe pas toute la largeur de l'écran.]({% image_buster /assets/img/slideup-tablet.png %}){: style="border: none;"}

{% endtab %}
{% endtabs %}

