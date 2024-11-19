---
nav_title: Gimbal
article_title: Gimbal
alias: /partners/gimbal/
description: "Cet article de référence décrit le partenariat entre Braze et Gimbal, qui vous permet de perfectionner la pertinence de votre marketing à l'aide de données de localisation."
page_type: partner
search_tag: Partner

---

# Gimbal

> [Gimbal](https://gimbal.com/) vous permet d'améliorer la pertinence de votre marketing à l'aide des données d'emplacement/localisation. Leur SDK d'emplacement/localisation, associé à un logiciel de géorepérage et à des balises, permet d'offrir des expériences mobiles pertinentes, personnalisées et sensibles à la proximité.

Combinez la prise en charge de votre balise ou de votre géorepérage avec les fonctionnalités de ciblage et d'envoi de messages de Braze pour en savoir plus sur les actions physiques de votre utilisateur et lui envoyer un message en conséquence. Cette intégration de partenariat ouvre de nombreux cas d'utilisation pour :

- **Marketing :** Envoyez des messages contextuels pertinents et créez des parcours consommateurs expérientiels.
- **Analyse concurrentielle :** Configurez des déclencheurs autour d'emplacements concurrents pour comprendre les tendances et les habitudes de consommation.
- **Informations sur l’audience :** Comprenez les comportements de visite de vos utilisateurs et segmentez davantage en fonction de ces connaissances.

{% alert note %}
Cette intégration fonctionne de la même manière pour les balises Gimbal et les solutions de géorepérage Gimbal.
{% endalert %}

## Conditions préalables

| Condition| Descriptif|
| ---| ---|
| [Compte du gestionnaire Gimbal][1] | Un compte Gimbal Manager est nécessaire pour profiter de ce partenariat. |
|[SDK de localisation de Gimbal](https://docs.gimbal.com/index.html) | Le SDK Gimbal Location permet de créer des expériences mobiles basées sur la macrolocalisation et la microlocalisation à l'aide de balises de proximité et de géorepérage qui vous permettent de communiquer plus efficacement avec les utilisateurs de votre application. Le SDK doit être mis en œuvre et les géorepérages (ou balises) configurés. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## intégration SDK

Pour intégrer Braze et Gimbal, vous devez déployer le SDK Gimbal Location et créer un compte Gimbal Manager. Les intégrations suivantes pour Android, FireOS et iOS créeront un événement personnalisé unique pour chaque nouvel endroit qu'un utilisateur accède. Ces événements pourront ensuite être utilisés pour le déclenchement et le reciblage de vos campagnes et de vos Canvases.

Si vous prévoyez de créer plus de 50 lieux, nous vous recommandons de créer un événement `Places Entered` personnalisé générique et d'ajouter le nom du lieu en tant que propriété de l'événement. 

1. Intégrez le [SDK Gimbal][2] pour Android et iOS dans votre application en suivant les instructions de la [documentation de Gimbal][3].
2. Utilisez l'[API REST Place][4] de Gimbal pour obtenir un utilisateur`places`.
3. [Associez votre compte Gimbal à Braze en saisissant la clé API Braze REST.][5]
4. Configurez des [événements personnalisés][6] dans le SDK de Braze. Vous pouvez intégrer Gimbal à Braze pour [Android, FireOS][7] et [iOS][8].
5. Consignez les propriétés de ces événements (nom du lieu, durée du séjour).
6. Utilisez ces propriétés et ces événements pour déclencher des campagnes et des Canvases in Braze. 

[1]: https://manager.gimbal.com/login/users/sign_in
[2]: https://manager.gimbal.com/sdk_downloads
[3]: https://docs.gimbal.com/
[4]: https://docs.gimbal.com/rest.html
[5]: https://manager.gimbal.com/apps
[6]: {{site.baseurl}}/user_guide/data_and_analytics/Custom_Data/custom_events/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons