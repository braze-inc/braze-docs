---
nav_title: Intégrations TV et OTT
article_title: Intégrations TV et OTT
page_order: 4
description: "Cet article vous donnera des détails sur les fonctionnalités de Braze TV et OTT, les intégrations, les plates-formes disponibles, et d'autres capacités."
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - Pare-feu
---

# Intégrations TV et OTT

Tandis que la technologie évolue vers de nouvelles plates-formes et dispositifs, votre messagerie avec le Brésil!

Braze offre différents canaux d'engagement pour un certain nombre de systèmes d'exploitation TV différents et "OTT" Set Top Boxes.

## Plateformes et fonctionnalités

Voici une liste des fonctionnalités et des canaux de messagerie pris en charge aujourd'hui.

<style>
#tv-feature-table td,
#tv-feature-table th {
    text-align: center !important;
    vertical-align: center;
}

</style>
<table id="tv-feature-table">
    <thead>
        <tr>
            <th>Type de périphérique</th>
            <th>Données et analyses</th>
            <th>Messages In-App</th>
            <th>Cartes de contenu</th>
            <th>Notifications push</th>
            <th>Toile</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Feu de Kindle</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>TV Android</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>LG TV (webOS)</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">N/A</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Samsung Tizen TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">N/A</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-times text-warning"></i></td>
            <td for="content-cards"><i class="fas fa-times text-warning"></i></td>
            <td for="push">N/A</td>
            <td for="canvas">N/A</td>
        </tr>
        <tr>
            <td>Apple TV OS</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-times text-warning"></i></td>
            <td for="content-cards"><i class="fas fa-times text-warning"></i></td>
            <td for="push"><i class="fas fa-times text-warning"></i></td>  
            <td for="canvas">N/A</td>
        </tr>
    </tbody>
</table>

- <i class="fas fa-check text-success"></i> = Prise en charge
- <i class="fas fa-times text-warning"></i> = Non pris en charge par Braze
- N/A = Non pris en charge par la plateforme

## Guides d'intégration

### Amazon Fire TV

Utilisez le SDK Fire OS de Braze pour intégrer les appareils Amazon Fire TV.

Les fonctionnalités incluent :

- Collecte de données et analyses pour l'engagement inter-canal
- Notifications push (connues sous le nom de ["Notifications flottantes"][7])
  - La priorité doit être définie à "HAUTE" pour que ceux-ci apparaissent. Toutes les notifications apparaissent dans le menu Paramètres de Fire TV.
- Cartes de contenu
- Messages In-App

Pour plus d'informations, consultez le [Guide d'intégration de Fire OS][2].

### Feu de Kindle

Utilisez le SDK Fire OS de Braze pour intégrer avec les appareils Amazon Kindle Feu.

Les fonctionnalités incluent :

- Collecte de données et analyses pour l'engagement inter-canal
- Notifications push
- Cartes de contenu
- Messages In-App

Pour plus d'informations, consultez le [Guide d'intégration de Fire OS][2].

### TV Android

Utilisez le SDK Android de Braze pour intégrer avec les appareils Android TV.

Les fonctionnalités incluent :

- Collecte de données et analyses pour l'engagement inter-canal
- Cartes de contenu
- Messages In-App
- &#42; Notifications push (intégration manuelle requise, voir ci-dessous)

Pour plus d'informations, consultez le [Guide d'intégration Android SDK][2].

Les notifications push ne sont pas prises en charge nativement sur Android TV. Pour plus d'informations pourquoi, consultez les [Directives de conception][5] de Google. Vous pouvez cependant __faire une intégration manuelle de l'interface de notification Push pour atteindre ceci__. Veuillez consulter notre [documentation][6] sur la façon de configurer cela.

### LG webOS

Utilisez le SDK Web de Braze pour intégrer avec [LG webOS TVs](http://webostv.developer.lge.com/discover/discover-webos-tv/).

Les fonctionnalités incluent :

- Collecte de données et analyses pour l'engagement inter-canal
- Cartes de contenu (via l'interface utilisateur personnalisée)
- Messages dans l'application (via l'interface utilisateur personnalisée)

Pour plus d'informations, consultez le [Guide d'intégration Web Smart TV][8].

### Samsung Tizen

Utilisez le SDK Web de Braze pour intégrer avec les [téléviseurs Samsung Tizen](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Les fonctionnalités incluent :

- Collecte de données et analyses pour l'engagement inter-canal
- Cartes de contenu (via l'interface utilisateur personnalisée)
- Messages dans l'application (via l'interface utilisateur personnalisée)

Pour plus d'informations, consultez le [Guide d'intégration Web Smart TV][8].

### Roku

Utilisez Braze Roku SDK pour collecter des données et des analyses sur vos utilisateurs Roku. Ces événements et attributs personnalisés peuvent être utilisés sur vos autres canaux pour la personnalisation et la messagerie promotionnelle.

La possibilité d'envoyer des messages In-App à vos utilisateurs Roku sera bientôt disponible - restez à l'écoute !

Pour plus d'informations, visitez le [Guide d'intégration Roku][3].

### Apple TV OS

Utilisez le SDK iOS de Braze pour collecter des données et des analyses sur vos utilisateurs de TV OS. Ces événements et attributs personnalisés peuvent être utilisés sur vos autres canaux pour la personnalisation et la messagerie promotionnelle.

Pour plus d'informations, consultez le [Guide d'intégration du SDK iOS][4].

## Message intégré avec une interface utilisateur personnalisée

Pour les plates-formes qui prennent en charge les messages In-App via une interface utilisateur personnalisée, votre application peut être configurée pour lire le modèle de données reçu par Braze SDK. Cette information contiendra les champs configurés dans le tableau de bord (titre, corps, texte du bouton, couleurs, etc.) que votre application peut lire et afficher en conséquence. Ces données peuvent également être utilisées pour personnaliser les modèles de messages intégrés natifs de Braze dans vos conceptions d'applications existantes.

[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/

[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/
[5]: https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android_tv_push/
[7]: https://developer.amazon.com/docs/fire-tv/notifications.html#headsup
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/smart_tvs/
