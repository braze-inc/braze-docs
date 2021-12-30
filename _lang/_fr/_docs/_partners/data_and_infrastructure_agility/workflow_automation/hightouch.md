---
nav_title: Toucher haut
article_title: Toucher haut
description: "Cet article décrit le partenariat entre Braze et Hightouch, une plateforme pour synchroniser les données de vos clients de votre entrepôt aux outils commerciaux."
alias: /fr/partners/hightouch/
page_type: partenaire
search_tag: Partenaire
---

# Toucher haut

> [Hightouch][1] est une plate-forme moderne d'intégration de données qui vous permet de synchroniser le client, le produit, le client ou des données de propriété de votre entrepôt ou de votre lac de données vers n'importe quelle application de votre choix, le tout sans l'aide de vos équipes informatiques ou d'ingénierie.

L'intégration de Braze et Hightouch vous permet de construire de meilleures campagnes sur Braze avec des données clients actualisées à partir de votre entrepôt de données. En synchronisant automatiquement les données des clients au Brésil, vous n'avez plus besoin de vous soucier de la cohérence des données et vous pouvez vous concentrer sur la création d'expériences clients de classe mondiale.

## Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte en mode Hightouch        | Un compte Hightouch est requis pour profiter de ce partenariat.                                                                                                                                                                                                                                                                                      |
| Braze clé API REST              | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le **tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API**                                                                                                                                         |
| Point de terminaison REST Braze | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance][2].<br><br>Hightouch requiert tout après "https://rest." pour spécifier votre terminal. Par exemple, si votre point de terminaison Braze est `https://rest.iad-01.braze.com`, vous aurez seulement besoin de `iad-01.braze.com`. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d'utilisation

* Synchronisez les données des utilisateurs et des comptes dans Braze pour créer des campagnes hyper-personnalisées.
* Mettre à jour automatiquement vos segments Braze avec de nouvelles données depuis votre entrepôt.
* Offrez de meilleures expériences en apportant des données provenant d'autres points de contact clients au Brésil.

## Intégration

### Étape 1 : Créez votre destination de Braze en mode Hightouch

1. Sur la plate-forme HighTouch, dans la section **Destinations** , cliquez sur **Ajouter une destination**.
2. Sélectionnez **Braze** dans la liste des destinations disponibles.
3. Fournissez votre point de terminaison Braze REST (à l'exception de "https://rest.") et votre clé d'API REST Braze.<br><br>!\[Ajouter une destination\]\[3\]

### Étape 2 : Synchronisation des objets et des événements

Hightouch prend en charge la synchronisation avec les objets utilisateur et les événements.

| Destination | Libellé                                                                                                                        | Modes pris en charge                 |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| Objet       | Synchronise les enregistrements vers des objets tels que les utilisateurs ou les organisations de votre destination.           | Mise à jour ou mise à jour           |
| Évènements  | Synchronise les enregistrements en tant qu'événements vers votre destination; c'est souvent sous la forme d'un appel de piste. | Suivre l’événement ou suivre l’achat |

#### Synchronisation des objets Braze

Vous pouvez synchroniser les objets Hightouch (champs utilisateur) avec les champs équivalents par défaut ou personnalisés de Braze. Vous pouvez également effectuer des correspondances d'enregistrements pour aider à unifier les données sur les deux plateformes.

#### Synchronisation des événements Braze

Hightouch vous permet de suivre les événements et acheter des données et de les synchroniser avec Braze. Plusieurs options peuvent être définies dans Hightouch qui affecteront le comportement de synchronisation, telles que la mise en place de données de suivi et la définition d'un comportement utilisateur inexistant.

{% alert important %}
Des instructions supplémentaires sur la synchronisation des objets et des événements peuvent être trouvées dans la [documentation Hightouch](https://hightouch.io/docs/destinations/braze/).
{% endalert %}
[3]: {% image_buster /assets/img/hightouch/hightouch_braze_setup.png %}


[1]: https://hightouch.io
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)