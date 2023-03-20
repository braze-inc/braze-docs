---
nav_title: Phrasee React
article_title: Phrasee React
page_order: 2
description: "Cet article de référence présente le partenariat entre Braze et Phrasee React. Celui-ci tire profit de Currents Braze et du Contenu connecté pour recueillir les informations de suivi des clics de vos utilisateurs abonnés à l’aide de webhooks. Phrasee associe ensuite ces événements à vos variantes de langue pour optimiser la langue en temps réel."
page_type: partner
search_tag: Partenaire

---

# Phrasee React

> [Phrasee][1] rassemble l’intelligence artificielle, la linguistique informatique et un esprit axé sur le client pour vous aider à déployer la langue utilisée par votre marque à grande échelle sur des canaux personnalisés en fonction de votre marque.

Phrasee [React](https://phrasee.co/platform/react/), de Phrasee X, tire profit de Currents Braze et du Contenu connecté pour collecter les informations de suivi des clics de vos utilisateurs abonnés à l’aide de webhooks. Phrasee associe ensuite ces événements à vos variantes de langue pour optimiser la langue en temps réel. 

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Phrasee | Un [compte Phrasee][3] est requis pour profiter de ce partenariat. |
| Jeton de connexion au serveur Phrasee | Une longue chaîne de caractères qui vous servira à accéder à votre langue Phrasee en tant que mot de passe pour votre campagne Braze.<br><br>Si vous n’avez pas encore reçu ce jeton, vous pouvez le demander à partir du gestionnaire du succès des clients Phrasee. |
| Currents | Pour exporter des données dans Currents, vous devez avoir configuré [Currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Demander des informations d'identification S3 Amazon pour Phrasee

Vous devrez faire en sorte que Phrasee configure un compartiment Amazon S3 pour recevoir vos événements de suivi des clics à partir de Braze. Contactez votre gestionnaire du succès des clients Phrasee pour initier ce processus. Lorsque le compartiment est créé, des informations d’identification uniques vous seront fournies pour créer votre Current. 

### Étape 2 : Créer un Current

1. Dans Braze, cliquez sur **Currents > Create New Current (Créer un nouveau Current) > Amazon S3 Data Export (Exporter les données Amazon S3)**. 
2. Ensuite, donnez un nom à votre Current et saisissez une adresse e-mail de contact.
3. Ajoutez votre ID de clé d’accès AWS Phrasee et votre clé d’accès secrète dans la case d’informations d’identification. Ensuite, ajoutez « phrasee-braze-currents-exports » comme nom du compartiment AWS S3. 
4. Enfin, ajoutez le dossier du compartiment S3 AWS que vous avez reçu de la part de votre gestionnaire du succès des clients Phrasee. Il s’agira probablement du nom de votre entreprise.
5. Sous **General Settings (Paramètres généraux)**, cochez la case « Include events from anonymous users » (Inclure les événements des utilisateurs anonymes), et sous **Manage Engagement Events (Gérer les événements d’engagement)**, cochez la case « Email Click » (Clic dans l’e-mail).
6. Lorsque vous avez terminé, cliquez sur **Launch Current (Lancer le Current)**.

### Étape 3 : Demandez de supprimer les informations personnellement identifiables.

Ensuite, contactez votre équipe Braze responsable de compte pour vous assurer qu’aucune information personnellement identifiable n’est transmise à Phrasee.

Par défaut, le Current inclura certains attributs contenant des informations personnellement identifiables, comme une adresse e-mail ou une adresse postale. Phrasee ne peut pas recevoir des informations personnellement identifiables et n’en recevra pas. Par conséquent, il est critique de demander à votre équipe Braze responsable de compte de désactiver cette fonctionnalité pour toutes les données d’événements transmises à Phrasee.

### Étape 4 : Extraits de code Phrasee X 

Contactez votre équipe de compte Phrasee pour obtenir les extraits de code requis.

Ces extraits de code exploitent le [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content). Une fois collés dans vos e-mails, ils extrairont la langue, ainsi qu’un pixel de suivi pour permettre à Phrasee d’optimiser votre langue en temps réel à l’aide de Phrasee X.


[1]: https://phrasee.co/
[3]: mailto:awesome@phrasee.co