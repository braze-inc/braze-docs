---
nav_title: Présentation du SDK
article_title: Présentation du SDK pour les développeurs
description: "Cette article de référence d’onboarding fournit un aperçu technique pour les développeurs de SDK Braze. Il aborde les analyses par défaut qui font l’objet d’un suivi par le SDK, le blocage de la collecte automatique de données et la version du SDK publiée de votre application."
page_order: 0
---

# [![Cours d’apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}Aperçu du SDK pour les développeurs

> Avant de commencer à intégrer les SDK Braze, vous vous demandez peut-être exactement ce que vous concevez et intégrez. Vous pourriez être curieux de savoir comment le SDK peut être personnalisé afin de mieux répondre à vos besoins. Cet article peut vous aider à répondre à toutes vos questions concernant SDK. 

Êtes-vous un spécialiste du marketing à la recherche d’un aperçu de base du SDK ? Consultez plutôt notre [présentation pour les marketeurs]({{site.baseurl}}/user_guide/getting_started/web_sdk/).

Le SDK Braze en bref :
* Collecte et synchronise les données de l'utilisateur dans un profil utilisateur consolidé.
* Recueille automatiquement les données de session, les informations sur l’appareil et les jetons push
* Capture les données d’engagement marketing et les données personnalisées spécifiques à votre entreprise
* Alimente les canaux de communication de notifications push, de messages in-app et de carte de contenu

## Performances applicatives

Braze ne devrait pas avoir d’impact négatif sur les performances de votre application.

Les SDK Braze ont une empreinte négligeable. Nous modifions automatiquement le taux auquel nous purgeons les données des utilisateurs en fonction de la qualité du réseau, en plus de permettre un contrôle manuel du réseau. Nous regroupons automatiquement les requêtes d’API depuis le SDK pour nous assurer que les données sont journalisées rapidement tout en maintenant une efficacité maximale du réseau. Enfin, la quantité de données envoyées par le client à Braze dans chaque appel d’API est extrêmement faible.

## Compatibilité SDK

Le SDK de Braze est conçu pour se comporter au mieux et ne pas interférer avec les autres SDK présents dans votre application. Si vous rencontrez des problèmes qui pourraient être dus à une incompatibilité avec un autre SDK, contactez le support Braze.

## Analyses par défaut et gestion de session

Certaines données utilisateur sont collectées automatiquement par notre SDK, par exemple, Première application utilisée, Dernière application utilisée, Nombre total de sessions, Système d’exploitation de l’appareil, etc. Si vous suivez nos guides d'intégration pour mettre en œuvre nos SDK, vous pourrez profiter de cette [collecte de données par défaut]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/). Vérifier cette liste pour éviter de stocker plusieurs fois les mêmes informations sur les utilisateurs. À l'exception du début et de la fin de la session, toutes les autres données suivies automatiquement ne sont pas prises en compte dans le calcul de votre nombre de points de données.

{% alert note %}
Toutes nos fonctionnalités sont configurables, mais il est judicieux de mettre en œuvre le modèle de collecte de données par défaut.

<br>Si cela est nécessaire pour votre cas d'utilisation, vous pouvez [limiter la collecte de certaines données](#blocking-data-collection) une fois l'intégration terminée.
{% endalert %}

## Téléchargement et chargement des données

Le SDK de Braze met les données en cache (sessions, événements personnalisés, etc.) et les télécharge périodiquement. Les valeurs seront mises à jour sur le tableau de bord uniquement après que les données auront été téléchargées. L’intervalle de téléchargement tient compte de l’état de l’appareil et est régi par la qualité de la connexion réseau :

|Qualité de connexion réseau |    Intervalle de purge des données|
|---|---|
|Excellent    |10 secondes|
|Bon    |30 secondes|
|Mauvais    |60 secondes|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

S’il n’y a pas de connexion réseau, les données sont mises en cache localement sur l’appareil jusqu’à ce que la connexion réseau soit rétablie. Lorsque la connexion est rétablie, les données seront téléchargées vers Braze.

Braze envoie des données au SDK au début d’une session en fonction des segments dans lesquels l’utilisateur tombe au moment de la session. Les nouveaux messages in-app ne seront pas mis à jour pendant la session. Cependant, les données de l’utilisateur pendant la session seront traitées en continu au fur et à mesure qu’elles seront envoyées par le client. Par exemple, un utilisateur inactif (qui a utilisé l’application pour la dernière fois il y a plus de 7 jours) recevra toujours du contenu destiné aux utilisateurs inactifs lors de sa première session de retour dans l’application.

