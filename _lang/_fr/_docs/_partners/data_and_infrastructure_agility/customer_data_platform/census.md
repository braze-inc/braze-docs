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

> [Recensement][1] est la plate-forme d'intégration de données qui vous permet de synchroniser les données clients et produits de votre entrepôt cloud aux applications de vente et de marketing de votre choix, le tout sans l'aide continue de votre service d'ingénierie.

L'intégration de Braze et Recensement vous permet d'importer dynamiquement les données de vos produits de recensement dans Braze pour créer des segments d'utilisateurs ciblés. Par exemple, après avoir testé et implémenté avec succès l'intégration, Braze peut créer un segment utilisateur à partir des nouvelles données de 'Utilisateurs actifs dans les 30 derniers jours' pour cibler des utilisateurs spécifiques pour leur demander de tester une prochaine fonctionnalité bêta.

## Pré-requis

| Exigences                                | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Compte de recensement                    | Un [compte de recensement][1] est requis pour profiter de ce partenariat.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Braze clé API REST                       | Une clé API Braze REST avec toutes les permissions de données utilisateur (à l'exception des permissions `users.delete`) et `segments.list`. Les permissions peuvent changer car le recensement ajoute la prise en charge de plus d'objets Braze, donc vous pouvez soit accorder plus de permissions maintenant, soit planifier de mettre à jour ces permissions à l'avenir. <br><br> Ceci peut être créé dans le **tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API** |
| Point de terminaison REST Braze          | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance][2].                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Entrepôt de données et modèle de données | Avant de commencer l'intégration, vous devez avoir un entrepôt de données installé dans le recensement et définir un modèle du sous-ensemble de données que vous voulez synchroniser avec Braze. Visitez la [documentation de recensement](https://docs.getcensus.com/destinations/braze) pour une liste des sources de données disponibles et des conseils sur la création de modèles.                                                                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Intégration

### Étape 1 : Créer une connexion au service Braze

Pour intégrer le recensement, dans la plate-forme de recensement, accédez à l'onglet **Paramètres** et sélectionnez **Add Service** pour créer une nouvelle connexion au service Braze.

Dans l'invite qui apparaît, nommez cette connexion, et fournissez votre URL de terminaison Braze et la clé d'API de Braze REST.

!\[Add service\]\[8\]{: style="max-width:60%;"}

### Étape 2 : Créer une synchronisation de recensement

Pour synchroniser vos clients avec Braze, vous devez construire une synchronisation. Ici, vous allez définir où synchroniser les données et comment vous voulez que les champs soient mappés sur les deux plateformes.

1. Naviguez dans l'onglet **Synchronisations** et sélectionnez **Ajouter une synchro**.
2. Dans l'invite qui apparaît, sous **Connexion**, sélectionnez votre entrepôt de données désiré.
3. Ensuite, sélectionnez la source. Il s'agit du modèle de données construit à partir des données de votre entrepôt de données.
4. Configurer où le modèle sera synchronisé. Sélectionnez **Braze** comme connexion, et le [type d'objet pris en charge](#supported-objects) pour synchroniser.<br>!\[Census sync\]\[10\]{: style="max-width:80%;"}<br><br>
5. Assurez-vous que **Mettre à jour ou Créer** est sélectionné comme une règle de synchronisation.
6. Ensuite, à des fins de concordance d'enregistrement, choisissez l'identifiant utilisateur [Braze que vous souhaitez](#supported-objects) pour votre type d'objet Braze et le champ de modèle associé.<br>!\[Sync\]\[9\]{: style="max-width:80%;"}<br><br>
7. Enfin, mappez les champs de données de recensement aux champs équivalents de Braze.<br>!\[Recensement mapping\]\[11\]{: style="max-width:80%;"}<br><br>
8. Confirmez les détails et créez la synchronisation.

Une fois que la synchronisation est créée, vous trouverez les données utilisateur déjà en Brésil. Vous pouvez maintenant créer un segment Braze et l'ajouter aux futures campagnes Braze et Canvases pour cibler ces utilisateurs finaux.

{% alert note %}
Lors de l'utilisation de l'intégration du recensement et de Braze, le recensement enverra uniquement les deltas (changement de données) à chaque synchronisation au Brésil.
{% endalert %}

## Objets pris en charge

Le recensement prend actuellement en charge la synchronisation des objets Braze suivants :

| Nom de l'objet | Identifiants             |
| -------------- | ------------------------ |
| Utilisateur    | ID d'utilisateur externe |
| Evénement      | ID de l'événement        |
[8]: {% image_buster /assets/img/census/add_service.png %} [9]: {% image_buster /assets/img/census/census_1. ng %} [10]: {% image_buster /assets/img/census/census_2.png %} [11]: {% image_buster /assets/img/census/census_3.png %}

[1]: https://www.getcensus.com/

[1]: https://www.getcensus.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints