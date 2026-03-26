---
nav_title: "Contenu push"
article_title: Contenu push
page_order: 2
page_type: reference
description: "Le présent article de référence couvre le contenu push, comment en créer, ainsi que quelques questions fréquemment posées."
channel:
  - push

---

# Contenu push

> Le contenu push est un nouveau type de notification push introduit par Braze. Cette fonctionnalité reprend le principe du carrousel photo popularisé sur Instagram et Facebook et permet aux marketeurs de créer un carrousel de pages au sein d'une notification push pour raconter une histoire riche et cohérente. Ces pages se composent d'une image, d'une action de clic, d'un titre et d'une description. Vos utilisateurs peuvent parcourir ces pages et découvrir l'histoire telle que vous l'avez conçue.

| Exemple Android (étendu) | Exemple iOS (étendu) |
| :-----: | :----------: |
| ![]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | ![]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
À partir de la version 3.13.0 du SDK iOS, en raison d'un changement dans la manière dont le SDK télécharge les images, la miniature de la première image ne s'affiche pas dans la vue condensée de la notification push. Assurez-vous que le texte de votre message invite les utilisateurs à développer la notification push pour voir les images.
{% endalert %}

## Conditions préalables

Les versions de SDK suivantes sont requises pour recevoir du contenu push :

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## Comment utiliser le contenu push

![]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Pour utiliser le contenu push, procédez comme suit :

1. Créez une [campagne de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/).
2. Pour votre **type de notification**, sélectionnez **Push Stories**.
3. Sélectionnez **iOS** ou **Android**. Si vous sélectionnez les deux pour un message push, l'option de création d'un contenu push n'apparaîtra pas. 

### Composeur de contenu push

Pour créer une page, procédez comme suit :

1. Cliquez sur **Gérer les pages** dans le composeur principal.
    <br><br>![]({% image_buster /assets/img_archive/pushstories_add_pages.png %}){: style="max-width:70%"}<br><br>
2. Insérez une image pour chaque page, ainsi que le comportement au clic pour cette image.
3. Si vous le souhaitez, ajoutez un **titre** et une **description** pour chaque page. Si vous utilisez un titre et une description pour une page, ils doivent être renseignés pour toutes les pages.

Les aperçus sont mis à jour en temps réel et sont interactifs.

![]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
Si vous récupérez des images via du [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content), assurez-vous que l'URL de votre image commence par `https://`. L'utilisation de `http://` provoquera un plantage de votre application.
{% endalert %}

### Spécifications des images et du texte

Les spécifications suivantes en matière d'image et de texte s'appliquent à la partie carrousel photo du contenu push. Pour plus d'informations sur la notification push de base avec laquelle les utilisateurs interagissent pour activer le contenu push, consultez les [spécifications d'image et de texte pour le push]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push).

{% tabs %}
{% tab Images %}

- **Rapport d'image :** 2:1 (obligatoire)
- **Taille d'image recommandée :** 500 Ko
- **Taille maximale de l'image :** 5 Mo
- **Types de fichiers :** PNG, JPEG

{% endtab %}
{% tab Text %}

- **Titre :** 30 caractères (recommandé)
- **Description :** 30 caractères (recommandé)

{% alert note %}
Bien que la longueur des caractères puisse varier d'un appareil à l'autre, le titre et la description du contenu push sont limités à une ligne chacun. Le reste de votre message sera tronqué. Testez toujours votre message sur un appareil réel.
{% endalert %}

{% endtab %}
{% endtabs %}

### Segmentation du contenu push

Lorsque vous créez une campagne ou un Canvas, vous pouvez filtrer les utilisateurs que vous souhaitez cibler selon qu'ils ont cliqué ou non sur une page de contenu push. Sélectionnez ensuite la campagne et la page que vous souhaitez utiliser pour cibler vos utilisateurs.

### Analytique du contenu push

L'analytique est très similaire à la section analytique actuelle des notifications push. Pour l'analytique du contenu push, vous pouvez ouvrir l'indicateur **Direct Opens** pour afficher les clics par page.

![Tableau des performances de notification push iOS avec un exemple d'analytique et des détails développés pour l'indicateur Direct Opens (Ouvertures directes).]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## Résolution des problèmes

### iOS

#### Je me suis envoyé un contenu push, mais je n'ai pas reçu la notification

Apple applique des règles spécifiques qui empêchent certains types de notifications d'être envoyés à un appareil en fonction de différents facteurs, notamment le forfait de données du client, la taille de la notification et la capacité de stockage de l'appareil. Il est donc possible que certaines notifications ne soient pas délivrées à vos utilisateurs.

Il s'agit de limitations imposées par Apple à prendre en compte lors de la conception de votre contenu push.

#### Je me suis envoyé un contenu push, mais j'ai vu la vue condensée à la place

Dans certaines situations où toutes les pages ne se chargent pas (par exemple en cas de perte de connexion), le contenu push affiche uniquement la notification condensée.

### Android

#### Le contenu push ne disparaît pas après avoir cliqué sur l'image

Sur Android, le contenu push n'est pas fermé par défaut lorsqu'un utilisateur clique sur l'image. Si vous souhaitez fermer la notification, appelez [`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721).