## Blocage de la collecte des données

Il est possible, bien que non recommandé, de bloquer la collecte automatique de certaines données de votre intégration SDK ainsi que des processus de liste d’autorisations qui le font. 

Il n’est pas recommandé de bloquer la collecte de données, car la suppression des données d'analyse réduit la capacité de personnalisation et de ciblage de votre plateforme. Par exemple :

- Si vous choisissez de ne pas intégrer complètement la localisation dans l’un des SDK, vous ne pourrez pas personnaliser vos messages en fonction de la langue ou de la localisation. 
- Si vous choisissez de ne pas intégrer le fuseau horaire, vous ne pourrez peut-être pas envoyer de messages dans le fuseau horaire d’un utilisateur. 
- Si vous choisissez de ne pas intégrer les informations visuelles d’un appareil spécifique, le contenu du message peut ne pas être optimisé pour cet appareil.

Nous recommandons fortement d’intégrer pleinement les SDK pour tirer le meilleur parti des capacités de nos produits.

{% tabs %}
{% tab Web SDK %}

Vous pouvez soit simplement ne pas intégrer certaines parties du SDK, soit utiliser [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) pour un utilisateur. Cette méthode synchronisera les données enregistrées avant que `disableSDK()` soit appelé et tous les appels ultérieurs vers le SDK Braze pour le Web pour cette page et les charges de page ultérieures seront ignorés. Si vous souhaitez reprendre le recueil de données ultérieurement, vous pouvez utiliser la méthode [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) plus tard pour reprendre la collecte des données. Pour en savoir plus à ce sujet, consultez notre article [Désactivation du suivi Web]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=web).

{% endtab %}
{% tab Android SDK %}

Vous pouvez utiliser [`setDeviceObjectAllowlist`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder) pour configurer le SDK de manière à ce qu'il n'envoie qu'un sous-ensemble de clés ou de valeurs d'objets d'appareils conformément à une liste d'autorisations définie. Cette fonction doit être activée par l'intermédiaire de [`setDeviceObjectAllowlistEnabled`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder).

{% alert important %}
Si la liste d'autorisations est vide, **aucune** donnée relative à l'appareil n'est envoyée à Braze.
{% endalert %}

{% endtab %}
{% tab Swift SDK %}

Vous pouvez attribuer un ensemble de champs éligibles à [`configuration.devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) sur votre site `Braze.Configuration` pour spécifier une liste d'autorisations pour les champs de l'appareil qui sont collectés par le SDK. La liste complète des champs est définie dans [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty). Pour désactiver la collecte de tous les champs de l'appareil, définissez la valeur de cette propriété à un ensemble vide (`[]`).

{% alert important %}
Par défaut, tous les champs sont collectés par le SDK Braze Swift. La suppression de certaines propriétés de l'appareil peut entraîner la désactivation de certaines des fonctionnalités du SDK.
{% endalert %}

Pour plus de détails sur l'utilisation, reportez-vous à la rubrique [Stockage]({{site.baseurl}}/developer_guide/storage/?tab=swift) dans la documentation du SDK Swift.

{% endtab %}
{% endtabs %}

## Quelle est la version du SDK que j'utilise ?

Vous pouvez utiliser le tableau de bord pour voir la version du SDK d'une application particulière en sélectionnant **Paramètres > Paramètres des applications**. La **version du SDK en ligne** indique la version la plus élevée du SDK de Braze utilisée par votre application en ligne/en production/instantanée la plus récente pour au moins 5 % de vos utilisateurs.

![Une application nommée Swifty dans un espace de travail. La version du SDK Live est la 6.6.0.]({% image_buster /assets/img/live-sdk-version.png %}){: style="max-width:80%"} 

{% alert tip %}
Si vous avez une application iOS, vous pouvez confirmer que vous utilisez le [SDK Swift]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) au lieu de l'ancien [SDK iOS Objective-C]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/) si la **version de votre Live SDK** est égale ou supérieure à 5.0.0, qui était la première version publiée du SDK Swift.
{% endalert %}

