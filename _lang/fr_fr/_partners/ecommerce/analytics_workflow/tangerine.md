---
nav_title: Mandarine
article_title: Mandarine
description: "Cet article présente le partenariat entre Braze et Tangerine Store360, une plateforme omnicanale qui relie les magasins physiques aux boutiques en ligne afin d'offrir des expériences supérieures en magasin aux consommateurs et aux employés des magasins. Grâce à cette intégration, les données brutes de campagne et d'impression de Braze sont disponibles sur Store360 via le partage sécurisé de données Snowflake, et les marques peuvent mesurer l'impact de leurs campagnes sur l'engagement en magasin et le trafic en magasin."
alias: /partners/tangerine/
page_type: partner
search_tag: Partner

---

# Tangerine Store360

> Tangerine conçoit, crée et exploite une plateforme omnicanal appelée Store360. Store360 est une plateforme facilitatrice omnicanal connectant les magasins physiques aux boutiques en ligne afin d'améliorer l'expérience des consommateurs et des employés en magasin. Store360 suit et analyse le trafic des visites dans les magasins physiques, y compris les utilisateurs de l'application mobile des commerçants et leur engagement en magasin.

L'intégration de Braze et Tangerine vous permet d'intégrer les données brutes de campagne et d'impression de Braze dans Store360 grâce au partage sécurisé des données de Snowflake. Les marques peuvent désormais mesurer l'impact de ces campagnes sur les visites en magasin physique et l'engagement en magasin.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Store360 | Un compte Store360 est nécessaire pour profiter de ce partenariat. |
| ID du compte Braze | Votre ID de groupe d'applications Braze. |
| Mise en correspondance des ID des utilisateurs | Vos données clients dans Store360 et Braze doivent avoir des ID utilisateurs correspondants sur les deux plateformes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

### Analyser l'impact de la campagne sur la fréquentation des magasins physiques.

Les marques utilisent Braze pour envoyer des messages de campagne aux consommateurs afin d'augmenter les visites en magasin. Pendant la campagne, Store360 capture les visites des utilisateurs de l'application mobile identifiés par l'ID de l'utilisateur.

Grâce à la capacité analytique de Store360 Insight, les marques peuvent visualiser les informations relatives à l'impact de la campagne, depuis les messages envoyés et lus (données de Braze) jusqu'à qui et combien de destinataires ont visité les magasins physiques (données de Store360).

## Intégration

### Étape 1 : Activer le partage sécurisé des données par Snowflake

Collaborez avec votre équipe Braze pour activer et configurer Snowflake Secure Data Share.

### Étape 2 : Configurer Store360 pour obtenir les données de Braze

Configurez votre groupe d'applications Braze ID à votre compte de service Store360 à l'aide de la console web du gestionnaire d'administration Store360. L'équipe d'administration de Tangerine devra synchroniser les données de Braze avec Store360 en utilisant le partage de données Snowflake.

### Étape 3 : Intégrer les SDK Store360 à l'application mobile

Pour suivre et analyser les visites des utilisateurs de l'application mobile en magasin et les activités en magasin ainsi que les données de campagne et d'impression de Braze, vous devez intégrer le SDK Store360 dans votre application mobile en suivant les étapes fournies dans la documentation d'installation du SDK Store360. Cette documentation vous sera fournie après la signature d'un contrat client avec Tangerine Store 360.

## Analysez les données de Braze dans Store360

Profitez du partage de données sécurisé Snowflake pour partager vos données brutes de campagne et d'impression Braze avec les informations analytiques Store360 Insight, offrant ainsi une image complète du cycle de vie et des activités des utilisateurs, de l'online à l'offline.

Pour référence, voici tous les [champs Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df) disponibles pour être incorporés dans l'analyse/analytique Store360. Les détails de cette étape sont très spécifiques au client et nécessitent des configurations particulières. Adressez-vous à votre gestionnaire de compte Store360 ou à support@tangerine.io pour en savoir plus.

## Informations importantes et limitations

### Disponibilité du service

Actuellement, le service Store360 est disponible au Japon et en Indonésie.

Tangerine prévoit un lancement du produit Store360 dans les pays suivants en 2023.
- États-Unis d'Amérique
- Thaïlande
- Singapour
- Vietnam
- Corée

### Conservation des données

Il existe une politique de conservation de deux ans de vos données Braze pour le partage des données Snowflake.

### Délai dans la génération des données des événements Braze

Les événements Braze sont traités avec une technologie de flux continu et sont disponibles quasiment en temps réel. En général, les événements sont disponibles dans les 30 minutes qui suivent.
