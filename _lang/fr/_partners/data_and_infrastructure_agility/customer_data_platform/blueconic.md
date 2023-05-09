---
nav_title: BlueConic
article_title: BlueConic
page_order: 8
description: "Cet article de référence présente le partenariat entre Braze et BlueConic, une plateforme de données client pure play leader du marché qui permet aux utilisateurs d’unifier les données dans des profils individuels persistants, puis de les synchroniser entre les deux systèmes pour réaliser des objectifs d’importation via un serveur Amazon Web Services S3."
alias: /partners/blueconic/
page_type: partner
search_tag: Partenaire

---

# BlueConic

> [BlueConic][1] est une la plateforme de données client pure play leader du marché qui libère les données first-party des entreprises stockées dans des systèmes disparates et les rend accessibles à tout moment et partout où elles sont nécessaires afin de transformer les relations client et de stimuler la croissance. 

L’intégration de Braze et BlueConic permet aux utilisateurs d’unifier les données dans des profils individuels persistants, puis de les synchroniser entre les deux systèmes pour réaliser des objectifs d’importation via un serveur Amazon Web Services S3. Les objectifs potentiels comprennent des initiatives axées sur la croissance, l’orchestration du cycle de vie des clients, la modélisation, l’analyse, les produits et expériences numériques, la monétisation basée sur les audiences, etc. Cette intégration prend en charge l’importation et l’exportation programmées de lots. 

{% alert important %}
Avec l’intégration, BlueConic enverra des deltas (données modifiées) lors de chaque synchronisation. Cela inclut tous les profils modifiés depuis le dernier envoi ainsi que tous les attributs de ce profil. Pensez à surveiller l’utilisation des points de données.
{% endalert %}

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte BlueConic | Un compte [BlueConic][1] est requis pour profiter de ce partenariat. Vous aurez besoin d’accéder à [view and edit connections (afficher et modifier les connexions)][4] sur votre compte BlueConic pour accéder aux plugins. |
| Clé d’API REST Braze | Une clé API REST de Braze avec des autorisations `users.track`, `users.export.segment`, `campaigns.list`, `campaigns.details`, `segments.lists` et `segments.details`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance][2]. |
| Authentification S3 | Vous aurez besoin d’accéder à un serveur Amazon Web Services (S3) pour exporter et importer des données. |
| ID de la clé d'accès<br>Clé d'accès secrète | L’ID de clé d’accès et la clé d’accès secrète vous permettent d’authentifier votre serveur S3 pour importe et exporter des données. |
| Compartiment AWS | Vous devrez vous connecter à S3 dans le plug-in. Après authentification, les compartiments disponibles s’afficheront dans un menu déroulant. C’est là que les fichiers à importer ou exporter sont stockés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Intégration

### Étape 1 : Créer une connexion Braze

Dans BlueConic, sélectionnez **Connections (Connexions)** dans la barre de navigation, puis cliquez sur **Add Connection (Ajouter une connexion)**. Dans l’invite qui apparaît, recherchez **Braze** et sélectionnez **Braze connection (Connexion Braze)**. 

Développez ou réduisez les champs de métadonnées disponibles dans la connexion en cliquant sur l’icône en forme de chevron gris. Dans ces champs, vous pouvez désigner cette connexion comme favori, nommer votre connexion, ajouter des étiquettes, inclure une description et choisir de recevoir des notifications par e-mail selon que la connexion [fonctionne ou échoue][5]. 

Enregistrez vos paramètres.

### Étape 2 : Configurer une connexion Braze

Pour configurer la connexion entre BlueConic et Braze, vous devez renseigner les identifiants de votre compte Braze et les informations de votre compte Amazon Web Services (S3) pour authentifier la connexion. 

1. Dans BlueConic, sélectionnez **Set up and run (Configurer et exécuter)** dans la section **Setup (Configuration)** du panneau gauche.<br><br>
2. Sur la page d’authentification Braze qui s’ouvre, saisissez votre endpoint d’API REST de Braze et la clé API Braze.<br>
![]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. Dans la section S3 Setup and Authentication (Configuration et authentification S3), saisissez l’ID de clé d’accès Amazon Web Services (S3), la clé d’accès secrète et le compartiment S3. Enregistrez vos paramètres. <br>![]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}

### Étape 3 : Créer des objectifs d’importation ou d’exportation (mappage d’importation)

