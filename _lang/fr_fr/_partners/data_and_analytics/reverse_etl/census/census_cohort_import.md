---
nav_title: Census
article_title: Importation de la cohorte du Census
description: "Cet article de référence présente la fonctionnalité d'importation de cohortes de Census, une plateforme d'intégration de données qui vous permet de créer dynamiquement des segments d'utilisateurs ciblés avec les données de votre entrepôt en nuage."
page_type: partner
search_tag: Partner

---

# Importation de la cohorte du Census

> Cet article décrit comment importer des cohortes d'utilisateurs de [Census](https://www.getcensus.com/) vers Braze. Pour plus d'informations sur l'intégration de Census, consultez l'[article sur Census]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/census/).

## Intégration de l'importation de cohortes

### Étape 1 : Créer un branchement de service Braze

Pour intégrer Census dans la plateforme Census, accédez à l'onglet **Connexions** et sélectionnez **Nouvelle destination** pour créer une nouvelle connexion de service Braze.

Dans l'invite qui s'affiche, nommez cette connexion et indiquez l'URL de votre endpoint Braze, la clé de l'API REST de Braze et la clé d'importation des données. La clé d'importation des données est nécessaire pour synchroniser les cohortes et peut être trouvée dans Braze en allant dans **Intégrations partenaires** > **Partenaires technologiques** > **Census.**

![]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Étape 2 : Créer une synchronisation Census

Pour synchroniser les clients avec Braze, vous devez créer une synchronisation. Ici, vous définirez où synchroniser les données et comment vous souhaitez que les champs soient mappés entre les deux plateformes.

1. Accédez à l'onglet **Syncs** et sélectionnez **New Sync (Nouvelle synchronisation)**.<br><br> 
2. Dans le compositeur, sélectionnez le modèle de données source de votre entrepôt de données.<br><br>
3. Configurez l'endroit où le modèle sera synchronisé. Sélectionnez **Braze** comme destination et **Utilisateur & Cohorte** comme objet à synchroniser.<br>![Dans l'invite "Sélectionnez une destination", "Braze" est sélectionné comme connexion et plusieurs objets sont listés.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Sélectionnez la **colonne source** qui identifie les utilisateurs à ajouter à une cohorte et sélectionnez **ID externe** comme **type d'identifiant**.<br><br>
5. Dans le menu déroulant **Nom de la cohorte**, sélectionnez une cohorte, créez une cohorte ou sélectionnez une colonne source pour remplir le nom de la cohorte.<br><br>
6. Utilisez le menu déroulant **Lorsqu'un enregistrement est supprimé des données source** pour sélectionner ce qui arrive aux utilisateurs lorsqu'ils sont supprimés de l'ensemble de données source, par exemple **Ne rien faire** ou **Supprimer l'enregistrement correspondant de la cohorte.**<br><br>
7. Enfin, mappez les champs de données du Census aux champs équivalents de Braze.<br>![Mappage du Census]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
8. Confirmez les détails et créez la synchronisation. 

Vous pouvez maintenant effectuer votre synchronisation !

Lors d'une synchronisation, tous les champs que vous mappez seront d'abord synchronisés avec l'objet utilisateur afin de mettre à jour ce qui existe déjà dans Braze. Ensuite, l'utilisateur mis à jour sera ajouté à la cohorte spécifiée.

Après la synchronisation, vous pouvez créer et ajouter un segment Braze avec un filtre de cohorte Census aux futures campagnes et Canvases Braze pour cibler ces utilisateurs. 

{% alert note %}
Lorsque vous utilisez l'intégration de Census et de Braze, Census n'envoie à Braze que les deltas (données modifiées) à chaque synchronisation.
{% endalert %}

{% alert important %}
Seuls les utilisateurs qui existent déjà dans Braze pourront être ajoutés ou supprimés d'une cohorte. L'importation d'une cohorte ne créera pas de nouveaux utilisateurs dans Braze.
{% endalert %}

## Correspondance entre les utilisateurs

Les utilisateurs identifiés peuvent être associés à leur adresse `external_id` ou `alias`. Les utilisateurs anonymes peuvent être mis en relation avec leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id`, et doivent être identifiés par leur `external_id` ou `alias`.

