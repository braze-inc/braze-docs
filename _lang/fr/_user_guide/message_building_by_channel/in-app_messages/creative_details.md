---
nav_title: Détails créatifs
article_title: Détails créatifs
page_order: 2
layout: dev_guide
guide_top_header: "Détails créatifs"
guide_top_text: "Soyez créatif avec nos messages In-App ! Avant cela, découvrez certaines directives. Tous les modèles de messages In-App sont conçus pour afficher des longueurs de texte et des tailles d’images variables sur des appareils modernes. Afin que votre message s’affiche correctement sur tous les téléphones, tablettes et ordinateurs, nous vous recommandons de suivre ces directives et toujours <a href='/docs/user_guide/message_building_by_channel/in-app_messages/testing/'>tester vos messages</a> avant envoi. Consultez les spécifications créatives suivantes pour les types de messages ou l’article sur Détails créatifs."
description: "Ce hub d’accueil couvre les exigences de conception et de contenu pour les trois types de messages In-App, à savoir modal, slideup et plein écran."

channel:
  - messages In-App
tools:
  - Media

guide_featured_title: "Spécifications pour chaque type de message"

guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal/
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Slideup
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup/
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: "Plein écran"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/
  image: /assets/img/braze_icons/expand-05.svg

---

## Directives relatives au contenu

### Texte

Nous recommandons que le corps et les en-têtes de messages In-App soient brefs et concis (une à deux lignes pour les en-têtes, trois pour le corps). Au-delà de trois lignes, un défilement vertical du message doit probablement se faire, et les utilisateurs peuvent ne pas avoir d’engagement avec la totalité du contenu. Le seuil de déclenchement du défilement peut varier en fonction de la taille du dispositif de l’utilisateur final, du style personnalisé ou de la présence d’images dans les messages, mais trois lignes garantissent un affichage sûr.

Si vous utilisez la dernière génération de messages In-App (Génération 3), vous constatez que les polices sont par défaut celles Sans Serif du système d’exploitation iOS et Android. Les messages In-App Web sont par défaut en Helvetica.

### Images

Nos directives pour les images sont plus structurées que celles pour le texte, car nous voulons que vos messages s’affichent comme prévu et parfaitement sur tous les modèles de téléphones, tablettes et ordinateurs de toutes tailles.

En général, Braze recommande d’utiliser des images tenant dans un écran 16:10.

- **Toutes les images doivent être inférieures à 5 Mo.**
- Nous acceptons uniquement les types de fichiers `PNG`, `JPG`, et `GIF`.
- Nous recommandons d’héberger des images dans la [médiathèque de Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) afin de permettre au SDK de Braze de télécharger des ressources de notre CDN pour l’affichage de messages hors ligne.
- Pour les messages plein écran, suivez nos directives afin d’avoir une [zone d’image sécurisée]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone).

{% alert tip %} Créez des ressources en toute confiance ! Nos modèles d’image de messages In-App et d’incrustations de zone sécurisée sont conçus pour s’adapter à des appareils de toutes tailles. [Télécharger le ZIP de modèles de conception]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

{% tabs %}{% tab FullScreen %}

![Message In-App plein écran sur un écran d’application. Le message plein écran comprend une grande image, un en-tête, un corps de message et deux boutons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

| Disposition | Taille de la ressource | Remarques |
|--- | --- | --- |
| Image + Texte | Format 6:5<br>Haute-Res 1200 x 1000 px<br> Min. 600 x 500 px | Un rognage peut se produire sur tous les côtés, mais l’image occupe toujours la moitié supérieure de la fenêtre |
| Image uniquement | Format 3:5<br>Haute-Res 1200 x 2000 px<br> Min. 600 x 1000 px | Un rognage peut se produire sur les bords gauche et droit des appareils de plus grande taille |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[Plus de détails pour les messages plein écran]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen)


{% endtab %}
{% tab Modal %}

![Message In-App modal apparaissant au centre d’une application et d’un site Web comme boîte de dialogue. Le modal comprend une image, un en-tête, un corps de message et deux boutons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

| Disposition | Taille de la ressource | Remarques |
|--- | --- | ------ |
| Image + Texte | 2Format 9:10<br>Haute-Res 1450 x 500 px<br> Min. 600 x 205 px | Les images hautes seront réduites et centrées horizontalement. Les images larges seront rognées sur les bords gauche et droit. |
| Image uniquement | Presque n’importe quel format<br>Haute-Res jusqu’à 1200 x 2000 px<br> Min. 600 x 600 px | Le message sera redimensionné pour s’adapter à la plupart des formats d’image. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[Plus de détails pour les modaux]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/modal)

{% endtab %}
{% tab Slideup %}

![Message In-App slideup apparaissant en bas de l’écran de l’application. Le slideup comprend une image d’icône et un bref message.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

| Disposition | Taille de la ressource | Remarques |
|--- | --- | --- |
| Image + Texte | Format 1:1<br>Haute-Res 150 x 150 px<br> Min. 50 x 50 px | Les images de différents formats seront insérées dans un conteneur d’images carré, sans rognage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[Plus de détails pour les slideups]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup)

{% endtab %}
{% endtabs %}

### GIF et vidéos

Braze prend actuellement en charge les GIF pour le Web (inclus), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/), et iOS (inclus) dans les messages In-App grâce à l’activation pendant l’intégration de la plateforme souhaitée. Pour plus d’informations sur les vidéos dans les messages In-App, consultez notre [documentation sur la personnalisation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#video).

## Considérations supplémentaires

Les messages In-App de Braze possèdent des spécifications de création globales et individuelles. Pour plus d’informations sur la personnalisation complète des messages In-App, consultez notre page [Personnalisation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/).

<br>