Une fois l’authentification terminée, vous devez créer au moins un objectif d’importation ou d’exportation, activer la connexion et planifier ou lancer la connexion.

{% tabs %}
{% tab Import %}

1. Sélectionnez **Import data into BlueConic (Importer des données dans BlueConic)** dans le panneau de gauche pour ouvrir la page de configuration des données Braze.<br><br>
2. Sélectionnez l’emplacement des données dans Braze. Ici, vous pouvez indiquer à BlueConic où trouver les données à importer en sélectionnant votre audience Braze.<br>![L’audience BlueConic Braze est définie comme « BlueConic Test Users (Utilisateurs tests BlueConic) ».]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. Ensuite, mappez les identifiants entre Braze et BlueConic. <br>![Le champ Braze « External ID (ID externe) » configuré pour le mapper au champ BlueConic « Braze external ID (ID externe Braze) ».]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> Pour lier les données client entre les deux systèmes, saisissez un ou plusieurs identifiants client.<br>Cochez la case **Allow creation… (Autoriser la création…)** pour permettre à BlueConic de créer de nouveaux profils pour les données qui ne correspondent pas à un profil BlueConic existant.<br><br>
4. Ensuite, associez les champs de données BlueConic que vous exportez à des champs Braze. Utilisez les champs déroulants pour sélectionner l’identifiant de profil BlueConic ou une propriété de profil à gauche, puis sélectionnez l’identifiant de profil Braze correspondant. Ensuite, utilisez le menu déroulant pour indiquer comment le contenu importé doit être ajouté aux valeurs existantes : ajouté, additionné, défini uniquement si la propriété du profil est vide ou défini pour être effacé (si le champ Braze est vide).<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>Cliquez sur le bouton **Add Mapping (Ajouter un mappage)** pour créer des lignes de mappage supplémentaires si nécessaire. Vous pouvez ajouter plusieurs lignes de mappage avec l’option **Add remaining fields (Ajouter les champs restants)**. BlueConic détecte les champs de Braze restants et les associe aux propriétés du profil BlueConic. Vous pouvez définir la stratégie de fusion pour les importations (définir, ajouter, additionner, définir si vide ou effacer) et fournir un préfixe personnalisé aux noms des propriétés de profil BlueConic.<br><br>
5. Enfin, cliquez sur **Run the connection (Exécuter la connexion)** pour démarrer la connexion. Rendez-vous sur le site Web de [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) pour en savoir plus sur la façon de programmer et d’exécuter des connexions.
{% endtab %}
{% tab Export %}

1. Sélectionnez **Export data to Braze (Exporter les données vers Braze)** dans le panneau de gauche pour configurer les données que vous exportez de BlueConic vers Braze.<br><br>
2. Choisissez un segment BlueConic pour l’exportation. Seuls les profils de ce segment qui comportent des identifiants correspondants dans Braze seront exportés.<br>![Un segment BlueConic contenant 20 000 profils.]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. Ensuite, reliez les identifiants entre les profils BlueConic et les champs Braze. Vous pouvez choisir de laisser BlueConic créer de nouveaux enregistrements si aucune correspondance n’est trouvée.<br>![Le champ Braze « External ID (ID externe) » configuré pour le mapper au champ BlueConic « Braze external ID (ID externe Braze) ».]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. Ensuite, associez les champs de données BlueConic que vous exportez à des champs Braze. Utilisez le menu déroulant de l’icône BlueConic pour choisir le type d’[informations](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals) que vous voulez exporter. Les informations disponibles comprennent les propriétés des profils, les identifiants de profil BlueConic, les segments associés, toutes les interactions affichées, les niveaux d’autorisation et une valeur de texte statique.<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. Enfin, cliquez sur **Run the connection (Exécuter la connexion)** pour démarrer la connexion. Rendez-vous sur le site Web de [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) pour en savoir plus sur la façon de programmer et d’exécuter des connexions.
{% endtab %}
{% endtabs %}

## Étape 4 : Activer la connexion

Utilisez le bouton bascule à côté du titre de la connexion Braze pour activer ou désactiver la connexion. Une connexion doit être activée pendant les heures programmées. 

[1]: https://www.blueconic.com/
[2]: https://portal.aws.amazon.com/billing/signup#/start
[3]: https://console.aws.amazon.com/iam/home?#security_credential
[4]: https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles
[5]: https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