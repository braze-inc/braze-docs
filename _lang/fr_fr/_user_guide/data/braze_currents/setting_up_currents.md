---
nav_title: Configuration de Currents
article_title: Configuration de Currents
page_order: 0
page_type: tutorial
description: "Cet article pratique vous guide dans le processus d’intégration et de configuration de Braze Currents."
tool: Currents
search_rank: 8
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"}Configuration de Currents

> Cette page décrit et décrit le processus générique d’intégration et de configuration de Braze Currents.

{% alert important %}
Currents est inclus dans certaines offres Braze. Contactez votre représentant Braze si vous avez des questions ou souhaitez y accéder.
{% endalert %}

## Conditions

L’utilisation de Currents avec l’un de nos partenaires nécessite les mêmes paramètres de base et méthodologie de connexion.

Chaque partenaire exige que Braze ait l’autorisation de lui écrire et de lui envoyer des fichiers de données, et Braze demande l’emplacement où elle doit écrire ces fichiers, en particulier les noms ou les clés des compartiments.

Les conditions suivantes sont les exigences élémentaires et minimales pour s’intégrer avec la plupart de nos partenaires. Certains partenaires exigeront des paramètres supplémentaires, qui sont énumérés dans la [documentation de leur partenaire]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) respectif, ainsi que toutes les nuances associées à ces exigences de base.

| Condition | Origine | Accès | Description
|---|---|---|---|
| Compte chez le partenaire | Créez un compte chez ce partenaire ou contactez votre gestionnaire de compte Braze pour obtenir des suggestions. | Consultez le site du partenaire ou contactez ce partenaire pour vous inscrire. | Braze n’enverra pas de données à un partenaire si vous n’avez pas accès à ces données via le compte de votre société.
| Clé ou Jeton (token) de l’API du partenaire | Généralement le tableau de bord du partenaire. | Copiez-le et collez-le dans le champ Braze désigné. | Braze a un champ désigné pour cela dans la page Intégrations pour ce partenaire. Nous en avons besoin pour mapper où nous envoyons vos données. **Il est important que vos clés/jetons de partenaires soient à jour ; des identifiants non valides peuvent entraîner la désactivation de votre connecteur et l'abandon d'événements.**
| Code/Clé d’authentification, Clé secrète, Fichier de certification | Contactez un représentant de votre compte chez ce partenaire. Elles sont parfois présentes sur le tableau de bord du partenaire. | Copiez et collez les clés dans le champ Braze désigné. Générez et chargez `.json`ou d’autres fichiers de certification dans l’emplacement approprié de Braze. | Braze a un champ désigné pour cela dans la page Intégrations pour ce partenaire. Cela fournit des identifiants à Braze et nous autorise à écrire des fichiers sur le compte du Partenaire. **Il est important que vos informations d'authentification soient à jour ; des identifiants non valides peuvent entraîner la désactivation de votre connecteur et l'abandon d'événements.**
| Compartiment, chemin de dossier | Certains partenaires organisent et trient des données par compartiments. Vous devriez le voir dans le tableau de bord du partenaire. | Si nécessaire, assurez-vous de copier exactement le nom ou le chemin du compartiment dans l’espace désigné à Braze. Nous ne voulons pas que vos données soient perdues ! | Certains partenaires l’exigent, et c’est important de ne pas se tromper si vous le faites. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Il est important de garder les identifiants et les clés/jetons de votre partenaire à jour ; si les identifiants de votre connecteur expirent, le connecteur cessera d’envoyer des événements. Si cette situation persiste pendant plus de **48 heures**, les événements du connecteur seront abandonnés et les données seront définitivement perdues.
{% endalert %}

## Configuration de Currents

### Étape 1 : Choisissez votre partenaire

Braze Currents vous permet d’intégrer via Data Storage à l’aide de fichiers plats, ou avec nos partenaires Behavioral Analytics et Customer Data, en utilisant des payloads JSON en batch pour un endpoint désigné.  

