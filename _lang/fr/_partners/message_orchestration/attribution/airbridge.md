---
nav_title: Airbridge
article_title: Airbridge
alias: /partners/airbridge/
description: "Cet article présente le partenariat entre Braze et Airbridge, qui offre une attribution basée sur les personnes et une mesure de l’incrémentalité pour mesurer la véritable efficacité du marketing à travers les appareils, les identités et les plateformes."
page_type: partner
search_tag: Partenaire

---

# Airbridge

> Airbridge offre une attribution basée sur les personnes et une mesure de l’incrémentalité pour mesurer et analyser la véritable efficacité du marketing à travers les appareils, les identités et les plateformes.

L’intégration de Braze et Airbridge vous permet de transmettre toutes les données d’attribution des installations organiques et non organiques à Braze pour créer des campagnes marketing personnalisées et comprendre exactement où les utilisateurs ont été acquis.

## Conditions préalables

| Configuration requise | Description |
|---|---|
| Compte Airbridge | Un compte Airbridge est requis pour profiter de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plateforme, les extraits de code peuvent être requis dans votre application. |
| SDK Airbridge | En plus du SDK Braze requis, vous devez installer le SDK Airbridge pour [Android](https://developers.airbridge.io/v1.0-en-us/docs/android-sdk) ou [iOS](https://developers.airbridge.io/v1.0-en-us/docs/ios-sdk). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

L’intégration de Airbridge à Braze sera effectuée de SDK à SDK. Les données d’attribution collectées par le SDK Airbridge seront transmises à Braze via le SDK Braze. Incluez l’extrait de code suivant dans votre application Android ou iOS.

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
AirbridgeConfig config = new AirbridgeConfig.Builder(BuildConfig.AIRBRIDGE_APP_NAME, BuildConfig.AIRBRIDGE_APP_TOKEN)
        .setOnAttributionResultReceiveListener(new OnAttributionResultReceiveListener() {
            @Override
            public void onAttributionResultReceived(Map<String, String> result) {
                AttributionData data = new AttributionData(
                    result.get("attributedChannel"),
                    result.get("attributedCampaign"),
                    result.get("attributedAdGroup"),
                    result.get("attributedAdCreative")
                );
              
                Braze.getInstance(applicationContext).getCurrentUser().setAttributionData(data);

                // NOTE: Data point will be consumed
                Braze.getInstance(applicationContext).getCurrentUser().setCustomUserAttribute("airbridge_ad_content", result.get("attributedContent"));
                Braze.getInstance(applicationContext).getCurrentUser().setCustomUserAttribute("airbridge_term", result.get("attributedTerm"));
                Braze.getInstance(applicationContext).getCurrentUser().setCustomUserAttribute("airbridge_sub_id", result.get("attributedSubPublisher"));
                Braze.getInstance(applicationContext).getCurrentUser().setCustomUserAttribute("airbridge_sub_id_1", result.get("attributedSubSubPublisher1"));
                Braze.getInstance(applicationContext).getCurrentUser().setCustomUserAttribute("airbridge_sub_id_2", result.get("attributedSubSubPublisher2"));
                Braze.getInstance(applicationContext).getCurrentUser().setCustomUserAttribute("airbridge_sub_id_3", result.get("attributedSubSubPublisher3"));
            }
        })
        .build();
Airbridge.init(this, config);
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
val config = AirbridgeConfig.Builder(BuildConfig.AIRBRIDGE_APP_NAME, BuildConfig.AIRBRIDGE_APP_TOKEN)
        .setOnAttributionResultReceiveListener(object : OnAttributionResultReceiveListener {
            override fun onAttributionResultReceived(result: Map<String, String>) {
                val data = AttributionData(
                    result["attributedChannel"],
                    result["attributedCampaign"],
                    result["attributedAdGroup"],
                    result["attributedAdCreative"]
                )

                Braze.getInstance(applicationContext).currentUser?.setAttributionData(data)
                  
                // NOTE: Data point will be consumed
                Braze.getInstance(applicationContext).currentUser?.setCustomUserAttribute("airbridge_ad_content", result["attributedContent"])
                Braze.getInstance(applicationContext).currentUser?.setCustomUserAttribute("airbridge_term", result["attributedTerm"])
                Braze.getInstance(applicationContext).currentUser?.setCustomUserAttribute("airbridge_sub_id", result["attributedSubPublisher"])
                Braze.getInstance(applicationContext).currentUser?.setCustomUserAttribute("airbridge_sub_id_1", result["attributedSubSubPublisher1"])
                Braze.getInstance(applicationContext).currentUser?.setCustomUserAttribute("airbridge_sub_id_2", result["attributedSubSubPublisher2"])
                Braze.getInstance(applicationContext).currentUser?.setCustomUserAttribute("airbridge_sub_id_3", result["attributedSubSubPublisher3"])
            }
        })
        .build()
Airbridge.init(this, config)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}
```swift
@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication, 
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AirBridge.setting()?.attributionCallback = { attribution in
            let data = ABKAttributionData(network: attribution["attributedChannel"],
                                          campaign: attribution["attributedCampaign"],
                                          adGroup: attribution["attributedAdGroup"],
                                          creative: attribution["attributedAdCreative"])
            
            // NOTE: Data point will be consumed
            Appboy.sharedInstance()?.user.attributionData = data
            
            [
                "attributedContent": "airbridge_content",
                "attributedTerm": "airbridge_term",
                "attributedSubPublisher": "airbridge_sub_id",
                "attributedSubSubPublisher1": "airbridge_sub_id_1",
                "attributedSubSubPublisher2": "airbridge_sub_id_2",
                "attributedSubSubPublisher3": "airbridge_sub_id_3",
            ].forEach { (key, brazeKey) in
                guard let value = attribution[key] else {
                    return
                }
                
                Appboy.sharedInstance()?.user.setCustomAttributeWithKey(brazeKey, andStringValue: value)
            }
            
            Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
        }
      
        AirBridge.getInstance("YOUR_APP_TOKEN", appName: "YOUR_APP_NAME", withLaunchOptions: launchOptions)
      
        return true
    }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    AirBridge.setting.attributionCallback = ^(NSDictionary<NSString*, NSString*>* _Nonnull attribution) {
        ABKAttributionData* data = [[ABKAttributionData alloc] initWithNetwork:attribution[@"attributedChannel"]
                                                                      campaign:attribution[@"attributedCampaign"]
                                                                       adGroup:attribution[@"attributedAdGroup"]
                                                                      creative:attribution[@"attributedAdCreative"]];
        [Appboy.sharedInstance.user setAttributionData:data];

        // NOTE: Data point will be consumed
        NSDictionary* keyMap = @{
            @"attributedContent": @"airbridge_content",
            @"attributedTerm": @"airbridge_term",
            @"attributedSubPublisher": @"airbridge_sub_id",
            @"attributedSubSubPublisher1": @"airbridge_sub_id_1",
            @"attributedSubSubPublisher2": @"airbridge_sub_id_2",
            @"attributedSubSubPublisher3": @"airbridge_sub_id_3",
        };
        
        for (NSString* key in keyMap.allKeys) {
            NSString* brazeKey = keyMap[key];
            NSString* value = attribution[key];
            
            [Appboy.sharedInstance.user setCustomAttributeWithKey:brazeKey andStringValue:value];
        }
        
        [Appboy.sharedInstance flushDataAndProcessRequestQueue];
    };
  
    [AirBridge getInstance:"YOUR_APP_TOKEN" appName:"YOUR_APP_NAME" withLaunchOptions:launchOptions];

    return YES;
}

@end
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Champs de données disponibles

Airbridge peut envoyer sept types de données à Braze répertoriés dans le tableau des champs de données suivants. Ces données peuvent être affichées dans le tableau de bord d’Airbridge et sont utilisées pour l’attribution d’installation d’utilisateur, l’attribution personnalisée et le filtrage.

Outre les quatre types de données de base (Source, Campagne, Groupe d’annonces et Annonce) fournis par Braze, Airbridge propose trois types de données supplémentaires, comme `airbridge_content`, `airbridge_sub_id` et `airbridge_term`, comme attribut personnalisé. Parmi eux, `airbridge_sub_id` offre un mot-clé à la valeur lorsqu’elle provient des publicités de recherche.

{% alert important %}
Les points de données de Braze seront utilisés lorsque vous enverrez des données marquées comme facultatives, car elles sont transmises comme un attribut utilisateur personnalisé.
{% endalert %}

| Champ de données Airbridge | Filtre de segment Braze | Type | Description |
| -------------------- | ---------------------| ---- | ----------- |
| `attributedChannel` | Source d’attribution d’installation | Données d’attribution d’installation | Nom du canal publicitaire payé |
| `attributedCampaign` | Campagne d’attribution d’installation | Données d’attribution d’installation | Nom de la campagne |
| `attributedAdGroup` | Groupe d’annonces d’attribution d’installation | Données d’attribution d’installation | Nom du groupe d’annonces |
| `attributedAdCreative` | Annonce d’attribution d’installation | Données d’attribution d’installation | Nom du générateur d’annonce |
| `attributedContent` <br>
(Facultatif) | `airbridge_content` | Attribut utilisateur personnalisé | Nom de la copie publicitaire, du slogan et de la promotion |
| `attributedTerm` <br>
(Facultatif) | `airbridge_term` | Attribut utilisateur personnalisé | Type de média |
| `attributedSubPublisher` <br>
(Facultatif) | `airbridge_sub_id` | Attribut utilisateur personnalisé | Mot-clé de recherche publicitaire |
| `attributedSubSubPublisher1` <br>
(Facultatif) | `airbridge_sub_id_1` | Attribut utilisateur personnalisé | |
| `attributedSubSubPublisher2` <br>
(Facultatif) | `airbridge_sub_id_2` | Attribut utilisateur personnalisé | |
| `attributedSubSubPublisher3` <br>
(Facultatif) | `airbridge_sub_id_3` | Attribut utilisateur personnalisé | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Données d’attribution Facebook

Les données d’attribution pour les campagnes Facebook ne sont pas disponibles par l’intermédiaire de nos partenaires. Cette source de médias ne permet pas à leurs partenaires de partager des données d’attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.

## URL d’Airbridge de suivi des clics dans Braze (facultatif)

L’utilisation des liens de suivi de vos campagnes Braze vous permettra de voir facilement quelles campagnes stimulent les installations des applications et le réengagement. Par conséquent, vous serez en mesure de mesurer vos efforts marketing plus efficacement et de prendre des décisions axées sur les données pour investir davantage de ressources selon le retour sur investissement (ROI) maximal.

Pour commencer avec les liens Airbridge de suivi des clics, consultez la documentation disponible [ici](https://help.airbridge.io/hc/en-us/articles/900001037886-Tracking-Link-Generation/). Une fois la configuration terminée, vous pouvez insérer directement les liens de suivi Airbridge dans vos campagnes Braze. Airbridge utilisera ensuite ses [méthodologies d’attribution probabilistes](https://help.airbridge.io/hc/en-us/articles/900003300526-Airbridge-Identity-Matching-Logic) pour attribuer l’utilisateur qui a cliqué sur le lien. Nous vous recommandons d’ajouter à vos liens de suivi Airbridge un identifiant de périphérique afin d’améliorer la précision des attributions de vos campagnes Braze. L’utilisateur ayant cliqué sur le lien sera attribué de manière déterministe.

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
Pour iOS, Braze et Airbridge collectent automatiquement l’IDFV de manière native via nos intégrations SDK. Cela peut être utilisé comme identifiant de périphérique. Vous pouvez inclure l’IDFV dans les liens de suivi de votre Airbridge en utilisant la logique Liquid suivante :

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

Si vous n’utilisez actuellement aucun identifiant de périphérique, comme IDFV ou GAID, dans vos liens de suivi de clic, ou si vous ne le prévoyez pas à l’avenir, Airbridge pourra toujours attribuer ces clics via ses modélisations probabilistes.
{% endalert %}