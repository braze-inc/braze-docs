---
nav_title: "Canaux de notification"
article_title: Canaux de notification push 
page_order: 4
page_type: reference
description: "Cet article de référence couvre les sujets relatifs aux canaux de notification push Android, comme la transition vers Android O, la façon d'ajouter un canal à Braze, la définition d'un canal de repli, et plus encore."
platform: Android
channel:
  - push

---

# Canaux de notification

> Les [canaux de notification](https://www.braze.com/blog/android-o-push-notifications-channels/) sont un moyen d'organiser les notifications push qui ont été ajoutées avec Android O. À partir de O, toutes les notifications push doivent avoir un canal de communication qui indique le type de message (par exemple, "notifications de chat" ou "notifications de suivi"). Vos utilisateurs peuvent alors contrôler certains aspects de leur notification (par exemple, la sieste, les paramètres de bruit/vibration, ou l'abonnement, etc.

## Transition vers Android O

Les canaux de notification ne peuvent être créés que dans le code de votre application et ne peuvent pas être créés de manière programmatique dans le tableau de bord de Braze. Nous recommandons à votre équipe d'ingénieurs de travailler avec vos marketeurs pour s'assurer que les canaux de notification souhaités sont correctement ajoutés au tableau de bord.

À partir d'Android O, les notifications push nécessitent un canal valide pour s'afficher. Si votre application cible Android O ou une version ultérieure, vous devez utiliser la version 2.1.0 du SDK de Braze ou une version ultérieure. Votre équipe de développement doit définir les canaux que vous souhaitez utiliser ainsi que les paramètres de notification suggérés (par exemple, importance, son, lumières) pour chaque canal dans le code de votre application. Vous trouverez la documentation pour les développeurs d'Android [ici](https://developer.android.com/preview/features/notification-channels.html) et la documentation pour les développeurs de Braze [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels).

{% alert note %}
Android prend en charge la localisation des noms de canaux, de sorte que dans le code de votre application, vous pouvez associer un ID de canal à plusieurs traductions d'un nom de canal.
{% endalert %}

Une fois ces canaux créés, vos ingénieurs devront transmettre les ID de canaux associés à votre équipe marketing. Votre équipe doit saisir les noms et les ID de vos canaux dans le tableau de bord de Braze pour les utiliser dans vos campagnes et Canvases.

Pour ajouter un canal au tableau de bord de Braze, naviguez jusqu'au gestionnaire de push Android, sélectionnez le champ des canaux de notification, puis "gérer les canaux".
{% alert important %}
Seuls les utilisateurs disposant d'autorisations incluant "gérer les apps" pourront gérer les chaînes.
{% endalert %}

## Canal par défaut du SDK

Android requiert un canal valide pour afficher les notifications push au niveau 26 de l'API (Android O) ou plus tard. Le SDK Android 2.1.0 de Braze inclut un canal par défaut appelé "Général", qui sera créé et utilisé si vous ne spécifiez pas de canaux supplémentaires dans le tableau de bord ou si vous tentez d'envoyer vers un canal non valide. Vous pouvez renommer cette étiquette dans le SDK et fournir une description du canal. Nous vous recommandons d'en tenir compte pour une meilleure expérience utilisateur.  

Une fois qu'un canal est ajouté à votre application, vous pouvez choisir de le supprimer. Cependant, les consommateurs pourront toujours voir le nombre de canaux que vous avez [supprimé][3] Le tableau de bord de Braze n'inclut pas la prise en charge de la création programmatique de canaux - les canaux doivent être créés et définis dans le code de votre application afin d'offrir une expérience fluide/sans heurts.

Encore une fois, nous vous recommandons de vous coordonner avec votre équipe d'ingénieurs pour assurer une transition fluide vers le ciblage d'Android O.

## Canal de repli du tableau de bord

Braze vous permet de spécifier un canal de repli pour le tableau de bord. L'objectif du canal de repli du tableau de bord est de fournir un ID de canal pour les anciens messages push sans sélection explicite de canal. Nous définissons la sélection d'un canal comme le choix d'un canal dans notre compositeur push Android.

Les messages pour lesquels aucun canal n'a été sélectionné seront envoyés avec l'ID du canal de repli du tableau de bord. Lorsque vous modifiez le canal de secours de votre tableau de bord, tout message pour lequel aucun canal n'a été explicitement sélectionné sera envoyé avec l'ID du nouveau canal de secours.

Voici un exemple du comportement attendu du canal de repli du tableau de bord :

Le canal de repli de votre tableau de bord s'appelle "Marketing" et vous avez 10 messages push Android pour lesquels vous n'avez jamais sélectionné de canal. Ces campagnes sont envoyées par le canal "Marketing" parce que le canal "Marketing" est le canal de repli du tableau de bord.

En outre, vous avez choisi d'envoyer 15 messages par l'intermédiaire du canal "Notifications sociales" et cinq messages par l'intermédiaire du canal "Marketing".

Vous décidez ensuite de changer le canal par défaut de votre tableau de bord de "Marketing" à "Mises à jour".

Dans cette situation, les 10 campagnes sans sélection de canal qui étaient auparavant envoyées par le canal "Marketing" seront désormais envoyées par le canal "Mises à jour", car ces messages sont envoyés par le canal de repli. Les 15 messages qui étaient envoyés par le biais du canal "Notifications sociales" continueront à être envoyés par le biais du canal "Notifications sociales". Les cinq messages qui ont été envoyés par le canal "Marketing" continueront à être envoyés par le canal "Marketing".

Dans le cas où un ID de canal non valide est fourni à Braze (par exemple si vous fournissez un ID de canal que vos développeurs n'ont pas créé dans le SDK), nous transmettrons la notification par le biais du canal par défaut de votre SDK. Par conséquent, nous vous encourageons vivement à tester vos canaux de notification via le tableau de bord de Braze pendant le développement.

Pour mieux comprendre le comportement attendu des canaux, reportez-vous au tableau suivant :

|Scénario |Résultats  |    
| ---|-------------
|**La société ABC** met à jour un SDK qui prend en charge Android O.<br>L'**entreprise ABC** n'ajoute aucune chaîne au tableau de bord de Braze.<br>L'**entreprise ABC** ne renomme pas son canal par défaut SDK | Les notifications push envoyées aux appareils Android O créeront un canal appelé "Général" et les notifications seront envoyées via le canal "Général"
|L**'entreprise XYZ** met à jour un SDK qui prend en charge Android O. <br>L'**entreprise XYZ** n'ajoute aucune chaîne au tableau de bord de Braze.<br>**La société XYZ** renomme le canal par défaut de son SDK en "Marketing". | Les notifications push envoyées aux appareils Android O créeront un canal appelé "Marketing" et les notifications seront envoyées via le canal "Marketing"
|**L'entreprise LMN** met à jour un SDK qui prend en charge Android O. <br>La **société LMN** définit deux canaux dans son code d'application, "Promotions" et "Mises à jour des commandes" <br>L**'entreprise LMN** ajoute les ID des canaux "Promotions" et "Mises à jour des commandes" au tableau de bord de Braze. <br>L**'entreprise LMN** désigne "Promotions" comme canal de repli du tableau de bord.<br>L**'entreprise LMN** renomme le canal par défaut de son SDK en "Marketing" | Les notifications push envoyées aux appareils Android O ne créeront pas de canal.<br><br>À moins que le marketeur ne spécifie explicitement que les notifications doivent être envoyées par le canal "Mises à jour des commandes" ou "Marketing", toutes les notifications créées avant l'ajout de ces canaux au tableau de bord seront envoyées par le canal "Promotions"<br><br>Le canal par défaut du SDK, "Marketing", n'est créé et utilisé que si l'entreprise tente d'envoyer une notification par l'intermédiaire d'un ID de canal non valide ou si elle est explicitement sélectionnée.
|L**'entreprise HIJ** se met à jour vers Android O mais ne met pas à jour le SDK Android de Braze vers la version 2.1.0 ou une version plus récente. | Les notifications envoyées aux utilisateurs sous Android O ou version ultérieure ne s'affichent pas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ajouter des canaux au tableau de bord de Braze

1. Ouvrez n'importe quelle campagne ou Canvas qui inclut un push Android et cliquez sur **Modifier la campagne.**
2. Naviguez jusqu'au compositeur de messages push Android.
3. Cliquez sur **Gérer les canaux de notification**. Tous les canaux ajoutés ici seront disponibles globalement pour toutes les campagnes et toutes les toiles. Vous devez disposer des [autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) "Gérer les applications" pour votre espace de travail afin de gérer les canaux.

Lorsque vous appliquez un canal de notification à une campagne spécifique ou à une étape du canvas, votre nombre d'**utilisateurs joignables** (emplacement/localisation de l'étape Target Audience) pour Android Push ne semble pas changer. Cependant, seuls les utilisateurs abonnés au canal de communication sélectionné verront le message, et les analyses/analytiques de votre campagne (comme les clics) seront mesurées en fonction de cette audience.

\![]({% image_buster /assets/img_archive/Click_Here.png %})

{:start="4"}
4\. Cliquez sur **Ajouter un canal de notification**.
5\. Saisissez le nom et l'ID du canal de notification que vous souhaitez ajouter.<br><br>\![]({% image_buster /assets/img_archive/Enter_Channel.png %})<br><br>
6\. Répétez les étapes 4 et 5 pour chaque canal de notification que vous souhaitez ajouter.
7\. Appuyez sur **Enregistrer** pour enregistrer vos modifications.

## Spécifier votre canal de repli

Votre canal de repli est le canal avec lequel Braze tentera d'envoyer votre message Android si vous n'avez pas sélectionné de canal pour le message. Les seules campagnes et toiles qui auront des messages Android sans sélection de canal sont les campagnes et toiles qui ont été créées avant que votre équipe n'ajoute des canaux au tableau de bord de Braze. Si vous modifiez votre canal de repli, le changement sera appliqué globalement à toutes les campagnes et Canevas sans sélection explicite de canal.

1. Ouvrez une campagne ou un canvas existant.
2. Naviguez jusqu'au compositeur de push Android.
3. Sélectionnez **Gérer les canaux de notification** après avoir développé les options de canaux de notification. <br><br>\![]({% image_buster /assets/img_archive/Change_Fallback.png %}){: style="max-width:80%;"}<br><br>
4. Ajoutez le canal au tableau de bord (s'il n'a pas déjà été ajouté).
5. Sélectionnez la case d'option à côté du canal que vous souhaitez désigner comme canal de repli.
6. Enregistrez vos modifications. Vos modifications seront appliquées globalement.

## Ajouter des canaux à vos envois de messages sur Android

1. Naviguez vers le compositeur de push Android sur n'importe quelle campagne ou Canvas.
2. Sélectionnez le canal que vous souhaitez utiliser dans la liste déroulante. Si vous n'avez pas de liste déroulante mais plutôt la vue suivante, vous devrez ajouter des canaux avant de les sélectionner pour les campagnes.

\![]({% image_buster /assets/img_archive/No_Select.png %})

[3]: https://developer.android.com/preview/features/notification-channels.html#DeletingChannels
