---
nav_title: Segment.io
article_title: Segment.io
page_order: 1
alias: /partners/segment/
description: "Cet article de référence présente le partenariat entre Braze et Segment.io, une plateforme de données client qui recueille et transfère des informations entre les différentes sources de votre pile marketing."
page_type: partner
search_tag: Partenaire

---

# Segment.io  

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment.io][5] est une plateforme de données client qui vous aide à collecter, nettoyer et activer vos données client. 

L’intégration de Braze et de Segment.io vous permet de suivre vos utilisateurs et de transmettre des données à divers fournisseurs d’analyse des utilisateurs. Segment.io vous permet de :
- Synchroniser des [Segment.io Engage]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_engage/) dans Braze pour l’utiliser dans des campagnes Braze et des segmentations de Canvas.
- [Importer des données sur les deux plateformes](#integration-options). Nous proposons une intégration SDK côte à côte pour vos applications Android, iOS et Web et une intégration serveur à serveur pour synchroniser vos données avec les API REST de Braze
- [Connecter les données sur Segment.io via Currents]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/). 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Segment.io | Un [compte Segment.io](https://app.segment.com/login) est requis pour profiter de ce partenariat. |
| [Bibliothèques](https://segment.com/docs/sources/) de la source installée et de la source Segment.io | L’origine de toutes les données envoyées dans Segment.io, comme des applications mobiles, des sites Web ou des serveurs de back-end.<br><br>Vous devez installer les bibliothèques dans votre application, votre site ou votre serveur avant de pouvoir configurer un flux `Source > Destination`. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Pour intégrer Braze et Segment.io, vous devez définir [Braze en tant que destination](#connection-settings), conformément au [type d’intégration que vous avez choisi](#integration-options) (mode de connexion). Si vous êtes un nouveau client de Braze, vous pouvez transmettre des données historiques à Braze en utilisant les [Segment.io Replays](#segment-replays). Ensuite, vous devez configurer les [mappages](#methods) et [tester votre intégration](#step-4-test-your-integration) pour assurer un flux de données régulier entre Braze et Segment.io.

### Étape 1 : Créer une destination Braze {#connection-settings}

Après avoir réussi à configurer vos sources, vous devrez configurer Braze comme [destination](https://segment.com/docs/destinations/) pour chaque source (iOS, Android, web, etc.). Vous disposerez de nombreuses options pour personnaliser le flux de données entre Braze et Segment.io en utilisant les paramètres de connexion.

### Étape 2 : Choisissez le cadre de destination et le type de connexion {#integration-options}

Dans Segment.io, naviguez vers **Destinations > Braze > Configure Braze > Select your Source > Setup (Destinations > Braze > Configurer Braze > Sélectionnez votre source > Configuration)**.

![La page de configuration de la source. Cette page comprend des paramètres permettant de définir le cadre de destination comme « actions » ou « classic » et de définir le mode de connexion en « mode cloud » ou en « mode appareil ».][42]

Vous pouvez intégrer les bibliothèques Web (Analytics.js) et les bibliothèques natives côté client de Segment avec Braze en utilisant une intégration côte à côte (mode appareil) ou une intégration serveur vers serveur (mode cloud).

Le choix de votre mode de connexion sera déterminé par le type de source pour lequel la destination est configurée.

| Intégration | Détails |
| ----------- | ------- |
| [Côte à côte<br>(mode-appareil)](#side-by-side-sdk-integration) |Ce mode d’intégration utilise le SDK de Segment.io pour traduire les événements en appels natifs de Braze, permettant d’accéder à des fonctionnalités plus avancées et de tirer le meilleur parti de l’intégration serveur à serveur de Braze.<br><br>Notez que Segment.io ne prend pas en charge toutes les méthodes Braze (par exemple, les cartes de contenu). Pour utiliser une méthode Braze qui n’est pas mappée à l’aide d’un mappage correspondant, vous devez invoquer la méthode en ajoutant le code Braze natif à votre base de code. |
| [Serveur à serveur<br>(mode-cloud)](#server-to-server-integration) | Ce mode d’intégration transfère les données de Segment.io aux endpoints d’API REST de Braze.<br><br>Il ne prend pas en charge les fonctionnalités d’interface utilisateur de Braze, telles que les messages in-app, les cartes de contenu ou les notifications push. Il existe également des données collectées automatiquement, telles que les champs d’appareil, qui ne sont pas disponibles avec cette méthode.<br><br>Optez pour une intégration côte à côte si vous souhaitez utiliser ces fonctionnalités.|
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
Visitez [Segment.io](https://segment.com/docs/destinations/#connection-modes) pour en savoir plus sur les deux options d'intégration (modes de connexion), y compris les avantages de chacune.
{% endalert %}

#### Intégration SDK côte à côte

Également appelée mode-appareil, cette intégration fait correspondre le SDK et les [méthodes](#methods) de Segment.io au SDK de Braze, ce qui permet d'accéder à toutes les fonctionnalités offertes par notre SDK, telles que les notifications push, la messagerie in-app et d'autres méthodes propres à Braze. 

{% alert note %}
Lorsque vous utilisez le mode-appareil de Segment.io, vous n'avez pas besoin d'intégrer directement le SDK Braze. Lors de l'ajout de Braze comme destination en mode-appareil pour Segment.io, le SDK de Segment.io initialisera le SDK de Braze et appellera les méthodes Braze mappées pertinentes.
{% endalert %}

Lors de l'utilisation d'une connexion en mode-appareil, similaire à l'intégration native du SDK de Braze, le SDK de Braze attribuera un `device_id` et un identifiant backend, `braze_id`, à chaque utilisateur. Cela permet à Braze de capturer l'activité anonyme de l'appareil en faisant correspondre ces identifiants au lieu de `userId`. 

{% tabs local %}
{% tab Android %}

{% alert important %}
Le code source pour l'intégration du mode appareil Android est maintenu par Braze et est mis à jour régulièrement pour refléter les nouvelles versions du SDK de Braze.

<br>
Le SDK Braze que vous utilisez dépendra du segment SDK que vous utilisez :

| | SDK de segment | SDK Braze |
| - | ----------- | --------- |
| Préféré | [Analytique-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Segment de Braze Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| Hérité | [Analytique-Android](https://github.com/segmentio/analytics-android) | [Segment Braze Android](https://github.com/Appboy/appboy-segment-android) |
{: .reset-td-br-1 .reset-td-br-2}


{% endalert %}

Pour configurer Braze comme destination en mode-appareil pour votre source Android, choisissez **Classic (Classique)** comme cadre de destination et cliquez sur **Save (Enregistrer)**. 

![]({% image_buster /assets/img/segment/android.png %})

Pour compléter l'intégration côte à côte, consultez les instructions détaillées de Segment.io pour ajouter la dépendance de destination Braze à votre application [Android](https://segment.com/docs/connections/destinations/catalog/braze/#android).

Le code source de la [destination Braze Web Mode (Actions)](https://github.com/segmentio/action-destinations/tree/main/packages/browser-destinations/src/destinations/braze) est maintenu par Segment.io. 

{% endtab %}
{% tab iOS %}

{% alert important %}
Le code source pour l'intégration du mode appareil iOS est maintenu par Braze et est mis à jour régulièrement pour refléter les nouvelles versions du SDK de Braze.

<br>
Le SDK Braze que vous utilisez dépendra du segment SDK que vous utilisez :

| | SDK de segment | SDK Braze |
| - | ----------- | --------- |
| Préféré | [Analytique-Swift](https://github.com/segmentio/analytics-swift) | [Swift Segment Braze](https://github.com/braze-inc/analytics-swift-braze) |
| Hérité | [Analytique-iOS](https://github.com/segmentio/analytics-ios) | [Segments Braze iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2}
{% endalert %}

Pour configurer Braze comme destination en mode-appareil pour votre source iOS, choisissez **Classic (Classique)** comme cadre de destination et cliquez sur **Save (Enregistrer)**. 

![]({% image_buster /assets/img/segment/ios.png %})

Pour compléter l'intégration côte à côte, consultez les instructions détaillées de Segment.io pour ajouter le pod Braze Segment.io à votre application [iOS](https://segment.com/docs/connections/destinations/catalog/braze/#ios).

Le code source pour l'intégration du [mode appareil iOS](https://github.com/Appboy/appboy-segment-ios) est maintenu par Braze et est mis à jour régulièrement pour refléter les nouvelles versions du SDK de Braze.

{% endtab %}
{% tab Web or Javascript %}

Le nouveau cadre Braze Web Mode (Actions) de Segment.io est recommandé pour configurer Braze comme une destination en mode-appareil pour votre source Web. 

Dans l'interface utilisateur de configuration, choisissez **Actions** comme cadre de destination et **mode-appareil** comme mode de connexion.

![]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% endtabs %}

#### Intégration serveur à serveur

Également appelée « mode-cloud », cette intégration transfère les données de Segment.io vers l’API REST de Braze. Utilisez le nouveau cadre [Braze Cloud Mode (Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) de Segment.io pour configurer une destination en mode-cloud pour n'importe laquelle de vos sources. 

Contrairement à l’intégration côte à côte, l’intégration serveur à serveur ne prend pas en charge les fonctionnalités de l’interface utilisateur de Braze, telles que les messages in-app, les cartes de contenu ou l’enregistrement automatique des jetons de notifications push. Il existe également des données [collectées automatiquement]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection) (telles que les utilisateurs anonymes et les champs de l’appareil), qui ne sont pas disponibles via le mode-cloud.

Si vous souhaitez utiliser ces données et ces fonctionnalités, envisagez d'utiliser l'intégration SDK en mode côte à côte (mode-appareil).

Le code source de la [destination Braze Cloud Mode (Actions)](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze) est maintenu par Segment.io.

### Étape 3 : Paramètres

Définissez les paramètres de votre destination. Tous les paramètres ne s'appliqueront pas à tous les types de destinations.

{% tabs local %}
{% tab Mobile Device-Mode %}

| Réglage | Description |
| ------- | ----------- |
| Identifiant d’application | L'identifiant de l'application utilisé pour référencer l'application spécifique. Vous le trouverez dans le tableau de bord de Braze, sous la rubrique **Manage Settings (Gérer les paramètres)**. | 
| Endpoint d’API personnalisé<br>(Endpoint SDK) | Votre endpoint Braze SDK qui correspond à votre instance (c'est-à-dire `sdk.iad-01.braze.com`) | 
| Région de l’endpoint | Votre instance Braze (c'est-à-dire US 01, US 02, EU 01, etc.) | 
| Activez l'enregistrement automatique des messages in-app | Désactivez cette option si vous souhaitez enregistrer manuellement les messages in-app. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Web Device-Mode %}

| Réglage | Description |
| ------- | ----------- |
| Identifiant d’application | L'identifiant de l'application utilisé pour référencer l'application spécifique. Vous le trouverez dans le tableau de bord de Braze, sous la rubrique **Manage Settings (Gérer les paramètres)**. | 
| Endpoint d’API personnalisé<br>(Endpoint SDK) | Votre endpoint Braze SDK qui correspond à votre instance (c'est-à-dire `sdk.iad-01.braze.com`) | 
| ID de notification push de site Web Safari | Si vous prenez en charge les notifications push Safari, vous devez spécifier cette option avec l'ID de site Web Push que vous avez fourni à Apple lors de la création de votre certificat de notifications push Safari (commence par `web`, par exemple, `web.com.example.domain`). |
| Version du SDK Web de Braze | La version du Web SDK de Braze que vous souhaitez utiliser |
| Envoyer automatiquement des messages in-app | Par défaut, tous les messages in-app auxquels un utilisateur a droit sont automatiquement transmis à l'utilisateur. Désactivez cette option si vous souhaitez afficher manuellement les messages in-app. |
| Ne pas charger FontAwesome | Braze utilise FontAwesome pour les icônes de message in-app. Par défaut, Braze chargera automatiquement FontAwesome depuis le CDN FontAwesome. Pour désactiver ce comportement (par exemple, parce que votre site utilise une version personnalisée de FontAwesome), réglez cette option sur `TRUE`. Notez que si vous faites cela, vous devez vous assurer que FontAwesome est chargé sur votre site - sinon, les messages in-app peuvent ne pas s'afficher correctement. |
| Activer les messages in-app HTML | L'activation de cette option permettra aux utilisateurs du tableau de bord de Braze d'utiliser des messages in-app HTML. | 
| Ouvrir les messages in-app dans un nouvel onglet | Par défaut, les liens provenant de clics sur des messages in-app se chargent dans l'onglet actuel ou dans un nouvel onglet, comme indiqué dans le tableau de bord, message par message. Définissez cette option sur `TRUE` pour obliger tous les liens provenant de clics sur des messages in-app à s'ouvrir dans un nouvel onglet ou une nouvelle fenêtre. |
| Position verticale du message in-app | Donnez une valeur à cette option pour remplacer les positions verticales par défaut de Braze. | 
| Exiger le rejet explicite des messages in-app | Par défaut, lorsqu’un message in-app s’affiche, appuyer sur le bouton d’échappement ou cliquer sur l’arrière-plan grisé de la page va rejeter le message. Paramétrez cette option sur « true » pour empêcher ce comportement et exiger un clic de bouton explicite pour ignorer les messages. |
| Intervalle minimum en secondes entre les actions de déclenchement | Par défaut sur 30.<br>Par défaut, une action de déclenchement ne s’activera que si au moins 30 secondes se sont écoulées depuis la dernière action de déclenchement. Donnez une valeur à cette option de configuration pour remplacer cette valeur par défaut par une valeur qui vous est propre. Nous ne recommandons pas de donner à cette valeur une valeur inférieure à 10 pour éviter de spammer l'utilisateur avec des notifications.|
| Emplacement du service de traitement | Par défaut, lors de l'enregistrement des utilisateurs pour les notifications push web, Braze cherchera le fichier service de traitement requis dans le répertoire racine de votre serveur web à l’adresse `/service-worker.js`. Si vous voulez héberger votre service de traitement à une adresse différente sur ce serveur, fournissez une valeur pour cette option qui est l’adresse absolue du fichier. (par exemple, `/mycustompath/my-worker.js`). Notez que le fait de définir une valeur ici limite la portée des notifications push sur votre site. Par exemple, dans l'exemple ci-dessus, le fichier du service de traitement étant situé dans le répertoire `/mycustompath/`, `requestPushPermission` peut être appelé uniquement à partir de pages Web commençant par `http://yoursite.com/mycustompath/`. |
| Désactiver la maintenance des jetons de notification push | Par défaut, les utilisateurs qui ont déjà accordé une autorisation de notification push web synchroniseront automatiquement leur jeton de notification push avec le backend Braze lors des nouvelles sessions afin de garantir la délivrabilité. Pour désactiver ce comportement, réglez cette option sur `FALSE`. |
| Gérer le service de traitement en externe | Si vous enregistrez votre propre service de traitement et dont vous contrôlez le cycle de vie, paramétrez cette option sur `TRUE`, et le SDK Braze n'enregistrera ou ne désenregistrera pas de service de traitement. Si vous paramétrez cette option sur `TRUE`, pour que la notification push fonctionne correctement, vous devez enregistrer vous-même le service de traitement avant de l'appeler `requestPushPermission` et vous assurer qu'il contient le code du service de traitement de Braze, soit avec `self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');`, soit en incluant directement le contenu de ce fichier. Lorsque cette option est `TRUE`, l'option `serviceWorkerLocation` n'est pas pertinente et est ignorée. |
| Sécurité du contenu Nonce | Si vous fournissez une valeur pour cette option, le SDK de Braze ajoutera le nonce à tous les `<script>` et les éléments `<style>` créés par le SDK. Cela permet au SDK Braze de fonctionner avec la politique de sécurité du contenu de votre site web. Outre la définition de ce nonce, vous devrez peut-être autoriser le chargement de FontAwesome, ce que vous pouvez faire en l'ajoutant `use.fontawesome.com` à la liste des autorisations de votre politique de sécurité du contenu ou en utilisant l'option `doNotLoadFontAwesome` et en le chargeant manuellement. |
| Autoriser les robots d’indexation | Par défaut, le Web SDK Braze ignore l'activité des spiders ou des crawlers web connus, tels que Google, sur la base de la chaîne de caractères de l'agent utilisateur. Cela permet d'économiser des points de données, de rendre les analyses plus précises et d'améliorer le classement des pages. Toutefois, si vous souhaitez que Braze enregistre l'activité de ces crawlers, vous pouvez régler cette option sur `TRUE`. |
| Activer la connexion | Définir sur `TRUE` pour activer la journalisation par défaut. Notez que Braze se connectera alors à la console JavaScript, qui est visible par tous les utilisateurs. Avant de mettre votre page en production, vous devez supprimer ce fichier ou fournir un autre enregistreur avec `setLogger`. |
| Ouvrir les cartes de fil d'actualité dans un nouvel onglet (ouvrir les cartes dans un nouvel onglet) | Par défaut, les liens des objets de la carte se chargent dans l'onglet ou la fenêtre en cours. Paramétrez cette option sur `TRUE` pour que les liens des cartes s'ouvrent dans un nouvel onglet ou une nouvelle fenêtre. <br><br>**Remarque :** Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus. |
| Autoriser le JavaScript fourni par l'utilisateur | Par défaut, le Web SDK Braze n'autorise pas les actions de clic JavaScript fournies par l'utilisateur, car il permet aux utilisateurs du tableau de bord de Braze d'exécuter JavaScript sur votre site. Pour indiquer que vous faites confiance aux utilisateurs du tableau de bord de Braze pour écrire des actions de clic JavaScript non malveillantes, définissez cette propriété sur `TRUE`. Si `enableHtmlInAppMessages` est `TRUE`, cette option sera également définie sur `TRUE`. |
| Version de l’application| Si vous fournissez une valeur pour cette option, les événements des utilisateurs envoyés à Braze seront associés à la version donnée, ce qui peut être utilisé pour la segmentation des utilisateurs. |
| Délai d’expiration de session en secondes | Par défaut sur 30.<br>Par défaut, les sessions expirent après 30 minutes d’inactivité. Donnez une valeur à cette option de configuration pour remplacer cette valeur par défaut par une valeur qui vous est propre. | 
| Liste des propriétés autorisées de l’appareil | Par défaut, le SDK de Braze détecte et collecte automatiquement toutes les propriétés de l’appareil au format `DeviceProperties`. Pour remplacer ce comportement, fournissez un tableau de `DeviceProperties`. Notez que sans certaines propriétés, toutes les fonctionnalités ne fonctionneront pas correctement. Par exemple, la livraison du fuseau horaire local ne fonctionnera pas sans le fuseau horaire. |
| Localisation | Par défaut, tous les messages visibles par l'utilisateur générés par le SDK seront affichés dans la langue du navigateur de l'utilisateur. Fournissez une valeur pour cette option afin de remplacer ce comportement et de forcer une langue spécifique. La valeur de cette option doit être un code de langue ISO 639-1. |
| Pas de cookies | Par défaut, le SDK de Braze stocke de petites quantités de données (identifiants d'utilisateur, identifiants de session) dans des cookies. Cela permet à Braze de reconnaître les utilisateurs et les sessions dans les différents sous-domaines de votre site. Si cela vous pose un problème, paramétrez cette option sur `TRUE` pour désactiver le stockage des cookies et vous fier entièrement au localStorage HTML 5 pour identifier les utilisateurs et les sessions. |
| Suivre toutes les pages | **Destination Web classique mode-appareil (maintenance) uniquement**<br><br>Segment.io recommande de migrer vers la destination du cadre des Actions Web où ce paramètre peut être [activé via mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Cela enverra tous les [appels de page](https://segment.com/docs/spec/page/) à Braze en tant qu'événement "Loaded/Viewed a Page" (page Chargée/Consultée). |
| Suivre uniquement les pages nommées | **Destination Web classique mode-appareil (maintenance) uniquement**<br><br>Segment.io recommande de migrer vers la destination du cadre des Actions Web où ce paramètre peut être [activé via mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Cela enverra uniquement les appels de page à Braze avec un nom qui leur est associé. |
| Enregistrer l’achat lorsque le chiffre d’affaires est présent | **Destination Web classique mode-appareil (maintenance) uniquement**<br><br>Segment.io recommande de migrer vers la destination du cadre des Actions Web où ce paramètre peut être [activé via mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Lorsque cette option est activée, tous les appels Track (de suivi) avec la propriété revenue déclencheront un événement d'achat. | 
| Suivre uniquement les utilisateurs connus | **Destination Web classique mode-appareil (maintenance) uniquement**<br><br>Segment.io recommande de migrer vers la destination du cadre des Actions Web où ce paramètre peut être activé via mappages.<br><br>S'il est activé, ce nouveau paramètre retarde l'appel de `window.appboy.initialize` jusqu'à ce qu'il y ait un `userId`. | 
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Cloud-Mode %}

| Réglage | Description |
| ------- | ----------- |
| Identifiant d’application | L'identifiant de l'application utilisé pour référencer l'application spécifique. Vous le trouverez dans le tableau de bord de Braze, sous la rubrique **Manage Settings (Gérer les paramètres)**. | 
| Clé API REST | Cela se trouve dans votre tableau de bord de Braze sous **Developer Console > API Settings (Console du développeur > Paramètres de l'API)**. | 
| Endpoint d’API REST personnalisé | Votre endpoint REST de Braze qui correspond à votre instance (par exemple, rest.iad-01.braze.com) | 
| Mettre à jour uniquement les utilisateurs existants | **Destination Web classique mode-cloud (Maintenance) uniquement**<br><br>Segment.io recommande de migrer vers la destination du cadre des Actions Cloud où ce paramètre peut être [activé via mappages](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Détermine s'il faut mettre à jour uniquement les utilisateurs existants. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

### Étape 4 : Méthodes de mappage {#methods}

Braze prend en charge les méthodes [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page), [Identify (Identifier)](https://segment.com/docs/spec/identify/), [Track (Suivre)](https://segment.com/docs/spec/track/) et [Group (Groupe)](https://segment.com/docs/connections/spec/group/) de Segment.io. Les types d'identifiants utilisés dans le cadre de ces méthodes dépendront de la manière dont les données sont envoyées, selon qu'il s'agit d'une intégration de serveur à serveur (mode-cloud) ou côte à côte (mode-appareil). Dans les destinations Braze Web Mode Actions et Cloud Mode Actions, vous pouvez également choisir de configurer un mappage pour un [appel d’alias Segment.io](https://segment.com/docs/connections/spec/alias/). 

{% alert note %}
Bien que les alias d'utilisateurs soient pris en charge comme identifiant dans la destination Braze Cloud Mode (Actions), il convient de noter que l'appel d'alias Segment.io n'est pas directement lié aux alias d'utilisateurs Braze.
{% endalert %}

| Types d’identifiant | Adresses supportées |
| --------------- | --------------------- |
| `userId` (`external_id`) | Tous |
| Utilisateur anonyme | Destinations mode-appareil |
| Alias utilisateur | Destinations mode-cloud |
{: .reset-td-br-1 .reset-td-br-2}

La destination Actions en mode cloud propose une [action de création d'alias](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#create-alias) qui peut être utilisée pour créer un utilisateur uniquement alias ou ajouter un alias à un profil `external_id` existant. L'[Identify User Action](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#identify-user) (action identifier l'utilisateur) peut être utilisée avec la Create Alias Action (action Créer un alias) pour fusionner un utilisateur alias uniquement avec un `external_id` dès qu'un alias est disponible pour l'utilisateur. 

Il est également possible de concevoir une solution de contournement et d'utiliser `braze_id` pour envoyer des données utilisateur anonymes en mode-cloud. Cela nécessite d'inclure manuellement la `braze_id` de l'utilisateur dans tous vos appels d'API Segment.io. Vous pouvez en savoir plus sur la configuration de cette solution de contournement dans la [documentation de Segment.io](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users).

{% tabs local %}
{% tab Identify %}
#### Identification

L'appel [Identify (d’identification)](https://segment.com/docs/spec/identify/) vous permet de lier un utilisateur à ses actions et d'enregistrer des attributs le concernant. 

Certaines caractéristiques spéciales de Segment.io correspondent aux champs de profil d'attribut standard de Braze :

| Caractéristiques spéciales de Segment.io | Attributs standard de Braze |
| ------------- | ----------- |
| `userId` | `external_id` |
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `email` | `email` |
| `birthday` | `dob` |
| `address.country` | `country` |
| `address.city` | `home_city` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2}

D'autres champs de profil Braze réservés, tels que `email_subscribe` et `push_subscribe` peuvent être envoyés en utilisant la convention de dénomination de Braze pour ces champs et en les passant comme caractéristiques dans un appel d'identification.

Toutes les autres caractéristiques seront enregistrées en tant qu’[attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/).

| Méthode Segment.io | Méthode Braze | Exemple |
|---|---|---|
| Identifier un utilisateur avec un ID utilisateur | Définir un ID externe | Segment.io : `analytics.identify("dawei");`<br>Braze : `Braze.changeUser("dawei")` |
| Identification avec des caractéristiques réservées | Définir les attributs utilisateur | Segment.io : `analytics.identify({email: "dawei@braze.com"});`<br> Braze : `Braze.getUser().setEmail("dawei@braze.com");`
| Identification avec des caractéristiques personnalisées | Définir des attributs personnalisés | Segment.io : `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze : `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")` ;
| Identification avec l’ID et les caractéristiques utilisateur | Segment.io : Définir l’ID externe et l’attribut | Combine les méthodes précédentes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Dans les destinations [Web Mode Actions (Actions mode Web)](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) et [Cloud Mode Actions (Actions mode cloud)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile), les mappages ci-dessus peuvent être définis à l'aide de l'action Mettre à jour le profil utilisateur.

{% alert important %}
Lorsque vous transmettez des données d’attribut utilisateur, assurez-vous de ne transmettre que les valeurs des attributs qui ont changé depuis la dernière mise à jour. Cela vous permettra de ne pas consommer inutilement de points de données pour votre allocation. Pour les sources côté client, utilisez l'outil open-source [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) de Segment.io pour optimiser votre intégration et limiter l'utilisation des points de données en éliminant les appels `identify()` en double de Segment. 

{% endalert %}
{% endtab %}

{% tab Track %}
#### Suivi

Lorsque vous suivez un événement, nous enregistrons cet événement comme un [événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) en utilisant le nom fourni. 

Les métadonnées envoyées dans l'objet de propriétés de l'appel de piste seront enregistrées dans Braze en tant que propriétés de l'événement personnalisé pour l'événement associé. Tous[ les types de données des propriétés de l'événement personnalisé](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) sont pris en charge.

Dans les destinations [Web Mode Actions (Actions mode Web)](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) et [Cloud Mode Actions (Actions mode cloud)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event), les mappages ci-dessus peuvent être définis à l'aide de l'action Suivi d'événement.

| Méthode Segment.io | Méthode Braze | Exemple |
|---|---|---|
| [Suivi](https://segment.com/docs/spec/track/) | Enregistré en tant qu’[événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events). | Segment.io : `analytics.track("played_game");` <br>Braze : `Braze.logCustomEvent("played_game");`|
| [Suivre avec les propriétés](https://segment.com/docs/spec/track/) | Enregistré en tant que [propriété de l’événement]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties). | Segment.io : `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze : `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Suivre avec le produit](https://segment.com/docs/spec/track/) | Enregistré en tant qu’[Événement d’achat]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/). | Segment.io : `analytics.track("purchase", {products: [product_id: "ab12", price: 19]});` <br>Braze : `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

##### Commande terminée {#order-completed}

Lorsque vous suivez un événement avec le nom `Order Completed` en utilisant le format décrit dans [l'API eCommerce](https://segment.com/docs/spec/ecommerce/v2/) de Segment.io, nous enregistrons les produits que vous avez listés comme des [achats]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

Dans les destinations [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) et [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase), le mappage par défaut peut être personnalisé par le biais de l'action Suivi des achats.

{% endtab %}

{% tab group %}
#### Groupe

L'appel de groupe enregistrera un [attribut personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) avec le nom `ab_segment_group_<groupId>`, où `groupId` est l'ID du groupe dans les paramètres de la méthode. Par exemple, si l’ID du groupe est `1234`, alors le nom de l’attribut personnalisé sera `ab_segment_group_1234`. La valeur de l’attribut personnalisé sera définie sur `true`.

Dans les destinations [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile-1) et [cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile), le type d'événement de groupe est un déclencheur par défaut pour l'action de mise à jour du profil utilisateur ; toutefois, ce mappage peut être personnalisé. En outre, un appel de groupe peut être utilisé pour déclencher des actions personnalisées. 

{% endtab %}
{% tab Page %}
#### Page {#page}

L’appel de [page](https://segment.com/docs/spec/page/) vous permet d’enregistrer chaque fois qu’un utilisateur voit une page sur votre site Web, ainsi que les propriétés facultatives de la page.

Ce type d'événement peut être utilisé comme déclencheur dans les destinations Web Mode Actions (Actions mode Web) et Cloud Actions (Actions cloud).
{% endtab %}

{% endtabs %}

### Étape 5 : Tester votre intégration

Lorsque vous utilisez l’intégration côte à côte (en mode appareil), vos indicateurs [d’overview][27] (sessions à vie, MAU, utilisateur actif par jour, adhérence, sessions quotidiennes et sessions quotidiennes par MAU) peuvent être utilisés pour vérifier que Braze reçoit des données de Segment.io.

Vous pouvez consulter vos données sur les pages [événements personnalisés][22] ou [chiffre d’affaires][28] ou encore en [créant un segment][23]. La page **Événements personnalisés** du tableau de bord vous permet de visualiser le décompte des événements personnalisés dans le temps. Notez que vous ne pourrez pas utiliser les [formules][24] qui incluent les statistiques Utilisateurs actifs par mois et Utilisateurs actifs quotidiens avec une intégration en mode cloud (de serveur à serveur).

Si vous envoyez des données d’achat à Braze (voir Commande terminée dans l’onglet **Suivi** de l’[Étape 3](#methods)), la page [chiffre d’affaires][28] vous permet d’afficher des données sur le chiffre d’affaires ou les achats correspondants à des périodes spécifiques ou sur le chiffre d’affaires total de votre application.

[Créer un segment][26] vous permet de filtrer vos utilisateurs en fonction des données d’attribut et d’événement personnalisés.

{% alert important %}
Si vous utilisez une intégration serveur à serveur (mode-cloud), les filtres liés aux données de session collectées automatiquement (par ex. « première application utilisée » et « dernière application utilisée ») ne fonctionneront pas. Utilisez une intégration côte à côte (mode-appareil) si vous souhaitez les utiliser dans votre intégration Segment.io et Braze.
{% endalert %}

## Effacer et supprimer des utilisateurs 

Si vous devez effacer ou supprimer des utilisateurs, notez que la [fonctionnalité de suppression d’utilisateurs de Segment.io](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) **est** mappée à l’[endpoint users/delete]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint) de Braze. Notez que la vérification de ces suppressions peut prendre jusqu’à 30 jours.

Assurez-vous de sélectionner un identifiant utilisateur qui est commun à Braze et Segment.io (comme dans `external_id`). Une fois que vous avez lancé une demande de suppression avec Segment.io, vous pouvez en consulter le statut dans l'onglet des demandes de suppression de votre tableau de bord Segment.io.

## Relectures via Segment.io

Segment.io fournit un service permettant de « relire » toutes les données historiques pour un nouveau partenaire technologique. Les nouveaux clients de Braze qui souhaitent importer toutes leurs données historiques pertinentes peuvent le faire via Segment.io. Parlez-en à votre représentant Segment.io si cela vous intéresse.

Segment.io se connectera à notre [endpoint /users/track]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) pour importer des données utilisateur dans Braze en votre nom.

{% alert important %}
Tous les identifiants pris en charge dans la destination des actions mode-cloud sont pris en charge dans le cadre des relectures de données via Segment.io.
{% endalert %}

## Bonnes pratiques

{% details Examiner les cas d’utilisation pour éviter les dépassements de données. %}

Segment.io **ne** limite pas le nombre d’éléments de données que les clients peuvent leur envoyer. Segment.io vous permet d’envoyer toutes vos données ou de décider quels événements vous souhaitez envoyer à Braze. Au lieu d’envoyer tous vos événements à l’aide de Segment.io, nous vous suggérons de revoir les cas d’utilisation avec vos équipes marketing et éditoriales afin de déterminer quels événements vous allez envoyer à Braze pour éviter les dépassements de données.

{% enddetails %}

{% details Comprendre la différence entre l’endpoint API personnalisé et l’endpoint API REST personnalisé dans les paramètres de destination du mode appareil mobile. %}

| Terminologie Braze | Équivalent Segment.io |
| ----------------- | ------------------ |
| Endpoint du SDK Braze | Endpoint d’API personnalisé |
| Endpoint REST de Braze | Endpoint d’API REST personnalisé |
{: .reset-td-br-1 .reset-td-br-2}

Votre endpoint d’API Braze (appelé « endpoint d’API personnalisé » dans Segment.io) est l’endpoint SDK que Braze configure pour votre SDK (par exemple, `sdk.iad-03.braze.com`). Votre endpoint d’API REST de Braze (appelé « endpoint d’API REST personnalisé » dans Segment.io) est l’endpoint d’API REST (par exemple, `https://rest.iad-03.braze.com`)
{% enddetails %}

{% details Assurez-vous que votre endpoint API personnalisé est correctement saisi dans les paramètres de destination du mode appareil mobile. %}

| Terminologie Braze | Équivalent Segment.io |
| ----------------- | ------------------ |
| Endpoint du SDK Braze | Endpoint d’API personnalisé |
| Endpoint REST de Braze | Endpoint d’API REST personnalisé |
{: .reset-td-br-1 .reset-td-br-2}

Le format approprié doit être respecté pour vous assurer de saisir correctement votre endpoint de SDK Braze. Votre endpoint SDK Braze ne doit pas inclure `https://` (par exemple, `sdk.iad-03.braze.com`), car cela invaliderait l’intégration de Braze. Ceci est requis parce que Segment.io précède automatiquement votre endpoint par `https://`, ce qui entraîne l’initialisation de Braze avec un endpoint non valide `https://https://sdk.iad-03.braze.com`.

{% enddetails %}

{% details Nuances de mappage de données. %}

Scénarios dans lesquels les données ne seront pas transmises comme prévu :

1. Attributs personnalisés imbriqués
  - Bien que les [attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/) puissent techniquement être envoyés à Braze via une destination mode-cloud, la **totalité de la charge utile** sera envoyée à chaque fois. Cela entraînera des [points de données]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#data-points) par clé passée dans l'objet imbriqué à chaque fois que les données utiles seront envoyées. 
2. Transfert de données anonymisées d’un serveur à l’autre.
  - Les clients peuvent utiliser les bibliothèques serveur à serveur de Segment pour transférer des données anonymes vers d’autres systèmes. Consultez la section sur les méthodes de cartographie pour en savoir plus sur l'envoi d'utilisateurs sans `external_id` à Braze via une intégration de serveur à serveur (mode-cloud).

{% enddetails %}

{% details Personnalisation de l’initialisation de Braze. %}

Il existe plusieurs façons de personnaliser Braze : les notifications push, les messages in-app, les cartes de contenu, et l’initialisation. L’intégration côte à côte vous permet de personnaliser les notifications push, les messages in-app et les cartes de contenu comme vous le feriez avec une intégration Braze directe.

Cependant, il peut être difficile, voire parfois impossible, de les personnaliser ou de définir des configurations d’initialisation lorsque le SDK de Braze est intégré. En effet, Segment initiera le SDK Braze pour vous lors de l’initialisation de Segment.io.

{% enddetails %}

{% details Envoyer des deltas à Braze. %}

Lorsque vous transmettez des données d’attribut utilisateur, assurez-vous de ne transmettre que les valeurs des attributs qui ont changé depuis la dernière mise à jour. Cela vous permettra de ne pas consommer inutilement de points de données pour votre allocation. Pour les sources côté client, utilisez l'outil open-source [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) de Segment.io pour optimiser votre intégration et limiter l'utilisation des points de données en éliminant les appels `identify()` en double de Segment. 

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
[27]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/
[28]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
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
