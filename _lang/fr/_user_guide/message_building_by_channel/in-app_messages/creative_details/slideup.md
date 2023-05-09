---
nav_title: Slideup
article_title: Messages In-App Slideup
page_order: 2
channel:
  - messages In-App
tool:
  - Media
description: "Le présent article de référence aborde les exigences de conception des messages In-App slideup."

---

# Messages In-App Slideup

> Nos slideups apparaissent généralement en haut ou en bas de l’écran de l’application (vous pouvez le définir à la création du message). Ils sont parfaits pour avertir vos utilisateurs de nouvelles conditions de service, cookies et autres extraits de code d’information. Ils ne supposent pas d’intrusion et permettent à vos utilisateurs finaux de poursuivre l’interaction avec votre application quand le message s’affiche.

![Deux messages In-App slideup, l’un apparaissant en haut de l’écran et l’autre en bas, indiquant les recommandations en matière d’image et de texte. Voir les sections suivantes pour plus de détails.][2a]{: style="max-width: 40%; border: none;"}

## Comportement d’image et de texte

Les messages slideup peuvent contenir jusqu’à trois lignes de texte avant troncature avec des ellipses. Les images dans les slideups ne sont jamais rognées ni coupées, car elles sont toujours réduites pour s’adapter au conteneur d’images 50X50.

- Toutes les images doivent être inférieures à 5 Mo.
- Nous acceptons uniquement les types de fichiers PNG, JPG et GIF.
- Nous recommandons que la taille de vos images soit de 500 ko.

{% alert tip %} Créez des ressources en toute confiance ! Nos modèles d’image de messages In-App et d’incrustations de zone sécurisée sont conçus pour s’adapter à des appareils de toutes tailles. [Télécharger le ZIP de modèles de conception]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Disposition | Taille de la ressource | Remarques |
|--- | --- | --- |
| Image + Texte | Format 1:1<br>Haute-Res 150 x 150 px<br> Min. 50 x 50 px | Les images de différents formats seront insérées dans un conteneur d’images carré, sans rognage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Vous devez toujours [prévisualiser et tester vos messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) sur divers appareils pour s’assurer que les parties les plus importantes de votre image et de votre message s’affichent comme prévu.

[2a]: {% image_buster /assets/img/slideup-spec.png %}
[2b]: {% image_buster /assets/img/slideup-large-viewport.png %}

### Écrans plus grands

Sur une tablette ou un navigateur de bureau, un message In-App slideup s’affiche dans le coin de l’écran de l’application, comme illustré dans la capture d’écran suivante (sauf indication contraire lors de la création du message In-App).

![Message In-App slideup tel qu’il apparaît sur un écran plus grand. Le message apparaît dans le coin inférieur droit de l’écran et n’occupe pas toute la largeur de l’écran.][2b]{: style="max-width: 800px; border: none;"}
