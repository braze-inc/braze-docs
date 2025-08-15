---
nav_title: Tealium
article_title: Tealium
page_order: 1
alias: /partners/tealium/
description: "Cet article de référence décrit le partenariat entre Braze et Tealium, un hub de données universel qui vous permet de connecter des données mobiles, web et alternatives à d'autres sources tierces."
page_type: partner
search_tag: Partner

---

# Tealium

> [Tealium](https://tealium.com/) est un hub de données universel et une plateforme de données client composée d'eventstream, AudienceStream et iQ Tag Management qui vous permet de connecter des données mobiles, web et alternatives provenant de sources tierces. La connexion de Tealium à Braze permet un flux de données d'événements personnalisés, d'attributs utilisateur et d'achats qui vous permet d'agir sur vos données en temps réel.

![Un graphique d'aperçu de Tealium montrant comment les différents produits Tealium et la plateforme Braze s'intègrent pour activer des campagnes cross-canal en temps réel.][22]{: style="border:0;"}

L'intégration de Braze et Tealium vous permet de suivre vos utilisateurs et de diriger les données vers divers fournisseurs d'analyse utilisateur. Tealium vous permet de :
- Synchronisez les audiences de Tealium avec [AudienceStream]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/) vers Braze pour les utiliser dans la personnalisation des campagnes et des Canvases de Braze ou la création de segments.
- [Importer des données entre les plateformes](#choose-your-integration-type). Braze propose à la fois une [intégration SDK](#side-by-side-sdk-integration) côte à côte pour vos applications Android, iOS et web et une [intégration serveur-à-serveur](#server-to-server-integration) qui peut être utilisée sur toute plateforme capable de rapporter des données d'événements.<br><br>

{% tabs %}
{% tab eventstream %}
Tealium eventstream est un centre de collecte de données et d'API qui se trouve au centre de vos données. eventstream gère l'ensemble de la chaîne d'approvisionnement en données, de la configuration et de l'installation à l'identification, la validation et l'amélioration des données utilisateur entrantes. eventstream prend des mesures en temps réel avec des flux d'événements et des connecteurs. Voici les fonctionnalités qui composent [EventStream](https://docs.tealium.com/server-side/getting-started/eventstream-api-hub/introduction/).
- Sources de données (installation et collecte de données)
- événements en ligne (inspection des données en temps réel)
- Spécifications et attributs d'événement (exigences et validation de la couche de donnée)
- Flux d'événements (types d'événements filtrés)
- Connecteurs d'événements (actions du hub API)

{% endtab %}
{% tab AudienceStream %}

Tealium AudienceStream est un moteur d'action en temps réel et de segmentation de la clientèle omnicanal. AudienceStream prend les données qui circulent dans EventStream et crée des profils de visiteurs qui représentent les attributs les plus importants de l'engagement de vos clients avec votre marque. Consultez notre article [AudienceStream]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/) pour les étapes de configuration.

{% endtab %}
{% tab Gestion des balises iQ %}
Tealium iQ vous permet de déclencher du code dans vos applications en utilisant une balise dans l'interface de gestion des balises Tealium iQ. Cette balise collectera, contrôlera et livrera les données d'événements des plateformes mobiles et web, vous permettant de configurer une mise en œuvre native de Braze sans ajouter de code spécifique à Braze dans vos applications. Les utilisateurs peuvent choisir d'intégrer des commandes à distance mobiles via la gestion des étiquettes iQ ou des fichiers de configuration JSON (approche recommandée par Tealium). Les utilisateurs qui utilisent le SDK Web Braze doivent s'intégrer via la balise web iQ.

