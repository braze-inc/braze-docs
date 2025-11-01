---
nav_title: Comment Braze Currents utilise les courants
article_title: Comment Braze Currents utilise les courants
page_order: 6
page_type: tutorial
description: "Cet article pratique de Currents vous guidera dans le processus de base pour la mise en place d'une collecte appropriée des données d'événements, ainsi que pour leur transfert dans une base de données et un outil d'aide à la décision (BI)."
tool: Currents
 
---

# Comment Braze Currents utilise les courants

> Braze utilise les Currents ! C'est vrai, nous aimons suffisamment notre propre produit pour l'utiliser avec quelques-uns de [nos partenaires.]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/)

Nous filtrons nos données issues de nos campagnes d'e-mail et de push dans un outil d'informations commerciales, Looker, mais il faut emprunter un chemin intéressant pour y parvenir. Nous utilisons une version légèrement inversée de la méthodologie Extraire, Transformer, Charger (ETL) - nous changeons simplement l'ordre en Extraire, Charger, Transformer (ELT) !

## Étape 1 : Données d'admission et données agrégées sur les événements

Après avoir lancé des campagnes à l'aide de l'un de nos outils d'engagement (comme les campagnes ou Canvas), nous suivons les données de l'événement à l'aide de notre propre système ainsi que de certains de nos partenaires en matière d'e-mail. Certaines de ces données sont agrégées et présentées dans le tableau de bord, mais nous souhaitons aller plus loin !

## Étape 2 : Envoi de données d'événements à un partenaire de stockage de données

Nous avons configuré Braze Currents pour qu'il envoie les données d'événements de Braze à Amazon S3 à des fins de stockage et d'extraction. Nous savons maintenant que vous pouvez utiliser [Athena](https://aws.amazon.com/athena/) pour vous asseoir au-dessus de S3 et exécuter des requêtes. C'est une excellente solution à court terme. Mais nous voulions une solution à long terme utilisant une base de données relationnelle et un outil d'aide à l'analyse/analyse (Business Intelligence/Analytique). (Nous vous recommandons de faire de même).

Nous considérons le S3 comme les clés du château ! Il ouvre la porte à tant de possibilités pour déplacer, pivoter et analyser nos données en les transférant là où nous avons besoin qu'elles aillent. Cependant, nous veillons à ne pas transformer nos données dans S3, car nous avons une structure très spécifique pour celles-ci.

## Étape 3 : Transformer les données d'événements avec une base de données relationnelle

Depuis S3, nous choisissons un entrepôt[(Partage de données](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) ou Comptes de lecteurs Snowflake, dans notre cas). Nous les transformons là, puis nous les déplaçons vers Looker, où nous avons mis en place des blocs qui vont structurer et organiser nos données.

Snowflake n'est pas la seule option d'entrepôt. Parmi les autres options, citons [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE) et bien d'autres encore !

### Comptes des lecteurs de Snowflake

Les comptes de lecteur Snowflake offrent aux utilisateurs un accès aux mêmes données et fonctionnalités que le [partage de données Snowflake]({{site.baseurl}}/partners/snowflake/), le tout sans nécessiter de compte Snowflake ou de relation client avec Snowflake. Avec les comptes de lecteur, Braze créera et partagera vos données dans un compte et vous fournira des identifiants pour vous connecter et accéder à vos données. Ainsi, le partage des données et la facturation de l'utilisation seront entièrement pris en charge par Braze. 

Pour en savoir plus, contactez votre gestionnaire de satisfaction client.

#### Ressources complémentaires
Pour des ressources utiles sur le contrôle de l'utilisation, consultez les articles de Snowflake sur le [contrôle des ressources](https://docs.snowflake.com/en/user-guide/resource-monitors.html) et la [visualisation de l'utilisation des crédits de l'entrepôt](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account).

## Étape 4 : Utiliser un outil d'aide à la décision (BI) pour manipuler vos données.

Enfin, nous utilisons un outil de BI pour analyser nos données, les transformer en graphiques et autres outils visuels, et plus encore en utilisant Looker [et Looker Blocks](https://www.marketplace.looker.com/) pour ne pas avoir à extraire ou à ELT les données à chaque fois qu'elles sont transférées de Currents.

Vous avez envie de faire de même ? Consultez les documentations suivantes pour obtenir plus d'informations sur ces derniers et sur la façon dont vous pouvez les utiliser pour créer votre base de données !

- [Bloc comportement de l'utilisateur](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [Bloc d'envoi des messages](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)

