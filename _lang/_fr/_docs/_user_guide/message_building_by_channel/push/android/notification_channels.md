---
nav_title: "Chaînes de notification"
article_title: Canaux de notification Push
page_order: 4
page_type: Référence
description: "Cet article de référence couvre les sujets de la chaîne de notification Android push, comme la transition d'Android O, comment ajouter un canal à Braze, définir un canal de secours et plus encore."
platform: Android
channel:
  - Pousser
---

# Canaux de notification

> Les [canaux de notification][1] sont un moyen d'organiser les notifications push qui ont été ajoutées avec Android O. À partir de O, toutes les notifications push doivent avoir un canal de notification qui indique le type de message (par exemple, "notifications de chat" ou "suivre les notifications"). Les utilisateurs finaux peuvent ensuite contrôler les aspects de leur notification (ex: mise en veille, réglage du bruit/vibration ou opt-out, etc.) en se basant sur des canaux individuels.

## Passer à Android O

Les canaux de notification ne peuvent être créés que dans le code de votre application et ne peuvent pas être créés par programme dans le tableau de bord Braze. Nous recommandons à votre équipe d'ingénieurs de travailler avec vos marketeurs pour s'assurer que les canaux de notification désirés sont correctement ajoutés au tableau de bord.

À partir d'Android O, les notifications push nécessitent un canal valide à afficher. Si votre application cible Android O ou supérieur, vous devez utiliser Braze SDK version 2.1.0 ou supérieure. Votre équipe de développement devrait définir les canaux que vous souhaitez utiliser ainsi que les paramètres de notification suggérés (e. ., importance, son, lumières) pour chaque canal dans le code de votre application. Vous pouvez trouver la documentation des développeurs d'Android [ici][4] et la documentation des développeurs de Braze [ici.][2]

{% alert note %}
Android prend en charge la localisation des noms de chaînes, donc dans le code de votre application, vous pouvez associer un ID de canal avec plusieurs traductions du nom d'un canal.
{% endalert %}

Une fois ces canaux créés, vos ingénieurs devront transmettre les identifiants des canaux associés à votre équipe marketing. Votre équipe doit entrer les noms de vos canaux et les identifiants de vos canaux dans le tableau de bord Braze pour les utiliser dans vos campagnes et vos Canvases.

Pour ajouter un canal au tableau de bord Braze, accédez au composeur de push Android, sélectionnez le champ de canaux de notification puis sélectionnez "Gérer les canaux".
{% alert important %}
Seuls les utilisateurs ayant les autorisations qui incluent « Gérer les applications» seront en mesure de gérer les salons.
{% endalert %}

## Canal SDK par défaut

Android nécessite un canal valide pour afficher les notifications push au niveau de l'API 26 (Android O) ou supérieur. Le SDK Android 2.1 de Brase. inclut un canal par défaut appelé "Général", qui sera créé et utilisé si vous ne spécifiez pas de canaux supplémentaires dans le tableau de bord ou si vous essayez d'envoyer à un canal invalide. Vous pouvez renommer ce label dans le SDK et fournir une description du canal. Nous vous recommandons de considérer cela afin de fournir une meilleure expérience utilisateur.

Une fois qu'un canal est ajouté à votre application, vous pouvez choisir de le supprimer. Cependant, les consommateurs pourront toujours voir le nombre de canaux que vous [avez retirés.][3] Le tableau de bord de Braze n'inclut pas le support pour la création programmatique de canaux - les canaux doivent être créés et définis dans le code de votre application pour fournir une expérience transparente.

Encore une fois, nous vous recommandons de vous coordonner avec votre équipe d'ingénierie pour assurer une transition transparente vers le ciblage d'Android O.

## Canal de secours du tableau de bord

Braze vous permet de spécifier un canal de repli du tableau de bord. Le but du tableau de bord du canal de secours est de fournir un ID de canal pour les messages push hérités sans aucune sélection de canal explicite. Nous définissons une sélection de canaux comme le choix d'un canal dans notre compositeur Android push.

Les messages qui n'ont pas de canal sélectionné seront envoyés avec l'ID de canal de secours du tableau de bord. Lorsque vous changez votre tableau de bord canal de repli, tout message qui n'a pas de canal explicitement sélectionné enverra avec l'ID du nouveau canal de repli.

Voici un exemple du comportement attendu du tableau de bord du canal de secours :

Votre tableau de bord est appelé "Marketing" et vous avez 10 messages push Android pour lesquels vous n'avez jamais sélectionné de canal. Ces campagnes sont envoyées via le canal "Marketing" parce que le canal "Marketing" est le canal de repli du tableau de bord.

De plus, vous avez 15 messages que vous avez sélectionnés pour les envoyer via le canal "Notifications Sociales" et cinq messages que vous avez sélectionnés pour envoyer via le canal "Marketing".

Vous décidez ensuite de changer le canal par défaut de votre tableau de bord de "Marketing" à "Mises à jour".

Dans cette situation, toutes les 10 campagnes sans sélection de canaux qui ont été précédemment envoyés par le canal "Marketing" enverra maintenant via le canal "Mises à jour" car ces messages sont envoyés par le canal de repli. Les 15 messages qui ont été envoyés via le canal "Notifications Sociales" continueront à être envoyés via le canal "Notifications Sociales". Les cinq messages qui ont été envoyés par le canal "Marketing" continueront à être envoyés par le canal "Marketing".

