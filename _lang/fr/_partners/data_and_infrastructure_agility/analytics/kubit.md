---
nav_title: Kubit
article_title: Kubit
page_order: 1
description: "Cet article présente le partenariat entre Braze et Kubit, une plateforme d’analyses sans code et en libre-service qui fournit des informations instantanées sur les produits."
alias: /partners/kubit/
page_type: partner
search_tag: Partenaire

---

# Kubit

> [Kubit](https://kubit.ai/) est une plateforme d’analyses en libre-service, sans code, qui fournit des informations instantanées sur les produits. 

L’intégration de Braze et Kubit vous permet d’importer des cohortes d’utilisateurs Kubit et de les cibler dans la messagerie Braze. En outre, grâce au [partage sécurisé des données Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/), vous pouvez également intégrer les données brutes de campagnes et d’impression de Braze avec les analyses de produits de Kubit pour mesurer l’impact de ces campagnes en temps réel. Cette approche fournit des informations sur le cycle de vie complet de vos utilisateurs sans aucun travail technique de votre part.

## Conditions préalables

| Condition | Description |
|---|---|
|Compte entreprise Kubit | Un compte d’entreprise Kubit est requis pour profiter de ce partenariat. |
| ID utilisateur correspondant | Les données de vos clients stockées dans Kubit et Braze doivent avoir des ID utilisateur correspondants sur les deux plateformes. Cela inclut également les identifiants uniques universels (UUID) anonymes. Consultez notre [documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) pour savoir comment Braze configure les ID utilisateur. |
{: .reset-td-br-1 .reset-td-br-2} 

## Intégration de l’importation de données

### Étape 1 : Obtenir la clé d’importation des données Braze

Dans Braze, accédez à **Technology Partners (partenaires technologiques)** et sélectionnez **Kubit**. Ici, vous trouverez l’endpoint REST pour générer votre clé d’importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d’importation des données et l’endpoint REST sont utilisés dans l’étape suivante pour configurer un postback dans le tableau de bord de Kubit.<br><br>![La page des partenaires de technologie Kubit dans Braze.]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### Étape 2 : Configurer Braze dans Kubit

Fournissez la clé d’importation des données de Braze et l’endpoint REST de Braze à votre conseiller client Kubit. Kubit se chargera de configurer l’intégration de son côté et vous préviendra lorsque l’intégration est en place.  

### Étape 3 : Importer des cohortes dans Braze

#### Créer une cohorte dans Kubit
[Créez une cohorte](https://www.kubit.ai/doc/fundamentals#cohort) dans Kubit et définissez les critères de vos utilisateurs cibles.<br><br>![]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### Importer des utilisateurs dans Braze
Après avoir enregistré votre cohorte, vous pouvez l’importer dans Braze pour l’utiliser dans des segments Braze. Ces segments peuvent ensuite être utilisés pour créer des campagnes ciblées par e-mail ou notification push et des Canvas.

Pour ce faire, accédez à votre cohorte et sélectionnez **Importer dans Braze** sous **Contrôle des cohortes**.

![]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

Sélectionnez ensuite la fréquence d’importation souhaitée. Les importations ponctuelles vous permettent d’importer une fois la cohorte. Les importations programmées vous permettent d’importer quotidiennement, hebdomadaire ou mensuelle à un moment précis. Notez que chaque cohorte peut uniquement avoir une planification d’importation en direct. 

![]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

#### Vérifier le statut d’importation
Après chaque importation effectuée avec succès, une notification par e-mail sera envoyée aux destinataires spécifiés dans la planification d’importation. Vous pouvez également vérifier le statut d’importation d’une cohorte dans la section **Planification** de Kubit. L’historique de planification affiche les délais d’importation, les résultats et le nombre total d’utilisateurs de la cohorte qui ont été importés dans Braze.<br><br>![]({% image_buster /assets/img/kubit/import_history.png %})<br><br>Vous pouvez déclencher manuellement une importation en cliquant sur **Import to Braze** (Importer dans Braze) dans cette planification d’importation.

### Étape 4 : Créer des segments Braze avec des cohortes Kubit
Après avoir importé des cohortes dans Braze, vous pouvez les utiliser comme filtres pour créer des segments Braze et les inclure dans des campagnes Braze ou des Canvas. Consultez notre documentation sur les segments pour savoir [comment créer des segments dans Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment).

![Dans le générateur de segments de Braze, l’attribut utilisateur « Kubit cohorts » (cohortes Kubit) est défini sur « includes_value » et affiche une liste des cohortes disponibles.]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}

## Analyser les données de Braze dans Kubit (optional)
Utilisez le [partage sécurisé de données Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/) pour partager vos données brutes de campagne et d’impression de Braze avec Kubit et les intégrer aux analyses en libre-service de Kubit afin d’obtenir un aperçu complète du cycle de vie de vos utilisateurs.

À titre informatif, voici tous les [champs Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2) qui peuvent être intégrés aux analyses de Kubit. Les détails de cette étape dépendent fortement de chaque client et nécessitent des configurations spéciales. Contactez votre gestionnaire de compte Kubit ou envoyez un e-mail à l’adresse [support@kubit.ai](support@kubit.ai) pour en savoir plus.