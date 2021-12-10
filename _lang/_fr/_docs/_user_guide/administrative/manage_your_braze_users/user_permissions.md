---
nav_title: Permissions utilisateur du compte Braze
article_title: Permissions utilisateur du compte Braze
page_order: 2
page_type: Référence
description: "Cet article de référence couvre les autorisations utilisateur au Brésil, comme le choix de qui peut accéder à vos applications sur le tableau de bord Braze."
tool: Tableau de bord
---

# Paramétrage des permissions de l'utilisateur

La fonction d’autorisation utilisateur de Braze vous permet de choisir qui peut accéder à vos applications sur le tableau de bord de Braze en assignant différents utilisateurs avec soit un administrateur (désigné par une couronne jaune à côté de votre nom d’utilisateur) soit une permission limitée. Le créateur du groupe d'applications recevra automatiquement l'accès Administrateur. Ces paramètres peuvent être trouvés en accédant à votre nom dans le coin supérieur droit du tableau de bord et en sélectionnant "Gérer les utilisateurs" dans le menu déroulant.

!\[Permissions utilisateurs\]\[30\]

| Niveau d'accès | Permissions                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administrateur | Les administrateurs ont accès à toutes les fonctionnalités disponibles.                                                                                                                                                                                                                                                                                                                            |
| Limité         | Les utilisateurs limités sont entièrement personnalisés à plusieurs niveaux (décrits ci-dessous). Lorsque vous basculez les permissions d'un utilisateur de l'administrateur à une limite, cet utilisateur n'a plus accès à aucune partie du tableau de bord de Braze jusqu'à ce que vous le jugiez possible en utilisant les cases à cocher qui apparaissent sous la case Modifier l'utilisateur. |
{: .reset-td-br-1 .reset-td-br-2}

## Modification des permissions de l'utilisateur

À partir de la page Gérer les utilisateurs, vous pouvez modifier les permissions d'un utilisateur spécifique, soit en leur permettant de rester en tant qu'administrateur par défaut, soit en les changeant pour un rôle limité. Pour modifier leur rôle, cliquez sur l'icône d'édition dans la ligne de l'utilisateur et sélectionnez Limité dans la liste déroulante du rôle utilisateur.

