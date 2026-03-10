{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

## Création d'un ensemble de permissions

Utilisez les ensembles d’autorisations pour regrouper les autorisations liées à des domaines ou actions spécifiques. Vous pouvez appliquer des ensembles d'autorisations aux utilisateurs du tableau de bord qui ont besoin du même accès dans différents espaces de travail. Pour créer un jeu de permissions, accédez à **Paramètres** > **Paramètres de permissions**, puis sélectionnez **Créer un jeu de permissions**. Pour obtenir une description de chaque autorisation, voir [Liste des autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Nom|Permissions|
\|-----------|----------------|
|Développeurs|« Afficher les clés API », « Modifier les clés API », « Afficher les groupes internes », « Modifier les groupes internes », « Afficher le journal des activités des messages », « Afficher le journal des événements utilisateurs », « Afficher les identifiants API », « Afficher le tableau de bord d'utilisation de l'API », « Afficher les limites de l'API », « Afficher les alertes d'utilisation de l'API », « Modifier les alertes d'utilisation de l'API », « Afficher le débogueur SDK », « Modifier le débogueur SDK ».
|Marketeurs|« Afficher les campagnes », « Modifier les campagnes », « Archiver les campagnes », « Afficher les canevas », « Modifier les canevas », « Archiver les canevas », « Afficher les règles de limite de fréquence », « Modifier les règles de limite de fréquence », « Afficher la hiérarchisation des messages », « Modifier la priorisation des messages », « Afficher les blocs de contenu », « Afficher les indicateurs de fonctionnalité », « Modifier les indicateurs de fonctionnalité », « Archiver les indicateurs de fonctionnalité », « Afficher les segments », « Modifier les segments », « Modifier le groupe de contrôle global », « Afficher les modèles IAM », « Modifier les modèles IAM », « Archiver les modèles IAM », « Afficher les modèles d'e-mail », Modifier les modèles d'e-mails, Archiver les modèles d'e-mails, Afficher les modèles de webhooks, Modifier les modèles de webhooks, Archiver les modèles de webhooks, Afficher les modèles de liens, Modifier les modèles de liens, Afficher les ressources de la bibliothèque multimédia, Afficher les localisations, Modifier les localisations, « Archiver les localisations », « Afficher les codes de promotion », « Modifier les codes de promotion », « Exporter les codes de promotion », « Afficher les centres de préférences », « Modifier les centres de préférences », « Modifier les rapports », « Afficher les modèles de bannières », « Afficher les paramètres multilingues », « Utiliser l'opérateur », « Afficher les agents Decisioning Studio », « Afficher l'événement de conversion Decisioning Studio ».|
Gestion des utilisateurs | « Afficher les utilisateurs du tableau de bord », « Modifier les utilisateurs du tableau de bord », « Afficher les Teams », « Modifier les Teams », « Archiver les Teams ».
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Création d'un rôle

Les rôles permettent une meilleure structuration en regroupant vos autorisations personnalisées individuelles avec les contrôles d'accès à l'espace de travail. Ceci est particulièrement utile si vous avez plusieurs marques ou espaces de travail régionaux dans un seul tableau de bord. Grâce aux rôles, vous pouvez ajouter les utilisateurs du tableau de bord aux bons espaces de travail et leur accorder directement les autorisations associées. Pour obtenir une description de chaque autorisation, voir [Liste des autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nom du rôle | Espace de travail | Permissions  
----------- | ----------- | ---------
| Marketeur - Marques de mode | {::nomarkdown}[DEV] Marque de mode, [QA] Marque de mode, [PROD] Marque de mode{:/}| « Afficher les campagnes », « Modifier les campagnes », « Archiver les campagnes », « Afficher les canevas », « Modifier les canevas », « Archiver les canevas », « Afficher les blocs de contenu », « Modifier les blocs de contenu », « Archiver les blocs de contenu », « Lancer les blocs de contenu », « Afficher les indicateurs de fonctionnalité », « Modifier les indicateurs de fonctionnalité », « Archiver les indicateurs de fonctionnalité », « Afficher les segments », « Modifier les segments », « Afficher les modèles de bannière », « Modifier les modèles de bannière », « Afficher les modèles d'e-mail », Modifier les modèles d'e-mails, Afficher les ressources de la bibliothèque multimédia, Modifier les ressources de la bibliothèque multimédia, Supprimer les ressources de la bibliothèque multimédia, Afficher les localisations, Modifier les localisations, Archiver les localisations, Afficher les codes de promotion, Modifier les codes de promotion, Exporter les codes de promotion, Afficher les centres de préférences, Modifier les centres de préférences. |
| Marketeur - Marques de soins de la peau | {::nomarkdown}[DEV] Marque de soins de la peau, [QA] Marque de soins de la peau, [PROD] Marque de soins de{:/} la peau | « Afficher les campagnes », « Modifier les campagnes », « Archiver les campagnes », « Afficher les canevas », « Modifier les canevas », « Archiver les canevas », « Afficher les blocs de contenu », « Modifier les blocs de contenu », « Archiver les blocs de contenu », « Lancer les blocs de contenu », « Afficher les indicateurs de fonctionnalité », « Modifier les indicateurs de fonctionnalité », « Archiver les indicateurs de fonctionnalité », « Afficher les segments », « Modifier les segments », « Afficher les modèles de bannière », « Modifier les modèles de bannière », « Afficher les modèles d'e-mail », Modifier les modèles d'e-mails, Afficher les ressources de la bibliothèque multimédia, Modifier les ressources de la bibliothèque multimédia, Supprimer les ressources de la bibliothèque multimédia, Afficher les emplacements/localisations, Modifier les emplacements/localisations, Archiver les emplacements/localisations, Afficher les codes de promotion, Modifier les codes de promotion, Exporter les codes de promotion, Afficher les centres de préférences, Modifier les centres de préférences.
Gestion des utilisateurs - Toutes les marques | {::nomarkdown}[DEV] Marque de mode, [QA] Marque de mode, [PROD] Marque de mode, [DEV] Marque de soins de la peau, [QA] Marque de soins de la peau, [PROD] Marque de soins de{:/} la peau | « Afficher les utilisateurs du tableau de bord », « Modifier les utilisateurs du tableau de bord », « Afficher les Teams », « Modifier les Teams », « Archiver les Teams » |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## En quoi les jeux de permissions et les rôles diffèrent-ils de Teams ?

{% multi_lang_include permissions.md content="Differences" %}

### Considérations relatives à l'ajout d'autorisations utilisateur à Teams

Vous pourriez rencontrer des difficultés lorsque vous essayez d'enregistrer les autorisations dans le tableau de bord de Braze, en particulier lorsque vous ajoutez ou supprimez des utilisateurs d'un espace de travail, ou lorsque vous les ajoutez à une équipe. Le bouton **Enregistrer/Mettre à jour les utilisateurs** peut être grisé si les autorisations de l'utilisateur sont identiques à celles dont il dispose déjà au niveau de l'espace de travail. Cette restriction existe car il n'y a aucun avantage à disposer de Teams si tous les utilisateurs possèdent les mêmes autorisations que l'ensemble de l'espace de travail.

Pour ajouter un utilisateur à une Team tout en conservant les mêmes autorisations, veuillez ne pas attribuer d'autorisations au niveau de l'espace de travail. Veuillez attribuer les autorisations exclusivement au niveau des équipes.

## Utilisateurs limités

Les utilisateurs limités disposent d'autorisations spécifiques qui leur permettent de gérer certains aspects du tableau de bord de Braze, tout en étant soumis à des restrictions par rapport aux administrateurs d'entreprise et aux administrateurs d'espace de travail.

| Champ d'application | Description |
| --- | --- |
| Autorisations | Les utilisateurs limités peuvent modifier les autorisations d'autres utilisateurs limités s'ils disposent des autorisations « Afficher les utilisateurs du tableau de bord » et « Modifier les utilisateurs du tableau de bord ». Ils peuvent également créer de nouveaux utilisateurs limités et modifier leurs ensembles d'autorisations. Cependant, ils ne peuvent pas créer ni gérer de comptes administrateur d'entreprise. |
| Limitations de rôle | Si un utilisateur limité dispose de toutes les autorisations à l'exception de « Administrateur de l'espace de travail », il aura toujours accès à toutes les autres autorisations généralement accordées à un administrateur d'espace de travail. |
| Visibilité des autorisations | Si un utilisateur limité dispose des autorisations « Afficher les utilisateurs du tableau de bord » et « Modifier les utilisateurs du tableau de bord » pour un espace de travail (tel que Dev), mais pas pour un autre (tel que Prod), il ne verra pas les autorisations de l'espace de travail Prod dans la page de détails des utilisateurs de son tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparaison des utilisateurs limités

| Type d'utilisateur limité | Description |
| --- | --- |
| Administrateur de l'espace de travail | Les administrateurs d'espace de travail disposent d'autorisations spécifiques à la gestion des espaces de travail, mais n'ont pas les mêmes prérogatives que les gestionnaires d'entreprise. Les utilisateurs limités peuvent hériter d'autorisations similaires à celles des administrateurs d'espace de travail s'ils disposent des autorisations nécessaires. |
| Administrateur (administrateur de l'entreprise) | Les administrateurs de l'entreprise disposent d'autorisations plus étendues, notamment la possibilité de supprimer des utilisateurs du tableau de bord. Cependant, ils ne peuvent pas supprimer leur propre compte et doivent contacter un autre administrateur de l'entreprise pour cette action. |
| Accès en lecture seule | Pour accéder à certaines parties du tableau de bord, telles que la page Campagnes, les utilisateurs doivent disposer des autorisations de consultation qui leur sont attribuées.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Erreur d'accès restreint

Les utilisateurs peuvent rencontrer des messages tels que « Vous devez disposer des autorisations « Afficher les pages de destination » pour accéder à cette page ». Dans de tels cas, l'utilisateur et l'administrateur du compte doivent s'assurer que les autorisations requises sont accordées. Si tel est le cas, veuillez tenter de résoudre le problème en désactivant puis en réactivant les autorisations de l'utilisateur. 

{% alert note %}
Il n'est pas possible de fusionner ou d'importer les autorisations d'un utilisateur d'un tableau de bord vers un autre.
{% endalert %}

## Modifier les autorisations d'un utilisateur

Pour modifier les autorisations actuelles d'un utilisateur en tant qu'administrateur, au sein de l'entreprise ou de l'espace de travail, veuillez vous rendre dans **Paramètres** > **Utilisateurs de l'entreprise**, puis sélectionner son nom.

![La page « Utilisateurs de l'entreprise » dans Braze affiche un tableau des utilisateurs du tableau de bord de Braze.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Admin

Les administrateurs ont accès à toutes les fonctionnalités et peuvent modifier tous les paramètres de l'entreprise. Ils peuvent le faire :

- Modifier les [paramètres d'approbation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Ajouter, modifier, supprimer, suspendre ou annuler la suspension d'autres [utilisateurs de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users).
- Exporter les utilisateurs de Braze au format CSV

Pour accorder ou supprimer les privilèges d'administrateur, sélectionnez **Cet utilisateur est un administrateur**, puis sélectionnez **Mettre à jour l'utilisateur**.

![Les détails de l'utilisateur sélectionné avec la case à cocher admin activée.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Si vous retirez les privilèges d'administrateur à un utilisateur, celui-ci ne pourra plus accéder à Braze tant que vous ne lui aurez pas attribué au moins une [autorisation au niveau de l'entreprise ou de l'espace de travail]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Company %}

### Entreprise

Pour gérer les autorisations suivantes au niveau de l'entreprise pour un utilisateur, cochez ou décochez la case en regard de l'autorisation en question. Lorsque vous avez terminé, sélectionnez **Mettre à jour l'utilisateur**.

|Nom de l’autorisation|Description|
|----------|-----------|
|Gérer les paramètres de l’entreprise|Permet aux utilisateurs de modifier les paramètres d'autorisation et la vérification de l'expéditeur.|
|Créer et supprimer des espaces de travail|Permet aux utilisateurs de créer et de supprimer des espaces de travail.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Espace de travail

Vous pouvez donner à un utilisateur des autorisations différentes pour chaque espace de travail auquel il appartient dans Braze. Pour gérer les autorisations au niveau de l'espace de travail, veuillez sélectionner **Sélectionner les espaces de travail et les autorisations**, puis choisissez manuellement leurs autorisations ou attribuez un [ensemble d'autorisations ou un rôle]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) que vous avez précédemment créé. Si vous devez donner à un utilisateur des autorisations différentes pour différents espaces de travail, répétez ce processus autant de fois que nécessaire. Pour obtenir une description de chaque autorisation, voir [Liste des autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Sous **Espaces de travail**, choisissez un ou plusieurs espaces de travail dans la liste déroulante. Ensuite, sous **Autorisations**, veuillez sélectionner une ou plusieurs autorisations. Ces autorisations ne leur seront attribuées que pour les espaces de travail que vous avez sélectionnés. Vous pouvez également sélectionner **Attribuer l'accès administrateur à l'espace de travail** si vous souhaitez leur accorder toutes les autorisations pour cet espace de travail.

Lorsque vous avez terminé, sélectionnez **Mettre à jour l'utilisateur**.

![Les autorisations au niveau de l'espace de travail sont sélectionnées manuellement dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Sous **Espaces de travail**, choisissez un ou plusieurs espaces de travail dans la liste déroulante. Ensuite, sous **Jeux de permissions**, choisissez un jeu de permissions. Ces autorisations ne leur seront attribuées que pour les espaces de travail que vous avez sélectionnés.

Lorsque vous avez terminé, sélectionnez **Mettre à jour l'utilisateur**.

![Autorisations au niveau de l'espace de travail attribuées via un ensemble d'autorisations dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Assign role %}

Sous **Espaces de travail**, choisissez un ou plusieurs espaces de travail dans la liste déroulante. Ensuite, sous **Rôle**, veuillez sélectionner un rôle. Ces autorisations ne leur seront attribuées que pour les espaces de travail que vous avez sélectionnés.

Lorsque vous avez terminé, sélectionnez **Mettre à jour l'utilisateur**.

![Autorisations au niveau de l'espace de travail attribuées via un rôle dans Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exporter les autorisations des utilisateurs

Pour télécharger une liste de vos utilisateurs et de leurs autorisations, allez dans **Paramètres** > **Utilisateurs de l'entreprise**, puis sélectionnez **Exporter les utilisateurs.** Un fichier CSV sera envoyé à votre adresse e-mail dans les plus brefs délais.

![La page « Utilisateurs de l'entreprise » dans Braze, avec l'option « Exporter les utilisateurs » mise en évidence.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Liste des autorisations

| Autorisation | Définition |
|-------------------------------------------------|---------------------|
| Afficher les détails de facturation                            | Veuillez consulter les détails de facturation. |
| Afficher les attributs personnalisés marqués comme PII            | Afficher les attributs personnalisés marqués comme PII |
| Afficher les données d'identification                                        | Afficher les données d'identification |
| Voir les profils utilisateur respectueux des données d'identification                | Accédez à la recherche d'utilisateurs et consultez les profils utilisateurs avec les informations personnelles identifiables (PII) expurgées. |
| Afficher les données d’utilisation                                 | Consulter les données d'utilisation |
| Fusionner les utilisateurs dupliqués                           | Veuillez fusionner les utilisateurs en double en un seul utilisateur. Les doublons sont supprimés après la fusion. |
| Afficher les utilisateurs dupliqués                         | Veuillez examiner quels profils utilisateurs sont des doublons. |
| Afficher les modèles Canvas                           | Afficher les modèles Canvas |
| Archiver les modèles Canvas                        | Déplacer les modèles canvas vers les archives |
| Lancer des blocs de contenu                           | Lancer des blocs de contenu |
| Gérer les centres de préférence                       | Lancement des centres de préférences |
| Exporter les données utilisateur                                | Veuillez télécharger les utilisateurs depuis le tableau de bord. |
| Modifier les intégrations Currents                      | Créer, mettre à jour et supprimer des intégrations currents |
| Voir l'intégration currents                       | Consulter les intégrations currents |
| Afficher les campagnes                                  | Afficher les campagnes |
| Modifier les campagnes                                  | Créer et mettre à jour des campagnes |
| Archiver les campagnes                               | Déplacer les campagnes vers les archives |
| Envoyer des campagnes                                  | Lancer, arrêter, suspendre ou reprendre des campagnes | 
| Envoyer des toiles                         		  | Démarrer, arrêter, mettre en pause ou reprendre les toiles |
| Afficher les règles de limite de fréquence                    | Afficher les règles de limite de fréquence |
| Modifier les règles de limitation de fréquence                    | Créer et mettre à jour les règles de limite de fréquence |
| Afficher les canvas                                   | Afficher les canvas |
| Modifier les canvas                                   | Créer et mettre à jour des canevas |
| Archiver les canvas                                | Déplacer les toiles vers les archives |
| Afficher les blocs de contenu                             | Afficher les blocs de contenu |
| Modifier les blocs de contenu                             | Créer et mettre à jour des blocs de contenu |
| Archiver les blocs de contenu                          | Déplacer les blocs de contenu vers les archives |
| Voir les indicateurs de fonctionnalité                              | Afficher les indicateurs de fonctionnalité |
| Modifier l’indicateur de fonctionnalité                              | Créer et mettre à jour des indicateurs de fonctionnalité |
| Indicateurs de fonctionnalité d'archivage                           | Déplacer les indicateurs de fonctionnalité vers les archives |
|  Consulter les modèles de messages WhatsApp                | Permet aux utilisateurs de visualiser [les modèles de messages WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/?tab=template%20messages#step-2-compose-your-whatsapp-message). |
| Modifier les modèles de messages WhatsApp | Permet aux utilisateurs de créer des modèles de messages WhatsApp dans le générateur de modèles. Cette fonctionnalité est actuellement disponible en accès anticipé. |
| Afficher le segment                                   | Afficher les segments. Les utilisateurs doivent disposer de l'autorisation « Afficher les segments » pour pouvoir bénéficier des autorisations « Modifier les segments » ou « Archiver les segments ». |
| Segments d'archives                                | Archiver et désarchiver des segments. Les utilisateurs disposant de l'autorisation « Archiver les segments » doivent également se voir accorder l'autorisation « Afficher les segments ». |
| Modifier les segments                                   | Créer et mettre à jour des segments. Les utilisateurs disposant de l'autorisation « Modifier les segments » doivent également se voir accorder l'autorisation « Afficher les segments ». |
| Voir le groupe de contrôle global                       | Veuillez consulter la page de configuration du groupe de contrôle global. |
| Modifier le groupe de contrôle global                       | Veuillez créer et enregistrer les modifications apportées au groupe de contrôle global. Les utilisateurs disposant de l'autorisation « Modifier le groupe de contrôle global » doivent également disposer des autorisations « Modifier les campagnes » et « Modifier les canevas ». Les utilisateurs disposant de l'autorisation « Modifier le groupe de contrôle global » se voient également accorder l'autorisation « Afficher le groupe de contrôle global ». |
| Afficher les modèles de bannières                           | Consulter les modèles de bannières |
| Modifier les modèles de bannières                           | Créer et mettre à jour des modèles de bannières |
| Modèles de bannières d'archives                   	  | Veuillez déplacer les modèles de bannières vers les archives. |
| Afficher les modèles d'e-mail                            | Consulter les modèles d'e-mails |
| Modifier les modèles d’e-mail                            | Créer et mettre à jour des modèles d'e-mails |
| Archiver les modèles d'e-mail                         | Veuillez déplacer les modèles d'e-mails vers les archives. |
| Afficher les modèles de lien   	                      | Consulter les modèles de lien |
| Modifier les modèles de lien	                          | Créer et mettre à jour des modèles de liens |
| Publier les pages d’accueil                           | Activer une page d'accueil provisoire |
| Modifier les projets de page de destination                        | Créer et enregistrer des brouillons de pages de destination |
| Afficher la page de destination			                  | Afficher les pages de destination |
| Modifier les modèles de page de destination	                  |  Créer et mettre à jour des modèles de pages d'accueil |
| Voir les modèles de pages d'accueil	                  | Consulter les modèles de pages d'accueil |
| Modèle de page d'accueil d'archives 	              | Veuillez déplacer les modèles de page d'accueil vers les archives. |
| Voir les ressources de la bibliothèque multimédia                       | Consulter les ressources de la bibliothèque multimédia |
| Modifier les ressources de la bibliothèque multimédia                       | Créer et mettre à jour les ressources de la bibliothèque multimédia |
| Supprimer des ressources de la bibliothèque multimédia                     | Supprimer définitivement les ressources de la bibliothèque multimédia |
| Afficher les emplacements                                  | Afficher les emplacements |
| Modifier les emplacements                                  | Créer et modifier des emplacements |
| Emplacement des archives                               | Déplacer les localisations vers les archives |
| Consulter les codes de promotion                            | Consulter les codes promotionnels |
| Modifier les codes de promotion                            | Créer et mettre à jour des codes promotionnels |
| Codes de promotion des exportations                          | Veuillez télécharger la liste des codes promotionnels depuis le tableau de bord. |
| Afficher les centres de préférences                         | Consulter les centres de préférences  |
| Modifier les centres de préférences                         | Créer et mettre à jour les centres de préférences |
| Gérer les centres de préférence	                      | Activer un brouillon de Centre de préférences ou mettre à jour un brouillon existant |
| Voir les clés API                                   | Afficher les clés API |
| Modifier les clés API                                   | Créer et mettre à jour des clés API |
| Afficher les groupes internes                            | Afficher les groupes internes |
| Modifier les groupes internes                            | Créer et mettre à jour des groupes internes |
| Afficher le journal d'activité des messages                       | Consulter les journaux d'activité des messages |
| Journal des événements utilisateurs                             | Consulter les journaux des événements utilisateurs |
| Afficher les identifiants API                            | Afficher les identifiants API et autres identifiants |
| Voir le tableau de bord d'utilisation de l'API                        | Consulter le tableau de bord d'utilisation de l'API |
| Voir les limites de l'API                                 | Consulter les limites de débit de l'API |
| Voir les alertes d'utilisation de l'API                           | Consulter les alertes d'utilisation de l'API |
| Modifier les alertes d'utilisation de l'API                           | Créer et mettre à jour des alertes d'utilisation de l'API |
| Modifier le débogueur SDK                               | Créer et télécharger des sessions SDK Debugger |
| Afficher le débogueur SDK                               | Consulter le débogueur SDK ou les sessions de débogage |
| Afficher les paramètres de l'application                               | Veuillez consulter la page Paramètres de l'application. |
| Modifier les paramètres de l'application                               | Créer, modifier et mettre à jour des applications dans les paramètres de l'application |
| Afficher les catalogues                                   | Consulter les catalogues et les sélections |
| Modifier les catalogues                                   | Créer et mettre à jour des catalogues et des sélections |
| Exporter des catalogues                                 | Veuillez télécharger les catalogues depuis le tableau de bord. |
| Supprimer les catalogues                                 | Supprimer définitivement les catalogues |
| Afficher les utilisateurs du tableau de bord                            | Afficher les utilisateurs de l'entreprise |
| Modifier les utilisateurs du tableau de bord                            | Créer et mettre à jour les utilisateurs de l'entreprise 
| Afficher les paramètres d'e-mail                             | Consulter les préférences de e-mail |
| Modifier les paramètres d'e-mail                             | Activer et mettre à jour les préférences de e-mail | 
| Modifier l'identifiant Cryptage au niveau du champ            | Activer et mettre à jour les paramètres de chiffrement au niveau du champ |
| Afficher les attributs personnalisés                          | Consulter les attributs personnalisés et le rapport d'utilisation |
| Modifier des attributs personnalisés                          | Créer et mettre à jour des attributs personnalisés |
| Ajouter des attributs personnalisés à la liste de blocage                     | Ajouter des attributs personnalisés à une liste de blocage qui restreint l'utilisation dans le tableau de bord |
| Supprimer des attributs personnalisés                        | Supprimer définitivement les attributs personnalisés |
| Exporter des attributs personnalisés                        | Veuillez télécharger les attributs personnalisés à partir du tableau de bord. |
| Afficher les événements personnalisés                              | Consultez les événements personnalisés et le rapport d'utilisation, et ajoutez des événements personnalisés au rapport d'analyse/analytique quotidien envoyé par e-mail. |
| Modifier des événements personnalisés                              | Créer et mettre à jour des custom events |
| Ajouter des événements personnalisés à la liste de blocage                         | Ajouter des événements personnalisés à une liste de blocage qui restreint l'utilisation dans le tableau de bord |
| Supprimer des événements personnalisés                            | Supprimer définitivement les custom events |
| Exportation d'événements personnalisés                            | Veuillez télécharger les custom events depuis le tableau de bord. |
| Modifier la segmentation des propriétés d'événements personnalisés         | Activer et désactiver la segmentation pour les propriétés d'événements personnalisés |
| Afficher les produits                                   | Consulter les produits |
| Modifier des produits                                   | Créer et mettre à jour des produits |
| Ajouter des produits à la liste de blocage                              | Ajouter des produits à une liste de blocage qui restreint leur utilisation dans le tableau de bord |
| Modifier la segmentation des propriétés d'achat             | Activer et désactiver la segmentation pour les propriétés d'achat |
| Modifier les partenaires technologiques                        | Créer et mettre à jour les partenaires technologiques |
| Modifier l'ingestion de données cloud                       | Créer, mettre à jour et supprimer des sources et des synchronisations |
| Afficher les paramètres multilingues                    | Afficher les paramètres multilingues |
| Créer des paramètres régionaux multilingues           | Créer et mettre à jour les paramètres régionaux multilingues |
| Supprimer les paramètres régionaux multilingues           | Supprimer définitivement les paramètres régionaux multilingues |
| Modifier les abonnements                              | Créer et mettre à jour des groupes d'abonnement |
| Afficher les balises                                       | Afficher les étiquettes |
| Modifier les balises                                       | Créer et mettre à jour des tags |
| Supprimer les balises                                     | Supprimer définitivement les tags |
| Voir les équipes                                      | Voir les équipes |
| Modifier les équipes                                      | Créer et mettre à jour des Teams |
| Archiver les équipes                                   | Déplacer les équipes vers les archives |
| Afficher la transformation des données                        | Afficher les transformations de données |
| Modifier la transformation des données                        | Créer et mettre à jour des transformations de données |
| Lancez des campagnes                                | Lancer, arrêter, suspendre ou reprendre des campagnes existantes |
| Lancer des canvas                                 | Démarrer, arrêter, mettre en pause ou reprendre des canevas existants |
| Modifier les modèles de canvas                           | Créer et mettre à jour des modèles Canvas |
| Approuver la campagne                               | Veuillez approuver ou refuser les campagnes. Le [processus d'approbation des campagnes]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) doit être activé pour que cette autorisation s'applique. Ce paramètre es actuellement disponible en accès anticipé. Veuillez contacter votre gestionnaire de compte si vous souhaitez participer à l'accès anticipé. |
| Approuver les canvas                                | Veuillez approuver ou refuser les Canvases. Le [processus d'approbation des toiles]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) doit être activé pour que cette autorisation s'applique. Ce paramètre es actuellement disponible en accès anticipé. Veuillez contacter votre gestionnaire de compte si vous souhaitez participer à l'accès anticipé. |
| Afficher les placements                                 | Afficher l'emplacement des bannières |
| Modifier les emplacements                                 | Afficher les emplacements des bannières sans apporter de modifications |
| Archiver les placements                              | Déplacer les emplacements des bannières vers les archives |
| Afficher les paramètres des notifications push                              | Afficher les paramètres Push |
| Modifier les paramètres des notifications push                              | Créer et mettre à jour les paramètres Push |
| Modifier les rapports                                    | Créer et mettre à jour des rapports |
| Voir les importations d'utilisateurs                               | Afficher les importations d'utilisateurs CSV |
| Importer des utilisateurs                                    | Veuillez ajouter les utilisateurs au tableau de bord. |
| Modifier les données d'utilisateur                                  | Créer et mettre à jour les données utilisateur |
| Afficher la fusion des utilisateurs                                | Consulter la liste des enregistrements fusionnés des utilisateurs |
| Afficher les enregistrements de suppression d'utilisateurs	            	  | Afficher les enregistrements de suppression d'utilisateurs |
| Supprimer des utilisateurs du tableau de bord	                  | Supprimez définitivement des utilisateurs du tableau de bord, individuellement ou en masse. |      
| Voir les agents d'intelligence artificielle personnalisés                           | Permet aux utilisateurs de visualiser les agents d’intelligence artificielle personnalisés. |
| Modifier les agents d'intelligence artificielle personnalisés                           | Permet aux utilisateurs de créer et de mettre à jour des agents d’intelligence artificielle personnalisés. |
| Archiver les agents d'intelligence artificielle personnalisés                        | Permet aux utilisateurs d'archiver des agents d'intelligence artificielle personnalisés. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }