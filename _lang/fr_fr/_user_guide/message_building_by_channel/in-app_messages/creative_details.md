---
nav_title: Détails créatifs
article_title: Détails créatifs
page_order: 3.5
layout: dev_guide
guide_top_header: "Détails créatifs"
guide_top_text: "Avant de faire preuve de créativité avec nos messages in-app, vous devez connaître certaines directives. Tous les modèles d'envois in-app sont conçus pour afficher des longueurs de texte et des tailles d'images variables sur les appareils modernes. Pour que votre message s'affiche correctement sur tous les téléphones, tablettes et ordinateurs, nous vous recommandons de suivre ces directives et de toujours <a href='/docs/user_guide/message_building_by_channel/in-app_messages/testing/'>tester vos messages</a> avant de les lancer."
description: "Ce hub d'atterrissage couvre les exigences en matière de conception et de contenu pour les trois types de messages in-app, modale, slideup et fullscreen."

channel:
  - in-app messages
tools:
  - Media

guide_featured_title: "Spécifications par type de message"

guide_featured_list:
- name: "Fenêtre modale/boîte de dialogue modale, etc."
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal/
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Contextuel
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup/
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: "Plein écran"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/
  image: /assets/img/braze_icons/expand-05.svg

---

## Lignes directrices sur le contenu

### Texte

Pour les corps de messages in-app ou les en-têtes, nous vous recommandons de rester bref et gentil - une à deux lignes pour les en-têtes et jusqu'à trois pour les corps de messages. Après trois lignes, le message devra probablement défiler verticalement, et les utilisateurs risquent de ne pas s'intéresser à l'ensemble du contenu. Le seuil qui déclenche le défilement peut varier en fonction de la taille de l'appareil de l'utilisateur final, du style personnalisé ou de la présence d'images dans les messages, mais trois lignes sont généralement suffisantes.

Si vous utilisez la dernière génération d'envois in-app (génération 3), vous constaterez que les polices sont par défaut Sans Serif du système d'exploitation pour iOS et Android. Les messages web in-app utiliseront par défaut la police Helvetica.

### Images

Nos lignes directrices pour les images sont plus structurées que celles pour le texte, car nous voulons nous assurer que vos messages s'affichent comme prévu, et magnifiquement sur les téléphones, les tablettes et les ordinateurs de tous les modèles et de toutes les tailles.

En général, Braze recommande d'utiliser des images qui s'intègrent dans un écran 16:10.

- **Toutes les images doivent être inférieures à 5 Mo.**
- Nous n'acceptons que les fichiers de type PNG, JPEG et GIF.
- Nous vous recommandons d'héberger les images dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) afin de permettre au SDK de Braze de télécharger des ressources depuis notre réseau de diffusion de contenu pour l'affichage des messages hors ligne.
- Pour les messages en plein écran, suivez nos lignes directrices pour la [zone de sécurité de l'image.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone)

{% alert tip %} Créez des ressources en toute confiance ! Nos modèles d'images de messages in-app et nos superpositions de zones de sécurité sont conçus pour s'adapter aux appareils de toutes tailles. [Téléchargez les modèles de conception ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

{% tabs %}{% tab Fullscreen %}

Un message in-app en plein écran envahit l'écran de l'application. Le message en plein écran comprend une grande image, un en-tête, le corps du message et deux boutons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

| Mise en page | Taille des ressources | Notes |
|--- | --- | --- |
| Image + texte | Rapport hauteur/largeur 6:5<br>Haute résolution 1200 x 1000 px<br> Minimum 600 x 500 px | L'image peut être recadrée de tous les côtés, mais elle remplira toujours les 50 % supérieurs de la fenêtre de visualisation. |
| Image seulement | Rapport hauteur/largeur 3:5<br>Haute résolution 1200 x 2000 px<br> Minimum 600 x 1000 px | Un recadrage peut se produire sur les bords gauche et droit sur les appareils plus grands |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Plus de détails pour les fullscreens]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen)


{% endtab %}
{% tab Modal %}

!message modal in-app apparaissant au centre d'une application et d'un site web sous forme de dialogue. La fenêtre modale comprend une image, un en-tête, un corps de message et deux boutons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

| Mise en page | Taille des ressources | Notes |
|--- | --- | ------ |
| Image + texte | Rapport hauteur/largeur 29:10<br>Haute résolution 1450 x 500 px<br> Minimum 600 x 205 px | Les images de grande taille seront réduites et centrées horizontalement. Les images larges seront coupées sur les bords gauche et droit. |
| Image seulement | Presque tous les rapports hauteur/largeur<br>Haute résolution jusqu'à 1200 x 2000 px<br> Minimum 600 x 600 px | Le message sera redimensionné pour s'adapter aux images de la plupart des rapports hauteur/largeur. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Détails supplémentaires pour les modaux]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/modal)

{% endtab %}
{% tab Slideup %}

!Message in-app contextuel apparaissant en bas de l'écran de l'application. Le contextuel comprend une image d'icône et un bref message.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

| Mise en page | Taille des ressources | Notes |
|--- | --- | --- |
| Image + texte | Rapport hauteur/largeur 1:1<br>Haute résolution 150 x 150 px<br> Minimum 50 x 50 px | Les images de différents rapports hauteur/largeur tiendront dans un conteneur d'image carré, sans recadrage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Plus de détails pour les contextuels]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup)

{% endtab %}
{% endtabs %}

### GIFs et vidéos

Braze prend actuellement en charge les GIF pour les messages in-app Web (inclus), [Android]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android) et iOS (inclus), étant donné qu'ils ont été activés lors de l'intégration souhaitée de la plateforme. Pour en savoir plus sur la vidéo dans les messages in-app, consultez notre [documentation sur la personnalisation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#video).

## Autres considérations

Les messages in-app de Braze ont des spécifications créatives à la fois globales et individuelles. Pour en savoir plus sur la personnalisation complète des messages in-app, consultez notre page [Personnalisation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

<br>
