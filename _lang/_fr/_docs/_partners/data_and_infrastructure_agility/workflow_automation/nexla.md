---
nav_title: Nexla
article_title: Nexla
page_order: 1
description: "Cet article décrit le partenariat entre Braze et Nexla, une plateforme unifiée d'opérations de données qui permet aux utilisateurs de Braze Currents d'extraire, transformer, et charger les données des lacs de données vers d'autres emplacements dans un format personnalisé."
alias: /partners/nexla/
page_type: partenaire
search_tag: Partenaire
---

# Nexla

> [Nexla](https://www.nexla.com) est un leader dans les opérations de données unifiées et un vendeur Gartner Cool 2021. La plateforme Nexla permet à tout le monde de créer des flux de données évolutifs, en produisant des frottements nuls, a régi les opérations de données, une meilleure collaboration et une agilité pour les équipes d’entreprises et de données. Les équipes travaillant avec les données obtiennent une expérience unifiée de code non ou de code bas pour intégrer, transformer, fournir et surveiller les données pour tout cas d'utilisation.

L'intégration de Braze et Nexla permet aux clients qui utilisent des [courants]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/) pour tirer parti de Nexla pour extraire, transformer, transformer, et charger les données des lacs vers d'autres endroits dans un format personnalisé, ce qui rend les données facilement accessibles dans tout votre écosystème.

## Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                      |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Compte Nexla                    | Un [compte Nexla][2] est requis pour profiter de ce partenariat.                                                                                                                                             |
| Braze clé API REST              | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le **tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API** |
| Point de terminaison REST Braze | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance][1].                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d'utilisation

Les données de Nexla comme un produit, [Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information), facilitent le travail avec des données de n'importe quel format sans se soucier des métadonnées. Lorsque vous configurez vos flux de données vers ou depuis Braze avec Nexla, les outils sans code le rendent facile et disponible en quelques minutes. Une fois que le flux de données est défini sur une destination, Nexla surveillera votre flux et votre échelle à n'importe quelle quantité de données.

## Intégration

### Étape 1 : Créer un compte Nexla

Si vous n'avez pas encore de compte Nexla, rendez-vous sur le site web [Nexla](https://www.nexla.com) pour demander une démo et un essai gratuits. Ensuite, connectez-vous à [www.dataops.nexla.io](https://www.dataops.nexla.io) et connectez-vous avec vos nouveaux identifiants.

### Étape 2 : Ajouter votre source

#### Si Braze est votre source de données
1. Dans la plate-forme Nexla, naviguez vers **Flux > Créer un nouveau flux** dans la barre d'outils de gauche.
2. Cliquez sur **Créer une nouvelle source**, sélectionnez le connecteur Braze, puis cliquez sur **Suivant**.
3. Sélectionnez **Ajouter un nouvel identifiant**, nommez l'identifiant, ajoutez votre clé API Braze et votre point de terminaison REST, et **Enregistrer**.
4. Enfin, sélectionnez vos données et cliquez sur **Enregistrer**.

Nexla va maintenant chercher dans la source toutes les données qu'elle trouve et générer un [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) pour la transformation ou l'envoi à la destination.

#### Si Braze est votre destination

Visitez la documentation Nexla sur [la connexion des sources à Nexla](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source).

### Étape 3 : Transformer (optionnel)

Si vous voulez effectuer des [transformations personnalisées](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations) sur vos données ou utiliser les connecteurs précompilés de Nexla, cliquez sur le bouton **Transformer** sur le jeu de données pour entrer dans le constructeur de transformations. Les directives sur l'utilisation du constructeur de transformation se trouvent dans la documentation de [Nexla](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data).

### Étape 4 : Envoyer à destination

Pour envoyer des données à une destination, cliquez sur la flèche **Envoyer à destination** sur le jeu de données, et sélectionnez l'un des connecteurs de destination de Nexla ou Braze si vous aviez une source différente. Entrez vos identifiants, configurez les options de destination et cliquez sur **Enregistrer**. Les données commencent instantanément à couler dans le format que vous avez spécifié à la destination de votre choix.

## Utiliser cette intégration

Une fois le flux installé, rien de plus n'est nécessaire. Nexla gérera tous les changements dans les données source, redimensionnera toutes les nouvelles données, et vous informera de toute modification de schéma ou d'erreurs pour le triage. Si vous souhaitez apporter des modifications aux transformations, à la source ou à la destination, vous pouvez cliquer dans ces options et faire le changement, et Nexla mettra à jour le flux instantanément.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: https://www.nexla.com/get-demo