Dans le cas où un ID de canal invalide est fourni à Braze (i.e. si vous fournissez un ID de canal que vos développeurs n'ont pas créé dans le SDK), nous livrerons la notification via votre canal SDK par défaut. Par conséquent, nous vous encourageons vivement à tester vos canaux de notification via le tableau de bord de Braze pendant le développement.

Pour mieux comprendre le comportement attendu pour les canaux, veuillez vous référer au tableau suivant :

| Scénario                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Résultat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **La société ABC** met à jour vers un SDK qui prend en charge Android O<br>**La société ABC** n'ajoute aucun canal au tableau de bord Braze<br>**La société ABC** ne renomme pas leur canal SDK par défaut                                                                                                                                                                                                                                                                                            | Les notifications envoyées aux appareils Android O créeront un canal appelé "Général" et les notifications seront envoyées via le canal "Général"                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **La société XYZ** se met à jour vers un SDK qui prend en charge Android O <br>**La société XYZ** n'ajoute aucun canal au tableau de bord Braze<br>**La société XYZ** renomme leur canal SDK par défaut en "Marketing"                                                                                                                                                                                                                                                                                | Les notifications envoyées aux appareils Android O créeront un canal appelé "Marketing" et les notifications seront envoyées via le canal "Marketing"                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **La société LMN** met à jour un SDK qui prend en charge Android O <br>**La société LMN** définit deux canaux dans le code de leur application, "Promotions" et "Commander Updates" <br>**La société LMN** ajoute les identifiants de canal pour les "Promotions" et les "Commandes à jour" au tableau de bord de Braze <br>**La société LMN** désigne "Promotions" comme le canal de repli du tableau de bord<br>**LMN de la société** renomme son canal de SDK par défaut à "Marketing" | Les notifications envoyées aux appareils Android O ne créeront pas de canal<br><br>sauf si le marketeur spécifie explicitement que les notifications doivent être envoyées via le canal « Commandes mises à jour» ou « Marketing», toutes les notifications créées avant que les salons aient été ajoutés au tableau de bord seront envoyées via le canal "Promotions"<br><br>Le canal SDK par défaut, Le "Marketing" n'est créé et utilisé que si l'entreprise tente d'envoyer une notification via un ID de canal invalide ou si explicitement sélectionné |
| **La société HIJ** met à jour vers Android O mais ne met pas à jour vers Braze Android SDK vers la version 2.1.0 ou supérieure                                                                                                                                                                                                                                                                                                                                                                                    | Les notifications envoyées aux utilisateurs utilisant Android O ou supérieur n'apparaissent pas                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
{: .reset-td-br-1 .reset-td-br-2}

## Ajout de salons au tableau de bord de Braze

1. Ouvrez n'importe quelle campagne ou Canvas qui inclut une poussée Android et cliquez sur **Modifier la campagne**.<br><br>
2. Naviguez vers le compositeur de message Push Android.<br><br>
3. Cliquez sur __Gérer les canaux de notification__. Notez que tous les canaux ajoutés ici seront disponibles globalement pour toutes les campagnes et Canvases et que vous devez avoir des autorisations pour « gérer les applications » pour votre groupe d'applications pour gérer les canaux.<br><br>!\[Chaînes de Notification\]\[6\]<br><br>
4.  Cliquez sur __Ajouter un canal de notification__.<br><br>
5.  Entrez le nom et l'ID du canal de notification que vous souhaitez ajouter.<br><br>!\[Enter Channel\]\[8\]<br><br>
6. Répétez les deux étapes ci-dessus pour chaque canal de notification que vous souhaitez ajouter.<br><br>
7. Appuyez sur __Save__ pour enregistrer vos modifications.

## Spécifier votre canal de secours

Votre canal de secours est le canal avec lequel Braze tentera d'envoyer votre message Android si vous n'avez pas sélectionné de canal pour le message. Les seules campagnes et Canvases qui auront des messages androïdes sans sélection de canaux sont les campagnes et les Canvases qui ont été créées avant que votre équipe n'ajoute des canaux au tableau de bord de Braze. Si vous changez votre canal de repli, le changement sera appliqué globalement à toutes les campagnes et Canvases sans sélection de canal explicite.

1. Ouvrir n'importe quelle campagne ou Canvas existante
2. Naviguez vers le compositeur Android push
3. Sélectionnez "Gérer les canaux de notifications" après avoir élargi les options du canal de notification.
4. Ajouter le salon au tableau de bord (si il n'a pas déjà été ajouté)
5. Sélectionnez la numérotation radio à côté du canal que vous souhaitez désigner comme canal de secours
6. Enregistrez vos modifications. Vos modifications seront appliquées globalement

!\[change_default\]\[9\]{: style="max-width:80%;"}

## Ajouter des canaux à vos messages push Android

* Naviguez vers le compositeur de Push Android sur n'importe quelle campagne ou Canvas

!\[choose_channel\]\[11\]

* Sélectionnez le canal que vous souhaitez utiliser dans la liste déroulante. Si vous n'avez pas de liste déroulante mais que vous avez plutôt la vue ci-dessous, vous devrez ajouter des salons avant de les sélectionner pour les campagnes

!\[no_dropdown\]\[10\]
[6]: {% image_buster /assets/img_archive/Click_Here.png %} [8]: {% image_buster /assets/img_archive/Enter_Channel.png %} [9]: {% image_buster /assets/img_archive/Change_Fallback. ng %} [10]: {% image_buster /assets/img_archive/No_Select.png %} [11]: {% image_buster /assets/img_archive/Select_Channel.png %}

[1]: https://www.braze.com/blog/android-o-push-notifications-channels/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels
[3]: https://developer.android.com/preview/features/notification-channels.html#DeletingChannels
[4]: https://developer.android.com/preview/features/notification-channels.html
