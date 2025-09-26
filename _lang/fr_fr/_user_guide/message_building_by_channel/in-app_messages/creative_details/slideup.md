---
nav_title: Fenêtre contextuelle
article_title: Messages in-app Slideup
page_order: 2
channel:
  - in-app messages
tool:
  - Media
description: "Le présent article de référence aborde les exigences de conception des messages in-app slideup."

---

# Messages in-app Slideup

> Nos slideups apparaissent généralement en haut ou en bas de l’écran de l’application (vous pouvez le définir à la création du message). Ils sont parfaits pour avertir vos utilisateurs de nouvelles conditions de service, cookies et autres extraits de code d’information. Ceux-ci sont non intrusifs et permettent à vos utilisateurs de continuer à interagir avec votre application pendant que le message s'affiche.

![Deux messages in-app slideup, l’un apparaissant en haut de l’écran et l’autre en bas, indiquant les recommandations en matière d’image et de texte. Voir les sections suivantes pour plus de détails.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width: 40%; border: none;"}

## Comportement d’image et de texte

Les messages slideup peuvent contenir jusqu’à trois lignes de texte avant troncature avec des ellipses. Les images dans les diaporamas ne seront jamais rognées ou coupées - elles seront toujours réduites pour s'adapter au conteneur d'image de 50 x 50 pixels.

- Toutes les images doivent être inférieures à 5 Mo.
- Nous n'acceptons que les types de fichiers PNG, JPEG et GIF.
- Nous recommandons que vos images soient de 500 Ko.

{% alert tip %} Créez des ressources en toute confiance ! Nos modèles d'images de messages in-app et nos superpositions de zones de sécurité sont conçus pour s'adapter aux appareils de toutes tailles. [Télécharger le ZIP de modèles de conception]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Disposition | Taille de la ressource | Remarques |
|--- | --- | --- |
| Image + Texte | Format 1:1<br>Haute résolution 150 x 150 px<br> Minimum 50 x 50 px | Les images de différents rapports hauteur/largeur seront insérées dans un conteneur d’images carré, sans rognage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Vous devez toujours [prévisualiser et tester vos messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) sur une variété d'appareils pour vous assurer que les zones les plus importantes de votre image et de votre message apparaissent comme prévu. Notez que, lors de la prévisualisation de votre message dans l’éditeur, le rendu réel sur les appareils peut différer.

## Appareils mobiles

Sur les appareils mobiles, les fenêtres glissantes apparaissent en haut ou en bas de l'écran de l'application. Vous pouvez spécifier cela lorsque vous créez votre message. Les utilisateurs peuvent glisser pour rejeter le slideup, ou taper pour l'ouvrir si une action de clic est incluse. Si une action de clic est ajoutée au message contextuel, un chevron « > » est affiché.

## Écrans plus grands

{% tabs %}
{% tab Ordinateur de bureau %}

Sur un navigateur de bureau, un message intégré apparaîtra dans le coin de l'écran comme indiqué dans la capture d'écran suivante (sauf indication contraire lors de la création du message intégré). Les utilisateurs peuvent cliquer sur le bouton de fermeture « X » pour fermer le message contextuel.

![Message in-app contextuel tel qu'il apparaît dans un navigateur sur ordinateur de bureau. Le message apparaît dans le coin inférieur droit de l’écran et n’occupe pas toute la largeur de l’écran.]({% image_buster /assets/img/slideup-large-viewport.png %}){: style="border: none;"}

{% endtab %}
{% tab Tablette %}

Sur une tablette, un message in-app contextuel apparaît en bas de l'écran. Comme sur les appareils mobiles, les utilisateurs peuvent glisser pour rejeter le slideup, ou taper pour l'ouvrir si une action de clic est incluse. Si une action de clic est ajoutée au message contextuel, un chevron « > » est affiché. Un bouton de fermeture "X" n'est pas affiché par défaut.

![Message in-app contextuel tel qu'il apparaît sur l'écran d'une tablette. Le message apparaît au milieu en bas de l'écran et n’occupe pas toute la largeur de l'écran.]({% image_buster /assets/img/slideup-tablet.png %}){: style="border: none;"}

{% endtab %}
{% endtabs %}

