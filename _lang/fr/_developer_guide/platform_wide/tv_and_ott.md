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
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fa-solid fa-minus"></i></td>  
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
    </tbody>
</table>

- <i class="fas fa-check text-success"></i> = Pris en charge
- <i class="fa-solid fa-minus"></i> = Assistance partielle
- <i class="fas fa-times text-warning"></i> = Non pris en charge par Braze
- S.O. = Non pris en charge par la plateforme OTT

## Guides d’intégration

### Amazon Fire TV

Utilisez le SDK de Braze Fire OS pour intégrer les appareils Amazon Fire TV.

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement multicanal
- Notifications Push (connues sous le nom de [Heads Up Notifications"][7])
  - La priorité doit être définie sur « HIGH » (Élevée) pour qu’elle apparaisse. Toutes les notifications apparaissent dans le menu des paramètres TV Fire.
- Cartes de contenu
- Messages in-app
  - Pour afficher les messages HTML sur des environnements non tactiles comme les TV, configurez `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` sur `false` (disponible sur[Android SDK v23.1.0][android-tv-html])

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
  - Pour afficher les messages HTML sur des environnements non tactiles comme les TV, configurez `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` sur `false` (disponible sur[Android SDK v23.1.0][android-tv-html])
- &#42; Notifications Push (Intégration manuelle requise)

Voir le [Guide d’intégration SDK pour Android][2] pour plus d’informations.

Les notifications push ne sont pas prises en charge nativement sur Android TV. Pour savoir pourquoi, consultez les [Directives de conception][5].de Google. Cependant, vous pouvez **effectuer une intégration manuelle de l’interface utilisateur de notification Push pour y parvenir**. Voir notre [documentation][6] sur la manière de configurer cet élément.

{% alert note %}
Assurez-vous de créer une nouvelle application Android dans le tableau de bord de votre intégration Android OTT.
{% endalert %}

### LG WebOS

Utilisez le SDK Web de Braze pour intégrer les [Téléviseurs LG WebOS](https://webostv.developer.lge.com/discover).

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement multicanal
- Cartes de contenu (via [Interface utilisateur Headless](#custom-ui))
- Messages in-app (via [Interface utilisateur Headless](#custom-ui))

Consultez le [Guide d’intégration de TV connectées][8] pour plus d’informations.

### Tizen Samsung

Utilisez le SDK Web de Braze pour intégrer les [Téléviseurs Samsung Tizen](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement multicanal
- Cartes de contenu (via [Interface utilisateur Headless](#custom-ui))
- Messages in-app (via [Interface utilisateur Headless](#custom-ui))

Consultez le [Guide d’intégration de TV connectées][8] pour plus d’informations.

### Roku

Utilisez le SDK Roku de Braze pour intégrer les [Téléviseurs Roku](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md)

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement multicanal
- Messages in-app (via [Interface utilisateur Headless](#custom-ui))

Consultez le [Guide d’intégration de Roku][3] pour plus d’informations.

### Apple TV OS

Utilisez le SDK Swift de Braze pour réaliser une intégration sur tvOS

Voir le [Guide d’intégration SDK Swift pour iOS pour plus d’informations][4].

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement multicanal
- Cartes de contenu (via [Interface utilisateur Headless](#custom-ui))
- Messages in-app (via [Interface utilisateur Headless](#custom-ui))
- Notification push silencieuses et mise à jour des badges

**Note**: Pour éviter d’afficher des messages in-app mobiles à vos utilisateurs de TV, assurez-vous de configurer soit [App Targeting](#app-targeting) (Ciblage application) ou d’utiliser les paires clé-valeur pour filtrer les messages. Par exemple, afficher uniquement les messages tvOS s’ils contiennent une `tv = true` paire clé-valeur spéciale.

## Ciblage de l’application {#app-targeting}

Pour cibler les applications OTT pour la messagerie, nous vous recommandons de créer un segment spécifique à votre application OTT.

![Un segment créé à l’aide de l’application Android OTT.][1]

## Interface utilisateur Headless {#custom-ui}

Pour les plateformes compatibles avec les messages in-app ou avec les Cartes de contenu via l’Interface utilisateur Headless, Braze fournira un modèle de données (c’est-à-dire, JSON) lisible par votre application et utilisable dans une Interface utilisateur commandée par votre application. Ces plateformes ne comprennent pas les Interfaces utilisateurs ou les Vues prêtes à l’emploi.

Ces informations contiendront les champs configurés dans le tableau de bord (titre, corps, texte du bouton, couleurs, etc.) que votre application peut lire et afficher en conséquence.

En savoir plus sur la gestion personnalisée de l’envoi de messages :

**Android SDK**
- [Personnalisation des messages in-app](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/)
- [Personnalisation des cartes de contenu](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/content_cards/implementation_guide/)

**Swift SDK**
- [Personnalisation des messages in-app](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [Personnalisation des cartes de contenu](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**Web SDK**
- [Personnalisation des messages in-app](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/in-app_messaging/customization/key_value_pairs)
- [Personnalisation des cartes de contenu](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/content_cards/customization/custom_ui/)
 

[1]: {% image_buster /assets/img/android_ott.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/
[4]: https://github.com/braze-inc/braze-swift-sdk
[5]: https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android_tv_push/
[7]: https://developer.amazon.com/docs/fire-tv/notifications.html#headsup
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/smart_tvs/
[android-tv-html]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310
