---
nav_title: "Création de notifications riches"
article_title: "Créer des notifications push riches pour iOS"
page_order: 3
page_type: tutorial
description: "Ce didacticiel décrit les exigences et les étapes de la création de notifications enrichies iOS pour vos campagnes Braze."

platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# Créer des notifications push riches pour iOS

> Les notifications enrichies permettent d’obtenir plus de personnalisation dans vos notifications push en ajoutant du contenu supplémentaire en plus du texte. Les notifications Android incluent les images, appelées « images de notification étendue », dans les notifications push depuis un certain temps. À partir d’iOS 10, vos clients pourront recevoir des notifications push iOS qui incluent des GIF, des images, des vidéos ou du son.

## Conditions préalables

Avant de créer une notification push riche pour iOS, notez les détails suivants :

- Pour que votre app puisse envoyer des notifications riches, suivez les instructions d'[intégration push d'iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications), car votre développeur devra ajouter une extension de service à votre app.
- Les types de fichiers que nous prenons actuellement en charge pour le téléchargement direct dans notre tableau de bord sont les suivants : JPEG, PNG ou GIF. Ces fichiers peuvent également être saisis dans le champ URL du modèle avec ces types de fichiers supplémentaires : AIF, M4A, MP3, MP4 ou WAV.
- Reportez-vous à la [documentation d'Apple](https://developer.apple.com/reference/usernotifications/unnotificationattachment) pour connaître les limites et les spécifications des supports.
- Les notifications riches iOS ne sont pas disponibles lors de la création d'une campagne push rapide.
- iOS met à l’échelle les images pour qu’elles s’adaptent à l’écran et met à l’échelle les images enrichies pour la vue active ou verrouillée.

{% alert note %}
À compter du mois de janvier 2020, les notifications push enrichies pour iOS peuvent gérer des images de 1 038 x1 038 de moins de 10 Mo, mais nous recommandons d’utiliser des fichiers aussi petits que possible. En pratique, l’envoi de fichiers volumineux peut entraîner une surcharge inutile du réseau et rendre les échecs de téléchargement plus courants.
{% endalert %}

### Nombre de caractères

Bien que nous ne puissions pas fournir de règle absolue concernant le nombre précis de caractères à inclure dans un message, nous [vous proposons quelques lignes directrices]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/) à prendre en compte lors de la conception des messages iOS. Il peut y avoir des variations en fonction de la présence d'une image, de l'état de la notification et des paramètres d'affichage de l'appareil de l'utilisateur, ainsi que de la taille de l'appareil. En cas de doute, gardez le contenu bref et agréable.

En guise de bonne pratique, Braze recommande de limiter chaque ligne de texte, tant pour le titre optionnel que pour le corps du message, à environ 30-40 caractères dans une notification push mobile.

#### États de notification

Vos utilisateurs peuvent voir les notifications push dans différentes situations, et pourraient voir différentes longueurs de texte comme suit.

<table>
<thead>
  <tr>
    <th>Écran de verrouillage ou Centre de notification</th>
    <th>Étendu</th>
    <th>Appareil actif</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">C’est le scénario le plus courant.<br><br><b>Titre :</b> 1 ligne de texte<br><b>Corps :</b> 4 lignes de texte<br><b>Image :</b> vignette carrée</td>
    <td width="33%">Lorsqu’un utilisateur appuie longtemps sur un message.<br><br><b>Titre :</b> 1 ligne de texte<br><b>Corps :</b> 7 lignes de texte<br><b>Image :</b> Rapport hauteur/largeur 2:1 (recommandé, voir note suivante)</td>
    <td width="33%">Lorsqu’un utilisateur reçoit une notification push alors que son téléphone est déverrouillé et actif.<br><br><b>Titre :</b> 1 ligne de texte<br><b>Corps :</b> 2 lignes de texte</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

![Exemple de notifications push affichées sur l’écran de verrouillage, lorsqu’il est étendu et lorsque l’appareil est actif.]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
Même si nous recommandons un rapport hauteur/largeur de 2:1 pour les notifications push étendues, presque tous les rapports hauteur/largeur sont pris en charge. Les images couvrent toujours la largeur totale de la notification et la hauteur est ajustée en conséquence.
{% endalert %}