Avant de commencer votre intégration, il est préférable de décider quelle intégration vous convient le mieux. Par exemple, si vous utilisez déjà mParticle et Segment et que vous souhaitez y envoyer les données de Braze, il vaut mieux utiliser un payload JSON en batch. Si vous préférez manipuler les données par vous-même ou si vous disposez d'un système d'analyse des données plus complexe, il est préférable d'utiliser le stockage des données ([Braze utilise cette méthode]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/) !).

### Étape 2 : Flux Currents ouverts

Pour commencer, sélectionnez **Intégrations partenaires** > **Exportation de données**. Vous serez dirigé vers la page de gestion des Intégrations Currents.

![Page actuelle du tableau de bord de Braze]({% image_buster /assets/img_archive/currents-main-page.png %})

### Étape 3 : Ajoutez votre partenaire

Ajoutez un partenaire, parfois appelé "connecteur actuel", en sélectionnant le menu déroulant en haut de l'écran.

Les étapes de configuration varient selon les partenaires. Pour activer chaque intégration, consultez notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) et suivez les instructions de leurs pages respectives.

### Étape 4 : Configurez vos événements

Choisissez les événements que vous souhaitez transmettre à ce partenaire en cochant les options disponibles. Vous trouverez la liste de ces événements dans nos bibliothèques [Événements de comportement client]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) et [Événements d’engagement liés aux messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

![]({% image_buster /assets/img/current4.png %})

Si nécessaire, vous pouvez en savoir plus sur nos événements dans notre article sur [la sémantique de réception/distribution des événements]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/).

### Étape 5 : Mise en place des transformations de champ

Vous pouvez utiliser les transformations de champs Currents pour supprimer ou hacher un champ de chaînes de caractères.

- **supprimer :** Remplace la chaîne de caractères par `[REDACTED]`. Ceci est utile si votre partenaire rejette les événements dont les champs sont manquants ou vides.
- **Hash :** Applique un algorithme de hachage SHA-256 à la chaîne de caractères.

La sélection d'un champ pour l'une de ces transformations appliquera cette transformation à tous les événements dans lesquels ce champ apparaît. Par exemple, si vous sélectionnez `email_address` pour le hachage, le champ `email_address` sera haché dans les champs Envoi d'e-mail, Ouverture d'e-mail, Rebond d'e-mail et Changement d'état du groupe d'abonnement.

![Ajout de transformations de champs]({% image_buster /assets/img/current3.png %})

### Étape 6 : Tester votre intégration

{% alert important %}
Currents abandonnera les événements dont la charge utile est excessivement importante (plus de 900 Ko).
{% endalert %}

Avant de tester, pensez à consulter notre [échantillon de données Currents sur GitHub](https://github.com/Appboy/currents-examples). Lorsque vous êtes prêt à tester, vous choisissez une option ci-dessous :

#### Envoi d'événements de test

Pour tester votre intégration, vous pouvez sélectionner **Envoyer des événements de test** pour envoyer un événement de chacun des types d'événements sélectionnés à ce Current. Pour obtenir des informations détaillées sur chaque type d'événement, consultez nos bibliothèques [Événements liés au comportement des clients]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) et [Événements liés à l'engagement des messages.]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) 

![La page "Currents Test" du tableau de bord de Braze.]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Test des connecteurs de courant

Les connecteurs Test Currents sont des versions gratuites de nos connecteurs existants qui peuvent être utilisées pour tester et essayer différentes destinations. Les connecteurs test Currents présentent les propriétés suivantes :

- Le nombre de connecteurs Test Currents que vous pouvez créer n'est pas limité.
- Un maximum global de 10 000 événements par période de déploiement de sept jours. Ce total d'événements est mis à jour toutes les heures sur le tableau de bord.

Lorsque vos connecteurs Test Currents atteignent la limite d'envoi, votre connecteur n'enverra plus d'événements jusqu'à la prochaine période de sept jours.

Pour mettre à niveau votre connecteur Test Currents, modifiez l'intégration dans le tableau de bord et sélectionnez **Mettre à niveau l'intégration de test**.

## Mise à jour des courants

{% multi_lang_include updating_currents.md %}

## Liste d’adresses IP autorisées

Braze enverra les données Currents à partir des adresses IP répertoriées :

{% multi_lang_include data_centers.md datacenters='ips' %}
