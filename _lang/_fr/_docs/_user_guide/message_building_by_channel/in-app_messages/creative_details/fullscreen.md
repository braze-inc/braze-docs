---
nav_title: "Plein écran"
article_title: Messages intégrés en plein écran
description: "Cet article de référence couvre les exigences de message et de conception des messages en plein écran dans l'application."
page_type: Référence
page_order: 0
channel:
  - messages intégrés à l'application
tool:
  - Médias
---

# Messages en plein écran dans l'application

Les messages en plein écran prennent la totalité de l'écran de l'appareil ! Ce type de message est parfait lorsque vous avez vraiment besoin de l'attention de votre utilisateur, comme pour les mises à jour obligatoires de l'application.

!\[Full-Screen Specs\]\[3a\]{: style="max-width: 801px; border: none;"}

## Images

Les messages en plein écran dans l'application rempliront toute la hauteur d'un appareil et recadreront horizontalement (côtés gauche et droite) au besoin. Les messages image et texte plein écran remplissent 50% de la hauteur d'un appareil. Tous les messages en plein écran dans l'application rempliront la barre d'état sur les appareils "incochés".

- __Toutes les images doivent être inférieures à 5 Mo.__
- Nous n'acceptons que les types de fichiers `PNG`, `JPG`, et `GIF`.
- Nous recommandons que vos images soient de 500 Ko.

{% alert tip %} Créez des actifs en toute confiance! Nos modèles d'images de messages intégrés et nos surcouches de zone sécurisées sont conçus pour jouer avec des appareils de toutes tailles. [Télécharger le ZIP des modèles de design]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

#### Portrait

| mise en page     | taille de la ressource                                                       | notes                                                                                                                 |
| ---------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Image + Texte    | Ratio d'aspect 6:5<br>Hi-Res 1200 x 1000px<br> Min. 600 x 500px  | Le recadrage peut se produire sur tous les côtés, mais l'image remplira toujours le top 50% de la fenêtre d'affichage |
| Image uniquement | Ratio d'aspect 3:5<br>Hi-Res 1200 x 2000px<br> Min. 600 x 1000px | Le recadrage peut se produire sur les bords gauche et droit sur les appareils plus grands                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Paysage

| mise en page     | taille de la ressource                                                       | notes                                                                                                                 |
| ---------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Image + Texte    | ratio d'aspect 10:3<br>Hi-Res 2000 x 600px<br> Min. 1000 x 300px | Le recadrage peut se produire sur tous les côtés, mais l'image remplira toujours le top 50% de la fenêtre d'affichage |
| Image uniquement | 5:3 ratio aspect<br>Hi-Res 2000 x 1200px<br> Min. 1000 x 600px   | Le recadrage peut se produire sur les bords gauche et droit sur les appareils plus grands                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Zone de sécurité de l'image

Lorsque vous prévisualisez un message en plein écran dans l'application sur la plateforme Braze, vous pouvez activer la Zone de sécurité d'image dans la zone du message qui est protégée contre le recadrage lorsqu'elle est affichée sur tous les appareils. En plus de tester la zone de sécurité d'image dans le volet de prévisualisation, nous vous recommandons [de tester votre message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) comme toujours.

!\[Zone de sécurité des images\]\[3c\]

## Ecrans plus grands

Sur une tablette ou un navigateur de bureau, un message intégré en plein écran s'assied au centre de l'écran de l'application, comme indiqué ci-dessous.

!\[Full-Screen Viewport\]\[3b\]{: style="max-width: 800px; border: none;"}
[3a]: {% image_buster /assets/img/full-screen-spec.png %} [3b]: {% image_buster /assets/img/full-screen-Large viewport.png %} [3c]: {% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %}
