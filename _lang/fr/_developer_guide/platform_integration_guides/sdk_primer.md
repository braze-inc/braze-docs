---
nav_title: Présentation du SDK
article_title: Présentation du SDK pour les développeurs
description: "Cette article de référence d’onboarding fournit un aperçu technique pour les développeurs de SDK Braze."
page_order: 0
---

# Présentation du SDK pour les développeurs

Avant de commencer à intégrer les SDK Braze, vous vous demandez peut-être exactement ce que vous concevez et intégrez. Vous pourriez être curieux de savoir comment le SDK peut être personnalisé afin de mieux répondre à vos besoins. Cet article peut vous aider à répondre à toutes vos questions concernant SDK. Vous pouvez également consulter notre [Listes de contrôle et outils d’intégration technique](https://learning.braze.com/technical-integration-checklists-and-toolkits) sur Braze Learning.

Êtes-vous un marketeur à la recherche d’un aperçu de base du SDK ? Consultez plutôt notre [présentation pour les marketeurs][3].

Le SDK Braze en bref :
* Recueille et synchronise les données utilisateur dans un profil utilisateur consolidé
* Recueille automatiquement les données de session, les informations sur l’appareil et les jetons push
* Capture les données d’engagement marketing et les données personnalisées spécifiques à votre entreprise
* Alimente les canaux de communication de notifications push, de messages in-app et de carte de contenu

## Performances applicatives

Braze ne devrait pas avoir d’impact négatif sur les performances de votre application.

Les SDK Braze ont une empreinte négligeable. Nous modifions automatiquement le taux auquel nous purgeons les données des utilisateurs en fonction de la qualité du réseau, en plus de permettre un contrôle manuel du réseau. Nous regroupons automatiquement les requêtes d’API depuis le SDK pour nous assurer que les données sont journalisées rapidement tout en maintenant une efficacité maximale du réseau. Enfin, la quantité de données envoyées par le client à Braze dans chaque appel d’API est extrêmement faible.

## Compatibilité SDK

Le SDK de Braze est conçu pour se comporter au mieux et ne pas interférer avec les autres SDK présents dans votre application. Si vous rencontrez des problèmes qui pourraient être dus à une incompatibilité avec un autre SDK, contactez le support Braze.

## Analyses par défaut et gestion de session

Certaines données utilisateur sont collectées automatiquement par notre SDK, par exemple, Première application utilisée, Dernière application utilisée, Nombre total de sessions, Système d’exploitation de l’appareil, etc. Si vous suivez nos guides d’intégration pour implémenter nos SDK, vous pourrez profiter de notre [collecte de données par défaut]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#automatically-collected-data). Vérifier cette liste pour éviter de stocker plusieurs fois les mêmes informations sur les utilisateurs. À l’exception du début et de la fin de session, toutes les autres données automatiquement suivies ne sont pas prises en compte dans votre compte de points de données.

{% alert note %}
Toutes nos fonctionnalités sont configurables, mais il est judicieux de mettre en œuvre le modèle de collecte de données par défaut.

<br>Si cela est nécessaire pour votre cas d’utilisation, vous pouvez [limiter la collecte de certaines données](#blocking-data-collection) une fois l’intégration terminée. 
{% endalert %}

### Propriétés de l’appareil

{% tabs %}
{% tab Web SDK %}

Ces propriétés sont collectées par le SDK Web dans une intégration correcte.

| Nom | Description  |
|---|---|
| NAVIGATEUR | Le nom du navigateur.  |
| BROWSER_VERSION | La version du navigateur. |
| OS | Le nom du système d’exploitation.  |
| RÉSOLUTION | La résolution de l’écran de l’appareil. Le format de cette valeur est « `<width>`x`<height>` ».  |
| LANGUE | La langue configurée pour être utilisée par le navigateur.  |
| TIME_ZONE | Le fuseau horaire de l’appareil.  |
| USER_AGENT | La chaîne de caractères de l’agent utilisateur du navigateur. <br> Consultez les [Documents de développeur Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) pour plus d’informations. |
{: .reset-td-br-1 .reset-td-br-2}

 {% endtab %}
 {% tab Android SDK %}

Ces propriétés sont collectées par le SDK Android dans une intégration correcte.

| Nom | Description |
|---|---|
| ANDROID_VERSION <br> `os_version` | La version du système d’exploitation Android installée sur l’appareil. |
| CARRIER | L’opérateur mobile. |
| MODEL | Le matériel spécifique de l’appareil. | 
| RÉSOLUTION | La résolution de l’écran de l’appareil. Le format de cette valeur est « `<width>`x`<height>` ». |
| LOCALE | Emplacement par défaut de l’appareil. Le format de cette valeur est « `<language>`_`<COUNTRY>` » (par exemple, « en_US »). |
| TIMEZONE <br> `time_zone` | Le fuseau horaire de l’appareil. |
| NOTIFICATIONS_ENABLED <br> `remote_notification_enabled` | Si des notifications sont activées pour cette application..|
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab iOS SDK %}

Ces propriétés sont collectées par le SDK iOS dans une intégration correcte.

| Nom | Description |
|---|---|
| Résolution de l’appareil <br> `ABKDeviceOptionResolution`| La résolution de l’écran de l’appareil. Le format de cette valeur est « `<width>`x`<height>` ». |  
| Opérateur mobile <br> `ABKDeviceOptionCarrier`| L’opérateur mobile déclaré. |
| Emplacement de l’appareil <br> `ABKDeviceOptionLocale`| Emplacement par défaut de l’appareil. |
| Modèle de l’appareil <br> `ABKDeviceOptionModel`| Le matériel spécifique de l’appareil.
| Version du système d’exploitation de l’appareil <br> `ABKDeviceOptionOSVersion` | La version du système d’exploitation iOS installée sur l’appareil. |
| IDFV de l’appareil <br> `ABKDeviceOptionIDFV`| Identifiant de l’appareil pour les fournisseurs. Le recueil des IDFV est désormais facultatif sur notre [SDK iOS v5.7.0 ou ultérieure](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/swift_idfv/)|
| IDFA de l’appareil <br> `ABKDeviceOptionIDFA`| (si fourni) Identifiant de l’appareil pour les annonceurs. |
| Notifications push d’appareil activées <br> `ABKDeviceOptionPushEnabled`| Si les notifications push sont activées sur cette application.
| Fuseau horaire d’appareil <br> `ABKDeviceOptionTimezone`| Le fuseau horaire de l’appareil.
| Statut d’autorisation des notifications push d’appareil  <br> `ABKDeviceOptionPushAuthStatus`| Si cette application dispose d’une autorisation de notification push pour l’appareil.
| Suivi des campagnes publicitaires activé sur l’appareil  <br> `ABKDeviceAdTrackingEnabled`| Si le suivi des campagnes publicitaires est activé sur cette application. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

## Téléchargement et chargement des données

Le SDK de Braze met les données en cache (sessions, événements personnalisés, etc.) et les télécharge périodiquement. Les valeurs seront mises à jour sur le tableau de bord uniquement après que les données auront été téléchargées. L’intervalle de téléchargement tient compte de l’état de l’appareil et est régi par la qualité de la connexion réseau :

|Qualité de connexion réseau |    Intervalle de purge des données|
|---|---|
|Excellent    |10 secondes|
|Bon    |30 secondes|
|Mauvais    |60 secondes|
{: .reset-td-br-1 .reset-td-br-2}

S’il n’y a pas de connexion réseau, les données sont mises en cache localement sur l’appareil jusqu’à ce que la connexion réseau soit rétablie. Lorsque la connexion est rétablie, les données seront téléchargées vers Braze.

Braze envoie des données au SDK au début d’une session en fonction des segments dans lesquels l’utilisateur tombe au moment de la session. Les nouveaux messages in-app ne seront pas mis à jour pendant la session. Cependant, les données de l’utilisateur pendant la session seront traitées en continu au fur et à mesure qu’elles seront envoyées par le client. Par exemple, un utilisateur inactif (qui a utilisé l’application pour la dernière fois il y a plus de 7 jours) recevra toujours du contenu destiné aux utilisateurs inactifs lors de sa première session de retour dans l’application.

## Blocage de la collecte des données

Il est possible, bien que non recommandé, de bloquer la collecte automatique de certaines données de votre intégration SDK ainsi que des processus de liste d’autorisations qui le font. 

Il n’est pas recommandé de bloquer la collecte de données, car la suppression des données analytiques réduit la capacité de personnalisation et de ciblage de votre plateforme. Par exemple :

- Si vous choisissez de ne pas intégrer complètement la localisation dans l’un des SDK, vous ne pourrez pas personnaliser vos messages en fonction de la langue ou de la localisation. 
- Si vous choisissez de ne pas intégrer le fuseau horaire, vous ne pourrez peut-être pas envoyer de messages dans le fuseau horaire d’un utilisateur. 
- Si vous choisissez de ne pas intégrer les informations visuelles d’un appareil spécifique, le contenu du message peut ne pas être optimisé pour cet appareil.

Nous recommandons fortement d’intégrer pleinement les SDK pour tirer le meilleur parti des capacités de nos produits.

{% tabs %}
{% tab Web SDK %}

Vous pouvez soit intégrer certaines parties du SDK, soit utiliser [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) pour un utilisateur. Cette méthode synchronisera les données enregistrées avant que `disableSDK()` soit appelé et tous les appels ultérieurs vers le SDK Braze pour le Web pour cette page et les charges de page ultérieures seront ignorés. Si vous souhaitez reprendre le recueil des données ultérieurement, vous pouvez utiliser la méthode [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) plus tard pour reprendre la collecte des données. Vous pouvez en apprendre plus à ce sujet dans notre article [Désactivation du suivi Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/disabling_tracking/).

{% endtab %}
{% tab Android SDK %}

Vous pouvez utiliser [`setDeviceObjectAllowlist`](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):% 20BrazeConfig.Builder) pour configurer le SDK afin qu’il envoie uniquement un sous-ensemble de clés d’objet d’appareil ou de valeurs selon une liste de valeurs définie. Cette option doit être activée via [`setDeviceObjectAllowlistEnabled`](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):% 20BrazeConfig.Builder).

{% alert important %}
Une liste vide d’autorisations entraînera le **non** envoi des données de l’appareil à Braze.
{% endalert %}

{% endtab %}
{% tab iOS SDK %}

Vous pouvez transférer une valeur `appboyOptions` pour `ABKDeviceAllowlistKey` afin de spécifier une liste de champs d’appareil collectés par le SDK. Les champs sont définis dans `ABKDeviceOptions`. Pour désactiver la collecte de tous les champs d’appareil, définissez la valeur de cette clé sur `ABKDeviceOptionNone`. Reportez-vous à la section [`Appboy.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) pour la documentation des clés `appboyOptions`.

Pour spécifier les champs d’appareil de la liste d’autorisations, assignez le niveau de bit OU les champs souhaités à `ABKDeviceAllowlistKey` dans l’objet `appboyOptions` transféré à `startWithApiKey`.

{% alert important %}
Par défaut, tous les champs sont collectés par le SDK Braze pour iOS.
{% endalert %}

{% endtab %}
{% endtabs %}


[3]: {{site.baseurl}}/user_guide/onboarding_with_braze/web_sdk/