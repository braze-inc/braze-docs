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

> [Kubit](https://kubit.ai/) est une plate-forme d'analyse en libre service sans code qui fournit des aperçus instantanés sur les produits. Par le biais de l'intégration transparente sans code avec Braze, vous pouvez importer des informations Cohort utilisateur dans Braze et lancer des campagnes d'engagement pour cibler des cohortes spécifiques. En outre, en utilisant [Snowflake Secure Data Sharing]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/), vous pouvez intégrer les données de la campagne brute et des impressions de Braze à l'analyse des produits dans Kubit pour mesurer l'impact de ces campagnes en temps réel. Cette approche fournit des informations sur le cycle de vie complet de vos utilisateurs, sans nécessiter aucun effort d'ingénierie.

## Exigences

* __Kubit Enterprise__ - La fonctionnalité d'intégration de Braze n'est disponible que pour les clients Kubit Entreprise.
* __Braze Data Import Key et REST Endpoint__ - Cette intégration appelle le Braze [/users/track endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour fonctionner. Ces appels seront comptés dans vos limites d'API [Braze]({{site.baseurl}}/api/basics/#api-limits).
* __Les identifiants d'utilisateur correspondants__ - Vos données clients dans Kubit et Braze doivent avoir des identifiants d'utilisateur correspondants pour cette intégration afin de faire correspondre les clients entre les deux plateformes. Cela inclut les UUID anonymes. Pour savoir comment Braze définit les identifiants d'utilisateur, visitez notre documentation [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/).

## Intégration de Braze et Kubit
### Étape 1 : Générer une clé d'importation de données Braze
À partir du tableau de bord de Braze, accédez à __Partenaires technologiques__ et sélectionnez __Kubit__.

Ici, vous trouverez le point de terminaison REST et générez votre clé d'importation de données de Braze. Une fois généré, vous serez en mesure de créer une nouvelle clé ou d'invalider une clé existante si nécessaire. La clé d'importation de données et le point d'extrémité REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord de Kubits.

![Configuration sur Kubit]({% image_buster /assets/img/kubit/kubit.png %}){: style="largeur-max:90%;"}

### Étape 2 : Configurer Kubit
Fournir la clé d'importation de données de Braze et le point de terminaison de Braze REST trouvé à l'étape 1.

![Configuration sur Kubit]({% image_buster /assets/img/kubit/config_on_kubit.png %}){: style="largeur-max:30%;"}

### Étape 3 : Importer des cohortes à Braze
1. __Créez une Cohorte en Kubit__<br> Créez une Cohorte en Kubit et définissez les critères des utilisateurs cibles.<br><br>![Create a Cohort]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}<br><br>
2. __Importer des utilisateurs à Braze__<br> Une fois que vous avez enregistré une Cohorte en Kubit, vous pouvez importer ces utilisateurs à Braze pour être utilisé dans Braze Segments pour envoyer des courriels ou des notifications push à travers l'utilisation de campagnes ou de Canvases.<br><br>![Import to Braze]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}<br><br>Il y a deux modes de calendrier d'importation :<br>- **Importation à usage unique** : Importer une fois.<br>- **Importation planifiée** : Importation quotidienne, hebdomadaire ou mensuelle à une heure spécifique. <br><br>![Import Schedule]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}<br><br>Notez que chaque cohorte ne peut avoir qu'un seul planning d'importation en direct.<br><br>
3. __Verify Import Status__<br> Une fois l'importation terminée, une notification par e-mail sera envoyée au ou aux destinataires spécifiés dans le calendrier d'importation. Vous pouvez également vérifier l'état d'import d'une Cohorte sous Schedule dans Kubit. L'historique des horaires affichera toutes les heures d'exécution de l'importation, les résultats et le nombre total d'utilisateurs de la Cohorte qui ont été importés au Brésil.<br><br>![Import History]({% image_buster /assets/img/kubit/import_history.png %})<br><br>Vous pouvez déclencher manuellement une importation en cliquant sur l'icône Import to Braze pour ce planning d'importation.

### Étape 4 : Créer des segments de Braze avec des cohortes de Kubit
Une fois que les cohortes sont importées au Brésil, vous pouvez les utiliser comme filtres pour créer des Segments Braze et les inclure dans les campagnes Braze ou Canvas. Visitez notre documentation de segment pour en savoir plus sur [comment créer des segments de Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment).

![Segment avec les Cohortes de Koubit]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="largeur-max-70%;"}

### Étape 5 : Analyser les données de Braze dans Kubit (optionnel)
Vous pouvez également profiter de [Snowflake Secure Data Sharing]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/) pour partager votre campagne brute de Braze et vos données d’impression avec Kubit pour les intégrer dans les Analyses de libre-service de Kubit et vous fournir une image complète du cycle de vie des utilisateurs, de l'attribution au comportement à l'engagement.

Pour les références, voici toutes les [tables Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2) qui sont disponibles pour être intégrées dans les analyses de Kubit. Les détails de cette étape sont très spécifiques au client et nécessitent des configurations spéciales. Veuillez parler à votre gestionnaire de comptes Kubit ou support@kubit.ai pour en savoir plus.