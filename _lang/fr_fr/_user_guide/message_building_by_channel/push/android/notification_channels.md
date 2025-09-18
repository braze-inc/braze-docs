---
nav_title: "Canaux de notification"
article_title: Canaux de notification push 
page_order: 4
page_type: reference
description: "Le présent article de référence couvre les sujets des canaux de notification push Android comme la transition vers Android O, comment ajouter un canal à Braze, définir un canal de secours, etc."
platform: Android
channel:
  - push

---

# Canaux de notification

> Les [canaux de notification](https://www.braze.com/blog/android-o-push-notifications-channels/) sont un moyen d'organiser les notifications push qui ont été ajoutées avec Android O. À partir de O, toutes les notifications push doivent avoir un canal de communication qui indique le type de message (par exemple, "notifications de chat" ou "notifications de suivi"). Vos utilisateurs peuvent alors contrôler certains aspects de leur notification (par exemple, les paramètres de veille, de bruit ou de vibration, de désabonnement, etc.) en fonction des différents canaux.

## Transition vers Android O

Les canaux de notification ne peuvent être créés que dans le code de votre application et ne peuvent pas être créés de façon programmatique dans le tableau de bord de Braze. Nous recommandons à votre équipe d’ingénierie de travailler avec vos spécialistes du marketing pour vous assurer que les canaux de notification souhaités sont correctement ajoutés au tableau de bord.

Depuis Android O, les notifications push nécessitent un canal valide pour s’afficher. Si votre application cible Android O ou ultérieur, vous devez utiliser le SDK Braze version 2.1.0 ou ultérieur. Votre équipe de développement doit définir les canaux que vous souhaitez utiliser ainsi que les paramètres de notification suggérés (par exemple, importance, son, lumières) pour chaque canal dans le code de votre application. Vous trouverez la documentation pour les développeurs d'Android [ici](https://developer.android.com/preview/features/notification-channels.html) et la documentation pour les développeurs de Braze [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels).

{% alert note %}
Android prend en charge la localisation pour les noms de canaux. Ainsi, dans le code de votre application, vous pouvez associer un ID de canal avec plusieurs traductions d’un nom de canal.
{% endalert %}

Une fois ces canaux créés, vos ingénieurs devront transmettre les ID de canal associées à votre équipe marketing. Votre équipe doit saisir les noms de canal et les ID de canal dans le tableau de bord de Braze pour les utiliser dans vos campagnes et vos Canvas.

Pour ajouter un canal au tableau de bord de Braze, accédez au composeur de notification push Android, sélectionnez le champ de canaux de notification, puis sélectionnez Gérer les canaux.
{% alert important %}
Seuls les utilisateurs disposant d’autorisations qui incluent « gérer les applications » pourront gérer les canaux.
{% endalert %}

## Canal par défaut du SDK

Android nécessite un canal valide pour afficher des notifications push sur l’API de niveau 26 (Android O) ou ultérieur. Le SDK Android 2.1.0 de Braze inclut un canal par défaut appelé "Général", qui sera créé et utilisé si vous ne spécifiez pas de canaux supplémentaires dans le tableau de bord ou si vous tentez d'envoyer vers un canal non valide. Vous pouvez renommer cette étiquette dans le SDK et fournir une description du canal. Nous vous recommandons d’envisager de le faire pour offrir une meilleure expérience utilisateur.  

Une fois qu’un canal est ajouté à votre application, vous pouvez choisir de le supprimer. Cependant, les consommateurs pourront toujours voir le nombre de canaux que vous avez [supprimé].[3] Le tableau de bord de Braze n'inclut pas la prise en charge de la création programmatique de canaux - les canaux doivent être créés et définis dans le code de votre application pour offrir une expérience fluide.

Encore une fois, nous vous recommandons de vous coordonner avec votre équipe d’ingénierie afin de garantir une transition sans heurt vers le ciblage d’Android O.

## Canal de secours du tableau de bord

Braze vous permet de spécifier un canal de secours du tableau de bord. L’objectif du canal de secours du tableau de bord est de fournir un ID de canal pour les messages de notification push hérités sans sélection de canal explicite. Nous définissons une sélection de canaux comme choisir un canal dans notre composeur de notification push Android.

Les messages qui n’ont pas de canal sélectionné seront envoyés avec l’ID de canal de secours du tableau de bord. Lorsque vous modifiez le canal de secours de votre tableau de bord, tout message qui n’a pas de canal explicitement sélectionné sera envoyé avec l’ID du nouveau canal de secours.

Voici un exemple du comportement attendu du canal de secours du tableau de bord :

Le canal de secours de votre tableau de bord s’appelle « Marketing » et vous disposez de 10 messages de notification push Android pour lesquels vous n’avez jamais sélectionné de canal. Ces campagnes sont envoyées via le canal « Marketing » car celui-ci est le canal de secours du tableau de bord.

De plus, vous avez 15 messages que vous avez sélectionnés pour être envoyés via le canal « Notifications sociales » et cinq messages que vous avez sélectionnés pour être envoyés via le canal « Marketing ».

Vous décidez ensuite de modifier le canal par défaut de votre tableau de bord de « Marketing » pour « Mises à jour ».

Dans cette situation, les 10 campagnes sans sélection de canal précédemment envoyées sur le canal « Marketing » vont maintenant être envoyées via le canal « Mises à jour », car ces messages sont envoyés par le canal de secours. Les 15 messages qui étaient envoyés sur le canal « Notifications sociales » continueront à être envoyés via celui-ci. Les cinq messages qui étaient envoyés sur le canal « Marketing » continueront à être envoyés via celui-ci.

Dans le cas où un ID de canal non valide est fourni à Braze (par exemple si vous fournissez un ID de canal que vos développeurs n'ont pas créé dans le SDK), nous distribuerons la notification par le biais du canal par défaut de votre SDK. Par conséquent, nous vous encourageons vivement à tester vos canaux de notification à l’aide du tableau de bord de Braze au cours du développement.

Pour mieux comprendre le comportement attendu pour les canaux, reportez-vous au tableau suivant :

|Scénario |Résultat  |    
| ---|-------------
|La **société ABC** procède à une mise à jour vers un SDK qui prend en charge Android O<br>La **société ABC** n'ajoute aucun canal au tableau de bord de Braze<br>La **société ABC** ne renomme pas le canal par défaut de son SDK | Les notifications push envoyées aux appareils Android O créeront un canal appelé « Général » et les notifications seront envoyées via ce canal
|La **société XYZ** procède à une mise à jour vers un SDK qui prend en charge Android O <br>La **société XYZ** n'ajoute aucun canal au tableau de bord de Braze<br>La **société XYZ** renomme le canal par défaut de son SDK en « Marketing » | Les notifications push envoyées aux appareils Android O créeront un canal appelé « Marketing » et les notifications seront envoyées via ce canal
|La **société LMN** procède à une mise à jour vers un SDK qui prend en charge Android O <br>La **société LMN** définit deux canaux dans son code d'application, "Promotions" et "Mises à jour des commandes" <br>**L'entreprise LMN** ajoute les ID des canaux "Promotions" et "Mises à jour des commandes" au tableau de bord de Braze. <br>La **société LMN** désigne « Promotions » comme canal de secours du tableau de bord<br>La **société LMN** renomme le canal par défaut de son SDK en « Marketing » | Les notifications push envoyées aux appareils Android O ne créeront pas de canal<br><br>Toutes les notifications créées avant que les canaux ne soient ajoutés au tableau de bord seront envoyées par le canal « Promotions » à moins que le spécialiste du marketing ne spécifie explicitement que les notifications doivent être envoyées avec le canal « Mises à jour des commandes » ou « Marketing »<br><br>Le canal par défaut du SDK, « Marketing » est créé et utilisé uniquement si la société essaie d’envoyer une notification à l’aide d’un ID de canal non valide ou s’il est sélectionné explicitement
|**L'entreprise HIJ** se met à jour vers Android O mais ne met pas à jour le SDK Android de Braze vers la version 2.1.0 ou une version plus récente. | Les notifications envoyées aux utilisateurs exécutant Android O ou ultérieur n’apparaissent pas |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ajouter des canaux au tableau de bord de Braze

1. Ouvrez n'importe quelle campagne ou n’importe quel canvas qui inclut une notification push Android et cliquez sur **Modifier la campagne**.
2. Accédez au composeur de messages de notification push Android.
3. Cliquez sur **Gérer les canaux de notification**. Tous les canaux ajoutés ici seront disponibles globalement pour toutes les campagnes et les Canvas. Vous devez disposer des [autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) "Gérer les applications" pour votre espace de travail afin de gérer les canaux.

Lorsque vous appliquez un canal de notification à une campagne spécifique ou à une étape du canvas, votre nombre d'**utilisateurs joignables** (emplacement/localisation de l'étape Target Audience) pour Android Push ne semble pas changer. Cependant, seuls les utilisateurs abonnés au canal de communication sélectionné verront le message, et les analyses/analytiques de votre campagne (comme les clics) seront mesurées en fonction de cette audience.

![]({% image_buster /assets/img_archive/Click_Here.png %})

{:start="4"}
4\. Cliquez sur **Ajouter un canal de notification**.
5\. Saisissez le nom et l’ID du canal de notification que vous souhaitez ajouter.<br><br>![]({% image_buster /assets/img_archive/Enter_Channel.png %})<br><br>
6\. Répétez les étapes 4 et 5 pour chaque canal de notification que vous souhaitez ajouter.
7\. Appuyez sur **Enregistrer** pour enregistrer vos modifications.

## Spécifier votre canal de secours

Votre canal de repli est le canal avec lequel Braze tentera d'envoyer votre message Android si vous n'avez pas sélectionné de canal pour le message. Les seules campagnes et toiles qui auront des messages Android sans sélection de canal sont les campagnes et toiles qui ont été créées avant que votre équipe n'ajoute des canaux au tableau de bord de Braze. Si vous modifiez votre canal de secours, le changement sera appliqué à l’échelle globale à toutes les campagnes et à tous les Canvas n’ayant pas de sélection explicite de canal.

1. Ouvrir toute campagne ou Canvas existant.
2. Accédez au composeur de notification push Android.
3. Sélectionnez **Gérer les canaux de notification** après avoir développé les options de canaux de notification. <br><br>![]({% image_buster /assets/img_archive/Change_Fallback.png %}){: style="max-width:80%;"}<br><br>
4. Ajoutez le canal au tableau de bord (s’il n’a pas encore été ajouté).
5. Sélectionnez le cadran radio à côté du canal que vous souhaitez désigner comme canal de secours.
6. Enregistrez vos modifications. Vos modifications seront appliquées à l’échelle globale.

## Ajouter des canaux à vos messages de notification push Android

1. Accédez au composeur de notification push Android sur n’importe quelle campagne ou Canvas.
2. Sélectionnez le canal que vous souhaitez utiliser dans la liste déroulante. Si vous n’avez pas de liste déroulante mais que vous avez la vue suivante, vous devrez ajouter des canaux avant de les sélectionner pour les campagnes.

![]({% image_buster /assets/img_archive/No_Select.png %})

[3]: https://developer.android.com/preview/features/notification-channels.html#DeletingChannels
