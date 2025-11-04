---
nav_title: Kubit
article_title: Kubit
description: "Cet article de référence présente le partenariat entre Braze et Kubit, une plateforme d'analyse/analytique en libre-service sans code qui fournit des informations instantanées sur les produits, vous permettant d'importer des cohortes d'utilisateurs Kubit et de les cibler dans l'envoi de messages de Braze."
alias: /partners/kubit/
page_type: partner
search_tag: Partner

---

# Kubit

> [Kubit](https://kubit.ai/) est une plateforme d'analyse en libre-service sans code qui fournit des informations instantanées sur les produits. 

L'intégration Braze et Kubit vous permet d'[importer des cohortes d'utilisateurs Kubit]({{site.baseurl}}/partners/data_and_analytics/cohort_import/kubit/) et de les cibler dans l'envoi de messages Braze. En outre, grâce à l'utilisation du [partage de données sécurisé Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/), vous pouvez intégrer les données brutes de campagne et d'impression de Braze à l'analyse/analytique produit de Kubit pour mesurer l'impact de ces campagnes en temps réel. Cette approche fournit des informations sur le cycle de vie complet de vos utilisateurs sans nécessiter d'efforts d'ingénierie.

## Conditions préalables

| Condition | Description |
|---|---|
|Compte entreprise Kubit | Un compte d'entreprise Kubit est nécessaire pour profiter de ce partenariat. |
| Mise en correspondance des ID des utilisateurs | Les données de vos clients dans Kubit et Braze doivent avoir des ID d'utilisateur correspondants sur les deux plateformes. Cela inclut également les UUID anonymes. Consultez notre [documentation]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android) pour savoir comment Braze définit les ID des utilisateurs. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Analyser les données de Braze dans Kubit

Profitez du [partage de données sécurisé Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) pour partager vos données brutes de campagne et d'impression Braze avec Kubit afin de les intégrer aux analyses en libre-service de Kubit, vous offrant ainsi une image complète du cycle de vie des utilisateurs.

Pour référence, voici tous les [champs Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2) qui sont disponibles pour être incorporés dans l'analyse/analytique de Kubit. Les détails de cette étape sont très spécifiques au client et nécessitent des configurations particulières. Pour en savoir plus, adressez-vous à votre gestionnaire de compte Kubit ou à [support@kubit.ai](support@kubit.ai).