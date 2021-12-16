---
nav_title: SDK 101
page_order: 0
---

# SDK 101

Avant de commencer à intégrer les SDK de Braze, vous pourriez vous demander ce que vous construisez et intégrez exactement. De plus, vous pourriez être curieux de savoir comment vous pouvez le personnaliser davantage en fonction de vos besoins. Cet article peut vous aider à répondre à toutes vos questions sur le SDK. Vous pouvez également consulter nos [listes de contrôle et kits d’intégration technique](https://lab.braze.com/technical-integration-checklists-and-toolkits/) cours LAB.

## Performances de l'application

Braze ne devrait avoir aucun impact négatif sur les performances de votre application.

Les SDK de Braze ont une très petite empreinte. Nous modifions automatiquement le taux de vidange des données utilisateur en fonction de la qualité du réseau, en plus de permettre le contrôle manuel du réseau. Nous effectuons automatiquement des requêtes API depuis le SDK pour nous assurer que les données sont enregistrées rapidement tout en maintenant une efficacité réseau maximale. Enfin, la quantité de données envoyées par le client à Braze dans chaque appel API est extrêmement faible.

## Paramétrage par défaut des fonctionnalités

Si vous suivez nos guides d'intégration pour implémenter nos SDK, vous pourrez profiter de notre [collecte de données par défaut]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#automatically-collected-data).

{% alert note %}
Toutes nos fonctionnalités sont configurables, mais il ne serait pas avantageux de les éviter dans votre intégration.

<br>Par exemple, si vous choisissez de ne pas s'intégrer complètement pour l'emplacement sur l'un des SDK, vous ne serez pas en mesure de personnaliser votre messagerie en fonction de la langue ou de l'emplacement. Si nécessaire, il est possible de [bloquer la collecte par défaut de certaines données, ainsi que les processus de liste qui le font](#blocking-data-collection).
{% endalert %}

### Propriétés de l'appareil

{% tabs %}
{% tab Web SDK %}

Ces propriétés sont collectées par le SDK Web après une bonne intégration.

| Nom                       | Libellé                                                                                                                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BROWSER                   | Le nom du navigateur.                                                                                                                                                                         |
| VERSION DE FONCTIONNALITÉ | La version du navigateur.                                                                                                                                                                     |
| Système d'exploitation    | Le nom du système d'exploitation.                                                                                                                                                             |
| RÉSOLUTION                | La résolution de l'écran de l'appareil. The format of this value is "`<width>`x`<height>`".                                                                                       |
| LANGUE                    | La langue que le navigateur est configuré pour utiliser.                                                                                                                                      |
| Fuseau horaire            | Le fuseau horaire de l'appareil.                                                                                                                                                              |
| USER_AGENT                | La chaîne user agent du navigateur. <br> Voir la documentation [du développeur Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) pour plus d'informations. |
{: .reset-td-br-1 .reset-td-br-2}

 {% endtab %}
 {% tab Android SDK %}

Ces propriétés sont collectées par le SDK Android lors d'une bonne intégration.

| Nom                                                            | Libellé                                                                                                                         |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| ANDROID_VERSION <br> `os_version`                        | La version de l'OS Android installée sur l'appareil.                                                                            |
| CARRIÈRE                                                       | L'opérateur de téléphonie mobile.                                                                                               |
| MODEL                                                          | Le matériel spécifique de l'appareil.                                                                                           |
| RÉSOLUTION                                                     | La résolution de l'écran de l'appareil. The format of this value is "`<width>`x`<height>`".                         |
| LOCALE                                                         | La locale par défaut de l'appareil. Le format de cette valeur est "`<language>`_`<COUNTRY>`" (par exemple "en_US"). |
| TIMEZONE <br> `fuseau horaire`                           | Le fuseau horaire de l'appareil                                                                                                 |
| NOTIFICATIONS_ENABLED <br> `remote_notification_enabled` | Si cette application a des notifications activées.                                                                              |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab iOS SDK %}

Ces propriétés sont collectées par le SDK iOS lors d'une bonne intégration.

| Nom                                                                            | Libellé                                                                                                 |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| Résolution de l'appareil <br> `ABKDeviceOptionRésolution`                | La résolution de l'écran de l'appareil. The format of this value is "`<width>`x`<height>`". |
| Opérateur de l'appareil <br> `ABKDeviceOptionCarrier`                    | L'opérateur de téléphonie mobile signalé                                                                |
| Localisation de l'appareil <br> `ABKDeviceOptionLocale`                  | La locale par défaut de l'appareil.                                                                     |
| Modèle de l'appareil <br> `ABKDeviceOptionModel`                         | Le matériel spécifique de l'appareil.                                                                   |
| Version de l'appareil OS <br> `ABKDeviceOptionOSVersion`                 | La version de l'OS iOS installée sur l'appareil.                                                        |
| Périphérique IDFV <br> `ABKDeviceOptionIDFV`                             | Identificateur de l'appareil pour les vendeurs.                                                         |
| Appareil IDFA <br> `ABKDeviceOptionIDFA`                                 | (s'il est fourni) Identificateur d'appareil pour les annonceurs.                                        |
| Device Push Enabled <br> `ABKDeviceOptionPushEnabled`                    | Si cette application a des notifications push activées.                                                 |
| Fuseau horaire de l'appareil <br> `ABKDeviceOptionFuseau horaire`        | Le fuseau horaire signalé de l'appareil.                                                                |
| Statut d'autorisation de l'appareil <br> `ABKDeviceOptionPushAuthStatus` | Si cette application a l'autorisation push pour l'appareil.                                             |
| Device Ad Tracking Enabled <br> `ABKDeviceAdTrackingEnabled`             | Si cette application a activé le suivi des annonces.                                                    |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

## Téléversement et téléchargement de données

Braze SDK met en cache des données (sessions, événements personnalisés, etc.) et les télécharge périodiquement. Ce n'est qu'après avoir téléchargé les données que les valeurs seront mises à jour sur le tableau de bord. L'intervalle de téléchargement prend en compte l'état de l'appareil et est régi par la qualité de la connexion réseau :

| Qualité de la connexion réseau | Intervalle de purge des données |
| ------------------------------ | ------------------------------- |
| Superbe                        | 10 secondes                     |
| Bon                            | 30 secondes                     |
| Mauvais                        | 60 secondes                     |
{: .reset-td-br-1 .reset-td-br-2}

S'il n'y a pas de connexion réseau, les données sont mises en cache localement sur le périphérique jusqu'à ce que la connexion réseau soit rétablie. Une fois la connexion rétablie, les données seront envoyées sur Braze.

Braze envoie des données au SDK au début d'une session en fonction des segments dans lesquels l'utilisateur tombe au moment de la session. Le fil d'actualité ou les nouveaux messages dans l'application ne seront pas mis à jour pendant la session. Cependant, les données des utilisateurs pendant la session seront traitées en permanence au fur et à mesure qu'elles sont envoyées par le client. Par exemple, un utilisateur expiré (dernière utilisation de l'application il y a plus de 7 jours) recevra toujours du contenu ciblé sur les utilisateurs périmés lors de leur première session dans l'application.

## Blocage de la collecte de données

Il est possible, mais non suggéré, de bloquer la collecte automatique de certaines données à partir de vos intégrations SDK. Comme nous l'avons dit ci-dessus, ne pas intégrer complètement nos SDK peut réduire les capacités de personnalisation et de ciblage.

Par exemple, si vous choisissez de ne pas s'intégrer complètement pour l'emplacement sur l'un des SDK, vous ne serez pas en mesure de personnaliser votre messagerie en fonction de la langue ou de l'emplacement. Si vous choisissez de ne pas intégrer le fuseau horaire, il se peut que vous ne puissiez pas envoyer de messages dans le fuseau horaire d'un utilisateur. Si vous choisissez de ne pas vous intégrer pour des informations visuelles spécifiques à votre appareil, il se peut que le contenu du message ne soit pas optimisé pour cet appareil.

Nous recommandons fortement l'intégration complète des SDK pour tirer pleinement parti des capacités de nos produits.

### SDK Web

Vous pouvez soit simplement ne pas intégrer certaines parties du SDK, soit utiliser [`stopWebTracking`](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.stopWebTracking) pour un utilisateur. Cette méthode va synchroniser les données enregistrées avant le moment où `stopWebTracking()` a été appelé, et fera que tous les appels ultérieurs au SDK Braze Web pour cette page et les prochaines pages seront ignorés. Si vous souhaitez reprendre la collecte de données à un moment ultérieur, vous pouvez utiliser la méthode [`resumeWebTracking()`](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.resumeWebTracking) pour reprendre la collecte de données. Vous pouvez en savoir plus à ce sujet dans notre article [Désactiver le suivi Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/disabling_tracking/).

### SDK Android

Vous pouvez utiliser [`setDeviceObjectAllowlist`](https://appboy.github.io/appboy-android-sdk/javadocs/) pour configurer pour n'envoyer qu'un sous-ensemble de clés ou de valeurs de l'objet périphérique selon une liste d'autorisations. Ceci doit être activé via `setDeviceObjectAllowlistEnabled`.

{% alert important %}
Une liste d'autorisations vide entraînera __aucune donnée de périphérique__ envoyée au Brésil.
{% endalert %}

### SDK iOS

Vous pouvez passer une valeur `appboyOptions` pour `ABKDeviceAllowlistKey` pour spécifier une liste d'autorisations pour les champs de périphérique qui sont collectés par le SDK. Les champs sont définis dans `ABKDeviceOptions`. Pour désactiver la collection de tous les champs de périphériques, définissez la valeur de cette clé à `ABKDeviceOptionNone`.

Pour spécifier les champs autorisés du périphérique, affecter le OU bitwise des champs désirés à `ABKDeviceAllowlistKey` dans l'objet `appboyOptions` passé à `startWithApiKey`.

{% alert important %}
Par défaut, tous les champs sont collectés par Braze iOS SDK.
{% endalert %}

## Compatibilité SDK

Le SDK de Braze est conçu pour être très bien comporté, et ne pas interférer avec les autres SDK présents dans votre application mobile. Si vous rencontrez des problèmes que vous pensez être dus à une incompatibilité avec un autre SDK mobile, veuillez contacter le support de Braze.

De plus, Braze iOS SDK prend entièrement en charge les applications RubyMotion.
