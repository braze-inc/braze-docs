---
nav_title: "Créer des notifications riches pour iOS"
article_title: Créer des notifications Rich Push
page_order: 3
page_type: tutoriel
description: "Ce tutoriel couvre les exigences et les étapes sur la façon de créer des notifications riches iOS pour vos campagnes de Braze."
platform: iOS
channel:
  - Pousser
tool:
  - Campagnes
---

# Créer des notifications riches iOS

> Les notifications riches permettent une plus grande personnalisation de vos notifications push en ajoutant du contenu supplémentaire au-delà de la copie. Les notifications Android ont inclus des images dans les notifications push depuis un certain temps maintenant, les messages sous forme de « Image de notification étendue». À partir d'iOS 10, vos clients pourront recevoir des notifications push iOS incluant des GIFs, des images, des vidéos ou de l'audio.

!\[Rich Not Blog\]\[7\]

## Exigences

- Pour vous assurer que votre application peut envoyer des notifications riches, veuillez suivre les instructions d'intégration [iOS push][1] , car votre développeur devra ajouter une extension de service à votre application.
- Vous devriez également référencer la documentation d' [Apple][2] pour les limitations et spécifications de médias.

> Depuis janvier 2020, les notifications iOS Rich Push peuvent gérer les images 1038x1038 tant qu'elles sont de moins de 10 Mo, mais nous vous recommandons d'utiliser un fichier aussi petit que possible. En pratique, l'envoi de fichiers volumineux peut causer des contraintes réseau inutiles et rendre les temps de téléchargement plus courants.

- iOS va mettre à l'échelle les images pour qu'elles s'adaptent à l'écran et va mettre à l'échelle les images riches pour la vue active/verrouillée.
- Les types de fichiers que nous supportons actuellement pour le téléchargement direct dans notre tableau de bord incluent JPG, PNG, ou GIF. Ces fichiers peuvent également être saisis dans le champ URL templatable avec ces types de fichiers supplémentaires : AIF, M4A, MP3, MP4 ou WAV.

### Nombre de caractères

Bien que nous ne puissions pas fournir une règle dure et rapide pour le nombre précis de caractères à inclure dans un push, nous [fournissons quelques lignes directrices]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications) à considérer lors de la conception de messages iOS. Il peut y avoir une certaine variance selon la présence d'une image, l'état de notification et le réglage d'affichage du périphérique de l'utilisateur, ainsi que la taille de l'appareil. En cas de doute, gardez-le court et sucré.

> En règle générale, Braze recommande de conserver chaque ligne de texte pour le titre et le corps du message facultatifs à environ 30-40 caractères dans une notification push mobile.

#### État des notifications

Vos utilisateurs peuvent voir les notifications push dans une variété de situations différentes, et peuvent voir différentes longueurs de texte comme suit.

<table>
<thead>
  <tr>
    <th>Verrouiller l'écran ou le centre de notification</th>
    <th>Étendu</th>
    <th>Appareil actif</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">C'est le scénario le plus courant.<br><br><b>Titre :</b> 1 ligne de texte<br><b>Corps :</b> 4 lignes de texte<br><b>Image :</b> vignette carrée</td>
    <td width="33%">Quand un utilisateur appuie longuement sur un message.<br><br><b>Titre :</b> 1 ligne de texte<br><b>Corps :</b> 7 lignes de texte<br><b>Image :</b> 2:1 rapport d'aspect (recommandé, voir la note ci-dessous)</td>
    <td width="33%">Lorsqu'un utilisateur reçoit un push tant que son téléphone est déverrouillé et actif.<br><br><b>Titre :</b> 1 ligne de texte<br><b>Corps :</b> 2 lignes de texte</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

![Exemple de notifications push pour les push affichés sur l'écran de verrouillage, lorsqu'ils sont étendus et quand l'appareil est actif]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
Bien que nous recommandions un ratio d'aspect 2:1 pour les notifications push étendues, presque tous les proportions sont prises en charge. Les images s'étendront toujours sur toute la largeur de la notification, et la hauteur sera ajustée en conséquence.
{% endalert %}

#### Variables dans la troncature du texte

Lors de la création de contenu, considérez les scénarios suivants qui peuvent avoir un impact sur la quantité de texte affichée.

{% tabs %}
{% tab Timing %}

##### Timing

Selon le moment où un utilisateur s’engage avec une notification push, l’horodatage peut raccourcir le texte du titre.

![Exemple de notification push avec un horodatage de "maintenant" et un nombre de caractères de titre de 35]({% image_buster/assets/img_archive/push_ios_timing_35.png %}) <br>Nombre de caractères de titre : **35**

![Exemple de notification push avec un horodatage de "il y a 3h" et le nombre de caractères de titre de 33]({% image_buster/assets/img_archive/push_ios_timing_33.png %}) <br>Nombre de caractères de titre : **33**

![Exemple de notification push avec un horodatage de "Hier, 8:37 AM" et un nombre de caractères de titre de 22]({% image_buster/assets/img_archive/push_ios_timing_22.png %}) <br>Nombre de caractères de titre : **22**

{% endtab %}
{% tab Images %}

##### Images

Le texte du corps est raccourci d'environ 10 caractères par ligne lorsqu'une image est présente.

![Exemple de notification push sans image et un nombre de caractères corporels de 179]({% image_buster/assets/img_archive/push_ios_images_179.png %}) <br>Nombre de caractères corporels : **179**

![Exemple de notification push avec une image et un nombre de caractères corporels de 154]({% image_buster/assets/img_archive/push_ios_images_154.png %}) <br>Nombre de caractères corporels : **154**

{% endtab %}
{% tab Interruption level %}

##### Niveau d'interruption (iOS 15)

Les dénotations sensibles au temps et critiques poussent le titre vers une nouvelle ligne sans l'horodatage, en lui donnant un peu plus d'espace.

![Exemple de notification push sans dénotation sensible au temps ou critique et un nombre de caractères de titre de 35]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %}) <br>Nombre de caractères de titre : **35**

![Exemple de notification push avec une denotation de temps sensible et un nombre de caractères de titre de 39]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %}) <br>Nombre de caractères de titre : **39**

{% endtab %}
{% tab More %}

##### Et plus encore

Le texte suivant a également un impact sur la troncation:

- **Paramètres d'affichage du téléphone :** un utilisateur peut augmenter ou diminuer la taille globale de police de l'interface utilisateur sur son téléphone, généralement pour des raisons d'accessibilité.
- **Largeur de l'appareil :** le message pourrait être affiché sur un petit téléphone ou sur un iPad large.
- **Types de contenu :** emojis et grands caractères comme "m" et "w" prennent plus d'espace que "i" ou "t", et des mots plus longs comme "engagement" peuvent enchaîner plus brusquement que des mots plus courts.

{% endtab %}
{% endtabs %}

## Configuration de votre notification enrichie iOS

### Étape 1 : Créer une campagne

Suivez les [étapes de la campagne][3] que vous faites normalement pour rédiger une notification push pour iOS. Vous utiliserez le même compositeur que vous utilisez pour configurer les notifications push qui ne contiennent pas de contenu riche.

### Étape 2 : Ajouter un média

Ajoutez votre image, GIF, audio ou vidéo dans le champ **Rich Notification Asset** dans le compositeur du message. Reportez-vous aux [exigences](#requirements) pour savoir comment ajouter vos fichiers de contenu.

!\[Add Image\]\[4\]{: style="max-width:70%;" }

Vous pouvez également limiter ce message à envoyer uniquement aux utilisateurs qui ont un appareil fonctionnant sur iOS 10. Pour les utilisateurs qui n'ont pas mis à jour vers iOS 10, il apparaîtra comme des notifications en mode texte sans le contenu riche si vous laissez la case ci-dessous décochée.

!\[Checkbox iOS 10\]\[5\]{: style="max-width:70%;" }

### Étape 3: Continuer à créer votre campagne

Une fois que votre contenu de notification enrichie est téléchargé dans le tableau de bord, vous pouvez continuer [à planifier votre campagne][6] comme vous le faites toujours.

Lorsqu'un utilisateur reçoit la notification push, il peut appuyer sur le message push pour agrandir l'image.

!\[Rich Push Example\]\[8\]{: style="max-width:50%;" }
[4]: {% image_buster /assets/img_archive/rich_notification_add_image.png %} [5]: {% image_buster /assets/img_archive/rich_notification_ios10_select. ng %} [7]: {% image_buster /assets/img_archive/RichNot_BlogImage.png %} [8]: {% image_buster /assets/img_archive/rich_notification_ios.gif %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#ios-10-rich-notifications
[2]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign
