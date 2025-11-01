---
nav_title: Permissions
article_title: Permissions de Braze
page_order: 2
page_type: reference
description: "Cet article de référence couvre le fonctionnement des permissions des utilisateurs chez Braze. Ici, vous apprendrez à modifier et à définir les autorisations des utilisateurs, en choisissant qui peut accéder à vos apps dans le tableau de bord."
tool: Dashboard

---

# Permissions de Braze

> Apprenez à créer des jeux de permissions, à créer des rôles, à modifier les permissions des utilisateurs et à exporter les permissions des utilisateurs, afin de vous assurer que vos utilisateurs n'accèdent qu'aux espaces de travail et aux fonctionnalités dont ils ont le plus besoin.

## Création d'un ensemble de permissions

Utilisez les jeux de permissions pour regrouper les permissions liées à des domaines ou à des actions spécifiques. Ils peuvent être appliqués aux utilisateurs du tableau de bord qui ont besoin du même accès dans différents espaces de travail. Pour créer un jeu de permissions, accédez à **Paramètres** > **Paramètres de permissions**, puis sélectionnez **Créer un jeu de permissions**. Pour une description de chaque autorisation, voir [Liste des autorisations.](#list-of-permissions)

{% tabs local %}
{% tab example permission sets %}
|Nom|Permissions|
\|-----------|----------------|
Développeurs|"Accéder à la console de développement"|Développeurs|"Accéder à la console de développement"|Développeurs|"Accéder à la console de développement".
|Marketeurs|"Accédez aux campagnes, aux toiles, aux cartes, aux drapeaux de fonctionnalité, aux segments, à la bibliothèque multimédia et aux centres de préférences". <br> "Gérer les ressources de la bibliothèque multimédia".
| Gestion des utilisateurs|"Gérer les utilisateurs du tableau de bord" <br> "Gérer les Teams".
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Créer un rôle

Les rôles permettent une meilleure structuration en regroupant vos autorisations personnalisées individuelles avec les contrôles d'accès à l'espace de travail. Ceci est particulièrement utile si vous avez plusieurs marques ou espaces de travail régionaux dans un seul tableau de bord. Grâce aux rôles, vous pouvez ajouter les utilisateurs du tableau de bord aux bons espaces de travail et leur accorder directement les autorisations associées. Pour une description de chaque autorisation, voir [Liste des autorisations.](#list-of-permissions)

{% tabs local %}
{% tab example roles %}
| Nom du rôle | Espace de travail | Permissions  
----------- | ----------- | ---------
| Marketer - Fashion Brands | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "Accédez aux campagnes, aux canevas, aux cartes, aux drapeaux de fonctionnalité, aux segments, à la bibliothèque multimédia et au centre de préférences"<br>"Gérer les ressources de la bibliothèque multimédia" |
| Marketer - Skincare Brands | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Access Campaigns, Canvases, Cards, Feature Flags, Segments, Media Library, and Preference Centers" <br>"Gérer les ressources de la bibliothèque multimédia" |
| Gestion des utilisateurs - Toutes les marques | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Gérer les utilisateurs du tableau de bord"<br>"Gestion des Teams".
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## En quoi les jeux de permissions et les rôles diffèrent-ils de Teams ?

{% multi_lang_include permissions.md content="Differences" %}

### Éléments à prendre en compte pour ajouter des autorisations d'utilisateur à Teams

Vous pouvez rencontrer des difficultés lorsque vous essayez d'enregistrer des autorisations dans le tableau de bord de Braze, notamment lorsque vous ajoutez ou supprimez des utilisateurs d'un espace de travail, ou lorsque vous les ajoutez à une équipe. Le bouton **Enregistrer/Mettre à jour les** utilisateurs peut devenir grisé si les autorisations de l'utilisateur sont identiques à celles dont il dispose déjà au niveau de l'espace de travail. Cette restriction existe parce qu'il n'y a aucun avantage à avoir une Teams si tous les utilisateurs possèdent les mêmes autorisations que l'ensemble de l'espace de travail.

Pour réussir à ajouter un utilisateur à une Teams tout en conservant les mêmes autorisations, n'attribuez aucune autorisation au niveau de l'espace de travail. Au lieu de cela, attribuez des autorisations exclusivement au niveau de l'équipe.

## Utilisateurs limités

Les utilisateurs limités disposent d'autorisations spécifiques qui leur permettent de gérer certains aspects du tableau de bord de Braze tout en ayant des restrictions par rapport aux administrateurs de l'entreprise et aux administrateurs de l'espace de travail.

| Permissions | Les utilisateurs limités peuvent modifier les permissions d'autres utilisateurs limités si l'autorisation "Gérer les utilisateurs du tableau de bord" est cochée. Ils peuvent également créer de nouveaux utilisateurs limités et modifier leurs autorisations. Cependant, ils ne peuvent pas créer ou gérer des comptes d'administrateurs de l'entreprise. |
| Si un utilisateur limité dispose de toutes les autorisations à l'exception de "App Group Admin", il aura toujours accès à toutes les autres autorisations généralement accordées à un administrateur d'espace de travail. |
| Si un utilisateur limité a coché la case "Gérer les utilisateurs du tableau de bord" pour un groupe d'applications (tel que Dev) mais pas pour un autre (tel que Prod), il ne verra pas les autorisations du groupe d'applications Prod dans son profil "Gérer les utilisateurs". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparaison des utilisateurs limités

| Type d'utilisateur limité | Description |
| --- | --- |
| Groupe d'applications admin. | Les administrateurs de groupes d'applications disposent d'autorisations spécifiques à la gestion des groupes d'applications, mais n'ont pas la même autorité que les administrateurs d'entreprises. Les utilisateurs limités peuvent hériter d'autorisations similaires à celles des administrateurs de groupes d'applications si les autorisations nécessaires sont cochées. |
| Administrateur de l'entreprise | Les administrateurs d'entreprise disposent d'autorisations plus étendues, y compris la possibilité de supprimer des utilisateurs du tableau de bord. Toutefois, ils ne peuvent pas supprimer leurs propres comptes et doivent contacter un autre administrateur de l'entreprise pour ce faire. |
| Autorisation de base en lecture seule | Pour accéder à certaines parties du tableau de bord, telles que la page partenaires technologiques, les utilisateurs doivent disposer d'une autorisation de base en lecture seule. Il faut notamment que l'option "Gérer les intégrations externes" soit activée, ainsi que les autorisations d'accès aux campagnes, aux canevas, aux cartes, aux segments et à la bibliothèque multimédia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erreur d'accès limité

Les utilisateurs peuvent recevoir des messages tels que "Accès limité". Vous n'avez pas l'autorisation d'accéder à cette page". Dans ce cas, l'administrateur du compte doit vérifier s'il peut résoudre le problème en désactivant et en réactivant les autorisations de l'utilisateur.

{% alert note %}
Il n'est pas possible de fusionner ou d'importer des autorisations d'utilisateurs d'un tableau de bord à un autre.
{% endalert %}

## Modifier les autorisations d'un utilisateur

Pour modifier les autorisations actuelles d'un utilisateur en matière d'administration, d'entreprise ou d'espace de travail, accédez à **Paramètres** > **Utilisateurs de l'entreprise**, puis sélectionnez son nom.

La page "Utilisateurs de l'entreprise" dans Braze avec un utilisateur listé dans les résultats.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %}){: style="max-width:80%;"}

{% tabs local %}
{% tab Admin %}

### Administrateur

Les administrateurs ont accès à toutes les fonctionnalités et peuvent modifier tous les paramètres de l'entreprise. Ils peuvent le faire :

- Modifier les [paramètres d'approbation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Ajouter, modifier, supprimer, suspendre ou annuler la suspension d'autres [utilisateurs de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users).
- Exporter les utilisateurs de Braze au format CSV

Pour accorder ou supprimer les privilèges d'administrateur, sélectionnez **Cet utilisateur est un administrateur**, puis sélectionnez **Mettre à jour l'utilisateur.**

Les détails de l'utilisateur sélectionné avec la case à cocher admin en évidence.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:40%;"}

{% alert warning %}
Si vous retirez les privilèges d'administrateur à un utilisateur, il ne pourra pas accéder à Braze tant que vous ne lui aurez pas attribué au moins une autorisation [au niveau de l'entreprise](#company) ou de l' [espace de travail](#workspace).
{% endalert %}

{% endtab %}
{% tab Company %}

### Entreprise

Pour gérer les autorisations suivantes au niveau de l'entreprise pour un utilisateur, cochez ou décochez la case en regard de l'autorisation en question. Lorsque vous avez terminé, sélectionnez **Mettre à jour l'utilisateur.**

|Nom de la permission|Description|
|----------|-----------|
|Gérer les paramètres de l'entreprise|Permet aux utilisateurs de modifier n'importe quel paramètre de l'entreprise.|
|Créer et supprimer des espaces de travail|Permet aux utilisateurs de créer et de supprimer des espaces de travail.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Espace de travail

Vous pouvez donner à un utilisateur des autorisations différentes pour chaque espace de travail auquel il appartient dans Braze. Pour gérer leurs autorisations au niveau de l'espace de travail, sélectionnez **Sélectionner les espaces de travail et les autorisations**, puis choisissez manuellement leurs autorisations pour sélectionner ou attribuer un ensemble d'autorisations [que vous avez précédemment créé](#creating-a-permission-set).

Si vous devez donner à un utilisateur des autorisations différentes pour différents espaces de travail, répétez ce processus autant de fois que nécessaire. Pour une description de chaque autorisation, voir [Liste des autorisations.](#list-of-permissions)

{% subtabs %}
{% subtab Select manually %}

Sous **Espaces de travail**, choisissez un ou plusieurs espaces de travail dans la liste déroulante. Ensuite, sous **Autorisations**, choisissez une ou plusieurs autorisations dans la liste déroulante. Ces autorisations ne leur seront attribuées que pour les espaces de travail que vous avez sélectionnés. En option, vous pouvez sélectionner **Activer l'accès administrateur** si vous souhaitez leur donner toutes les autorisations pour cet espace de travail.

Lorsque vous avez terminé, sélectionnez **Mettre à jour l'utilisateur.**

Les autorisations au niveau de l'espace de travail sont sélectionnées manuellement dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Sous **Espaces de travail**, choisissez un ou plusieurs espaces de travail dans la liste déroulante. Ensuite, sous **Jeux de permissions**, choisissez un jeu de permissions. Ces autorisations ne leur seront attribuées que pour les espaces de travail que vous avez sélectionnés.

Lorsque vous avez terminé, sélectionnez **Mettre à jour l'utilisateur.**

Permissions au niveau de l'espace de travail attribuées par le biais d'un jeu de permissions dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exporter les autorisations des utilisateurs

Pour télécharger une liste de vos utilisateurs et de leurs autorisations, allez dans **Paramètres** > **Utilisateurs de l'entreprise**, puis sélectionnez **Exporter les utilisateurs.** Un fichier CSV sera envoyé à votre adresse e-mail dans les plus brefs délais.

La page "Utilisateurs de l'entreprise" dans Braze avec l'option "Exporter les utilisateurs" en point de mire.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Liste des autorisations

{% alert important %}
À partir d'avril 2024, pour créer ou mettre à jour des listes de codes de promotion, les utilisateurs de Braze doivent disposer de l'autorisation "Accéder aux campagnes, toiles, cartes, segments, médiathèque".
{% endalert %}

|Niveau|Nom|Définition|
|---|---|---|
|Administrateur|Administrateur|Permet aux utilisateurs d'accéder à toutes les fonctionnalités disponibles. Il s'agit du paramètre par défaut pour tous les nouveaux utilisateurs. Peut mettre à jour les paramètres de l'entreprise (nom de l'entreprise et fuseau horaire), ce que les utilisateurs limités ne peuvent pas faire.|
|Entreprise|Créer et supprimer des espaces de travail|Permet aux utilisateurs de créer et de supprimer des espaces de travail.|
|Entreprise|Gérer les paramètres de l'entreprise|Permet aux utilisateurs de modifier n'importe quel paramètre de l'entreprise.|
|Espace de travail|Accédez aux campagnes, aux toiles, aux cartes, aux blocs de contenu, aux drapeaux de fonctionnalité, aux segments, à la bibliothèque multimédia, aux emplacements, aux codes de promotion et aux centres de préférences.|Permet aux utilisateurs d'afficher les indicateurs de performance des campagnes et des Canvas, de créer et de dupliquer des brouillons de campagnes et de Canvas, de modifier des brouillons et des modèles de campagnes et de Canvas, d'afficher des brouillons de segments, des modèles et des médias, de créer des modèles, de télécharger des médias, de créer ou de mettre à jour des listes de codes de promotion, de créer ou de mettre à jour des listes de codes de promotion, de créer ou de mettre à jour des listes de codes de promotion, de créer ou de mettre à jour des listes de codes de promotion, de créer ou de mettre à jour des listes de codes de promotion, de créer ou de mettre à jour des listes de codes de promotion, de créer ou de mettre à jour des listes de codes de promotion, de créer ou de mettre à jour des listes de codes de promotion, de créer ou de mettre à jour des listes de codes de promotion, de créer ou de mettre à jour des listes de codes de promotion, de créer ou de mettre à jour des listes de codes de promotion, de créer ou de mettre à jour des listes de codes de promotion, de créer ou de mettre à jour des listes de codes de promotion, de créer ou de mettre à jour des listes de codes de promotion, de créer ou de mettre à jour des listes de codes de promotion, de créer ou de mettre à jour des paramètres généraux des messages dans le tableau de bord. Toutefois, les utilisateurs disposant de cette autorisation ne peuvent pas mettre en pause ou modifier une ligne/une production/instantanée existante.|
|Espace de travail|Accéder à la console de développement|Permet un accès complet aux paramètres et journaux suivants :{::nomarkdown}<ul><li><a href='/docs/user_guide/administrative/app_settings/api_settings_tab/'>Clés API</a></li><li><a href='/docs/user_guide/administrative/app_settings/internal_groups_tab/'>Groupes internes</a></li><li><a href='/docs/user_guide/administrative/app_settings/message_activity_log_tab/'>Journal d'activité des messages</a></li><li><a href='/docs/user_guide/administrative/app_settings/event_user_log_tab/'>Journal des événements utilisateurs</a></li></ul>{:/}|
|Espace de travail|Campagnes d'approbation et de refus|Permet aux utilisateurs d'approuver ou de refuser des campagnes. Le [processus d'approbation des campagnes]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) doit être activé pour que cette autorisation s'applique. Cet environnement est actuellement en accès anticipé. Contactez votre gestionnaire de compte si vous souhaitez participer à l'accès anticipé.|
|Espace de travail|Approuver et refuser les toiles|Permet aux utilisateurs d'approuver ou de refuser les canevas. Le [processus d'approbation des toiles]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) doit être activé pour que cette autorisation s'applique.|
|Espace de travail|Modifier les intégrations currents|Permet aux utilisateurs de modifier une connexion Currents, y compris les informations d'identification. Par défaut, les utilisateurs auxquels est attribuée l'autorisation "Intégrations externes" se voient également attribuer cette autorisation.|
|Espace de travail|Modifier les segments|Permet aux utilisateurs de créer et de modifier des segmentations. Vous pouvez toujours créer des campagnes avec des segments et des filtres existants sans cette autorisation. Vous avez besoin de cette autorisation pour générer un segment à partir des utilisateurs d'un CSV ou pour recibler le groupe d'utilisateurs du CSV.|
|Espace de travail|Exporter les données de l'utilisateur|Permet aux utilisateurs d'exporter leurs données utilisateur à partir des segments, des campagnes et des Canevas. Cette autorisation comprend des informations sensibles sur les utilisateurs, telles que les noms, les adresses e-mail et d'autres informations personnelles identifiables (IPI) collectées. |
|Espace de travail|Importation d'utilisateurs et mise à jour des données|Permet aux utilisateurs d'importer des fichiers CSV et des fichiers de mise à jour des utilisateurs de l'application, ainsi que d'afficher la page d'importation des utilisateurs. Cela vous permet également de modifier le statut de l'abonnement d'un utilisateur et les règles d'abonnement/de désabonnement de son groupe d'abonnement.|
|Espace de travail|Lancer et gérer les blocs de contenu|Permet aux utilisateurs de lancer et de gérer des [blocs de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/).|
|Espace de travail|Lancer les centres de préférences|Permet aux utilisateurs de lancer des [centres de préférences]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).|
|Espace de travail|Gestion des applications|Permet aux utilisateurs de modifier les **paramètres de l'application.**|
|Espace de travail|Permission du tableau de bord Gestion des catalogues|Permet aux utilisateurs de créer et de gérer des catalogues.|
|Espace de travail|Gestion des utilisateurs du tableau de bord| Permet aux non-administrateurs d'afficher, de modifier et de gérer la page **Utilisateurs de la société**, et de gérer les utilisateurs du tableau de bord dans leur espace de travail en modifiant les autorisations de n'importe quel utilisateur, y compris les leurs. Les utilisateurs disposant de cette autorisation ne peuvent pas supprimer des utilisateurs (seuls les administrateurs peuvent supprimer des utilisateurs).|
|Espace de travail|Gérer les paramètres de l'e-mail|Permet aux utilisateurs d'enregistrer les modifications apportées à la configuration de l'e-mail**(Paramètres** > **Préférences e-mail**).|
|Espace de travail|Gérer les événements, les attributs et les achats|Permet aux utilisateurs de modifier les attributs personnalisés (les utilisateurs qui n'ont pas cette capacité peuvent toujours afficher les attributs personnalisés), de modifier et d'afficher les propriétés des événements personnalisés, et de modifier et d'afficher les propriétés des produits sous **Paramètres des données.**|
|Espace de travail|Gérer les intégrations externes|Permet d'accéder à tous les onglets sous **Partenaires technologiques**, de synchroniser Braze avec d'autres plateformes et de gérer l'[ingestion de données dans le nuage]({{site.baseurl}}/user_guide/data/cloud_ingestion/).|
|Espace de travail|Gérer les drapeaux de fonctionnalité|Permet aux utilisateurs de créer ou de modifier des [drapeaux de fonctionnalité]({{site.baseurl}}/developer_guide/feature_flags/).|
|Espace de travail|Gestion des ressources de la bibliothèque multimédia|Permet aux utilisateurs d'ajouter, de modifier et de supprimer des ressources de la bibliothèque multimédia.|
|Espace de travail|Gestion des subscription groups|Permet aux utilisateurs de créer et de gérer des groupes d'abonnements.|
|Espace de travail|Gérer les étiquettes|Permet aux utilisateurs de modifier ou de supprimer des étiquettes (sous **Gestion des étiquettes)**. Vous n'avez pas besoin de cette autorisation pour ajouter des tags aux campagnes ou aux segments.|
|Espace de travail|Gestion des Teams|Permet aux utilisateurs de gérer des **Teams internes**. La possibilité de sélectionner cette autorisation dépend de votre contrat avec Braze.|
|Espace de travail|Gérer les transformations|Permet aux utilisateurs de créer et de gérer des transformations de données.|
|Espace de travail|Envoyer des campagnes, des toiles|Permet aux utilisateurs de modifier, d'archiver et d'arrêter des campagnes et des campagnes, de créer des campagnes et de lancer des campagnes. |
|Espace de travail|Voir les détails de la facturation|Permet aux utilisateurs de visualiser les abonnements et la facturation.|
|Espace de travail|Voir l'intégration currents|Permet aux utilisateurs d'afficher toutes les informations relatives à une connexion Currents, à l'exception des informations d'identification. Par défaut, cette autorisation est également attribuée aux utilisateurs bénéficiant de l'autorisation "Accéder aux campagnes, aux toiles, aux cartes, aux blocs de contenu, aux drapeaux de fonctionnalité, aux segments, à la bibliothèque multimédia, aux emplacements, aux codes de promotion et aux centres de préférences".|
|Espace de travail|Afficher les attributs personnalisés marqués comme PII|Permet aux utilisateurs non administrateurs de visualiser les attributs personnalisés qui contiennent des informations sensibles et sont marqués comme des informations personnelles identifiables (PII).|
|Espace de travail|Voir l'IIP|Permet aux utilisateurs d'afficher les champs d'informations personnelles identifiables (IPI) tels que définis par votre entreprise dans le tableau de bord. Les utilisateurs peuvent également visualiser les champs IIP dans l'onglet **Aperçu en tant qu'utilisateur** des aperçus de messages.<br><br>Vous avez besoin de cette autorisation pour utiliser le [générateur de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/), car il permet d'accéder directement à certaines données des clients.|
|Espace de travail|Visualisation des profils utilisateurs conformes à la directive PII|Permet aux utilisateurs de consulter des profils utilisateurs contenant des champs que votre entreprise a définis comme des informations personnelles identifiables (IPI), mais en expurgeant les champs IPI.<br><br>Vous avez besoin de cette autorisation pour utiliser l'outil de recherche d'utilisateurs. |
|Espace de travail|Voir les transformations|Permet aux utilisateurs de visualiser les [transformations de données de Braze]({{site.baseurl}}/user_guide/data/data_transformation/overview/).|
|Espace de travail|Voir les données d'utilisation|Permet aux utilisateurs de consulter l'utilisation de l'app, y compris les tableaux de bord des performances des canaux.|
|Espace de travail|Fusionner les utilisateurs en double|Permet aux utilisateurs de fusionner des profils utilisateurs en double.|
|Espace de travail|Aperçu des utilisateurs en double|Permet aux utilisateurs de voir quels profils utilisateurs sont dupliqués.|
|Espace de travail|Créer et modifier des modèles de canvas|Permet aux utilisateurs de créer et de modifier des modèles de canvas.|
|Espace de travail|Voir les modèles de canvas|Permet aux utilisateurs de visualiser les modèles de Canvas.|
|Espace de travail|Modèles de canevas d'archives|Permet aux utilisateurs d'archiver les modèles de canvas.|
|Espace de travail|Gérer la segmentation des propriétés d'événements personnalisés|Permet aux utilisateurs de créer des segments en fonction de la récence et de la fréquence des propriétés d'événement.|
|Espace de travail|Publier des pages d'atterrissage|Permet aux utilisateurs de publier des [pages d'atterrissage]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/).|
|Espace de travail|Créez des ébauches de page d'atterrissage|Permet aux utilisateurs de créer et d'enregistrer des brouillons de pages d'atterrissage.|
|Espace de travail|Accéder aux pages d'atterrissage|Permet aux utilisateurs d'accéder à la page **Pages d'atterrissage**.|
|Espace de travail|Créer et modifier des modèles de page d'atterrissage|Permet aux utilisateurs de créer et de modifier des modèles de page d'atterrissage.|
|Espace de travail|Voir les modèles de page d'atterrissage|Permet aux utilisateurs de visualiser les modèles de pages d'atterrissage.|
|Espace de travail|Modèles de page d'atterrissage pour les archives|Permet aux utilisateurs d'archiver des modèles de pages d'atterrissage.|
|Espace de travail|Voir les agents d'intelligence artificielle personnalisés|Permet aux utilisateurs de visualiser les [agents d'intelligence artificielle personnalisés]({{site.baseurl}}/user_guide/brazeai/agents/). Cette fonctionnalité est actuellement en version bêta.|
|Espace de travail|Créer des agents d'intelligence artificielle personnalisés|Permet aux utilisateurs de créer des agents d'intelligence artificielle personnalisés. Cette fonctionnalité est actuellement en version bêta.|
|Espace de travail|Modifier les agents d'intelligence artificielle personnalisés|Permet aux utilisateurs de modifier les agents d'intelligence artificielle personnalisés. Cette fonctionnalité est actuellement en version bêta.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
