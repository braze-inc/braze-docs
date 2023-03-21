---
nav_title: Census
article_title: Census
page_order: 9
description: "Cet article présente de référence le partenariat entre Braze et Census, une plateforme d’intégration de données qui vous permet de créer dynamiquement des segments d’utilisateur ciblés en vous servant des données de votre entrepôt cloud."
alias: /partners/census/
page_type: partner
search_tag: Partenaire

---

# Census

> [Census][1] est une plateforme d’intégration de données qui vous permet de synchroniser les données client et produit de votre entrepôt cloud vers les applications de vente et de marketing de votre choix, sans faire continuellement appel à votre service technique. 

L’intégration de Braze et de Census vous permet d’importer dynamiquement vos données de produits Census dans Braze pour créer des segments d’utilisateur ciblés. Par exemple, après avoir testé et mis en œuvre l’intégration, Braze peut créer un segment d’utilisateur en utilisant les nouvelles données des « Utilisateurs actifs au cours des 30 derniers jours » pour cibler des utilisateurs spécifiques afin de leur demander de tester une fonctionnalité bêta à venir.

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte Census | Un compte [Census][1] est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé API REST de Braze qui inclut toutes les autorisations de données utilisateur (sauf pour `users.delete`) et des autorisations `segments.list`. Les autorisations peuvent changer à mesure que Census prend en charge un plus grand nombre d’objets Braze. Vous pouvez donc choisir d’accorder davantage d’autorisations maintenant ou prévoir de mettre à jour ces autorisations à l’avenir. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze  | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance][2]. |
| Entrepôt de données et modèle de données | Avant de commencer l’intégration, vous devez disposer d’un entrepôt de données configuré dans Census et définir un modèle du sous-ensemble de données que vous souhaitez synchroniser avec Braze. Consultez la [documentation Census](https://docs.getcensus.com/destinations/braze) pour obtenir une liste des sources de données disponibles et des conseils pour vous aider à créer un modèle. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Intégration

### Étape 1 : Créer une connexion de service Braze

Pour intégrer Census, rendez-vous sur la plateforme Census, accédez à l’onglet **Settings (Paramètres)** et sélectionnez **Add Service (Ajouter un service)** afin de créer une nouvelle connexion de service Braze.

Dans l’invite qui apparaît, nommez cette connexion et fournissez votre URL d’endpoint Braze et votre clé API REST Braze.

![][8]{: style="max-width:60%;"}

### Étape 2 : Créer une synchronisation avec Census

Pour synchroniser des clients sur Braze, vous devez créer une synchronisation. Ici, vous définirez où synchroniser les données et comment vous souhaitez que les champs soient mappés sur les deux plateformes.

1. Accédez à l’onglet **Syncs (Synchronisations)** et sélectionnez **Add Sync (Ajouter une synchronisation)**. 
2. Dans l’invite qui apparaît, sous **Connection (Connexion)**, sélectionnez l’entrepôt de données souhaité.
3. Ensuite, sélectionnez la source. Il s’agit du modèle de données conçu à l’aide des données de votre entrepôt de données.
4. Configurez l’emplacement de synchronisation du modèle. Sélectionnez **Braze** comme connexion, et le [type d’objet pris en charge](#supported-objects) à synchroniser.<br>![Dans l’invite « What do you want to sync (Que voulez-vous synchroniser ? ) », « Redshift » est sélectionné comme connexion et « Golden Users - VIP » est défini comme source. Dans l’invite « Where do you want to sync data to? (Où voulez-vous synchroniser les données ?) », « Braze » est sélectionné comme connexion, et « User (Utilisateur) » est défini en tant qu’objet.][10]{: style="max-width:80%;"}<br><br>
5. Assurez-vous de sélectionner **Update or Create (Mettre à jour ou créer)** comme règle de synchronisation.
6. Ensuite, pour que les enregistrements correspondent, choisissez l’option souhaitée [dans l’invite « How are source and destination records matched? (Comment les enregistrements de source et de destination sont-ils mis en correspondance ?) », « External User ID (ID utilisateur externe) » est défini comme « id ».](#supported-objects) pour votre type d’objet Braze et le champ de modèle associé.<br>![Dans l’invite « Which fields should be updated? (Quels champs doivent être mis à jour ?) », « External User ID (ID utilisateur externe) » est défini comme « id », « Email » est défini comme « e-mail », « First Name (Prénom) » est défini comme « first_name », et « Last Name (Nom de famille) » est défini comme « last_name ».][9]{: style="max-width:80%;"}<br><br>
7. Enfin, mappez les champs de données Census aux champs équivalents de Braze.<br>![Mappage de Census][11]{: style="max-width:80%;"}<br><br>
8. Confirmez les détails et créez la synchronisation. 

Une fois la synchronisation créée, les données utilisateur se trouveront déjà dans Braze. Vous pouvez maintenant créer un segment Braze et l’ajouter à de futures campagnes et Canvas Braze pour cibler ces utilisateurs finaux. 

{% alert note %}
Si vous utilisez l’intégration de Census et Braze, Census enverra uniquement les deltas (données modifiées) lors de chaque synchronisation à Braze. 
{% endalert %}

## Objets pris en charge

Actuellement, Census prend en charge la synchronisation des objets d’utilisateur et d’événement Braze suivants :

| Nom de l’objet | Identifiants |
| --- | --- |
| Utilisateur | ID utilisateur externe |
| Événement | ID de l’événement |

De plus, Census prend en charge l’envoi de [données structurées](https://docs.getcensus.com/destinations/braze#supported-objects) à Braze : 
- Jetons de notification push utilisateur : Pour envoyer des jetons de notification push, vos données doivent être structurées comme une matrice d’objets comportant deux ou trois valeurs : `app_id`, `token`et `device_id` (facultatif).
- Attributs personnalisés imbriqués : Les objets et les matrices sont pris en charge. Au mois d’avril 2022, cette fonctionnalité est toujours proposée en accès anticipé. Vous devrez peut-être contacter votre gestionnaire de compte Braze pour y accéder.

[1]: https://www.getcensus.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[8]: {% image_buster /assets/img/census/add_service.png %}
[9]: {% image_buster /assets/img/census/census_1.png %}
[10]: {% image_buster /assets/img/census/census_2.png %}
[11]: {% image_buster /assets/img/census/census_3.png %}