#### Variables dans la troncature de texte

Lorsque vous créez du contenu, tenez compte des scénarios suivants qui peuvent avoir un impact sur la quantité de texte affichée.

{% tabs %}
{% tab Timing %}

Selon le moment où un utilisateur s’engage dans une notification push, l’horodatage peut raccourcir le texte du titre.

![Exemple de notification push avec un horodatage de "now" et un titre de 35 caractères.]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>Nombre de caractères du titre : **35**

![Exemple de notification push avec un horodatage de "3h ago" et un titre de 33 caractères.]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>Nombre de caractères du titre : **33**

![Exemple de notification push avec un horodatage de "Yesterday, 8:37 AM" et un titre de 22 caractères.]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>Nombre de caractères du titre : **22**

{% endtab %}
{% tab Images %}

Le corps du texte est raccourci d’environ 10 caractères par ligne lorsqu’une image est présente.

![Exemple de notification push sans image et avec un corps de 179 caractères.]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>Nombre de caractères du corps : **179**

![Exemple de notification push avec une image et un corps de 154 caractères.]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>Nombre de caractères du corps : **154**

{% endtab %}
{% tab Niveau d'interruption %}

Dans iOS 15, les dénotations "Time Sensitive" et "Critical" font passer le titre sur une nouvelle ligne sans l'horodatage, ce qui lui donne un peu plus d'espace.

![Exemple de notification push sans indication de délai ou de criticité et avec un titre de 35 caractères.]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>Nombre de caractères du titre : **35**

![Exemple de notification push avec dénotation Temporel et un titre de 39 caractères.]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>Nombre de caractères du titre : **39**

{% endtab %}
{% tab Plus %}

Les détails suivants peuvent également avoir un impact sur la troncature du texte :

- **Paramètres d'affichage du téléphone :** un utilisateur peut augmenter ou réduire la taille de la police de l'interface utilisateur globale sur son téléphone, généralement pour des raisons d'accessibilité.
- **Largeur de l'appareil :** le message peut être affiché sur un petit téléphone ou sur un large iPad.
- **Types de contenu : les** emojis et les caractères larges comme "m" et "w" occupent plus d'espace que "i" ou "t", et les mots longs comme "engagement" peuvent s'aligner de manière plus abrupte que les mots plus courts.

{% endtab %}
{% endtabs %}

## Configurer votre notification enrichie iOS

### Étape 1 : Créer une campagne de notification push

Suivez les [étapes de la campagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) pour composer une notification push pour iOS. Vous utiliserez le même composeur utilisé pour configurer des notifications push ne contenant pas de contenu enrichi.

### Étape 2 : Ajouter des médias

Ajoutez votre fichier image, GIF, audio ou vidéo dans le champ **Rich Notification Media** dans le compositeur du message. Reportez-vous aux [exigences](#requirements) pour savoir comment ajouter vos fichiers de contenu.

![Exemple de texte de synthèse pour une notification push.]({% image_buster /assets/img_archive/rich_notification_add_image.png %}){: style="max-width:70%;" }

Vous pouvez également limiter ce message à des utilisateurs qui ont un appareil qui exécute iOS 10. Pour les utilisateurs qui ne sont pas passés à iOS 10, elle apparaîtra sous forme de notifications textuelles sans le contenu enrichi si vous ne cochez pas l'option **N'envoyer qu'aux appareils prenant en charge les notifications enrichies**.

![La section de l'image de la notification étendue où vous pouvez ajouter une image ou entrer l'URL d'une image.]({% image_buster /assets/img_archive/rich_notification_ios10_select.png %}){: style="max-width:70%;" }

### Étape 3 : Continuer à créer votre campagne

Une fois que votre contenu de notification enrichie est téléchargé sur le tableau de bord, vous pouvez continuer à [planifier votre campagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign).

Lorsqu’un utilisateur reçoit la notification push, il peut appuyer longtemps sur le message de notification push pour développer l’image.

![Un utilisateur reçoit une notification push et appuie sur le message pour afficher une image agrandie qui dit "Hello !".]({% image_buster /assets/img_archive/rich_notification_ios.gif %}){: style="max-width:50%;" }

