---
nav_title: Assistance technique en matière de protection des données
article_title: Assistance technique en matière de protection des données dans les services de Braze
page_order: 1
description: "Cette page fournit des instructions techniques pour vous permettre de gérer, par le biais des services Braze, les demandes des personnes en ce qui concerne leurs droits en matière de données à caractère personnel."
alias: /help/dp-technical-assistance/
permalink: /dp-technical-assistance/
hide_toc: true
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Assistance technique en matière de protection des données dans les services de Braze

Il existe une gamme de lois sur la protection des données qui régissent ce que les organisations peuvent faire avec les données personnelles (« Lois sur la protection des données »), y compris le Règlement général sur la protection des données de l'UE et du Royaume-Uni (« RGPD »), la California Consumer Privacy Act (« CCPA ») et la Health Insurance Portability and Accountability Act (« HIPAA »). Il existe d’autres lois et réglementations sur la protection des données au niveau national, régional et sectoriel qui peuvent s’appliquer à votre entreprise.

Ces lois sur la protection des données accordent aux individus des « droits à la vie privée » sur leurs données personnelles. Les organisations sont tenues de recevoir et de répondre aux demandes des individus qui exercent leurs droits à la vie privée. Les services Braze peuvent vous aider à vous conformer à ces lois sur la protection des données en fournissant des fonctionnalités qui facilitent certaines actions requises par ces lois. Ce document fournit des instructions techniques pour utiliser ces fonctionnalités afin de gérer les demandes de droits de confidentialité. Il vous appartient de déterminer quelles lois sur la protection des données s'appliquent à votre entreprise et d'agir en conformité avec elles.

## Avis juridique

Aucune des informations suivantes n'est destinée à être, ni ne doit être considérée comme, un conseil juridique de la part de Braze. Il vous est conseillé de demander l’avis de votre propre conseiller juridique en ce qui concerne votre situation particulière et la manière dont les lois sur la protection des données s’appliquent à vous et à votre utilisation des services Braze.

## Terminologie

Aux fins du présent document, toute référence aux données personnelles peut également être comprise comme une référence aux informations personnelles ou aux informations personnellement identifiables (« Données Personnelles »). Pour des raisons de simplicité, nous nous appuyons généralement sur le langage du RGPD lorsque nous abordons les droits des utilisateurs finaux. La terminologie du RGPD est souvent interchangeable ou étroitement alignée avec un terme ou un concept défini dans d’autres lois sur la protection des données.

## Fondamentaux

La plupart des lois sur la confidentialité définissent trois principales parties prenantes impliquées dans le traitement des données personnelles : les personnes concernées, les responsables du traitement et les sous-traitants. Chaque groupe a des droits et des responsabilités différents concernant l’utilisation des données à caractère personnel :

- Une personne concernée est une personne dont les données à caractère personnel sont traitées par le sous-traitant des données ou le responsable du traitement
- Un responsable du traitement des données est une entité qui détermine les finalités et les moyens du traitement des données personnelles
- Un processeur de données est une entité qui traite les données personnelles pour le compte et selon les instructions du responsable du traitement des données

En ce qui concerne les services de Braze :

- Les personnes concernées sont, par exemple, les utilisateurs finaux de votre application client (e.g., vos clients) ou vos employés qui sont des utilisateurs de tableau de bord dans votre instance des services Braze.
- Vous, le client de Braze, êtes le responsable du traitement des données qui décide comment et pourquoi les Données à caractère personnel des personnes concernées seront collectées et traitées dans le cadre des Services de Braze.
- Braze est un sous-traitant de données qui traite les données à caractère personnel dans les services de Braze en votre nom et conformément aux instructions que nous recevons de votre part.

Les termes ci-dessus sont ceux du RGPD, mais, par exemple, les termes comparables dans le cadre du CCPA sont :

- « consommateurs » pour les personnes concernées par les données.
- « entreprises » pour les responsables du traitement des données.
- « fournisseurs de services » pour les processeurs de données.

Vous trouverez ci-dessous des informations pertinentes sur les demandes de droits à la confidentialité des données les plus courantes émanant des personnes concernées, y compris la manière dont vous pouvez y répondre par le biais des fonctionnalités techniques du service Braze.

## Le droit d’être informé

Le droit d’être informé englobe votre obligation de fournir des « informations sur le traitement équitable », généralement par le biais d’un avis de confidentialité. Il souligne la nécessité d’une transparence sur la manière dont vous utilisez les données à caractère personnel.

