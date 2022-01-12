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

L'intégration de Braze et BlueConic permet aux utilisateurs d'unifier les données de manière persistante, les profils individuels et ensuite les synchroniser sur les deux systèmes pour les objectifs d'importation via un serveur Amazon Web Services S3. Parmi les objectifs potentiels figurent des initiatives axées sur la croissance, l'orchestration du cycle de vie des clients, la modélisation et l'analyse, les produits et expériences numériques, la monétisation basée sur le public, et plus encore. Cette intégration prend en charge à la fois l'importation et l'exportation de lots planifiés.

## Pré-requis

| Exigences                                   | Libellé                                                                                                                                                                                                      |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Compte BlueConic                            | Un [compte BlueConic][1] est requis pour profiter de ce partenariat. Vous aurez besoin d'accéder à la vue [et modifier les connexions][4] dans votre compte BlueConic pour accéder aux plugins.              |
| Braze clé API REST                          | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le **tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API** |
| Point de terminaison REST Braze             | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance][2].                                                                                                  |
| Authentification S3                         | Vous aurez besoin d'accéder à un serveur Amazon Web Services (S3) pour exporter et importer les données.                                                                                                     |
| Clé d'accès ID<br>clé d'accès secrète | L'ID de la clé d'accès et la clé d'accès secrète vous permettront d'authentifier votre serveur S3 pour l'importation et l'exportation.                                                                       |
| Seau AWS                                    | Vous devrez vous connecter à S3 dans le plugin. Après l'authentification, les segments disponibles s'afficheront dans un menu déroulant. C'est là que les fichiers à importer ou à exporter sont stockés.    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Intégration

### Étape 1 : Créer une connexion Braze

Dans BlueConic, sélectionnez **Connexions** dans la barre de navigation, puis **Ajouter une connexion**. Dans l'invite qui apparaît, recherchez **Braze** et sélectionnez **Connexion Braze**.

Développer ou réduire les champs de métadonnées disponibles dans la connexion en cliquant sur l'icône du chevron gris. Dans ces champs, vous pouvez mettre en favori cette connexion, nommer votre connexion, ajouter des étiquettes, inclure une description, et choisissez d'obtenir des notifications par courriel si la connexion [s'exécute ou échoue à exécuter][5].

Enregistrez vos paramètres.

### Étape 2 : Configurer une connexion Braze

Pour configurer la connexion entre BlueConic et Braze, vous devez ajouter vos identifiants de compte Braze et les informations de compte Amazon Web Services (S3) pour authentifier la connexion.

1. Dans BlueConic, sélectionnez **Configurer et exécuter** dans la section **Configuration** dans le panneau de gauche.<br><br>
2. Dans la page d'authentification de Braze qui s'ouvre, entrez votre point de terminaison de l'API Braze et votre clé API Braze.<br> ![BlueConic Authentication]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. Dans la section Configuration et authentification S3, entrez l'ID de la clé d'accès Amazon Web Services (S3), la clé d'accès secrète et le compartiment S3. Enregistrez vos paramètres. <br>![BlueConic S3 Authentication]({% image_buster /assets/img/blueconic/braze3.png %})![BlueConic S3 Authentication]({% image_buster /assets/img/blueconic/braze3.png %}) {: style="max-width:80%;"}

### Étape 3 : Créer des objectifs d'importation ou d'exportation (mappage d'importation)

Une fois l'authentification terminée, vous devez créer au moins un objectif d'importation ou d'exportation, allumer la connexion et planifier ou exécuter la connexion.

{% tabs %}
{% tab Import %}

1. Sélectionnez **Importer des données dans BlueConic** dans le panneau de gauche pour ouvrir la page de configuration des données de Braze.<br><br>
2. Sélectionnez l'emplacement des données au Brésil. Ici vous pouvez dire à BlueConic où trouver les données à importer en sélectionnant votre public Braze.<br>![BlueConic import goal]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. Ensuite, cartographiez les identifiants entre Braze et BlueConic. <br>![BlueConic import goal]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> Pour lier les données client entre les deux systèmes, entrez un ou plusieurs identifiants client.<br>Utiliser la **Autoriser la création...** case à cocher pour permettre à BlueConic de créer de nouveaux profils pour des données qui ne correspondent pas à un profil BlueConic existant.<br><br>
4. Ensuite, correspondez aux champs de données BlueConic que vous exportez vers les champs Braze. Utilisez les champs déroulants pour sélectionner l'identifiant de profil BlueConic ou une propriété de profil sur la gauche et sélectionnez l'identifiant de profil Braze correspondant. Ensuite, utilisez le menu déroulant pour spécifier comment le contenu importé doit être ajouté aux valeurs existantes : ajouté, , ne définit que si la propriété de profil est vide, ou à effacer (si le champ Braze est vide).<br>![BlueConic import map]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>Utilisez le bouton **Ajouter mapping** pour créer des lignes de mappage supplémentaires au besoin. Vous pouvez ajouter plusieurs lignes de mappage avec l'option **Ajouter les champs restants**. BlueConic détecte les champs restants de Braze et les met en correspondance avec les propriétés de profil BlueConic. Vous pouvez définir la stratégie de fusion pour les importations (ensemble, ajouter, somme, si vide ou vides) et fournir un préfixe personnalisé pour les noms des propriétés de profil BlueConic.<br><br>
5. Enfin, sélectionnez **Exécuter la connexion** pour démarrer la connexion. Visitez [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) pour en savoir plus sur la planification et l'exécution des connexions.
{% endtab %}
{% tab Export %}

1. Sélectionnez **Exporter des données à Braze** dans le panneau de gauche pour configurer votre exportation de données de BlueConic vers Braze.<br><br>
2. Choisissez un segment BlueConic pour l'exportation. Seuls les profils dans ce segment avec des identifiants correspondants à Braze seront exportés.<br>![BlueConic segment]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. Ensuite, liez les identifiants entre les profils BlueConic et les champs Braze. Vous pouvez optionnellement choisir de laisser BlueConic créer de nouveaux enregistrements si aucune correspondance existante n'est trouvée.<br>![BlueConic export map]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. Ensuite, correspondez aux champs de données BlueConic que vous exportez vers les champs Braze. Utilisez le menu déroulant de l'icône BlueConic pour choisir le type d'informations [](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals) que vous souhaitez exporter. Les informations disponibles incluent les propriétés de profil, les identifiants de profil BlueCinic, les segments associés, toutes les interactions vues, les niveaux de permission et une valeur de texte statique.<br>![BlueConic import map]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. Enfin, cliquez sur **Exécuter la connexion** pour démarrer la connexion. Visitez [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) pour en savoir plus sur la planification et l'exécution des connexions.
{% endtab %}
{% endtabs %}

## Étape 4 : Activer/désactiver la connexion

Utilisez le bouton à côté du titre de la connexion Braze pour activer/désactiver la connexion. Une connexion doit être activée pour être exécutée pendant les heures planifiées.

[1]: https://www.blueconic.com/

[1]: https://www.blueconic.com/
[2]: https://portal.aws.amazon.com/billing/signup#/start
[4]: https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles
[5]: https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