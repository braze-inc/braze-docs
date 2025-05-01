---
nav_title: Infillion
article_title: Infillion
alias: /partners/infillion/
description: ""
page_type: partner
search_tag: Partner

---

# Infillion

>  Leur SDK d'emplacement/localisation, associé à un logiciel de géorepérage et à des balises, permet d'offrir des expériences mobiles pertinentes, personnalisées et sensibles à la proximité.

 Cette intégration de partenariat ouvre de nombreux cas d'utilisation pour :

- **Marketing :** Envoyez des messages contextuels pertinents et créez des parcours consommateurs expérientiels.
- **Analyse concurrentielle :** Configurez des déclencheurs autour d'emplacements concurrents pour comprendre les tendances et les habitudes de consommation.
- **Informations sur l’audience :** Comprenez les comportements de visite de vos utilisateurs et segmentez davantage en fonction de ces connaissances.

{% alert note %}

{% endalert %}

## Conditions préalables

| Condition| Description|
| ---| ---|
|  |  |
| |  Le SDK doit être mis en œuvre et les géorepérages (ou balises) configurés. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration SDK

 Les intégrations suivantes pour Android, FireOS et iOS créeront un événement personnalisé unique pour chaque nouvel endroit qu'un utilisateur accède. Ces événements pourront ensuite être utilisés pour le déclenchement et le reciblage de vos campagnes et de vos Canvases.

Si vous prévoyez de créer plus de 50 lieux, nous vous recommandons de créer un événement `Places Entered` personnalisé générique et d'ajouter le nom du lieu en tant que propriété de l'événement. 

1. 
2. 
3. 
4. Configurez des [événements personnalisés][6] dans le SDK de Braze. 
5. Consignez les propriétés de ces événements (nom du lieu, durée du séjour).
6. Utilisez ces propriétés et ces événements pour déclencher des campagnes et des Canvases in Braze. 

[1]: https://manager.gimbal.com/login/users/sign_in
[2]: https://manager.gimbal.com/sdk_downloads
[3]: https://docs.gimbal.com/
[4]: https://docs.gimbal.com/rest.html
[5]: https://manager.gimbal.com/apps
[6]: {{site.baseurl}}/user_guide/data/custom_data/custom_attributes/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons