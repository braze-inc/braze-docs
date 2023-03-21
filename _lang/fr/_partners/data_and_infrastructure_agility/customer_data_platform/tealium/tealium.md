---
nav_title: Tealium
article_title: Tealium
page_order: 2
alias: /partners/tealium/
description: "Cet article de référence présente le partenariat entre Braze et Tealium, un hub de données universel qui vous permet de connecter des données mobiles, Web ou autres à d’autres sources tierces."
page_type: partner
search_tag: Partenaire

---

# Tealium

> [Tealium](https://tealium.com/) est une plateforme de données client et un hub de données universel composé d’EventStream, AudienceStream et iQ Tag Management, qui vous permet de connecter des données mobiles, Web ou autres à des sources tierces. La connexion de Tealium à Braze permet de configurer un flux de données d’événements personnalisés, d’attributs utilisateur et d’achats qui vous permet d’agir en temps réel en fonction de vos données.

![Un graphique de présentation de Tealium montrant comment la plateforme Braze et les différents produits Tealium s’associent pour vous permettre de lancer des campagnes cross-canal en temps réel.][22]{: style="border:0;"}

L’intégration de Braze et de Tealium vous permet de suivre vos utilisateurs et de transmettre des données à de nombreux fournisseurs d’analyse des utilisateurs. Tealium vous permet de :
- Synchroniser les audiences Tealium avec [AudienceStream]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/) sur Braze pour personnaliser des campagnes et des Canvas Braze ou créer des segments.
- [Importer des données sur plusieurs plateformes](#choose-your-integration-type). Braze offre à la fois une intégration SDK [côte à côte](#side-by-side-sdk-integration) pour vos applications Android, iOS et Web, et une intégration [serveur à serveur](#server-to-server-integration) qui peuvent être utilisées avec toutes les plateformes pouvant fournir des données d’événements.<br><br>

{% tabs %}
{% tab EventStream %}
Tealium EventStream est un hub de collecte de données et d’API qui se situe au cœur de vos données. EventStream gère l’ensemble de la chaîne d’approvisionnement des données, de la configuration à l’amélioration des données utilisateur entrantes, en passant par l’installation, l’identification et la validation des données. EventStream prend des mesures en temps réel avec les flux et les connecteurs d’événements. Les fonctionnalités d’[EventStream](https://community.tealiumiq.com/t5/Customer-Data-Hub/Introduction-to-EventStream/ta-p/20387#toc-hId--2077371752) sont présentées ci-dessous.
- Sources de données (installation et collecte de données)
- Événements en direct (inspection des données en temps réel)
- Spécifications et attributs d’événements (exigences et validation de la couche de données)
- Flux d’événements (types d’événements filtrés)
- Connecteurs d’événements (actions du hub d’API)

{% endtab %}
{% tab AudienceStream %}

Tealium AudienceStream est un moteur de segmentation client omnicanal et d’action en temps réel. AudienceStream extrait les données qui affluent dans EventStream et crée des profils de visiteurs qui représentent les attributs les plus importants concernant l’engagement de vos clients envers votre marque. Consultez notre article sur [AudienceStream]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/) pour découvrir les étapes de configuration.

{% endtab %}
{% tab iQ Tag Management %}
Tealium iQ vous permet de déclencher du code dans vos applications en utilisant une balise de l’interface de gestion des balises Tealium iQ. Cette balise collecte, contrôle et fournit des données d’événements issues des plateformes mobiles et Web pour vous permettre de configurer une implémentation native de Braze sans ajouter de code spécifique à Braze dans vos applications. Les utilisateurs peuvent choisir d’intégrer des commandes mobiles à distance via les fichiers de l’interface de gestion des balises iQ ou de JSON (approche recommandée par Tealium). Les utilisateurs utilisant le SDK Web de Braze doivent s’intégrer via la balise Web iQ.

Pour en savoir plus sur les avantages et les inconvénients de chaque méthode, reportez-vous à la section [Gestionnaire de balises Tealium iQ](#mobile-remote-commands).
{% endtab %}
{% endtabs %}

{% alert important %}
Tealium propose des actions de connecteur liées ou non à des lots. Le connecteur sans lots doit être utilisé lorsque des demandes en temps réel sont importantes pour le cas d’utilisation et qu’il n’y a aucun risque d’atteindre la limite de débit d’API de Braze. Si vous avez des questions, contactez le service d’assistance de Braze ou votre gestionnaire du succès des clients.<br><br>

Pour les connecteurs de lots, les requêtes sont placées en file d’attente jusqu’à ce que l’un des seuils suivants soit atteint :
- Nombre maximum de requêtes : 75
- Durée max. depuis la requête la plus ancienne : 10 minutes
- Taille maximale des requêtes : 1 Mo

Tealium ne regroupe pas les événements de consentement (préférences d’abonnement) ou les événements de suppression d’utilisateurs par défaut.
{% endalert %}

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Tealium | Un [compte Tealium](https://my.tealiumiq.com/) avec un accès au serveur et/ou un accès côté client est nécessaire pour profiter de ce partenariat. | 
| [Bibliothèques](https://community.tealiumiq.com/t5/Customer-Data-Hub/Data-Sources/ta-p/17933) de la source installée et de la source Tealium | L’origine de toutes les données envoyées dans Tealium, telles que des applications mobiles, des sites Web ou des serveurs de back-end.<br><br>Vous devez installer les bibliothèques dans votre application, votre site ou votre serveur avant de pouvoir configurer un connecteur Tealium. |
| Endpoint et SDK et d’API REST Braze | L’URL de votre endpoint REST ou SDK. Votre endpoint dépendra de l’[URL Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints). |
| Clé d’identification de l’application Braze (intégration côte à côte uniquement) | Votre clé d’identification de l’application. <br><br>Vous pouvez y trouver ce que vous pouvez trouver dans le **Tableau de bord de Braze > Manage Settings (Gérer les paramètres) > API Key (Clé API)**. |
| Version du code (intégration côte à côte uniquement) | Correspond à la version du SDK et doit être au format majeur/mineur (par ex. : 3.2 et non 3.0.1). La version du code doit être 3.0 ou une version ultérieure. |
| Clé API REST (intégration serveur à serveur uniquement) | Une clé API REST Braze avec des autorisations `users.track` et `users.delete`. <br><br>Pour créer une clé API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé API REST) > Create New API Key (Créer une nouvelle clé API)**.|
{: .reset-td-br-1 .reset-td-br-2}

## Choisir votre type d’intégration

| Intégration | Détails |
| ----------- | ------- |
| [Côte à côte](#side-by-side-sdk-integration) | Ce mode d’intégration utilise le SDK de Tealium pour traduire les événements en appels natifs de Braze, permettant d’accéder à des fonctionnalités plus avancées et de tirer le meilleur parti de l’intégration serveur à serveur de Braze.<br><br>Si vous prévoyez d’utiliser les commandes à distance de Braze, notez que Tealium ne prend pas en charge toutes les méthodes de Braze (par ex., les cartes de contenu). Pour utiliser une méthode Braze qui n’est pas mappée à l’aide d’une commande à distance correspondante, vous devez invoquer la méthode en ajoutant le code Braze natif à votre base de code.|
| [Serveur à serveur](#server-to-server-integration) | Ce mode d’intégration transfère les données de Tealium aux endpoints d’API REST de Braze.<br><br>Il ne prend pas en charge les fonctionnalités d’interface utilisateur de Braze, telles que les messages in-app, les cartes de contenu ou les notifications push. Il existe également des données collectées automatiquement, telles que les champs d’appareil, qui ne sont pas disponibles avec cette méthode.<br><br>Optez pour une intégration côte à côte si vous souhaitez utiliser ces fonctionnalités.|
{: .reset-td-br-1 .reset-td-br-2}

## Intégration SDK côte à côte

### Commandes à distance

Les commandes à distance sont une fonctionnalité des bibliothèques iOS et Android de Tealium qui vous permettent de passer des appels depuis le SDK de Tealium (par le biais des serveurs Braze) vers Braze. Le module de commande à distance de Braze installe et conçoit automatiquement les bibliothèques Braze requises et gère tous les processus d’affichage des messages et d’analyses. Pour utiliser la commande mobile à distance de Braze, vous devez installer les bibliothèques Tealium dans vos applications.

Tealium propose deux façons d’intégrer la commande mobile à distance. Ces deux types d’intégration bénéficient des mêmes fonctionnalités et le code natif sous-jacent est identique.

| Méthode de commande mobile à distance | Avantages | Inconvénients |
| --- | --- | --- |
| **Balise de commande à distance** | Modifiez facilement les mappages et les données envoyées à la commande à distance à l’aide de l’interface utilisateur Tealium iQ.<br><br>Cela nous permet d’envoyer des données ou des événements supplémentaires à un SDK tiers lorsque l’application est dans l’App Store, sans que le client ait à mettre à jour l’application. | Le module de gestion des balises de l’application repose sur une vue Web masquée pour traiter JavaScript. |
| **Fichier de configuration JSON**<br>([Recommandé](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#how-it-works)) | La méthode JSON permet de ne pas utiliser de vue Web cachée dans l’application et réduit considérablement la consommation de mémoire.<br><br>Le fichier JSON peut être hébergé à distance ou localement dans l’application du client. | À l’heure actuelle, il n’existe pas d’interface utilisateur permettant de gérer cette méthode, elle demande donc un peu plus de temps.<br><br>Remarque : Tealium travaille actuellement sur une interface utilisateur de gestion pour résoudre ce problème et apporter le même niveau de flexibilité aux commandes à distance JSON qu’avec la version de gestion des balises iQ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Utilisez les mappages de données de la commande mobile à distance de Braze pour définir les attributs utilisateur par défaut et les attributs personnalisés, tout en suivant les achats et les événements personnalisés. Reportez-vous au tableau ci-dessous pour découvrir les méthodes de Braze correspondantes.

| Commande à distance | Méthode Braze |
| -------------- | ------------ |
| appendcustomarrayattribute | addToCustomAttributeArrayWithKey()|
| emailnotification | setEmailNotificationSubscriptionType() |
| incrementcustomattribute | incrementCustomAttribute() |
| Initalize | startWithApiKey() |
| logcustomevent | logCustomEvent() |
| logpurchase | logPurchase() |
| pushnotification | setPushNotificationSubscriptionType() |
| removecustomattribute | setCustomAttributeWithKey() |
| setcustomattribute | setCustomAttributeArrayWithKey() |
| setcustomarrayattribute | setCustomAttributeArrayWithKey() |
| setlastknownlocation | setLastKnownLocationWithLatitude() |
| unsetcustomattribute | unsetCustomAttributeWithKey() |
| useralias | addAlias() |
| userattribute | ABKUser() |
| useridentifier | changeUser() |
{: .reset-td-br-1 .reset-td-br-2}

Vous trouverez plus de détails sur la configuration de la commande mobile à distance de Braze et un aperçu des méthodes prises en charge dans la [documentation pour les développeurs](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Mobile-Remote-Command-Tag-Setup-Guide/ta-p/32828) de Tealium.
- [Commande à distance](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#json-template)
- [Balise de commande à distance](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Mobile-Remote-Command-Tag-Setup-Guide/ta-p/32828)

{% alert important %}
Les commandes mobiles à distance de Braze ne prennent pas en charge toutes les méthodes et les canaux de communication de Braze (par ex., les cartes de contenu). Pour utiliser une méthode Braze qui n’est pas mappée à l’aide d’une commande à distance correspondante, vous devez invoquer directement la méthode en ajoutant le code Braze natif à votre base de code.
{% endalert%}

### Balise du SDK Web de Braze

Utilisez la balise du SDK Web de Braze pour déployer le SDK Web de Braze sur votre site Internet. L’interface de [gestion des balises de Tealium iQ](https://community.tealiumiq.com/t5/iQ-Tag-Management/Introduction-to-iQ-Tag-Management/ta-p/15883) permet aux clients d’ajouter Braze comme balise dans le tableau de bord de Tealium pour suivre l’activité des visiteurs. Les balises sont généralement utilisées par les marketeurs pour comprendre l’efficacité des publicités en ligne, du marketing par e-mail et des personnalisations de sites Web.

1. Dans Tealium, accédez à **iQ [Tag Management (Gestion des balises)](https://community.tealiumiq.com/t5/iQ-Tag-Management/Tags/ta-p/5016) > Tags (Balises) > + Add Tag (+ Ajouter une balise) > Braze Web SDK (SDK Web de Braze)**.
2. Dans la boîte de dialogue Configuration des balises, saisissez la clé API (votre clé d’identification d’application Braze), l’URL de base (endpoint SDK de Braze), et la [version du code du SDK Web de Braze](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md). Vous pouvez également activer la journalisation pour consigner les informations dans la console Web à des fins de débogage.
3. Dans la boîte de dialogue [Load Rules (Règles de chargement)](https://community.tealiumiq.com/t5/iQ-Tag-Management/Load-Rules/ta-p/5098), choisissez « Load on All Pages (Charger sur toutes les pages) » ou sélectionnez **Create Rule (Créer une règle)** pour déterminer quand et où charger une instance de cette balise sur votre site.
4. Dans la boîte de dialogue **[Data Mappings (Mappages de données)](https://community.tealiumiq.com/t5/iQ-Tag-Management/Data-Mappings/ta-p/10645#mapping_data_sources)**, sélectionnez **Create Mappings (Créer des mappages)** pour mapper les données de Tealium vers Braze. Les variables de destination de la balise du SDK Web de Braze sont intégrées dans l’onglet **Data Mapping (Mappage des données)** de la balise. Les [tableaux suivants](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Web-SDK-Tag-Setup-Guide/ta-p/20106#toc-hId--2077373923) répertorient les catégories de destination disponibles et décrivent chaque nom de destination.
5. Cliquez sur **Finish (Terminer)**.

### Ressources des intégrations côte à côte

- Commandes à distance pour iOS : [Documentation Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Référentiel Tealium GiThub](https://github.com/Tealium/tealium-ios-braze-remote-command)
- Commande à distance Android : [Documentation Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Référentiel Tealium GiThub](https://github.com/Tealium/tealium-android-braze-remote-command)
- Balise du SDK Web : [Documentation Tealium](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Web-SDK-Tag-Setup-Guide/ta-p/20106)

## Intégration serveur à serveur

Cette intégration transfère les données de Tealium à l’API REST de Braze.

L’intégration serveur à serveur ne prend pas en charge les fonctionnalités d’interface utilisateur de Braze, telles que les messages in-app, les cartes de contenu ou les notifications push. Il existe également des données collectées automatiquement (telles que les champs d’appareil), qui ne sont pas disponibles avec cette méthode.

Optez pour notre intégration SDK [côte à côte]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium/#side-by-side-sdk-integration) si vous souhaitez utiliser ces données et fonctionnalités.

### Étape 1 : Configurer une source

Tealium exige que vous configuriez d’abord une source de données valide pour que votre connecteur puisse extraire des données.
1. Dans la barre latérale de Tealium, sous **Server-Side (Côté serveur)**, accédez à **Sources > Data Sources (Sources de données) > + Add Data Source (+ Ajouter une source de données)**.
2. Recherchez la plateforme souhaitée dans les catégories disponibles et nommez votre source. Ce champ est obligatoire.<br>![][6]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. Dans les options **Event Specifications (Spécifications d’événement)**, choisissez les [spécifications d’événement](https://community.tealiumiq.com/t5/Customer-Data-Hub/Event-Specifications/ta-p/19329) que vous souhaitez inclure. Les spécifications d’événement vous aident à identifier les noms d’événements et les attributs requis pour suivre votre installation. Ces spécifications seront appliquées aux événements entrants.<br>![][7]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>Prenez le temps de réfléchir aux données qui vous conviennent le mieux et aux spécifications qui vous semblent les plus appropriées pour votre cas d’utilisation. Des [spécifications d’événements personnalisés][19] sont également disponibles. <br>
4. La prochaine boîte de dialogue vous mène à l’étape **Get Code (Obtenir le code)**. Le code de base et le code de suivi des événements fournis ici servent de guide d’installation. Téléchargez le PDF fourni si vous souhaitez partager ces instructions avec votre équipe. Cliquez sur **Save & Continue (Enregistrer et continuer)** lorsque vous avez terminé.<br>
5. Vous pouvez maintenant consulter votre source enregistrée et ajouter ou supprimer des spécifications d’événement. <br>![][18]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>La vue détaillée de la source de données vous permet d’effectuer les actions suivantes :
- Afficher et copier la clé de la source de données
- Consulter les instructions d’installation
- Revenir à la page **Get Code (Obtenir le code)**
- Ajouter ou supprimer des spécifications d’événement
- Naviguer pour visualiser les événements en direct liés à une spécification d’événement
- Et plus encore…<br>
6. Enfin, cliquez sur **Save / Publish (Enregistrer/Publier)** en haut de la page. Si vous ne publiez pas votre source, vous ne pourrez pas la retrouver au moment de configurer votre connecteur Braze.

Consultez les [Data Sources (Sources de données)](https://community.tealiumiq.com/t5/Customer-Data-Hub/Data-Sources/ta-p/17933) pour plus d’instructions sur la façon de configurer et de modifier votre source de données.

### Étape 2 : Créer un connecteur d’événement

Un connecteur est une intégration entre Tealium et un autre fournisseur qui est utilisée pour transmettre des données. Ces connecteurs contiennent des actions qui représentent les API prises en charge par leur partenaire. 

1. Dans la barre latérale de Tealium, sous **Server-Side (Côté serveur)**, accédez à **EventStream > Event Connectors (Connecteurs d’événements)**.
2. Cliquez sur le bouton bleu **+ Add Connector (+ Ajouter un connecteur)** pour ouvrir le marketplace des connecteurs. Dans la boîte de dialogue qui apparaît, utilisez la recherche Spotlight pour trouver le connecteur **Braze**.
3. Pour ajouter ce connecteur, cliquez sur la vignette du connecteur **Braze**. Après avoir cliqué, vous pouvez afficher le résumé de la connexion et la liste des informations requises, des actions prises en charge et des instructions de configuration. La configuration comprend trois étapes : source, configuration et action.

#### Source

Une fois la source configurée, revenez à la page du connecteur Braze sous **EventStream > Event Connectors (Connecteurs d’événements) > + Add Connector (+ Ajouter un connecteur) > Braze**. 

Dans la boîte de dialogue qui s’ouvre, sélectionnez la source de données que vous venez de construire, et sous **Event Feed (Flux d’événements)**, sélectionnez **All Events (Tous les événements)** ou une spécification d’événement, le chemin recommandé pour envoyer uniquement des valeurs modifiées dans Braze. Cliquez sur **Continue (Continuer)**.

#### Configuration

Ensuite, sélectionnez **Add Connector (Ajouter un connecteur)** au bas de la page. Donnez un nom à votre connecteur et fournissez votre endpoint d’API Braze et la clé API REST de Braze.

![][15]{: style="max-width:70%;"}

Si vous aviez déjà créé un connecteur auparavant, vous avez la possibilité d’utiliser un élément existant dans la liste des connecteurs disponibles et de le modifier pour répondre à vos besoins en cliquant sur l’icône Crayon ou de le supprimer en cliquant sur l’icône Corbeille. 

#### Action

Ensuite, nommez l’action de votre connecteur et sélectionnez un type d’action pour envoyer des données en fonction du mappage que vous configurez. Ici, vous allez mapper les attributs, événements et achats de Braze aux noms des attributs, événements et achats de Tealium.

{% alert important %}
Tous les champs ne sont pas obligatoires.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Track User (Batch and Non-Batch) %}

Cette action vous permet de suivre les attributs des utilisateurs, événements et achats en une seule action.

| Paramètres | Description |
| ---------- | ----------- |
| ID utilisateur | Utilisez ce champ pour mapper le champ ID utilisateur de Tealium à son équivalent dans Braze. Mappez un ou plusieurs attributs d’ID utilisateur. Si plusieurs ID ont été indiqués, la première valeur non vide sera prélevée en fonction de l’ordre de priorité suivant : ID externe, ID Braze, nom d’alias et libellé d’alias.<br><br>- L’ID externe et l’ID de Braze ne doivent pas être indiqués si vous importez des jetons de notification push.<br>- Si vous indiquez un alias d’utilisateur, le nom d’alias et le libellé d’alias doivent également être fournis. <br><br>Pour plus d’informations, consultez l’[endpoint /users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze. |
| Attributs utilisateur | Utilisez les champs de profil utilisateur de Braze pour mettre à jour les valeurs de profil utilisateur dans le tableau de bord de Braze ou ajouter vos propres données d’[attribut utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/) personnalisées dans les profils utilisateur.<br><br>- Par défaut, de nouveaux utilisateurs seront créés s’il n’en existe aucun.<br>- En définissant **Update Existing Only (Mettre uniquement à jour les utilisateurs existants)** sur `true`, seuls les utilisateurs existants seront mis à jour, et aucun nouvel utilisateur ne sera créé.<br>- Si un attribut Tealium est vide, il sera défini en « nul » et supprimé du profil utilisateur Braze. Les enrichissements doivent être utilisés si les valeurs nulles ne doivent pas être envoyées à Braze pour supprimer un attribut utilisateur. |
| Modifier les attributs utilisateur | Utilisez ce champ pour incrémenter ou décrémenter certains attributs utilisateur<br><br>- Les attributs entiers peuvent être incrémentés par des entiers positifs ou négatifs.<br>- Les attributs de matrice peuvent être modifiés en ajoutant ou en supprimant des valeurs provenant des matrices existantes. |
| Événement | Un événement représente une occurrence unique d’un événement personnalisé pour un utilisateur particulier à un horodatage donné. Utilisez ce champ pour suivre et mapper les attributs d’événements tels que ceux de l’[objet Événement]({{site.baseurl}}/api/objects_filters/event_object/) de Braze. <br><br>- Le `Name` de l’attribut événement est requis pour chaque événement mappé.<br>- Le `Time` de l’attribut événement est automatiquement défini à l’heure actuelle, sauf si cela est explicitement mappé. <br>- Par défaut, de nouveaux événements seront créés s’il n’en existe aucun. En définissant `Update Existing Only` sur `true`, seuls les événements existants seront mis à jour, et aucun nouvel événement ne sera créé.<br>- Mappez les attributs de type de matrice pour ajouter plusieurs événements. Les attributs de type de matrice doivent être de longueur égale.<br>- Les attributs de valeur unique peuvent être utilisés et appliqués à chaque événement. |
| Modèle d’événement | Fournissez des modèles d’événements à référencer dans les données du corps. Les modèles peuvent être utilisés pour transformer des données avant de les envoyer à Braze. Consultez le [Guide des modèles](https://community.tealiumiq.com/t5/AudienceStream/Webhook-Send-Custom-Request-Trimou-Templating-Engine-Guide/ta-p/15246/) de Tealium pour en savoir plus. |
| Variable du modèle d’événement | Fournissez des variables de modèle d’événement comme entrée de données. Consultez le [Guide des variables de modèles](https://community.tealiumiq.com/t5/AudienceStream/Webhook-Send-Custom-Request-Template-Variables-Guide/ta-p/15245/) de Tealium pour en savoir plus. |
| Achat | Utilisez ce champ pour suivre et mapper les achats des utilisateurs tels que ceux de l’[objet achat]({{site.baseurl}}/api/objects_filters/purchase_object/) de Braze.<br><br>- Les attributs d’achat `Product ID`, `Currency` et `Price` sont nécessaires pour chaque achat mappé.<br>- Le `Time` de l’attribut achat est automatiquement défini à l’heure actuelle, sauf si cela est explicitement mappé.<br>- Par défaut, de nouveaux achats seront créés s’il n’en existe aucun. En définissant `Update Existing Only` sur `true`, seuls les achats existants seront mis à jour, et aucun nouvel achat ne sera créé.<br>- Mappez les attributs de type de matrice pour ajouter plusieurs éléments d’achat. Les attributs de type de matrice doivent être de longueur égale.<br>- Les attributs de valeur unique peuvent être utilisés et s’appliqueront à chaque élément.|
| Modèle d’achat | Les modèles peuvent être utilisés pour transformer des données avant de les envoyer à Braze.<br>- Définissez un modèle d’achat si vous avez besoin de prendre en charge des objets imbriqués.<br>- Lorsqu’un modèle d’achat est défini, la configuration de la section Achats de votre action sera ignorée.<br>- Consultez le [Guide des modèles](https://community.tealiumiq.com/t5/AudienceStream/Webhook-Send-Custom-Request-Trimou-Templating-Engine-Guide/ta-p/15246/) de Tealium pour en savoir plus.|
| Variable du modèle d’achat | Fournissez des variables de modèle de produit comme entrée de données. Consultez le [Guide des variables de modèles](https://community.tealiumiq.com/t5/AudienceStream/Webhook-Send-Custom-Request-Template-Variables-Guide/ta-p/15245/) de Tealium pour en savoir plus. |
{: .reset-td-br-1 .reset-td-br-2}

![]({% image_buster /assets/img/tealium/track_user_example.png %})

{% endtab %}
{% tab Delete User (Non-Batch) %}

Cette action vous permet de supprimer des utilisateurs du tableau de bord de Braze.

| Paramètres | Description |
| ---------- | ----------- |
| ID utilisateur | Utilisez ce champ pour mapper le champ ID utilisateur de Tealium à son équivalent dans Braze. <br><br>- Mappez un ou plusieurs attributs d’ID utilisateur. Si plusieurs ID ont été indiqués, la première valeur non vide sera prélevée en fonction de l’ordre de priorité suivant : ID externe, ID Braze, nom d’alias et libellé d’alias.<br>- Si vous indiquez un alias d’utilisateur, le nom d’alias et le libellé d’alias ne doivent pas être fournis.<br><br>Consultez l’[endpoint /users/delete]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) de Braze pour plus d’informations. |
{: .reset-td-br-1 .reset-td-br-2}

![]({% image_buster /assets/img/tealium/track_user_delete.png %})

Si vous souhaitez modifier les options sélectionnées, cliquez sur **Back (Retour)** pour les modifier ou sur **Finish (Terminer)**.

{% endtab %}
{% endtabs %}

Cliquez sur **Continue (Continuer)**.

Votre connecteur s’affiche maintenant dans la liste des connecteurs sur votre page d’accueil Tealium.  <br>![][13]{: style="max-width:80%;"}

Assurez-vous d’**Enregistrer/Publier** votre connecteur une fois terminé. Les actions que vous avez configurées vont maintenant se déclencher lorsque les connexions du déclencheur sont satisfaites. 

### Étape 3 : Tester votre connecteur Tealium

Une fois votre connecteur en marche et en cours d’exécution, vous devez le tester pour vous assurer qu’il fonctionne correctement. Le moyen le plus simple de tester votre connecteur est d’utiliser l’**outil Trace** de Tealium. Pour commencer à utiliser Trace, assurez-vous d’avoir ajouté l’extension de navigateur Tealium Tools.

1. Pour démarrer une nouvelle action de suivi, sélectionnez **Trace** sur la barre latérale sous les options **Server-Side (Côté serveur)**. Cliquez sur **Start (Démarrer)** et notez l’ID de Trace.
2. Ouvrez l’extension du navigateur et saisissez l’ID de Trace dans AudienceStream Trace.
3. Vérifiez le journal en temps réel.
4. Vérifiez l’action que vous souhaitez valider en cliquant sur l’entrée **Actions Triggered (Actions déclenchées)** pour développer la liste.
5. Recherchez l’action que vous souhaitez valider et consultez l’état du journal. 

Consultez la [documentation Trace][21] de Tealium pour obtenir des instructions détaillées sur l’utilisation de l’outil Trace de Tealium.

## Démo de l’intégration

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Dépassements potentiels des points de données

Il existe trois façons principales d’atteindre accidentellement des dépassements de données lorsque vous intégrez Braze via Tealium :

#### Envoyer des données en double - envoyez uniquement des deltas d’attributs à Braze
Tealium n’envoie pas de deltas d’attributs utilisateur à Braze. Par exemple, si vous avez une action EventStream qui suit le prénom, l’e-mail et le numéro de téléphone portable d’un utilisateur, Tealium enverra ces trois attributs à Braze chaque fois que l’action est déclenchée. Tealium ne recherchera pas ce qui a changé ou ce qui a été mis à jour pour n’envoyer que ces informations.<br><br> 
**Solution** : <br>Vous pouvez vérifier votre back-end pour déterminer si un attribut a changé ou non. Si c’est le cas, suivez les méthodes de Tealium correspondantes pour mettre à jour le profil utilisateur. **C’est ce que font généralement les utilisateurs qui intègrent directement Braze.** <br>**OU**<br> Si vous ne stockez pas votre propre version d’un profil utilisateur dans votre dossier et si vous ne pouvez pas déterminer si des attributs changent ou non, vous pouvez utiliser AudienceStream et 
[créer des enrichissements](https://community.tealiumiq.com/t5/Customer-Data-Hub/Using-Enrichments/ta-p/11932) pour envoyer uniquement les attributs d’utilisateur lorsque les valeurs ont changé. Consultez la documentation de Tealium sur les [règles d’enrichissement](https://community.tealiumiq.com/t5/Server-Side-Connectors/Braze-Connector-Setup-Guide/ta-p/29761#).

#### Envoyer des données non pertinentes ou écraser inutilement des données
Si vous avez plusieurs EventStream qui ciblent le même flux d’événements, **toutes les actions activées pour ce connecteur** se déclencheront automatiquement chaque fois qu’une action est déclenchée, **cela pourrait également entraîner l’écrasement des données dans Braze et une consommation inutile de vos points de données.**<br><br>
**Solution** : <br>Configurez une spécification ou un flux d’événement distinct pour suivre chaque action. <br>**OU**<br> Désactivez les actions (ou les connecteurs) que vous ne voulez pas déclencher en utilisant les boutons de bascule du tableau de bord Tealium.

#### Initialiser Braze trop tôt
Il se peut que les utilisateurs qui intègrent Tealium à l’aide de la balise du SDK Web de Braze observent une augmentation spectaculaire de leur MAU. **Si Braze est initialisé pendant le chargement de la page, Braze créera un profil anonyme chaque fois qu’un utilisateur Web navigue sur le site pour la première fois.** Certaines personnes voudront suivre le comportement des utilisateurs uniquement lorsque ceux-ci ont effectué certaines actions, comme « Signed In (Connecté) » ou « Watched Video (Vidéo regardée) », pour réduire leur MAU. <br><br>
**Solution** : <br>Configurez les règles de chargement pour déterminer exactement quand et où une balise doit charger sur votre site. Vous pouvez en savoir plus sur les règles de chargement et sur la manière de les configurer dans le [Centre d’apprentissage Tealium](https://community.tealiumiq.com/t5/Customer-Data-Hub/Building-an-Audience/ta-p/11881).

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[5]: {% image_buster /assets/img/tealium/braze_connector_marketplace.png %}
[6]: {% image_buster /assets/img/tealium/data_source.png %}
[7]: {% image_buster /assets/img/tealium/event_specs.png %}
[8]: {% image_buster /assets/img/tealium/get_code.png %}
[9]: {% image_buster /assets/img/tealium/summary.png %}
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[13]: {% image_buster /assets/img/tealium/summary_list.png %}
[15]: {% image_buster /assets/img/tealium/create_configuration.png %}
[16]: {% image_buster /assets/img/tealium/connector_summary.png %}
[17]: {% image_buster /assets/img/tealium/save_publish.png %}
[18]: {% image_buster /assets/img/tealium/braze_connection.png %}
[19]: https://community.tealiumiq.com/t5/Customer-Data-Hub/Event-Specifications/ta-p/19329#toc-hId--2078027338
[21]: https://community.tealiumiq.com/t5/Customer-Data-Hub/Trace/ta-p/12058
[22]: {% image_buster /assets/img/tealium/tealium_overview.png %}
[23]: {% image_buster /assets/img/tealium/remote_mappings.png %}
