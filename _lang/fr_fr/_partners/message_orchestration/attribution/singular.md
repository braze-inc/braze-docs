---
nav_title: Singular
article_title: Singular
alias: /partners/singular/
description: "Cet article de référence présente le partenariat entre Braze et Singular, une plateforme d'analyse marketing unifiée qui vous permet d'importer des données d'attribution d'installation payante."
page_type: partner
search_tag: Partner

---

# Singular

> Singular est une plateforme d'analyse marketing unifiée qui permet l'attribution, l'agrégation des coûts, l'analyse marketing, les rapports créatifs et l'automatisation des flux de travail.

_Cette intégration est maintenue par Singular._

## À propos de l'intégration

L'intégration de Braze et Singular vous permet d'importer des données d'attribution d'installation payante pour segmenter intelligemment au sein de vos campagnes sur cycle de vie.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Singular | Un compte Singular est nécessaire pour profiter de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. En fonction de votre plateforme, des extraits de code peuvent être requis dans votre application. Vous trouverez des détails sur ces exigences à l'étape 1 du processus d'intégration. |
| SDK Singular | En plus du SDK Braze requis, vous devez installer le [SDK Singular](https://support.singular.net/hc/en-us/articles/360037640172-Getting-Started-with-the-Singular-SDK-S2S). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Mapper les ID utilisateur

#### Android

Si vous avez une application Android, vous devrez inclure l'extrait de code suivant, qui transmet un ID utilisateur unique de Braze à Singular.

```java
String appboyDeviceId = Braze.getInstance(context).getDeviceId();
SingularConfig config = new SingularConfig("SDK KEY", "SDK SECRET")
  .withGlobalProperty(“brazeDeviceID”, appboyDeviceId, true);
```
#### iOS

{% alert important %}
Avant février 2023, notre intégration d'attribution Singular utilisait l'IDFV comme identifiant principal pour faire correspondre les données d'attribution d'iOS. Il n'est pas nécessaire pour les clients de Braze utilisant Objective-C de récupérer l’ID `device_id` de Braze et de l'envoyer à Singular lors de l'installation car il n'y aura pas d'interruption de service.
{% endalert%}

Pour ceux qui utilisent le SDK Swift v5.7.0+, si vous souhaitez continuer à utiliser l'IDFV comme identifiant mutuel, vous devez vous assurer que le champ `useUUIDAsDeviceId` est défini sur `false` afin que rien ne vienne perturber l'intégration. 

Si la valeur est `true`, vous devez mettre en œuvre le mappage de l'ID de l'appareil iOS pour Swift afin de transmettre l'adresse `device_id` de Braze à Singular lors de l'installation de l'application pour que Braze corresponde correctement aux attributions d'iOS.

{% tabs local %}
{% tab Objective-C %}

```objc
SingularConfig* config = [[SingularConfig
  alloc] initWithApiKey:SDKKEY andSecret:SDKSECRET];

  [config setGlobalProperty:@"brazeDeviceId" withValue:brazeDeviceId
  overrideExisting:YES];
  [Singular start:config];
```

{% endtab %}
{% tab Swift%}

```swift
config.setGlobalProperty("brazeDeviceId", withValue: brazeDeviceId, overrideExisting: true)
```

{% endtab %}
{% endtabs %}

### Étape 2 : Obtenir la clé d'importation des données de Braze

Dans Braze, naviguez vers **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Singular**. 

Ici, vous trouverez l’endpoint REST et générerez votre clé d'importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. 

Vous devrez fournir la clé d'importation des données et l'endpoint REST à votre gestionnaire de compte Singular pour terminer l'intégration.<br><br>![Cette image montre la boîte "Importation de données pour l'attribution d'installation" qui se trouve sur la page de la technologie Singular. Dans cette boîte, la clé d'importation des données et l'endpoint REST sont affichés.]({% image_buster /assets/img/attribution/singular.png %}){: style="max-width:90%;"}

### Étape 3 : Confirmer l'intégration

Une fois que Braze aura reçu les données d'attribution de Singular, l'indicateur de connexion d'état sur la page des partenaires technologiques de Singular dans Braze passera de "Non connecté" à "Connecté". Un horodatage de la dernière requête réussie sera également inclus. 

Notez que cela ne se produira pas tant que nous n'aurons pas reçu de données d’une attribution d'installation. Les installations organiques, qui doivent être exclues du système de communication automatisé de Singular, sont ignorées par notre API et ne sont pas comptabilisées pour déterminer si une connexion a été établie avec succès.

## Données d'attribution de Facebook et de X (anciennement Twitter)

Les données d'attribution pour les campagnes Facebook et X (anciennement Twitter) ne sont pas disponibles auprès de nos partenaires. Ces sources médiatiques n'autorisent pas leurs partenaires à partager les données d'attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.

## URL de suivi des clics Singular dans Braze (facultatif)

L'utilisation de liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes favorisent les installations d'applications et le réengagement. Vous serez ainsi en mesure de mesurer plus efficacement vos efforts de marketing et de prendre des décisions fondées sur des données pour savoir où investir davantage de ressources afin d'obtenir un ROI maximal.

Pour commencer à utiliser les liens de suivi des clics de Singular, consultez leur [documentation](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true). Vous pouvez insérer les liens de suivi des clics de Singular directement dans vos campagnes Braze. Singular utilisera alors ses [méthodes d'attribution probabiliste](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true) pour attribuer l'utilisateur qui a cliqué sur le lien. Nous vous recommandons d'ajouter à vos liens de suivi Singular un identifiant d'appareil afin d'améliorer la précision des attributions de vos campagnes Braze. Cela permettra d'attribuer de manière déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs local %}
{% tab Android %}
Pour Android, Braze permet à ses clients de s'abonner à la [collecte d'ID publicitaires de Google (GAID).]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id) Le GAID est également collecté de manière native grâce à l'intégration du SDK Singular. Vous pouvez inclure le GAID dans vos liens de suivi des clics Singular en utilisant la logique Liquid suivante :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Singular collectent automatiquement l'IDFV de manière native grâce à nos intégrations SDK. Il peut être utilisé comme identifiant de l'appareil. Vous pouvez inclure l'IDFV dans vos liens de suivi des clics Singular en utilisant la logique Liquid suivante :

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
Si vous n'utilisez actuellement aucun identifiant d'appareil - tel que l'IDFV ou le GAID - dans vos liens de suivi des clics, ou si vous ne prévoyez pas de le faire à l'avenir, Singular sera toujours en mesure d'attribuer ces clics grâce à sa modélisation probabiliste.
{% endalert %}


