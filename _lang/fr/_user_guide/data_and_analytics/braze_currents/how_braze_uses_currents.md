---
nav_title: Comment Braze utilise Currents
article_title: Comment Braze utilise Currents
page_order: 6
page_type: tutorial
description: "Cet article « How to » sur Currents vous guidera dans le processus de base pour configurer les intakes appropriés pour les données d’événements, et pour les déplacer vers une base de données et un outil BI."
tool: Currents
 
---

# Comment Braze utilise Currents

> Braze utilise Currents ! C’est exact, nous aimons tant notre propre produit que nous l’utilisons conjointement avec quelques-uns [nos partenaires]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/).

Nous filtrons les données de nos campagnes de notification push et d’e-mail dans Looker, un outil de visualisation de données, et le chemin qu’elles prennent pour y arriver est intéressant. Nous utilisons une version légèrement différente de la méthodologie ETL (Extract, Transform, Load) - nous avons changé l’ordre et nous faisons de l’ELT (Extract, Load, Transform) !

## Étape 1 : Intake et agrégation des Données d’événements

Après avoir lancé des campagnes à l’aide de l’un de nos outils d’engagement (comme les Campagnes ou Canvas), nous suivons les données d’événements avec notre propre système et avec certains de nos partenaires d’e-mail. Certaines de ces données sont agrégées et affichées dans le tableau de bord, mais nous voulions creuser plus profond !

## Étape 2 : Envoi des données d’événement à un partenaire de stockage de données

Nous avons configuré Currents pour envoyer les données d’événements Braze à Amazon S3 pour stockage et extraction. Nous savons bien sûr qu’on peut utiliser [Athena][2] avec S3 pour lancer des requêtes. C’est une excellente solution à court terme. Mais nous voulions (et nous vous recommandons) une solution à long terme utilisant une base de données relationnelle et un outil analytique d’aide à la décision.

Pour nous, S3 est « la clé du château » ! Il nous ouvre la porte à tant de possibilités pour déplacer, pivoter et analyser nos données, en les transférant là où nous en avons besoin. Cependant, nous faisons attention à ne pas transformer nos données dans S3, car nous avons une structure très spécifique.

## Étape 3 : Transformer les données d’événements avec une base de données relationnelle

Depuis S3, nous choisissons un entrepôt ([Partage de données Snowflake](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) ou Comptes Lecture Snowflake dans notre cas). Nous les transformons sur place puis nous les déplaçons vers Looker, où nous avons des blocs pour structurer et organiser nos données.

Snowflake n’est pas votre seule option pour l’entreposage. Vous pouvez également choisir [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery ](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE)et d’autres encore !

### Comptes Lecture Snowflake

Les comptes Lecture Snowflake donnent accès aux utilisateurs aux mêmes données et fonctionnalités que le [Snowflake Data Sharing]({{site.baseurl}}/partners/snowflake/) (Partage de données Snowflake), sans nécessiter de compte ou de relation client avec Snowflake. Avec les comptes Lecture, Braze créera et partagera vos données dans un compte et vous donnera les identifiants pour vous connecter et accéder à vos données. Tous les partages et facturations de données seront alors gérés intégralement par Braze. 

Contactez votre gestionnaire du succès des clients pour en savoir plus.

**Ressources complémentaires**<br>
Pour obtenir des ressources de surveillance d’utilisation utiles, consultez les articles [Dispositif de surveillance de ressources](https://docs.snowflake.com/en/user-guide/resource-monitors.html) et [Afficher l’utilisation de crédits de l’entrepôt](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account) de Snowflake.

## Étape 4 : Utilisez un outil BI pour manipuler vos données

Enfin, nous utilisons un outil BI pour analyser nos données, les transformer en graphiques et autres outils visuels, en utilisant [Blocs Looker et Looker](https://www.marketplace.looker.com/) donc nous n’avons pas à faire d’ETL (ou d’ELT) sur les données à chaque fois qu’elles arrivent de Currents.

Consultez les documents suivants pour obtenir plus d’informations et voir comment vous pouvez les utiliser pour construire votre base de données !

- [Bloc de Comportement Utilisateur](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [Bloc d’Engagement Message](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)

[2]: https://aws.amazon.com/athena/
