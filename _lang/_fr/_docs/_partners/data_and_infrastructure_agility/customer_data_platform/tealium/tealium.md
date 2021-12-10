---
nav_title: Tealium
article_title: Tealium
page_order: 2
alias: /partners/tealium/
description: "Cet article décrit le partenariat entre Braze et Tealium, un hub de données universel qui vous permet de connecter des données mobiles, Web et alternatives à d'autres sources tierces."
page_type: partenaire
search_tag: Partenaire
---

# Tealium

> Tealium est un concentrateur de données universel et une plateforme de données client composée de EventStream, AudienceStream, et iQ Tag Management qui vous permet de connecter des données mobiles, web et alternatives provenant de sources tierces. La connexion de Tealium à Braze permet un flux de données d’événements personnalisés, d’attributs utilisateur et d’achats qui vous permettent d’agir sur vos données en temps réel.

!\[Vue d'ensemble de Tealium\]\[22\]{: style="border:0;"}

Braze offre [à la fois](#choose-your-integration-type) une intégration SDK côte à côte pour votre Android, iOS, et les applications web et une intégration de serveur à serveur pour vos services de backend afin que vous puissiez commencer à créer des profils d'utilisateurs plus riches.

## Tealium EventStream

Tealium EventStream est un concentrateur de données et d'API qui se trouve au centre de vos données. EventStream gère l'ensemble de la chaîne logistique de données depuis la configuration et l'installation jusqu'à l'identification, la validation et l'amélioration des données utilisateur entrantes. EventStream prend des actions en temps réel avec les flux d'événements et les connecteurs. Voici la liste des fonctionnalités qui composent le [EventStream](https://community.tealiumiq.com/t5/Customer-Data-Hub/Introduction-to-EventStream/ta-p/20387#toc-hId--2077371752).
- Sources de données (Installation et Collecte de données)
- Événements en direct (Inspection des données en temps réel)
- Spécifications et attributs de l'événement (Exigences de la couche de données et validation)
- Flux d'événements (Types d'événements stérilés)
- Connecteurs d'événements (API Hub Actions)

## Flux auditif de Tealium

Tealium AudienceStream est un moteur de segmentation client Omnichannel et d'action en temps réel. AudienceStream prend les données qui affluent dans EventStream et crée des profils de visiteurs qui représentent les attributs les plus importants de l'engagement de vos clients avec votre marque. Pour en savoir plus sur la façon de configurer Tealium AudienceStream, consultez notre [documentation]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium_audience_stream/).

{% alert important %}
Veuillez noter que Tealium AudienceStreams et EventStreams sont empilés selon les spécifications de Braze afin que nos clients ne courent pas le risque de dépasser la limite de taux [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Veuillez contacter le support de Braze ou votre CSM si vous avez des questions.
{% endalert %}

## Configurer la vue d'ensemble

1. Adhérer aux conditions et aux conditions préalables
2. Choisissez votre type d'intégration
4. Configurez les mappings pour votre intégration
5. [Testez votre intégration](#step-3-test-your-integration) pour vous assurer que les données s'écoulent sans problème entre Braze et Tealium

## Pré-requis

| Exigences                                            | Origine | Accès                                                                                                                              | Libellé                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Tealium & Informations sur le compte          | Tealium | [https://my.tealiumiq.com/](https://my.tealiumiq.com/)                                                                             | Vous devez avoir un compte Tealium actif avec le serveur et l'accès côté client pour utiliser leurs services avec Braze.                                                                                                                                                                                          |
| Installer les bibliothèques Source et Tealium Source | Tealium | [Librairies source de Tealium](https://community.tealiumiq.com/t5/Customer-Data-Hub/Data-Sources/ta-p/17933)                       | L'origine de toutes les données envoyées dans Tealium, telles que les applications mobiles, les sites Web ou les serveurs d'arrière-plan.<br><br>Vous devez installer les bibliothèques dans votre application, votre site ou votre serveur avant de pouvoir configurer un connecteur Tealium réussi. |
| Intégration de Braze SDK                             | Brasero | Pour plus de détails concernant les SDK de Braze, veuillez vous référer à notre documentation [iOS][1], [Android][2], et [Web][10] | Braze doit être installé avec succès sur votre application ou votre site.                                                                                                                                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Choisissez votre type d'intégration

| Intégration                                        | Détails du produit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Côte-à-côte](#side-by-side-sdk-integration)       | Carte le SDK de Tealiums vers le SDK de Braze, permettant d'accéder à des fonctionnalités plus profondes et une utilisation plus complète de Braze que l'intégration serveur-serveur.<br><br>Si vous prévoyez d'utiliser des commandes distantes de Braze, notez qu'elles ne prennent pas en charge toutes les méthodes de Braze (par exemple les cartes de contenu). Afin d'utiliser une méthode Braze qui n'est pas mappée par une commande distante correspondante, vous devrez appeler la méthode en ajoutant du code natif Braze à leur base de code. |
| [Serveur-à-Serveur](#server-to-server-integration) | Forwards data from Tealium to Braze's [users/track endpoint]({{site.baseurl}}/api/endpoints/user_data?redirected=true#user-track-endpoint).<br><br>Does __not__ support Braze UI features such as In-App Messaging, News Feed, or Push notifications. Il existe également des données capturées automatiquement (Sessions, première application utilisée, et dernière application utilisée) qui ne sont pas disponibles par cette méthode. Envisagez une intégration côte à côte si vous souhaitez utiliser ces fonctionnalités.                           |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration de SDK côte à côte

### Commandes distantes

Les commandes distantes permettent aux clients de déclencher du code dans leurs applications en utilisant un tag dans Tealium iQ Tag Management - qui collecte, contrôle et livre les données des événements à partir des applications mobiles. Les clients peuvent facilement utiliser la gestion des balises pour configurer une implémentation native de Braze sans avoir à ajouter de code spécifique au Brésil à leurs applications. À la place, le module de commande à distance de Braze installera et compilera automatiquement les bibliothèques requises de Braze. Afin d'utiliser Braze Mobile Remote Command, le client devra avoir des bibliothèques Tealium installées dans ses applications. !\[Mappings de commandes à distance\]\[23\]{: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

En utilisant des commandes distantes, les SDK Braze et Tealium travaillent en tandem permettant aux clients de faire des appels depuis le SDK Tealium - par le biais des serveurs Braze - vers Brésil. Ici, les balises de Tealium retournent à être cartographiées par le Brésil. __Le SDK Braze continuera à gérer les affichages, les renvois de messages et les analyses de messages.__

Braze Mobile Remote Command affiche les attributs par défaut des utilisateurs et les attributs personnalisés et peut suivre les achats et les événements personnalisés. Il vous permet également de suivre l'emplacement, et les données sociales sur Twitter et Facebook - comme le nombre de suiveurs ou le nombre d'amis d'un utilisateur. Consultez le graphique de commande à distance pour voir les méthodes de Braze correspondantes.

Vous pouvez trouver plus de détails sur la façon de configurer la balise de commande à distance Braze Mobile, ainsi qu'une vue d'ensemble des méthodes supportées dans les [Docs de développement de Tealium](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Mobile-Remote-Command-Tag-Setup-Guide/ta-p/32828).

{% alert important %}
Braze Mobile Remote Commands ne prend pas en charge toutes les méthodes Braze (cartes de contenu). Afin d'utiliser une méthode Braze qui n'est pas mappée à travers une commande distante correspondante, les utilisateurs devront invoquer la méthode en ajoutant du code natif Braze à leur codebase.
{% endalert%}

### Balise Braze web SDK
Le SDK Tag Web Braze est utilisé par les clients pour déployer le SDK Web de Braze sur leurs sites Web. [Tealium iQ Tag Management](https://community.tealiumiq.com/t5/iQ-Tag-Management/Introduction-to-iQ-Tag-Management/ta-p/15883) permet aux clients d'ajouter Braze en tant que Tag dans le tableau de bord de Tealium. Un tag est un snippet de code qui est placé sur un site Web pour suivre l'activité des visiteurs. Les balises sont généralement utilisées par les marketeurs pour comprendre l'efficacité de la publicité en ligne, du marketing par courriel et de la personnalisation du site. En utilisant le tag Braze Web SDK, vous pouvez avoir un aperçu de la façon dont les clients interagissent avec leurs sites Web.

#### Données dans l'intégration
Intégrez Braze dans votre application web à l'aide de Tag Manager. Afin de configurer correctement cette intégration, il y a un certain nombre d'étapes que vous devez faire pour configurer l'intégration principale. Il est donc important de pouvoir comprendre comment vous commencez à envoyer des données à Braze en configurant des événements personnalisés/attributs personnalisés.<br>

1. Configurez Braze comme un « Tag » dans votre tableau de bord de Tealium.
2. Dans la boîte de dialogue Configuration des tags, entrez votre clé API et votre point d'extrémité approprié.
  * Trouvez votre clé API et votre point de terminaison dans votre compte Braze ou confirmez-la auprès de votre gestionnaire d'intégration ou de votre représentant d'assistance.
  * Cette clé API est pour l'identifiant de l'application, plutôt que pour la clé API REST
3. Depuis le Centre de Code de Tealium, copiez le code snippet pour l'environnement que vous êtes en train de construire (dev, QA, prod) et collez-le en haut de la balise body dans votre HTML.
5. Vérifiez que le Braze SDK est en cours de chargement par Tealium en ouvrant les outils de développement du navigateur et dans la console en tapant "appboy".
  * La liste des fonctions disponibles doit alors être imprimée sur la console.

#### Personnalisation de votre intégration
Pour personnaliser votre intégration (comme la journalisation des événements personnalisés ou des attributs personnalisés), cliquez sur l'onglet de la couche de données dans votre tableau de bord de Tealium et commencez à ajouter les données personnalisées dont vous avez besoin.

* Afin que Tealium reconnaisse ces points de données, copiez et collez à nouveau le code snippet du centre de code avec le `utag_data` contenant toutes vos données.
* Pour personnaliser lorsque le Braze SDK est chargé, cliquez sur l'onglet __Charger les règles__ de votre tableau de bord de Tealium, choisissez ensuite sur quelles pages le SDK doit initialiser.

{% alert warning %}
Si la couche de données n'est pas configurée correctement, ou si vous entrez incorrectement votre [Endpoint]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), votre intégration peut échouer ou ne pas retourner des résultats corrects.
{% endalert %}

### Ressources d'intégration côte à côte
- Commande à distance iOS
    - [Documentation de Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/)
    - [Tealium Github Repository](https://github.com/Tealium/tealium-ios-braze-remote-command)<br><br>
- Commande à distance Android
    - [Documentation de Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/)
    - [Tealium Github Repository](https://github.com/Tealium/tealium-android-braze-remote-command)<br><br>
- Balise SDK Web
    - [Documentation de Tealium](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Web-SDK-Tag-Setup-Guide/ta-p/20106)

## Intégration du serveur à serveur

Cette intégration transfère les données de Tealium à l'API REST de Braze.

{% alert note %}
L'intégration Server-to-Server ne prend pas en charge ____ les fonctionnalités de Braze UI telles que la messagerie In-App, le fil d'actualités ou les notifications Push. Il existe également des données capturées automatiquement (Sessions, première application utilisée, et dernière application utilisée) qui ne sont pas disponibles par cette méthode. <br>Si vous souhaitez utiliser ces données et ces fonctionnalités, considérez notre intégration [côte à côte]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#side-by-side-sdk-integration) SDK .
{% endalert %}

### Pré-requis

| Nom                                         | Libellé                                                                                                                                                                                                                 |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clé API REST                                | Une clé API Braze REST avec les permissions `users.track`. <br><br>Ceci peut être créé dans le __tableau de bord Braze__ -> __Console développeur__ -> __Clé d'API REST__ -> __Créer une nouvelle clé API__ |
| Compte Tealium & Informations sur le compte | Vous devez avoir un compte Tealium actif avec le serveur et l'accès côté client pour utiliser leurs services avec Braze.                                                                                                |
{: .reset-td-br-1 .reset-td-br-2}

### Étape 1 : Ajouter un connecteur dans Tealium

!\[Place du Marché du Connecteur\]\[5\]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

Un connecteur est une intégration entre Tealium et un autre fournisseur qui est utilisé pour transmettre des données. Ces connecteurs contiennent des actions qui représentent les API prises en charge par le fournisseur. Nous pouvons créer un connecteur entre Tealium et Braze en localisant et en configurant le connecteur de Braze.

1. À partir de la barre latérale gauche dans Tealium sous `côté serveur`, accédez à __EventStream__ -> __Connecteurs événementiels__<br> pour les connecteurs de données des visiteurs, allez sur __AudienceStream__ -> __Connecteurs Audience__
2. Sélectionnez le bouton bleu `+ Ajouter un connecteur` pour parcourir le Marketplace du connecteur.
2. Dans la nouvelle boîte de dialogue qui apparaît, utilisez la recherche sur les projecteurs pour trouver le connecteur de Braze.
3. Pour ajouter ce connecteur, cliquez sur la tuile __du connecteur Braze__. <br>Une fois que vous avez cliqué, vous pouvez consulter le résumé de la connexion, ici Tealium fournit une liste des informations requises, des actions prises en charge et des instructions de configuration. <br><br> Cliquez sur __Continuer__ pour commencer la configuration.

### Étape 2 : Configurer les paramètres de votre connecteur

La configuration du connecteur Braze Tealium est composée de quatre étapes : Source, Configuration, Action et Résumé.

#### Étape 2: Configurer la source

Tealium nécessite que vous définissiez d'abord une source de données valide à partir de laquelle votre connecteur peut puiser.

__Configuration de votre source de données__
1. À partir de la barre latérale gauche dans Tealium sous `côté serveur`, accédez à __Sources__ -> __Sources de données__
2. Cliquez sur le bouton __+ Ajouter une source de données__
3. Localisez la plateforme __HTTP API__ dans les catagories disponibles, et nommez votre application HTTP API, c'est un champ obligatoire.<br><br>!\[Source de données\]\[6\]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
4. Dans les options __Spécifications d'événement__ , choisissez les spécifications d'événement que vous souhaitez inclure. Les spécifications de l'événement vous aident à identifier les noms d'événements et les attributs nécessaires pour suivre votre installation. Ces spécifications seront appliquées aux événements entrants. <br><br>Prenez le temps de réfléchir aux données qui vous sont les plus précieuses et aux spécifications qui vous semblent les plus appropriées pour votre cas d'utilisation. Notez que vous avez également la possibilité de créer des spécifications d'événements personnalisés, consultez la [documentation de Tealium][19] pour en savoir plus. <br><br>!\[Specs d'événements\]\[7\]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
5. Le prochain dialogue passe à l'étape __Obtenir le code__. Ceci affiche la clé source de données et le code d'installation. Le code de base et le code de suivi des événements fournis ici servent de guide d'installation. Téléchargez le PDF fourni si vous souhaitez partager ces instructions avec votre équipe. <br><br>!\[Get Code\]\[8\]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>
6. Cliquez sur __Enregistrer & Continuer__ <br><br>!\[Résumé de la source de données\]\[9\]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
7. Une fois enregistré, vous pourrez maintenant voir votre source sauvegardée ainsi que ajouter ou supprimer les spécifications d'événement. <br><br>!\[Connector\]\[18\]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>Dans la vue détaillée de la source de données, vous pouvez effectuer les actions suivantes :
- Voir et copier la clé source de données
- Voir les instructions d'installation
- Retourner à la page Obtenir le code
- Ajouter ou supprimer les spécifications de l'événement
- Voir les événements en direct liés à une spécification d'événement
- Et plus...<br><br>
8. !\[Save/Publish\]\[17\]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}Enfin, assurez-vous de sauvegarder et de publier. Si vous n'enregistrez pas et ne publiez pas votre source de données, vous ne pourrez pas la trouver lors de la configuration de votre connecteur Braze.

Pour plus d'instructions sur la configuration et l'édition de votre source de données, consultez [ici](https://community.tealiumiq.com/t5/Customer-Data-Hub/Data-Sources/ta-p/17933).

#### Étape 2b : Configurer la source du connecteur Braze

Une fois configuré, revenez au connecteur Braze et sélectionnez votre source de données.

1. Dans la liste déroulante Data Source Source, sélectionnez la source de données Braze que vous avez créée.
2. Ensuite, dans la liste déroulante Event Feed, sélectionnez une spécification d'événement que vous souhaitez configurer.
3. Nommez cette action et cliquez sur __Continuer__.

#### Etape 2c: Configuration
!\[Create Configuration\]\[15\]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

Ensuite, une boîte de dialogue __Créer la configuration__ apparaîtra. Ici, vous devez renseigner certaines valeurs demandées par Tealium et Brésil :

| Nom          | Libellé                                                                                                                                                                                                         |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nom          | Le nom du connecteur                                                                                                                                                                                            |
| Clé API REST | Une clé API Braze REST avec les permissions __users.track__. <br><br>Ceci peut être défini dans le __tableau de bord Braze -> Console développeur -> Clefs REST API -> Créer une nouvelle clé API__ |
{: .reset-td-br-1 .reset-td-br-2}

Si vous avez créé un connecteur avant, vous pouvez optionnellement utiliser un connecteur existant dans la liste disponible et le modifier pour correspondre à vos besoins avec l'icône crayon ou le supprimer avec l'icône de la corbeille.

#### Étape 2: Action

Ensuite, vous devez sélectionner une action de connecteur. Une action de connecteur envoie des données en fonction du mapping qui est configuré. Le connecteur Braze vous permet de mapper les attributs de Braze aux noms d'attributs de Tealium.

Il est également important de noter que les alias des utilisateurs peuvent être utilisés pour suivre et cibler les utilisateurs anonymes. Par exemple, une fois obtenus, ces utilisateurs peuvent recevoir des messages personnalisés qui pourraient convertir des utilisateurs potentiels en utilisateurs actifs.

1. Dans la boîte de dialogue __Ajouter une action__ , sélectionnez l'une des actions à mettre en place.
2. Selon l'action que vous avez choisie, il y aura une sélection variée de champs requis par Tealium. Voici des exemples et des explications de ces champs.

{% alert important %}
__Notez que tous les champs proposés ne sont pas obligatoires__. <br>Si vous souhaitez sauter un champ, Tealium vous demande de le minimiser avant de passer à l'étape suivante.

![Minimize]({% image_buster /assets/img/tealium/minimize.gif %}){: style="largeur-max-80%"}
{% endalert %}

{% tabs local %}
{% tab Track User %}

Cette action vous permet de suivre les attributs des utilisateurs, des événements et des achats en une seule action.

| Paramètres                              | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Identifiant de l'utilisateur            | Utilisez ce champ pour associer le champ ID de l'utilisateur de Tealium à son équivalent Braze. <br><br>- Si l'importation de Push Tokens, ID externe et ID Braze ne doit pas être spécifiée.<br>- Si vous spécifiez un alias utilisateur, le nom d'alias et l'étiquette d'alias doivent tous deux être définis. <br><br>Pour plus d'informations, consultez le Braze [/users/track endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Attributs de l'utilisateur              | Utilisez les noms de champs de profil utilisateur existants de Braze pour mettre à jour les valeurs de profil d'utilisateur dans le tableau de bord Braze ou ajoutez vos propres données d'attributs personnalisés aux profils d'utilisateurs.<br><br>- Par défaut, les nouveaux utilisateurs seront créés si on n'existe pas.<br>- En définissant `Mettre à jour uniquement` à `vrai` seuls les utilisateurs existants seront mis à jour et aucun nouvel utilisateur ne sera créé.<br><br>Pour en savoir plus sur l'objet Attributs d'utilisateur, consultez notre documentation []({{site.baseurl}}/api/objects_filters/user_attributes_object/)                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Modifier les attributs de l'utilisateur | Utilisez ce champ pour incrémenter ou décrémenter certains attributs utilisateur<br><br>- Les attributs entiers peuvent être incrémentés par des entiers positifs ou négatifs.<br>- Les attributs d'un tableau peuvent être modifiés en ajoutant ou en supprimant des valeurs des tableaux existants.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Attributs de l'événement                | Un événement représente une seule occurrence d'un événement personnalisé par un utilisateur particulier à la valeur horaire désignée. Utilisez ce champ pour suivre et cartographier les attributs d'événement comme ceux de l'objet Braze. <br><br>- Attribut d'événement `Nom` est requis pour chaque événement associé.<br>- Attribut événement `Temps` est automatiquement défini à maintenant, sauf si explicitement associé. <br>- Par défaut, de nouveaux événements seront créés si on n'existe pas. En définissant `Mettre à jour uniquement` à `true` seuls les événements existants seront mis à jour et aucun nouvel événement ne sera créé.<br>- Attributs de type tableau de carte pour ajouter plusieurs événements. Les attributs de type de tableau doivent être de longueur égale.<br>- Les attributs de valeur unique peuvent être utilisés et s'appliqueront à chaque événement.<br><br>Pour en savoir plus sur l'objet événement de Braze, consultez notre [documentation]({{site.baseurl}}/api/objects_filters/event_object/). |
| Attributs d'Achat                       | Utilisez ce champ pour suivre et cartographier les attributs d'achat des utilisateurs comme ceux de l'objet Achat Braze.<br><br>- Attributs d'achat `ID Produit`, `La devise` et `le prix` sont requis pour chaque achat cartographié.<br>- Attribut d'achat `Temps` est automatiquement réglé sur maintenant, à moins qu'il ne soit explicitement associé.<br>- Par défaut, de nouveaux achats seront créés si on n'existe pas. En définissant `Mettre à jour uniquement` à `vrai` seuls les achats existants seront mis à jour et aucun nouvel achat ne sera créé.<br>- Attributs de type Tableau de carte pour ajouter plusieurs articles d'achat. Les attributs de type de tableau doivent être de longueur égale.<br>- Les attributs de valeur unique peuvent être utilisés et s'appliqueront à chaque élément.<br><br>Pour en savoir plus sur l'objet d'achat de Braze, consultez notre [documentation]({{site.baseurl}}/api/objects_filters/purchase_object/)                                                                                 |
{: .reset-td-br-1 .reset-td-br-2}

![Suivre l'exemple d'utilisateur]({% image_buster /assets/img/tealium/track_user_example.jpg %}){: style="largeur-max-80%"}

{% endtab %}
{% tab Delete User %}

Cette action vous permet de supprimer des utilisateurs du tableau de bord Braze.

| Paramètres                   | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Identifiant de l'utilisateur | Utilisez ce champ pour associer le champ ID de l'utilisateur de Tealium à son équivalent Braze. <br><br>- Mapper un ou plusieurs identifiants d'utilisateur. Lorsque plusieurs identifiants sont spécifiés, la première valeur non vide est choisie en fonction de l'ordre de priorité suivant : ID externe, ID Braze, Nom d'alias & Étiquette d'alias.<br>- Lorsque vous spécifiez un alias utilisateur, le nom d'alias et l'étiquette d'alias doivent tous deux être définis.<br><br>Pour plus d'informations, voir le Braze [/users/delete endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/). |
{: .reset-td-br-1 .reset-td-br-2}

![Supprimer les utilisateurs]({% image_buster /assets/img/tealium/track_user_delete.png %}){: style="largeur-max-70%"}

{% endtab %}
{% endtabs %}

Sélectionnez __Continuer__.

#### Étape 2: Résumé

Ici, vous pouvez voir le résumé du connecteur que vous avez créé. Si vous souhaitez modifier les options que vous avez choisies, sélectionnez __Retour__ pour éditer ou __Terminer__ pour terminer.

!\[Connector Summary\]\[16\]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}

Votre connecteur s'affiche maintenant dans la liste des connecteurs de votre page d'accueil de Tealium.

!\[Connector\]\[13\]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}

#### Étape 2 : Enregistrer et publier
!\[Save/Publish\]\[17\]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"} Les actions que vous avez configurées vont maintenant se déclencher lorsque les connexions de déclenchement sont satisfaites. Les données se remplissent en temps réel à mesure que chaque action se déclenche.

### Étape 3 : Testez votre connecteur de Tealium

Une fois que votre connecteur est opérationnel, vous devriez le tester pour vous assurer qu'il fonctionne correctement. La façon la plus simple de tester ceci est d'utiliser le Tealium __Outil de traçage__.

1. Commencer une nouvelle trace. Cela peut être fait en sélectionnant Trace dans la barre latérale gauche dans les options `côté serveur`.
2. Examinez le journal en temps réel.
3. Vérifiez l'action que vous voulez valider en cliquant sur __Actions Déclenchées__ entrée pour développer.
4. Recherchez l'action que vous souhaitez valider et afficher le statut du journal.

Pour des instructions plus détaillées sur la façon d'implémenter l'outil Trace de Tealium, consultez leur [documentation Trace][21].

## Surcharges de données potentielles

Il y a trois moyens primaires de frapper accidentellement les dépassements de données lors de l'intégration de Braze dans Tealium :

#### __La journalisation des données est insuffisante__
Tealium n'envoie pas les deltas de Braze des attributs de l'utilisateur. Par exemple, si vous avez une action EventStream qui suit le prénom d'un utilisateur et le numéro de téléphone cellulaire, Tealium enverra les trois attributs à Braze chaque fois que l'action est déclenchée. Tealium ne cherchera pas ce qui a changé ou a été mis à jour et n'enverra que cette information.<br><br> __Solution__: <br>Vous pouvez vérifier votre propre backend pour évaluer si un attribut a changé ou non et dans l'affirmative, appeler les méthodes pertinentes de Tealiums pour mettre à jour le profil de l’utilisateur. __C'est ce que font les utilisateurs qui intègrent Braze directement.__ <br>__OR__<br> Si vous ne stockez pas votre propre version d'un profil utilisateur dans votre backend, et ne peut pas dire si les attributs changent ou pas, vous pouvez utiliser AudienceStream pour suivre les changements d'attribut utilisateur.

#### __Envoi de données non pertinentes__
Si vous avez plusieurs EventStream qui ciblent le même flux d'événement, __toutes les actions activées pour ce connecteur__ seront automatiquement déclenchées à chaque fois qu'une seule action est déclenchée, __cela pourrait aussi résulter en l'écrasement des données en Brésil. _<br><br> __Solution__: <br>Configurez une spécification d'événement séparée ou un flux pour suivre chaque action. <br>__OR__<br> Désactivez les actions (ou connecteurs) que vous ne voulez pas tirer en utilisant les commutateurs du tableau de bord de Tealium.

#### __Initialisation de Braze trop tôt__
Les utilisateurs qui intègrent Tealium à l'aide de Braze Web SDK Tag peuvent assister à une augmentation spectaculaire de leur MAU. __Si Braze est initialisé au chargement de la page, Braze créera un profil anonyme chaque fois qu'un utilisateur navigue sur le site pour la première fois.__ Certains peuvent ne vouloir suivre le comportement de l'utilisateur qu'une fois que les utilisateurs ont terminé une action, comme « Connecté » ou « Vidéo visionnée » afin de réduire leur nombre de MAU. <br><br> __Solution__: <br>Configurer des règles de charge pour déterminer exactement quand et où un Tag se charge sur votre site. Vous pouvez en savoir plus sur les règles de chargement et comment les configurer dans le [Tealium Learning Center](https://community.tealiumiq.com/t5/Customer-Data-Hub/Building-an-Audience/ta-p/11881).
[5]: {% image_buster /assets/img/tealium/braze_connector_marketplace.png %} [6]: {% image_buster /assets/img/tealium/data_source.png %} [7]: {% image_buster /assets/img/tealium/event_specs. ng %} [8]: {% image_buster /assets/img/tealium/get_code.png %} [9]: {% image_buster /assets/img/tealium/summary.png %} [13]: {% image_buster /assets/img/tealium/summary_list. ng %} [15]: {% image_buster /assets/img/tealium/create_configuration.png %} [16]: {% image_buster /assets/img/tealium/connector_summary.png %} [17]: {% image_buster /assets/img/tealium/save_publish. ng %} [18]: {% image_buster /assets/img/tealium/braze_connection.png %} [22]: {% image_buster /assets/img/tealium/tealium_overview. ng %} [23]: {% image_buster /assets/img/tealium/remote_mappings.png %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[19]: https://community.tealiumiq.com/t5/Customer-Data-Hub/Event-Specifications/ta-p/19329#toc-hId--2078027338
[21]: https://community.tealiumiq.com/t5/Customer-Data-Hub/Trace/ta-p/12058
