---
nav_title: "Créer des notifications enrichies iOS"
article_title: Créer des notifications push enrichies
page_order: 3
page_type: tutorial
description: "Ce didacticiel décrit les exigences et les étapes de la création de notifications enrichies iOS pour vos campagnes Braze."

platform: iOS
channel:
  - Notification push
tool:
  - Campaigns

---

# Créer des notifications enrichies iOS

> Les notifications enrichies permettent d’obtenir plus de personnalisation dans vos notifications push en ajoutant du contenu supplémentaire en plus du texte. Les notifications Android incluent les images, appelées « images de notification étendue », dans les notifications push depuis un certain temps. À partir d’iOS 10, vos clients pourront recevoir des notifications push iOS qui incluent des GIF, des images, des vidéos ou du son.

## Conditions

- Pour que votre application puisse envoyer des notifications enrichies, suivez les instructions d’[intégration des notifications push iOS][1], car votre développeur devra ajouter une extension de service à votre application.
- Vous devez également vous reporter à la [documentation d’Apple][2] pour les limitations et les spécifications des médias.

> À compter du mois de janvier 2020, les notifications push enrichies pour iOS peuvent gérer des images de 1 038 x1 038 tant que leur taille est inférieure à 10 Mo, mais nous recommandons d’utiliser des fichiers aussi petits que possible. En pratique, l’envoi de fichiers volumineux peut entraîner une surcharge inutile du réseau et rendre les échecs de téléchargement plus courants.

- iOS met à l’échelle les images pour qu’elles s’adaptent à l’écran et met à l’échelle les images enrichies pour la vue active ou verrouillée.
- Les types de fichiers que nous prenons actuellement en charge pour le téléchargement direct dans notre tableau de bord sont JPG, PNG ou GIF. Ces fichiers peuvent également être saisis dans le champ URL du modèle avec ces types de fichiers supplémentaires : AIF, M4A, MP3, MP4 ou WAV.

### Nombre de caractères

Bien que nous ne puissions pas fournir une règle stricte concernant le nombre précis de caractères à inclure dans une notification push, nous [fournissons quelques directives]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications) à prendre en compte lors de la conception de messages iOS. Il peut y avoir une variation en fonction de la présence d’une image, de l’état de la notification et du réglage d’affichage de l’appareil de l’utilisateur, ainsi que de sa taille. En cas de doute, gardez le contenu bref et agréable.

> En règle générale, Braze recommande de limiter chaque ligne de texte, aussi bien pour le titre facultatif que pour le corps du message, à environ 30-40 caractères dans une notification push mobile.

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
    <td width="33%">C’est le scénario le plus courant.<br><br><b>Titre :</b> 1 ligne de texte<br><b>Corps :</b> 4 lignes de texte<br><b>Image :</b> vignette carrée</td>
    <td width="33%">Lorsqu’un utilisateur appuie longtemps sur un message.<br><br><b>Titre :</b> 1 ligne de texte<br><b>Corps :</b> 7 lignes de texte<br><b>Image :</b> rapport d’aspect 2:1 (recommandé, voir la remarque suivante)</td>
    <td width="33%">Lorsqu’un utilisateur reçoit une notification push alors que son téléphone est déverrouillé et actif.<br><br><b>Titre :</b> 1 ligne de texte<br><b>Corps :</b> 2 lignes de texte</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

![Exemple de notifications push affichées sur l’écran de verrouillage, lorsqu’il est étendu et lorsque l’appareil est actif.]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
Même si nous recommandons un rapport de largeur 2:1 pour les notifications push étendues, presque tous les rapports de largeur sont pris en charge. Les images couvrent toujours la largeur totale de la notification et la hauteur est ajustée en conséquence.
{% endalert %}

#### Variables dans la troncature de texte

Lorsque vous créez du contenu, tenez compte des scénarios suivants qui peuvent avoir un impact sur la quantité de texte affichée.

{% tabs %}
{% tab Timing %}

##### Timing