### Recommandation de Braze

La plupart des lois sur la protection des données mettent l'accent sur la nécessité de la transparence en ce qui concerne l'utilisation des données personnelles. C'est la responsabilité des responsables du traitement des données, qui maintiendront généralement un avis de confidentialité facilement accessible aux utilisateurs de leurs produits et services et couvrant le traitement effectué par Braze.

## Le droit d’accès

En vertu des lois sur la protection des données, les personnes concernées peuvent avoir le droit d'obtenir :

- la confirmation que leurs données à caractère personnel sont traitées ;
- l’accès à leurs données à caractère personnel ; et
- Autres informations supplémentaires déterminées par la loi applicable sur la protection des données.

### Recommandation de Braze

Afin de fournir des données personnelles de Braze dans un format lisible par machine en réponse à une demande d'accès de la part d’une personne concernée, vous pouvez exporter son profil d'utilisateur final en faisant un appel API aux [API REST](https://www.braze.com/docs/api/endpoints/export/#user-export) de Braze avec soit son identifiant utilisateur (défini par vous comme l’`external_id` fourni à Braze) et/ou son identifiant d’appareil.

## Le droit de rectification

Les personnes ont le droit de faire corriger leurs données à caractère personnel si celles-ci sont inexactes ou incomplètes. Si vous avez divulgué les données personnelles en question à des tiers, vous pouvez envisager la nécessité de les informer de la rectification si possible.

### Recommandation de Braze

Dans le cas où une personne concernée vous demande de rectifier les inexactitudes des données personnelles traitées par vous ou par Braze en votre nom, vous pouvez utiliser les SDK Braze ou les [API REST](https://www.braze.com/docs/api/endpoints/user_data/#user-track-endpoint) de Braze pour corriger ces données personnelles.

## Le droit à l’effacement

Le droit à l’effacement est également connu sous le nom de « droit à l’oubli » ou « droit à la suppression ».

### Recommandation de Braze

#### Suppression standard 

Une fois que vous avez arrêté la collecte des données, vous pouvez utiliser [le point de terminaison de l'API REST de suppression d'utilisateur de](https://www.braze.com/docs/api/endpoints/user_data/post_user_delete/) Braze pour supprimer un utilisateur final, ce qui supprimera tous les enregistrements de cet utilisateur final dans les services de Braze :

- Pour les utilisateurs finaux qui disposent d'un ID externe dans les services Braze, vous pouvez utiliser cet ID pour supprimer les données de cet utilisateur final.
- Pour les utilisateurs finaux anonymes qui n'ont pas d'identifiant externe dans les services Braze, vous pouvez récupérer l'identifiant de l'appareil de cet utilisateur final à l'aide du SDK Braze et utiliser l'identifiant de l'appareil pour trouver le profil de l'utilisateur final associé à cet appareil. Vous pouvez ensuite utiliser l'API de suppression d'utilisateurs pour supprimer le profil associé à cet utilisateur final.

La suppression d'un utilisateur final des services Braze supprimera définitivement le profil utilisateur centralisé de Braze pour cet utilisateur final tel que défini par le `external_id` fourni. Cela inclut les informations de profil structurées que Braze a collectées par défaut ou que vous avez configuré les services Braze pour collecter, telles que les informations sur l'appareil, le pays, la langue et l'adresse e-mail.

Notez que l'adresse e-mail ou le numéro de téléphone associé au profil de l'utilisateur final pourrait toujours être stocké par Braze, car ils pourraient être associés à un autre profil d'utilisateur final. Les e-mails et les numéros de téléphone ne sont pas uniques dans les services Braze. Cela signifie que votre équipe pourrait avoir configuré Braze pour stocker le même e-mail ou le même numéro de téléphone avec plusieurs profils d’utilisateurs. Si votre équipe a configuré Braze de cette manière, sachez que vous devrez peut-être supprimer tous les profils utilisateur qui représentent un sujet de données donné afin de vous conformer à une demande de suppression d'un sujet de données, et votre équipe devra passer plusieurs appels API pour supprimer tous les profils utilisateur qui se réfèrent à un sujet de données particulier.

#### Considérations supplémentaires sur la suppression

<style>
#considerations td {
    word-break: break-word;
    width: 100%;
    font-size: 16px;
}
</style>

<table id="considerations">
<tbody>
  <tr>
    <td>
        <p>Les clients peuvent créer des champs personnalisés pour les propriétés des événements et les extras des messages. Ces champs ne sont pas destinés aux données personnelles, par conséquent, ces champs ne sont pas inclus dans le processus de suppression par défaut décrit ci-dessus. Si, cependant, vous utilisez Braze pour saisir ou collecter des données personnelles via les propriétés d'événement et les suppléments de message, vous pouvez configurer le processus de suppression déclenché par l’endpoint d'API REST de suppression d'utilisateurs pour inclure également ces champs, afin que les données contenues dans ces champs soient également supprimées.</p>
        <p>Les paramètres par défaut sont appliqués au niveau de l'entreprise, mais vous pouvez choisir de supprimer les champs suivants lorsque le processus de suppression s'exécute, au niveau du groupe d'applications/espace de travail :</p>
    <ul>
        <li>PROPRIÉTÉS pour UTILISATEURS_COMPORTEMENTS_ÉVÉNEMENTPERSONNALISÉ</li>
        <li>PROPRIÉTÉS pour USERS_BEHAVIORS_PURCHASE</li>
        <li>MESSAGE_EXTRAS pour:</li>
            <ul>
            <li>CONTENU DE LA CARTE DES MESSAGES DES UTILISATEURS</li>
            <li>USERS_MESSAGES_EMAIL_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_RETRYSEND_SHARED</li>
            <li>ENVOYER_MESSAGES_UTILISATEURS_WEBHOOK</li>
            <li>UTILISATEURS_MESSAGES_SMS_ENVOYER</li>
            <li>Événements d'envoi de messages futurs</li>
            </ul>
    </ul>
    <p>Les paramètres de ceci peuvent être accessibles via <b>Paramètres de l'entreprise</b> > <b>Paramètres d'administration</b> > <b>Paramètres de sécurité</b>. Les préférences de suppression des données sont définies par type d'événement ou catégorie. Seul un utilisateur avec des préférences d'administrateur peut apporter des modifications à ces paramètres. Alternativement, un administrateur peut déléguer ces autorisations à un autre utilisateur.</p>
    <p>Si un type d'événement ou un message supplémentaire est configuré pour être inclus dans le processus de suppression, les données de ce champ seront supprimées à l'avenir pour les utilisateurs pour lesquels vous exécutez un point de terminaison de l'API REST de suppression d'utilisateur. De plus, lorsque vous sélectionnez cette préférence de suppression, lors du prochain travail de suppression planifié, les données de ces champs seront supprimées de tout ensemble de données anonymisées existant contenant ces champs. La restauration des champs de données supprimés ne sera pas possible.</p>
    </td>
  </tr>
</tbody>
</table>

#### Analyse

Afin de maintenir l’intégrité des analyses d’utilisation des campagnes et des applications, les données agrégées anonymes ne seront pas modifiées lorsqu’un utilisateur final est supprimé. Par exemple, Braze ne réduira pas le nombre total de sessions d’une application lorsqu’un utilisateur final est supprimé. La ou les sessions au cours desquelles cet utilisateur final a visité l’application seront toujours incluses dans le nombre total de visites de cette application, mais ces données ne seront en aucun cas reliées au profil de l’utilisateur final oublié, ce qui garantit que ces données anonymes et agrégées ne peuvent pas être reliées à un utilisateur final individuel.

Les analyses effectuées dans le cadre des services Braze sont liées à l’identifiant de l’utilisateur final Braze. Après la suppression du profil de l'utilisateur final, l'identifiant utilisateur Braze devient effectivement un identifiant complètement anonymisé, car Braze ne peut pas le relier à un utilisateur final individuel.

#### Après la suppression

Vous êtes généralement censé faire des efforts raisonnables pour informer les personnes concernées lorsque vous avez satisfait à leur demande d'effacement de leurs données personnelles. Un utilisateur final supprimé peut se réinscrire ou se réengager avec votre application ou service à une date ultérieure, et Braze ne pourra pas les identifier comme l'utilisateur supprimé ou oublié. Les services Braze ne sont pas en mesure de créer des listes d'identifiants d'utilisateurs supprimés ou d'adresses e-mail en votre nom.

## Le droit à la limitation du traitement

Les personnes concernées peuvent avoir le droit de « bloquer » ou de supprimer le traitement de leurs données personnelles dans certaines circonstances. La restriction du traitement signifie ne pas effectuer de traitement auquel une personne concernée s'est opposée.

### Recommandation de Braze

Les services Braze ne prennent pas en charge la limitation du traitement de catégories individuelles de données à caractère personnel. Si une personne concernée vous a demandé de restreindre le traitement de certains sous-ensembles de ses données personnelles, vous devez utiliser les [API Braze](https://www.braze.com/docs/api/home/) pour exporter l'ensemble du profil de cet utilisateur final, puis [supprimer](https://www.braze.com/docs/api/endpoints/user_data/#user-delete-endpoint) celui-ci de Braze. Les API de Braze peuvent être utilisées pour réimporter ces données dans le cas où l’utilisateur final vous autorise ultérieurement à traiter ces sous-ensembles particuliers de ses données à caractère personnel. De plus, vous devriez recommander à votre utilisateur final de désinstaller ou de se déconnecter de toutes vos applications qui utilisent le SDK Braze pour arrêter de collecter des données supplémentaires sur la personne concernée.

## Le droit à la portabilité des données

Le droit à la portabilité des données permet aux personnes concernées d'obtenir et de réutiliser leurs données personnelles à leurs propres fins sur différents services. Les données à caractère personnel doivent être fournies dans un format structuré, lisible par machine et couramment utilisé.

### Recommandation de Braze

Similaire au droit d'accès, vous pouvez utiliser l'[API REST](https://www.braze.com/docs/api/endpoints/export/#user-export) de Braze pour exporter les données personnelles d'un utilisateur final et les fournir à la personne concernée conformément à sa demande.

## Le droit d’opposition

Les personnes peuvent avoir le droit de s’opposer au :

- traitement fondé sur des intérêts légitimes ou l’exécution d’une tâche d’intérêt public/exercice de l’autorité publique (y compris le profilage) ;
- marketing direct (y compris le profilage) ; et
- traitement à des fins de recherche scientifique/historique et de statistiques.

### Recommandation de Braze

Braze offre la possibilité de marquer un profil utilisateur comme étant désabonné des SMS, e-mails ou notifications push via nos [API REST](https://www.braze.com/docs/api/home/) et via les SDK [iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/), [Android](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) et [Web](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/). Si les personnes concernées s’opposent à la réception de tels messages, vous pouvez utiliser les API de Braze pour désinscrire ces utilisateurs finaux.

Si cela ne suffit pas, pour éviter le traitement des données personnelles de l’utilisateur final par Braze, le profil de l’utilisateur final doit être supprimé de la même manière que celle spécifiée dans le « Droit à l’effacement ».

## Droits liés à la prise de décision automatisée et au profilage

Certaines lois sur la protection des données empêchent, ou permettent aux personnes concernées de refuser, la prise de décision automatisée ou le profilage dans certaines circonstances, en particulier pour les décisions qui « produisent un effet juridique ou un effet similaire significatif sur l'individu. »

### Recommandation de Braze

Braze ne réalise aucune action de profilage ou de prise de décision automatisée ayant des conséquences juridiques ou équivalentes pour les personnes concernées. Si vous estimez que votre propre utilisation des services de Braze aura des répercussions juridiques ou équivalentes et que vous avez reçu une objection à ce sujet, vous pouvez choisir de supprimer le profil utilisateur de la même manière que dans le cadre du "Droit à l'effacement".

## Publicité ciblée

En vertu de certaines lois sur la confidentialité des États-Unis, les personnes concernées peuvent s'opposer à l'utilisation de leurs données personnelles à des fins de publicité ciblée.

### Recommandation de Braze

Lors de la création d'audiences dans le but de cibler des publicités vers vos personnes concernées, vous devez vous assurer d'avoir exclu toute personne concernée qui s'est opposée à la publicité ciblée, par exemple, les consommateurs californiens qui ont exercé leur droit de « Ne pas vendre ou partager » en vertu du CCPA.

Pour plus d'informations sur la façon de créer des audiences à synchroniser avec des plateformes tierces, consultez la rubrique [Synchronisation de l’audience](https://www.braze.com/docs/partners/canvas_steps).

## Le droit à la non-discrimination 

Les personnes concernées ont le droit d'exercer leurs droits en matière de protection de la vie privée sans discrimination.

### Recommandation de Braze

Dans leur utilisation des services Braze, les clients doivent s'assurer qu'ils ne commettent pas de discrimination envers les personnes concernées qui ont exercé leurs droits en matière de protection de la vie privée. Par exemple, nous recommandons que les personnes concernées qui ont exercé leurs droits à la vie privée ne soient pas segmentées en audiences ou autrement ciblées de manière à les discriminer.