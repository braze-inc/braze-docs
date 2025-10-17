---
nav_title: Jacquard
article_title: Jacquard
alias: /partners/jacquard/
page_order: 1
description: "Cet article de référence présente le partenariat entre Braze et Jacquard Dynamic Optimisation qui s'appuie sur Braze Currents et Connected Content pour collecter les informations de suivi des clics de vos abonnés par le biais de webhooks. Jacquard relie ensuite ces événements à vos variantes linguistiques pour une optimisation linguistique en temps réel."
page_type: partner
search_tag: Partner
---

# Optimisation dynamique du jacquard

> [Jacquard](https://www.jacquard.com/) réunit l'intelligence artificielle, la linguistique informatique et un esprit centré sur le client pour aider à déployer le langage de la marque à grande échelle, sur des canaux personnalisés aux couleurs de votre marque.

L'optimisation dynamique, alimentée par Jacquard X, s'appuie sur Braze Currents et Connected Content pour collecter des informations de suivi des clics auprès de vos abonnés par le biais de webhooks. Jacquard relie ensuite ces événements à vos variantes linguistiques pour une optimisation linguistique en temps réel. 

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Jacquard | Un [compte Jacquard](https://www.jacquard.com/) est nécessaire pour bénéficier de ce partenariat. |
| Jeton du serveur de connexion Jacquard | Une longue chaîne de caractères qui servira de mot de passe à votre campagne Braze pour accéder à votre langage Jacquard.<br><br>Vous pouvez en faire la requête auprès de votre gestionnaire de la satisfaction client Jacquard si vous ne l'avez pas encore reçu. |
| Currents | Pour pouvoir exporter des données vers Currents, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Demander les identifiants Amazon S3 de Jacquard

Vous aurez besoin de Jacquard pour configurer un compartiment Amazon S3 dédié afin de recevoir vos événements de suivi des clics de Braze. Contactez votre gestionnaire de la satisfaction client Jacquard pour démarrer ce processus. Lorsque le compartiment est créé, vous recevrez des identifiants uniques pour créer votre flux Currents. 

### Étape 2 : Créer un flux Currents

1. Dans Braze, sélectionnez **Currents > Créer un nouveau flux Currents > Exporter des données Amazon S3.** 
2. Ensuite, nommez votre flux Currents et entrez un e-mail de contact.
3. Ajoutez votre ID de clé d'accès Jacquard AWS et votre clé d'accès secrète dans la section des informations d'identification. Ensuite, ajoutez "Exports Phrasee-Braze-Currents" comme nom de compartiment S3 AWS. 
4. Enfin, ajoutez le dossier du compartiment AWS S3 que vous avez reçu de votre gestionnaire de satisfaction client Jacquard. Il s'agira probablement du nom de votre entreprise.
5. Sous **Paramètres généraux**, cochez la case "Inclure les événements des utilisateurs anonymes", et sous **Gérer les événements d'engagement**, cochez "Cliquer sur l'e-mail".
6. Lorsque vous avez terminé, sélectionnez **Lancer le flux Currents**.

### Étape 3 : requête de suppression d'informations personnellement identifiables (IPI).

Ensuite, contactez l'équipe de votre compte Braze pour vous assurer qu'aucune information personnelle identifiable n'est transmise à Jacquard.

Par défaut, le flux Currents inclura certains attributs par défaut comme l'e-mail et l'adresse. Jacquard ne peut pas recevoir et ne recevra pas d'IIP, il est donc essentiel que vous demandiez à l'équipe de votre compte Braze de désactiver cette fonction pour toutes les données d'événements transmises à Jacquard.

### Étape 4 : Extraits de code Jacquard X 

Contactez l'équipe de votre compte Jacquard pour obtenir les extraits de code nécessaires.

Ces extraits tirent parti du [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) et, une fois placés dans vos e-mails, ils intègrent de manière dynamique la langue et un pixel de suivi afin que Jacquard puisse optimiser votre langue en temps réel à l'aide de Jacquard X.


