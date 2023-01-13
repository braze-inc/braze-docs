---
nav_title: Intégrations TV et OTT
article_title: Intégrations TV et OTT
page_order: 4

description: "Cet article vous donnera des détails sur les fonctionnalités TV et OTT de Braze, les intégrations, les plateformes disponibles et d’autres fonctionnalités."
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
  
---

# Intégrations TV et OTT

Alors que la technologie évolue vers de nouvelles plateformes et de nouveaux appareils, Braze vous ouvre la voie d’une communication facile !

Braze offre différents canaux d’engagement pour plusieurs systèmes d’exploitation TV et des décodeurs « OTT ».

## Plateformes et fonctionnalités

Les fonctionnalités et canaux de messagerie suivants sont pris en charge aujourd’hui.

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
            <th>Type de dispositif</th>
            <th>Données et analyses</th>
            <th>Messages in-app</th>
            <th>Cartes de contenu</th>
            <th>Notifications push</th>
            <th>Canvas</th>
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
            <td>Kindle Fire</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Téléviseur Android</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>LG TV (WebOS)</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">S.O.</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Téléviseur Samsung Tizen</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">S.O.</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-times text-warning"></i></td>
            <td for="push">S.O.</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Apple TV OS</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-times text-warning"></i></td>
            <td for="content-cards"><i class="fas fa-times text-warning"></i></td>
            <td for="push"><i class="fas fa-times text-warning"></i></td>  
            <td for="canvas">S.O.</td>
        </tr>
    </tbody>
</table>

- <i class="fas fa-check text-success"></i> = Pris en charge
- <i class="fas fa-times text-warning"></i> = Non pris en charge par Braze
- S.O. = Non pris en charge par la plateforme

## Guides d’intégration

### Amazon Fire TV

Utilisez le SDK de Braze Fire OS pour intégrer les appareils Amazon Fire TV.

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement multicanal
- Notifications Push (connues sous le nom de [Heads Up Notifications"][7])
  - La priorité doit être définie sur « HIGH » (Élevée) pour qu’elle apparaisse. Toutes les notifications apparaissent dans le menu des paramètres TV Fire.
- Cartes de contenu
- Messages in-app

Consultez le [Guide d’intégration de Fire OS][2] pour plus d’informations.

### Kindle Fire

Utilisez le SDK de Braze Fire OS pour intégrer les appareils Amazon Kindle Fire.

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement multicanal
- Notifications Push
- Cartes de contenu
- Messages in-app

Consultez le [Guide d’intégration de Fire OS][2] pour plus d’informations.

### Téléviseur Android

Utilisez le SDK Android de Braze pour intégrer les appareils Android TV.

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement multicanal
- Cartes de contenu
- Messages in-app 
- &#42; Notifications Push (Intégration manuelle requise)

Voir le [Guide d’intégration SDK pour Android][2] pour plus d’informations.

Les notifications push ne sont pas prises en charge nativement sur Android TV. Pour savoir pourquoi, consultez les [Directives de conception][5] de Google. Cependant, vous pouvez **effectuer une intégration manuelle de l’interface utilisateur de notification Push pour y parvenir**. Voir notre [documentation][6] sur la manière de configurer cela.

{% alert note %}
Assurez-vous de créer une nouvelle application Android dans le tableau de bord de votre intégration Android OTT.
{% endalert %}

### LG WebOS

Utilisez le SDK Web de Braze pour intégrer les [Téléviseurs LG WebOS](http://webostv.developer.lge.com/discover/discover-webos-tv/).

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement multicanal
- Cartes de contenu (via IU personnalisée)
- Messages dans l’application (via l’interface utilisateur personnalisée)

Consultez le [Guide d’intégration de TV connectées][8] pour plus d’informations.

### Tizen Samsung

Utilisez le SDK Web de Braze pour intégrer les [Téléviseurs Samsung Tizen](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement multicanal
- Cartes de contenu (via IU personnalisée)
- Messages dans l’application (via l’interface utilisateur personnalisée)

Consultez le [Guide d’intégration de TV connectées][8] pour plus d’informations.

### Roku

Utilisez le SDK Roku de Braze pour intégrer les [Téléviseurs Roku](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md)

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement multicanal
- Messages dans l’application (via l’interface utilisateur personnalisée)

Consultez le [Guide d’intégration de Roku][3] pour plus d’informations.

### Apple TV OS

Utilisez le SDK iOS de Braze pour recueillir des données et des analyses sur vos utilisateurs de systèmes d’exploitation TV. Ces événements et attributs personnalisés peuvent être utilisés sur vos autres canaux pour la personnalisation et la messagerie promotionnelle.

Voir le [Guide d’intégration SDK pour iOS][4] pour plus d’informations.

## Ciblage des applications

Pour cibler les applications OTT pour la messagerie, nous vous recommandons de créer un segment spécifique à votre application OTT.

![Un segment créé à l’aide de l’application Android OTT.][1]

## Messages dans l’application avec l’interface utilisateur personnalisée

Pour les plateformes prenant en charge des messages dans l’application via une interface utilisateur personnalisée, votre application peut être configurée pour lire le modèle de données reçu par le SDK Braze. Ces informations contiennent les champs configurés dans le tableau de bord (titre, corps, texte du bouton, couleurs, etc.) que votre application peut lire et afficher en conséquence. Ces données peuvent également être utilisées pour personnaliser les modèles de messages de Braze dans l’application dans vos conceptions d’applications existantes.

[1]: {% image_buster /assets/img/android_ott.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/
[5]: https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android_tv_push/
[7]: https://developer.amazon.com/docs/fire-tv/notifications.html#headsup
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/smart_tvs/
