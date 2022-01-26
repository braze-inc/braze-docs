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

L’intégration de Braze et de Tealium vous permet de suivre vos utilisateurs et d’acheminer des données vers différents fournisseurs d’analyse. Tealium vous permet de :
- Synchronisez les audiences de Tealium avec [AudienceStream]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/) à Braze pour une utilisation dans la campagne de Braze et la segmentation de Canvas .
- [Importer des données sur des plates-formes](#choose-your-integration-type). Braze offre à la fois une intégration [côte à côte](#side-by-side-sdk-integration) de SDK pour votre Android, iOS, et des applications web et une intégration de [serveur à serveur](#server-to-server-integration) pour vos services d'arrière-plan.<br><br>

{% tabs %}
{% tab EventStream %}

Tealium EventStream est un concentrateur de données et d'API qui se trouve au centre de vos données. EventStream gère l'ensemble de la chaîne logistique de données depuis la configuration et l'installation jusqu'à l'identification, la validation et l'amélioration des données utilisateur entrantes. EventStream prend des actions en temps réel avec les flux d'événements et les connecteurs. Voici la liste des fonctionnalités qui composent le [EventStream](https://community.tealiumiq.com/t5/Customer-Data-Hub/Introduction-to-EventStream/ta-p/20387#toc-hId--2077371752).
- Sources de données (installation et collecte de données)
- Événements en direct (inspection des données en temps réel)
- Spécifications et attributs de l'événement (exigences de la couche de données et validation)
- Flux d'événements (types d'événements filtrés)
- Connecteurs d'événements (actions du hub API)

{% endtab %}
{% tab AudienceStream %}

Tealium AudienceStream est un moteur de segmentation de clients omnicanal et d'action en temps réel. AudienceStream prend les données qui affluent dans EventStream et crée des profils de visiteurs qui représentent les attributs les plus importants de l'engagement de vos clients avec votre marque. Consultez notre documentation sur la façon de configurer [AudienceStream]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_audience_stream/).

{% endtab %}
{% endtabs %}

