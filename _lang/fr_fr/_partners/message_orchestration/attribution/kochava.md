---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "Cet article de référence décrit le partenariat entre Braze et Kochava, une plateforme d'attribution mobile qui propose des informations d'attribution et d'analyse pour vous aider à exploiter vos données pour renforcer votre croissance."
page_type: partner
search_tag: Partner

---

# Kochava

> Kochava propose des fonctionnalités d'attribution et d'analyse mobiles pour vous aider à exploiter vos données pour stimuler votre croissance. La plateforme d'audience de Kochava vous permet de planifier, de cibler, d'activer, de mesurer et d'optimiser vos campagnes d'applications.

_Cette intégration est maintenue par Kochava._

## À propos de l'intégration

L'intégration de Braze et Kochava contribue à une compréhension plus globale de vos campagnes en envoyant des données d'attribution à Braze afin de mieux comprendre quelles campagnes génèrent des installations, des activités intégrées à l'application, etc.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Kochava | Un compte à Kochava est nécessaire pour bénéficier de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. En fonction de votre plateforme, des extraits de code peuvent être requis dans votre application. Vous trouverez des informations détaillées sur ces exigences à l'étape 1 du processus d'intégration. |
| SDK de Kochava | [Outre le SDK Braze requis, vous devez installer le SDK Kochava](https://support.kochava.com/sdk-integration/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Mapper les ID utilisateur

#### Android

Le SDK [Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) génère un GUID en tant que Braze ID au démarrage de la session. Il s'agit de l'identifiant que nous recommandons de transmettre à la méthode `IdentityLink` Kochava car il permet à Braze de réconcilier les données avec le bon profil utilisateur. L’ID Braze peut être récupéré à l'aide de la méthode suivante :

```java
Apppboy.getInstance(context).getDeviceId();
```

#### iOS

{% alert important %}
Avant février 2023, notre intégration d'attribution à Kochava utilisait l'IDFV comme identifiant principal pour correspondre aux données d'attribution iOS. Les clients de Braze utilisant Objective-C n'ont pas besoin de récupérer le paramètre `device_id` Braze et de l’envoyer à Kochava lors de l'installation, car il n'y aura aucune interruption de service.
{% endalert%}

Pour ceux qui utilisent le SDK Swift v5.7.0 et versions ultérieures, si vous souhaitez continuer à utiliser IDFV comme identifiant mutuel, vous devez vous assurer que le champ `useUUIDAsDeviceId` est défini sur `false` afin de ne pas perturber l'intégration. Si ce paramètre est défini sur`true`, vous devez déployer le mappage des ID d'appareils iOS pour Swift afin de transmettre le paramètre `device_id` Braze à Kochava lors de l'installation de l'application afin que Braze corresponde correctement aux attributions iOS.

Braze possède deux API qui produiront la même valeur, l'une avec un gestionnaire de finalisation et l'autre avec le nouveau support de simultanéité Swift. [Notez que vous devrez modifier les extraits de code suivants pour vous conformer aux instructions du SDK iOS de Kochava.](https://support.kochava.com/sdk-integration/ios-sdk-integration/) Pour obtenir de l'aide supplémentaire, contactez le service d'assistance de Kochava.

##### Gestionnaire de complétion
```
AppDelegate.braze?.deviceId(completion: { deviceId in
  // Use `deviceId`
})
```
##### Simultanéité Swift
```
let deviceId = await AppDelegate.braze?.deviceId()
```

### Étape 2 : Obtenez la clé d'importation des données Braze

Dans Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Kochava**. 

Ici, vous trouverez l’endpoint REST et générerez votre clé d'importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation des données et l’endpoint REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord de Kochava.<br><br>![Cette image montre la case « Importation de données pour l'attribution de l'installation » qui se trouve sur la page technologique de Kochava. Dans cette boîte, la clé d'importation des données et l'endpoint REST sont affichés.]({% image_buster /assets/img/attribution/kochava.png %}){: style="max-width:90%;"}

### Étape 3 : Configurer un système de communication automatisé depuis Kochava

[Ajoutez un postback](https://support.kochava.com/campaign-management/create-a-kochava-certified-postback) dans votre tableau de bord de Kochava. Vous serez invité à indiquer la clé d'importation des données et l'endpoint REST que vous avez trouvés dans le tableau de bord de Braze.

### Étape 4 : Confirmez l'intégration

Une fois que Braze aura reçu les données d'attribution de Kochava, l'indicateur de statut de connexion sur la page des partenaires technologiques de Kochava dans Braze passera de « Non connecté » à « Connecté ». Un horodatage de la dernière requête réussie sera également inclus. 

Notez que cela ne se produira pas tant que nous n'aurons pas reçu les données relatives à une installation attribuée. Les installations organiques, qui devraient être exclues du postback de Kochava, sont ignorées par notre API et ne sont pas prises en compte pour déterminer si une connexion a été établie avec succès.

## Données d'attribution sur Facebook et X (anciennement Twitter)

Les données d'attribution pour les campagnes Facebook et X (anciennement Twitter) ne sont pas disponibles auprès de nos partenaires. Ces sources médiatiques n'autorisent pas leurs partenaires à partager les données d'attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.

## URL de suivi des clics Kochava dans Braze (facultatif)

L'utilisation de liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes génèrent des installations d'applications et un réengagement. Ainsi, vous serez en mesure de mesurer vos efforts marketing de manière plus efficace et de prendre des décisions fondées sur des données pour investir davantage de ressources pour un retour sur investissement maximal.

[Pour démarrer avec Kochava, cliquez sur les liens de suivi et consultez leur documentation.](https://support.kochava.com/reference-information/attribution-overview/) Vous pouvez insérer les liens de suivi des clics de Kochava directement dans vos campagnes Braze. Kochava utilisera ensuite [ses méthodologies d'attribution probabilistes](https://www.kochava.com/getting-prepared-for-ios-14/) pour attribuer l'utilisateur qui a cliqué sur le lien. Nous vous recommandons d'ajouter à vos liens de suivi de Kochava un identifiant d'appareil afin d'améliorer la précision des attributions issues de vos campagnes Braze. Cela attribuera de manière déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs local %}
{% tab Android %}
Pour Android, Braze permet aux clients de s'abonner à la [collecte d'identifiants publicitaires de Google (GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)). Le GAID est également collecté de manière native via l'intégration du SDK Kochava. Vous pouvez inclure le GAID dans vos liens de suivi des clics sur Kochava en utilisant la logique Liquid suivante :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Kochava collectent automatiquement l'IDFV de manière native via nos intégrations de SDK. Cela peut être utilisé comme identifiant de l'appareil. Vous pouvez inclure l'IDFV dans vos liens de suivi des clics sur Kochava en utilisant la logique Liquid suivante :

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Cette recommandation est purement facultative**<br>
Si vous n'utilisez actuellement aucun identifiant d'appareil, tel que l'IDFV ou le GAID, dans vos liens de suivi des clics, ou si vous ne prévoyez pas de le faire à l'avenir, Kochava pourra toujours attribuer ces clics grâce à sa modélisation probabiliste.
{% endalert %}


