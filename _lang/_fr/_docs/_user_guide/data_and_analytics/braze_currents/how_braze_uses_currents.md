---
nav_title: Comment Braze utilise les courants
article_title: Comment Braze utilise les courants
page_order: 6
page_type: tutoriel
description: "Cet article en cours vous guidera à travers le processus de base pour mettre en place des apports appropriés pour les données de l'événement, en plus de le déplacer dans une base de données et un outil BI."
tool: Courants
---

# Comment Braze utilise les courants

> Braze utilise le courant! C'est vrai, nous aimons assez notre propre produit pour l'utiliser en conjonction avec quelques-uns de nos [partenaires]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/).

Nous filtrons nos données à partir de nos e-mails et poussons des campagnes dans un outil de vision d'entreprise, Looker, mais cela prend une route intéressante pour y arriver. Nous utilisons une version légèrement inversée de la méthodologie ETL (Extract, Transform, Load) - nous venons de passer à ELT (Extract, Load, Transform)!

## Étape 1 : Données d'admission et d'agrégation des événements

Après avoir lancé des campagnes en utilisant l'un de nos outils d'engagement (comme des campagnes ou Canvas), Nous surveillons les données de nos événements en utilisant notre propre système ainsi que certaines de nos partenaires e-mail. Certaines de ces données sont agrégées et affichées dans le tableau de bord, mais nous étions intéressés à plonger plus profondément !

## Étape 2 : Envoyer les données de l'événement à un partenaire de stockage de données

Nous avons mis en place des Monnaies pour envoyer des données d'événement Braze à Amazon S3 pour le stockage et l'extraction. Maintenant, nous savons que vous pouvez utiliser [Athena][2] pour vous asseoir sur S3 et exécuter des requêtes. C'est une excellente solution à court terme. Mais nous avons voulu (et vous recommander) une solution à long terme à l'aide d'une base de données relationnelle et d'un outil d'intelligence commerciale/analytique.

Nous considérons le S3 comme nos clés du château! Il ouvre la porte à tant de possibilités de déplacement, de pivot et d’analyse de nos données en les transférant là où nous en avons besoin. Cependant, nous veillons à ne pas transformer nos données en S3, car nous avons une structure très spécifique pour elle.

## Étape 3 : Transformer les données de l'événement avec une base de données relationnelle

À partir de S3, nous choisissons un entrepôt ([Snowflake](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE), dans notre cas). Nous le transformons là, puis le déplacons vers Looker, où nous avons des blocs mis en place qui vont structurer et organiser nos données.

Le flocon de neige n'est pas votre seule option d'entreposage. Vous pouvez également choisir [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE), et plus encore !

## Étape 4 : Utilisez un outil de BI pour manipuler vos données

Enfin, nous utilisons un outil de BI pour analyser nos données, les transformer en graphiques et autres outils visuels et plus en utilisant les [Looker et Looker Blocks](https://looker.com/platform/blocks/directory?utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct#braze) pour que nous n'ayons pas à ETL/ELT les données chaque fois qu'il bouge de Courant.

Consultez la documentation ci-dessous pour obtenir plus d'informations à ce sujet et comment vous pouvez les utiliser pour construire votre base de données!

- [Bloc de comportement de l'utilisateur](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [Bloc d'engagement de message](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)




[2]: https://aws.amazon.com/athena/
