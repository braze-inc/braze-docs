---
nav_title: Assistance technique en matière de protection des données
article_title: Assistance technique en matière de protection des données
page_order: 10
noindex: false
hide_nav: true

page_type: reference
description: "Cette page fournit des instructions techniques pour vous permettre de gérer, par le biais de la plateforme Braze, les demandes des personnes concernées en rapport avec leurs droits en matière de données à caractère personnel."
permalink: /dp-technical-assistance/
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Assistance technique en matière de protection des données

Ces dernières années, une série de nouvelles lois sur la protection des données ont été adoptées pour réglementer ce que les organisations peuvent faire avec les données à caractère personnel (**Lois sur la protection des données**), notamment le règlement général sur la protection des données de l’Union européenne (**RGPD**), la loi californienne sur la protection de la vie privée des consommateurs (**CCPA**) ainsi que des lois plus établies comme la loi sur la portabilité et la responsabilité de l’assurance maladie (**HIPAA**). Il existe d’autres lois et réglementations sur la protection des données au niveau national, régional et sectoriel qui peuvent s’appliquer à votre entreprise.

La plateforme Braze peut vous aider à vous conformer à ces lois sur la protection des données en fournissant des fonctionnalités techniques pour faciliter certaines actions requises par ces lois. Il appartient à chaque client de déterminer quelles lois sur la protection des données s’appliquent à son activité et d’agir en conformité avec ces lois. 

Ce document fournit des instructions techniques pour vous permettre de gérer, par le biais de la plateforme Braze, les demandes des personnes en rapport avec leurs droits sur les données à caractère personnel.

Aux fins du présent document, toute référence aux données à caractère personnel peut également être comprise comme une référence aux informations personnelles ou aux informations personnellement identifiables (**Données à caractère personnel**). Dans un souci de simplicité, nous nous appuyons sur la terminologie du RGPD pour expliquer les droits des utilisateurs finaux et la manière dont vous pouvez les mettre en œuvre. La terminologie du RGPD est souvent interchangeable ou étroitement alignée avec un terme ou un concept défini dans d’autres lois sur la protection des données. Par exemple, la section ci-dessous sur le « droit à l’effacement » peut être assimilée au « droit de suppression » prévu par la CCPA.  

## Avis juridique

Aucun des éléments suivants n’est destiné à constituer, ni ne doit être considéré comme un conseil juridique de Braze sur la manière de se conformer au RGPD, au CCPA ou aux lois applicables en matière de protection des données. Il vous est conseillé de demander l’avis de votre propre conseiller juridique en ce qui concerne votre situation particulière et la manière dont les lois sur la protection des données s’appliquent à vous et à votre utilisation des services Braze.

## Fondamentaux

La plupart des lois sur la protection de la vie privée définissent trois parties prenantes principales qui sont impliquées dans le traitement des données à caractère personnel : Personnes concernées, responsable du traitement des données, sous-traitants des données. Chaque groupe a des droits et des responsabilités différents concernant l’utilisation des données à caractère personnel :
- Une personne concernée est une personne dont les données à caractère personnel sont traitées par le sous-traitant des données ou le responsable du traitement.
- Un responsable du traitement des données est l’entité qui détermine les finalités et les moyens du traitement des données à caractère personnel
- Un sous-traitant des données est une entité qui traite les données à caractère personnel pour le compte et sur les instructions du responsable du traitement

En ce qui concerne la plateforme Braze :
- Les personnes concernées sont par exemple les utilisateurs finaux de votre application client (vos clients, par exemple) ou vos employés qui sont des utilisateurs du tableau de bord dans votre instance de la plateforme Braze. 
- Vous, en tant que client de Braze, êtes le responsable du traitement des données et décidez comment et pourquoi les données à caractère personnel des personnes concernées seront collectées et traitées.
- Braze est un sous-traitant des données qui traite les données à caractère personnel en votre nom et conformément aux instructions que nous recevons de votre part.

