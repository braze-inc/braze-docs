{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

## Création d'un ensemble d'autorisations

Utilisez les ensembles d'autorisations pour regrouper les autorisations liées à des domaines ou actions spécifiques. Vous pouvez appliquer ces ensembles aux utilisateurs du tableau de bord qui ont besoin du même accès dans différents espaces de travail. Pour créer un ensemble d'autorisations, accédez à **Paramètres** > **Paramètres des autorisations**, puis sélectionnez **Créer un ensemble d'autorisations**. Pour obtenir une description de chaque autorisation, consultez la [Liste des autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Nom|Autorisations|
|-----------|----------------|
|Développeurs|« Afficher les clés API », « Modifier les clés API », « Afficher les groupes internes », « Modifier les groupes internes », « Afficher le journal d'activité des messages », « Afficher le journal des événements utilisateurs », « Afficher les identifiants API », « Afficher le tableau de bord d'utilisation de l'API », « Afficher les limites de l'API », « Afficher les alertes d'utilisation de l'API », « Modifier les alertes d'utilisation de l'API », « Afficher le débogueur SDK », « Modifier le débogueur SDK ».|
|Marketeurs|« Afficher les campagnes », « Modifier les campagnes », « Archiver les campagnes », « Afficher les Canvas », « Modifier les Canvas », « Archiver les Canvas », « Afficher les règles de limite de fréquence », « Modifier les règles de limite de fréquence », « Afficher la hiérarchisation des messages », « Modifier la priorisation des messages », « Afficher les blocs de contenu », « Afficher les indicateurs de fonctionnalité », « Modifier les indicateurs de fonctionnalité », « Archiver les indicateurs de fonctionnalité », « Afficher les segments », « Modifier les segments », « Modifier le groupe de contrôle global », « Afficher les modèles IAM », « Modifier les modèles IAM », « Archiver les modèles IAM », « Afficher les modèles d'e-mail », « Modifier les modèles d'e-mail », « Archiver les modèles d'e-mail », « Afficher les modèles de webhook », « Modifier les modèles de webhook », « Archiver les modèles de webhook », « Afficher les modèles de liens », « Modifier les modèles de liens », « Afficher les ressources de la bibliothèque multimédia », « Afficher les emplacements », « Modifier les emplacements », « Archiver les emplacements », « Afficher les codes de promotion », « Modifier les codes de promotion », « Exporter les codes de promotion », « Afficher les centres de préférences », « Modifier les centres de préférences », « Modifier les rapports », « Afficher les modèles de bannières », « Afficher les paramètres multilingues », « Utiliser l'opérateur », « Afficher les agents Decisioning Studio », « Afficher l'événement de conversion Decisioning Studio ».|
|Gestion des utilisateurs|« Modifier les utilisateurs du tableau de bord », « Afficher les équipes », « Modifier les équipes », « Archiver les équipes ».|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Création d'un rôle

Les rôles offrent une meilleure structuration en regroupant vos autorisations personnalisées avec les contrôles d'accès aux espaces de travail. C'est particulièrement utile lorsque vous gérez plusieurs marques ou espaces de travail régionaux dans un même tableau de bord. Grâce aux rôles, vous pouvez ajouter les utilisateurs du tableau de bord aux bons espaces de travail et leur accorder directement les autorisations associées. Pour obtenir une description de chaque autorisation, consultez la [Liste des autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nom du rôle    | Espace de travail | Autorisations  
----------- | ----------- | ---------
| Marketeur - Marques de mode | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | « Afficher les campagnes », « Modifier les campagnes », « Archiver les campagnes », « Afficher les Canvas », « Modifier les Canvas », « Archiver les Canvas », « Afficher les blocs de contenu », « Modifier les blocs de contenu », « Archiver les blocs de contenu », « Lancer les blocs de contenu », « Afficher les indicateurs de fonctionnalité », « Modifier les indicateurs de fonctionnalité », « Archiver les indicateurs de fonctionnalité », « Afficher les segments », « Modifier les segments », « Afficher les modèles de bannières », « Modifier les modèles de bannières », « Afficher les modèles d'e-mail », « Modifier les modèles d'e-mail », « Afficher les ressources de la bibliothèque multimédia », « Modifier les ressources de la bibliothèque multimédia », « Supprimer les ressources de la bibliothèque multimédia », « Afficher les emplacements », « Modifier les emplacements », « Archiver les emplacements », « Afficher les codes de promotion », « Modifier les codes de promotion », « Exporter les codes de promotion », « Afficher les centres de préférences », « Modifier les centres de préférences ». |
| Marketeur - Marques de soins de la peau | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} |« Afficher les campagnes », « Modifier les campagnes », « Archiver les campagnes », « Afficher les Canvas », « Modifier les Canvas », « Archiver les Canvas », « Afficher les blocs de contenu », « Modifier les blocs de contenu », « Archiver les blocs de contenu », « Lancer les blocs de contenu », « Afficher les indicateurs de fonctionnalité », « Modifier les indicateurs de fonctionnalité », « Archiver les indicateurs de fonctionnalité », « Afficher les segments », « Modifier les segments », « Afficher les modèles de bannières », « Modifier les modèles de bannières », « Afficher les modèles d'e-mail », « Modifier les modèles d'e-mail », « Afficher les ressources de la bibliothèque multimédia », « Modifier les ressources de la bibliothèque multimédia », « Supprimer les ressources de la bibliothèque multimédia », « Afficher les emplacements », « Modifier les emplacements », « Archiver les emplacements », « Afficher les codes de promotion », « Modifier les codes de promotion », « Exporter les codes de promotion », « Afficher les centres de préférences », « Modifier les centres de préférences ».|
| Gestion des utilisateurs - Toutes les marques | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | « Modifier les utilisateurs du tableau de bord », « Afficher les équipes », « Modifier les équipes », « Archiver les équipes »|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## Quelle est la différence entre les ensembles d'autorisations, les rôles et les Teams ?

{% multi_lang_include permissions.md content="Differences" %}

### Points à considérer lors de l'ajout d'autorisations utilisateur aux Teams

Vous pourriez rencontrer des difficultés en essayant d'enregistrer les autorisations dans le tableau de bord de Braze, notamment lorsque vous ajoutez ou supprimez des utilisateurs d'un espace de travail, ou lorsque vous les ajoutez à une équipe. Le bouton **Enregistrer/Mettre à jour les utilisateurs** peut apparaître grisé si les autorisations de l'utilisateur sont identiques à celles dont il dispose déjà au niveau de l'espace de travail. Cette restriction existe car il n'y a aucun intérêt à utiliser des Teams si tous les utilisateurs possèdent les mêmes autorisations que l'ensemble de l'espace de travail.

Pour ajouter un utilisateur à une Team tout en conservant les mêmes autorisations, n'attribuez aucune autorisation au niveau de l'espace de travail. Attribuez-les exclusivement au niveau de l'équipe.

## Utilisateurs limités

Les utilisateurs limités disposent d'autorisations spécifiques qui leur permettent de gérer certains aspects du tableau de bord de Braze, tout en étant soumis à des restrictions par rapport aux administrateurs d'entreprise et aux administrateurs d'espace de travail.

| Portée | Description |
| --- | --- |
| Autorisations | Les utilisateurs limités peuvent modifier les autorisations d'autres utilisateurs limités s'ils disposent de l'autorisation « Modifier les utilisateurs du tableau de bord ». Ils peuvent également créer de nouveaux utilisateurs limités et modifier leurs ensembles d'autorisations. En revanche, ils ne peuvent pas créer ni gérer de comptes administrateur d'entreprise. |
| Limitations de rôle | Si un utilisateur limité dispose de toutes les autorisations sauf « Administrateur de l'espace de travail », il conserve l'accès à toutes les autres autorisations généralement accordées à un administrateur d'espace de travail. |
| Visibilité des autorisations | Si un utilisateur limité dispose de l'autorisation « Modifier les utilisateurs du tableau de bord » pour un espace de travail (par exemple Dev) mais pas pour un autre (par exemple Prod), il ne verra pas les autorisations de l'espace de travail Prod dans la page de détails des utilisateurs de son tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparaison des types d'utilisateurs limités

| Type d'utilisateur limité | Description |
| --- | --- |
| Administrateur de l'espace de travail | Les administrateurs d'espace de travail disposent d'autorisations spécifiques à la gestion des espaces de travail, mais n'ont pas les mêmes prérogatives que les administrateurs d'entreprise. Les utilisateurs limités peuvent hériter d'autorisations similaires à celles des administrateurs d'espace de travail s'ils disposent des autorisations nécessaires. |
| Administrateur (administrateur d'entreprise) | Les administrateurs d'entreprise disposent d'autorisations plus étendues, notamment la possibilité de supprimer des utilisateurs du tableau de bord. Cependant, ils ne peuvent pas supprimer leur propre compte et doivent contacter un autre administrateur d'entreprise pour cette action. |
| Accès en lecture seule | Pour accéder à certaines parties du tableau de bord, comme la page Campagnes, les utilisateurs doivent disposer des autorisations de consultation correspondantes.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erreur d'accès restreint

Les utilisateurs peuvent rencontrer des messages tels que « Vous devez disposer de l'autorisation "Afficher les pages d'accueil" pour accéder à cette page ». Dans ce cas, l'utilisateur et l'administrateur du compte doivent vérifier que les autorisations requises sont bien accordées. Si c'est le cas, essayez de résoudre le problème en désactivant puis en réactivant les autorisations de l'utilisateur. 

{% alert note %}
Il n'est pas possible de fusionner ou d'importer les autorisations d'un utilisateur du tableau de bord vers un autre.
{% endalert %}

## Modifier les autorisations d'un utilisateur

Pour modifier les autorisations actuelles d'un utilisateur (administrateur, entreprise ou espace de travail), accédez à **Paramètres** > **Utilisateurs de l'entreprise**, puis sélectionnez son nom.

![La page « Utilisateurs de l'entreprise » dans Braze affichant un tableau des utilisateurs du tableau de bord.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Admin

Les administrateurs ont accès à toutes les fonctionnalités et peuvent modifier tous les paramètres de l'entreprise. Ils peuvent :

- Modifier les [paramètres d'approbation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Ajouter, modifier, supprimer, suspendre ou réactiver d'autres [utilisateurs de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users)
- Exporter les utilisateurs de Braze au format CSV

Pour accorder ou retirer les privilèges d'administrateur, sélectionnez **Cet utilisateur est un administrateur**, puis sélectionnez **Mettre à jour l'utilisateur**.

![Les détails de l'utilisateur sélectionné avec la case à cocher admin mise en évidence.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Si vous retirez les privilèges d'administrateur à un utilisateur, celui-ci ne pourra plus accéder à Braze tant que vous ne lui aurez pas attribué au moins une [autorisation au niveau de l'entreprise ou de l'espace de travail]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Company %}

### Entreprise

Pour gérer les autorisations suivantes au niveau de l'entreprise pour un utilisateur, cochez ou décochez la case correspondante. Lorsque vous avez terminé, sélectionnez **Mettre à jour l'utilisateur**.

|Nom de l'autorisation|Description|
|----------|-----------|
|Gérer les paramètres de l'entreprise|Permet aux utilisateurs de modifier les paramètres d'autorisation et la vérification de l'expéditeur.|
|Créer et supprimer des espaces de travail|Permet aux utilisateurs de créer et de supprimer des espaces de travail.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Espace de travail

Vous pouvez attribuer à un utilisateur des autorisations différentes pour chaque espace de travail auquel il appartient dans Braze. Pour gérer les autorisations au niveau de l'espace de travail, sélectionnez **Sélectionner les espaces de travail et les autorisations**, puis choisissez les autorisations manuellement ou attribuez un [ensemble d'autorisations ou un rôle]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) que vous avez précédemment créé. Si vous devez attribuer des autorisations différentes pour différents espaces de travail, répétez ce processus autant de fois que nécessaire. Pour obtenir une description de chaque autorisation, consultez la [Liste des autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Sous **Espaces de travail**, choisissez un ou plusieurs espaces de travail dans la liste déroulante. Ensuite, sous **Autorisations**, sélectionnez une ou plusieurs autorisations. Elles ne seront attribuées que pour les espaces de travail sélectionnés. Vous pouvez également sélectionner **Attribuer l'accès administrateur à l'espace de travail** si vous souhaitez accorder toutes les autorisations pour cet espace de travail.

Lorsque vous avez terminé, sélectionnez **Mettre à jour l'utilisateur**.

![Autorisations au niveau de l'espace de travail sélectionnées manuellement dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Sous **Espaces de travail**, choisissez un ou plusieurs espaces de travail dans la liste déroulante. Ensuite, sous **Ensembles d'autorisations**, choisissez un ensemble d'autorisations. Ces autorisations ne seront attribuées que pour les espaces de travail sélectionnés.

Lorsque vous avez terminé, sélectionnez **Mettre à jour l'utilisateur**.

![Autorisations au niveau de l'espace de travail attribuées via un ensemble d'autorisations dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Assign role %}

Sous **Espaces de travail**, choisissez un ou plusieurs espaces de travail dans la liste déroulante. Ensuite, sous **Rôle**, sélectionnez un rôle. Ces autorisations ne seront attribuées que pour les espaces de travail sélectionnés.

Lorsque vous avez terminé, sélectionnez **Mettre à jour l'utilisateur**.

![Autorisations au niveau de l'espace de travail attribuées via un rôle dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exporter les autorisations des utilisateurs

Pour télécharger la liste de vos utilisateurs et de leurs autorisations, accédez à **Paramètres** > **Utilisateurs de l'entreprise**, puis sélectionnez **Exporter les utilisateurs**. Un fichier CSV sera envoyé à votre adresse e-mail sous peu.

![La page « Utilisateurs de l'entreprise » dans Braze avec l'option « Exporter les utilisateurs » mise en évidence.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Liste des autorisations

| Autorisation | Définition |
|-------------------------------------------------|---------------------|
| Afficher les détails de facturation                            | Consulter les détails de facturation |
| Afficher les attributs personnalisés marqués comme PII            | Afficher les attributs personnalisés marqués comme données personnelles identifiables (PII) |
| Afficher les PII                                        | Afficher les données personnelles identifiables |
| Voir les profils utilisateur conformes PII                | Accéder à la recherche d'utilisateurs et consulter les profils utilisateurs avec les PII expurgées |
| Afficher les données d'utilisation                                 | Consulter les données d'utilisation |
| Fusionner les utilisateurs en double                           | Fusionner les utilisateurs en double en un seul utilisateur. Les doublons sont supprimés après la fusion. |
| Prévisualiser les utilisateurs en double                         | Examiner quels profils utilisateurs sont des doublons |
| Afficher les modèles Canvas                           | Afficher les modèles Canvas |
| Archiver les modèles Canvas                        | Déplacer les modèles Canvas vers les archives |
| Lancer des blocs de contenu                           | Lancer des blocs de contenu |
| Lancer les centres de préférences                       | Lancer les centres de préférences |
| Modifier les intégrations Currents                      | Créer, mettre à jour et supprimer des intégrations Currents |
| Afficher les intégrations Currents                       | Consulter les intégrations Currents |
| Afficher les campagnes                                  | Afficher les campagnes |
| Modifier les campagnes                                  | Créer et mettre à jour des campagnes |
| Archiver les campagnes                               | Déplacer les campagnes vers les archives |
| Lancer les campagnes                                | Lancer, arrêter, suspendre ou reprendre des campagnes existantes |
| Afficher les règles de limite de fréquence                    | Afficher les règles de limite de fréquence |
| Modifier les règles de limite de fréquence                    | Créer et mettre à jour les règles de limite de fréquence |
| Afficher les Canvas                                   | Afficher les Canvas |
| Modifier les Canvas                                   | Créer et mettre à jour des Canvas |
| Archiver les Canvas                                | Déplacer les Canvas vers les archives |
| Lancer les Canvas                                 | Lancer, arrêter, suspendre ou reprendre des Canvas existants |
| Afficher les blocs de contenu                             | Afficher les blocs de contenu |
| Modifier les blocs de contenu                             | Créer et mettre à jour des blocs de contenu |
| Archiver les blocs de contenu                          | Déplacer les blocs de contenu vers les archives |
| Afficher les indicateurs de fonctionnalité                              | Afficher les indicateurs de fonctionnalité |
| Modifier les indicateurs de fonctionnalité                              | Créer et mettre à jour des indicateurs de fonctionnalité |
| Archiver les indicateurs de fonctionnalité                           | Déplacer les indicateurs de fonctionnalité vers les archives |
| Consulter les modèles de messages WhatsApp                 | Permet aux utilisateurs de visualiser les [modèles de messages WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/?tab=template%20messages#step-2-compose-your-whatsapp-message). |
| Modifier les modèles de messages WhatsApp | Permet aux utilisateurs de créer des modèles de messages WhatsApp dans le générateur de modèles. Cette fonctionnalité est actuellement disponible en accès anticipé. |
| Afficher les segments                                   | Afficher les segments. Les utilisateurs doivent disposer de l'autorisation « Afficher les segments » pour pouvoir bénéficier des autorisations « Modifier les segments » ou « Archiver les segments ». |
| Archiver les segments                                | Archiver et désarchiver des segments. Les utilisateurs disposant de l'autorisation « Archiver les segments » doivent également se voir accorder l'autorisation « Afficher les segments ». |
| Modifier les segments                                   | Créer et mettre à jour des segments. Les utilisateurs disposant de l'autorisation « Modifier les segments » doivent également se voir accorder l'autorisation « Afficher les segments ». |
| Afficher le groupe de contrôle global                       | Consulter la page de configuration du groupe de contrôle global |
| Modifier le groupe de contrôle global                       | Créer et enregistrer les modifications apportées au groupe de contrôle global. Les utilisateurs disposant de l'autorisation « Modifier le groupe de contrôle global » doivent également disposer des autorisations « Modifier les campagnes » et « Modifier les Canvas ». Les utilisateurs disposant de l'autorisation « Modifier le groupe de contrôle global » se voient également accorder l'autorisation « Afficher le groupe de contrôle global ». |
| Afficher les modèles de bannières                           | Consulter les modèles de bannières |
| Modifier les modèles de bannières                           | Créer et mettre à jour des modèles de bannières |
| Archiver les modèles de bannières                   	  | Déplacer les modèles de bannières vers les archives |
| Afficher les modèles d'e-mail                            | Consulter les modèles d'e-mail |
| Modifier les modèles d'e-mail                            | Créer et mettre à jour des modèles d'e-mail |
| Archiver les modèles d'e-mail                         | Déplacer les modèles d'e-mail vers les archives |
| Afficher les modèles de liens   	                  | Consulter les modèles de liens sans apporter de modifications |
| Modifier les modèles de liens	                      | Créer et mettre à jour des modèles de liens |
| Publier les pages d'accueil                           | Rendre active une page d'accueil en brouillon |
| Modifier les brouillons de pages d'accueil                        | Créer et enregistrer des brouillons de pages d'accueil |
| Afficher les pages d'accueil			                  | Afficher les pages d'accueil |
| Modifier les modèles de pages d'accueil	                  | Créer et mettre à jour des modèles de pages d'accueil |
| Afficher les modèles de pages d'accueil	                  | Consulter les modèles de pages d'accueil |
| Archiver les modèles de pages d'accueil 	              | Déplacer les modèles de pages d'accueil vers les archives |
| Afficher les ressources de la bibliothèque multimédia                       | Consulter les ressources de la bibliothèque multimédia |
| Modifier les ressources de la bibliothèque multimédia                       | Créer et mettre à jour les ressources de la bibliothèque multimédia |
| Supprimer les ressources de la bibliothèque multimédia                     | Supprimer définitivement les ressources de la bibliothèque multimédia |
| Afficher les emplacements                                  | Afficher les emplacements |
| Modifier les emplacements                                  | Créer et modifier des emplacements |
| Archiver les emplacements                               | Déplacer les emplacements vers les archives |
| Afficher les codes de promotion                            | Consulter les codes de promotion |
| Modifier les codes de promotion                            | Créer et mettre à jour des codes de promotion |
| Exporter les codes de promotion                          | Télécharger la liste des codes de promotion depuis le tableau de bord |
| Afficher les centres de préférences                         | Consulter les centres de préférences  |
| Modifier les centres de préférences                         | Créer et mettre à jour les centres de préférences |
| Lancer les centres de préférences	                      | Activer un brouillon de centre de préférences ou mettre à jour un centre existant |
| Afficher les clés API                                   | Afficher les clés API |
| Modifier les clés API                                   | Créer et mettre à jour des clés API |
| Afficher les groupes internes                            | Afficher les groupes internes |
| Modifier les groupes internes                            | Créer et mettre à jour des groupes internes |
| Supprimer les groupes internes                          | Supprimer des groupes internes |
| Afficher le journal d'activité des messages                       | Consulter les journaux d'activité des messages |
| Afficher le journal des événements utilisateurs                             | Consulter les journaux des événements utilisateurs |
| Afficher les identifiants API                            | Afficher les identifiants API et autres identifiants |
| Afficher le tableau de bord d'utilisation de l'API                        | Consulter le tableau de bord d'utilisation de l'API |
| Afficher les limites de l'API                                 | Consulter les limites de débit de l'API |
| Afficher les alertes d'utilisation de l'API                           | Consulter les alertes d'utilisation de l'API |
| Modifier les alertes d'utilisation de l'API                           | Créer et mettre à jour des alertes d'utilisation de l'API |
| Modifier le débogueur SDK                               | Créer et télécharger des sessions du débogueur SDK |
| Afficher le débogueur SDK                               | Consulter le débogueur SDK ou les sessions de débogage |
| Afficher les paramètres de l'application                               | Consulter la page Paramètres de l'application |
| Modifier les paramètres de l'application                               | Créer, modifier et mettre à jour des applications dans les paramètres de l'application |
| Afficher les catalogues                                   | Consulter les catalogues et les sélections |
| Modifier les catalogues                                   | Créer et mettre à jour des catalogues et des sélections |
| Exporter les catalogues                                 | Télécharger les catalogues depuis le tableau de bord |
| Supprimer les catalogues                                 | Supprimer définitivement les catalogues |
| Modifier les utilisateurs du tableau de bord                            | Afficher, créer et modifier les utilisateurs de l'entreprise |
| Afficher les paramètres d'e-mail                             | Consulter les préférences d'e-mail |
| Modifier les paramètres d'e-mail                             | Activer et mettre à jour les préférences d'e-mail | 
| Modifier le chiffrement au niveau du champ de l'identifiant            | Activer et mettre à jour les paramètres de chiffrement au niveau du champ |
| Afficher les attributs personnalisés                          | Consulter les attributs personnalisés et le rapport d'utilisation |
| Modifier les attributs personnalisés                          | Créer et mettre à jour des attributs personnalisés |
| Ajouter des attributs personnalisés à la liste de blocage                     | Ajouter des attributs personnalisés à une liste de blocage qui en restreint l'utilisation dans le tableau de bord |
| Supprimer des attributs personnalisés                        | Supprimer définitivement les attributs personnalisés |
| Exporter des attributs personnalisés                        | Télécharger les attributs personnalisés depuis le tableau de bord |
| Afficher les événements personnalisés                              | Consulter les événements personnalisés et le rapport d'utilisation, et ajouter des événements personnalisés au rapport analytique quotidien envoyé par e-mail |
| Modifier les événements personnalisés                              | Créer et mettre à jour des événements personnalisés |
| Ajouter des événements personnalisés à la liste de blocage                         | Ajouter des événements personnalisés à une liste de blocage qui en restreint l'utilisation dans le tableau de bord |
| Supprimer des événements personnalisés                            | Supprimer définitivement les événements personnalisés |
| Exporter des événements personnalisés                            | Télécharger les événements personnalisés depuis le tableau de bord |
| Modifier la segmentation des propriétés d'événements personnalisés         | Activer et désactiver la segmentation pour les propriétés d'événements personnalisés |
| Afficher les produits                                   | Consulter les produits |
| Modifier les produits                                   | Créer et mettre à jour des produits |
| Ajouter des produits à la liste de blocage                              | Ajouter des produits à une liste de blocage qui en restreint l'utilisation dans le tableau de bord |
| Modifier la segmentation des propriétés d'achat             | Activer et désactiver la segmentation pour les propriétés d'achat |
| Modifier les partenaires technologiques                        | Créer et mettre à jour les partenaires technologiques |
| Modifier l'ingestion de données cloud                       | Créer, mettre à jour et supprimer des sources et des synchronisations |
| Afficher les paramètres multilingues                      | Afficher la page des paramètres multilingues |
| Modifier les paramètres multilingues                      | Créer des paramètres régionaux multilingues |
| Supprimer les paramètres multilingues                    | Supprimer des paramètres régionaux multilingues |
| Modifier les abonnements                              | Créer et mettre à jour des groupes d'abonnement |
| Afficher les étiquettes                                       | Afficher les étiquettes |
| Modifier les étiquettes                                       | Créer et mettre à jour des étiquettes |
| Supprimer les étiquettes                                     | Supprimer définitivement les étiquettes |
| Afficher les équipes                                      | Afficher les équipes |
| Modifier les équipes                                      | Créer et mettre à jour des équipes |
| Archiver les équipes                                   | Déplacer les équipes vers les archives |
| Afficher les transformations de données                        | Afficher les transformations de données |
| Modifier les transformations de données                        | Créer et mettre à jour des transformations de données |
| Modifier les modèles Canvas                           | Créer et mettre à jour des modèles Canvas |
| Approuver les campagnes                               | Approuver ou refuser les campagnes. Le [processus d'approbation des campagnes]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) doit être activé pour que cette autorisation s'applique. Ce paramètre est actuellement disponible en accès anticipé. Contactez votre Account Manager si vous souhaitez participer à l'accès anticipé. |
| Approuver les Canvas                                | Approuver ou refuser les Canvas. Le [processus d'approbation des Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) doit être activé pour que cette autorisation s'applique. Ce paramètre est actuellement disponible en accès anticipé. Contactez votre Account Manager si vous souhaitez participer à l'accès anticipé. |
| Afficher les placements                                 | Afficher les emplacements de bannières |
| Modifier les placements                                 | Afficher les emplacements de bannières sans apporter de modifications |
| Archiver les placements                              | Déplacer les emplacements de bannières vers les archives |
| Afficher les paramètres Push                              | Afficher les paramètres Push |
| Modifier les paramètres Push                              | Créer et mettre à jour les paramètres Push |
| Modifier les rapports du tableau de bord                          | Créer et mettre à jour des rapports |
| Afficher les importations d'utilisateurs                               | Afficher les importations d'utilisateurs CSV sans apporter de modifications |
| Importer des utilisateurs                                    | Importer des utilisateurs dans le tableau de bord |
| Exporter les données utilisateur                                | Télécharger les utilisateurs depuis le tableau de bord |
| Modifier les données utilisateur                                  | Créer et mettre à jour les données utilisateur |
| Afficher la fusion des utilisateurs                                | Consulter la liste des enregistrements de fusion d'utilisateurs |
| Afficher les enregistrements de suppression d'utilisateurs	            	  | Afficher les enregistrements de suppression d'utilisateurs |
| Supprimer des utilisateurs du tableau de bord	                  | Supprimer définitivement des utilisateurs du tableau de bord, individuellement ou en masse. |      
| Afficher les agents d'intelligence artificielle personnalisés                           | Permet aux utilisateurs de visualiser les agents d'intelligence artificielle personnalisés. |
| Modifier les agents d'intelligence artificielle personnalisés                           | Permet aux utilisateurs de créer et de mettre à jour des agents d'intelligence artificielle personnalisés. |
| Archiver les agents d'intelligence artificielle personnalisés                        | Permet aux utilisateurs d'archiver des agents d'intelligence artificielle personnalisés. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }