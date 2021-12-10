---
nav_title: "Envoyer des histoires"
article_title: Envoyer des histoires
page_order: 2
page_type: Référence
description: "Cet article de référence couvre ce que sont les Histoires Push, comment en créer un, ainsi que quelques questions fréquemment posées."
channel:
  - Pousser
---

# Envoyer des histoires

> Cet article de référence couvre ce que sont les Histoires Push, comment en créer un, ainsi que quelques questions fréquemment posées.

Push Stories est un nouveau type de notification push introduit par Braze. Cette fonctionnalité prend la fonctionnalité de carrousel photo popularisée dans Instagram et Facebook et permet aux marketeurs de créer un carrousel de pages dans une poussée qui raconte un riche, histoire cohérente. Ces pages se composent d'une image, d'une action de clic, d'un titre et d'une description. Vos utilisateurs peuvent glisser à travers ces pages et voir l'histoire, comme vous l'avez dit.

| Exemple Android (Expandu) | Exemple IOS (Expandu) |
|:-------------------------:|:---------------------:|
| !\[Aperçu Android\]\[1\]  | !\[Aperçu IOS\]\[2\]  |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
Sur iOS SDK versions 3.13. +, en raison d'un changement dans la façon dont le SDK télécharge les images, une vignette de la première image ne sera pas affichée sur la vue condensée de la push. Assurez-vous que votre copie de message invite les utilisateurs à étendre le push pour voir les images.
{% endalert %}

## Pré-requis

Les utilisateurs doivent mettre à jour vers la dernière version d'Android (version 2.2.0+) et d'iOS (version 3.2.0+) pour recevoir des histoires push.

## Comment utiliser Push Stories

!\[Composer dropdown\]\[6\]{: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Pour utiliser les Histoires Push, créez une [campagne de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) et sélectionnez **Histoires Push** comme votre **Type de Notification**.

### Compositeur de l'Histoire Push

Pour créer une page, effectuez les étapes suivantes :

1. Cliquez sur **Gérer les pages** du compositeur principal. <br><br>!\[Gérer les pages\]\[4\]{: style="max-width:70%"}<br><br>
2. Insérez une image pour chaque page, avec le comportement de clic pour cette image.
3. Si vous le souhaitez, ajoutez un **Titre** et **Description** pour chaque page. Si vous utilisez un titre et une décription pour une page, elles doivent être insérées pour toutes les pages.

Les aperçus seront réfléchis et interactifs.

!\[Composer Workflow\]\[3\]{: style="max-width:60%"}

{% alert important %}
Si vous tirez des images avec [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content), assurez-vous que l'URL de votre image commence par `https://`. L'utilisation de `http://` va faire planter votre application.
{% endalert %}

### Segmentation de l'histoire poussée

Lorsque vous créez une campagne ou Canvas, vous pouvez filtrer les utilisateurs que vous voulez cibler en fonction de s'ils ont cliqué sur une page de l'Histoire. Ensuite, sélectionnez la campagne et la page que vous souhaitez utiliser pour cibler vos utilisateurs.

### Analyses des Histoires Push

!\[Analyses de l'histoire Push\]\[5\]

Les analytiques ressembleront beaucoup à la section d'analyse actuelle pour la notification push. La seule différence est que lorsque vous ouvrez la section « Débit direct », vous pouvez maintenant voir les clics par page.

## Dépannage

### Je me suis envoyé une histoire Push Story sur iOS mais je n'ai pas reçu la notification

Apple a mis en place des règles spécifiques qui empêcheront que certains types de notifications soient envoyés à un appareil en fonction d'un certain nombre de facteurs différents, ce qui inclut l'évaluation du plan de données des clients, la taille de la notification et la capacité de stockage du client. Par conséquent, parfois, aucune notification ne sera envoyée à vos clients.

Ce sont des limitations imposées par Apple qui devraient être prises en compte lors de la conception de votre histoire Pushing.

### Je me suis envoyé une histoire sur iOS mais j'ai vu la vue condensée à la place

Dans certaines situations où toutes les pages ne sont pas chargées, par exemple, en raison d'une perte de connexion de données, le message Push Story n'affichera que la notification condensée.
[1]: {% image_buster /assets/img_archive/pushstories_android_preview.png %} [2]: {% image_buster /assets/img_archive/pushstories_ios_preview.png %} [3]: {% image_buster /assets/img_archive/pushstories_composer. ng %} [4]: {% image_buster /assets/img_archive/pushstories_add_pages.png %} [5]: {% image_buster /assets/img_archive/pushstories_analytics. ng %} [6]: {% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}
