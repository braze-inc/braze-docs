---
nav_title: "Contenu push"
article_title: Contenu push
page_order: 2
page_type: reference
description: "Le présent article de référence couvre les Push Stories, comment en créer une, ainsi que quelques questions fréquemment posées."
channel:
  - push

---

# Contenu push

> Les « Push Stories » sont un nouveau type de notification push introduit par Braze. Cette fonctionnalité utilise celle de carrousel photo popularisée sur Instagram et Facebook et permet aux spécialistes du marketing de créer un carrousel de pages dans une notification push qui raconte une histoire riche et cohésive. Ces pages se composent d’une image, d’une action de clic, d’un titre et d’une description. Vos utilisateurs peuvent parcourir ces pages et afficher l’histoire telle que vous l’avez racontée.

| Exemple Android (étendu) | Exemple iOS (étendu) |
| :-----: | :----------: |
| ![]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | ![]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Sur les SDK iOS versions 3.13.0 et ultérieures, en raison d’un changement dans la manière dont le SDK télécharge les images, une miniature de la première image ne s’affichera pas sur la vue condensée de la notification push. Assurez-vous que le texte de votre message invite les utilisateurs à étendre la notification push pour voir les images.
{% endalert %}

## Conditions préalables

Les versions SDK suivantes sont requises pour recevoir les Push Stories :

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## Comment utiliser les Push Stories

![]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Pour utiliser les contenus push, procédez comme suit :

1. Créez une [campagne de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/).
2. Pour votre **type de notification**, sélectionnez **Contenus push.**
3. Sélectionnez **iOS** ou **Android**. Notez que si vous sélectionnez les deux pour un message push, l'option de création d'un Push Story n'apparaîtra pas. 

### Composeur de Push Story

Pour créer une page, procédez comme suit :

1. Cliquez sur **Gérer les pages** dans le compositeur principal.
    <br><br>![]({% image_buster /assets/img_archive/pushstories_add_pages.png %}){: style="max-width:70%"}<br><br>
2. Insérez une image pour chaque page, ainsi que le comportement lors du clic pour cette image.
3. Si vous le souhaitez, ajoutez un **titre** et une **description** pour chaque page. Si vous utilisez un titre et une description pour une page, ils doivent être insérés pour toutes les pages.

Les aperçus seront reflétés et interactifs.

![]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
Si vous importez des images avec un [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content), assurez-vous que l'URL de votre image commence par `https://`. Utiliser `http://` fera planter votre application.
{% endalert %}

### Spécifications de l’image et du texte

Les spécifications suivantes en matière d'image et de texte s'appliquent à la partie carrousel de photos de Push Stories. Pour plus d'informations sur le push de base avec lequel les utilisateurs interagissent pour activer la Push Story, reportez-vous aux [lignes directrices du texte pour le push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#native-mobile-push-notifications).

{% tabs %}
{% tab Images %}

- **Rapport d'image :** 2:1 (obligatoire)
- **Taille d'image recommandée :** 500 KB
- **Taille maximale de l'image :** 5 MB
- **Types de fichiers :** PNG, JPEG

{% endtab %}
{% tab Texte %}

- **Titre :** 30 caractères (recommandé)
- **Description :** 30 caractères (recommandé)

{% alert note %}
Bien que la longueur des caractères puisse varier d'un appareil à l'autre, le titre et la description des contenus push sont limités à une ligne chacun. Le reste de votre message sera tronqué. Testez toujours votre message sur un appareil réel.
{% endalert %}

{% endtab %}
{% endtabs %}

### Segmentation de la Push Story

Lorsque vous créez une campagne ou un Canvas, vous pouvez filtrer les utilisateurs que vous souhaitez cibler selon qu’ils ont cliqué sur une page de Push Story. Sélectionnez ensuite la campagne et la page que vous souhaitez utiliser pour cibler vos utilisateurs.

### Analytique des Push Stories

L’analytique sera très similaire à la section analytique actuelle pour les notifications push. Pour Push Stories analytics, vous pouvez ouvrir l'indicateur **Direct Opens** pour afficher les clics par page.

![Tableau iOS Push Performance avec des exemples d'analyses/analytiques et des détails étendus pour l'indicateur Direct Opens.]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## Résolution des problèmes

### iOS

#### Je me suis envoyé une Push Story, mais je n’ai pas reçu la notification.

Apple a mis en place des règles spécifiques qui empêcheront certains types de notifications d’être envoyés à un appareil sur la base d’un certain nombre de facteurs différents. Cela inclut l’évaluation du plan de données des clients, la taille de la notification et la capacité de stockage des clients. Par conséquent, les notifications ne seront parfois pas envoyées à vos clients.

Il s’agit des limitations imposées par Apple qui doivent être prises en compte lors de la conception de votre Push Story.

#### Je me suis envoyé une Push Story, mais j’ai reçu la vue condensée à la place.

Dans certaines situations où toutes les pages ne sont pas chargées, par exemple en raison d’une perte de connexion aux données, la Push Story affichera uniquement la notification condensée.

### Android

#### La Push Story ne disparaît pas après avoir cliqué sur l’image. 

Sur Android, les Push Stories ne sont pas enlevées par défaut après qu’un utilisateur ait cliqué sur l’image. Si vous souhaitez fermer la notification, appelez [`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721).  

