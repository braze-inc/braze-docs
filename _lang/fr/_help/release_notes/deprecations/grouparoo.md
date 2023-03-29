---
nav_title: Grouparoo
page_order: 1
description: "Cet article présente le partenariat entre Braze et Grouparoo, un outil ETL inversé open source qui alimente vos outils Marketing, Ventes et Support avec les données de votre entrepôt de données."
page_type: update

---

# Grouparoo

{% alert update %}
La prise en charge de Grouparo a été arrêtée en avril 2022.
{% endalert %}

> [Grouparo][1] est un outil ETL inversé open source qui alimente vos outils Marketing, Ventes et Support avec les données de votre entrepôt de données. La configuration est effectuée dans une interface utilisateur centrée sur les modèles, ce qui permet aux collaborateurs non techniques de configurer et planifier des synchronisations de données dans le cadre des opérations.

L’intégration entre Braze et Grouparoo facilite l’opérationnalisation des données stockées dans un entrepôt en les envoyant à Braze. En configurant des calendriers de synchronisation automatique, vous pouvez constamment améliorer vos communications client grâce à des informations actualisées.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte et projet Grouparoo | Un compte Grouparoo est requis pour profiter de ce partenariat.<br><br>Cette intégration peut être utilisée avec l’édition gratuite pour la communauté et les solutions d’entreprise fournies par Grouparoo. La configuration se fait dans l’interface utilisateur de configuration Grouparoo. |
| Clé d’API REST Braze | Une clé API REST Braze avec des utilisateurs et autorisations de suivi. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][1]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créer une application Braze dans Grouparoo

Dans Grouparoo, naviguez jusqu’à **Applications** et sélectionnez **Braze** pour créer une nouvelle application Braze. Sur l’écran modal qui apparaît, entrez votre clé API Braze et votre point de terminaison REST.

![][2]

### Étape 2 : Configurer un modèle et une source de données

Cette intégration nécessite que vous ayez configuré un modèle et une source de données existants avant de passer à l’étape suivante. Si vous n’avez pas cette configuration, consultez la documentation de Grouparoo pour voir comment configurer un [modèle](https://www.grouparoo.com/docs/config/models) et une [source de données](https://www.grouparoo.com/docs/config/sources).

### Étape 3 : Créer une destination Braze dans Grouparoo

#### Sélectionner le mode synchronisation

Dans Grouparoo, sélectionnez votre modèle dans la barre de navigation. Ensuite, faites défiler jusqu’à la **Destinations** et cliquez sur **Add new Destination** (Ajouter une nouvelle destination).

Ensuite, sélectionnez votre application **Braze**, nommez la destination et sélectionnez le mode de synchronisation souhaité parmi les éléments suivants :
- **Synchroniser** : Ajoutez, mettez à jour et supprimez des utilisateurs Braze si nécessaire. Cette option recherche les nouveaux enregistrements, les modifications apportées aux enregistrements existants et les suppressions.
- **Cumulatif** : Ajoutez et mettez à jour les utilisateurs de Braze si nécessaire, mais ne supprimez personne. Cette option recherche les nouveaux utilisateurs à ajouter au Braze et les modifications apportées aux utilisateurs de Braze existants, mais elle ne fait pas de suivi des suppressions.
- **Enrichir** : Mettre à jour uniquement les utilisateurs qui existent déjà dans Braze. Ne pas ajouter ni supprimer des utilisateurs. Cette option met uniquement à jour les utilisateurs existants dans Braze.

#### Mappage des champs de propriété

Ensuite, vous devez mapper les champs de propriété de Grouparoo vers les champs de propriété de Braze. 

![Exemple de champs de mappage de propriété. L’userID Grouparoo est configuré pour mapper vers le champ external_id. Les champs e-mail, firstName et lastName de Braze sont définis sur les champs équivalents « e-mail », « first_name », and « last_name » de Grouparoo.][3]{: style="max-width:80%;"}

Assurez-vous que le champ Braze `external_id` est mappé sur la clé primaire dans votre table source. Mappez le reste des champs si nécessaire pour votre cas d’utilisation.

Section **Send Record Properties** (Envoyer les propriétés d’enregistrement) : Liste des champs de profil utilisateur prédéfinis disponibles pour mapper des données. L’un d’eux peut être synchronisé avec les propriétés de Grouparoo.

Section **Optional Braze User Profile Fields** (Champs de profil utilisateur Braze facultatifs) : Créer des champs de profil utilisateur Braze personnalisés facultatifs. Si vous cliquez sur **Add New Braze User Profile (Ajouter un champ de profil utilisateur Braze)**, vous verrez toutes les propriétés disponibles que vous pouvez mapper vers Braze. Si vous créez un champ, son nom sera identique à celui de la propriété Grouparoo, mais vous pouvez le renommer.

#### Groupes Grouparoo

Outre le mappage, vous pouvez également choisir d’ajouter des groupes Grouparoo aux groupes d’abonnement Braze. 

![Sous « Braze Subscription Groups (Groupes d’abonnement Braze) » dans la fenêtre de configuration de la destination Grouparoo, le groupe Grouparoo « High value with recent automotive purchase » sera ajouté au groupe d’abonnement Braze du même nom.][4]{: style="max-width:80%;"}

{% alert important %}
Vous trouverez plus d’informations et de mises à jour sur cette intégration dans notre [Documentation Grouparoo](https://www.grouparoo.com/docs/integrations/grouparoo-braze).
{% endalert %}

[1]: https://www.grouparoo.com/
[2]: {% image_buster /assets/img/grouparoo/add-app.png %}
[3]: {% image_buster /assets/img/grouparoo/mapping.png %}
[4]: {% image_buster /assets/img/grouparoo/lists.png %}