{% alert important %}
Veuillez noter que Tealium AudienceStreams et EventStreams sont empilés selon les spécifications de Braze afin que vous ne courriez pas le risque de dépasser la limite de taux [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Veuillez contacter le support de Braze ou votre CSM si vous avez des questions.
{% endalert %}

## Pré-requis

| Exigences                                                                                                                         | Libellé                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Tealium                                                                                                                    | Un [compte Tealium](https://my.tealiumiq.com/) avec accès au serveur et au côté client est requis pour tirer parti de ce partenariat.                                                                                                                                                                             |
| Bibliothèques source et source [Tealium installées](https://community.tealiumiq.com/t5/Customer-Data-Hub/Data-Sources/ta-p/17933) | L'origine de toutes les données envoyées dans Tealium, telles que les applications mobiles, les sites Web ou les serveurs d'arrière-plan.<br><br>Vous devez installer les bibliothèques dans votre application, votre site ou votre serveur avant de pouvoir configurer un connecteur Tealium réussi. |
| Point de terminaison REST Braze                                                                                                   | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints).                                                                                                                                                                  |
| Clé d'identification de l'application Braze                                                                                       | (Side-by-side only) Votre clé d'identification de l'application. <br><br>son peut être trouvé dans le **Tableau de bord Braze > Gérer les paramètres > Clé API**.                                                                                                                                     |
| Clé API REST                                                                                                                      | (Server-to-server uniquement) Une clé d'API Braze REST avec les permissions `users.track` et `users.delete`. <br><br>Ceci peut être créé dans le **tableau de bord Braze** > **Console développeur** > **Clé d'API REST** > **Créer une nouvelle clé API**                                            |
{: .reset-td-br-1 .reset-td-br-2}

## Choisissez votre type d'intégration

| Intégration                                        | Détails du produit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [côte à côte](#side-by-side-sdk-integration)       | Carte le SDK de Tealium vers le SDK de Braze, permettant d'accéder à des fonctionnalités plus profondes et une utilisation plus complète de Braze que l'intégration serveur-serveur.<br><br>Si vous prévoyez d'utiliser des commandes distantes de Braze, notez que Tealium ne supporte pas toutes les méthodes Braze (par exemple, les cartes de contenu). Pour utiliser une méthode Braze qui n'est pas mappée par une commande distante correspondante, vous devrez appeler la méthode en ajoutant du code natif Braze à votre code de base.                                                        |
| [Serveur à serveur](#server-to-server-integration) | Transfère les données de Tealium vers le point de terminaison [de Braze / trace]({{site.baseurl}}/api/endpoints/user_data?redirected=true#user-track-endpoint) .<br><br>Ne prend pas en charge les fonctionnalités de Braze UI telles que la messagerie intégrée, le fil d'actualités ou les notifications push. Il existe également des données capturées automatiquement (sessions, première application utilisée, et dernière application) qui ne sont pas disponibles via cette méthode.<br><br>Considérez une intégration côte à côte si vous souhaitez utiliser ces fonctionnalités. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration de SDK côte à côte

### Commandes distantes

Les commandes distantes vous permettent de déclencher du code dans vos applications en utilisant un tag dans Tealium iQ Tag Management - qui collecte, contrôle et livre les données des événements à partir des applications mobiles. Vous pouvez facilement utiliser la gestion des balises pour configurer une implémentation native de Braze sans ajouter de code spécifique au Brésil à vos applications. À la place, le module de commande à distance de Braze installera et compilera automatiquement les bibliothèques requises de Braze. Pour utiliser la commande à distance de Braze, vous aurez besoin de bibliothèques Tealium installées dans vos applications.

À l'aide de commandes à distance, les SDK Braze et Tealium fonctionnent en tandem, vous permettant de faire des appels depuis le SDK Tealium - via les serveurs Braze - vers Braze. Ici, les balises de Tealium retournent à être cartographiées par le Brésil. **Le SDK Braze continuera à gérer les affichages, les renvois de messages et les analyses de messages.**

Braze mobile commande à distance carte les attributs par défaut de l'utilisateur et les attributs personnalisés et peut suivre les achats et les événements personnalisés. Il vous permet également de suivre l'emplacement et les données sociales sur Twitter et Facebook - comme le nombre de suiveurs ou d'amis d'un utilisateur. Consultez le tableau de commandes à distance pour voir les méthodes de Braze correspondantes.

!\[Remote command mappings\]\[23\]{: style="max-width:60%;"}

Vous pouvez trouver plus de détails sur la façon de configurer le tag de commande à distance de Braze, ainsi qu'un aperçu des méthodes prises en charge dans la documentation [du développeur Tealium](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Mobile-Remote-Command-Tag-Setup-Guide/ta-p/32828).

{% alert important %}
Les commandes à distance mobiles Braze ne prennent pas en charge toutes les méthodes Braze (par exemple, les cartes de contenu). Pour utiliser une méthode Braze qui n'est pas mappée à travers une commande distante correspondante, vous devrez appeler la méthode en ajoutant du code natif Braze à votre code de base.
{% endalert%}

### Balise Braze Web SDK

Utilisez Braze Web SDK Tag pour déployer le Web SDK de Braze sur votre site Web. [Tealium iQ Tag Management](https://community.tealiumiq.com/t5/iQ-Tag-Management/Introduction-to-iQ-Tag-Management/ta-p/15883) permet aux clients d'ajouter Braze comme un tag dans le tableau de bord de Tealium pour suivre l'activité des visiteurs. Les balises sont généralement utilisées par les marketeurs pour comprendre l'efficacité de la publicité en ligne, du marketing par courriel et de la personnalisation du site.

1. Dans Tealium, accédez à **iQ [Gestion des balises](https://community.tealiumiq.com/t5/iQ-Tag-Management/Tags/ta-p/5016) > Tags > + Ajouter Tag > Braze Web SDK**.
2. Dans la boîte de dialogue **Configuration des balises** , entrez votre clé d'identification Braze, Braze REST terminal, et Braze Web SDK [version de code](https://github.com/Appboy/appboy-web-sdk/blob/master/CHANGELOG.md). Vous pouvez également activer/désactiver la journalisation de débogage pour enregistrer les informations de débogage dans la console web.
3. Dans la boîte de dialogue **[Charger les règles]((https://community.tealiumiq.com/t5/iQ-Tag-Management/Load-Rules/ta-p/5098))** sélectionnez **Créer une règle** pour déterminer quand et où charger une instance de ce tag sur votre site.
4. Dans la boîte de dialogue **[Data Mappings](https://community.tealiumiq.com/t5/iQ-Tag-Management/Data-Mappings/ta-p/10645#mapping_data_sources)** , sélectionnez **Create Mappings** pour mapper les données de Tealium au Brésil. Les variables de destination de la balise Braze Web SDK sont intégrées dans l'onglet **Data Mapping** de la balise. Les [tables suivantes](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Web-SDK-Tag-Setup-Guide/ta-p/20106#toc-hId--2077373923)) listent les catégories de destination disponibles et décrivent chaque nom de destination.
5. Sélectionnez **Terminer**.

### Ressources d'intégration côte à côte

- Commande distante iOS : [Documentation de Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Dépôt Tealium Github](https://github.com/Tealium/tealium-ios-braze-remote-command)
- Commande distante Android : [Documentation de Tealium](https://docs.tealium.com/platforms/remote-commands/integrations/braze/), [Dépôt de Tealium Github](https://github.com/Tealium/tealium-android-braze-remote-command)
- Balise Web SDK : [Documentation de Tealium](https://community.tealiumiq.com/t5/Client-Side-Tags/Braze-Web-SDK-Tag-Setup-Guide/ta-p/20106)

## Intégration du serveur à serveur

Cette intégration transfère les données de Tealium à l'API REST de Braze.

L'intégration de serveur à serveur ne prend pas en charge les fonctionnalités de Braze UI telles que la messagerie intégrée, le fil d'actualités ou les notifications push. Il existe également des données capturées automatiquement (sessions, première application utilisée, et dernière application) qui ne sont pas disponibles via cette méthode.

Si vous souhaitez utiliser ces données et ces fonctionnalités, considérez notre intégration [côte à côte]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#side-by-side-sdk-integration) de SDK.

### Étape 1 : Mettre en place une source

Tealium nécessite que vous définissiez d'abord une source de données valide à partir de laquelle votre connecteur peut puiser.
1. À partir de la barre latérale gauche dans Tealium sous **côté serveur**, accédez à **Sources > Sources de données > + Ajouter une source de données**.
2. Localisez la plateforme **HTTP API** dans les catagories disponibles, et nommez votre application HTTP API, c'est un champ obligatoire.<br>!\[Data Source\]\[6\]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}
3. Dans les options **Spécifications d'événement** , choisissez les [spécifications d'événement](https://community.tealiumiq.com/t5/Customer-Data-Hub/Event-Specifications/ta-p/19329) que vous souhaitez inclure. Les spécifications de l'événement vous aident à identifier les noms d'événements et les attributs nécessaires pour suivre votre installation. Ces spécifications seront appliquées aux événements entrants.<br>! Spécifications d'événements][7]{: style="max-width:80%;margin-left:15px;margin-bottom:15px; }<br>Prenez le temps de réfléchir aux données qui vous sont les plus précieuses et aux spécifications qui vous semblent les plus appropriées pour votre cas d'utilisation. [Des spécifications d'événements personnalisés][19] sont également disponibles. <br>
4. Le prochain dialogue passe à l'étape **Obtenir le code**. Le code de base et le code de suivi des événements fournis ici servent de guide d'installation. Téléchargez le PDF fourni si vous souhaitez partager ces instructions avec votre équipe. Sélectionnez **Enregistrer & Continuer** une fois terminé. <br>!\[Get Code\]\[8\]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>
5. Vous pourrez maintenant voir votre source sauvegardée ainsi que ajouter ou supprimer les spécifications d'événement. <br>!\[Connector\]\[18\]{: style="max-width:80%;margin-left:15px;margin-bottom:15px;"}<br>Dans la vue de la source de données détaillée, vous pouvez effectuer les actions suivantes :
- Voir et copier la clé source de données
- Voir les instructions d'installation
- Retournez à la page **Obtenir le code**
- Ajouter ou supprimer les spécifications de l'événement
- Voir les événements en direct liés à une spécification d'événement
- Et plus...<br>
6. Enfin, sélectionnez **Enregistrer / Publier** en haut de la page. Si vous ne publiez pas votre source, vous ne pourrez pas le trouver lors de la configuration de votre connecteur Braze.

Pour de plus amples instructions sur la configuration et l'édition de votre source de données, consultez [les sources de données](https://community.tealiumiq.com/t5/Customer-Data-Hub/Data-Sources/ta-p/17933).

### Étape 2 : Créer un connecteur d'événement

Un connecteur est une intégration entre Tealium et un autre fournisseur utilisé pour transmettre des données. Ces connecteurs contiennent des actions qui représentent les API supportées par leur partenaire.

1. À partir de la barre latérale gauche dans Tealium sous **côté serveur**, accédez à **EventStream > Connecteurs d'événements**.
2. Sélectionnez le bouton bleu **+ Ajouter un connecteur** pour regarder à travers la place de marché du connecteur. Dans la nouvelle boîte de dialogue qui apparaît, utilisez la recherche de spotlight pour trouver le connecteur **Braze**.
3. Pour ajouter ce connecteur, cliquez sur la tuile du connecteur **Braze**. Une fois cliqué, vous pouvez consulter le résumé de la connexion et une liste des informations requises, des actions prises en charge et des instructions de configuration. La configuration comprend quatre étapes : source, configuration, action et résumé.

#### Source

Une fois que la source a été configurée, revenez à la page du connecteur Braze sous **EventStream > Connecteurs d'événements > + Ajouter Conncetor > Braze**.

Dans le dialogue qui s'ouvre, sélectionnez la source de données que vous venez de construire et sous **Event Feed**, sélectionnez **Tous les événements** ou une spécification d'événement spécifique, si nécessaire. Cliquez sur **Continuer**.

#### Configuration

Ensuite, sélectionnez **Ajouter un connecteur** au bas de la page. Vous devez nommer votre connecteur et fournir votre point de terminaison Braze API et votre clé API Braze REST ici.

!\[Create Configuration\]\[15\]{: style="max-width:70%;"}

Si vous avez créé un connecteur avant, vous pouvez optionnellement utiliser un connecteur existant dans la liste disponible et le modifier pour correspondre à vos besoins avec l'icône crayon ou le supprimer avec l'icône de la corbeille.

#### Action

Ensuite, nommez l'action de votre connecteur et sélectionnez un type d'action qui enverra des données en fonction du mapping que vous configurez. Ici, vous associerez les attributs Braze aux noms d'attributs de Tealium. Selon le type d'action que vous choisissez, il y aura une sélection variée de champs requis par Tealium. Voici des exemples et des explications de ces champs.

{% alert important %}
**Notez que tous les champs proposés ne sont pas obligatoires**. <br>Si vous souhaitez sauter un champ, Tealium vous demande de le minimiser avant de passer à l'étape suivante.

![Minimize]({% image_buster /assets/img/tealium/minimize.gif %}){: style="largeur-max-80%"}
{% endalert %}

{% tabs local %}
{% tab Track User %}

Cette action vous permet de suivre les attributs des utilisateurs, des événements et des achats en une seule action.

| Paramètres                              | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Identifiant de l'utilisateur            | Utilisez ce champ pour associer le champ ID de l'utilisateur de Tealium à son équivalent Braze. <br><br>- L'ID externe et l'ID Braze ne doivent pas être spécifiés si l'importation de jetons push est importée.<br>- Si vous spécifiez un alias d'alias, le nom de l'alias et l'étiquette de l'alias doivent être définis. <br><br>Pour plus d'informations, consultez le Braze [/users/track endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Attributs de l'utilisateur              | Utilisez les noms de champs de profil utilisateur existants de Braze pour mettre à jour les valeurs de profil d'utilisateur dans le tableau de bord Braze ou ajoutez vos propres données personnalisées [d'attribut utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/) aux profils d'utilisateur.<br><br>- Par défaut, de nouveaux utilisateurs seront créés si on n'existe pas.<br>- En définissant **Mettre à jour uniquement** à `vrai`, seuls les utilisateurs existants seront mis à jour et aucun nouvel utilisateur ne sera créé.                                                                                                                                                                                                                                                                                                                                                                                                |
| Modifier les attributs de l'utilisateur | Utilisez ce champ pour incrémenter ou décrémenter certains attributs utilisateur<br><br>- Les attributs entiers peuvent être incrémentés par des entiers positifs ou négatifs.<br>- Les attributs d'un tableau peuvent être modifiés en ajoutant ou en supprimant des valeurs des tableaux existants.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Attributs de l'événement                | Un événement représente une seule occurrence d'un événement personnalisé par un utilisateur particulier à un horodatage. Utilisez ce champ pour suivre et cartographier les attributs d'événement comme ceux de l'objet [événement Braze]({{site.baseurl}}/api/objects_filters/event_object/). <br><br>- Attribut événement `Nom` est requis pour chaque événement associé.<br>- Attribut événement `Temps` est automatiquement défini à maintenant, sauf si explicitement associé. <br>- Par défaut, de nouveaux événements seront créés si on n'existe pas. En définissant `Update Existing Only` à `true`, seuls les événements existants seront mis à jour et aucun nouvel événement ne sera créé.<br>- Attributs de type tableau de carte pour ajouter plusieurs événements. Les attributs de type de tableau doivent être de longueur égale.<br>- Les attributs de valeur unique peuvent être utilisés et appliqués à chaque événement. |
| Attributs d'achat                       | Utilisez ce champ pour suivre et cartographier les attributs d'achat des utilisateurs comme ceux de l'objet d'achat [Braze]({{site.baseurl}}/api/objects_filters/purchase_object/).<br><br>- Attributs d'achat `ID Produit`, `La devise` et `le prix` sont requis pour chaque achat cartographié.<br>- L'attribut d'achat `Time` est automatiquement défini à maintenant, sauf si explicitement associé.<br>- Par défaut, de nouveaux achats seront créés si on n'existe pas. En définissant `Update Existing Only` à `true`, seuls les achats existants seront mis à jour et aucun nouvel achat ne sera créé.<br>- Attributs de type tableau de carte pour ajouter plusieurs articles d'achat. Les attributs de type de tableau doivent être de longueur égale.<br>- Les attributs de valeur unique peuvent être utilisés et s'appliqueront à chaque élément.                                                                                |
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

Sélectionnez **Continuer**.

#### Summary

Voir le résumé du connecteur que vous avez créé. Si vous souhaitez modifier les options de votre choix, sélectionnez **Retour** pour modifier ou **Terminer** pour terminer.

!\[Connector Summary\]\[16\]{: style="max-width:80%;"}

Votre connecteur s'affiche maintenant dans la liste des connecteurs sur votre page d'accueil de Tealium. <br>!\[Connector\]\[13\]{: style="max-width:80%;"}

Assurez-vous de **Enregistrer / Publier** votre connecteur une fois terminé. Les actions que vous avez configurées vont maintenant se déclencher lorsque les connexions de déclenchement seront atteintes.

### Étape 3 : Testez votre connecteur de Tealium

Une fois que votre connecteur est opérationnel, vous devriez le tester pour vous assurer qu'il fonctionne correctement. La façon la plus simple de tester ceci est d'utiliser le Tealium **Outil de traçage**.

1. Pour démarrer une nouvelle trace, sélectionnez **Trace** dans la barre latérale gauche sous les options **Server-Side**.
2. Examinez le journal en temps réel.
3. Vérifiez l'action que vous voulez valider en cliquant sur l'entrée **Actions Déclenchées** pour développer.
4. Recherchez l'action que vous souhaitez valider et afficher le statut du journal.

Pour des instructions plus détaillées sur l'implémentation de l'outil Trace de Tealium, consultez leur [documentation de traces][21].

## Surcharges de données potentielles

Il y a trois moyens primaires de frapper accidentellement les dépassements de données lors de l'intégration de Braze dans Tealium :

#### La journalisation des données est insuffisante
Tealium n'envoie pas les deltas de Braze des attributs de l'utilisateur. Par exemple, si vous avez une action EventStream qui suit le prénom d'un utilisateur et le numéro de téléphone cellulaire, Tealium enverra les trois attributs à Braze chaque fois que l'action est déclenchée. Tealium ne cherchera pas ce qui a changé ou a été mis à jour et n'enverra que cette information.<br><br> **Solution**: <br>Vous pouvez vérifier votre backend pour évaluer si un attribut a changé ou pas, et, le cas échéant, appelez les méthodes pertinentes de Tealium pour mettre à jour le profil de l’utilisateur. **C'est ce que font les utilisateurs qui intègrent Braze directement.** <br>**OU**<br> Si vous ne stockez pas votre propre version d'un profil utilisateur dans votre backend et ne pouvez pas dire si les attributs changent ou pas, vous pouvez utiliser AudienceStream pour suivre les changements d'attributs de l'utilisateur.

#### Envoi de données non pertinentes
Si vous avez plusieurs EventStreams qui ciblent le même flux d'événement, **toutes les actions activées pour ce connecteur** seront automatiquement déclenchées à chaque fois qu'une seule action est déclenchée, **cela pourrait aussi résulter en l'écrasement des données en Brésil.**<br><br> **Solution**: <br>Mettre en place une spécification d'événement séparée ou un flux pour suivre chaque action. <br>**OU**<br> Désactivez les actions (ou connecteurs) que vous ne voulez pas tirer en utilisant les interrupteurs du tableau de bord de Tealium.

#### Initialisation de Braze trop tôt
Les utilisateurs qui intègrent Tealium à l'aide de la balise Braze Web SDK peuvent assister à une augmentation spectaculaire de leur MAU. **Si Braze est initialisé au chargement de la page, Braze créera un profil anonyme chaque fois qu'un utilisateur navigue sur le site pour la première fois.** Certains peuvent ne vouloir suivre le comportement de l'utilisateur qu'une fois que les utilisateurs ont terminé une action, comme « Connecté » ou « Vidéo visionnée », pour abaisser leur nombre de MAU. <br><br> **Solution**: <br>Configurer des règles de charge pour déterminer exactement quand et où un tag se charge sur votre site. Vous pouvez en savoir plus sur les règles de charge et comment les configurer dans le [centre d'apprentissage de Tealium](https://community.tealiumiq.com/t5/Customer-Data-Hub/Building-an-Audience/ta-p/11881).
[5]: {% image_buster /assets/img/tealium/braze_connector_marketplace.png %} [6]: {% image_buster /assets/img/tealium/data_source.png %} [7]: {% image_buster /assets/img/tealium/event_specs. ng %} [8]: {% image_buster /assets/img/tealium/get_code.png %} [9]: {% image_buster /assets/img/tealium/summary.png %} [13]: {% image_buster /assets/img/tealium/summary_list. ng %} [15]: {% image_buster /assets/img/tealium/create_configuration.png %} [16]: {% image_buster /assets/img/tealium/connector_summary.png %} [17]: {% image_buster /assets/img/tealium/save_publish. ng %} [18]: {% image_buster /assets/img/tealium/braze_connection.png %} [22]: {% image_buster /assets/img/tealium/tealium_overview. ng %} [23]: {% image_buster /assets/img/tealium/remote_mappings.png %}

[19]: https://community.tealiumiq.com/t5/Customer-Data-Hub/Event-Specifications/ta-p/19329#toc-hId--2078027338
[21]: https://community.tealiumiq.com/t5/Customer-Data-Hub/Trace/ta-p/12058