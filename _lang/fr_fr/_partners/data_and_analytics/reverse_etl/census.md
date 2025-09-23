---
nav_title: Census
article_title: Census
description: "Cet article de référence présente le partenariat entre Braze et Census, une plateforme d'intégration de données qui vous permet de créer dynamiquement des segments d'utilisateurs ciblés avec les données de votre entrepôt cloud."
alias: /partners/census/
page_type: partner
search_tag: Partner

---

# Census

> [Census](https://www.getcensus.com/) est une plateforme d'activation des données qui connecte les entrepôts de données dans le cloud comme Snowflake et BigQuery à Braze. Les équipes marketing peuvent exploiter la puissance de leurs données first-party pour créer des segments d'audience dynamiques, synchroniser les attributs des clients pour personnaliser les campagnes et maintenir à jour toutes leurs données dans Braze. Il est plus facile que jamais de prendre des mesures grâce à des données fiables et exploitables - pas besoin de télécharger des fichiers CSV ou de faire appel à des ingénieurs.

L'intégration entre Braze et Census vous permet d'importer dynamiquement des audiences ou des données produit dans Braze afin d'envoyer des campagnes personnalisées. Par exemple, vous pouvez créer une cohorte dans Braze pour les "abonnés au bulletin d’information avec CLV > 1000" afin de cibler les clients à forte valeur ajoutée ou les "utilisateurs actifs au cours des 30 derniers jours" afin de cibler des utilisateurs spécifiques pour tester une fonctionnalité bêta à venir.

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte Census | Un [compte Census](https://www.getcensus.com/) est nécessaire pour profiter de ce partenariat. |
| Clé d'API REST Braze | Une clé API REST Braze avec toutes les autorisations relatives aux données utilisateur (à l'exception de `users.delete`) et des autorisations `segments.list`. Le jeu de permissions peut changer au fur et à mesure que Census prend en charge d'autres objets Braze. Vous pouvez donc soit accorder plus de permissions maintenant, soit prévoir de mettre à jour ces permissions à l'avenir. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST Braze  | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
| Entrepôt de données et modèle de données | Avant de commencer l'intégration, vous devez disposer d'un entrepôt de données configuré dans Census et définir un modèle du sous-ensemble de données que vous souhaitez synchroniser avec Braze. Consultez la [documentation sur le Census](https://docs.getcensus.com/destinations/braze) pour obtenir une liste des sources de données disponibles et des conseils sur la création de modèles. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Intégration

### Étape 1 : Créer un branchement de service Braze

Pour intégrer Census dans la plateforme Census, accédez à l'onglet **Connexions** et sélectionnez **Nouvelle destination** pour créer une nouvelle connexion de service Braze.

Dans l'invite qui s'affiche, donnez un nom à cette connexion et indiquez l'URL de votre endpoint Braze ainsi que la clé API REST de Braze (et, éventuellement, votre clé d'importation des données pour synchroniser les cohortes).

![]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Étape 2 : Créer une synchronisation Census

Pour synchroniser les clients avec Braze, vous devez créer une synchronisation. Ici, vous définirez où synchroniser les données et comment vous souhaitez que les champs soient mappés entre les deux plateformes.

1. Accédez à l'onglet **Syncs** et sélectionnez **New Sync (Nouvelle synchronisation)**.<br><br> 
2. Dans le compositeur, sélectionnez le modèle de données source de votre entrepôt de données.<br><br>
3. Configurez l'endroit où le modèle sera synchronisé. Sélectionnez **Braze** comme destination et le [type d'objet pris en charge](#supported-objects) à synchroniser.<br>![Dans l'invite "Sélectionnez une destination", "Braze" est sélectionné comme connexion et plusieurs objets sont listés.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Sélectionnez la règle de synchronisation que vous souhaitez appliquer**(la mise à jour ou la création** est le choix le plus courant, mais vous pouvez choisir des règles plus avancées pour gérer la suppression de données, par exemple).<br><br>
5. Ensuite, à des fins de mappage des enregistrements, choisissez une clé de synchronisation pour [mapper](#supported-objects) votre objet Braze à un champ de modèle.<br>![Dans l'invite "Select a Sync Key", "External User ID" de Braze correspond à "user_id" dans la source.]({% image_buster /assets/img/census/census_1.png %}){: style="max-width:80%;"}<br><br>
6. Enfin, mappez les champs de données du Census aux champs équivalents de Braze.<br>![Mappage du Census]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
7. Confirmez les détails et créez la synchronisation. 

Après la synchronisation, les données de l'utilisateur existeront dans Braze. Vous pouvez désormais créer et ajouter un segment Braze aux futures campagnes et Canvas Braze afin de cibler ces utilisateurs. 

{% alert note %}
Lorsque vous utilisez l'intégration de Census et de Braze, Census n'envoie à Braze que les deltas (données modifiées) à chaque synchronisation.
{% endalert %}

## Objets pris en charge

Census prend actuellement en charge la synchronisation des objets suivants de Braze :

| Nom de l'objet | Comportements de synchronisation |
| --- | --- |
| Utilisateur | Mise à jour, création, miroir, suppression |
| Cohorte | Mettre à jour, créer, refléter | 
| Catalogue | Mettre à jour, créer, refléter |
| Groupe d'abonnement | Miroir |
| Événement | Ajouter |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

En outre, Census prend en charge l'envoi de [données structurées](https://docs.getcensus.com/destinations/braze#supported-objects) à Braze : 
- Jetons de poussée de l'utilisateur : Pour envoyer des jetons de notifications push, vos données doivent être structurées comme un tableau d'objets avec 2-3 valeurs : `app_id`, `token` et une valeur facultative `device_id`.
- Attributs personnalisés imbriqués : Les objets et les tableaux sont pris en charge. En avril 2022, cette fonctionnalité est encore en accès anticipé. Il se peut que vous deviez contacter votre gestionnaire de compte Braze pour y accéder.

