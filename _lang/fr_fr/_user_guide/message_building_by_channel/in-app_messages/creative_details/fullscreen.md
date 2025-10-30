---
nav_title: "Plein écran"
article_title: Messages in-app en plein écran
description: "Cet article de référence couvre les exigences en matière de message et de conception des messages in-app en plein écran."
page_type: reference
page_order: 0
channel:
  - in-app messages
tool:
  - Media

---

# Messages in-app en plein écran

> Les messages en plein écran occupent tout l'écran de l'appareil ! Ce type de message est idéal lorsque vous avez vraiment besoin de l'attention de votre utilisateur, comme pour les mises à jour obligatoires d'une application.

{% tabs %}
{% tab Portrait %}

Deux messages in-app en plein écran, côte à côte, en orientation portrait, détaillant l'image et les recommandations textuelles. Voir les sections suivantes pour plus de détails.]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Landscape %}

Deux messages in-app en plein écran, côte à côte, en orientation paysage, détaillant l'image et les recommandations textuelles. Voir les sections suivantes pour plus de détails.]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## Images

Les messages in-app en plein écran occuperont toute la hauteur d'un appareil et seront recadrés horizontalement (côtés gauche et droit) si nécessaire. Les messages image et texte en plein écran occupent 50 % de la hauteur de l'appareil. Tous les messages in-app en plein écran rempliront la barre d'état sur les appareils "à encoche".

- Toutes les images doivent être inférieures à 5 Mo.
- Nous n'acceptons que les fichiers de type PNG, JPEG et [GIF]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs#gifs).
- Nous recommandons que vos images aient une taille de 500 KB.

{% alert tip %} Créez des ressources en toute confiance ! Nos modèles d'images de messages in-app et nos superpositions de zones de sécurité sont conçus pour s'adapter aux appareils de toutes tailles. [Téléchargez les modèles de conception ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

### Portrait

| disposition | taille des ressources | notes |
|--- | --- | --- |
| Image et texte | Rapport hauteur/largeur 6:5<br> Haute résolution 1200 x 1000 px<br> Minimum 600 x 500 px | L'image peut être recadrée de tous les côtés, mais elle remplira toujours les 50 % supérieurs de la fenêtre de visualisation. |
| Image seulement | Rapport hauteur/largeur 3:5<br> Haute résolution 1200 x 2000 px<br> Minimum 600 x 1000 px | Un recadrage peut se produire sur les bords gauche et droit sur les appareils plus grands |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Paysage

| disposition | taille des ressources | notes |
|--- | --- | --- |
| Image et texte | Rapport hauteur/largeur 10:3<br> Haute résolution 2000 x 600px<br> Minimum 1000 x 300 px | L'image peut être recadrée de tous les côtés, mais elle remplira toujours les 50 % supérieurs de la fenêtre de visualisation. |
| Image seulement | Rapport hauteur/largeur 5:3<br> Haute résolution 2000 x 1200px<br> Minimum 1000 x 600 px | Un recadrage peut se produire sur les bords gauche et droit sur les appareils plus grands |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Zone de sécurité de l'image

Lors de la prévisualisation d'un message in-app en plein écran dans la plateforme Braze, vous pouvez activer la zone de sécurité de l'image vers la zone du message qui ne risque pas d'être recadrée lors de l'affichage sur les appareils. En plus de tester la zone de sécurité de l'image dans le volet de prévisualisation, nous vous recommandons de [tester votre message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) comme d'habitude.

L'envoi d'un message in-app dans Braze avec l'option "Show Image Safe Zone" activée. La zone de sécurité de l'image est une superposition de l'image qui visualise les parties de l'image qui ne seront pas recadrées.]({% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %})

## Des écrans plus grands

Sur une tablette ou un navigateur de bureau, un message in-app en plein écran se trouve au centre de l'écran de l'application, comme le montre la capture d'écran suivante.

{% tabs %}
{% tab Portrait %}

Message in-app en plein écran tel qu'il apparaîtrait sur un grand écran en orientation portrait. Le message s'affiche sous la forme d'une grande fenêtre modale/boîte de dialogue, au centre de l'écran.]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Landscape %}

Message in-app en plein écran tel qu'il apparaîtrait sur un grand écran en orientation paysage. Le message s'affiche sous la forme d'une grande fenêtre modale/boîte de dialogue, au centre de l'écran.]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

