---
nav_title: Collecte de données SDK
article_title: Collecte de données SDK
page_order: 1
page_type: reference
description: "Cet article de référence traite des données collectées par le SDK via une intégration personnalisée, une intégration avec collecte automatique et une intégration minimale."

---

# Collecte de données SDK

> Lorsque vous intégrez le SDK de Braze à votre application ou à votre site, Braze collecte automatiquement certains types de données. Certaines de ces données sont essentielles à nos processus, tandis que d'autres peuvent être activées ou désactivées en fonction de vos besoins. Vous pouvez également configurer Braze pour collecter d'autres types de données afin d'enrichir votre segmentation et votre envoi de messages.

Braze est conçu pour offrir une collecte de données flexible. Vous pouvez intégrer le SDK de Braze de plusieurs manières :

- **[Intégration minimale](#minimum-integration) :** Braze collecte automatiquement les données nécessaires à la communication avec les services de Braze.
- **[Données facultatives collectées par défaut](#optional-data-collected-by-default) :** Braze capture automatiquement certaines données utiles pour la plupart de vos cas d'utilisation. Vous pouvez désactiver la collecte automatique de ces données si elles ne sont pas indispensables à la communication avec les services de Braze.
- **[Données facultatives non collectées par défaut](#data-not-collected-by-default) :** Braze capture certaines données utiles pour des cas d'utilisation spécifiques, mais n'active pas automatiquement leur collecte pour des raisons de conformité générale. Vous pouvez choisir de collecter ces données lorsque cela correspond à vos besoins.
- **[Intégration personnalisée](#personalized-integration) :** Braze vous offre la possibilité de collecter des données supplémentaires en plus des données facultatives par défaut.

## Intégration minimale

Voici la liste des données strictement nécessaires, générées et reçues par Braze lors de l'initialisation du SDK. Ces données ne sont pas configurables et sont essentielles au fonctionnement de base de la plateforme. À l'exception du début et de la fin de session, toutes les autres données suivies automatiquement ne sont pas comptabilisées dans votre consommation de points de donnée.

| Attribut | Description | Pourquoi cette donnée est collectée |
| --------- | ----------- | ------------------ |
| Nom-de-la-version-de-l'application /<br> Code-de-version-de-l'application | La version la plus récente de l'application | Cet attribut permet d'envoyer les messages relatifs à la compatibilité de version aux bons appareils. Il peut servir à informer les utilisateurs d'interruptions de service ou de bogues. |
| Pays | Pays identifié par la géolocalisation de l'adresse IP. Si la géolocalisation de l'adresse IP n'est pas disponible, le pays est identifié par la [locale de l'appareil](#optional-data-collected-by-default). La valeur peut également être celle définie directement par les SDK avec `setCountry`, mais notez que transmettre une valeur d'attribut via le SDK ou l'API entraîne l'enregistrement de points de donnée. **Une fois le pays défini manuellement (via la méthode SDK, l'API REST ou un import CSV), le SDK ne met plus à jour automatiquement cette valeur.** | Cet attribut permet de cibler les messages en fonction de la localisation. |
| ID de l'appareil | Identifiant de l'appareil, chaîne de caractères générée aléatoirement | Cet attribut permet de différencier les appareils des utilisateurs et d'envoyer les messages au bon appareil. |
| Système d'exploitation et version du système d'exploitation | Appareil ou navigateur actuellement déclaré, et sa version | Cet attribut permet d'envoyer des messages uniquement aux appareils compatibles. Il peut également servir dans la segmentation pour cibler les utilisateurs devant mettre à jour leur application. |
| Début et fin de session | Moment où l'utilisateur commence à utiliser votre application ou site intégré | Le SDK de Braze transmet les données de session utilisées par le tableau de bord de Braze pour calculer l'engagement des utilisateurs et d'autres analyses essentielles à la compréhension de vos utilisateurs. Le moment exact où le début et la fin de session sont déclenchés par votre application ou votre site est configurable par un développeur ([Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web)). |
| Données d'interaction des messages SDK | Ouvertures directes par notification push, interactions avec les messages in-app, interactions avec les cartes de contenu | Cet attribut est utilisé à des fins de contrôle qualité, par exemple pour vérifier qu'un message a bien été reçu et que l'envoi n'est pas dupliqué. |
| Version du SDK | Version actuelle du SDK | Cet attribut permet d'envoyer des messages uniquement aux appareils compatibles et d'éviter toute interruption de service. |
| ID et horodatage de la session | Identifiant de session (chaîne de caractères générée aléatoirement) et horodatage de la session | Permet de déterminer si l'utilisateur démarre une nouvelle session ou reprend une session existante, et d'évaluer la rééligibilité aux messages destinés à cet utilisateur.<br><br>Certains canaux de communication, tels que les messages in-app et les cartes de contenu, sont synchronisés sur l'appareil au début de la session. Le backend utilise ensuite les données relatives au dernier contact avec les serveurs de Braze (stockées et renvoyées par l'appareil) pour déterminer si l'utilisateur est éligible à de nouveaux messages.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Indicateurs calculés

Braze génère des indicateurs calculés à partir des données SDK, des données d'interaction avec les messages non SDK et des informations dérivées. Pour clarifier, ces données calculées ne sont pas suivies par le SDK mais générées par les services de Braze. Un profil utilisateur affiche à la fois les données suivies et les données générées. 

Les indicateurs calculés comprennent les attributs suivants.

| Attribut                                      | Description                                                          |
|-----------------------------------------------|----------------------------------------------------------------------|
| Première utilisation de l'application                                 | Date                                                                 |
| Dernière utilisation de l'application                                  | Date                                                                 |
| Nombre total de sessions                            | Nombre                                                               |
| Carte cliquée                                   | Nombre                                                               |
| Dernier message reçu                     | Date                                                                 |
| Dernière campagne e-mail reçue                   | Date                                                                 |
| Dernière campagne push reçue                    | Date                                                                 |
| Nombre d'éléments de feedback                       | Nombre                                                               |
| Nombre de sessions au cours des Y derniers jours          | Nombre et date                                                      |
| Message reçu d'une campagne                  | Valeur booléenne. Ce filtre cible les utilisateurs selon qu'ils ont reçu ou non une campagne précédente.                               |
| Message reçu d'une campagne avec étiquette        | Valeur booléenne. Ce filtre cible les utilisateurs selon qu'ils ont reçu ou non une campagne comportant actuellement une étiquette donnée.                  |
| Campagne de reciblage                              | Valeur booléenne. Ce filtre cible les utilisateurs selon qu'ils ont ouvert ou cliqué sur un e-mail, une notification push ou un message in-app spécifique par le passé. |
| Application désinstallée                                    | Valeur booléenne et date |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Si vous souhaitez uniquement l'intégration minimale et que vous utilisez mParticle, Segment, Tealium ou GTM, notez les points suivants :
- **Plateformes mobiles :** Vous devez mettre à jour manuellement le code pour ces configurations. mParticle et Segment ne proposent pas de moyen de le faire via leur plateforme. 
- **Web :** L'intégration de Braze doit se faire de manière native pour permettre la configuration d'intégration minimale. Les gestionnaires d'étiquettes ne proposent pas de moyen de le faire via leur plateforme. 
{% endalert %} 

## Données facultatives collectées par défaut

En plus des données d'intégration minimale, les attributs suivants sont automatiquement capturés par Braze lors de l'initialisation de l'intégration SDK. Vous pouvez [désactiver]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection) la collecte de ces attributs pour vous limiter à une intégration minimale.

| Attribut               | Plateforme          | Description                                                                        | Pourquoi cette donnée est collectée                                                                                                                                                      |
|-------------------------|-------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nom du navigateur            | Web               | Nom du navigateur                                                                | Cet attribut permet d'envoyer des messages uniquement aux navigateurs compatibles. Il peut également servir à la segmentation par navigateur.                                     |
| Locale de l'appareil           | Android, iOS      | La locale par défaut de l'appareil                                                   | Cet attribut permet de traduire les messages dans la langue préférée de l'utilisateur.                                                                                            |
| Locale la plus récente de l'appareil           | Android, iOS      | La locale par défaut la plus récente de l'appareil                                                   | Cet attribut provient des paramètres de l'appareil de l'utilisateur et permet de traduire les messages dans sa langue préférée. Il est indépendant de l'attribut `Most Recent Location`.                                                                                            |
| Modèle de l'appareil            | Android, iOS      | Le matériel spécifique de l'appareil                                                | Cet attribut permet d'envoyer des messages uniquement aux appareils compatibles. Il peut également servir dans la segmentation.                                                 |
| Marque de l'appareil            | Android           | La marque de l'appareil (par exemple, Samsung)                                         | Cet attribut permet d'envoyer des messages uniquement aux appareils compatibles.                                                                                          |
| Opérateur sans fil de l'appareil | Android, iOS      | L'opérateur de téléphonie mobile                                                                 | Cet attribut peut être utilisé de manière facultative pour le ciblage des messages.<br><br>**Remarque :** Ce champ est obsolète depuis iOS 16 et prendra par défaut la valeur `--` dans une prochaine version d'iOS. |
| Langue                | Android, iOS, Web | Langue de l'appareil ou du navigateur, déterminée à partir de la locale de l'appareil.                                                           | Cet attribut permet de traduire les messages dans la langue préférée de l'utilisateur. Il est basé sur la locale de l'appareil.                                                                                            |
| Paramètres de notification   | Android, iOS, Web | Indique si les notifications push sont activées pour cette application.                                   | Cet attribut permet d'activer les notifications push.                                                                                                                    |
| Résolution              | Android, iOS, Web | Résolution de l'appareil ou du navigateur                                                          | Utilisé de manière facultative pour le ciblage des messages en fonction de l'appareil. Le format de cette valeur est « `<width>`x`<height>` ».                                                                 |
| Fuseau horaire               | Android, iOS, Web | Fuseau horaire de l'appareil ou du navigateur                                                           | Cet attribut permet d'envoyer les messages au bon moment, en fonction du fuseau horaire local de chaque utilisateur.                                                   |
| Agent utilisateur              | Web               | [Agent utilisateur](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) | Cet attribut permet d'envoyer des messages uniquement aux appareils compatibles. Il peut également servir dans la segmentation.                                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Pour en savoir plus sur le suivi des propriétés au niveau de l'appareil (opérateur sans fil, fuseau horaire, résolution, etc.), consultez la documentation spécifique à chaque plateforme : [Android]({{site.baseurl}}/developer_guide/storage/?tab=android), [iOS]({{site.baseurl}}/developer_guide/storage/?tab=swift), [Web]({{site.baseurl}}/developer_guide/storage/#cookies).

## Données non collectées par défaut

Par défaut, les attributs suivants ne sont pas collectés. Chaque attribut doit être intégré manuellement.

| Attribut                  | Plateforme     | Description                                                                                                                                                                                                                                                                                                               | Pourquoi cette donnée n'est pas collectée                                                                                                                                                                                                                                                                 |
|----------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Suivi publicitaire activé sur l'appareil | Android, iOS | Sur iOS :<br>[`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:))<br><br>Sur Android :<br>[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) | Cette propriété nécessite des autorisations supplémentaires au niveau de l'application, qui doivent être accordées par l'intégrateur.                                                                                                                                                                                      |
| IDFA de l'appareil                | iOS          | Identifiant de l'appareil pour les annonceurs                                                                                                                                                                                                                                                                                         | Cela nécessite le framework App Tracking Transparency, qui déclenche un examen supplémentaire de la confidentialité par l'App Store. Pour plus de détails, consultez [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)). |
| ID publicitaire Google      | Android      | Identifiant publicitaire pour les applications Google Play                                                                                                                                                                                                                                                                        | L'application doit récupérer le GAID et le transmettre à Braze. Pour plus de détails, consultez la section [ID publicitaire Google facultatif]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id).                                         |
| Localisation la plus récente | Android, iOS | Dernier emplacement GPS connu de l'appareil de l'utilisateur. Cette donnée est mise à jour au début de la session et stockée dans le profil de l'utilisateur. | L'utilisateur doit accorder l'autorisation de localisation à votre application. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Le SDK de Braze ne stocke aucune adresse IP localement.
{% endalert %}

## Intégration personnalisée

Pour tirer le meilleur parti de Braze, nos intégrateurs SDK implémentent généralement les SDK de Braze et enregistrent des [attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes), des [événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#logging-custom-events) et des [événements d'achat]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#logging-purchase-events) pertinents pour leur activité, en complément des données collectées automatiquement.

Une intégration personnalisée permet une communication sur mesure, adaptée à l'expérience de vos utilisateurs.

{% alert important %}
Braze bloquera les utilisateurs ayant plus de 5 000 000 de sessions (« utilisateurs fictifs ») et cessera d'ingérer leurs événements SDK. Pour plus d'informations, consultez la section [Filtrage du spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).
{% endalert %}