---
nav_title: "Plein écran"
article_title: Messages In-App plein écran
description: "Le présent article de référence aborde les exigences de conception des messages In-App plein écran."
page_type: reference
page_order: 0
channel:
  - messages In-App 
tool:
  - Media

---

# Messages In-App plein écran

Les messages plein écran occupent tout l’écran de l’appareil. Ce type de message est idéal lorsque vous avez vraiment besoin de toute l’attention de votre utilisateur, dans le cas par exemple de mises à jour obligatoires de l’application.

![Deux messages In-App plein écran, côte à côte, indiquant les recommandations en matière d’image et de texte. Voir les sections suivantes pour plus de détails.][3a]{: style="max-width: 801px; border: none;"}

## Images

Les messages In-App plein écran remplissent toute la hauteur d’un appareil et sont rognés horizontalement (côtés gauche et droit) si nécessaire. Les messages plein écran avec image et texte remplissent 50 % de la hauteur d’un appareil. Tous les messages In-App plein écran remplissent la barre d’état sur les appareils avec encoche.

- Toutes les images doivent être inférieures à 5 Mo.
- Nous acceptons uniquement les types de fichiers PNG, JPG et GIF.
- Nous recommandons que la taille de vos images soit de 500 ko.

{% alert tip %} Créez des ressources en toute confiance ! Nos modèles d’image de messages In-App et d’incrustations de zone sécurisée sont conçus pour s’adapter à des appareils de toutes tailles. [Télécharger le ZIP de modèles de conception]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

#### Portrait

| disposition | taille de la ressource | remarques |
|--- | --- | --- |
| Image + Texte | Rapport d’aspect 6:5<br>Haute résolution 1 200 x 1 000 px<br> Min. 600 x 500 px | Un rognage peut se produire sur tous les côtés, mais l’image occupe toujours la moitié supérieure de la fenêtre |
| Image uniquement | Rapport d’aspect de 3:5<br>Haute résolution 1 200 x 2 000 px<br> Min. 600 x 1 000 px | Un rognage peut se produire sur les bords gauche et droit des appareils de plus grande taille |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Paysage

| disposition | taille de la ressource | remarques |
|--- | --- | --- |
| Image + Texte | Rapport de 10:3<br>Haute résolution 2 000 x 600 px<br> Min. 1 000 x 300 px | Un rognage peut se produire sur tous les côtés, mais l’image occupe toujours la moitié supérieure de la fenêtre |
| Image uniquement | Rapport d’aspect 5:3<br>Haute résolution 2 000 x 1 200 px<br> Min. 1 000 x 600 px | Un rognage peut se produire sur les bords gauche et droit des appareils de plus grande taille |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Zone sécurisée d’image

Lors de la prévisualisation d’un message In-App plein écran dans la plateforme Braze, vous pouvez activer la zone de sécurité d’image dans la zone du message, sans danger à l’affichage d’un message sur divers appareils. Outre le test de la zone de sécurité d’image dans le volet d’aperçu, nous vous recommandons de [tester votre message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) comme toujours.

![Aperçu d’un message In-App en Braze avec l’option « Show Image Safe Zone » (Afficher la zone sécurisée d’image) activée. La zone sécurisée d’image est une incrustation sur l’image qui montre les parties de l’image non sujettes au rognage.][3c]

## Écrans plus grands

Sur une tablette ou un navigateur de bureau, un message In-App plein écran s’affiche au centre de l’écran de l’application, comme illustré dans la capture d’écran suivante.

![Message In-App plein écran tel qu’il apparaîtrait sur un grand écran. Le message apparaît comme un grand modal au centre de l’écran.][3b]{: style="max-width: 800px; border: none;"}

[3a]: {% image_buster /assets/img/full-screen-spec.png %}
[3b]: {% image_buster /assets/img/full-screen-large-viewport.png %}
[3c]: {% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %}
