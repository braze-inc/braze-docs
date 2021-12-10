---
nav_title: BleuConic
page_order: 8
description: "Cet article couvre l’intégration de Braze et BlueConic. BlueConic est une plateforme de données client de premier plan qui fournit des données accessibles à la première partie partout et à chaque fois qu’il est nécessaire de transformer les relations avec les clients et de stimuler la croissance de l’entreprise."
alias: /fr/partners/blueconic/
page_type: partenaire
search_tag: Partenaire
---

# BleuConic

> [BlueConic][1], la plateforme de données client la plus performante, libère les données de la première partie des entreprises de systèmes disparates et les rend accessibles partout et à chaque fois qu'il est nécessaire de transformer les relations avec les clients et de stimuler la croissance de l'entreprise.

Avec Blueconic, les utilisateurs de Braze peuvent unifier les données en permanent, les profils individuels et ensuite les synchroniser entre les points de contact des clients et les systèmes à l'appui d'un large éventail d'initiatives axées sur la croissance. y compris l'orchestration du cycle de vie des clients, la modélisation et l'analyse, les produits et expériences numériques, la monétisation basée sur le public et bien plus encore.

## Pré-requis

| Exigences                       | Origine                     | Accès                                                                                                                                                                                                        | Libellé                                                                                                                                                                                                                                   |
| ------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Point de terminaison REST Braze | Brasero                     | [Liste des points d'extrémité REST Braze][2]                                                                                                                                                                 | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL de Braze pour votre instance.                                                                                                                                 |
| Clé API Braze                   | Brasero                     | Vous devrez créer une nouvelle clé d'API.<br><br>Ceci peut être créé dans la __Console Développeur -> Paramètres API -> Créer une nouvelle clé API__ avec __utilisateurs. permissions__ de rack. | Cette clé d'API vous permet d'authentifier Braze au sein de la plateforme BlueConic                                                                                                                                                       |
| Authentification S3             | Services Web d'Amazon (AWS) | [Compte AWS][2]                                                                                                                                                                                              | Vous devez avoir accès à un serveur Amazon Web Services (S3) car les données seront exportées et/ou importées via un serveur S3.                                                                                                          |
| ID de clé d'accès & clé secrète | AWS                         | [Page des identifiants de sécurité S3][3]                                                                                                                                                                    | L'ID de la clé d'accès vous permettra d'authentifier votre serveur S3 pour l'importation et l'exportation de<br><br>La clé d'accès secrète vous permettra d'authentifier votre serveur S3 pour l'importation et l'exportation |
| Seau                            | AWS                         | Vous devrez vous connecter à S3 dans le plugin. Après authentification, les segments disponibles s'afficheront dans un menu déroulant                                                                        | C'est là que les fichiers à importer ou à exporter sont stockés.                                                                                                                                                                          |
| Compte BlueConic                | BleuConic                   | [BleuConic][1]                                                                                                                                                                                               | Vous devrez avoir un accès [pour voir et éditer les Connexions][4] dans votre compte BlueConic pour accéder aux plugins                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

La connexion Braze et BlueConic vous permet d'enrichir les données de profil sur les deux plates-formes pour les objectifs d'importation via un serveur Amazon S3. Cette connexion prend en charge l'importation et l'exportation de lots planifiés. La plate-forme de données client BlueConic exploite les données requises pour alimenter la reconnaissance d'une personne à chaque interaction et synchronise ensuite son intention à travers l'écosystème de marketing. En échangeant des données de profil entre BlueConic et Braze, vous pouvez partager des données clients provenant de profils BlueConic en utilisant des données stockées au Brésil.

### Étape 1 : Créer une connexion Braze

1. Sur la plate-forme BlueConic, sélectionnez __Connexions__ dans la barre de navigation, puis __Ajouter une connexion__. Dans la fenêtre pop-up qui apparaît, entrez "Braze" dans la barre de recherche et sélectionnez __Connexion Braze__.<br><br>![BlueConic Plugin Gallery Braze Connection]({% image_buster /assets/img/blueconic/braze1.png %}){: style="max-width:50%;"}<br><br>
2. Dans la connexion Braze, développez ou réduisez les champs de métadonnées en cliquant sur l'icône du chevron gris. Dans ces champs, vous pouvez marquer la connexion comme un favori, ajouter des libellés et écrire une brève description. Vous pouvez également choisir d'obtenir [des notifications par e-mail lorsque la connexion s'exécute ou échoue à exécuter][5]. <br><br>
3. Enfin, entrez le nom de votre connexion en haut de la page et enregistrez vos paramètres.

### Étape 2 : Configurer une connexion de Braze avec BlueConic

Pour configurer la connexion entre BlueConic et Braze, vous devez ajouter vos identifiants de compte Braze et les informations de compte Amazon Web Services (S3) pour authentifier la connexion.

1. Sélectionnez __Configurer et exécuter__ dans la section Configuration dans le panneau de gauche.<br><br>
2. Dans la section d'authentification de Braze, entrez l'URL de votre instance Braze et la clé de l'API Braze.<br><br>![BlueConic Authentication]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. Dans la section Configuration et authentification S3, entrez l'ID de la clé d'accès Amazon Web Services (S3), la clé d'accès secrète et le compartiment S3.<br><br>![BlueConic S3 Authentication]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}<br><br>
4. Enregistrez vos paramètres.

### Étape 3 : Création d'objectifs d'importation (mapping d'importation)

Une fois l'authentification terminée, vous créerez au moins un objectif d'importation ou d'exportation, allumerez la connexion et planifierez ou exécuterez la connexion.

1. Sélectionnez __Importer des données dans BlueConic__ dans le panneau de gauche pour ouvrir la page pour configurer l'importation de données de Braze vers BlueConic.<br><br>
2. Sélectionnez l'emplacement des données au Brésil. Ici vous pouvez dire à BlueConic où trouver les données à importer en sélectionnant votre public Braze.<br><br>![BlueConic Import Goal]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. Ensuite, vous devez cartographier les identifiants entre Braze et BlueConic. <br><br>![BlueConic Import Goal]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> Pour lier les données client entre les deux systèmes, entrez un ou plusieurs identifiants client. Utilisez les champs déroulants pour sélectionner l'identifiant du profil BlueConic ou une propriété de profil sur la gauche, puis sélectionnez l'identifiant du profil Braze correspondant. Ensuite, utilisez le menu déroulant pour spécifier comment le contenu importé doit être ajouté aux valeurs existantes : ajouté, , ne définit que si la propriété de profil est vide, ou à effacer (si le champ Braze est vide). <br><br>Utiliser la __Autoriser la création...__ case à cocher pour permettre à BlueConic de créer de nouveaux profils pour les données qui ne correspondent pas à un profil BlueConic existant.<br><br>![BlueConic Import Map]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
4. Utilisez le bouton __Ajouter un mapping__ pour créer des lignes de mappage supplémentaires au besoin. Vous pouvez ajouter plusieurs lignes de mappage à la fois avec l'option __Ajouter les champs restants__. BlueConic détecte les champs restants de Braze et les met en correspondance avec les propriétés de profil BlueConic. Vous pouvez définir la stratégie de fusion pour les importations (ensemble, ajout, somme, si vide ou vides) et fournir un préfixe personnalisé pour les noms des propriétés de profil BlueConic.<br><br>
5. Enfin, sélectionnez __Exécuter la connexion__ pour démarrer la connexion. Voir [la planification et l'exécution des connexions][6].

## Étape 4 : Créer des objectifs d'exportation (mappage d'exportation)

Sélectionnez __Exporter des données à Braze__ dans le panneau de gauche pour configurer votre exportation de données de BlueConic vers Braze. Choisissez un segment BlueConic pour l'exportation. Seuls les profils dans ce segment qui ont des identifiants correspondants dans Braze seront exportés.

Comme le mappage d'importation affiché à l'étape 3, vous devez lier les identifiants entre BlueConic et Braze, les identifiants d'exportation correspondants entre les profils BlueConic et les champs Braze. Vous pouvez optionnellement choisir de laisser BlueConic créer de nouveaux enregistrements dans Braze si aucune correspondance existante n'est trouvée.

![Carte BlueConic Export]({% image_buster /assets/img/blueconic/braze7.png %}){: style="largeur-max-80%;"}

Utilisez le menu déroulant de l'icône BlueConic pour choisir le type d'informations que vous souhaitez exporter.

Enfin, cliquez sur __Exécuter la connexion__ pour démarrer la connexion. Voir [la planification et l'exécution des connexions][6]

## Utiliser cette intégration

Utilisez le bouton à côté du titre de la connexion Braze pour activer/désactiver la connexion. Une connexion doit être _sur_ pour être exécutée pendant les heures planifiées.

[1]: https://www.blueconic.com/

[1]: https://www.blueconic.com/
[2]: https://portal.aws.amazon.com/billing/signup#/start
[2]: https://portal.aws.amazon.com/billing/signup#/start
[3]: https://console.aws.amazon.com/iam/home?#security_credential
[4]: https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles
[5]: https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ
[6]: https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections
