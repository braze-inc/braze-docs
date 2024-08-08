---
nav_title: Configuration de Currents
article_title: Configuration de Currents
page_order: 0
page_type: tutorial
description: "Cet article pratique vous guide dans le processus d’intégration et de configuration des currents Braze."
tool: Currents
search_rank: 8
---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"}Configuration de Currents

> Cette page décrit et décrit le processus générique d’intégration et de configuration des currents Braze.

{% alert important %}
Currents est inclus dans certaines offres Braze. Contactez votre représentant Braze si vous avez des questions ou souhaitez y accéder.
{% endalert %}

## Conditions

L’utilisation de Currents avec l’un de nos partenaires nécessite les mêmes paramètres de base et méthodologie de connexion.

Chaque partenaire exige que Braze ait l’autorisation de lui écrire et de lui envoyer des fichiers de données, et Braze demande l’emplacement où elle doit écrire ces fichiers, en particulier les noms ou les clés des compartiments.

Les conditions suivantes sont les exigences élémentaires et minimales pour s’intégrer avec la plupart de nos partenaires. Certains partenaires nécessitent des paramètres supplémentaires, qui sont indiqués dans leurs [documentations respectives ]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/)ainsi que les nuances associées à ces exigences de base.

| Condition | Origine | Accès | Description
|---|---|---|---|
| Compte chez le partenaire | Créez un compte chez ce partenaire ou contactez votre gestionnaire de compte Braze pour obtenir des suggestions. | Consultez le site du partenaire ou contactez ce partenaire pour vous inscrire. | Braze n’enverra pas de données à un partenaire si vous n’avez pas accès à ces données via le compte de votre société.
| Clé ou Jeton (token) de l’API du partenaire | Généralement le tableau de bord du partenaire. | Copiez-le et collez-le dans le champ Braze désigné. | Braze a un champ désigné pour cela dans la page Intégrations pour ce partenaire. Nous en avons besoin pour mapper où nous envoyons vos données. **Il est important de tenir à jour vos clés/jetons partenaires ; les informations d’identification non valides peuvent entraîner la désactivation de votre connecteur et la suppression des événements.**
| Code/Clé d’authentification, Clé secrète, Fichier de certification | Contactez un représentant de votre compte chez ce partenaire. Elles sont parfois présentes sur le tableau de bord du partenaire. | Copiez et collez les clés dans le champ Braze désigné. Générez et chargez `.json`ou d’autres fichiers de certification dans l’emplacement approprié de Braze. | Braze a un champ désigné pour cela dans la page Intégrations pour ce partenaire. Cela fournit des identifiants à Braze et nous autorise à écrire des fichiers sur le compte du Partenaire. **Il est important de tenir à jour vos clés/jetons partenaires ; les informations d’identification non valides peuvent entraîner la désactivation de votre connecteur et la suppression des événements.**
| Compartiment, chemin de dossier | Certains partenaires organisent et trient des données par compartiments. Vous devriez le voir dans le tableau de bord du partenaire. | Si nécessaire, assurez-vous de copier exactement le nom ou le chemin du compartiment dans l’espace désigné à Braze. Nous ne voulons pas que vos données soient perdues ! | Certains partenaires l’exigent, et c’est important de ne pas se tromper si vous le faites. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert important %}
Il est important de garder les identifiants et les clés/jetons de votre partenaire à jour ; si les identifiants de votre connecteur expirent, le connecteur cessera d’envoyer des événements. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront perdues définitivement.
{% endalert %}


## Étape 1 : Choisissez votre partenaire

Les currents Braze vous permettent d’intégrer via Data Storage à l’aide de fichiers plats, ou avec nos partenaires Behavioral Analytics et Customer Data, en utilisant des payloads JSON en batch pour un endpoint désigné.  

Avant de commencer votre intégration, il est préférable de décider quelle intégration vous convient le mieux. Par exemple, si vous utilisez déjà mParticle et Segment.io et que vous souhaitez y envoyer les données de Braze, il vaut mieux utiliser un payload JSON en batch. Si vous préférez manipuler les données vous-même ou si vous avez un système d’analyse des données plus complexe, il est préférable d’utiliser Data Storage données ([c’est la méthode utilisée par Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/) !)

## Étape 2 : Accéder à Currents

Pour commencer, consultez la page Currents sur la barre latérale, dans la section « Intégrations » du tableau de bord. Vous serez dirigé vers la page de gestion des Intégrations Currents.

![Page Currents sur le tableau de bord de Braze]({% image_buster /assets/img_archive/currents-main-page.png %})

## Étape 3 : Ajouter un partenaire

Ajoutez un partenaire, parfois appelé « Connecteur Currents », en cliquant sur le menu déroulant en haut de l’écran.

![Ajouter une intégration]({% image_buster /assets/img/new_current.png %}){: style="max-width:30%;"}

Les étapes de configuration varient selon les partenaires. Pour activer chaque intégration, consultez notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) et suivez les instructions indiquées sur leurs pages respectives.

## Étape 4 : Configurer les événements

Choisissez les événements que vous souhaitez transmettre à ce partenaire en cochant les options disponibles. Vous pouvez trouver des listes de ces événements dans nos bibliothèques [Événements de comportement client]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) et [Événements d’engagement sur les messages]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/).

Si nécessaire, vous pouvez en savoir plus sur nos événements dans notre article sur la [Sémantique des événements de livraison]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_delivery_semantics/).

## Étape 5 : Tester votre intégration

Vous pouvez tester votre intégration ou examiner les échantillons de données Currents dans notre [Référentiel GitHub](https://github.com/Appboy/currents-examples) d’exemple Currents.

{% alert important %}
De plus, notez que Currents ignorera les événements avec des charges utiles excessivement importantes de plus de 900 Ko. 
{% endalert %}