Les termes ci-dessus sont ceux du RGPD, mais, par exemple, les termes comparables dans le cadre du CCPA sont :
- « Consommateurs » pour les personnes concernées.
- « Entreprises » pour les responsables du traitement des données. 
- « Prestataires de services » pour les sous-traitants des données.

En tant que responsable du traitement des données, vous pouvez être tenu, en vertu des lois applicables sur la protection des données, de permettre aux personnes concernées d’exercer divers droits, chacun étant décrit plus en détail ci-dessous.

## Le droit d’être informé

Le droit d’être informé englobe votre obligation de fournir des « informations sur le traitement équitable », généralement par le biais d’un avis de confidentialité. Il souligne la nécessité d’une transparence sur la manière dont vous utilisez les données à caractère personnel.

### Recommandation de Braze
En vertu de certaines lois sur la protection des données, les clients de Braze, en tant que responsables du traitement des données, doivent permettre aux personnes concernées de comprendre comment ils traiteront les données à caractère personnel qu’ils collectent. De nombreux responsables du traitement des données s’acquittent de cette obligation en publiant un avis de confidentialité sur leur site Web. La plupart des lois sur la protection des données mettent l’accent sur la nécessité d’être transparent quant à la manière dont vous utilisez les données à caractère personnel. C’est la responsabilité du responsable du traitement des données. Par conséquent, vous devez fournir un avis de confidentialité qui soit facilement accessible aux utilisateurs de vos produits et services. En outre, votre avis de confidentialité doit également indiquer que vous pouvez partager des données à caractère personnel avec des tiers qui peuvent traiter ces données à caractère personnel en votre nom et fournir des informations suffisantes sur ce traitement afin que la personne concernée soit informée de ce que vous et vos sous-traitants des données ferez des données à caractère personnel.

## Le droit d’accès 

En vertu de certaines lois sur la protection des données, les personnes peuvent avoir le droit d’obtenir :
- la confirmation que leurs données à caractère personnel sont traitées ;
- l’accès à leurs données à caractère personnel ; et
- d’autres informations complémentaires, correspondant en grande partie aux informations qui devraient être fournies dans un avis de confidentialité.

### Recommandation de Braze

