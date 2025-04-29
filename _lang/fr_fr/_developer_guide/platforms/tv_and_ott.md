---
nav_title: Télévision et OTT
article_title: Intégrations TV et OTT pour Braze
page_order: 15

description: "Cet article vous donnera des détails sur les fonctionnalités TV et OTT de Braze, les intégrations, les plateformes disponibles et d’autres fonctionnalités."
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
---

# Intégrations TV et OTT

> Alors que la technologie évolue vers de nouvelles plateformes et de nouveaux appareils, Braze vous ouvre la voie d’une communication facile ! Braze propose différents canaux d'engagement pour un certain nombre de systèmes d'exploitation télévisuels et de méthodes de réception/distribution de contenu OTT (Over-the-Top).

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
            <th>Type d’appareil</th>
            <th>Données et analyses</th>
            <th>in-app Messages</th>
            <th>Cartes de contenu</th>
            <th>Notifications push</th>
            <th>Canvas</th>
            <th>Indicateurs de fonctionnalité</th>
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
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Kindle Fire</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>LG TV (WebOS)</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">S.O.</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Téléviseur Samsung Tizen</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">S.O.</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-times text-warning"></i></td>
            <td for="push">S.O.</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Apple TV OS</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
             <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fa-solid fa-minus"></i></td>  
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
       <tr>
          <td>Apple Vision Pro</td>
          <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
           <td for="iam"><i class="fas fa-check text-success"></i></td>
          <td for="content-cards"><i class="fas fa-check text-success"></i></td>
          <td for="push"><i class="fa-solid fa-minus"></i></td>  
          <td for="canvas"><i class="fas fa-check text-success"></i></td>
          <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
      </tr>
    </tbody>
</table>

- <i class="fas fa-check text-success"></i> = Pris en charge
- <i class="fa-solid fa-minus"></i> = Assistance partielle
- <i class="fas fa-times text-warning"></i> = Non pris en charge par Braze
- S.O. = Non pris en charge par la plateforme OTT

## Guides d’intégration

### Amazon Fire TV {#fire-tv}

Utilisez le SDK Fire OS de Braze pour l'intégration avec les appareils Amazon Fire TV.

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement cross-canal
- Notifications push (connues sous le nom de ["Heads Up Notifications")](https://developer.amazon.com/docs/fire-tv/notifications.html#headsup)
  - La priorité doit être définie sur « HIGH » (Élevée) pour qu’elle apparaisse. Toutes les notifications apparaissent dans le menu des paramètres TV Fire.
- Cartes de contenu
- Indicateurs de fonctionnalité
- in-app Messages
  - Pour afficher les messages HTML sur des environnements non tactiles tels que les téléviseurs, définissez `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` sur `false` (disponible à partir de la [version 23.1.0 du SDK Android)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310).

Pour plus d'informations, consultez le [guide d'intégration de Fire OS.]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)

### Kindle Fire {#kindle-fire}

Utilisez le SDK Braze Fire OS pour intégrer les appareils Amazon Kindle Fire.

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement cross-canal
- Notifications push
- Cartes de contenu
- Indicateurs de fonctionnalité
- in-app Messages

Pour plus d'informations, consultez le [guide d'intégration de Fire OS.]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)

### Android TV {#android-tv}

Utilisez le SDK Android de Braze pour intégrer les appareils Android TV.

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement cross-canal
- Cartes de contenu
- Indicateurs de fonctionnalité
- in-app Messages 
  - Pour afficher les messages HTML sur des environnements non tactiles tels que les téléviseurs, définissez `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` sur `false` (disponible à partir de la [version 23.1.0 du SDK Android)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310).
- \* Notifications push (intégration manuelle requise)
  - Les notifications push ne sont pas prises en charge nativement sur Android TV. Pour en savoir plus, consultez les [règles de conception de](https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html) Google. Vous pouvez toutefois **procéder à une intégration manuelle de l'interface utilisateur des notifications push pour y parvenir.** Consultez notre [documentation]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android%20tv) pour savoir comment procéder.

Pour plus d'informations, consultez le [guide d'intégration SDK Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).

{% alert note %}
Assurez-vous de créer une nouvelle application Android dans le tableau de bord de votre intégration Android OTT.
{% endalert %}

### LG webOS {#lg-webos}

