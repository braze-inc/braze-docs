---
nav_title: Collecte de données SDK
article_title: Collecte de données SDK
page_order: 1
page_type: reference
description: "Cet article de référence traite des données qui sont collectées par le SDK à travers une intégration personnalisée, d’une intégration collectée automatiquement et d’une intégration minimale."

---

# Options de collecte de données du SDK

Braze est conçu pour permettre une collecte de données flexible via nos SDK et API. Le SDK de Braze peut être intégré de trois façons :
- **Intégration personnalisée** ; les intégrateurs ont la possibilité de collecter des données en plus des données collectées automatiquement.
- **Intégration collectée automatiquement** ; les intégrateurs peuvent bénéficier des données collectées automatiquement (ce qui inclut toutes les données d’intégration minimale) sans avoir à intégrer des données supplémentaires.
- **Intégration minimale** ; les intégrateurs peuvent désactiver les données collectées automatiquement pour ne recevoir que les données strictement nécessaires pour permettre la communication avec les services Braze. 

## Intégration personnalisée 

Pour tirer le meilleur parti des fonctionnalités de la plate-forme Braze, les intégrateurs mettent le plus souvent en œuvre les SDK Braze et enregistrent [les attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes), [les événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#logging-custom-events) et [les événements d’achat]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#logging-purchase-events) qui sont pertinents pour leur activité en plus des données collectées automatiquement (y compris l’intégration minimale). 

Une intégration personnalisée permet une communication adaptée à l’expérience de l’utilisateur. 

## Intégration collectée automatiquement

La liste suivante énumère les données automatiquement capturées, générées et reçues par Braze lorsqu’un intégrateur initialise le SDK ; ceci inclut les propriétés trouvées dans le tableau d’intégration minimale.

| Attribut | Plateforme | Description | Pourquoi sont-elles collectées |
| --------- | -------- | ----------- | ------------------ |
| Nom du navigateur | Web | Nom du navigateur. | Utilisé pour garantir que les messages ne sont envoyés qu’aux navigateurs compatibles. Peut également être utilisé pour une segmentation basée sur le navigateur. |
| Fuseau horaire | Android, iOS, Web | Fuseau horaire de l’appareil/navigateur. | Utilisé pour garantir que les messages sont envoyés à l’heure appropriée, en fonction du fuseau horaire local de chaque utilisateur. |
| Résolution | Android, iOS, Web | Résolution de l’appareil/navigateur. | Utilisé en option pour le ciblage des messages en fonction de l’appareil. |
| Langue | Android, iOS, Web | Langue de l’appareil/navigateur. | Utilisé pour traduire les messages dans la langue préférée de l’utilisateur. |
| Agent de l’utilisateur | Web | [Agent utilisateur](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent). | Utilisé pour s’assurer que les messages ne sont envoyés qu’aux appareils compatibles. Peut également être utilisé dans le cadre de la segmentation. |
| Emplacement de l’appareil | Android, iOS | Emplacement par défaut de l’appareil. | Utilisé pour traduire les messages dans la langue préférée de l’utilisateur. |
| Modèle de l’appareil | Android, iOS | Le matériel spécifique de l’appareil. | Utilisé pour s’assurer que les messages ne sont envoyés qu’aux appareils compatibles. Peut également être utilisé dans le cadre de la segmentation. |
| Transporteur sans fil de l’appareil | Android, iOS | L’opérateur mobile. | Utilisé de manière facultative pour le ciblage des messages. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Tous ces champs peuvent être désactivés pour permettre une intégration minimale : 
- Android : [champs au niveau de l’appareil][1], [documentation de la liste des autorisations]({{site.baseurl}}/developer_guide/platform_integration_guides/android/storage/ "Android allowlist documentation")
- iOS : [champs au niveau de l’appareil](https://github.com/Appboy/appboy-ios-sdk/blob/16e893f2677af7de905b927505d4101c6fb2091d/AppboyKit/headers/AppboyKitLibrary/Appboy.h#L181 « champs au niveau de l’appareil iOS »), [documentation de la liste des autorisations]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/storage/ "iOS allowlist documentation")
- Web : [champs au niveau de l’appareil](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.deviceproperties.html « champs au niveau de l’appareil Web»), [documentation de la liste des autorisations]({{site.baseurl}}/developer_guide/platform_integration_guides/web/cookies_and_storage/#device-properties "Web allowlist documentation")

## Intégration minimale

La liste suivante énumère les données strictement nécessaires générées et reçues par Braze lorsqu’un intégrateur choisit d’initialiser le SDK pour la communication et de désactiver les données capturées automatiquement. Ces éléments ne sont pas configurables et sont essentiels dans les fonctions centrales de la plateforme. 

| Attribut | Plateforme | Description | Pourquoi sont-elles collectées |
| --------- | -------- | ----------- | ------------------ |
| OS et version de l’OS | Android, iOS, Web | Appareil/navigateur et version de l’appareil/navigateur actuellement signalés. | Utilisé pour s’assurer que les messages ne sont envoyés qu’aux appareils compatibles. Peut également être utilisé dans le cadre d’une segmentation pour cibler les utilisateurs qui doivent mettre à jour leurs applications. |
| IDFV | iOS | Identifiant de l’appareil. Le recueil des IDFV est désormais facultatif sur notre [SDK Swift](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/swift_idfv/) | Utilisé pour différencier les appareils des utilisateurs et s’assurer que les messages sont envoyés au bon appareil. |
| ID de l’appareil | Android, iOS, Web | Identifiant de l’appareil, une chaîne de caractères générée de façon aléatoire. | Utilisé pour différencier les appareils des utilisateurs et s’assurer que les messages sont envoyés au bon appareil. |
| ID de la session et horodatage de la session | Android, iOS, Web | Identifiant de la session, une chaîne de caractères générée de façon aléatoire et un horodatage de la session. | Utilisé pour déterminer si l’utilisateur démarre une nouvelle session ou une session existante et pour déterminer la rééligibilité des messages destinés à cet utilisateur.<br><br>Certains canaux de communication, tels que les messages in-app et les cartes de contenu, sont synchronisés sur l’appareil au début de la session. Notre backend utilisera ensuite les données relatives à la date du dernier contact avec les serveurs de Braze (que l’appareil stocke et renvoie) pour savoir si l’utilisateur peut recevoir de nouveaux messages.|
| Version du SDK | Android, iOS, Web | Version actuelle du SDK. | Utilisée pour s’assurer que les messages ne sont envoyés qu’aux appareils compatibles et pour éviter toute perturbation du service. |
| Nom-de-la-version-de-l’application /<br> Code-de-version-de-l’application | Android, iOS, Web | Nom de la version de l’application. | Utilisé pour garantir que les messages relatifs à la compatibilité des versions des applications sont envoyés aux bons appareils. Peut être utilisé pour informer les utilisateurs d’une interruption de service ou d’un bogue. |
| Données d’interaction des messages SDK | Android, iOS, Web | Ouvertures directes par notification push, interactions avec les messages in-app, interactions avec les cartes de contenu. | Utilisées à des fins de contrôle de la qualité, comme vérifier qu’un message a été reçu et que l’envoi n’est pas dupliqué.|
| Pays | Android, iOS | Pays | Identifié par la géolocalisation de l’adresse IP. Utilisé pour cibler les messages en fonction de l’emplacement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Le backend/service Braze génère des indicateurs calculés sur les données SDK (par exemple, le nombre total d’événements de conversion de sessions, [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/), etc.), les données d’interaction de message liées aux messages non SDK (par exemple, les envois de SMS), et les informations dérivées, par exemple, une désinstallation à partir du rebondissement d’une notification push. Pour plus de clarté, ces données calculées ne sont pas suivies par le SDK mais générées par les services Braze, et l’exportation d’un profil d’utilisateur affichera à la fois les données suivies et les données générées.

{% alert important %}
Si vous êtes intéressé par l’intégration minimale uniquement et que vous intégrez mParticle, Segment, Tealium ou GTM, notez ce qui suit :
- **Plateformes mobiles** : Vous devez mettre à jour manuellement le code pour ces configurations. mParticle et Segment ne proposent pas de moyen de le faire via leur plateforme. 
- **Web :** L’intégration de Braze doit se faire de manière native pour permettre la configuration de l’intégration minimale. Les gestionnaires de balises n’offrent pas de moyen de le faire via leur plateforme. 

{% endalert %} 

[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.appboy.enums/-device-key/index.html "Android device-level fields"
