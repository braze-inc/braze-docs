---
nav_title: Airbridge
article_title: Airbridge
alias: /partners/airbridge/
description: "Cet article de référence décrit le partenariat entre Braze et Airbridge, qui offre une attribution basée sur les personnes et une mesure incrémentielle pour mesurer l'efficacité réelle du marketing sur les appareils, les identités et les plateformes."
page_type: partner
search_tag: Partner

---

# Airbridge

> [Airbridge](https://www.airbridge.io/) est une plateforme de mesure mobile unifiée qui vous aide à découvrir les véritables sources de croissance grâce à l'attribution mobile, à la mesure incrémentielle et à la modélisation du mix marketing.

_Cette intégration est maintenue par Airbridge._

## À propos de l'intégration

L'intégration de Braze et Airbridge vous permet de transmettre toutes les données d'attribution d'installation non organiques d'Airbridge à Braze pour créer des campagnes marketing personnalisées.

## Conditions préalables

| Condition | Description |
|---|---|
| compte Airbridge | Un compte Airbridge est nécessaire pour profiter de ce partenariat. |
| application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. En fonction de votre plateforme, des extraits de code peuvent être nécessaires dans votre application. |
| Airbridge SDK | Outre le SDK Braze requis, vous devez installer le SDK Airbridge [Android](https://help.airbridge.io/en/developers/android-sdk) ou [iOS](https://help.airbridge.io/en/developers/ios-sdk). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Mapper l’ID de l'appareil

L'intégration serveur-à-serveur peut être activée en incluant les extraits de code suivants dans vos applications.

#### Android

Si vous avez une application Android, vous devrez transmettre un ID d'appareil Braze unique à Airbridge.

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

Si vous avez une application iOS, vous pouvez choisir de collecter l'IDFV en définissant le champ useUUIDAsDeviceId sur false. S'il n'est pas défini, l'attribution iOS ne sera probablement pas mappée avec précision d'Airbridge à Braze. Pour plus d'informations, consultez la collecte de l'IDFV.

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

#### React native

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

### Étape 2 : Obtenir la clé d'importation des données de Braze

Dans Braze, accédez à **Intégrations de partenaires** > **Partenaires technologiques** et sélectionnez **Airbridge**.

Vous y trouverez l'endpoint REST et générerez votre clé d'importation des données Braze. Après la génération de la clé, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation des données et l'endpoint REST sont utilisés à l'étape suivante lors de la configuration d'un système automatisé de communication dans le tableau de bord d'Airbridge.

![]({% image_buster /assets/img/airbridge/airbridge_integration_step_1.png %})

### Étape 3 : Configurez Braze dans le tableau de bord d'Airbridge

1. Dans Airbridge, accédez à **Intégrations > Intégrations tierces** dans la barre latérale gauche et sélectionnez **Braze**.
2. Indiquez la clé d'importation des données et le point de terminaison REST que vous avez trouvés dans le tableau de bord de Braze.
3. Sélectionnez le type d'événement (Événement d'installation ou Événement d'installation et d'ouverture de lien profond) et enregistrer.

{% alert note %}
Les données d'attribution pour les campagnes qui ont conduit à des événements d'ouverture de lien profond sont mises à jour au niveau de l'appareil. Par exemple, si deux utilisateurs utilisent un seul appareil et qu'un utilisateur effectue un événement d'ouverture de lien profond, les données d'attribution de cet événement sont également reflétées dans les données de l'autre utilisateur.
{% endalert %}

Pour des instructions plus détaillées, visitez [Airbridge](https://help.airbridge.io/en/guides/braze).

### Étape 4 : Confirmer l'intégration

Une fois que Braze reçoit les données d'attribution d'Airbridge, l'indicateur d’état de la connexion sur la page des partenaires technologiques d'Airbridge dans Braze passera de "Non connecté" à "Connecté". Un horodatage de la dernière requête réussie sera également inclus.

Notez que cela ne se produira pas tant que nous n'aurons pas reçu de données concernant une installation attribuée. Les installations organiques, qui doivent être exclues du système de communication automatisé Airbridge, sont ignorées par notre API et ne sont pas prises en compte lors de la détermination de l'établissement d'une connexion réussie.

## Champs de données disponibles

Airbridge peut envoyer quatre types de données d'attribution à Braze répertoriés dans le tableau de données suivant. Ces données peuvent être consultées dans le tableau de bord Airbridge et sont utilisées pour l'attribution et le filtrage des installations des utilisateurs.

En supposant que vous configurez votre intégration comme suggéré, Braze mappera les données d'installation aux filtres de segment.

| Airbridge champ de donnée | Filtre de segments Braze | Description |
| -------------------- | ---------------------| ---- |
| `Channel` | Source d'attribution d'installation | Le canal auquel les installations ou les liens profonds sont attribués |
| `Campaign` | Campagne d’attribution d'installations | La campagne à laquelle les installations ou les ouvertures de deeplink sont attribuées |
| `Ad Group` | Groupe d’annonces d’attribution d'installations | Le groupe d'annonces auquel les installations ou les ouvertures de deeplink sont attribuées |
| `Ad Creative` | Publicité d'attribution d'installation | Le contenu publicitaire auquel les installations ou les ouvertures de liens profonds sont attribuées |

Votre base d'utilisateurs peut être segmentée par les données d'attribution dans le tableau de bord de Braze en utilisant les filtres d'attribution d'installation.

![]({% image_buster /assets/img/airbridge/airbridge_integration_step_2.png %})

## Données d'attribution Meta Business

Les données d'attribution pour les campagnes Meta Business ne sont pas disponibles via nos partenaires. Cette source de média ne permet pas à ses partenaires de partager les données d'attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.

## URLs de suivi des clics Airbridge dans Braze (optionnel)

L'utilisation de liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes génèrent des installations d'applications et du réengagement. En conséquence, vous serez en mesure de mesurer plus efficacement vos efforts marketing et de prendre des décisions basées sur les données concernant l'endroit où investir plus de ressources pour un ROI maximal.

Pour commencer avec les liens de suivi des clics Airbridge, visitez [Airbridge](https://help.airbridge.io/en/guides/creating-a-new-tracking-link). Après avoir terminé la configuration, vous pouvez directement insérer les liens de suivi des clics Airbridge dans vos campagnes Braze. Airbridge utilisera ensuite ses [méthodologies d'attribution probabiliste](https://help.airbridge.io/en/guides/identity-matching) pour attribuer l'utilisateur qui a cliqué sur le lien. Nous recommandons d'ajouter vos liens de suivi Airbridge avec un identifiant d'appareil pour améliorer la précision des attributions de vos campagnes Braze. Cela attribuera de manière déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs %}
{% tab Android %}
Pour Android, Braze permet aux clients de s'abonner à la [collecte de l'ID publicitaire de Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté nativement via l'intégration du SDK Airbridge. Vous pouvez inclure le GAID dans vos liens de suivi de clics Airbridge en utilisant la logique Liquid suivante :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Airbridge collectent automatiquement l'IDFV nativement via nos intégrations de SDK. Cela peut être utilisé comme identifiant de l'appareil. Vous pouvez inclure l'IDFV dans vos liens de suivi de clics Airbridge en utilisant la logique Liquid suivante :

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
Si vous n'utilisez actuellement aucun identifiant d'appareil - tel que l'IDFV ou le GAID - dans vos liens de suivi de clics, ou ne prévoyez pas de le faire à l'avenir, Airbridge sera toujours en mesure d'attribuer ces clics grâce à leur modélisation probabiliste.
{% endalert %}