Utilisez le SDK Web de Braze pour intégrer les [téléviseurs LG webOS](https://webostv.developer.lge.com/discover).

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement cross-canal
- Cartes de contenu (via [Interface utilisateur Headless](#custom-ui))
- Indicateurs de fonctionnalité
- Messages in-app (via [Headless UI)](#custom-ui)

Pour plus d'informations, consultez le [guide d'intégration de la TV connectée Web.]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs/)

### Samsung Tizen {#tizen}

Utilisez le SDK Web de Braze pour intégrer les [téléviseurs Samsung Tizen](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement cross-canal
- Cartes de contenu (via [Interface utilisateur Headless](#custom-ui))
- Indicateurs de fonctionnalité
- Messages in-app (via [Headless UI)](#custom-ui)

Pour plus d'informations, consultez le [guide d'intégration de la TV connectée Web.]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs/)

### Roku {#roku}

Utilisez le SDK Roku de Braze pour l'intégration avec les [téléviseurs Roku](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md).

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement cross-canal
- Messages in-app (via [Headless UI)](#custom-ui)
  - Les Webviews ne sont pas prises en charge par la plateforme Roku. Par conséquent, les messages in-app HTML ne sont pas pris en charge.
- Indicateurs de fonctionnalité

Pour plus d'informations, consultez le [guide d'intégration Roku]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=roku).

### Apple TV OS {#tvos}

Utilisez le SDK Swift de Braze pour l'intégration avec tvOS. Gardez à l'esprit que le SDK Swift n'inclut aucune interface utilisateur ou vue par défaut pour tvOS, vous devrez donc implémenter les vôtres.

Les fonctionnalités comprennent :

- Recueil de données et d’analyses pour l’engagement cross-canal
- Cartes de contenu (via [Interface utilisateur Headless](#custom-ui))
- Indicateurs de fonctionnalité
- Messages in-app (via [Headless UI)](#custom-ui)
  - Les Webviews ne sont pas prises en charge par la plateforme tvOS. Par conséquent, les messages in-app HTML ne sont pas pris en charge.
  - Consultez notre [exemple d'application](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui) pour en savoir plus sur l'utilisation d'une interface utilisateur sans tête pour un envoi personnalisé de messages sur tvOS.
- Notification push silencieuses et mise à jour des badges

Pour plus d'informations, consultez le [guide d'intégration SDK Swift pour iOS](https://github.com/braze-inc/braze-swift-sdk).

{% alert note %}
Pour éviter d'afficher des messages in-app mobiles à vos utilisateurs TV, veillez à configurer soit [le ciblage App](#app-targeting), soit l'utilisation de paires clé-valeur pour filtrer les messages. Par exemple, afficher uniquement les messages tvOS s’ils contiennent une `tv = true` paire clé-valeur spéciale.
{% endalert %}

### Apple Vision Pro {#vision-pro}

Utilisez le SDK Swift de Braze pour l’intégration avec visionOS. La plupart des fonctionnalités disponibles sur iOS sont également disponibles sur visionOS, notamment :

- Analyse/analytique (sessions, événements personnalisés, achats, etc.)
- Envoi de messages in-app (modèles de données et interface utilisateur)
- Cartes de contenu (modèles de données et interface utilisateur)
- Notifications push (visibles par l'utilisateur grâce à des boutons d'action et à des notifications silencieuses)
- Indicateurs de fonctionnalité
- Analyse des localisations

Pour plus d'informations, consultez le [guide d'intégration SDK Swift pour iOS](https://github.com/braze-inc/braze-swift-sdk).

{% alert important %}
Certaines fonctionnalités d'iOS sont partiellement prises en charge ou non prises en charge. Pour obtenir la liste complète, consultez le [support de visionOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/visionos).
{% endalert %}

## Ciblage des applications {#app-targeting}

Pour cibler les applications OTT pour la messagerie, nous vous recommandons de créer un segment spécifique à votre application OTT.

![Un segment créé à l'aide de l'application OTT Android.]({% image_buster /assets/img/android_ott.png %})

## Interface utilisateur Headless {#custom-ui}

{% alert important %}
Les plateformes qui prennent en charge les messages in-app ou les cartes de contenu via l'interface utilisateur Headless **n' incluent pas** d'interface utilisateur ou de vues par défaut, veillez donc à mettre en œuvre votre propre interface utilisateur personnalisée.
{% endalert %}

Avec l'interface utilisateur Headless, Braze fournit un modèle de données, tel que JSON, que votre application peut lire et utiliser au sein d'une interface utilisateur contrôlée par votre application. Ces informations contiendront les champs configurés dans le tableau de bord (titre, corps, texte du bouton, couleurs, etc.) que votre application peut lire et afficher en conséquence. Pour plus d'informations sur l'envoi personnalisé de messages, voir ce qui suit :

**SDK Android**
- [Personnalisation des messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners)
- [Personnalisation des cartes de contenu]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)

**SDK Swift**
- [Personnalisation des messages in-app](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [Exemple d'application Headless UI](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)
- [Personnalisation des cartes de contenu](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**Web SDK**
- [Personnalisation des messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web)
- [Personnalisation des cartes de contenu]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)

