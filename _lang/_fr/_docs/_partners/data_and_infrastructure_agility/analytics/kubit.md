---
nav_title: Koubit
article_title: Koubit
page_order: 1
description: "Cet article décrit le partenariat entre Braze et Kubit, une plate-forme d'analyse en libre service sans code qui fournit des aperçus instantanés sur les produits."
alias: /fr/partners/kubit/
page_type: partenaire
search_tag: Partenaire
---

# Koubit

> [Kubit](https://kubit.ai/) est une plate-forme d'analyse en libre service sans code qui fournit des aperçus instantanés sur les produits.

L'intégration de Braze et Kubit vous permet d'importer des cohortes d'utilisateurs de Kubit et de les cibler dans le message de Braze. En outre, en utilisant [Snowflake sécurisé de partage de données]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/), vous pouvez également intégrer les données de campagne brute et d’impression de Braze avec les analytiques de produits Kubit pour mesurer l’impact de ces campagnes en temps réel. Cette approche vous donne un aperçu du cycle de vie complet de vos utilisateurs sans nécessiter aucun effort d'ingénierie.

## Pré-requis

| Exigences                      | Libellé                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte d'entreprise Kubit      | Un compte d'entreprise Kubit est requis pour profiter de ce partenariat.                                                                                                                                                                                                                                                                                                  |
| ID d'utilisateur correspondant | Vos données clients dans Kubit et Braze doivent avoir des identifiants d'utilisateurs correspondants sur les deux plateformes. Cela inclut également les UUID anonymes. Visitez notre [documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) pour savoir comment Braze définit les identifiants d'utilisateur. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Récupère la clé d'importation de données Braze

Au Brésil, accédez aux **partenaires technologiques** et sélectionnez **Kubit**. Ici, vous trouverez le point de terminaison REST et générez votre clé d'importation de données Braze. Une fois généré, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation de données et le point de terminaison REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord de Kubit.<br><br>![Config on Kubit]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### Étape 2 : Configurer Braze en Kubit

Fournissez la clé d'importation de données Braze et le point de terminaison de Braze REST à votre contact de support Kubit. Ils configureront l'intégration de leur côté et vous indiqueront quand l'intégration sera en vie.

### Étape 3 : Importer des cohortes à Braze

#### Créer une cohorte en Kubit
[Créez une cohorte](https://www.kubit.ai/doc/fundamentals#cohort) en Kubit et définissez les critères des utilisateurs ciblés.<br><br>![Create a cohort]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### Importer des utilisateurs à Braze
Une fois que vous avez sauvegardé votre cohorte, vous pouvez les importer à Braze pour être utilisé dans les segments de Braze. Ces segments peuvent ensuite être utilisés pour créer des campagnes d'email ou de push ciblées et des Canvases.

Pour cela, accédez à votre cohorte existante et sous **Cohort Control** sélectionnez **Import to Braze**.

![Importer dans Braze]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="largeur-max-80%;"}

Ensuite, sélectionnez la cadence d'importation souhaitée. Les importations ponctuelles vous permettent d'importer dès maintenant. Les importations planifiées vous permettent d'importer tous les jours, toutes les semaines ou tous les mois à une heure précise. Notez que chaque cohorte ne peut avoir qu'un seul planning d'importation en direct.

![Importer un calendrier]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="largeur-max:40%;"}

#### Vérifier le statut d'importation
Une fois l'importation terminée, une notification par courriel sera envoyée au ou aux destinataires spécifiés dans le calendrier d'importation. Vous pouvez également vérifier l'état d'import d'une cohorte sous **Schedule** dans Kubit. L'historique des horaires affichera toutes les heures d'exécution de l'importation, les résultats et le nombre total d'utilisateurs de la cohorte qui ont été importés au Brésil.<br><br>![Import History]({% image_buster /assets/img/kubit/import_history.png %})<br><br>Vous pouvez déclencher manuellement une importation en cliquant sur l'icône **Importer vers Braze** pour ce planning d'importation.

### Étape 4 : Créer des segments de Braze avec des cohortes de Kubit
Après avoir importé des cohortes au Brésil, vous pouvez les utiliser comme filtres pour créer des segments Braze et les inclure dans les campagnes Braze ou Canvas. Visitez notre documentation de segment pour en savoir plus sur [comment créer des segments de Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment).

![Segment avec les Cohortes de Koubit]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="largeur-max-70%;"}

## Analyser les données de Braze dans Kubit (optionnel)
Profitez de [Snowflake sécurisé de partage de données]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/) pour partager votre campagne brute Braze et vos données d’impression avec Kubit pour les intégrer dans les analyses en libre-service de Kubit, vous fournissant une image complète du cycle de vie des utilisateurs.

Pour référence, voici tous les [champs Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2) qui sont disponibles pour être incorporés dans les analyses de Kubit. Les détails de cette étape sont très spécifiques au client et nécessitent des configurations spéciales. Veuillez parler à votre gestionnaire de comptes Kubit ou [support@kubit.ai](support@kubit.ai) pour en savoir plus.