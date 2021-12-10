---
nav_title: Nexla
article_title: Nexla
page_order: 1
description: "Les courants de Braze et Nexla rendent les données accessibles dans l'ensemble de votre écosystème à l'entrepôt de données de votre choix."
alias: /partners/nexla/
page_type: partenaire
search_tag: Partenaire
---

# Nexla

> [Nexla](https://www.nexla.com) est le leader des opérations de données unifiées et un vendeur de Gartner Cool 2021. La plateforme Nexla facilite la création de flux de données évolutifs. Les équipes travaillant avec les données obtiennent une expérience unifiée de code non ou de code bas pour intégrer, transformer, fournir et surveiller les données pour tout cas d'utilisation. Nexla réduit l'expertise technique nécessaire pour comprendre et utiliser les données. Il procure une friction zéro, des opérations de données régies, une meilleure collaboration et une agilité pour les équipes d’affaires et de données.

Les clients qui utilisent [courants]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/) pour envoyer des données à des entrepôts de données peuvent tirer parti de Nexla pour extraire, transformez et chargez ces données dans d'autres endroits, ce qui rend les données facilement accessibles dans l'ensemble de votre écosystème. Nexla vous permet d'utiliser les courants de Braze pour obtenir des données dans un format personnalisé livré à votre destination de choix en un simple point et en un clic.

## Pré-requis

| Exigences                       | Origine | Accès                                                                                                                                                                                                        | Libellé                                                                                                     |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| Clé API Braze                   | Brasero | Vous devrez créer une nouvelle clé d'API.<br><br>Ceci peut être créé dans la __Console Développeur -> Paramètres API -> Créer une nouvelle clé API__ avec __utilisateurs. permissions__ de rack. | Enregistrez cette clé API pour entrer dans Nexla dans le cadre de vos identifiants Braze.                   |
| Point de terminaison REST Braze | Brasero | [Liste des points d'extrémité REST Braze][1]                                                                                                                                                                 | Enregistrez votre point de terminaison REST pour entrer dans Nexla dans le cadre de vos identifiants Braze. |
| Compte Nexla                    | Nexla   | [Commencez votre essai gratuit][2]                                                                                                                                                                           | L'accès à la plateforme Nexla et à un compte Nexla sont nécessaires pour utiliser les connecteurs Braze.    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Intégrer à Braze est simple sur Nexla. Une fois que vous avez créé un compte et que vous vous êtes connecté à la plateforme, les connecteurs de Braze sont prêts à être mis en production. Il vous suffit de sélectionner le connecteur, d'ajouter vos identifiants Braze et de commencer immédiatement à intégrer, à préparer et à surveiller vos données sous n'importe quel format.

### Étape 1 : Créer un compte Nexla

Si vous n'avez pas encore de compte Nexla, rendez-vous sur le site web [Nexla](https://www.nexla.com) pour demander une démo et un essai gratuits. Ensuite, connectez-vous à [www.dataops.nexla.io](https://www.dataops.nexla.io) et connectez-vous avec vos nouveaux identifiants.

### Étape 2 : Ajouter votre source

#### Si Braze est votre source de données:
1. Naviguez vers __Flux > Créer un nouveau flux__ sur la barre d'outils de gauche.
2. Cliquez sur __Créer une nouvelle source__, et sélectionnez le connecteur Braze.
3. Cliquez sur __Suivant__, puis __Ajouter un nouvel identifiant__.
4. Nommez les identifiants, et ajoutez votre clé API Braze et votre point de terminaison REST, et cliquez sur __Enregistrer__.
5. Ensuite, sélectionnez vos données et cliquez sur __Enregistrer__. Nexla va maintenant chercher dans la source toutes les données qu'elle trouve et générer un [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) pour la transformation ou l'envoi à la destination.

#### Si Braze est votre destination
Visitez la documentation Nexla sur [la connexion des sources à Nexla](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source).

### Étape 3 : Transformer (optionnel)

Si vous voulez effectuer des [transformations personnalisées](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations) sur vos données ou utiliser les connecteurs précompilés de Nexla, cliquez sur le bouton __Transformer__ sur le jeu de données pour entrer dans le constructeur de transformations.

### Étape 4 : Envoyer à destination

Similaire à l'ajout d'une source, cliquez sur la flèche __Envoyer à destination__ sur le jeu de données, et sélectionnez l'un des connecteurs de destination de Nexla ou Braze si vous aviez une source différente. Entrez vos identifiants, configurez les options de destination et cliquez sur __Enregistrer__. Les données commencent instantanément à couler dans le format que vous avez spécifié à la destination de votre choix.

## Utiliser cette intégration

Une fois le flux installé, rien de plus n'est nécessaire. Nexla gérera toutes les modifications apportées aux données sources et vous informera de toute modification ou erreur de triage. Si vous souhaitez apporter des modifications aux transformations, à la source ou à la destination, vous pouvez cliquer et faire le changement, et Nexla mettra à jour le flux instantanément.

## Cas d'utilisation

Les données de Nexla comme un produit, [Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information), facilitent le travail avec des données de n'importe quel format sans se soucier des métadonnées. Lorsque vous configurez vos flux de données vers ou depuis Braze avec Nexla, les outils sans code le rendent facile et disponible en quelques minutes. Une fois que le flux de données est défini sur une destination, Nexla surveillera votre flux et votre échelle à n'importe quelle quantité de données. Notre plateforme facilite la création de flux de données évolutifs. Les équipes travaillant avec les données obtiennent une expérience unifiée de code non ou de code bas pour intégrer, transformer, fournir et surveiller les données pour tout cas d'utilisation.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: https://www.nexla.com/get-demo
