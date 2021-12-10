---
nav_title: Recensement
article_title: Recensement
page_order: 9
description: "Cet article décrit le partenariat entre Braze et le recensement, une plate-forme d'intégration de données qui vous permet de créer dynamiquement des segments d'utilisateurs ciblés avec des données de votre entrepôt cloud."
alias: /fr/partners/recense/
page_type: partenaire
search_tag: Partenaire
---

# Recensement

> [Recensement][1] est la plate-forme d'intégration de données qui vous permet de synchroniser les données clients et produits de votre entrepôt cloud avec les applications de vente et de marketing de votre choix.

Avec le recensement, la réussite de vos clients, les ventes et les équipes de marketing sur la même page n'ont jamais été aussi faciles. En tant que partenaire technologique de Braze, le recensement maintient les données de vos clients synchronisées sans l'aide continue de votre service d'ingénierie.

## Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                      |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Clé API Braze                   | Vous devrez créer une nouvelle clé d'API.<br><br>Ceci peut être créé dans la **Console Développeur -> Paramètres API -> Créer une nouvelle clé API** avec **utilisateurs. permissions** de rack. |
| Point de terminaison REST Braze | Votre REST [Endpoint URL][2]. Votre point de terminaison dépendra de l'URL de Braze pour votre instance.                                                                                                     |
| Compte de recensement           | Un compte de recensement actif est nécessaire pour profiter de cette intégration de Braze.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration de Braze et Recensement

L'intégration de Braze et Recensement vous permet d'utiliser les données de vos produits pour créer dynamiquement des segments d'utilisateurs ciblés au Brésil. Par exemple, après avoir testé et implémenté avec succès l'intégration, Braze peut créer un segment utilisateur de 'Utilisateurs actifs dans les 30 derniers jours' pour cibler des utilisateurs spécifiques pour leur demander de tester une prochaine fonctionnalité bêta.

### Étape 1 : Créer une clé API Braze

Braze vous permet de créer plusieurs clés API, chacune avec ses propres permissions. Dans la plupart des cas, la pratique recommandée est de créer une nouvelle clé API pour le recensement plutôt que de réutiliser une clé existante.

1. Dans Braze, accédez à **Paramètres** en bas de la barre de navigation de gauche et cliquez sur **Console développeur**.
2. Dans l'onglet **Paramètres de l'API** , sous **Clefs d'API Rest**, cliquez sur **+ Créer une nouvelle clé API**.
3. Nommez cette clé API et sélectionnez toutes les autorisations de données utilisateur, à l'exception de `users.delete`. Les permissions peuvent changer car le recensement ajoute la prise en charge de plus d'objets Braze, donc vous pouvez soit accorder plus de permissions maintenant, soit planifier de mettre à jour ces permissions à l'avenir. Ensuite, sélectionnez **Enregistrer la clé API**.
4. Enfin, copiez la clé API trouvée sous **Identificateur** à utiliser lors de la création de votre connexion de recensement.

### Étape 2 : Sélectionnez votre point de terminaison de l'API Braze

Localisez et notez votre point de terminaison de l'API REST Braze ; cela sera nécessaire lors de la création de votre connexion de recensement avec Braze. Votre point de terminaison dépendra de l'URL [Braze][2] pour votre instance.

### Étape 3 : Créer la connexion de recensement

1. Dans l'onglet **Paramètres du recensement** , sélectionnez **Ajouter un service** et créez un nouveau **Braze Service Connection**.
2. Nommez cette connexion et fournissez votre URL de point de terminaison Braze et votre clé API.<br><br>!\[add_service\]\[8\]{: style="max-width:60%;"}

## Synchronisation dans le recensement

Lors de l'utilisation de l'intégration du recensement et de Braze, le recensement enverra uniquement les deltas (changement de données) à chaque synchronisation au Brésil.

### Comportements de synchronisation pris en charge

Le recensement prend en charge la synchronisation de vos données à la fois à l'utilisateur et à l'objet événement au Brésil. Visitez la [documentation de recensement](https://docs.getcensus.com/destinations/braze) suivante pour en savoir plus sur cette intégration et les comportements de synchronisation de recensement.
[8]: {% image_buster /assets/img/census/add_service.png %}

[1]: https://www.getcensus.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints