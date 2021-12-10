---
nav_title: Gimbal
article_title: Gimbal
alias: /fr/partners/gimbal/
description: "Cet article décrit le partenariat entre Braze et Gimbal, qui vous permet de perfectionner votre pertinence marketing en utilisant les données de localisation."
page_type: partenaire
search_tag: Partenaire
---

# Gimbal

> [Gimbal](https://gimbal.com/) vous permet de perfectionner votre pertinence marketing en utilisant les données de localisation. Leur emplacement SDK jumelé à des logiciels de géorepérage et des balises de puissance pertinentes, des expériences mobiles personnalisées et respectueuses de la proximité.

Combinez votre support de balises ou de géorepérage avec les fonctionnalités de ciblage et de messagerie de Braze pour en savoir plus sur les actions physiques de votre utilisateur et les envoyer en conséquence. Cette intégration de partenariat ouvre un tableau de cas d'utilisation pour:
- __Marketing :__ Envoyez des messages contextuels pertinents et construisez des voyages de consommation expérimentaux.
- __Analyse compétitive :__ Mettre en place des déclencheurs autour de lieux compétitifs pour comprendre les tendances et les pratiques des consommateurs.
- __Aperçus publics :__ Comprendre les comportements de visite de vos utilisateurs et le segment ultérieur basé sur ces apprentissages.

## Pré-requis

| Exigences                                                                | Libellé                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [SDK de l'emplacement de la nacelle](https://docs.gimbal.com/index.html) | Le SDK de localisation Gimbal permet de mettre en œuvre des expériences mobiles basées sur la macro et la micro localisation en utilisant des balises de proximité et des géorepérages qui vous permettent de communiquer plus efficacement avec les utilisateurs de votre application. Vous devez avoir le SDK implémenté et les géorepérages (ou balises). |
| [Compte Gimbal][1]                                                       | Vous devez avoir un compte Gimbal manager actif pour utiliser leurs services avec Braze                                                                                                                                                                                                                                                                      |
| Braze clé API REST                                                       | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__                                                                                                                                                 |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration du SDK

Pour intégrer Braze et Gimbal, vous devez implémenter le SDK Gimbal Location et créer un compte Gimbal manager. Les intégrations pour Android, FireOS et iOS ci-dessous créeront un événement personnalisé unique pour chaque nouvel endroit où un utilisateur entre, ces événements peuvent ensuite être utilisés pour déclencher et retargeter dans vos campagnes et Canvases.

Si vous prévoyez de créer plus de 50 places, nous vous recommandons de créer un événement personnalisé générique `Lieux entrés` et d'ajouter le nom du lieu en tant que propriété d'événement.

1. Intégrez le [SDK Gimbal][2] pour Android et iOS dans votre application en suivant les instructions de la [documentation Gimbal][3].
2. Utilisez la [place REST API][4] de Gimbal pour obtenir les `places de l'utilisateur`.
3. Associez votre compte Gimbal à Braze en entrant la clé [REST API de Braze][5].
4. Configurez [événements personnalisés][6] dans le Braze SDK. Vous pouvez intégrer Gimbal avec Braze pour [Android et FireOS][7] et [iOS][8].
5. Propriétés de log pour ces événements (Place Name, Dwell Time).
6. Utilisez ces propriétés et événements pour déclencher des campagnes et des Canvases au Brésil.

[1]: https://manager.gimbal.com/login/users/sign_in
[2]: https://manager.gimbal.com/sdk_downloads
[3]: https://docs.gimbal.com/
[4]: https://docs.gimbal.com/rest.html
[5]: https://manager.gimbal.com/apps
[6]: {{site.baseurl}}/user_guide/data_and_analytics/Custom_Data/custom_events/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons