---
nav_title: Assistance technique pour la protection des données
article_title: Assistance technique pour la protection des données
page_order: 10
noindex: Faux
page_type: reference
description: "Cette page fournit des instructions techniques pour vous permettre de gérer, par le biais de la plateforme Braze, les demandes de personnes en relation avec leurs droits de données personnelles."
permalink: /dp-technical-assistance/
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Assistance technique pour la protection des données

Ces dernières années, il y a eu une série de nouvelles lois sur la protection des données qui réglementent ce que les organisations peuvent faire avec les données personnelles (__Loi sur la protection des données__), y compris le règlement général de l'Union européenne sur la protection des données (__RGPD__), la California Consumer Privacy Act (__CCPA__) ainsi que des lois plus établies telles que la Health Insurance Portability and Accountability Act (__HIPAA__). Il existe d'autres lois et réglementations nationales, nationales et sectorielles en matière de protection des données qui peuvent s'appliquer à votre entreprise.

La Plateforme Braze peut vous aider à respecter ces lois en matière de protection des données en fournissant des fonctionnalités techniques pour faciliter certaines actions requises en vertu de ces lois. Il appartient à chaque client de déterminer quelles lois sur la protection des données s'appliquent à son activité et d'agir en conformité avec celle-ci.

Ce document fournit des instructions techniques pour vous permettre de gérer, par le biais de la plateforme Braze, les demandes de personnes en relation avec leurs droits de données personnelles.

Aux fins de ce document, toute référence aux données personnelles peut également être comprise comme une référence à des informations personnelles ou à des informations personnelles identifiables (__Données à caractère personnel__). Dans un souci de simplicité, nous comptons sur le langage du RGPD pour expliquer les droits des utilisateurs finaux et comment vous pouvez les faciliter. Le langage du RGPD est souvent interchangeable ou étroitement aligné sur un terme ou un concept défini provenant d'autres lois sur la protection des données. Par exemple, la section ci-dessous sur « Le droit à la rareté » peut être assimilée au « droit à la suppression » en vertu de la LCPP.

## Avertissement légal

Aucune des propositions suivantes ne doit être ni considérée comme telle, ni comme telle, des conseils juridiques de Braze sur la façon de se conformer aux lois sur la protection des données du RGPD, de l’ACCP ou des lois applicables en matière de protection des données. Nous vous conseillons de demander l’avis de votre propre avocat en ce qui concerne votre situation particulière et la façon dont les lois sur la protection des données s’appliquent à vous et à votre utilisation des services de Braze.

## Les Bases

La plupart des lois sur la protection des renseignements personnels définissent trois principaux acteurs impliqués dans le traitement des données personnelles : les sujets de données, les contrôleurs de données et les traiteurs de données. Chaque groupe a des droits et des responsabilités différents en ce qui concerne l'utilisation des données personnelles:
- Un sujet de données est une personne dont les données personnelles sont traitées par le processeur ou le contrôleur de données
- Un contrôleur de données est l'entité qui détermine les buts et moyens du traitement des données personnelles
- Un processeur de données est une entité qui traite les données personnelles au nom et sur les instructions du contrôleur de données

En ce qui concerne la plateforme Braze :
- Les sujets de données sont par exemple les utilisateurs finaux de votre application client (par ex. vos clients/clients) ou vos employés qui sont des utilisateurs du tableau de bord dans votre instance de la plateforme Braze.
- Vous, le client de Braze, êtes le contrôleur de données qui décide comment et pourquoi les données personnelles des sujets seront collectées et traitées.
- Braze est un Data Processor qui traite les Données Personnelles en votre nom et conformément aux instructions que nous recevons de votre part.

Ce qui précède sont les termes du RGPD mais par exemple, les termes comparables de l’ACCP sont:
- « Consommateurs » pour les sujets de données.
- « Entreprises » pour les contrôleurs de données.
- « Fournisseurs de services » pour les processeurs de données.

En tant que contrôleur de données, vous pourriez être requis par les lois applicables sur la protection des données pour permettre aux sujets de données d'exercer de nombreux droits, chacune d'entre elles est décrite plus en détail ci-dessous.

## Le droit à l'information

Le droit d’être informé englobe votre obligation de fournir des « informations de traitement équitable », généralement par un avis de confidentialité. Il souligne le besoin de transparence sur la façon dont vous utilisez les données personnelles.

### Recommandation de Braze
En vertu de certaines lois sur la protection des données, les clients de Braze, en tant que contrôleurs de données, doit permettre aux sujets de données de comprendre comment ils traiteront les données personnelles qu'ils recueillent. De nombreux contrôleurs de données remplissent cette obligation par une déclaration de confidentialité sur leur site Web. La plupart des lois sur la protection des données mettent l'accent sur le besoin de transparence en ce qui concerne la façon dont vous utilisez les données personnelles. C'est la responsabilité du contrôleur de données. Par conséquent, vous devez conserver une déclaration de confidentialité facilement accessible aux utilisateurs de vos produits et services. En outre, votre déclaration de confidentialité devrait également divulguer que vous pouvez partager des données personnelles avec des tiers qui peuvent traiter ces données personnelles en votre nom, et fournir une divulgation suffisante à propos de ce traitement afin que le sujet des données soit informé de ce que vous et vos responsables de traitement de données allez faire avec les données personnelles.

## Le droit d'accès

En vertu de certaines lois sur la protection des données, les individus peuvent avoir le droit d'obtenir :
- Confirmation que leurs données personnelles sont en cours de traitement,
- Accès à leurs données personnelles, et
- Autres informations supplémentaires – ceci correspond en grande partie aux informations qui devraient être fournies dans un avis de confidentialité.

### Recommandation de Braze

Les Services de Braze peuvent être configurés pour accéder à l'identifiant d'utilisateur final (défini par vous comme external_id fourni au Brésil) et/ou l'identifiant du périphérique. Vous pouvez utiliser l'un de ces identifiants pour exporter un profil d'utilisateur final contenant des données personnelles provenant des [API REST de Braze](https://www.braze.com/docs/api/endpoints/export/#user-export), et de fournir ces Données à Caractère Personnel à un sujet de données en réponse à leur demande d'accès à toutes les Données Personnelles traitées par Braze en votre nom.

Par exemple, vous pouvez exporter l' [identifiant de l'utilisateur final](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-profile-lifecycle) ou l'identifiant de l'appareil, et votre équipe de support peut alors passer un appel API (ou utiliser un système qui fait des appels API) pour récupérer et fournir les données personnelles stockées par Braze à un sujet de données donné.

## Le droit à la rectification

Les personnes ont le droit de faire corriger leurs données personnelles si elles sont inexactes ou incomplètes. Si vous avez communiqué les Données à Caractère Personnel en question à des tiers, vous devez les informer de la rectification dans la mesure du possible.

### Recommandation de Braze

