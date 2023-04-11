---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "Cet article de référence décrit le partenariat entre Braze et AppsFlyer, une plateforme d’analytiques et d’attribution de marketing mobile qui vous aide à analyser et à optimiser vos applications."
page_type: partner
search_tag: Partenaire

---

# AppsFlyer

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> AppsFlyer est une plateforme d’analytiques et d’attribution de marketing mobile qui vous aide à analyser et à optimiser vos applications grâce à des analytiques marketing, à l’attribution mobile et à la création de liens profonds.

L’intégration Braze-AppsFlyer vous permet de mieux comprendre comment optimiser et créer des campagnes plus globales en tirant parti des données d’attribution d’installation mobile depuis AppsFlyer.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte AppsFlyer | Un compte AppsFlyer est requis pour profiter de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plateforme, les extraits de code peuvent être requis dans votre application. Vous trouverez des détails sur ces exigences à l’étape 1 du processus d’intégration. |
| SDK AppsFlyer | En plus du SDK Braze requis, vous devez installer le [SDK AppsFlyer](https://support.appsflyer.com/hc/en-us/categories/201114756-SDK-integration-). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Mapper l’ID d’appareil

#### Android

Si vous avez une application Android, vous devez transmettre un ID d’appareil Braze unique à AppsFlyer. 

Assurez-vous que les lignes de code suivantes sont insérées au bon endroit, après le lancement du SDK Braze et avant le code d’initialisation du SDK AppsFlyer. Voir le [Guide d’intégration SDK pour Android](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk) de AppsFlyer pour plus d’informations.

```java
HashMap<String, Object> customData = new HashMap<String,Object>();
String deviceId =(Braze.getInstance(MyActivity.this).getDeviceId());
customData.put("brazeCustomerId", deviceId);
AppsFlyerLib.setAdditionalData(customData);
```

#### iOS

{% alert important %}
Avant février 2023, notre intégration d’attribution AppsFlyer utilisait l’IDFV comme identifiant principal pour faire correspondre les données d’attribution iOS. Il n’est pas nécessaire que les clients de Braze utilisant Objective-C récupèrent le `device_id` de Braze et l’envoient à AppsFlyer lors de l’installation, car il n’y aura aucune interruption de service. 
{% endalert%}

Pour ceux qui utilisent le SDK Swift v5.7.0+, si vous souhaitez continuer à utiliser IDFV comme identifiant mutuel, vous devez vous assurer que le champ `useUUIDAsDeviceId` est défini sur `false` afin qu’il n’y ait aucune perturbation de l’intégration. 

Si cette option est définie sur `true`, vous devez implémenter le mappage d’ID d’appareil iOS pour Swift afin de transmettre le `device_id` de Braze à AppsFlyer lors de l’installation de l’application afin que Braze fasse corresponde correctement les attributions iOS.

{% tabs local %}
{% tab Objective-C %}

```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[braze deviceIdWithCompletion:^(NSString * _Nonnull brazeDeviceId) {
    NSLog(@">>[BRZ]: %@", brazeDeviceId);
    [[AppsFlyerLib shared] setAdditionalData:@{
        @"brazeDeviceId": brazeDeviceId
    }];
}];
```

{% endtab %}
{% tab Swift %}

##### Gestionnaire d’achèvement Swift
```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
braze.deviceId {
    brazeDeviceId in
    AppsFlyerLib.shared().customData = ["brazeDeviceId": brazeDeviceId]
}
```
##### Swift attend
```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
let brazeDeviceId = await braze.deviceId()
AppsFlyerLib.shared().customData = ["brazeDeviceId": brazeDeviceId]
```

{% endtab %}
{% endtabs %}

#### Unity

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```

### Étape 2 : Obtenir la clé d’importation des données Braze

Dans Braze, accédez à **Technology Partners (Partenaires technologiques)** et sélectionnez **AppsFlyer**. Ici, vous trouverez l’endpoint REST pour générer votre clé d’importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d’importation des données et l’endpoint REST sont utilisés dans l’étape suivante lors de la configuration d’un postback dans le tableau de bord d’AppsFlyer.<br><br>![La zone « Data Import for Install Attribution » (Importation de données pour l’attribution d’installation) est disponible sur la page AppsFlyer Technology. Cette section inclut la clé d’importation des données et l’endpoint REST.][4]{: style="max-width:70%;"}

### Étape 3 : Configurer Braze dans le tableau de bord d’AppsFlyer

1. Dans AppsFlyer, accédez à la page **Integrated Partners (Partenaires intégrés)** sur la barre de gauche. Ensuite, recherchez **Braze** et cliquez sur le logo Braze pour ouvrir une fenêtre de configuration.
2. Dans l’onglet **Integration (Intégration)**, sélectionnez **Activate Partner (Activer un partenaire)**.
3. Fournissez la clé d’importation des données et l’endpoint REST que vous avez trouvés dans le tableau de bord de Braze. 
4. Désactivez **Advanced Privacy (Confidentialité avancée)** et enregistrez votre configuration.

Des informations supplémentaires sur ces instructions sont disponibles dans la [documentation d’AppsFlyer][16].

### Étape 4 : Confirmer l’intégration

Lorsque Braze reçoit les données d’attribution d’AppsFlyer, l’indicateur de l’état de connexion sur la page des partenaires de technologie d’AppsFlyer dans Braze passe de « Not Connected » (Non connecté) à « Connected » (Connecté). Un horodatage de la dernière demande réussie sera également inclus. 

Notez que cela ne se produira pas tant que nous ne recevrons pas de données sur une installation attribuée. Les installations organiques, qui doivent être exclues du postback d’AppsFlyer, sont ignorées par notre API et ne sont pas comptées lors de la détermination si une connexion réussie a été établie.

### Étape 5 : Affichage des données d’attribution de l’utilisateur

#### Champs de données disponibles

En supposant que vous configurez votre intégration comme indiqué, Braze mappera toutes les données d’installation organiques et non organiques pour segmenter les filtres.

| Champ de données AppsFlyer | Filtre de segment Braze |
| -------------------- | --------------------- |
| `media_source` | Source attribuée |
| `campaign` | Campagne attribuée |
| `af_adset` | Groupe d’annonces attribué |
| `af_ad` | Annonce attribuée |
{: .reset-td-br-1 .reset-td-br-2}

Votre base d’utilisateurs peut être segmentée par des données d’attribution dans le tableau de bord de Braze à l’aide des filtres d’attribution d’installation.

![Quatre filtres disponibles. Le premier est « Install Attribution Source is network_val_0 ». Le deuxième est « Install Attribution Source is campaign_val_0 ». Le troisième est « Install Attribution Source is adgroup_val_0 ». Le quatrième est « Install Attribution Source is creative_val_0 ». En regard des filtres répertoriés, vous pouvez voir comment ces sources d’attribution seront ajoutées au profil utilisateur. Dans la zone « Install Attribution » (Attribution d’installation) sur la page d’informations d’un utilisateur, la source d’installation est répertoriée comme network_val_0, la campagne est répertoriée campaign_val_0 etc.][2]

De plus, les données d’attribution d’un utilisateur particulier sont disponibles sur le profil de chaque utilisateur dans le tableau de bord de Braze.

## Données d’attribution Facebook, Snapchat et Twitter

Les données d’attribution pour les campagnes Facebook et Twitter ne sont pas disponibles par l’intermédiaire de nos partenaires. Ces sources de médias ne permettent pas à leurs partenaires de partager des données d’attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.

## Liens profonds par e-mail et suivi des clics

Les liens profonds, les liens qui dirigent les utilisateurs vers une page spécifique ou qui sont placés dans une application ou un site Internet sont essentiels pour créer une expérience utilisateur personnalisée. Bien que largement utilisés, les problèmes surviennent souvent lorsque vous les utilisez avec un suivi de clic, une autre fonctionnalité vitale utilisée pour collecter les données utilisateur. Ces problèmes sont dus aux ESP (fournisseurs de services d’e-mail) qui enveloppent les liens profonds dans leur propre domaine d’enregistrement des clics et modifient le lien original. 

Il y a, toutefois, des ESP comme SendGrid qui prennent en charge les liens profonds et le suivi des clics. Braze recommande d’intégrer les [liens d’attribution basés sur Onelink][3] dans votre système de messagerie SendGrid ou [SparkPost](https://support.appsflyer.com/hc/en-us/articles/360014381317-SparkPost-integration-with-AppsFlyer) pour insérer de manière harmonieuse les liens profonds dans vos e-mails.

### URL de suivi des clics d’AppsFlyer dans Braze (facultatif)

Vous pouvez utiliser les [liens d’attribution Onelink](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) d’AppsFlyer dans les campagnes Braze à travers les notifications push, les e-mails et plus encore. Cela vous permet d’envoyer des données d’attribution ou de réengagement de l’attribution de leurs campagnes Braze dans AppsFlyer. Par conséquent, vous serez en mesure de mesurer vos efforts marketing plus efficacement et de prendre des décisions axées sur les données pour investir davantage de ressources selon le retour sur investissement (ROI) maximal.

Vous pouvez simplement créer votre URL de suivi Onelink dans AppsFlyer et l’insérer directement dans vos campagnes Braze. AppsFlyer utilisera ensuite ses [méthodologies d’attribution probabilistes](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) pour attribuer l’utilisateur qui a cliqué sur le lien. Nous vous recommandons d’associer vos liens de suivi AppsFlyer à un identifiant d’appareil pour améliorer la précision des attributions de vos campagnes Braze. L’utilisateur ayant cliqué sur le lien sera attribué de manière déterministe.

{% tabs local %}
{% tab Android %}
Pour Android, Braze permet aux clients de s’abonner à la [collection d’ID publicitaires Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté de manière native par l’intégration SDK AppsFlyer. Vous pouvez inclure le GAID dans vos liens AppsFlyer de suivi de clics en utilisant la logique Liquid suivante :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et AppsFlyer collectent automatiquement l’IDFV par l’intermédiaire de nos intégrations SDK. Cela peut être utilisé comme identifiant d’appareil. Vous pouvez inclure l’IDFV dans votre navigateur AppsFlyer en cliquant sur la logique Liquid suivante :

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
Si vous n’utilisez actuellement aucun identifiant d’appareil, comme IDFV ou GAID, dans vos liens de suivi de clic, ou si vous ne le prévoyez pas à l’avenir, AppsFlyer pourra toujours attribuer ces clics via ses modélisations probabilistes.
{% endalert %}

[1]: {% image_buster /assets/img/braze_integration.png %}
[2]: {% image_buster /assets/img/braze_attribution.png %}
[3]: https://support.appsflyer.com/hc/en-us/articles/360001294118
[16]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration "AppsFlyer Push API"
[31]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Braze-Formerly-Appboy-Integration
[4]: {% image_buster /assets/img/attribution/appsflyer.png %}