Les services Braze peuvent être configurés pour accéder à l’identifiant d’utilisateur d’un utilisateur final (défini par vous comme l’external_id fourni à Braze) et/ou à l’identifiant de son appareil. Vous pouvez utiliser l’un ou l’autre de ces identifiants pour exporter un profil d’utilisateur final contenant des données personnelles à partir des API [REST](https://www.braze.com/docs/api/endpoints/export/#user-export) de Braze et pour fournir ces données personnelles à une personne concernée en réponse à sa demande d’accès à toutes les données personnelles traitées par Braze en tant que responsable du traitement des données pour votre compte.

Par exemple, vous pouvez exporter l’[identifiant utilisateur](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-profile-lifecycle) ou l’identifiant d’appareil d’un utilisateur final, et votre équipe d’assistance peut alors effectuer un appel API (ou utiliser un système qui effectue des appels API) pour récupérer et fournir les données à caractère personnel stockées par Braze à une personne concernée donnée.

## Le droit de rectification

Les personnes ont le droit de faire corriger leurs données à caractère personnel si celles-ci sont inexactes ou incomplètes. Si vous avez divulgué les données à caractère personnel en question à des tiers, vous devez les informer de la rectification lorsque cela est possible.

### Recommandation de Braze

Dans le cas où une personne concernée vous demande de rectifier des inexactitudes dans les données personnelles traitées par vous ou par Braze en votre nom, vous pouvez utiliser les SDK de Braze ou les [API REST](https://www.braze.com/docs/api/endpoints/user_data/#user-track-endpoint) de Braze pour corriger ces données à caractère personnel.

## Le droit à l’effacement

Le droit à l’effacement est également connu sous le nom de « droit à l’oubli » ou « droit à la suppression ».

### Recommandation de Braze

Braze propose deux solutions pour arrêter le traitement supplémentaire des données par Braze :
- Les SDK de Braze permettent aux clients de désactiver toutes les opérations de Braze. Cela empêchera toutes les données d’être envoyées à Braze depuis ce site Web ou cette application. La documentation Braze fournit des instructions détaillées sur la manière de désactiver le SDK sur les pages de documentation spécifiques à la plateforme ([iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/), [Android](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) et [Web](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/initial_sdk_setup/)).
- Vous pouvez également recommander à votre utilisateur final de désinstaller ou de se déconnecter de toutes vos applications qui utilisent le SDK Braze.

Après avoir mis fin à la collecte de données, vous pouvez utiliser l’[endpoint de l’API REST de Braze de suppression d’utilisateurs](https://www.braze.com/docs/api/endpoints/user_data/#user-delete-endpoint) afin de supprimer un utilisateur final, ce qui supprimera tous les enregistrements de cet utilisateur final des services de Braze :
- Pour les utilisateurs finaux qui ont un `external_id` dans les services, vous pouvez utiliser cet ID pour supprimer les données de ces utilisateurs finaux.
- Pour les utilisateurs finaux anonymes qui n’ont pas d’external_id dans les services, vous pouvez récupérer l’identifiant de l’appareil de ces utilisateurs finaux à l’aide du kit SDK de Braze et utiliser cet identifiant pour trouver le profil de l’utilisateur final associé à cet appareil. Vous pouvez ensuite utiliser l’[API de suppression d’utilisateurs](https://www.braze.com/docs/api/endpoints/user_data/#user-delete-endpoint) pour supprimer le profil associé à cet utilisateur final.

La suppression d’un utilisateur final des services Braze entraînera la suppression _permanente_ du profil utilisateur centralisé de Braze pour cet utilisateur final, tel que défini par l’external_id fourni. Cela inclut toutes les données personnelles, y compris les informations de profil structurées, que Braze a collectées par défaut ou dont vous avez configuré la collecte par les services Braze, telles que les informations sur les appareils, le pays, la langue et l’e-mail. 

Notez que l’e-mail ou le numéro de téléphone associés au profil de l’utilisateur final peuvent toujours être stockés par Braze, car ils peuvent être associés au profil d’un autre utilisateur final. Les e-mails et les numéros de téléphone ne sont pas uniques dans les services Braze. Cela signifie que votre équipe pourrait avoir configuré Braze pour stocker le même e-mail ou le même numéro de téléphone avec plusieurs profils d’utilisateurs. Si votre équipe a configuré Braze de cette manière, sachez que vous devrez peut-être supprimer tous les profils d’utilisateurs qui représentent une certaine personne concernée afin de vous conformer à une demande de suppression émanant de cette personne concernée et votre équipe devra effectuer plusieurs appels API pour supprimer tous les profils d’utilisateurs qui font référence à une personne concernée particulière.

#### Analytique

Afin de maintenir l’intégrité des analyses d’utilisation des campagnes et des applications, les données agrégées anonymes ne seront pas modifiées lorsqu’un utilisateur final est supprimé. Par exemple, Braze ne réduira pas le nombre total de sessions d’une application lorsqu’un utilisateur final est supprimé. La ou les sessions au cours desquelles cet utilisateur final a visité l’application seront toujours incluses dans le nombre total de visites de cette application, mais ces données ne seront en aucun cas reliées au profil de l’utilisateur final oublié, ce qui garantit que ces données anonymes et agrégées ne peuvent pas être reliées à un utilisateur final individuel.

Les analyses effectuées dans le cadre des services Braze sont liées à l’identifiant de l’utilisateur final Braze. Une fois que le profil de l’utilisateur final a été supprimé, l’identifiant de l’utilisateur Braze devient alors un identifiant entièrement anonyme, car Braze ne peut plus le relier à un utilisateur final individuel.

#### Une fois que la suppression a eu lieu

On attend généralement de vous que vous fassiez des efforts raisonnables pour informer les personnes concernées que vous avez donné suite à leur demande d’effacement des données à caractère personnel.
Un utilisateur final supprimé peut se réinscrire ou réutiliser votre application ou service à une date ultérieure et Braze ne sera pas en mesure de l’identifier comme l’utilisateur supprimé ou oublié. Les services Braze ne sont pas en mesure de créer des listes d’identifiants d’utilisateurs ou d’e-mails supprimés au nom des clients. 

## Le droit à la limitation du traitement

Les personnes concernées peuvent avoir le droit de « bloquer » ou de supprimer le traitement de certains sous-ensembles de leurs données à caractère personnel si des données sont inexactes ou ont été obtenues de manière inappropriée. Lorsque le traitement est limité, vous êtes autorisé à conserver les données à caractère personnel, mais pas à les traiter ultérieurement. Vous pouvez conserver juste assez d’informations sur la personne pour garantir le respect de leur droit de limitation du traitement à l’avenir.

### Recommandation de Braze

Les services Braze ne prennent pas en charge la limitation du traitement de catégories individuelles de données à caractère personnel. Si une personne concernée vous a demandé de restreindre le traitement de certains sous-ensembles de ses données à caractère personnel, vous devez utiliser les [API de Braze](https://www.braze.com/docs/api/home/) pour exporter l’ensemble du ou des profils de cet utilisateur final, puis le [supprimer](https://www.braze.com/docs/api/endpoints/user_data/#user-delete-endpoint) de Braze. Les API de Braze peuvent être utilisées pour réimporter ces données dans le cas où l’utilisateur final vous autorise ultérieurement à traiter ces sous-ensembles particuliers de ses données à caractère personnel.

## Le droit à la portabilité des données

Le droit à la portabilité des données permet aux personnes concernées d’obtenir et de réutiliser leurs données à caractère personnel à leurs propres fins dans différents services. Les données à caractère personnel doivent être fournies dans un format structuré, lisible par machine et couramment utilisé. 

### Recommandation de Braze

Comme pour le droit d’accès, vous pouvez utiliser l’[API REST](https://www.braze.com/docs/api/endpoints/export/#user-export) de Braze pour exporter les données à caractère personnel d’un utilisateur final et les fournir à la personne concernée à sa demande.

## Le droit d’opposition

Les personnes peuvent avoir le droit de s’opposer au :
- traitement fondé sur des intérêts légitimes ou l’exécution d’une tâche d’intérêt public/exercice de l’autorité publique (y compris le profilage) ;
- marketing direct (y compris le profilage) ; et
- traitement à des fins de recherche scientifique/historique et de statistiques.

### Recommandation de Braze

Braze offre la possibilité de marquer un profil d’utilisateur comme étant désabonné des SMS, des e-mails ou des notifications push via nos [API REST](https://www.braze.com/docs/api/home/) et via les SDK [iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/), [Android](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) et [Web](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/). Si les personnes concernées s’opposent à la réception de tels messages, vous pouvez utiliser les API de Braze pour désinscrire ces utilisateurs finaux.

Si cela ne suffit pas, pour éviter le traitement des données personnelles de l’utilisateur final par Braze, le profil de l’utilisateur final doit être supprimé de la même manière que celle spécifiée dans le « droit à l’effacement ».

## Droits liés à la prise de décision automatisée et au profilage

Certaines lois sur la protection des données empêchent la prise de décision automatisée sans intervention humaine dans certaines circonstances, en particulier pour les décisions qui « produisent un effet juridique ou un effet significatif similaire sur la personne »."

### Recommandation de Braze

Braze n’effectue aucune action de profilage automatisé ou de prise de décision ayant des ramifications légales ou équivalentes pour les utilisateurs finaux. Si vous pensez que votre propre utilisation de la plateforme Braze aura des impacts légaux ou équivalents sur la base de votre propre utilisation et que vous avez reçu une objection à ce sujet, vous pouvez choisir de supprimer le profil utilisateur de la même manière que dans le cadre du « droit à l’effacement »."



