---
nav_title: Créez des notifications enrichies
article_title: "Créer des notifications push riches pour iOS"
page_order: 3
page_type: tutorial
description: "Ce tutoriel décrit les conditions préalables et les étapes pour créer des notifications push riches iOS pour vos campagnes Braze."

platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# Créer des notifications push riches pour iOS

> Les notifications enrichies permettent de personnaliser davantage vos notifications push en ajoutant du contenu supplémentaire au-delà du simple texte. Les notifications Android incluent des images dans les notifications push depuis un certain temps déjà, sous la forme d'une « image de notification étendue ». À partir d'iOS 10, vos clients peuvent recevoir des notifications push iOS contenant des GIF, des images, des vidéos ou du son.

## Conditions préalables

Avant de créer une notification push riche pour iOS, prenez note des points suivants :

- Pour que votre app puisse envoyer des notifications riches, suivez les instructions d'[intégration push iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications), car votre développeur devra ajouter une extension de service à votre app.
- Les types de fichiers actuellement pris en charge pour le téléchargement direct dans notre tableau de bord sont : JPEG, PNG et GIF. Ces fichiers peuvent également être saisis dans le champ URL du modèle, avec les types de fichiers supplémentaires suivants : AIF, M4A, MP3, MP4 et WAV.
- Consultez la [documentation d'Apple](https://developer.apple.com/reference/usernotifications/unnotificationattachment) pour connaître les limites et les spécifications des médias.
- Les notifications riches iOS ne sont pas disponibles lors de la création d'une campagne push rapide.
- iOS redimensionne les images pour les adapter à l'écran et ajuste les images enrichies pour la vue active ou verrouillée.

{% alert note %}
Depuis janvier 2020, les notifications push riches iOS peuvent gérer des images de 1 038 x 1 038 pixels de moins de 10 Mo, mais nous recommandons d'utiliser des fichiers aussi légers que possible. En pratique, l'envoi de fichiers volumineux peut entraîner une surcharge inutile du réseau et rendre les délais d'expiration de téléchargement plus fréquents.
{% endalert %}

### Nombre de caractères

Bien qu'il n'existe pas de règle absolue concernant le nombre précis de caractères à inclure dans un message push, nous [proposons quelques lignes directrices]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push) à prendre en compte lors de la conception de vos messages iOS. Les résultats peuvent varier en fonction de la présence d'une image, de l'état de la notification, des paramètres d'affichage de l'appareil de l'utilisateur et de la taille de l'écran. En cas de doute, restez bref et concis.

En guise de bonne pratique, Braze recommande de limiter chaque ligne de texte, tant pour le titre facultatif que pour le corps du message, à environ 30-40 caractères dans une notification push mobile.

#### États de notification

Vos utilisateurs peuvent voir les notifications push dans différentes situations, avec des longueurs de texte variables comme suit.

<table>
<thead>
  <tr>
    <th>Écran de verrouillage ou Centre de notifications</th>
    <th>Étendu</th>
    <th>Appareil actif</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">C'est le scénario le plus courant.<br><br><b>Titre :</b> 1 ligne de texte<br><b>Corps :</b> 4 lignes de texte<br><b>Image :</b> vignette carrée</td>
    <td width="33%">Lorsqu'un utilisateur appuie longuement sur un message.<br><br><b>Titre :</b> 1 ligne de texte<br><b>Corps :</b> 7 lignes de texte<br><b>Image :</b> rapport hauteur/largeur 2:1 (recommandé, voir note ci-dessous)</td>
    <td width="33%">Lorsqu'un utilisateur reçoit une notification push alors que son téléphone est déverrouillé et actif.<br><br><b>Titre :</b> 1 ligne de texte<br><b>Corps :</b> 2 lignes de texte</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

![Exemples de notifications push affichées sur l'écran de verrouillage, en mode étendu et lorsque l'appareil est actif.]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
Même si nous recommandons un rapport hauteur/largeur de 2:1 pour les notifications push étendues, presque tous les rapports hauteur/largeur sont pris en charge. Les images couvrent toujours la largeur totale de la notification et la hauteur s'ajuste en conséquence.
{% endalert %}

