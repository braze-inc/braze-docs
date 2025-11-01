---
nav_title: "Contenus push"
article_title: Contenus push
page_order: 2
page_type: reference
description: "Cet article de référence traite de ce que sont les contenus push, de la manière d'en créer un, ainsi que de quelques questions fréquemment posées."
channel:
  - push

---

# Contenus push

> Les contenus push sont un nouveau type de notification push introduit par Braze. Cette fonctionnalité reprend la fonctionnalité de carrousel de photos popularisée par Instagram et Facebook et permet aux marketeurs de créer un carrousel de pages au sein d'un push qui raconte une histoire riche et cohérente. Ces pages se composent d'une image, d'une action de clic, d'un titre et d'une description. Vos utilisateurs peuvent parcourir ces pages et voir l'histoire, telle que vous l'avez racontée.

| Exemple Android (étendu) | Exemple d'IOS (élargi) |
| :-----: | :----------: |
| \![]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | \![]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Sur les versions 3.13.0+ du SDK iOS, en raison d'un changement dans la façon dont le SDK télécharge les images, une vignette de la première image ne s'affiche pas sur la vue condensée du push. Veillez à ce que le texte de votre message incite les utilisateurs à développer le push pour voir les images.
{% endalert %}

## Conditions préalables

Les versions suivantes du SDK sont nécessaires pour recevoir les contenus push :

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## Comment utiliser les contenus push

\![]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Pour utiliser les contenus push, procédez comme suit :

1. Créez une [campagne de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/).
2. Pour votre **type de notification**, sélectionnez **Contenus push.**
3. Sélectionnez **iOS** ou **Android**. Notez que si vous sélectionnez les deux pour un message push, l'option de création d'un Push Story n'apparaîtra pas. 

### Compositeur de Push Story

Pour créer une page, procédez comme suit :

1. Cliquez sur **Gérer les pages** dans le compositeur principal.
    <br><br>\![]({% image_buster /assets/img_archive/pushstories_add_pages.png %}){: style="max-width:70%"}<br><br>
2. Insérez une image pour chaque page, ainsi que le comportement de clic pour cette image.
3. Si vous le souhaitez, ajoutez un **titre** et une **description** pour chaque page. Si vous utilisez un titre et une description pour une page, ils doivent être insérés pour toutes les pages.

Les aperçus seront reflétés et interactifs.

\![]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
Si vous tirez des images avec le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content), assurez-vous que l'URL de votre image commence par `https://`. L'utilisation de `http://` fera planter votre application.
{% endalert %}

### Spécifications des images et des textes

Les spécifications suivantes en matière d'image et de texte s'appliquent à la partie carrousel de photos de Push Stories. Pour plus d'informations sur le push de base avec lequel les utilisateurs interagissent pour activer la Push Story, reportez-vous aux [lignes directrices du texte pour le push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#native-mobile-push-notifications).

{% tabs %}
{% tab Images %}

- **Rapport d'image :** 2:1 (obligatoire)
- **Taille d'image recommandée :** 500 KB
- **Taille maximale de l'image :** 5 MB
- **Types de fichiers :** PNG, JPEG

{% endtab %}
{% tab Text %}

- **Titre :** 30 caractères (recommandé)
- **Description :** 30 caractères (recommandé)

{% alert note %}
Bien que la longueur des caractères puisse varier d'un appareil à l'autre, le titre et la description des contenus push sont limités à une ligne chacun. Le reste de votre message sera tronqué. Testez toujours votre message sur un appareil réel.
{% endalert %}

{% endtab %}
{% endtabs %}

### Segmentation des contenus push

Lorsque vous créez une campagne ou un Canvas, vous pouvez filtrer les utilisateurs que vous souhaitez cibler en fonction du fait qu'ils ont ou non cliqué sur une page de Push Story. Ensuite, sélectionnez la campagne et la page que vous souhaitez utiliser pour cibler vos utilisateurs.

### Analyse/analytique des contenus push (si utilisés adjectifs)

L'analyse/analytique ressemblera beaucoup à la section analytique actuelle pour les notifications push. Pour Push Stories analytics, vous pouvez ouvrir l'indicateur **Direct Opens** pour afficher les clics par page.

Tableau des performances de Push iOS avec des exemples d'analyses et des détails étendus pour l'indicateur Ouvertures directes.]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## Résolution des problèmes

### iOS

#### Je me suis envoyé un contenu push mais je n'ai pas reçu la notification.

Apple a mis en place des règles spécifiques qui empêcheront certains types de notifications d'être envoyées à un appareil en fonction d'un certain nombre de facteurs différents. Il s'agit notamment d'évaluer le plan de données des clients, la taille des notifications et la capacité de stockage des clients. Par conséquent, il arrive qu'aucune notification ne soit envoyée à vos clients.

Il s'agit de limitations imposées par Apple qui doivent être prises en compte lors de la conception de votre contenu push.

#### Je me suis envoyé un contenu push mais j'ai vu la vue condensée à la place

Dans certaines situations où toutes les pages ne se chargent pas, par exemple en raison d'une perte de connexion aux données, la Push Story n'affichera que la notification condensée.

### Android

#### Push Story ne se ferme pas après avoir cliqué sur l'image 

Par défaut, les contenus push ne sont pas rejetés sur Android après qu'un utilisateur a cliqué sur l'image. Si vous souhaitez annuler la notification, appelez le [`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721).  