!\[Modifier les permissions d'utilisateur\]\[29\]

Lorsque vous basculez les autorisations d'un utilisateur de Admin à Limited, cet utilisateur n'a plus accès à aucune partie de Braze tant que vous n'avez pas défini ces permissions spécifiques en utilisant les cases à cocher qui apparaissent sous la case Modifier l'utilisateur. Les explications pour chacune de ces permissions peuvent être trouvées dans le diagramme de niveau d'accès en haut de cette page.

## Autorisations de rôle limité et d'équipe

Vous pouvez gérer les autorisations utilisateur par groupe ou individuellement en utilisant la page Permissions de l'utilisateur.

!\[userpermissions\]\[89\]

| Nom de la permission                                         | Définition/Paramètres                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administrateur                                               | A accès à toutes les fonctionnalités disponibles, paramètre par défaut pour tous les nouveaux utilisateurs. Peut mettre à jour les paramètres de la société (nom de la société et fuseau horaire), ce que les Utilisateurs Limités ne peuvent pas faire.                                                                              |
| Accès aux campagnes, Canvases, Cartes, Segments, Médiathèque | L'utilisateur peut voir les métriques de performance de campagne et de Canvas et créer des brouillons de campagnes et de toiles, afficher le fil d'actualité, les segments, les modèles et les médias, créer des modèles, télécharger des médias et afficher les rapports d'engagement.                                               |
| Envoyer des campagnes, des toiles                            | Permet à l'utilisateur d'éditer, d'archiver, d'arrêter, de dupliquer des campagnes et des toiles, de créer des campagnes, de lancer des toiles. Pour lancer des blocs de contenu existants, les autorisations **Envoyer des campagnes, Canvases** et **Publier des cartes** sont requises.                                            |
| Publier des cartes                                           | Permet à l'utilisateur de créer et modifier des cartes de flux d'actualités. Vous pouvez toujours voir les cartes sans cette autorisation. Pour lancer des blocs de contenu existants, à la fois **Publier des Cartes** et **Envoyer des campagnes, les autorisations de Canvases** sont requises.                                    |
| Modifier les segments                                        | Permet aux utilisateurs de créer et de modifier un segment. Vous pouvez toujours créer des campagnes avec des segments et des filtres existants sans cette autorisation. Vous avez besoin de cette autorisation pour générer un segment à partir des utilisateurs dans un CSV ou redimensionner le groupe d'utilisateurs dans le CSV. |
| Exporter les données utilisateur                             | Permet à l'utilisateur d'exporter vos données utilisateur depuis des Segments, des campagnes et des Canvases.                                                                                                                                                                                                                         |
| View PII                                                     | Permet à l'utilisateur de voir les informations personnelles identifiables dans le tableau de bord. Notez que les deux adresses e-mail et le numéro de téléphone seront visibles.                                                                                                                                                     |
| Voir le profil utilisateur                                   | Permet à l'utilisateur d'accéder à la page de recherche d'utilisateurs.                                                                                                                                                                                                                                                               |
| Gérer les utilisateurs du tableau de bord                    | Permet à l'utilisateur de visualiser, modifier et gérer l'onglet Gérer les utilisateurs. Les utilisateurs ayant cette permission peuvent modifier les permissions de n'importe quel utilisateur, y compris lui-même. À ce titre, cette autorisation devrait être considérée comme un niveau d'accès administratif.                    |
| Gérer la médiathèque                                         | Permet à l'utilisateur de télécharger des images dans la bibliothèque. Vous pouvez toujours télécharger des photos/audio, etc. directement dans une campagne sans cette autorisation.                                                                                                                                                 |
| Voir les données d'utilisation                               | Permet à l'utilisateur de voir l'utilisation de l'application.                                                                                                                                                                                                                                                                        |
| Importer et mettre à jour les données utilisateur            | Permet à l'utilisateur d'importer des fichiers CSV et de mettre à jour des utilisateurs de l'application ainsi que de voir la page d'importation des utilisateurs.                                                                                                                                                                    |
| Voir les détails de facturation                              | Permet à l'utilisateur de voir les abonnements et la facturation.                                                                                                                                                                                                                                                                     |
| Accéder à la console de développement                        | Permet d'accéder à la console développeur (où vous pouvez afficher les clés de l'API, le journal d'activité de la campagne API, le journal des utilisateurs d'événements et les groupes internes pour les messages de test).                                                                                                          |
| Gérer les intégrations externes                              | Permet d'accéder à tous les onglets sous partenaires technologiques et la possibilité de synchroniser Braze avec d'autres plateformes.                                                                                                                                                                                                |
| Gérer les applications                                       | Permet à l'utilisateur de modifier les paramètres (sous Gérer les paramètres).                                                                                                                                                                                                                                                        |
| Gérer les équipes                                            | Permet à l'utilisateur de gérer les équipes qui se trouvent sous "Gérer les paramètres". La possibilité de sélectionner cette autorisation dépend de votre contrat avec Braze.                                                                                                                                                        |
| Gérer les événements, les attributs, les achats              | Permet à l'utilisateur de modifier les attributs personnalisés, (les utilisateurs sans cette capacité peuvent toujours voir les attributs personnalisés), éditer et afficher les propriétés des événements personnalisés, et modifier et afficher les propriétés des produits (tout cela sous Gérer les paramètres).                  |
| Gérer les tags                                               | Permet aux utilisateurs de modifier ou de supprimer des tags (sous Gérer les paramètres). Vous n'avez pas besoin de cette autorisation pour ajouter des tags à des campagnes ou des segments.                                                                                                                                         |
| Gérer les paramètres de messagerie                           | Permet à l'utilisateur d'enregistrer les modifications de configuration de l'e-mail (onglet Paramètres de messagerie sous "Gérer les paramètres").                                                                                                                                                                                    |
| Gérer les groupes d'abonnement                               | Permet à l'utilisateur de créer et de gérer des groupes d'abonnement.                                                                                                                                                                                                                                                                 |
{: .reset-td-br-1 .reset-td-br-2}

## Autorisations utilisateur App-by-app

Les utilisateurs individuels peuvent se voir accorder différents degrés d'accès sur une base d'application par application.

| Diplôme d'autorisations limité                 | Détails du produit                                                                  |
| ---------------------------------------------- | ----------------------------------------------------------------------------------- |
| Niveau de la société                           | Concernant la gestion des paramètres d'application et de groupe de l'entreprise.    |
| Permissions de niveau de groupe d'applications | Quels groupes d'applications l'utilisateur limité doit-il être en mesure de gérer ? |
| Paramètres du niveau de l'application          | Quel niveau d'accès d'édition devrait avoir cet utilisateur limité ?                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
[29]: {% image_buster /assets/img_archive/editing_user_permission_new.png %} "Modifier les permissions utilisateur" [30]: {% image_buster /assets/img_archive/two_factor_authentication_manage_users_new.png %} [89]: {% image_buster /assets/img/user_permissions_selection.png %}