Pour en savoir plus sur les avantages et les inconvénients de chaque méthode, reportez-vous à la section suivante [Gestionnaire des balises Tealium iQ](#mobile-remote-commands).
{% endtab %}
{% endtabs %}

{% alert important %}
Tealium propose des actions de connecteur par lot et sans lot. Le connecteur non-batch doit être utilisé lorsque les requêtes en temps réel sont importantes pour le cas d'utilisation et qu'il n'y a pas d'inquiétude quant à la limite de débit de l'API Braze. Contactez le service d’assistance de Braze ou votre gestionnaire de la satisfaction des clients si vous avez des questions.<br><br>

Pour les connecteurs par lots, les requêtes sont mises en file d'attente jusqu'à ce que l'un des seuils suivants soit atteint :<br><br>
- Nombre maximum de requêtes : 75
- Temps maximum depuis la requête la plus ancienne : 10 minutes
- Taille maximale des requêtes : 1 MO

Tealium ne regroupe pas par défaut les événements de consentement (préférences d'abonnement) ou les événements de suppression d'utilisateur.
{% endalert %}

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Tealium | Un [compte Tealium](https://my.tealiumiq.com/) avec un accès serveur et/ou côté client est requis pour profiter de ce partenariat. | 
| [Bibliothèques](https://docs.tealium.com/platforms/) des sources installées et sources Tealium | L'origine de toute donnée envoyée dans Tealium, telle que des applications mobiles, des sites web ou des serveurs backend.<br><br>Vous devez installer les bibliothèques dans votre application, site ou serveur avant de pouvoir configurer un connecteur Tealium avec succès. |
| Endpoint REST et SDK Braze | Votre URL d’endpoint REST ou SDK. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints). |
| Clé d'identification de l'application Braze (côte à côte uniquement) | Votre clé d'identifiant d'application. <br><br>Elle se trouve sous **Tableau de bord de Braze > Gérer les paramètres > Clé API**. |
| Version du code (côte à côte uniquement) | Correspond à la version du SDK et doit être au format major.minor (par exemple, 3.2 et non 3.0.1). La version du code doit être 3.0 ou supérieure. |
| clé API REST (serveur-à-serveur seulement) | Une clé API REST Braze avec les autorisations `users.track` et `users.delete`. <br><br>Elle peut être créée sous **Tableau de bord de Braze > Console de développement > Clé API REST > Créer une nouvelle clé API**.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Choisissez votre type d'intégration

| Intégration | Détails |
| ----------- | ------- |
| [Côte à côte](#side-by-side-sdk-integration) | Utilise le SDK de Tealium pour traduire les événements en appels natifs de Braze, ce qui permet d'accéder à des fonctionnalités plus profondes et à une utilisation plus complète de Braze que l'intégration de serveur à serveur.<br><br>Si vous prévoyez d'utiliser les commandes à distance Braze, notez que Tealium ne prend pas en charge toutes les méthodes Braze (par exemple, les cartes de contenu). Pour utiliser une méthode Braze qui n'est pas mappée via une commande à distance correspondante, vous devrez invoquer la méthode en ajoutant du code Braze natif à votre base de code.|
| [Serveur-à-serveur](#server-to-server-integration) | Transmet les données de Tealium aux endpoints de l'API REST de Braze.<br><br>Ne prend pas en charge les fonctionnalités de l'interface utilisateur de Braze telles que l'envoi de messages dans l'application, les cartes de contenu ou les notifications push. Il existe également des données capturées automatiquement, telles que des champs au niveau de l'appareil, qui ne sont pas disponibles par cette méthode.<br><br>Envisagez une intégration côte à côte si vous souhaitez utiliser ces fonctionnalités.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## intégration SDK côte à côte

### Commandes à distance

Les commandes à distance sont une fonctionnalité des bibliothèques iOS et Android de Tealium qui vous permettent de passer des appels depuis le SDK Tealium—via les serveurs Braze—vers Braze. Le module de commande à distance Braze installera automatiquement et créera les bibliothèques Braze nécessaires et gérera tout le rendu des messages et le suivi analytique. Pour utiliser la commande à distance mobile Braze, vous aurez besoin des bibliothèques Tealium installées dans vos applications.

Tealium propose deux façons d'intégrer Mobile Remote Command, il n'y a aucune perte de fonctionnalité entre les types d'intégration et le code natif sous-jacent est identique.

| Méthode de commande à distance mobile | Avantages | Inconvénients |
| --- | --- | --- |
| **Balise de commande à distance** | Modifiez facilement les mappages et les données envoyées à la commande distante en utilisant l'interface utilisateur de Tealium iQ.<br><br>Cela nous permet d'envoyer des données ou des événements supplémentaires à un SDK tiers après que l'application soit déjà dans l'App Store, sans que le client ait à mettre à jour l'application. | Le module de gestion des étiquettes dans l'application repose sur une webview cachée pour traiter JavaScript. |
| **Fichier de configuration JSON**<br>([Recommandé](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#how-it-works)) | L'utilisation de la méthode JSON élimine le besoin d'avoir une vue Web cachée dans l'application et réduit considérablement la consommation de mémoire.<br><br>Le fichier JSON peut être hébergé à distance ou localement dans l'application du client. | Pour le moment, il n'y a pas d'interface utilisateur pour gérer cela, donc cela nécessite un peu d'effort supplémentaire.<br><br>Remarque: Tealium travaille sur l'ajout d'une interface de gestion qui résoudra ce problème et apportera le même niveau de flexibilité aux commandes à distance JSON qu'ils ont avec la version de gestion des étiquettes iQ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Utilisez les mappages de données de commande à distance mobile Braze pour définir des attributs utilisateur par défaut et des attributs personnalisés et suivre les achats et les custom events. Reportez-vous au tableau suivant pour les méthodes Braze correspondantes.

| Commande à distance | méthode Braze |
| -------------- | ------------ |
| appendcustomarrayattribute | addToCustomAttributeArrayWithKey()|
| emailnotification | setEmailNotificationSubscriptionType() |
| incrementcustomattribute | incrementCustomAttribute() |
| Initialiser | startWithApiKey() |
| logcustomevent | logCustomEvent() |
| logpurchase | logPurchase() |
| notification push | setPushNotificationSubscriptionType() |
| supprimerlattributpersonnalisé | setCustomAttributeWithKey() |
| setcustomattribute | setCustomAttributeArrayWithKey() |
| setcustomarrayattribute | setCustomAttributeArrayWithKey() |
| setlastknownlocation | setLastKnownLocationWithLatitude() |
| unsetcustomattribute | unsetCustomAttributeWithKey() |
| useralias | addAlias() |
| userattribute | ABKUser() |
| useridentifier | changeUser() |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Vous pouvez trouver plus de détails sur la façon de configurer la commande à distance mobile Braze et un aperçu des méthodes prises en charge dans la documentation du développeur Tealium :
- [Commande à distance](https://docs.tealium.com/platforms/remote-commands/integrations/braze/#json-template)
- [Balise de commande à distance](https://docs.tealium.com/client-side-tags/braze-mobile-remote-command-tag/)

{% alert important %}
Les commandes à distance mobiles de Braze ne prennent pas en charge toutes les méthodes et tous les canaux d'envoi de messages de Braze (par exemple, les cartes de contenu). Pour utiliser une méthode Braze qui n'est pas mappée via une commande à distance correspondante, vous devrez invoquer la méthode directement en ajoutant du code Braze natif à votre base de code.
{% endalert%}

### Balise du SDK Web Braze

Utilisez l'étiquette Braze Web SDK pour déployer le Braze Web SDK sur votre site web. [Tealium iQ Tag Management](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) permet aux clients d'ajouter Braze comme balise dans le tableau de bord Tealium pour suivre l'activité des visiteurs. Les balises sont généralement utilisées par les marketeurs pour comprendre l'efficacité de la publicité en ligne, du marketing par e-mail et de la personnalisation du site.

1. Dans Tealium, accédez à **iQ > Balises > + Ajouter une balise > SDK Web Braze**.
2. Dans la boîte de dialogue Configuration des balises, entrez la clé API (votre clé d'identification d'application Braze), l'URL de base (endpoint SDK Braze) et la [version du code SDK Web Braze](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md). Vous pouvez également activer la journalisation pour enregistrer des informations dans la console web à des fins de débogage.
3. Dans la boîte de dialogue [Load Rules](https://docs.tealium.com/iq-tag-management/load-rules/about/), choisissez "Charger sur toutes les pages" ou sélectionnez **Create Rule** pour déterminer quand et où charger une instance de cette étiquette sur votre site.
4. Dans la boîte de dialogue **[données Mappings](https://docs.tealium.com/iq-tag-management/data-mappings/about/)**, sélectionnez **Créer des Mappings** pour mapper les données Tealium à Braze. Les variables de destination de la balise SDK Web Braze sont intégrées dans l'onglet **Mappage des données** de la balise. Les [tableaux suivants](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/) répertorient les catégories de destination disponibles et décrivent chaque nom de destination.
5. Sélectionnez **Terminer**.

### Ressources d'intégrations côte à côte

- Commande à distance iOS: [Documentation Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Dépôt Tealium GitHub](https://github.com/Tealium/tealium-ios-braze-remote-command)
- Commande à distance Android : [Documentation Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Dépôt Tealium GitHub](https://github.com/Tealium/tealium-android-braze-remote-command)
- Balise SDK Web : [Documentation Tealium](https://docs.tealium.com/client-side-tags/braze-web-sdk-tag/)

## Intégration serveur-à-serveur

Cette intégration transfère des données de Tealium à l'API REST de Braze.

L'intégration serveur à serveur ne prend pas en charge les fonctionnalités de l'interface utilisateur de Braze telles que l'envoi de messages in-app, les cartes de contenu ou les notifications push. Il existe également des données capturées automatiquement (telles que des champs au niveau de l'appareil) qui ne sont pas disponibles par cette méthode.

Si vous souhaitez utiliser cette donnée et ces fonctionnalités, envisagez notre [intégration SDK]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium/#side-by-side-sdk-integration) côte à côte.

### Étape 1 : Configurer une source

Tealium exige que vous configuriez d'abord une source de données valide pour que votre connecteur puisse s'en servir.
1. Depuis la barre latérale dans Tealium sous **serveur**, accédez à **Sources > Sources de données > + Ajouter une source de données**.
2. Recherchez la plateforme souhaitée dans les catégories disponibles et nommez votre source, il s'agit d'un champ obligatoire.<br>![][6]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. À partir des **spécifications de l'événement**, choisissez les [spécifications de l'événement](https://docs.tealium.com/server-side/event-specifications/about/) que vous souhaitez inclure. Les spécifications des événements vous aident à identifier les noms des événements et les attributs requis à suivre dans votre installation. Ces spécifications seront appliquées aux événements entrants.<br>![][7]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>Prenez le temps de réfléchir aux données qui vous sont les plus précieuses et aux spécifications qui semblent les plus appropriées pour votre cas d'utilisation. [Les spécifications d'événements personnalisés][19] sont également disponibles. <br>
4. Le boîte de dialogue suivante passe à l'étape **Obtenir le code**. Le code de base et le code de suivi des événements fournis ici servent de guide d'installation. Téléchargez le PDF fourni si vous souhaitez partager ces instructions avec votre équipe. Sélectionnez **enregistrer et continuer** lorsque vous avez terminé.<br>
5. Vous pourrez désormais voir votre source enregistrée ainsi qu'ajouter ou supprimer des spécifications d'événements. <br>![][18]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>À partir de la vue détaillée de la source de données, vous pouvez effectuer les actions suivantes :
- Afficher et copier la clé de source de donnée
- Voir les instructions d'installation
- Retournez à la page **Obtenir le code**
- Ajouter ou supprimer des spécifications d'événement
- Accédez à la vue des événements en ligne/en production/instantané liés à une spécification d'événement
- Et plus...<br>
6. Enfin, sélectionnez **Enregistrer/Publier**dans le haut de la page. Si vous ne publiez pas votre source, vous ne pourrez pas la trouver lors de la configuration de votre connecteur Braze.

Reportez-vous aux [données sources](https://docs.tealium.com/server-side/data-sources/about-data-sources/) pour plus d'instructions sur la configuration et la modification de votre source de données.

### Étape 2 : Créer un connecteur d'événement

Un connecteur est une intégration entre Tealium et un autre fournisseur utilisé pour transmettre des données. Ces connecteurs contiennent des actions qui représentent les API prises en charge par leur partenaire. 

1. Depuis la barre latérale dans Tealium sous **Côté serveur**, accédez à **Eventstream > Connecteurs d'événements**.
2. Sélectionnez le bouton **\+ Ajouter un connecteur** bleu pour parcourir la place de marché des connecteurs. Dans la nouvelle boîte de dialogue qui apparaît, utilisez la recherche par projecteur pour trouver le connecteur **Braze**.
3. Pour ajouter ce connecteur, cliquez sur la tuile de connecteur **Braze**. Cliquez sur la vignette du connecteur a pour effet d’afficher le résumé de la connexion et une liste des informations requises, des actions prises en charge et des instructions de configuration. La configuration comprend trois étapes : source, configuration et action.

#### Source

Une fois la source configurée, retournez à la page du connecteur Braze sous **EventStream** > **Connecteurs d'événements** > **\+ Ajouter un connecteur** > **Braze**. 

Ensuite, sélectionnez la source de données que vous venez de créer et, sous **Flux d'événements**, sélectionnez **Tous les événements** ou une spécification d'événement spécifique, le chemin recommandé pour envoyer uniquement les valeurs modifiées dans Braze. Sélectionnez **Continuer**.

#### Configuration

Ensuite, sélectionnez **Ajouter un connecteur** en bas de la page. Nommez votre connecteur et fournissez votre endpoint API Braze et votre clé API REST Braze ici.

![][15]{: style="max-width:70%;"}

Si vous avez déjà créé un connecteur, vous pouvez éventuellement utiliser un connecteur existant de la liste des connecteurs disponibles et le modifier pour répondre à vos besoins avec l'icône de crayon ou le supprimer avec l'icône de poubelle. 

#### Action

Ensuite, nommez votre action de connecteur et sélectionnez un type d'action qui enverra les données selon le mappage que vous configurez. Ici, vous allez mapper les attributs, événements et achats de Braze aux noms d'attribut, d'événement et d'achat de Tealium.

{% alert important %}
Tous les champs proposés ne sont pas obligatoires.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Suivi des utilisateurs - lots et non-lots %}

Cette action vous permet de suivre les attributs des utilisateurs, des événements et des achats en une seule action.

| Paramètres | Description |
| ---------- | ----------- |
| ID utilisateur | Utilisez ce champ pour mapper le champ ID utilisateur de Tealium à son équivalent Braze. Mapper un ou plusieurs attributs d'ID utilisateur. Lorsque plusieurs identifiants sont spécifiés, la première valeur non vide est choisie en fonction de l'ordre de priorité suivant : ID externe, ID Braze, Nom d'alias, et libellé d'alias.<br><br>\- L’ID externe et l’ID Braze ne doivent pas être spécifiés si vous importez des jetons de notifications push.<br>Si vous spécifiez un alias d'utilisateur, le nom de l'alias et le libellé d'alias doivent être définis. <br><br>Pour plus d'informations, consultez l’[`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Braze. |
| Attributs utilisateur | Utilisez les noms de champs existants du profil utilisateur de Braze pour mettre à jour les valeurs du profil utilisateur dans le tableau de bord de Braze ou ajoutez vos propres données d'[attributs]({{site.baseurl}}/api/objects_filters/user_attributes_object/) personnalisés aux profils utilisateurs.<br><br>Par défaut, de nouveaux utilisateurs seront créés s’il n’en existe aucun.<br>En définissant **Mettre à jour uniquement les existants** sur `true`, seuls les utilisateurs existants seront mis à jour et aucun nouvel utilisateur ne sera créé.<br>Si un attribut Tealium est vide, il sera converti en null et supprimé du profil utilisateur Braze. Les enrichissements doivent être utilisés si des valeurs nulles ne doivent pas être envoyées à Braze pour supprimer un attribut utilisateur. |
| Modifier les attributs de l'utilisateur | Utilisez ce champ pour augmenter ou diminuer certains attributs utilisateur<br><br>Les attributs entiers peuvent être incrémentés par des entiers positifs ou négatifs.<br>Les attributs de tableau peuvent être modifiés en ajoutant ou en supprimant des valeurs provenant des tableaux existants. |
| Événement | Un événement représente une seule occurrence d'un événement personnalisé par un utilisateur particulier à un horodatage. Utilisez ce champ pour suivre et mapper les attributs d'événement comme ceux de l'objet d'événement Braze [event object]({{site.baseurl}}/api/objects_filters/event_object/). <br><br>L'attribut d'événement `Name` est requis pour chaque événement mappé.<br>L'attribut d'événement `Time` est automatiquement défini sur Maintenant à moins qu’il ne soit explicitement mappé. <br>Par défaut, de nouveaux événements seront créés s'il n'en existe pas. En définissant `Update Existing Only` sur `true`, seuls les événements existants seront mis à jour, et aucun nouvel événement ne sera créé.<br>Mapper les attributs de type tableau pour ajouter plusieurs événements. Les attributs de type tableau doivent être de longueur égale.<br>\- Des attributs à valeur unique peuvent être utilisés et appliqués à chaque événement. |
| Modèle d'événement | Fournir des modèles d'événements à référencer dans les données de corps. Les modèles peuvent être utilisés pour transformer des données avant de les envoyer à Braze. Reportez-vous au [Guide des modèles](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium pour en savoir plus. |
| Variable de modèle d'événement | Fournir des variables de modèle d'événement comme entrée de donnée. Reportez-vous au [Guide des variables de modèle](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium pour en savoir plus. |
| Achat | Utilisez ce champ pour suivre et mapper les attributs d'achat des utilisateurs comme ceux dans l'objet d'achat Braze [purchase object]({{site.baseurl}}/api/objects_filters/purchase_object/).<br><br>\- Les attributs d'achat `Product ID`, `Currency` et `Price` sont requis pour chaque achat mappé.<br>\- L'attribut d'achat `Time` est automatiquement défini sur Maintenant à moins qu’il ne soit explicitement mappé.<br>Par défaut, de nouveaux achats seront créés s'il n'en existe pas. En définissant `Update Existing Only` sur `true`, seules les achats existants seront mis à jour, et aucun nouvel achat ne sera créé.<br>Mapper les attributs de type tableau pour ajouter plusieurs articles d'achat. Les attributs de type tableau doivent être de longueur égale.<br>Les attributs à valeur unique peuvent être utilisés et s'appliqueront à chaque élément.|
| Acheter le modèle | Les modèles peuvent être utilisés pour transformer les données avant qu'elles ne soient envoyées à Braze.<br>\- Définissez un modèle d'achat si vous avez besoin de prendre en charge des objets imbriqués.<br>Lorsqu'un modèle d'achat est défini, la configuration définie dans la section des achats de votre action sera ignorée.<br>Reportez-vous au [Guide des modèles](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium pour en savoir plus.|
| Variable du modèle d’achat | Fournir les variables de modèle de produit comme entrée de donnée. Reportez-vous au [Guide des variables de modèle](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium pour en savoir plus. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example.png %})

{% endtab %}
{% tab Suppression d'un utilisateur - hors lot %}

Cette action vous permet de supprimer des utilisateurs du tableau de bord de Braze.

| Paramètres | Description |
| ---------- | ----------- |
| ID utilisateur | Utilisez ce champ pour mapper le champ ID utilisateur Tealium à son équivalent Braze. <br><br>\- Mapper un ou plusieurs attributs d'ID utilisateur. Lorsque plusieurs identifiants sont spécifiés, la première valeur non vide est choisie en fonction de l'ordre de priorité suivant : ID externe, ID Braze, Nom d'alias, et libellé d'alias.<br>Lors de la spécification d'un alias d'utilisateur, le nom d'alias et le libellé d'alias doivent être définis tous les deux.<br><br>Pour plus d'informations, consultez [`/users/delete`l'endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete.png %})

Si vous souhaitez modifier vos options choisies, sélectionnez **Retour** pour modifier ou **Terminer** pour compléter.

{% endtab %}
{% endtabs %}

Sélectionnez **Continuer**.

Votre connecteur s'affiche désormais dans la liste des connecteurs sur votre page d'accueil Tealium. <br>![][13]{: style="max-width:80%;"}

Veillez à sélectionner **Enregistrer / Publier** pour votre connecteur lorsque vous avez terminé. Les actions que vous avez configurées se déclencheront maintenant lorsque les connexions de déclencheur seront remplies. 

### Étape 3 : Testez votre connecteur Tealium

Après que votre connecteur soit opérationnel, vous devriez le tester pour vous assurer qu'il fonctionne correctement. La façon la plus simple de tester votre connecteur est d'utiliser l’**outil de traçage Tealium**. Pour commencer à utiliser l’outil de traçage, assurez-vous d'avoir ajouté l'extension de navigateur des outils Tealium.

1. Pour démarrer un nouveau traçage, sélectionnez **Traçage** dans la barre latérale sous les options **Côté serveur**. Sélectionnez **Démarrer** et capturez l'ID de la trace.
2. Ouvrez l'extension du navigateur et entrez l'ID de traçage dans AudienceStream Trace.
3. Examinez le journal en temps réel.
4. Recherchez l'action que vous souhaitez valider en sélectionnant l'entrée **Actions déclenchées** pour la développer.
5. Recherchez l'action que vous voulez valider et consultez l’état du journal. 

Reportez-vous à la [documentation de l’outil de traçage][21] de Tealium pour des instructions plus détaillées sur sa mise en œuvre.

## démonstration d'intégration

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Dépassements potentiels de point de donnée

Il existe principalement trois façons de dépasser accidentellement les limites de données lors de l'intégration de Braze via Tealium :

#### Envoi de données en double - n'envoyez que des deltas d'attributs Braze

Tealium ne transmet pas les deltas d'attributs utilisateur à Braze. Par exemple, si vous avez une action eventstream qui suit le prénom, l'e-mail et le numéro de téléphone portable d'un utilisateur, Tealium enverra les trois attributs à Braze chaque fois que l'action est déclenchée. Tealium ne cherchera pas ce qui a changé ou a été mis à jour et n'enverra que ces informations.

**Solution** : <br>Vous pouvez vérifier votre backend pour évaluer si un attribut a changé ou non, et si c'est le cas, appeler les méthodes pertinentes de Tealium pour mettre à jour le profil utilisateur. **C'est ce que font généralement les utilisateurs qui intègrent Braze directement.** <br>**OU**<br> Si vous ne stockez pas votre propre version d'un profil utilisateur dans votre backend et ne pouvez pas dire si les attributs changent ou non, vous pouvez utiliser AudienceStream et
[créer des enrichissements](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/) pour n'envoyer les attributs utilisateur que lorsque les valeurs ont changé. Voir la documentation de Tealium sur les [règles d'enrichissement](https://docs.tealium.com/server-side-connectors/braze-connector/).

#### Envoi de données non pertinentes ou réécriture inutile de données

Si vous avez plusieurs EventStreams qui ciblent le même flux d'événements, **toutes les actions activées pour ce connecteur** se déclencheront automatiquement à chaque fois qu'une action unique est déclenchée, \*\*ce qui pourrait également entraîner l'écrasement de données dans Braze et la consommation de points de données inutiles.\\N- Vous ne pouvez pas vous permettre d'utiliser un seul connecteur pour un seul événement.

**Solution** : <br>Configurez une spécification d'événement distincte ou un flux pour suivre chaque action. <br>**OU**<br> Désactivez les actions (ou connecteurs) que vous ne souhaitez pas déclencher en utilisant les commutateurs dans le tableau de bord Tealium.

#### Initialisation de Braze trop tôt

Les utilisateurs intégrant Tealium en utilisant la balise du SDK Web Braze peuvent voir une augmentation spectaculaire de leur MAU. **Si Braze est initialisé au chargement de la page, Braze créera un profil anonyme chaque fois qu'un utilisateur web navigue sur le site pour la première fois.** Certains peuvent vouloir suivre le comportement des utilisateurs uniquement lorsque ceux-ci ont effectué une action, telle que "Connecté" ou "Regardé une vidéo", afin de réduire leur nombre de MAU.

**Solution** : <br>Configurez les [règles de chargement](https://docs.tealium.com/iq-tag-management/load-rules/about/) pour déterminer exactement quand et où une étiquette se charge sur votre site. 

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/
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
Il y a [19]: https://docs.tealium.com/iq-tag-management/events/about/
Il y a [21]: https://docs.tealium.com/server-side/connectors/trace/about/
[22]: {% image_buster /assets/img/tealium/tealium_overview.png %}
[23]: {% image_buster /assets/img/tealium/remote_mappings.png %}