Selon le moment où un utilisateur s’engage dans une notification push, l’horodatage peut raccourcir le texte du titre.

![Exemple de notification push avec un horodatage « maintenant » et un titre de 35 caractères.]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>Nombre de caractères du titre : **35**

![Exemple de notification push avec un horodatage « il y a 3h » et un titre de 33 caractères.]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>Nombre de caractères du titre : **33**

![Exemple de notification push avec un horodatage « hier 8 h 37 » et un titre de 22 caractères.]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>Nombre de caractères du titre : **22**

{% endtab %}
{% tab Images %}

##### Images

Le corps du texte est raccourci d’environ 10 caractères par ligne lorsqu’une image est présente.

![Exemple de notification push sans image et un corps de 179 caractères.]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>Nombre de caractères du corps : **179**

![Exemple de notification push avec une image et un corps de 154 caractères.]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>Nombre de caractères du corps : **154**

{% endtab %}
{% tab Interruption level %}

##### Niveau d’interruption (iOS 15)

Les dénotations Time Sensitive (Temporel) et Critical (Critique) poussent le titre vers le bas sur une nouvelle ligne sans l’horodatage, lui donnant ainsi un peu plus d’espace.

![Exemple de notification push sans dénotation Temporel ou Critique et un titre de 35 caractères.]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>Nombre de caractères du titre : **35**

![Exemple de notification push avec dénotation Temporel et un titre de 39 caractères.]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>Nombre de caractères du titre : **39**

{% endtab %}
{% tab More %}

##### Et plus encore

Les éléments suivants ont également un impact sur la troncature de texte :

- **Phone display settings (Paramètres d’affichage du téléphone) :** un utilisateur peut augmenter ou diminuer la taille de police de l’interface utilisateur globale sur son téléphone, généralement pour des raisons d’accessibilité.
- **Device width (Largeur de l’appareil) :** le message peut être affiché sur un petit téléphone ou sur un iPad.
- **Content types (Types de contenu) :** les émojis et les caractères larges comme « m » et « w » prennent plus d’espace que « i » ou « t », et les mots plus longs comme « engagement » peuvent créer une nouvelle ligne par rapport aux mots plus courts.

{% endtab %}
{% endtabs %}

## Configurer votre notification enrichie iOS

### Étape 1 : Créer une campagne

Suivez les [étapes de campagne][3] pour composer une notification push pour iOS. Vous utiliserez le même composeur utilisé pour configurer des notifications push ne contenant pas de contenu enrichi.

### Étape 2 : Ajouter des médias

Ajoutez votre fichier image, GIF, audio ou vidéo dans le champ **Rich Notification Media (Média de notification enrichie)** dans le composeur du message. Reportez-vous aux [exigences](#requirements) pour ajouter vos fichiers de contenu.

![][4]{: style="max-width:70%;" }

Vous pouvez également limiter ce message à des utilisateurs qui ont un appareil qui exécute iOS 10. Pour les utilisateurs qui n’ont pas effectué la mise à niveau vers iOS 10, les notifications apparaîtront sous forme de texte seul, sans le contenu enrichi, si vous ne cochez pas la case **Envoyer uniquement aux appareils prenant en charge les notifications enrichies**.

![][5]{: style="max-width:70%;" }

### Étape 3 : Continuer à créer votre campagne

Une fois que votre contenu de notification enrichie est téléchargé sur le tableau de bord, vous pouvez continuer à [planifier votre campagne][6].

Lorsqu’un utilisateur reçoit la notification push, il peut appuyer longtemps sur le message de notification push pour développer l’image.

![Un utilisateur reçoit une notification push et appuie longtemps sur le message pour afficher l’image étendue qui dit « Hello ».][8]{: style="max-width:50%;" }

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#ios-10-rich-notifications
[2]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[4]: {% image_buster /assets/img_archive/rich_notification_add_image.png %}
[5]: {% image_buster /assets/img_archive/rich_notification_ios10_select.png %}
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign
[8]: {% image_buster /assets/img_archive/rich_notification_ios.gif %}
