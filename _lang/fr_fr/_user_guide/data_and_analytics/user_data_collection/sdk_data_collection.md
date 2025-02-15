---
nav_title: Collecte de données SDK
article_title: Collecte de données SDK
page_order: 1
page_type: reference
description: "Cet article de référence traite des données qui sont collectées par le SDK à travers une intégration personnalisée, d’une intégration collectée automatiquement et d’une intégration minimale."

---

# Collecte de données SDK

> Lorsque vous intégrez le SDK de Braze à votre app ou à votre site, Braze collecte automatiquement certains types de données. Certaines de ces données sont essentielles pour nos processus et d'autres peuvent être activées ou désactivées en fonction de vos besoins. Vous pouvez également configurer Braze pour qu'il recueille d'autres types de données afin d'améliorer la segmentation et l'envoi de messages.

Braze est conçu pour permettre une collecte de données flexible, vous pouvez donc intégrer le SDK de Braze de la manière suivante :

- **[Intégration minimale](#minimum-integration):** Braze collecte automatiquement les données nécessaires à la communication avec les services de Braze.
- **[Données facultatives collectées par défaut](#optional-data-collected-by-default):** Braze capture automatiquement certaines données qui sont largement utiles pour la plupart de vos cas d'utilisation. Vous pouvez choisir de désactiver la collecte automatique de ces données si elles ne sont pas indispensables à la communication avec les services de Braze.
- **[Données facultatives non collectées par défaut](#data-not-collected-by-default):** Braze capture certaines données utiles pour certains cas d'utilisation et n'active pas automatiquement la collecte pour des raisons de conformité générale. Vous pouvez opter pour la collecte de ces données lorsque cela correspond à vos cas d'utilisation.
- **[Intégration personnalisée](#personalized-integration):** Braze vous offre la possibilité de collecter des données en plus des données facultatives par défaut.

## Intégration minimale

Vous trouverez ci-dessous la liste des données strictement nécessaires générées et reçues par Braze lors de l'initialisation du SDK. Ces données ne sont pas configurables et sont essentielles pour les fonctions de base de la plate-forme. À l'exception du début et de la fin de la session, toutes les autres données suivies automatiquement ne sont pas prises en compte dans le calcul de votre nombre de points de données.

| Attribut | Description | Pourquoi il est collecté |
| --------- | ----------- | ------------------ |
| Nom-de-la-version-de-l’application /<br> Code-de-version-de-l’application | La version la plus récente de l'application | Cet attribut est utilisé pour envoyer les messages relatifs à la compatibilité de la version de l'app aux bons appareils. Il peut être utilisé pour informer les utilisateurs des interruptions de service ou des bogues. |
| Pays | Pays identifié par la géolocalisation de l'adresse IP | Cet attribut est utilisé pour cibler les messages en fonction de l'emplacement/localisation. |
| ID de l’appareil | Identifiant de l'appareil, chaîne de caractères générée de manière aléatoire | Cet attribut est utilisé pour différencier les appareils des utilisateurs et envoyer les messages au bon appareil. |
| Système d'exploitation et version du système d'exploitation | Appareil ou navigateur actuellement déclaré et version de l'appareil ou du navigateur | Cet attribut est utilisé pour envoyer des messages uniquement aux appareils compatibles. Peut également être utilisé dans le cadre d’une segmentation pour cibler les utilisateurs qui doivent mettre à jour leurs applications. |
| Début et fin de la session | Lorsque l'utilisateur commence à utiliser votre app ou site intégré. | Le SDK Braze rapporte les données de session utilisées par le tableau de bord de Braze pour calculer l’engagement des utilisateurs et d’autres analyses essentielles à une meilleure connaissance de vos utilisateurs. Le moment exact où le début et la fin de la session sont appelés par votre application ou votre site est configurable par un développeur ([Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/)). |
| Données d'interaction du message SDK | Ouvertures directes par notification push, interactions avec les messages in-app, interactions avec les cartes de contenu | Cet attribut est utilisé à des fins de contrôle de la qualité, par exemple pour vérifier qu'un message a bien été reçu et que l'envoi n'est pas dupliqué. |
| Version du SDK | Version actuelle du SDK | Cet attribut est utilisé pour n'envoyer des messages qu'aux appareils compatibles et éviter toute interruption de service. |
| ID et horodatage de la session | Identifiant de session, chaîne de caractères générée de manière aléatoire et horodatage de la session | Utilisé pour déterminer si l’utilisateur démarre une nouvelle session ou une session existante et pour déterminer la rééligibilité des messages destinés à cet utilisateur.<br><br>Certains canaux de communication, tels que les messages in-app et les cartes de contenu, sont synchronisés sur l’appareil au début de la session. Notre backend utilisera alors les données relatives au dernier contact avec les serveurs de Braze (que l'appareil stocke et renvoie) pour savoir si l'utilisateur est éligible à tout nouvel envoi de messages.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Indicateurs calculés

Braze génère des indicateurs calculés à partir des données SDK, des données d'interaction avec les messages non SDK et des informations dérivées. Pour plus de clarté, ces données calculées ne sont pas suivies par le SDK mais générées par les services Braze, et un profil utilisateur affichera à la fois les données suivies et les données générées. 

Les indicateurs calculés comprennent les attributs suivants.

| Attribut                                      | Description                                                          |
|-----------------------------------------------|----------------------------------------------------------------------|
| Première application utilisée                                 | Date                                                                 |
| Dernière application utilisée                                  | Date                                                                 |
| Nombre total de sessions                            | Nombre                                                               |
| Carte cliquée                                   | Nombre                                                               |
| Dernier message reçu                     | Date                                                                 |
| Dernière campagne d'e-mail reçue                   | Date                                                                 |
| Dernière campagne de push reçue                    | Date                                                                 |
| Nombre d'éléments de feedback                       | Nombre                                                               |
| Nombre de sessions au cours des Y derniers jours          | Nombre et heure                                                      |
| Message reçu de la campagne                  | Booléen. Ce filtre cible les utilisateurs en fonction de la réception ou non d'une campagne précédente.                               |
| Message reçu à partir d’une campagne avec tag        | Booléen. Ce filtre cible les utilisateurs selon qu'ils ont reçu ou non une campagne comportant une étiquette.                  |
| Campagne de reciblage                              | Booléen. Ce filtre cible les utilisateurs en fonction du fait qu'ils ont ouvert ou cliqué sur un e-mail, un push ou un message in-app spécifique par le passé. |
| Application désinstallée                                    | Booléen et temps |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Si vous n'êtes intéressé que par l'intégration minimale et que vous intégrez mParticle, Segment, Tealium ou GTM, notez ce qui suit :
- **Plates-formes mobiles**: Vous devez mettre à jour manuellement le code pour ces configurations. mParticle et Segment n'offrent pas de moyen de le faire par le biais de leur plateforme. 
- **Web**: L'intégration de Braze doit se faire de manière native pour permettre la configuration minimale d'intégration. Les gestionnaires d'étiquettes n'offrent pas de moyen de le faire par le biais de leur plateforme.
{% endalert %} 

## Données facultatives collectées par défaut

Outre les données d'intégration minimales, les attributs suivants sont automatiquement capturés par Braze lorsque vous initialisez l'intégration SDK. Vous pouvez vous [abstenir de]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection) collecter ces attributs pour permettre une intégration minimale.

| Attribut               | Plateforme          | Description                                                                        | Pourquoi sont-elles collectées                                                                                                                                                      |
|-------------------------|-------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nom du navigateur            | Web               | Nom du navigateur                                                                | Cet attribut est utilisé pour n'envoyer des messages qu'aux navigateurs compatibles. Peut également être utilisé pour une segmentation basée sur le navigateur.                                     |
| Paramètres régionaux de l’appareil           | Android, iOS      | Les paramètres régionaux par défaut de l'appareil                                                   | Cet attribut est utilisé pour traduire les messages dans la langue préférée de l'utilisateur.                                                                                            |
| Modèle d'appareil            | Android, iOS      | Le matériel spécifique de l'appareil                                                | Cet attribut est utilisé pour envoyer des messages uniquement aux appareils compatibles. Peut également être utilisé dans le cadre de la segmentation.                                                 |
| Marque de l'appareil            | Android           | La marque de l'appareil (par exemple, Samsung)                                         | Cet attribut est utilisé pour envoyer des messages uniquement aux appareils compatibles.                                                                                          |
| Opérateur sans fil de l’appareil | Android, iOS      | L'opérateur de téléphonie mobile                                                                 | Cet attribut est utilisé de manière facultative pour le ciblage des messages.<br><br>**Remarque :** Ce champ est obsolète depuis iOS 16 et prendra par défaut la valeur `--` dans une prochaine version d'iOS. |
| Langue                | Android, iOS, Web | Langue de l'appareil ou du navigateur                                                            | Cet attribut est utilisé pour traduire les messages dans la langue préférée de l'utilisateur.                                                                                            |
| Paramètres de notification   | Android, iOS, Web | Si les notifications push sont activées sur cette application.                                   | Cet attribut est utilisé pour activer les notifications push.                                                                                                                    |
| Résolution              | Android, iOS, Web | Résolution de l'appareil ou du navigateur                                                          | Utilisé en option pour le ciblage des messages en fonction de l’appareil. Le format de cette valeur est « `<width>`x`<height>` ».                                                                 |
| Fuseau horaire               | Android, iOS, Web | Fuseau horaire de l'appareil ou du navigateur                                                           | Cet attribut est utilisé pour envoyer les messages à l'heure appropriée, en fonction du fuseau horaire local de chaque utilisateur.                                                   |
| Agent utilisateur              | Web               | [Agent utilisateur](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) | Cet attribut est utilisé pour envoyer des messages uniquement aux appareils compatibles. Peut également être utilisé dans le cadre de la segmentation.                                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Pour en savoir plus sur le suivi des propriétés au niveau de l'appareil (telles que l'opérateur sans fil de l'appareil, le fuseau horaire, la résolution et autres), consultez la documentation spécifique à la plateforme : [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/storage/ "Documentation sur la liste d’autorisation Android"), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/storage/ "Documentation sur la liste d’autorisation iOS"), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/cookies_and_storage/#device-properties "Documentation sur la liste d’autorisation Web").

## Données non collectées par défaut

Par défaut, les attributs suivants ne sont pas collectés. Chaque attribut doit être intégré manuellement.

| Attribut                  | Plateforme     | Description                                                                                                                                                                                                                                                                                                               | Pourquoi les données ne sont pas collectées                                                                                                                                                                                                                                                                 |
|----------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Suivi des campagnes publicitaires activé sur l’appareil  | Android, iOS | Sur iOS :<br>[`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:))<br><br>Sur Android :<br>[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) | Cette propriété nécessite des autorisations supplémentaires au niveau de l'app, qui doivent être accordées par l'intégrateur.                                                                                                                                                                                      |
| IDFA de l’appareil                | iOS          | Identifiant de l'appareil pour les annonceurs                                                                                                                                                                                                                                                                                         | Cela nécessite le cadre de transparence du suivi publicitaire, qui déclenchera un examen supplémentaire de la protection de la vie privée de la part de l'App Store. Pour plus de détails, consultez [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)) |
| ID publicitaire Google      | Android      | Identifiant pour la publicité dans les applications Google Play                                                                                                                                                                                                                                                                        | Pour ce faire, l'application doit récupérer le GAID et le transmettre à Braze. Pour plus de détails, consultez la section [ID publicitaire Google en option]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection).                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Intégration personnalisée

Pour tirer le meilleur parti de Braze, nos intégrateurs SDK mettent souvent en œuvre les SDK de Braze et enregistrent des [attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes), des [événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#logging-custom-events) et des [événements d'achat]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#logging-purchase-events) pertinents pour leur entreprise en plus des données collectées automatiquement.

Une intégration personnalisée permet une communication personnalisée et adaptée à l'expérience de vos utilisateurs.

{% alert important %}
Braze interdira ou bloquera les utilisateurs ayant plus de 5 000 000 de sessions ("utilisateurs fictifs") et n'ingérera plus leurs événements SDK. Pour plus d'informations, consultez la section [Filtrage du spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).
{% endalert %}


[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.enums/-device-key/index.html "Champs au niveau de l'appareil Android"
