---
nav_title: Nexla
article_title: Nexla
description: "Cet article de référence décrit le partenariat entre Braze et Nexla, une plateforme unifiée d'opérations de données qui permet aux utilisateurs de Braze Currents d'extraire, de transformer et de charger des données de lacs de données vers d'autres emplacements dans un format personnalisé."
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# Nexla

> [Nexla](https://www.nexla.com) est un leader des opérations de données unifiées et figure parmi les meilleurs fournisseurs du classement Gartner 2021. La plateforme Nexla permet de créer facilement des flux de données évolutifs, en garantissant des opérations de données gouvernées et sans friction, une meilleure collaboration et une plus grande agilité pour les équipes commerciales et chargées des données. Les équipes qui travaillent avec des données bénéficient d'une expérience unifiée sans code ou avec peu de code pour intégrer, transformer, provisionner et surveiller les données pour tous les cas d'utilisation. 

L'intégration de Braze et Nexla permet aux clients qui utilisent Currents de tirer parti de Nexla [pour]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/) extraire, transformer et charger les données des lacs de données vers d'autres emplacements dans un format personnalisé, rendant ainsi les données facilement accessibles dans l'ensemble de votre écosystème.

## Prérequis

| Condition | Descriptif |
|---|---|
| Compte Nexla | Un compte [Nexla] ][2] est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST Braze  | L'URL de votre endpoint REST. Votre endpoint dépendra de l'URL [Braze] de votre instance. ][1] |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

La solution DaaP de Nexla, [Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information), permet de travailler facilement avec des données de n'importe quel format sans se soucier des métadonnées. Lorsque vous configurez vos flux de données à destination ou en provenance de Braze avec Nexla, des outils sans code le rendent facile et disponible en quelques minutes. Une fois le flux de données défini sur une destination, Nexla surveillera votre flux et pourra prendre en charge n'importe quelle quantité de données.

## Intégration

### Étape 1 : Créez un compte Nexla

Si vous n'avez pas encore de compte Nexla, rendez-vous sur le [site Web](https://www.nexla.com) de Nexla pour demander une démonstration et un essai gratuits. Ensuite, ouvrez une session [www.dataops.nexla.io](https://www.dataops.nexla.io)et connectez-vous avec vos nouvelles informations d'identification.

### Étape 2 : Ajoutez votre source

#### Si Braze est votre source de données
1. Sur la plateforme Nexla, accédez à **Flux > Créer un nouveau flux** dans la barre d’outils de gauche.
2. Cliquez sur **Créer une nouvelle source**, sélectionnez le connecteur Braze, puis cliquez sur **Suivant**. 
3. Sélectionnez **Ajouter un nouvel identifiant**, nommez-le et ajoutez votre clé API Braze et votre endpoint REST, puis **Enregistrer**.
4. Enfin, sélectionnez vos données et cliquez sur **Enregistrer**. 

Nexla va désormais rechercher dans la source toutes les données qu'elle trouve et générer un [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) à transformer ou à envoyer à destination.

#### Si Braze est votre destination

Consultez la documentation de Nexla sur la [connexion de sources à Nexla](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source).

### Étape 3 : Transformer (facultatif)

Si vous souhaitez effectuer des [transformations](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations) personnalisées sur vos données ou utiliser les connecteurs prédéfinis de Nexla, cliquez sur le **bouton** Transformer de l'ensemble de données pour accéder au Transform Builder. Vous trouverez des conseils sur l'utilisation de Transform Builder dans la [documentation de Nexla](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data).

### Étape 4 : Envoyer à destination

Pour envoyer des données vers une destination, cliquez sur la flèche **Envoyer vers la destination** du jeu de données et sélectionnez l'un des connecteurs de destination de Nexla ou Braze si vous aviez une autre source. Entrez vos informations d'identification, configurez les options de destination, puis cliquez sur **Enregistrer**. Les données commenceront instantanément à circuler dans le format que vous avez spécifié vers la destination de votre choix.

## Utilisation de cette intégration

Une fois le flux configuré, vous n’avez plus rien à faire. Nexla gérera toutes les modifications apportées aux données sources, s'adaptera à toutes les nouvelles données et vous informera de toute modification du schéma ou de toute erreur de triage. Si vous souhaitez apporter des modifications aux transformations, à la source ou à la destination, vous pouvez cliquer sur ces options et effectuer la modification, et Nexla mettra à jour le flux instantanément.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
Il y a [2]: https://www.nexla.com/get-demo