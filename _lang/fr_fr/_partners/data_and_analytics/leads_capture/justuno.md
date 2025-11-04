---
nav_title: Justuno
article_title: Justuno
description: "Découvrez comment intégrer Justuno à Braze afin d'exploiter les données personnalisées des clients sur les deux plateformes pour créer des expériences plus personnalisées pour toutes les audiences."

alias: /partners/justuno
page_type: partner
search_tag: Partner
---

# Justuno

> [Justuno](https://www.justuno.com/) vous permet de créer des expériences visiteurs entièrement optimisées pour toutes vos audiences avec des segments dynamiques, offrant le ciblage le plus avancé disponible - le tout sans impacter la vitesse du site ou augmenter le travail de développement. Analysez les taux de conversion en consultant des analyses/analytiques personnalisées telles que le nombre de profils créés, le taux de retour des visiteurs influencés et les pages par session afin de conserver un avantage marketing dans votre secteur. Justuno vous permet d'augmenter le chiffre d'affaires par visiteur, d'établir des engagements clients significatifs et de développer votre activité. Optimisez le parcours de l'audience de bout en bout avec une plateforme connectée.

## Cas d’utilisation

Braze permet à tout marketeur de collecter et d'agir sur n'importe quelle quantité de données provenant de n'importe quelle source, afin que vous puissiez engager de manière créative avec les clients en temps réel, sur tous les canaux, à partir d'une seule plateforme.

L'intégration de Justuno et de Braze vous offre le meilleur des deux mondes. Vous pouvez combiner les données clients enregistrées dans Braze avec les données visiteurs et clients enregistrées dans Justuno et créer des expériences plus personnalisées pour toutes les audiences. Vous augmentez ainsi l'efficacité de vos campagnes marketing et de vos engagements clients.

## Conditions préalables

| Une clé API REST de Braze avec les autorisations `users.track` et `custom_attributes.get`.<br><br>Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Point d'accès REST de Braze | URL de votre point d'accès REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration de Justuno à Braze

### Étape 1 : Créer des attributs personnalisés dans Braze

Pour synchroniser les attributs des utilisateurs de Justuno vers Braze, vous devrez créer ces attributs dans Braze si ce n'est pas déjà fait. Vous pouvez le faire en allant dans **Paramètres des données** > **Attributs personnalisés**, puis en créant vos attributs personnalisés. Pour une présentation complète, voir [Gérer les attributs personnalisés dans Braze]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/).

### Étape 2 : Ajouter l'application Braze à Justuno

#### Étape 2.1 : Ajoutez-le à votre compte

Pour ajouter l'appli Braze à votre compte Justuno, allez dans **Paramètres du compte** > **Apps**, puis recherchez et sélectionnez l'appli Braze.

![La page "Connect Apps" de Justuno avec l'application Braze dans la liste des résultats de recherche.]({% image_buster /assets/img/justuno/search-for-braze.png %})

Saisissez la clé API et l'URL de base [que vous avez créées précédemment](#prerequisites), puis sélectionnez **Connecter**.

![La fenêtre contextuelle d'authentification de Braze demandant une clé API de Braze et une URL de base.]({% image_buster /assets/img/justuno/authenticate-braze.png %}){: style="max-width:75%;"}

#### Étape 2.2 : Ajoutez-le à votre flux de travail

Pour ajouter l'application Braze à votre [flux de travail Justuno](https://hub.justuno.com/knowledge/workflows-overview), glissez-déposez l'action **Sync to App** dans votre flux de travail, puis choisissez **Select App** > **Braze**.

![L'option "Select App" est située sur l'action "Sync to App".]({% image_buster /assets/img/justuno/select-app.png %}){: style="max-width:45%;"}

### Étape 3 : Connectez vos groupes d'abonnement Braze

Pour envoyer des données de profil depuis Justuno vers un e-mail ou un groupe d'abonnement SMS spécifique de Braze, vous devez ajouter leur ID à l'application Braze dans votre flux de travail Justuno.

| Type d'ID                          | Requis ? | Description                                                                                                   |
|----------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| ID du groupe d'abonnement SMS de Braze  | Oui       | Cet ID est utilisé pour recueillir le consentement à l'envoi de SMS à partir des profils utilisateurs. Si aucun ID n'est saisi dans Justuno, les profils n'auront pas de consentement lorsque Justuno transmettra ce profil à Braze. |
| ID du groupe d'abonnement e-mail de Braze | Non        | Si cet ID n'est pas saisi dans Justuno, Justuno enverra les données du profil à Braze en tant qu'utilisateur sans groupe d'abonnement associé. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Étape 3.1 : Emplacement/localisation des ID dans Braze

Pour localiser ces ID dans le tableau de bord de Braze :

1. Allez dans **Audience** > **Abonnements**.
2. Pour chaque groupe d'abonnement, notez l'emplacement/localisation de l'ID dans la colonne ID.

#### Étape 3.2 : Ajouter les ID à l'application Braze

Dans votre flux de travail Justuno, ouvrez l'appli Braze, puis introduisez les ID de chaque groupe d'applications.

![L'application Braze s'est ouverte dans un flux de travail Justuno avec la possibilité d'ajouter des groupes d'abonnement ID e-mail et SMS.]({% image_buster /assets/img/justuno/enter-subscription-groups.png %}){: style="max-width:55%;"}

### Étape 4 : Configurez vos attributs

Les attributs suivants sont automatiquement synchronisés entre Justuno et Braze :

- E-mail  
- Téléphone  
- Prénom  
- Nom  
- Langue  
- Genre  
- Pays

Pour synchroniser des attributs supplémentaires :

1. Dans l'application Braze au sein de votre flux de travail, sélectionnez **Synchroniser une autre propriété.**
    ![L'application Braze s'est ouverte dans un flux de travail Justuno et montre l'option "Synchroniser un autre bien".]({% image_buster /assets/img/justuno/sync-another-property.png %}){: style="max-width:55%;"}
2. Choisissez les attributs de Braze que vous souhaitez synchroniser.
3. Faites correspondre les propriétés dans Justuno avec leurs équivalents dans Braze (tels que les poignées sociales, l'anniversaire, les préférences d'achat, les réponses aux enquêtes, et similaires). Gardez à l'esprit que ces propriétés sont considérées comme des données 0 party ou 1st party. Pour en savoir plus, consultez le site [Justuno : Collecte de données sur les visiteurs](https://www.justuno.com/guides/zero-first-party-data/).
4. Dans le générateur de flux de travail, choisissez d'**enregistrer**, de **prévisualiser** ou de **publier** votre flux de travail.
    ![Le menu "Publier" s'est ouvert avec des options permettant d'enregistrer, de prévisualiser ou d'afficher l'historique des versions.]({% image_buster /assets/img/justuno/publish-workflow.png %}){: style="max-width:45%;"}

## Choses à savoir

- Vous devez saisir manuellement l'ID du groupe d'abonnements dans les paramètres de l'app.  
- Les types de données suivants de Braze ne sont **pas pris en charge** : Objet, tableau d'objets.  
- Le consentement implicite par SMS est fourni lorsque le champ de consentement par SMS de Justuno n'est pas utilisé.  
- Le consentement explicite par SMS est respecté si le design Justuno inclut le champ de consentement.
