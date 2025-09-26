---
nav_title: "Plein écran"
article_title: Messages in-app plein écran
description: "Le présent article de référence aborde les exigences de conception des messages in-app plein écran."
page_type: reference
page_order: 0
channel:
  - in-app messages
tool:
  - Media

---

# Messages in-app plein écran

> Les messages plein écran occupent tout l’écran de l’appareil ! Ce type de message est idéal lorsque vous avez vraiment besoin de toute l’attention de votre utilisateur, dans le cas par exemple de mises à jour obligatoires de l’application.

{% tabs %}
{% tab Portrait %}

![Deux messages in-app plein écran, côte à côte en orientation portrait, indiquant les recommandations en matière d’image et de texte. Voir les sections suivantes pour plus de détails.]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Paysage %}

![Deux messages in-app plein écran, côte à côte en orientation paysage, indiquant les recommandations en matière d’image et de texte. Voir les sections suivantes pour plus de détails.]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## Images

Les messages in-app plein écran remplissent toute la hauteur d’un appareil et sont rognés horizontalement (côtés gauche et droit) si nécessaire. Les messages plein écran avec image et texte remplissent 50 % de la hauteur d’un appareil. Tous les messages in-app plein écran remplissent la barre d’état sur les appareils avec encoche.

- Toutes les images doivent être inférieures à 5 Mo.
- Nous n'acceptons que les fichiers de type PNG, JPEG et [GIF]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs#gifs).
- Nous recommandons que vos images aient une taille de 500 KB.

{% alert tip %} Créez des ressources en toute confiance ! Nos modèles d'images de messages in-app et nos superpositions de zones de sécurité sont conçus pour s'adapter aux appareils de toutes tailles. [Télécharger le ZIP de modèles de conception]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

### Portrait

| disposition | taille de la ressource | remarques |
|--- | --- | --- |
| Image et texte | Rapport hauteur/largeur de 6:5<br> Haute résolution 1200 x 1000 px<br> Minimum 600 x 500 px | Un rognage peut se produire sur tous les côtés, mais l’image occupe toujours la moitié supérieure de la fenêtre |
| Image uniquement | Rapport hauteur/largeur de 3:5<br> Haute résolution 1200 x 2000 px<br> Minimum 600 x 1000 px | Un rognage peut se produire sur les bords gauche et droit des appareils de plus grande taille |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Paysage

| disposition | taille de la ressource | remarques |
|--- | --- | --- |
| Image et texte | Rapport hauteur/largeur de 10:3<br> Haute résolution 2000 x 600px<br> Minimum 1000 x 300 px | Un rognage peut se produire sur tous les côtés, mais l’image occupe toujours la moitié supérieure de la fenêtre |
| Image uniquement | Rapport hauteur/largeur de 5:3<br> Haute résolution 2000 x 1200px<br> Minimum 1000 x 600 px | Un rognage peut se produire sur les bords gauche et droit des appareils de plus grande taille |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Zone sécurisée d’image

Lors de la prévisualisation d’un message in-app plein écran dans la plateforme Braze, vous pouvez activer la zone de sécurité d’image dans la zone du message, sans danger à l’affichage d’un message sur divers appareils. En plus de tester la zone de sécurité de l'image dans le volet de prévisualisation, nous vous recommandons de [tester votre message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) comme d'habitude.

![Aperçu d’un message in-app en Braze avec l’option « Show Image Safe Zone » (Afficher la zone sécurisée d’image) activée. La zone de sécurité de l'image est un recouvrement de l'image qui visualise les parties de l'image qui ne seront pas recadrées.]({% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %})

## Écrans plus grands

Sur une tablette ou un navigateur de bureau, un message in-app plein écran s’affiche au centre de l’écran de l’application, comme illustré dans la capture d’écran suivante.

{% tabs %}
{% tab Portrait %}

![Message in-app plein écran tel qu’il apparaîtrait sur un grand écran en orientation portrait. Le message s'affiche sous la forme d'une grande fenêtre modale au centre de l'écran.]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Paysage %}

![Message in-app plein écran tel qu’il apparaîtrait sur un grand écran en orientation paysage. Le message s'affiche sous la forme d'une grande fenêtre modale au centre de l'écran.]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