#### Variables influençant la troncature du texte

Lorsque vous créez du contenu, tenez compte des scénarios suivants qui peuvent avoir un impact sur la quantité de texte affichée.

{% tabs %}
{% tab Timing %}

Selon le moment où un utilisateur interagit avec une notification push, l'horodatage peut raccourcir le texte du titre.

![Exemple de notification push avec un horodatage « maintenant » et un titre de 35 caractères.]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>Nombre de caractères du titre : **35**

![Exemple de notification push avec un horodatage « il y a 3h » et un titre de 33 caractères.]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>Nombre de caractères du titre : **33**

![Exemple de notification push avec un horodatage « hier 8 h 37 » et un titre de 22 caractères.]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>Nombre de caractères du titre : **22**

{% endtab %}
{% tab Images %}

Le corps du texte est raccourci d'environ 10 caractères par ligne lorsqu'une image est présente.

![Exemple de notification push sans image avec un corps de 179 caractères.]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>Nombre de caractères du corps : **179**

![Exemple de notification push avec une image et un corps de 154 caractères.]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>Nombre de caractères du corps : **154**

{% endtab %}
{% tab Interruption level %}

Sous iOS 15, les mentions « Time Sensitive » et « Critical » font passer le titre sur une nouvelle ligne sans l'horodatage, ce qui lui donne un peu plus d'espace.

![Exemple de notification push sans mention Time Sensitive ou Critical avec un titre de 35 caractères.]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>Nombre de caractères du titre : **35**

![Exemple de notification push avec mention Time Sensitive et un titre de 39 caractères.]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>Nombre de caractères du titre : **39**

{% endtab %}
{% tab More %}

Les éléments suivants peuvent également influencer la troncature du texte :

- **Paramètres d'affichage du téléphone :** un utilisateur peut augmenter ou réduire la taille de police globale de l'interface sur son téléphone, généralement pour des raisons d'accessibilité.
- **Largeur de l'appareil :** le message peut s'afficher sur un petit téléphone ou sur un iPad large.
- **Types de contenu :** les emojis et les caractères larges comme « m » et « w » occupent plus d'espace que « i » ou « t », et les mots longs comme « engagement » peuvent provoquer des retours à la ligne plus abrupts que les mots courts.

{% endtab %}
{% endtabs %}

## Configurer votre notification enrichie iOS

### Étape 1 : Créer une campagne de notification push

Suivez les [étapes de création de campagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) pour composer une notification push pour iOS. Vous utiliserez le même composeur que celui servant à configurer des notifications push sans contenu enrichi.

### Étape 2 : Ajouter des médias

Ajoutez votre fichier image, GIF, audio ou vidéo dans le champ **Rich Notification Media** du composeur de message. Consultez les [exigences](#requirements) pour savoir comment ajouter vos fichiers de contenu.

![Un exemple de texte récapitulatif pour une notification push.]({% image_buster /assets/img_archive/rich_notification_add_image.png %}){: style="max-width:70%;" }

Vous pouvez également limiter ce message aux seuls utilisateurs disposant d'un appareil sous iOS 10. Pour les utilisateurs qui n'ont pas mis à jour vers iOS 10, la notification apparaîtra sous forme de texte uniquement, sans le contenu enrichi, si vous laissez l'option **Only send to devices with Rich Notification support** décochée.

![La section de l'image de notification étendue dans laquelle vous pouvez ajouter une image ou saisir une URL d'image.]({% image_buster /assets/img_archive/rich_notification_ios10_select.png %}){: style="max-width:70%;" }

### Étape 3 : Poursuivre la création de votre campagne

Une fois le contenu de votre notification enrichie téléchargé sur le tableau de bord, vous pouvez poursuivre la [planification de votre campagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign).

Lorsqu'un utilisateur reçoit la notification push, il peut appuyer longuement sur le message pour développer l'image.

![Un utilisateur reçoit une notification push et appuie longuement sur le message pour afficher l'image étendue qui dit « Hello ! ».]({% image_buster /assets/img_archive/rich_notification_ios.gif %}){: style="max-width:50%;" }