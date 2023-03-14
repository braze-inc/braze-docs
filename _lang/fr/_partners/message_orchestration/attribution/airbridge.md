---
nav_title: Airbridge
article_title: Airbridge
alias: /partners/airbridge/
description: "Cet article présente le partenariat entre Braze et Airbridge, qui offre une attribution basée sur les personnes et une mesure de l’incrémentalité pour mesurer la véritable efficacité du marketing à travers les appareils, les identités et les plateformes."
page_type: partner
search_tag: Partenaire

---

# Airbridge

> [Airbridge](https://www.airbridge.io/) est une plateforme de mesure mobile unifiée qui vous aide à découvrir les véritables sources de croissance grâce à l’attribution mobile, à la mesure de l'incrémentalité et à la modélisation du mix marketing.

L’intégration de Braze et Airbridge vous permet de transmettre toutes les données d’attribution d'installation non organiques d’Airbridge à Braze pour créer des campagnes marketing personnalisées et comprendre exactement où les utilisateurs ont été acquis.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Airbridge | Un compte Airbridge est requis pour profiter de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plateforme, les extraits de code peuvent être requis dans votre application. |
| SDK Airbridge | En plus du SDK Braze requis, vous devez installer le SDK Airbridge pour [Android](https://developers.airbridge.io/v1.1-en/docs/android-sdk) ou [iOS](https://developers.airbridge.io/v1.1-en/docs/ios-sdk). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Mapper l’ID d’appareil

L’intégration serveur à serveur peut être activée en incluant les snippets de code suivants dans vos applications.

#### Android

Si vous avez une application Android, vous devez transmettre un ID d’appareil Braze unique à Airbridge.

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
// MainApplciation.java
@Override
public void onCreate() {
    super.onCreate();
    // Initialize Airbridge SDK
    AirbridgeConfig config = new AirbridgeConfig.Builder("APP_NAME", "APP_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build();
    Airbridge.init(this, config);
    
    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).getDeviceId());
    // Explicitly start tracking
    Airbridge.startTracking();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// MainApplication.kt
override fun onCreate() {
    super.onCreate()
    // Initialize Airbridge SDK
    val config = AirbridgeConfig.Builder("YOUR_APP_NAME", "YOUR_APP_SDK_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build()
    Airbridge.init(this, config)

    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).deviceId)
    // Explicitly start tracking
    Airbridge.startTracking()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### iOS

Si vous avez une appli iOS, vous pouvez choisir de collecter l’IDFV en définissant le champ useUUIDAsDeviceId sur « false ». S’il n’est pas configuré, l’attribution iOS ne sera probablement pas bien définie entre Airbridge et Braze. Pour plus d’informations, consultez Recueillir les IDFV.

{% tabs %}
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

```swift
// AppDelegate.swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]?
) {
    AirBridge.setAutoStartTrackingEnabled(false)
    AirBridge.getInstance("YOUR_APP_TOKEN", appName:"YOUR_APP_NAME", withLaunchOptions:launchOptions)

    AirBridge.state()?.addUserAlias(withKey:"braze_device_id", value:Appboy.sharedInstance()?.getDeviceId())
    AirBridge.startTracking()
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// AppDelegate.m
-           (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  AirBridge.autoStartTrackingEnabled = NO;
  [AirBridge getInstance:@"YOUR_APP_TOKEN" appName:@"YOUR_APP_NAME" withLaunchOptions:launchOptions];

    [AirBridge.state addUserAliasWithKey:@"braze_device_id" value:Appboy.sharedInstance.getDeviceId];
    [AirBridge startTracking];
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### React Native

{% tabs %}
{% tab TypeScript %}

```typescript
Braze.getInstallTrackingId(function (error, brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
    Airbirdge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Cordova

{% tabs %}
{% tab TypeScript %}

```typescript
AppboyPlugin.getDeviceId(function (brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Flutter

{% tabs %}
{% tab TypeScript %}

```typescript
BrazePlugin.getInstallTrackingId().then((brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Unity

{% tabs %}
{% tab C# %}

```c#
string BrazeID = AppboyBinding.GetInstallTrackingId();
AirbridgeUnity.SetDeviceAlias("braze_device_id", BrazeID);
AirbridgeUnity.StartTracking()
```

{% endtab %}
{% endtabs %}

### Étape 2 : Obtenir la clé d’importation des données Braze

Dans Braze, accédez à **Technology Partners (partenaires technologiques)** et sélectionnez **Airbridge**. Ici, vous trouverez l’endpoint REST pour générer votre clé d’importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d’importation des données et l’endpoint REST sont utilisés dans l’étape suivante lors de la configuration d’un postback dans le tableau de bord d’Airbridge.

![][1]

### Étape 3 : Configurer Braze dans le tableau de bord d’Airbridge

1. Dans Airbridge, naviguez jusqu’à **Integrations > Third-party Integrations (Intégrations > Intégrations tierces)** dans la barre latérale gauche et sélectionnez **Braze**.
2. Fournissez la clé d’importation des données et l’endpoint REST que vous avez trouvés dans le tableau de bord de Braze.
3. Sélectionnez le type d’événement (Installer un événement ou Installer et Deeplink Ouvrir un événement) et enregistrer.

{% alert note %}
Les données d’attribution pour les campagnes qui ont menées à des événements ouverts deeplink sont mises à jour au niveau de l’appareil. Par exemple, si deux utilisateurs utilisent un seul appareil et qu’un utilisateur exécute un événement de lien profond, les données d’attribution de cet événement sont également reflétées dans les données de l’autre utilisateur.
{% endalert %}

Pour des instructions plus détaillées, consultez [Airbridge](https://help.airbridge.io/hc/en-us/articles/900004368546-Braze).

### Étape 4 : Confirmer l’intégration

Lorsque Braze reçoit les données d’attribution d’Airbridge, l’indicateur de l’état de connexion sur la page des partenaires de technologie d’Airbridge dans Braze passe de « Not connected » (Non connecté) à « Connected » (Connecté). Un timestamp de la dernière demande réussie sera également inclus.

Notez que cela ne se produira pas tant que nous ne recevrons pas de données sur une installation attribuée. Les installations organiques, qui doivent être exclues du postback d’Airbridge, sont ignorées par notre API et ne sont pas comptées lors de la détermination si une connexion réussie a été établie.

## Champs de données disponibles

Airbridge peut envoyer quatre types de données d’attribution à Braze, répertoriés dans le tableau des champs de données suivant. Ces données peuvent être affichées dans le tableau de bord d’Airbridge et sont utilisées pour l’attribution d’installation et le filtrage.

En supposant que vous configurez votre intégration comme indiqué, Braze mappera toutes les données d’installation pour segmenter les filtres.

| Champ de données Airbridge | Filtre de segment Braze | Description |
| -------------------- | ---------------------| ---- |
| `Channel` | Source d’attribution d’installation | Le canal d’installation ou de lien profond est attribué à |
| `Campaign` | Campagne d’attribution d’installation | La campagne d’installation ou de lien profond est attribuée à |
| `Publicité de groupe` | Groupe d’annonces d’attribution d’installation | Le groupe d’annonces ou les fenêtres d’installation ou de lien profond sont attribués à |
| `Publicité créative` | Annonce d’attribution d’installation | L’annonce publicitaire de l’installation ou de lien profond est attribuée à |

Votre base d’utilisateurs peut être segmentée par des données d’attribution dans le tableau de bord de Braze à l’aide des filtres d’attribution d’installation.

![][2]

## Données d’attribution Meta Business

Les données d’attribution pour les campagnes Meta Business ne sont pas disponibles par l’intermédiaire de nos partenaires. Cette source de médias ne permet pas à leurs partenaires de partager des données d’attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.

## URL d’Airbridge de suivi des clics dans Braze (optional)

L’utilisation des liens de suivi de vos campagnes Braze vous permettra de voir facilement quelles campagnes stimulent les installations des applications et le réengagement. Par conséquent, vous serez en mesure de mesurer vos efforts marketing plus efficacement et de prendre des décisions axées sur les données pour investir davantage de ressources selon le retour sur investissement (ROI) maximal.

Pour commencer avec les liens de suivi des clics Airbridge, consultez [Airbridge](https://help.airbridge.io/hc/en-us/articles/900001037886-Tracking-Link-Generation/). Une fois la configuration terminée, vous pouvez insérer directement les liens de suivi Airbridge dans vos campagnes Braze. Airbridge utilisera ensuite ses [méthodologies d’attribution probabilistes](https://help.airbridge.io/hc/en-us/articles/900003300526-Airbridge-Identity-Matching-Logic) pour attribuer l’utilisateur qui a cliqué sur le lien. Nous vous recommandons d’ajouter à vos liens de suivi Airbridge un identifiant d’appareil afin d’améliorer la précision des attributions de vos campagnes Braze. L’utilisateur ayant cliqué sur le lien sera attribué de manière déterministe.

{% tabs %}
{% tab Android %}
Pour Android, Braze permet aux clients de s’abonner à la [collection d’ID publicitaires Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté de manière native par l’intégration du SDK Airbridge. Vous pouvez inclure le GAID dans les liens de suivi de votre Airbridge en utilisant la logique Liquid suivante :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Airbridge collectent automatiquement l’IDFV de manière native via nos intégrations SDK. Cela peut être utilisé comme identifiant d’appareil. Vous pouvez inclure l’IDFV dans les liens de suivi de votre Airbridge en utilisant la logique Liquid suivante :

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
Si vous n’utilisez actuellement aucun identifiant d’appareil, comme IDFV ou GAID, dans vos liens de suivi de clic, ou si vous ne le prévoyez pas à l’avenir, Airbridge pourra toujours attribuer ces clics via ses modélisations probabilistes.
{% endalert %}

[1]: {% image_buster /assets/img/airbridge/airbridge_integration_step_1.png %}
[2]: {% image_buster /assets/img/airbridge/airbridge_integration_step_2.png %}
