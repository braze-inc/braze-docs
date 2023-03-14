---
nav_title: Gimbal
article_title: Gimbal
alias: /partners/gimbal/
description: "Cet article décrit le partenariat entre Braze et Gimbal, qui vous permet de perfectionner votre pertinence marketing en utilisant les données de localisation."
page_type: partner
search_tag: Partenaire

---

# Gimbal

> [Gimbal](https://gimbal.com/) vous permet de perfectionner votre pertinence marketing en utilisant les données de localisation. Leur SDK de localisation, associé à un logiciel de géorepérage et à des balises, permet de créer des expériences mobiles pertinentes, personnalisées et adaptées à la proximité.

Combinez votre support de balise ou de geofence avec les fonctionnalités de ciblage et d’envois de messages de Braze pour en savoir plus sur les actions physiques de vos utilisateurs et leur envoyer des messages en conséquence. Cette intégration de partenariat ouvre un éventail de cas d’utilisation pour :
- **Marketing :** Envoyez des messages contextuellement pertinents et construisez des voyages d’expérience client.
- **Analyse concurrentielle :** Configurez des déclencheurs autour des sites concurrents pour comprendre les tendances et les comportements des consommateurs.
- **Informations sur l’audience :** Comprenez les comportements de visite de vos utilisateurs et affinez votre segmentation sur la base de ces apprentissages.

## Conditions préalables

| Condition| Description|
| ---| ---|
| [Compte de gestionnaire Gimbal][1] | Un compte de gestionnaire Gimbal est requis pour profiter de ce partenariat. |
|[SDK de localisation Gimbal](https://docs.gimbal.com/index.html) | Le kit SDK Location de Gimbal permet de créer des expériences mobiles basées sur la macro et la micro localisation à l’aide de balises de proximité et de geofences qui vous permettent de communiquer plus efficacement avec les utilisateurs de vos applications. Vous devez disposer du SDK implémenté et des geofences (ou balises) configurées. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration SDK

Pour intégrer Braze et Gimbal, vous devez mettre en œuvre le SDK Location de Gimbal et créer un compte de gestionnaire Gimbal. Les intégrations suivantes pour Android, FireOS et iOS créeront un événement personnalisé unique pour chaque nouvel endroit où un utilisateur entre. Ces événements peuvent ensuite être utilisés pour le déclenchement et le reciblage dans vos campagnes et vos Canvas.

Si vous prévoyez de créer plus de 50 lieux, nous vous recommandons de créer un événement personnalisé `Lieux visités` générique et d’ajouter le nom du lieu comme propriété de l’événement. 

1. Intégrez le [SDK Gimbal][2] pour Android et iOS dans votre application en suivant les instructions de la [documentation Gimbal][3].
2. Utilisez l’[API REST place][4] de Gimbal pour obtenir la valeur `places` de l’utilisateur.
3. Connectez votre compte Gimbal à Braze en saisissant la [clé d’API REST][5] de Braze.
4. Configurez les [événements personnalisés][6] dans le SDK Braze. Vous pouvez intégrer Gimbal à Braze pour [Android, FireOS][7] et [iOS][8].
5. Enregistrez les propriétés de ces événements (Nom du lieu, Durée de séjour).
6. Utilisez ces propriétés et événements pour déclencher des campagnes et des Canvas dans Braze. 

[1]: https://manager.gimbal.com/login/users/sign_in
[2]: https://manager.gimbal.com/sdk_downloads
[3]: https://docs.gimbal.com/
[4]: https://docs.gimbal.com/rest.html
[5]: https://manager.gimbal.com/apps
[6]: {{site.baseurl}}/user_guide/data_and_analytics/Custom_Data/custom_events/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons