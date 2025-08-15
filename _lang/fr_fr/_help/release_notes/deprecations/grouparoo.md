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

> [Grouparoo](https://www.grouparoo.com/) est un outil d'ETL inverse open-source qui permet d'alimenter facilement vos outils de marketing, de vente et de support en utilisant les données de votre entrepôt. La configuration est effectuée dans une interface utilisateur centrée sur les modèles, ce qui permet aux collaborateurs non techniques de configurer et planifier des synchronisations de données dans le cadre des opérations.

L’intégration entre Braze et Grouparoo facilite l’opérationnalisation des données stockées dans un entrepôt en les envoyant à Braze. En configurant des calendriers de synchronisation automatique, vous pouvez constamment améliorer vos communications client grâce à des informations actualisées.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte et projet Grouparoo | Un compte Grouparoo est requis pour profiter de ce partenariat.<br><br>Cette intégration peut être utilisée avec l’édition gratuite pour la communauté et les solutions d’entreprise fournies par Grouparoo. La configuration se fait dans l’interface utilisateur de configuration Grouparoo. |
| Clé API REST Braze | Une clé API REST Braze avec des utilisateurs et autorisations de suivi. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.](https://www.grouparoo.com/) Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Créer une application Braze dans Grouparoo

Dans Grouparoo, naviguez vers **Apps** et sélectionnez **Braze** pour créer une nouvelle application Braze. Sur l’écran modal qui apparaît, entrez votre clé API Braze et votre point de terminaison REST.

![]({% image_buster /assets/img/grouparoo/add-app.png %})

### Étape 2 : Configurer un modèle et une source de données

Cette intégration nécessite que vous ayez configuré un modèle et une source de données existants avant de passer à l’étape suivante. Si ce n'est pas le cas, consultez la documentation de Grouparoo pour apprendre à configurer un [modèle](https://www.grouparoo.com/docs/config/models) et une [source de données](https://www.grouparoo.com/docs/config/sources).

### Étape 3 : Créer une destination Braze dans Grouparoo

#### Sélectionner le mode synchronisation

Dans Grouparoo, sélectionnez votre modèle dans la barre de navigation. Ensuite, faites défiler jusqu'à la section **Destinations** et cliquez sur **Ajouter une nouvelle destination**.

Ensuite, sélectionnez l'application **Braze** que vous avez créée, nommez la destination et sélectionnez le mode de synchronisation de votre choix parmi les suivants :
- **Sync**: Ajoutez, mettez à jour et supprimez des utilisateurs Braze si nécessaire. Cette option recherche les nouveaux enregistrements, les modifications apportées aux enregistrements existants et les suppressions.
- **Additif**: Ajoutez et mettez à jour les utilisateurs de Braze si nécessaire, mais ne supprimez personne. Cette option recherche les nouveaux utilisateurs à ajouter au Braze et les modifications apportées aux utilisateurs de Braze existants, mais elle ne fait pas de suivi des suppressions.
- **Enrichissez**: Mettre à jour uniquement les utilisateurs qui existent déjà dans Braze. Ne pas ajouter ni supprimer des utilisateurs. Cette option met uniquement à jour les utilisateurs existants dans Braze.

#### Mappage des champs de propriété

Ensuite, vous devez mapper les champs de propriété de Grouparoo vers les champs de propriété de Braze. 

![Exemple de champs de mappage de propriété. L'identifiant de l'utilisateur Grouparoo est mappé sur l'identifiant externe. L'e-mail, le prénom et le nom de famille sont définis comme des champs grouparoo équivalents "e-mail", "prénom" et "nom de famille".]({% image_buster /assets/img/grouparoo/mapping.png %}){: style="max-width:80%;"}

Assurez-vous que le champ Braze `external_id` est mappé sur la clé primaire dans votre table source. Mappez le reste des champs si nécessaire pour votre cas d’utilisation.

Section **Propriétés de l'enregistrement d'envoi**: Liste des champs de profil utilisateur prédéfinis disponibles pour mapper des données. L’un d’eux peut être synchronisé avec les propriétés de Grouparoo.

La section **Champs du profil utilisateur de Braze est facultative**: Créer des champs de profil utilisateur Braze personnalisés facultatifs. Si vous cliquez sur **Ajouter un nouveau champ de profil utilisateur Braze**, vous verrez toutes les propriétés disponibles que vous pouvez mapper à Braze. Si vous créez un champ, son nom sera identique à celui de la propriété Grouparoo, mais vous pouvez le renommer.

#### Groupes Grouparoo

Outre le mappage, vous pouvez également choisir d’ajouter des groupes Grouparoo aux groupes d’abonnement Braze. 

![Dans la fenêtre de configuration de la destination Grouparoo, sous "Groupes d'abonnement Braze", le groupe Grouparoo "Valeur élevée avec achat automobile récent" sera ajouté au groupe d'abonnement Braze "Valeur élevée avec achat automobile récent".]({% image_buster /assets/img/grouparoo/lists.png %}){: style="max-width:80%;"}

{% alert important %}
Vous trouverez plus de détails et de mises à jour sur cette intégration dans la [documentation de Grouparoo](https://www.grouparoo.com/docs/integrations/grouparoo-braze).
{% endalert %}

