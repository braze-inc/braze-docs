---
nav_title: SDK 101
page_order: 0
---

# SDK 101

Avant de commencer à intégrer les SDK Braze, vous vous demandez peut-être exactement ce que vous concevez et intégrez. De plus, vous pourriez être curieux de savoir comment vous pouvez davantage les personnaliser pour répondre à vos besoins. Cet article peut vous aider à répondre à toutes vos questions concernant SDK. Vous pouvez également consulter notre [Listes de contrôle et outils d’intégration technique](https://learning.braze.com/technical-integration-checklists-and-toolkits) sur Braze Learning.

## Performances applicatives

Braze ne devrait pas avoir d’impact négatif sur les performances de votre application.

Les SDK Braze ont une empreinte négligeable. Nous modifions automatiquement le taux auquel nous purgeons les données des utilisateurs en fonction de la qualité du réseau, en plus de permettre un contrôle manuel du réseau. Nous regroupons automatiquement les requêtes d’API depuis le SDK pour nous assurer que les données sont journalisées rapidement tout en maintenant une efficacité maximale du réseau. Enfin, la quantité de données envoyées par le client à Braze dans chaque appel d’API est extrêmement faible.

## Paramètres par défaut des fonctionnalités

Si vous suivez nos guides d’intégration pour implémenter nos SDK, vous pourrez profiter de notre [collecte de données par défaut]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#automatically-collected-data).

{% alert note %}
Toutes nos fonctionnalités sont configurables, mais il ne serait pas avantageux de ne pas les utiliser dans votre intégration. 

<br>Par exemple, si vous choisissez de ne pas intégrer complètement la localisation dans l’un des SDK, vous ne pourrez pas personnaliser votre messagerie en fonction de la langue ou de la localisation. Si nécessaire, il est possible de [bloquer la collecte par défaut de certaines données, ainsi que les processus de liste d’autorisations qui bloquent la collecte](#blocking-data-collection).
{% endalert %}

### Propriétés du périphérique

{% tabs %}
{% tab Web SDK %}

Ces propriétés sont collectées par le SDK Web dans une intégration correcte.

| Nom | Description  |
|---|---|
| BROWSER | Le nom du navigateur.  |
| BROWSER_VERSION | La version du navigateur. |
| OS | Le nom du système d’exploitation.  |
| RESOLUTION | La résolution de l’écran du périphérique. Le format de cette valeur est « `<width>`x`<height>` ».  |
| LANGUAGE | La langue configurée pour être utilisée par le navigateur.  |
| TIME_ZONE | Le fuseau horaire du périphérique.  |
| USER_AGENT | La chaîne de caractères de l’agent utilisateur du navigateur. <br> Consultez les [Documents de développeur Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) pour plus d’informations. |
{: .reset-td-br-1 .reset-td-br-2}

 {% endtab %}
 {% tab Android SDK %}

Ces propriétés sont collectées par le SDK Android dans une intégration correcte.

| Nom | Description |
|---|---|
| VERSION_ANDROID <br> `os_version` | La version du système d’exploitation Android installée sur le périphérique. |
| CARRIER | L’opérateur mobile. |
| MODEL | Le matériel spécifique du périphérique. | 
| RESOLUTION | La résolution de l’écran du périphérique. Le format de cette valeur est « `<width>`x`<height>` ». |
| LOCALE | L’emplacement par défaut du périphérique. Le format de cette valeur est « `<language>`_`<COUNTRY>` » (par exemple, « en_US »). |
| TIMEZONE <br> `time_zone` | Le fuseau horaire du périphérique |
| NOTIFICATIONS_ACTIVÉES <br> `remote_notification_enabled` | Si cette application a des notifications activées.|
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab iOS SDK %}

Ces propriétés sont collectées par le SDK iOS dans une intégration correcte.

| Nom | Description |
|---|---|
| Résolution du périphérique <br> `ABKDeviceOptionResolution`| La résolution de l’écran du périphérique. Le format de cette valeur est « `<width>`x`<height>` ». |  
| Opérateur mobile <br> `ABKDeviceOptionCarrier`| L’opérateur mobile déclaré. |
| Emplacement du périphérique <br> `ABKDeviceOptionLocale`| L’emplacement par défaut du périphérique. |
| Modèle de l’appareil <br> `ABKDeviceOptionModel`| Le matériel spécifique du périphérique.
| Version du système d’exploitation <br> `ABKDeviceOptionOSVersion` | La version du système d’exploitation iOS installée sur le périphérique. |
| IDFV du dispositif <br> `ABKDeviceOptionIDFV`| Identifiant du périphérique pour les fournisseurs. |
| IDFA du dispositif <br> `ABKDeviceOptionIDFA`| (si fourni) Identifiant du périphérique pour les annonceurs. |
| Notifications push d’appareil activées <br> `ABKDeviceOptionPushEnabled`| Si les notifications push sont activées sur cette application.
| Fuseau horaire d’appareil  <br> `ABKDeviceOptionTimezone`| Le fuseau horaire du périphérique.
| Statut d’autorisation des notifications push d’appareil  <br> `ABKDeviceOptionPushAuthStatus`| Si cette application dispose d’une autorisation de notification push pour le périphérique.
| Suivi des campagnes publicitaires activé sur l’appareil  <br> `ABKDeviceAdTrackingEnabled`| Si le suivi des campagnes publicitaires est activé sur cette application. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

## Téléchargement et chargement des données

Le SDK Braze met les données en cache (sessions, événements personnalisés, etc.) et les télécharge périodiquement. Les valeurs seront mises à jour sur le tableau de bord uniquement après que les données auront été téléchargées. L’intervalle de téléchargement tient compte de l’état du périphérique et est régi par la qualité de la connexion réseau :

|Qualité de connexion réseau |    Intervalle de purge des données|
|---|---|
|Excellent    |10 secondes|
|Bon    |30 secondes|
|Mauvais    |60 secondes|
{: .reset-td-br-1 .reset-td-br-2}

S’il n’y a pas de connexion réseau, les données sont mises en cache localement sur le périphérique jusqu’à ce que la connexion réseau soit rétablie. Lorsque la connexion est rétablie, les données seront téléchargées vers Braze.

Braze envoie des données au SDK au début d’une session en fonction des segments dans lesquels l’utilisateur tombe au moment de la session. Le fil d’actualité ou les nouveaux messages in-app ne seront pas mis à jour pendant la session. Cependant, les données de l’utilisateur pendant la session seront traitées en continu au fur et à mesure qu’elles seront envoyées par le client. Par exemple, un utilisateur inactif (qui a utilisé l’application pour la dernière fois il y a plus de 7 jours) recevra toujours du contenu destiné aux utilisateurs inactifs lors de sa première session de retour dans l’application.

## Blocage de la collecte des données

Il est possible, bien que non recommandé, de bloquer la collecte automatique de certaines données de vos intégrations SDK. Comme indiqué dans la section [Paramètres par défaut des de fonctions](#feature-set-defaults), ne pas intégrer complètement nos SDK peut réduire les capacités de personnalisation et de ciblage.

Par exemple, si vous choisissez de ne pas intégrer complètement la localisation dans l’un des SDK, vous ne pourrez pas personnaliser votre messagerie en fonction de la langue ou de la localisation. Si vous choisissez de ne pas intégrer le fuseau horaire, vous ne pourrez peut-être pas envoyer de messages dans le fuseau horaire d’un utilisateur. Si vous choisissez de ne pas intégrer les informations visuelles d’un périphérique spécifique, le contenu du message peut ne pas être optimisé pour ce périphérique.

Nous recommandons fortement d’intégrer pleinement les SDK pour tirer le meilleur parti des capacités de nos produits.

### Web SDK

Vous pouvez soit intégrer certaines parties du SDK, soit utiliser [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) pour un utilisateur. Cette méthode synchronisera les données enregistrées avant que `disableSDK()` soit appelé et tous les appels ultérieurs vers le SDK Braze pour le Web pour cette page et les charges de page ultérieures seront ignorés. Si vous souhaitez reprendre le recueil des données ultérieurement, vous pouvez utiliser la méthode [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) plus tard pour reprendre la collecte des données. Vous pouvez en apprendre plus à ce sujet dans notre article [Désactivation du suivi Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/disabling_tracking/).

### Android SDK

Vous pouvez utiliser [`setDeviceObjectAllowlist`][1] pour configurer uniquement un sous-ensemble de clés d’objet d’appareil ou de valeurs selon une liste de valeurs définie. Cette option doit être activée via [`setDeviceObjectAllowlistEnabled`][2].

{% alert important %}
Une liste vide d’autorisations entraînera le **non** envoi des données du périphérique à Braze.
{% endalert %}

### SDK iOS

Vous pouvez transférer une valeur `appboyOptions` pour `ABKDeviceAllowlistKey` afin de spécifier une liste de champs de périphérique collectés par le SDK. Les champs sont définis dans `ABKDeviceOptions`. Pour désactiver la collecte de tous les champs de périphérique, définissez la valeur de cette clé sur `ABKDeviceOptionNone`.

Pour spécifier les champs de périphérique de la liste d’autorisations, assignez le niveau de bit OU les champs souhaités à `ABKDeviceAllowlistKey` dans l’objet `appboyOptions` transféré à `startWithApiKey`.

{% alert important %}
Par défaut, tous les champs sont collectés par le SDK Braze pour iOS.
{% endalert %}

## Compatibilité SDK

Le SDK de Braze est conçu pour se comporter au mieux et ne pas interférer avec les autres SDK présents dans votre application mobile. Si vous rencontrez des problèmes qui pourraient être dus à une incompatibilité avec un autre SDK mobile, contactez le support Braze.

De plus, le SDK Braze pour iOS prend en charge les applications RubyMotion.

[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder
[2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder
