---
nav_title: "Branch pour l'attribution"
article_title: "Branch pour l'attribution"
alias: /partners/branch_for_attribution/
description: "Cet article de référence présente le partenariat entre Braze et Branch, une plateforme de liaison mobile qui vous aide à acquérir, engager et mesurer sur tous les appareils, canaux et plateformes."
page_type: partner
search_tag: Partner

---

# Branch pour l'attribution {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://docs.branch.io/pages/integrations/braze/), une plateforme de liaison mobile, vous aide à acquérir, engager et mesurer à travers tous les appareils, canaux et plateformes en fournissant une vue complète de tous les points de contact de l'utilisateur.

_Cette intégration est maintenue par la branche._

## À propos de l'intégration

L'intégration de Braze et Branch vous aidera à comprendre exactement quand et où les utilisateurs ont été acquis, ainsi que la façon de personnaliser leurs parcours grâce à l'attribution robuste et aux [liens profonds]({{site.baseurl}}/partners/message_orchestration/attribution/branch/branch_for_deeplinking/).

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Branch | Pour bénéficier de ce partenariat, vous devez disposer d'un compte Branch. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. En fonction de votre plateforme, des extraits de code peuvent être requis dans votre application. Vous trouverez des détails sur ces exigences à l'étape 1 du processus d'intégration. |
| SDK Branch | En plus du SDK Braze requis, vous devez installer le [SDK Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Mapper les ID des appareils

#### Android 

Si vous disposez d'une application Android, vous devez transmettre l’ID unique de l'appareil Braze à Branch. Cet ID peut être défini dans la méthode `setRequestMetadataKey()` du SDK de Branch. L'extrait de code suivant doit être inclus avant d'appeler `initSession`. Vous devez également initialiser le SDK Braze avant de définir les métadonnées de la requête dans le SDK de Branch.

{% tabs local %}
{% tab Java %}
```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId); 
```
{% endtab %}
{% tab Kotlin %}
```kotlin
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId)
```
{% endtab %}
{% endtabs %}

#### iOS

{% alert important %}
Avant février 2023, notre intégration d'attribution Branch utilisait l'IDFV comme identifiant principal pour mapper les données d'attribution iOS. Il n'est pas nécessaire pour les clients de Braze utilisant Objective-C de récupérer le site `device_id` de Braze et de l'envoyer à Branch lors de l'installation, car il n'y aura pas d'interruption de service.
{% endalert%}

Pour ceux qui utilisent le SDK Swift v5.7.0+, si vous souhaitez continuer à utiliser l'IDFV comme identifiant mutuel, vous devez vous assurer que le champ `useUUIDAsDeviceId` est défini sur `false` afin que rien ne vienne perturber l'intégration. 

Si la valeur est `true`, vous devez mapper les ID d'appareil iOS pour Swift afin de transmettre le paramètre `device_id` de Braze à Branch lors de l'installation de l'application pour que les attributions Braze correspondent aux attributions iOS.

{% tabs local %}
{% tab Objective-C %}
```objc
[braze deviceIdOnQueue:dispatch_get_main_queue() completion:^(NSString * _Nonnull deviceId) {
  [[Branch getInstance] setRequestMetadataKey:@"$braze_install_id" value:deviceId];
  // Branch init
}];
```
{% endtab %}
{% tab Swift %}

```swift
braze.deviceId { deviceId in
  Branch.getInstance.setRequestMetadata("$braze_install_id", deviceId)
  // Branch init 
}
```

{% endtab %}
{% endtabs %}

### Étape 2 : Obtenir la clé d'importation des données de Braze

Dans Braze, naviguez vers **Intégrations de partenaires** > **Partenaires technologiques** et sélectionnez **Branch**. 

Ici, vous trouverez l’endpoint REST et générerez votre clé d'importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation des données et l'endpoint REST sont utilisés à l'étape suivante lors de la configuration d'un système de communication automatisé dans le tableau de bord Branch.<br><br>![Cette image montre la section "Importation de données pour l'attribution d'installation" qui se trouve sur la page de la technologie Branch. Cette section affiche la clé d'importation des données et l'endpoint REST.][4]{: style="max-width:90%;"}

### Étape 3 : Mettre en place des flux de données

1. Dans Branch, sous la section **Exports**, sélectionnez **Data Feeds**.
2. Sur la page du **gestionnaire des flux de données**, sélectionnez l'onglet **Intégrations de données** en haut de la page. 
3. Sélectionnez Braze dans la liste des partenaires de données disponibles. 
4. Sur la page d'exportation de Braze, indiquez la clé d'importation des données et le point de terminaison REST que vous avez trouvés dans le tableau de bord de Braze, puis sélectionnez **Activer**.

### Étape 4 : Confirmer l'intégration

Une fois que Braze aura reçu les données d'attribution de Branch, l'indicateur de connexion d'état sur la page des partenaires technologiques de Branch dans Braze passera de "Non connecté" à "Connecté". Un horodatage de la dernière requête réussie sera également inclus. 

Notez que cela ne se produira pas tant que nous n'aurons pas reçu de données d’une attribution d'installation. Les installations organiques, qui doivent être exclues du système de communication automatisé de Branch, sont ignorées par notre API et ne sont pas prises en compte pour déterminer si une connexion a été établie avec succès.

## Données d'attribution de Facebook et de X (anciennement Twitter)

Les données d'attribution pour les campagnes Facebook et X (anciennement Twitter) ne sont pas disponibles auprès de nos partenaires. Ces sources médiatiques n'autorisent pas leurs partenaires à partager les données d'attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.

## URL de suivi des clics Branch dans Braze (facultatif)

L'utilisation de liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes favorisent les installations d'applications et le réengagement. Vous serez ainsi en mesure de mesurer plus efficacement vos efforts de marketing et de prendre des décisions fondées sur des données pour savoir où investir davantage de ressources afin d'obtenir un ROI maximal.

Pour commencer à utiliser les liens de suivi des clics de Branch, consultez leur [documentation](https://help.branch.io/using-branch/docs/ad-links). Vous pouvez insérer les liens de suivi des clics de Branch directement dans vos campagnes Braze. Branch utilisera alors ses [méthodes d'attribution probabiliste](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings) pour attribuer l'utilisateur qui a cliqué sur le lien. Nous vous recommandons d'ajouter à vos liens de suivi Branch un identifiant d'appareil afin d'améliorer la précision des attributions de vos campagnes Braze. Cela permettra d'attribuer de manière déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs local %}
{% tab Android %}
Pour Android, Braze permet à ses clients de s'abonner à la [collecte d'ID publicitaires de Google (GAID).]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id) Le GAID est également collecté de manière native grâce à l'intégration SDK de Branch. Vous pouvez inclure le GAID dans les liens de suivi des clics Branch en utilisant la logique Liquid suivante :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Branch collectent automatiquement l'IDFV de manière native grâce à nos intégrations SDK. Il peut être utilisé comme identifiant de l'appareil. Vous pouvez inclure l'IDFV dans les liens de suivi des clics Branch en utilisant la logique liquide suivante :

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
user_data_idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Cette recommandation est purement facultative**<br>
Si vous n'utilisez actuellement aucun identifiant d'appareil, tel que l'IDFV ou le GAID, dans vos liens de suivi des clics, ou si vous n'envisagez pas de le faire à l'avenir, Branch pourra tout de même attribuer ces clics grâce à sa modélisation probabiliste.
{% endalert %}


[22]: https://docs.branch.io/pages/exports/ua-webhooks/ "Webhooks de Branch"
[4]: {% image_buster /assets/img/attribution/branch.png %}
