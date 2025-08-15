---
nav_title: Segment
article_title: Segment
page_order: 1
alias: /partners/segment/
description: "Cet article de référence décrit le partenariat entre Braze et Segment, une plateforme de données clients qui collecte et achemine des informations entre les sources de votre pile marketing."
page_type: partner
search_tag: Partner

---

# Segment

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment][5] est une plateforme de données clients qui vous aide à collecter, nettoyer et activer vos données clients. 

L'intégration de Braze et Segment vous permet de suivre vos utilisateurs et d'acheminer les données vers différents fournisseurs d'analyse des utilisateurs. Le segment vous permet de :

- Synchronisez [Segment Engage avec]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_engage/) Braze pour une utilisation dans la campagne Braze et la segmentation de Canvas.
- [Importez des données entre les deux plateformes](#integration-options). Nous proposons une intégration côte à côte SDK pour vos applications Android, iOS et web, ainsi qu'une intégration serveur à serveur pour la synchronisation de vos données avec les API REST de Braze
- [Connectez les données à Segment par le biais de Currents]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/). 

## Prérequis

| Condition | Description |
| ----------- | ----------- |
| Compte Segment | Un [compte Segment](https://app.segment.com/login) est nécessaire pour bénéficier de ce partenariat. |
| [Bibliothèques](https://segment.com/docs/sources/) sources et Segment installées | L'origine de toutes les données envoyées à Segment, telles que les applications mobiles, les sites Web ou les serveurs principaux.<br><br>Vous devez installer les bibliothèques dans votre application, votre site ou votre serveur pour configurer correctement un flux `Source > Destination`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Pour intégrer Braze et Segment, vous devez définir [Braze comme destination conformément au type d'](#connection-settings)[intégration que vous avez choisi](#integration-options) (mode de connexion). [Si vous êtes un nouveau client de Braze, vous pouvez transmettre des données historiques à Braze à l'aide de rediffusions segmentées.](#segment-replays) Ensuite, vous devez configurer [des mappages](#methods) et [tester votre intégration](#step-4-test-your-integration) pour garantir un flux de données fluide entre Braze et Segment.

### Étape 1 : Créez une destination Braze {#connection-settings}

Après avoir configuré vos sources avec succès, vous devrez configurer Braze comme [destination](https://segment.com/docs/destinations/) pour chaque source (iOS, Android, Web, etc.). Vous disposerez de nombreuses options pour personnaliser le flux de données entre Braze et Segment à l'aide des paramètres de connexion.

### Étape 2 : Choisissez le framework de destination et le type de connexion {#integration-options}

Dans Segmentation, naviguez vers **Destinations** > **Braze** > **Configurer Braze** > **Sélectionnez votre source** > Configuration.

![La page de configuration de la source. Cette page inclut des paramètres permettant de définir le cadre de destination comme « actions » ou « classique » et de définir le mode de connexion comme « mode cloud » ou « mode appareil ».][42]

Vous pouvez intégrer la source Web (Analytics.js) et les bibliothèques natives côté client de Segment à Braze à l'aide d'une intégration côte à côte (mode appareil) ou d'une intégration serveur à serveur (mode cloud).

Votre choix de mode de connexion sera déterminé par le type de source pour lequel la destination est configurée.

| Intégration | Détails |
| ----------- | ------- |
| [Côte à côte<br>(mode appareil)](#side-by-side-sdk-integration) |Utilise le SDK de Segment pour traduire les événements en appels natifs de Braze, ce qui permet d'accéder à des fonctionnalités plus profondes et à une utilisation plus complète de Braze que l'intégration de serveur à serveur.<br><br>Notez que Segment ne prend pas en charge toutes les méthodes Braze (par exemple, les cartes de contenu). Pour utiliser une méthode Braze qui n'est pas mappée via un mappage correspondant, vous devrez invoquer la méthode en ajoutant du code Braze natif à votre base de code. |
| [Serveur à serveur<br>(mode cloud)](#server-to-server-integration) | Transfère les données du segment aux endpoints de l'API Braze REST.<br><br>Ne prend pas en charge les fonctionnalités de l'interface utilisateur de Braze telles que l'envoi de messages intégrés à l'application, les cartes de contenu ou les notifications push. Il existe également des données capturées automatiquement, telles que des champs au niveau de l'appareil, qui ne sont pas disponibles par cette méthode.<br><br>Envisagez une intégration côte à côte si vous souhaitez utiliser ces fonctionnalités.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Consultez [Segment](https://segment.com/docs/destinations/#connection-modes) pour en savoir plus sur les deux options d'intégration (modes de connexion), y compris les avantages de chacune d'entre elles.
{% endalert %}

#### Intégration du SDK côte à côte

Également appelée mode appareil, cette intégration associe le SDK et les méthodes de Segment au SDK Braze, ce qui permet d'accéder [à](#methods) toutes les fonctionnalités fournies par notre SDK, telles que le push, l'envoi de messages intégrés à l'application et d'autres méthodes natives de Braze. 

{% alert note %}
Lorsque vous utilisez le mode appareil de Segment, vous n'avez pas besoin d'intégrer directement le SDK Braze. Lors de l'ajout de Braze en tant que destination en mode appareil pour Segment, le SDK Segment initialise le SDK Braze et appelle les méthodes Braze mappées pertinentes.
{% endalert %}

Lorsque vous utilisez une connexion en mode appareil, comme si vous intégriez le SDK Braze de manière native, le SDK Braze attribuera un identifiant `device_id` et un identifiant de backend `braze_id` à chaque utilisateur. Cela permet à Braze de capturer l'activité anonyme de l'appareil en faisant correspondre ces identifiants plutôt que `userId`. 

{% tabs local %}
{% tab Android %}

{% alert important %}
Le code source pour l'intégration du mode appareil Android est géré par Braze et est mis à jour régulièrement pour refléter les nouvelles versions du SDK Braze.

<br>
Le SDK Braze que vous utilisez dépend de votre SDK Segment :

| | SDK Segment | SDK Braze |
| - | ----------- | --------- |
| Préféré | [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| Legacy | [Analytics-Android](https://github.com/segmentio/analytics-android) | [Braze Segment Android](https://github.com/braze-inc/braze-segment-android) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endalert %}

Pour configurer Braze comme destination en mode appareil pour votre source Android, choisissez **Actions** comme **cadre de destination**, puis sélectionnez **Enregistrer.** 

[Pour terminer l'intégration côte à côte, consultez les instructions détaillées de Segment pour ajouter la dépendance de destination Braze à votre application Android](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/).

Le code source pour l'intégration du [mode appareil Android](https://github.com/braze-inc/braze-segment-kotlin) est maintenu par Braze et est mis à jour régulièrement pour refléter les nouvelles versions du SDK Braze.

{% endtab %}
{% tab iOS %}

{% alert important %}
Le code source pour l'intégration du mode appareil iOS est géré par Braze et est mis à jour régulièrement pour refléter les nouvelles versions du SDK Braze.

<br>
Le SDK Braze que vous utilisez dépend de votre SDK Segment :

| | SDK Segment | SDK Braze |
| - | ----------- | --------- |
| Préféré | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze Segment Swift](https://github.com/braze-inc/braze-segment-swift) |
| Legacy | [Analytics-iOS](https://github.com/segmentio/analytics-ios) | [Braze Segment iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endalert %}

Pour configurer Braze comme destination en mode appareil pour votre source iOS, choisissez **Actions** comme **cadre de destination**, puis sélectionnez **Enregistrer.** 

Pour terminer l'intégration côte à côte, consultez les instructions détaillées de Segment pour ajouter le module Braze Segment à votre application[iOS](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/).

Le code source pour l'intégration du [mode appareil iOS](https://github.com/braze-inc/braze-segment-swift) est géré par Braze et est mis à jour régulièrement pour refléter les nouvelles versions du SDK Braze.

{% endtab %}
{% tab Web ou JavaScript %}

Le cadre Braze Web Mode (Actions) de Segment est recommandé pour configurer Braze en tant que destination en mode appareil pour votre source Web. 

Dans Segmentation, sélectionnez **Actions** comme cadre de destination et **Mode appareil** comme mode de connexion.

![]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
Le code source du [plugin React Native Braze](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze) est maintenu par Segment et est mis à jour régulièrement pour refléter les nouvelles versions du SDK Braze.

Lorsque vous connectez une source de segment React Native à Braze, vous devez configurer une source et une destination par système d'exploitation. Par exemple, vous devez configurer une destination iOS et une destination Android. 

Dans la base de code de votre application, initialisez de manière conditionnelle le SDK Segment par type d'appareil, à l'aide de la clé d'écriture source associée à chaque application.

Lorsqu'un jeton de notification push est enregistré depuis un appareil et envoyé à Braze, il est associé à l'identifiant de l'application utilisé lors de l'initialisation du SDK. L'initialisation conditionnelle du type d'appareil permet de confirmer que tous les jetons push envoyés à Braze sont associés à l'application concernée.

{% alert important %}
Si l'application React Native initialise Braze avec le même identifiant d'application Braze pour tous les appareils, tous les utilisateurs de React Native seront considérés comme des utilisateurs Android ou iOS dans Braze, et tous les jetons push seront associés à ce système d'exploitation.
{% endalert %}

Pour configurer Braze comme destination en mode appareil pour chaque source, choisissez **Actions** comme **cadre de destination**, puis sélectionnez **Enregistrer.**

{% endtab %}
{% endtabs %}

#### intégration de serveur à serveur

Également appelée mode cloud, cette intégration transmet les données de Segment aux API REST de Braze. Utilisez le cadre [Braze Cloud Mode (Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) de Segment pour configurer une destination en mode cloud pour n'importe laquelle de vos sources. 

Contrairement à l'intégration côte à côte, l'intégration serveur à serveur ne prend pas en charge les fonctionnalités de Braze UI, telles que les messages in-app, les cartes de contenu ou l'enregistrement automatique des jetons push. Il existe également des données [capturées automatiquement]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection) (telles que des utilisateurs anonymes et des champs au niveau de l'appareil) qui ne sont pas disponibles via le mode cloud.

Si vous souhaitez utiliser ces données et ces fonctionnalités, pensez à utiliser le SDK d'intégration côte à côte (mode appareil).

Le code source de la [destination Braze Cloud Mode (Actions)](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze) est géré par Segment.

### Étape 3 : Paramètres

Définissez les paramètres de votre destination. Les paramètres ne s'appliqueront pas du tout à tous les types de destinations.

{% tabs local %}
{% tab Mode appareil mobile %}

| Réglage | Descriptif |
| ------- | ----------- |
| Identifiant de l'application | L'identifiant de l'application utilisé pour référencer l'application spécifique. Il figure dans le tableau de bord de Braze, sous **Gérer les paramètres**. | 
| endpoint d'API personnalisé<br>(endpoint du SDK) | Votre endpoint du SDK Braze qui correspond à votre instance (tel que `sdk.iad-01.braze.com`) | 
| Région de l'endpoint | Votre instance Braze (telle que US 01, US 02, EU 01, etc.) | 
| Activer l'enregistrement automatique des messages in-app | Désactivez cette option si vous souhaitez enregistrer manuellement les messages intégrés à l'application. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Mode appareil Web %}

| Réglage | Descriptif |
| ------- | ----------- |
| Identifiant de l'application | L'identifiant de l'application utilisé pour référencer l'application spécifique. Il figure dans le tableau de bord de Braze, sous **Gérer les paramètres**. | 
| endpoint d'API personnalisé<br>(endpoint du SDK) | Votre endpoint du SDK Braze qui correspond à votre instance (tel que `sdk.iad-01.braze.com`) | 
| ID push du site Safari | Si vous prenez en charge les notifications push Safari, vous devez spécifier cette option à l'aide de l'ID de notification push du site Web que vous avez fourni à Apple lors de la création de votre certificat de notification push Safari (qui commence par`web`, par exemple,`web.com.example.domain`). |
| Version du SDK Web de Braze | La version du SDK Web Braze que vous souhaitez utiliser |
| Envoyer automatiquement des messages intégrés à l'application | Par défaut, tous les messages intégrés à l'application auxquels un utilisateur est éligible sont automatiquement envoyés à l'utilisateur. Désactivez cette option si vous souhaitez afficher manuellement les messages intégrés à l'application. |
| Ne chargez pas la police Awesome | Braze utilise Font Awesome pour les icônes de message in-app. Par défaut, Braze chargera automatiquement FontAwesome à partir du réseau de diffusion de contenu FontAwesome. Pour désactiver ce comportement (par exemple, parce que votre site utilise une version personnalisée de FontAwesome), définissez cette option sur. `TRUE` Notez que dans ce cas, vous êtes responsable de vous assurer que FontAwesome est chargé sur votre site. Sinon, les messages intégrés à l'application risquent de ne pas s'afficher correctement. |
| Activer les messages HTML intégrés à l'application | L'activation de cette option permettra aux utilisateurs du tableau de bord de Braze d'utiliser des messages HTML intégrés à l'application. | 
| Ouvrez les messages intégrés à l'application dans un nouvel onglet | Par défaut, les liens provenant de clics sur un message in-app sont chargés dans l'onglet actuel ou dans un nouvel onglet, comme indiqué dans le tableau de bord, message par message. Définissez cette option pour `TRUE` forcer l'ouverture dans un nouvel onglet ou une nouvelle fenêtre de tous les liens contenus dans les messages in-app. |
| Index Z des messages intégrés à l'application | Indiquez une valeur pour cette option afin de remplacer les indices z par défaut de Braze. | 
| Exiger le rejet explicite des messages in-app | Par défaut, lorsqu'un message in-app s'affiche, le message peut être supprimé en appuyant sur la touche Échap ou en cliquant sur l'arrière-plan grisé de la page. Définissez cette option sur true pour empêcher ce comportement et exiger un clic explicite sur un bouton pour ignorer les messages. |
| Intervalle minimal entre les actions du déclencheur en secondes | La valeur par défaut est 30.<br>Par défaut, une action de déclenchement ne se déclenche que si au moins 30 secondes se sont écoulées depuis la dernière action de déclenchement. Entrez une valeur pour cette option de configuration afin de remplacer cette valeur par défaut par une valeur qui vous est propre. Nous vous déconseillons de définir cette valeur en dessous de 10 pour éviter de spammer l'utilisateur avec des notifications.|
| Emplacement du service de traitement | Par défaut, lors de l'enregistrement des utilisateurs pour les notifications push Web, Braze recherche le fichier de service de traitement requis dans le répertoire racine de votre serveur Web à l'adresse. `/service-worker.js` Si vous souhaitez héberger votre service de traitement sur un autre chemin sur ce serveur, indiquez une valeur pour cette option qui est le chemin absolu vers le fichier. (Par exemple,`/mycustompath/my-worker.js`). Notez que définir une valeur ici limite la portée des notifications push sur votre site. Par exemple, dans l'exemple ci-dessus, étant donné que le fichier du service de traitement se trouve dans le répertoire `/mycustompath/`, `requestPushPermission` ne peut être appelé qu'à partir de pages Web commençant par `http://yoursite.com/mycustompath/`. |
| Désactiver la maintenance des jetons push | Par défaut, les utilisateurs qui ont déjà accordé l'autorisation Web Push synchroniseront automatiquement leur jeton push avec le backend Braze lors des nouvelles sessions afin de garantir la livrabilité. Pour désactiver ce comportement, définissez cette option sur`FALSE`. |
| Gérer le service de traitement de manière externe | Si vous avez votre propre service de traitement dont vous enregistrez et contrôlez le cycle de vie, définissez cette option sur`TRUE`, et le SDK Braze n'enregistrera pas ou n'annulera pas l'enregistrement d'un service de traitement. Si vous attribuez la valeur `TRUE` à cette option, vous devez enregistrer vous-même le service de traitement avant d'appeler `requestPushPermission` et vous assurer qu'il contient le code du service de traitement de Braze, soit à l'aide de `self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');`, soit en incluant directement le contenu de ce fichier. Lorsque cette option est définie sur `TRUE`, l’option `serviceWorkerLocation` est ignorée. |
| Sécurité du contenu : nonce | Si vous indiquez une valeur pour cette option, le SDK Braze ajoutera le nonce à tous les `<script>` et éléments `<style>` créés par le SDK. Cela permet au SDK Braze de fonctionner avec la politique de sécurité du contenu de votre site Web. En plus de définir ce nonce, vous devrez peut-être également autoriser le chargement de FontAwesome, ce que vous pouvez faire en ajoutant `use.fontawesome.com` à la liste d'autorisation de votre politique de sécurité du contenu ou en utilisant l'option `doNotLoadFontAwesome` et en la chargeant manuellement. |
| Autoriser l'activité des robots d'exploration | Par défaut, le SDK Web de Braze ignore l'activité des robots ou robots d'exploration connus, tels que Google, en fonction de la chaîne de caractères de l'agent utilisateur. Cela permet d'économiser des points de données, de rendre l'analyse plus précise et peut améliorer le classement des pages. Toutefois, si vous souhaitez que Braze enregistre plutôt l'activité de ces robots d'exploration, vous pouvez définir cette option sur. `TRUE` |
| Activer la journalisation | Définissez sur `TRUE` pour activer la journalisation par défaut. Notez que cela obligera Braze à se connecter à la console JavaScript, qui est visible à tous les utilisateurs. Avant de publier votre page dans l’environnement de production, vous devez la supprimer ou fournir un autre enregistreur avec le paramètre `setLogger`. |
| Ouvrez les cartes du fil d'actualité dans un nouvel onglet (ouvrez les cartes dans un nouvel onglet) | Par défaut, les liens des objets de la carte sont chargés dans l'onglet ou la fenêtre en cours. Définissez cette option `TRUE` pour que les liens des cartes s'ouvrent dans un nouvel onglet ou une nouvelle fenêtre. <br><br>**Remarque :** Le fil d'actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus. |
| Autoriser le JavaScript fourni par l'utilisateur | Par défaut, le SDK Web de Braze n'autorise pas les actions de clic JavaScript fournies par l'utilisateur, car il permet aux utilisateurs du tableau de bord de Braze d'exécuter JavaScript sur votre site. Pour indiquer que vous faites confiance aux utilisateurs du tableau de bord de Braze pour écrire des actions de clic JavaScript non malveillantes, définissez cette propriété sur. `TRUE` Si la paramètre `enableHtmlInAppMessages` est défini sur `TRUE`, cette option sera également définie sur`TRUE`. |
| Version de l'application| Si vous fournissez une valeur pour cette option, les événements utilisateur envoyés à Braze seront associés à la version donnée, qui peut être utilisée pour la segmentation des utilisateurs. |
| Délai d'expiration de la session en secondes | La valeur par défaut est 30.<br>Par défaut, les sessions expirent après 30 minutes d'inactivité. Entrez une valeur pour cette option de configuration afin de remplacer cette valeur par défaut par une valeur qui vous est propre. | 
| Liste autorisée des propriétés de l'appareil | Par défaut, le SDK Braze détecte et collecte automatiquement toutes les propriétés de l'appareil `DeviceProperties`. Pour modifier ce comportement, fournissez un tableau de `DeviceProperties`. Notez que sans certaines propriétés, toutes les fonctionnalités ne fonctionneront pas correctement. Par exemple, la distribution dans le fuseau horaire local ne fonctionnera pas sans le fuseau horaire. |
| Localisation | Par défaut, tous les messages visibles par l'utilisateur générés par le SDK seront affichés dans la langue du navigateur de l'utilisateur. Entrez une valeur pour cette option afin de modifier ce comportement et de forcer l'utilisation d'une langue spécifique. La valeur de cette option doit être un code de langue ISO 639-1. |
| Pas de cookies | Par défaut, le SDK de Braze stocke de petites quantités de données (identifiants d'utilisateur, identifiants de session) dans des cookies. Ceci est fait pour permettre à Braze de reconnaître les utilisateurs et les sessions dans les différents sous-domaines de votre site. Si cela vous pose un problème, transmettez la valeur `TRUE` pour cette option avin de désactiver le stockage des cookies et utilisez entièrement HTML 5 localStorage pour identifier les utilisateurs et les sessions. |
| Suivez toutes les pages | **Mode périphérique Web de destination classique (maintenance) uniquement**<br><br>Segment recommande de migrer vers la destination du framework Web Actions où ce paramètre peut être [activé via des mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Cela enverra tous les [appels de page](https://segment.com/docs/spec/page/) à Braze sous la forme d'un événement « Page chargée/consultée ». |
| Suivre uniquement les pages nommées | **Mode périphérique Web de destination classique (maintenance) uniquement**<br><br>Segment recommande de migrer vers la destination du framework Web Actions où ce paramètre peut être [activé via des mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Cela enverra uniquement les appels de page à Braze avec un nom qui leur est associé. |
| Consignez l’achat lorsque le chiffre d'affaires est présent | **Mode périphérique Web de destination classique (maintenance) uniquement**<br><br>Segment recommande de migrer vers la destination du framework Web Actions où ce paramètre peut être [activé via des mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Lorsque cette option est activée, tous les appels Track avec la propriété du chiffre d'affaires déclencheront un événement d'achat. | 
| Suivez uniquement les utilisateurs connus | **Mode périphérique Web de destination classique (maintenance) uniquement**<br><br>Segment recommande de migrer vers la destination Web Actions Framework où ce paramètre peut être activé via des mappages.<br><br>S'il est activé, ce nouveau paramètre retarde l'appel de `window.appboy.initialize` jusqu'à ce qu'il y ait un appel `userId` valide. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Mode cloud %}

| Réglage | Descriptif |
| ------- | ----------- |
| Identifiant de l'application | L'identifiant de l'application utilisé pour référencer l'application spécifique. Il figure dans le tableau de bord de Braze, sous **Gérer les paramètres**. | 
| Clé d'API REST | Vous pouvez la trouver dans le tableau de bord de Braze sous **Paramètres > Clés** **API**. | 
| Endpoint de l'API REST personnalisé | Votre endpoint REST Braze qui correspond à votre instance (par exemple rest.iad-01.braze.com). | 
| Mettre à jour les utilisateurs existants uniquement | **Mode cloud de destination classique (maintenance) uniquement**<br><br>Segment recommande de migrer vers la destination Cloud Actions Framework où ce paramètre peut être [activé via des mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Détermine s'il faut uniquement mettre à jour les utilisateurs existants. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Étape 4 : Méthodes de mappage {#methods}

Braze prend en charge les méthodes [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page), [Identify](https://segment.com/docs/spec/identify/) et [Track](https://segment.com/docs/spec/track/) Segment. Les types d'identificateurs utilisés dans le cadre de ces méthodes varient selon que les données sont envoyées via une intégration de serveur à serveur (mode cloud) ou côte à côte (mode appareil). Dans les destinations Braze Web Mode Actions et Cloud Mode Actions, vous pouvez également choisir de configurer un mappage pour un appel d'alias de [segment](https://segment.com/docs/connections/spec/alias/). 

{% alert note %}
Bien que les alias d'utilisateur soient pris en charge en tant qu'identifiant dans la destination Braze Cloud Mode (Actions), il convient de noter que l'appel d'alias de Segment n'est pas directement lié aux alias utilisateur Braze.
{% endalert %}

| Type d'identifiant | Destination prise en charge |
| --------------- | --------------------- |
| `userId` (`external_id`) | Tous |
| Utilisateur anonyme | Destinations en mode appareil |
| Alias d'utilisateur | Destinations en mode cloud |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

La destination du mode cloud (Actions) propose une [action Créer un alias](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias) qui peut être utilisée pour créer un utilisateur uniquement avec un alias ou pour ajouter un alias à un profil existant`external_id`. L'[action Identifier l'utilisateur](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user) peut être utilisée conjointement à l'action Créer un alias pour fusionner un utilisateur uniquement avec un alias une `external_id` fois que celui-ci est devenu disponible pour l'utilisateur. 

Il est également possible de concevoir une solution de contournement et d'utiliser `braze_id` pour envoyer des données utilisateur anonymes en mode cloud. Cela nécessite d'inclure manuellement le nom de l'utilisateur `braze_id` dans tous vos appels d'API Segment. Pour en savoir plus sur la configuration de cette solution de contournement, consultez la [documentation de Segment](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users).

Les données de destination envoyées à Braze peuvent être regroupées par lots dans Cloud Mode Actions. La taille des lots est limitée à 75 événements, et ces lots s'accumuleront sur une période de 30 secondes avant d'être vidés. Le traitement par lots des requêtes est effectué par action. Par exemple, Identifier les appels (attributs) sera groupé dans une requête et Suivre les appels (événements personnalisés) sera groupé dans une deuxième requête. Braze recommande d'activer cette fonctionnalité car elle réduira le nombre de requêtes envoyées de Segment à Braze. Cela réduira à son tour le risque que la destination atteigne les limites de débit de Braze et tente à nouveau les requêtes. 

**Vous pouvez activer le traitement par lots pour une action en accédant à Braze Destination > Mappages**. À partir de là, cliquez sur l'icône à 3 points à droite du mappage et sélectionnez **Modifier** le mappage. Faites défiler la section **Select mappings** vers le bas et assurez-vous que l’option **Envoyer les données à Braze par lots** est définir sur **Oui**.


{% tabs local %}
{% tab Identifier %}
#### Identifier

L'appel [Identify](https://segment.com/docs/spec/identify/) vous permet de lier un utilisateur à ses actions et d'enregistrer les attributs le concernant. 

Certaines caractéristiques spéciales de segment correspondent à des champs de profil d'attributs standard dans Braze :

| Caractéristiques du segment spécial | Attributs standard de Braze |
| ------------- | ----------- |
| `userId` | `external_id` |
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `email` | `email` |
| `birthday` | `dob` |
| `address.country` | `country` |
| `address.city` | `home_city` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

D'autres champs de profil Braze réservés tels que `email_subscribe` et `push_subscribe` peuvent être envoyés en utilisant la convention de dénomination Braze pour ces champs et en les transmettant en tant que traits dans un appel d'identification.

##### Ajouter un utilisateur à un groupe d'abonnement

Vous pouvez également vous abonner ou vous désabonner d'un utilisateur d'un groupe d'abonnement donné à l'aide des champs suivants du paramètre traits.

Utilisez le champ de profil Braze réservé appelé`braze_subscription_groups`, qui peut être associé à un tableau d'objets. Chaque objet du tableau doit avoir deux clés réservées :

1. `subscription_group_state`: Indique si l'utilisateur s’est `"subscribed"` ou `"unsubscribed"` d’un groupe d'abonnement spécifique.
2. `subscription_group_id`: Représente l'ID unique du groupe d'abonnement. Vous pouvez trouver cet ID dans le tableau de bord de Braze, sous Gestion des **groupes d'abonnements**.

{% subtabs %}
{% subtab Swift %}
```swift
analytics.identify(
  userId: "{your-user}",
  traits: [
    "braze_subscription_groups": [
      [
        "subscription_group_id": "{your-group-id}",
        "subscription_group_state": "subscribed"
      ],
      [
        "subscription_group_id", "{your-group-id}",
        "subscription_group_state": "unsubscribed"
      ]
    ]
  ]
)
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
analytics.identify(
  "{your-user}",
  buildJsonObject {
    put("braze_subscription_groups", buildJsonArray {
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "subscribed")
          }
        )
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "unsubscribed")
          }
        )
      }
    )
  }
)
```
{% endsubtab %}
{% subtab TypeScript %}
```typescript
analytics.identify(
  "{your-user}",
  {
    braze_subscription_groups: [
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "subscribed"
      },
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "unsubscribed"
      }
    ]
  }
)
```
{% endsubtab %}
{% endsubtabs %}

##### Attributs personnalisés

Tous les autres traits seront enregistrés en tant qu'[attributs personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/).

| Méthode de segment | Méthode Braze | Exemple |
|---|---|---|
| Identifiez-vous à l'aide d'un ID utilisateur | Définir un ID externe | Segment :  `analytics.identify("dawei");`<br>Braze : `Braze.changeUser("dawei")` |
| Identifiez-vous avec des traits réservés | Définir les attributs de l'utilisateur | Segment : `analytics.identify({email: "dawei@braze.com"});`<br> Braze : `Braze.getUser().setEmail("dawei@braze.com");`
| Identifiez-vous à l'aide de traits personnalisés | Définir des attributs personnalisés | Segment : `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze : `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`
| Identifiez-vous à l'aide de votre identifiant utilisateur et de vos caractéristiques | Segment : Définir un ID externe et un attribut | Combinez les méthodes précédentes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Dans les destinations Actions en [mode Web et Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) [en mode cloud](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile), les mappages ci-dessus peuvent être définis à l'aide de l'action Mettre à jour le profil utilisateur.