Dans le cas où un sujet de données vous demande de rectifier les inexactitudes au sein des Données à Caractère Personnel que vous ou Braze traitez en votre nom, vous pouvez utiliser les SDK Braze ou les [API Braze](https://www.braze.com/docs/api/endpoints/user_data/#user-track-endpoint) pour corriger de telles données personnelles.

## Le droit à l'éradication

Le droit à l’effacement est également connu sous le nom de «droit à l’oubli» ou de «droit à la suppression».

### Recommandation de Braze

Braze propose deux solutions pour empêcher le traitement supplémentaire des données par le Brésil :
- Les SDK de Braze permettent aux clients de désactiver toutes les opérations de Braze. Cela empêchera que toutes les données soient envoyées à Braze à partir de ce site Web ou de cette application. La documentation de Braze fournit des instructions détaillées sur la façon de désactiver le SDK sur les pages de documentation spécifiques à la plate-forme ([iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/), [Android](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/), et [Web](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/initial_sdk_setup/)).
- Alternativement, vous pouvez recommander que votre utilisateur final désinstalle ou se déconnecte de toutes vos applications qui utilisent le Braze SDK.

Une fois que vous avez arrêté la collecte de données, vous pouvez utiliser le [point de terminaison de l'API REST de suppression d'utilisateur](https://www.braze.com/docs/api/endpoints/user_data/#user-delete-endpoint) de Braze pour supprimer un utilisateur final, qui supprimera tous les enregistrements de cet utilisateur final des Services de Braze :
- Pour les utilisateurs qui ont un `external_id` dans les Services, vous pouvez utiliser cet ID pour supprimer les données de cet utilisateur final.
- Pour les utilisateurs anonymes qui n'ont pas d'external_id dans les services, vous pouvez récupérer l'identifiant du périphérique de cet utilisateur final en utilisant le SDK Braze et pouvez utiliser l'identifiant de l'appareil pour trouver le profil de l'utilisateur final associé à ce périphérique. Vous pouvez ensuite utiliser l'API de suppression d'utilisateur [](https://www.braze.com/docs/api/endpoints/user_data/#user-delete-endpoint) pour supprimer le profil associé à cet utilisateur final.

La suppression d’un utilisateur final des Services Braze supprimera _définitivement_ le profil utilisateur centralisé de Braze pour cet utilisateur final, tel que défini par l’external_id fourni. Ceci inclut toutes les données personnelles, y compris les informations de profil structurées, que Braze collecté par défaut ou que vous avez configuré les Services de Braze à collecter, tels que les informations sur l'appareil, le pays, la langue et l'adresse e-mail.

Notez que l'adresse e-mail ou le numéro de téléphone associé au profil de l'utilisateur final peuvent toujours être stockés par Braze, car ils pourraient être associés au profil d’un autre utilisateur final. Les adresses e-mail et les numéros de téléphone ne sont pas uniques dans les services de Braze. Cela signifie que votre équipe pourrait avoir configuré Braze pour stocker la même adresse e-mail ou le même numéro de téléphone sur plusieurs profils d'utilisateurs. Si votre équipe a configuré Braze de cette manière, soyez conscient que vous devrez peut-être supprimer tous les profils d'utilisateurs qui représentent un sujet de données donné afin de répondre à une demande de suppression d'un sujet de données, et votre équipe devrait faire plusieurs appels API pour supprimer tous les profils d'utilisateurs qui font référence à un sujet de données particulier.

#### Analyses

Afin de maintenir l’intégrité des analyses d’utilisation des campagnes et des applications, les données agrégées anonymes ne seront pas modifiées lorsqu’un utilisateur final est supprimé. Par exemple, Braze ne décrétera pas le nombre total de sessions d’une application lorsqu’un utilisateur final est supprimé. La (les) session(s) lorsque cet utilisateur final a visité l'application sera toujours incluse dans le nombre total de visites de cette application, mais ces données ne seront en aucun cas connectées au profil de l'utilisateur final oublié, s'assurer que ces données anonymes et agrégées ne peuvent pas être reliées à un utilisateur final individuel.

Les analytiques au sein des services de Braze sont liés à l'identifiant de l'utilisateur final de Braze. Une fois que le profil de l'utilisateur final a été supprimé, l'identifiant de l'utilisateur Braze devient effectivement un identifiant complètement anonyme, Parce que Braze est incapable de l'attacher à n'importe quel utilisateur final.

#### Une fois la suppression effectuée

Vous êtes généralement censé faire des efforts raisonnables pour informer les sujets de données lorsque vous avez répondu à leur demande d'effacer leurs données personnelles. Un utilisateur final supprimé peut se réinscrire ou se réengager avec votre application ou votre service à une date ultérieure et Braze ne pourra pas les identifier comme l'utilisateur supprimé ou oublié. Les Services Braze ne sont pas en mesure de créer des listes d’identifiants d’utilisateur ou d’adresses e-mail supprimés pour le compte de clients.

## Le droit à la restriction du traitement

Les sujets de données peuvent avoir le droit de « bloquer » ou de supprimer le traitement de certains sous-ensembles de leurs données personnelles en cas de données inexactes ou mal obtenues. Lorsque le traitement est restreint, vous êtes autorisé à stocker les données personnelles, mais pas à les traiter. Vous pouvez conserver juste suffisamment d'informations sur l'individu pour vous assurer que la restriction est respectée à l'avenir.

### Recommandation de Braze

Les Services de Braze ne supportent pas la restriction du traitement de certaines catégories de données personnelles. Si un sujet de données vous a demandé de restreindre le traitement de certains sous-ensembles des données personnelles de ce sujet, vous devriez utiliser les API [Braze](https://www.braze.com/docs/api/basics/) pour exporter le profil complet de cet utilisateur et ensuite [le supprimer](https://www.braze.com/docs/api/endpoints/user_data/#user-delete-endpoint) de Braze. Les API de Braze peuvent être utilisées pour réimporter ces données dans le cas où l'utilisateur final vous autorise par la suite à traiter ces sous-ensembles particuliers de ses données personnelles.

## La portabilité du droit aux données

Le droit à la portabilité des données permet aux sujets de données d'obtenir et de réutiliser leurs données personnelles à leurs propres fins à travers différents services. Les données personnelles doivent être fournies dans un format structuré, lisible par les machines et couramment utilisé.

### Recommandation de Braze

Similaire au droit d’accès, vous pouvez utiliser la [REST API](https://www.braze.com/docs/api/endpoints/export/#user-export) de Braze pour exporter les données personnelles d'un utilisateur final et les fournir au sujet des données conformément à leur demande.

## Le droit à l'objet

Les personnes peuvent avoir le droit de s'opposer à :
- traitement basé sur des intérêts légitimes ou sur l'exécution d'une tâche dans l'intérêt public/l'exercice de l'autorité officielle (y compris le profilage);
- le marketing direct (y compris le profilage) ; et
- traitement à des fins de recherche et de statistiques scientifiques/historiques.

### Recommandation de Braze

Braze fournit la possibilité de marquer un profil utilisateur comme désabonné de SMS, e-mails ou notifications push via nos [API REST](https://www.braze.com/docs/api/basics/) et via le [iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/), [Android](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/), et [SDK Web](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/). Si vous recevez des objections de Data Subjects à la réception de tels messages, vous pouvez utiliser les API de Braze pour désabonner ces utilisateurs.

Si ce n'est pas suffisant, pour éviter le traitement des données personnelles de l'utilisateur final par Brésil, le profil de l’utilisateur final doit être supprimé de la même manière que celle spécifiée dans le ‘Droit à la rare’.

## Droits relatifs à la prise de décision automatisée et au profilage

Certaines lois sur la protection des données empêchent la prise de décision automatisée sans intervention humaine dans certaines circonstances, en particulier pour les décisions qui « produisent un effet juridique ou un effet tout aussi significatif sur l’individu. »

### Recommandation de Braze

Braze n'effectue aucune action de profilage ou de prise de décision automatique avec des ramifications légales ou équivalentes pour les utilisateurs finaux. Si vous pensez que votre propre utilisation de la plateforme Braze aura des impacts légaux ou équivalents en fonction de votre propre utilisation et que vous avez reçu une objection à ceci, vous pouvez choisir de supprimer le profil d'utilisateur de la même manière que dans le cadre du "droit à la rare".



