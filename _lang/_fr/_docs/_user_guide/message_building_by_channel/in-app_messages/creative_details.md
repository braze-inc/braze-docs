---
nav_title: Détails de la création
article_title: Détails de la création
page_order: 1
layout: en vedette
guide_top_header: "Détails de la création"
guide_top_text: "Soyez créatif avec nos messages dans l'application! Mais vous devriez d'abord connaître certaines lignes directrices! Tous les modèles de messages intégrés sont conçus pour afficher des longueurs de texte et des tailles d'images variées sur les appareils modernes. Afin de s'assurer que votre message s'affiche bien sur tous les téléphones, tablettes et ordinateurs, nous vous recommandons de suivre ces directives et de toujours <a href='/docs/user_guide/message_building_by_channel/in-app_messages/testing/'>tester vos messages</a> avant de lancer. Consultez les spécifications créatives de chaque type de message ou les détails créatifs globaux ci-dessous."
description: "Ce hub d'atterrissage couvre la conception et les exigences de contenu pour les trois types de messages intégrés, de messages modaux, de glissements et en plein écran."
channel:
  - messages intégrés à l'application
tools:
  - Médias
guide_featured_title: "Spécifications pour chaque type de message"
guide_featured_list:
  - 
    name: Modal
    link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal/
    image: /assets/img/icon_modal.png
  - 
    name: Glissement vers le haut
    link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup/
    image: /assets/img/icon_slideup.png
  - 
    name: "Plein écran"
    link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/
    image: /assets/img/icon_full_screen.png
---

## Directives de contenu

### Texte du texte

Pour les corps de messages intégrés ou les en-têtes, nous vous recommandons de le garder court et doux - une à deux lignes pour les en-têtes; jusqu'à trois pour les corps. Après trois lignes, le message devra probablement faire défiler verticalement, et les utilisateurs pourraient ne pas s'engager avec tout le contenu. Le seuil qui déclenche le défilement peut varier en fonction de la taille du périphérique de l'utilisateur final, style personnalisé, ou présence d'images dans les messages, mais trois lignes sont généralement sûres!

Si vous utilisez la dernière génération de messages dans l'application (Génération 3), vous trouverez que les polices sont par défaut sans Serif pour iOS et Android. Les messages Web dans l'application seront par défaut à Helvetica.

### Images

Nos directives pour les images sont plus structurées que celles pour le texte, comme nous voulons nous assurer que vos messages s'affichent comme prévu, et magnifiquement sur les téléphones, les tablettes et les ordinateurs de tous les modèles et tailles.

En général, Braze recommande d'utiliser des images qui s'intègrent dans un écran 16:10.

- __Toutes les images doivent être inférieures à 5 Mo.__
- Nous n'acceptons que les types de fichiers `PNG`, `JPG`, et `GIF`.
- Nous vous recommandons d'héberger des images dans la [Braze Media Library]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) pour permettre au Braze SDK de télécharger des ressources de notre CDN pour l'affichage de messages hors ligne.
- Pour les messages en plein écran, suivez nos consignes pour la [Zone de sécurité d'image]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone).

{% alert tip %} Créez des actifs en toute confiance! Nos modèles d'images de messages intégrés et nos surcouches de zone sécurisées sont conçus pour jouer avec des appareils de toutes tailles. [Télécharger le ZIP des modèles de design]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

{% tabs %}{% tab Full-Screen %}

![Comportement plein écran]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

[Plus de détails pour les écrans entiers]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen)

| Mise en page     | Taille de l'actif                                                            | Notes                                                                                                                 |
| ---------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Image + Texte    | Ratio d'aspect 6:5<br>Hi-Res 1200 x 1000px<br> Min. 600 x 500px  | Le recadrage peut se produire sur tous les côtés, mais l'image remplira toujours le top 50% de la fenêtre d'affichage |
| Image uniquement | Ratio d'aspect 3:5<br>Hi-Res 1200 x 2000px<br> Min. 600 x 1000px | Le recadrage peut se produire sur les bords gauche et droit sur les appareils plus grands                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


{% endtab %}
{% tab Modal %}

![Comportement modal]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

[Plus de détails pour les modals]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/modal)

| Mise en page     | Taille de l'actif                                                                                      | Notes                                                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| Image + Texte    | Rapport d'aspect 29:10<br>Hi-Res 1450 x 500px<br> Min. 600 x 205 px                        | Les grandes images seront réduites et centrées horizontalement. Les grandes images seront coupées sur les bords gauche et droite. |
| Image uniquement | Presque n'importe quel ratio d'aspect<br>Hi-Res jusqu'à 1200 x 2000px<br> Min. 600 x 600px | Le message va être redimensionné pour correspondre aux images de la plupart des proportions de la taille.                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% tab Slideup %}

![Comportement de glissement]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

[Plus de détails pour les slideups]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup)

| Mise en page  | Taille de l'actif                                                         | Notes                                                                                                |
| ------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Image + Texte | Rapport d'aspect 1:1<br>Hi-Res 150 x 150px<br> Min. 50 x 50px | Les images de différents ratios d'aspect s'insèrent dans un conteneur d'image carré, sans recadrage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% endtabs %}

### GIFs et vidéos

Braze supporte actuellement les GIFs pour le Web (inclus), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#gifs-IAMs), et la messagerie iOS (incluse) dans l'application, étant donné qu'elle a été activée lors de l'intégration de la plate-forme souhaitée. Pour plus d'informations sur la vidéo dans les messages de l'application, consultez notre [documentation de personnalisation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#video).

## Considérations supplémentaires

Les messages de Braze dans l'application ont des spécifications à la fois globales et individuelles créatives. Pour plus d'informations sur la personnalisation complète des messages dans l'application, allez sur notre page [Personnaliser]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/).

{% alert important %}
  Ces détails ne s'appliquent qu'à notre plus récente génération de messages dans l'application (Génération 3). Si vous n'utilisez pas notre dernière génération de messages dans l'application, consultez notre documentation de [précédentes générations de messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/previous_in-app_message_generations/) dans l'application.
{% endalert %}

<br>