{% alert important %}
Lorsque vous transmettez des données d'attributs utilisateur, vérifiez que vous ne transmettez que des valeurs pour les attributs qui ont changé depuis la dernière mise à jour. Cela vous évitera de consommer inutilement des points de données pour votre allocation. Pour les sources côté client, utilisez l'outil [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) open source de Segment pour optimiser votre intégration et limiter l'utilisation des points de données en supprimant les appels `identify()` dupliqués provenant de Segment. 

{% endalert %}
{% endtab %}

{% tab Piste %}
#### Piste

Lorsque vous suivez un événement, nous l'enregistrons en tant qu'[événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) en utilisant le nom fourni. 

Les métadonnées envoyées dans l'objet de propriétés de l'appel de suivi seront enregistrées dans Braze en tant que propriétés d'événement personnalisées pour l'événement associé. Tous les [types de données de propriétés d'événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) sont pris en charge.

Dans les destinations Actions en [mode Web et Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) [en mode cloud](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event), les mappages ci-dessus peuvent être définis à l'aide de l'action Track Event.

| Méthode de segment | Méthode Braze | Exemple |
|---|---|---|
| [Piste](https://segment.com/docs/spec/track/) | Enregistré en tant qu'[événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events). | Segment : `analytics.track("played_game");` <br>Braze : `Braze.logCustomEvent("played_game");`|
| [Piste avec propriétés](https://segment.com/docs/spec/track/) | Enregistré en tant que [propriété de l'événement]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties). | Segment : `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze : `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Suivi avec le produit](https://segment.com/docs/spec/track/) | Enregistré en tant qu'[événement d'achat]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web). | Segment : `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Braze : `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

##### Commande terminée {#order-completed}

Lorsque vous suivez un événement portant le nom `Order Completed` en utilisant le format décrit dans l ['API eCommerce](https://segment.com/docs/spec/ecommerce/v2/) de Segment, nous enregistrons les produits que vous avez répertoriés en tant qu' [achats]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

Dans les destinations [Actions en mode Web](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) et [Actions en mode cloud](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase), le mappage par défaut peut être personnalisé via l'action de suivi des achats.

{% endtab %}

{% tab Page %}
#### Page {#page}

L'appel de [page](https://segment.com/docs/spec/page/) vous permet d'enregistrer chaque fois qu'un utilisateur voit une page de votre site Web, ainsi que toutes les propriétés facultatives relatives à cette page.

Ce type d'événement peut être utilisé comme déclencheur dans les destinations Web Mode Actions et Cloud Actions pour enregistrer un événement personnalisé dans Braze.
{% endtab %}

{% endtabs %}

### Étape 5 : Testez votre intégration

Lorsque vous utilisez l'intégration côte à côte (mode appareil), vos indicateurs d'[aperçu][27] (sessions à vie, MAU, utilisateur actif, adhérence, sessions quotidiennes et sessions quotidiennes par MAU) peuvent être utilisés pour garantir que Braze reçoit des données de Segment.

Vous pouvez consulter vos données sur les pages des [événements personnalisés][22] ou sur les pages de [chiffre d'affaires][28], ou [en créant un segment][23]. La page **Événements personnalisés** du tableau de bord vous permet de consulter le nombre d'événements personnalisés au fil du temps. Notez que vous ne pourrez pas utiliser de [formules][24] incluant les statistiques MAU et utilisateur actif quotidien lors de l'utilisation d'une intégration de serveur à serveur (mode cloud).

Si vous envoyez des données d'achat à Braze (voir la commande terminée dans l'onglet **Suivi** de l'[étape 3](#methods)), la page des [revenus][28] vous permet de consulter les données relatives aux revenus ou aux achats effectués sur des périodes spécifiques ou le chiffre d'affaires total de votre application.

[La création d'un segment][26] vous permet de filtrer vos utilisateurs en fonction de l'événement personnalisé et des données d'attribut.

{% alert important %}
Si vous utilisez une intégration de serveur à serveur (mode cloud), les filtres liés aux données de session collectées automatiquement (tels que « première application utilisée » et « dernière application utilisée ») ne fonctionneront pas. Utilisez une intégration côte à côte (mode appareil) si vous souhaitez les utiliser dans votre intégration Segment et Braze.
{% endalert %}

## Suppression et suppression d'utilisateurs 

Si vous devez supprimer des utilisateurs, notez que la [fonctionnalité de suppression d'utilisateurs de Segment](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) **est** mappée à l’endpoint [`/users/delete`Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/). Notez que la vérification de ces suppressions peut prendre jusqu'à 30 jours.

Vous devez vous assurer de sélectionner un identifiant utilisateur commun entre Braze et Segment (comme dans`external_id`). Une fois que vous avez lancé une requête de suppression avec Segment, vous pouvez consulter son état dans l'onglet des requêtes de suppression de votre tableau de bord Segment.

## Rediffusion de segments

Segment fournit un service aux clients qui leur permet de « retransmettre » toutes les données historiques à un nouveau partenaire technologique. Les nouveaux clients de Braze qui souhaitent importer toutes les données historiques pertinentes peuvent le faire via Segment. Adressez-vous à votre représentant Segment si cela vous intéresse.

Segment se connectera à notre [`/users/track`endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour importer les données utilisateur dans Braze en votre nom.

{% alert important %}
Tous les identifiants pris en charge dans la destination Cloud Mode Actions sont pris en charge dans le cadre des Segment Replays.
{% endalert %}

## Les meilleures pratiques

{% details Passez en revue les cas d'utilisation pour éviter les excès de données. %}

**Le segment ne limite pas** le nombre d'éléments de données que les clients leur envoient. Segment vous permet de tout envoyer ou de décider quels événements vous allez envoyer à Braze. Plutôt que d'envoyer tous vos événements via Segment, nous vous suggérons de passer en revue les cas d'utilisation avec vos équipes marketing et éditoriales afin de déterminer quels événements vous enverrez à Braze afin d'éviter les excès de données.

{% enddetails %}

{% details Comprenez la différence entre l’endpoint d'API personnalisé et l’endpoint d'API REST personnalisé dans les paramètres de destination du mode Appareil mobile. %}

| Terminologie de Braze | Équivalent Segment |
| ----------------- | ------------------ |
| Endpoint du SDK Braze | endpoint d'API personnalisé |
| Endpoint REST de Braze | Endpoint de l'API REST personnalisé |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Votre endpoint d'API Braze (appelé « endpoint d'API personnalisé » dans Segment) est l’endpoint du SDK que Braze configure pour votre SDK (par exemple, `sdk.iad-03.braze.com`). Votre endpoint de l'API REST Braze (appelé « endpoint de l'API REST personnalisé » dans Segment) est l’endpoint de l'API REST (par exemple, `https://rest.iad-03.braze.com`)
{% enddetails %}

{% details Assurez-vous que votre endpoint d'API personnalisé est correctement saisi dans les paramètres de destination du mode appareil mobile. %}

| Terminologie de Braze | Équivalent Segment |
| ----------------- | ------------------ |
| Endpoint du SDK Braze | endpoint d'API personnalisé |
| Endpoint REST de Braze | Endpoint de l'API REST personnalisé |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Le format approprié doit être suivi pour vous assurer de saisir correctement votre endpoint du SDK Braze. Votre endpoint du SDK Braze ne doit pas inclure `https://` (par exemple,`sdk.iad-03.braze.com`), sinon l'intégration de Braze sera interrompue. Cela est obligatoire car Segment ajoute automatiquement à votre endpoint le préfixe`https://`, ce qui entraîne l'initialisation de Braze avec un endpoint non valide `https://https://sdk.iad-03.braze.com`.

{% enddetails %}

{% details Nuances de mappage des données. %}

Scénarios dans lesquels les données ne sont pas transmises comme prévu :

1. Attributs personnalisés imbriqués
  - Bien que [les attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/) puissent techniquement être envoyés à Braze via Segment, **la charge utile complète** sera envoyée à chaque fois. Cela entraînera des [points de données]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#data-points) par clé transmise dans l'objet imbriqué chaque fois que la charge utile est envoyée.<br><br> Pour ne dépenser qu'un sous-ensemble de points de données lors de l'envoi de la charge utile, vous pouvez utiliser la [fonctionnalité des fonctions de destination](https://segment.com/docs/connections/functions/destination-functions/) personnalisées appartenant à Segment. Cette fonctionnalité de la plateforme Segment vous permet de personnaliser la manière dont les données sont envoyées vers les destinations en aval.

  {% alert note %}
  Les fonctions de destination personnalisées sont contrôlées dans Segment, et Braze a une vision limitée des fonctions configurées en externe.
  {% endalert %}

{: start="2"}
2\. Transmission de données anonymes de serveur à serveur.
  - Les clients peuvent utiliser les bibliothèques serveur à serveur de Segment pour transmettre des données anonymes vers d'autres systèmes. Consultez la section sur les méthodes cartographiques pour en savoir plus sur l'envoi d'utilisateurs sans connexion `external_id` vers Braze via une intégration de serveur à serveur (mode cloud).

{% enddetails %}

{% details Personnalisation de l'initialisation de Braze. %}

Braze peut être personnalisé de différentes manières : push, messages intégrés à l'application, fiches de contenu et initialisation. Grâce à une intégration côte à côte, vous pouvez toujours personnaliser les messages push, les messages intégrés à l'application et les cartes de contenu comme vous le feriez avec une intégration directe de Braze.

Cependant, il peut être difficile, voire impossible, de personnaliser le moment où le SDK Braze est intégré ou de spécifier des configurations d'initialisation. En effet, Segment initialisera le SDK Braze pour vous lors de l'initialisation de Segment.

{% enddetails %}

{% details Envoi de deltas à Braze. %}

Lorsque vous transmettez des données d'attributs utilisateur, vérifiez que vous ne transmettez que des valeurs pour les attributs qui ont changé depuis la dernière mise à jour. Cela vous évitera de consommer inutilement des points de données pour votre allocation. Pour les sources côté client, utilisez l'outil [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) open source de Segment pour optimiser votre intégration et limiter l'utilisation des points de données en supprimant les appels `identify()` dupliqués provenant de Segment. 

{% enddetails %}


[5]: https://segment.com
[13]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events
[14]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[18]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[19]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[22]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data/#custom-event-data
[23]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[24]: {{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula/#creating-a-formula
[25]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection
[26]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[27]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/
[28]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[36]: https://segment.com/docs/sources/#server
[38]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[39]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[40]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[41]: https://segment.com/docs/spec/identify/#user-id
[42]: {% image_buster /assets/img/segment/setup.png %}
[43]: {% image_buster /assets/img/segment/website.png %}
[44]: {% image_buster /assets/img/segment/ios.png %}
[45]: {% image_buster /assets/img/segment/android.png %}
