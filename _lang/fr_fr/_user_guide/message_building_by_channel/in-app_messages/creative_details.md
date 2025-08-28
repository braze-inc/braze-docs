---
nav_title: Détails créatifs
article_title: Détails créatifs
page_order: 3.5
layout: dev_guide
guide_top_header: "Détails créatifs"
guide_top_text: "Avant de faire preuve de créativité avec nos messages in-app, vous devez connaître certaines directives. Tous les modèles de messages in-app sont conçus pour afficher des longueurs de texte et des tailles d’images variables sur des appareils modernes. Pour que votre message s'affiche correctement sur tous les téléphones, tablettes et ordinateurs, nous vous recommandons de suivre ces directives et de toujours <a href='/docs/user_guide/message_building_by_channel/in-app_messages/testing/'>tester vos messages</a> avant de les lancer."
description: "Ce hub d’accueil couvre les exigences de conception et de contenu pour les trois types de messages in-app, à savoir modal, slideup et plein écran."

channel:
  - in-app messages
tools:
  - Media

guide_featured_title: "Spécifications par type de message"

guide_featured_list:
- name: Boîte de dialogue modale
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal/
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Fenêtre contextuelle
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup/
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: "Plein écran"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/
  image: /assets/img/braze_icons/expand-05.svg

---

## Directives relatives au contenu

### Texte

Nous recommandons que le corps et les en-têtes de messages in-app soient brefs et concis (une à deux lignes pour les en-têtes, trois pour le corps). Au-delà de trois lignes, un défilement vertical du message doit probablement se faire, et les utilisateurs peuvent ne pas avoir d’engagement avec la totalité du contenu. Le seuil qui déclenche le défilement peut varier en fonction de la taille de l'appareil de l'utilisateur final, du style personnalisé ou de la présence d'images dans les messages, mais trois lignes sont généralement suffisantes.

Si vous utilisez la dernière génération de messages in-app (Génération 3), vous constatez que les polices sont par défaut celles Sans Serif du système d’exploitation iOS et Android. Les messages in-app Web sont par défaut en Helvetica.

### Images

Nos lignes directrices pour les images sont plus structurées que celles pour le texte, car nous voulons nous assurer que vos messages s'affichent comme prévu, et magnifiquement sur les téléphones, les tablettes et les ordinateurs de tous les modèles et de toutes les tailles.

En général, Braze recommande d’utiliser des images tenant dans un écran 16:10.

- **Toutes les images doivent être inférieures à 5 Mo.**
- Nous n'acceptons que les fichiers de type PNG, JPEG et GIF.
- Nous vous recommandons d'héberger les images dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) afin de permettre au SDK de Braze de télécharger des ressources à partir de notre réseau de diffusion contenu pour l'affichage des messages hors ligne.
- Pour les messages en plein écran, suivez nos lignes directrices pour la [zone de sécurité de l'image.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone)

{% alert tip %} Créez des ressources en toute confiance ! Nos modèles d'images de messages in-app et nos superpositions de zones de sécurité sont conçus pour s'adapter aux appareils de toutes tailles. [Télécharger le ZIP de modèles de conception]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

{% tabs %}{% tab Plein écran %}

![Message in-app plein écran sur un écran d’application. Le message plein écran comprend une grande image, un en-tête, le corps du message et deux boutons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

| Disposition | Taille de la ressource | Remarques |
|--- | --- | --- |
| Image + Texte | Rapport hauteur/largeur de 6:5<br>Haute résolution 1200 x 1000 px<br> Minimum 600 x 500 px | Un rognage peut se produire sur tous les côtés, mais l’image occupe toujours la moitié supérieure de la fenêtre |
| Image uniquement | Rapport hauteur/largeur de 3:5<br>Haute résolution 1200 x 2000 px<br> Minimum 600 x 1000 px | Un rognage peut se produire sur les bords gauche et droit des appareils de plus grande taille |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Plus de détails pour les messages plein écran]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen)


{% endtab %}
{% tab Fenêtre modale %}

![Message in-app modal apparaissant au centre d’une application et d’un site Web comme boîte de dialogue. Le message modal comprend une image, un en-tête, un corps de message et deux boutons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

| Disposition | Taille de la ressource | Remarques |
|--- | --- | ------ |
| Image + Texte | Rapport hauteur/largeur 29:10<br>Haute résolution 1450 x 500 px<br> Minimum 600 x 205 px | Les images hautes seront réduites et centrées horizontalement. Les images larges seront rognées sur les bords gauche et droit. |
| Image uniquement | Presque n’importe quel rapport hauteur/largeur<br>Haute résolution jusqu'à 1200 x 2000 px<br> Minimum 600 x 600 px | Le message sera redimensionné pour s’adapter à la plupart des tailles d'image. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Détails supplémentaires pour les modaux]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/modal)

{% endtab %}
{% tab Contextuel %}

![Message in-app slideup apparaissant en bas de l’écran de l’application. Le contextuel comprend une image d'icône et un bref message.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

| Disposition | Taille de la ressource | Remarques |
|--- | --- | --- |
| Image + Texte | Format 1:1<br>Haute résolution 150 x 150 px<br> Minimum 50 x 50 px | Les images de différents rapports hauteur/largeur seront insérées dans un conteneur d’images carré, sans rognage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Plus de détails pour les contextuels]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup)

{% endtab %}
{% endtabs %}

### GIF et vidéos

Braze prend actuellement en charge les GIF pour les messages in-app Web (inclus), [Android]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android) et iOS (inclus), étant donné qu'ils ont été activés lors de l'intégration de la plateforme souhaitée. Pour en savoir plus sur la vidéo dans les messages in-app, consultez notre [documentation sur la personnalisation.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#video)

## Considérations supplémentaires

Les messages in-app de Braze possèdent des spécifications de création globales et individuelles. Pour en savoir plus sur la personnalisation complète des messages in-app, consultez notre page [Personnalisation.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/) 

<br>
