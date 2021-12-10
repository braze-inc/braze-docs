---
nav_title: Airbridge
article_title: Airbridge
alias: /fr/partners/airbridge
description: "Cet article décrit le partenariat entre Braze et Airbridge, qui offre des mesures d'attribution et d'incrémentalité basées sur les personnes pour mesurer l'efficacité réelle du marketing entre les appareils, les identités et les plates-formes."
page_type: partenaire
search_tag: Partenaire
---

# Airbridge

> Airbridge offre des mesures d'attribution et d'incrémentalité basées sur les personnes pour mesurer et analyser l'efficacité réelle du marketing sur les appareils, les identités et les plates-formes.

Avec Airbridge et Braze, vous pouvez transmettre toutes les données d’attribution d’installation organique et non organique à Braze pour construire des campagnes de marketing plus personnalisées et comprendre exactement où les utilisateurs ont été acquis.

## Intégration

Pour en savoir plus sur l'intégration d'Airbridge et de Braze, veuillez visiter la [documentation Airbridge](https://developers.airbridge.io/v1.0-en-us/docs/braze).

### Étape 1 : Exigences d'intégration

* Cette intégration prend en charge les applications iOS et Android.
* Votre application aura besoin du SDK de Braze et du SDK d'Airbridge installés.

### Étape 2 : Inclure le snippet de code

L'intégration d'Airbridge à Braze se fera via SDK-to-SDK. Les données d'attribution recueillies par Airbridge SDK seront transmises à Braze via le Braze SDK. Inclure le code snippet suivant dans votre application Android ou iOS.

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
AirbridgeConfig config = new AirbridgeConfig.Builder(BuildConfig.AIRBRIDGE_APP_NAME, BuildConfig.AIRBRIDGE_APP_TOKEN)
        . etOnAttributionResultReceiveListener(new OnAttributionResultReceiveListener() {
            @Override
            public void onAttributionResultReceived(Map<String, String> result) {
                AttributionData data = new AttributionData(
                    resultat. et("attributedChannel"),
                    résultat. et("attributedCampaign"),
                    résultat. et("attributedAdGroup"),
                    résultat. et("attributedAdCreative")
                );

                Brésil. etInstance(applicationContext). etUtilisateur(). etAttributionData(données) ;

                // NOTE: Le point de données sera consommé
                Brésil. etInstance(applicationContext).getCurrentUser().setCustomUserAttribute("airbridge_ad_content", résultat. et("attributedContent"));
                Braze.getInstance(applicationContext).getCurrentUser(). etCustomUserAttribute("airbridge_term", result.get("attributedTerm"));
                Braze.getInstance(applicationContext). etCurrentUser().setCustomUserAttribute("airbridge_sub_id", result.get("attributedSubPublisher"));
                Braze.getInstance(applicationContext).getCurrentUser().setCustomUserAttribute("airbridge_sub_id_1", résultat. et("attributedSubSubPublisher1"));
                Braze.getInstance(applicationContext).getCurrentUser(). etCustomUserAttribute("airbridge_sub_id_2", result.get("attributedSubSubPublisher2"));
                Braze. etInstance(applicationContext).getCurrentUser().setCustomUserAttribute("airbridge_sub_id_3", résultat. et("attributedSubPublisher3"));
            }
        })
        . uild();
Airbridge.init(ceci, config);
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
val config = AirbridgeConfig.Builder(BuildConfig.AIRBRIDGE_APP_NAME, BuildConfig.AIRBRIDGE_APP_TOKEN)
        . etOnAttributionResultReceiveListener(object : OnAttributionResultReceiveListener {
            surcharge fun onAttributionResultReceived(result: Map<String, String>) {
                données val = AttributionData(
                    result["attributedChannel"],
                    résultat["attributedCampaign"],
                    résultat["attributedAdGroup"],
                    résultat["attributedAdCreative"]
                )

                Brésil. etInstance(applicationContext).currentUser?. etAttributionData(data)

                // NOTE: Le point de données sera consommé
                Braze. etInstance(applicationContext).currentUser?.setCustomUserAttribute("airbridge_ad_content", result["attributedContent"])
                Braze. etInstance(applicationContext).currentUser?.setCustomUserAttribute("airbridge_term", result["attributedTerm"])
                Braze.getInstance(applicationContext).currentUser?. etCustomUserAttribute("airbridge_sub_id", result["attributedSubPublisher"])
                Braze.getInstance(applicationContext). urrentUser?.setCustomUserAttribute("airbridge_sub_id_1", result["attributedSubSubSubPublisher1"])
                Braze. etInstance(applicationContext).currentUser?.setCustomUserAttribute("airbridge_sub_id_2", result["attributedSubSubPublisher2"])
                Braze.getInstance(applicationContext).currentUser?. etCustomUserAttribute("airbridge_sub_id_3", result["attributedSubSubPublisher3"])
            }
        })
        . uild()
Airbridge.init(ceci, config)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}
```swift
@UIApplicationMain
classe AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication, 
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AirBridge.setting()?. ttributionCallback = { attribution in
            let data = ABKAttributionData(network: attribution["attributedChannel"],
                                          campagne: attribution["attributedCampaign"],
                                          adGroup: attribution["attributedAdGroup"],
                                          creative: attribution["attributedAdCreative"])

            // NOTE: Le point de données sera consommé
            Appboy. haredInstance()?.user ttributionData = data

            [
                "attributedContent": "airbridge_content",
                "attributedTerm": "airbridge_term",
                "AttributedSubPublisher": "airbridge_sub_id",
                "attributedSubSubSubPublisher1": "airbridge_sub_id_1",
                "attributedSubSubSubPublisher2": "airbridge_sub_id_2",
                "attributedSubSubSubPublisher3": "airbridge_sub_id_3",
            ]. orChaque { (clé, brazeKey) dans
                garde let value = attribution[key] else {
                    return
                }

                Appboy. haredInstance()?.user etCustomAttributeWithKey(brazeKey, andStringValue: value)
            }

            Appboy. haredInstance()?.flushDataAndProcessRequestQueue()
        }

        AirBridge. etInstance("VOTRE_APP_TOKEN", appName: "VOTRE_APP_NAME", withLaunchOptions: launchOptions)

        return true
    }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    AirBridge.setting. ttributionCallback = ^(NSDictionary<NSString*, NSString*>* attribut _Nonnulle) {
        ABKAttributionData* data = [[ABKAttributionData alloc] initWithNetwork:attribution[@"attributedChannel"]
                                                                      campaign:attribution[@"attributedCampaign"]
                                                                       adGroup:attribution[@"attributedAdGroup"]
                                                                      creative:attribution[@"attributedAdGroup"]];
        [Appboy. Instance partagée. ser setAttributionData:data];

        // NOTE: Le point de données sera consommé
        NSDictionary* keyMap = @{
            @"attributedContent": @"airbridge_content",
            @"attributedTerm": @"airbridge_term",
            @"attributedSubPublisher": @"airbridge_sub_id",
            @"attributedSubSubSubPublisher1": @"airbridge_sub_id_1",
            @"attributedSubSubSubPublisher2": @"airbridge_sub_id_2",
            @"attributedSubSubSubPublisher3": @"airbridge_sub_id_3",
        };

        pour la touche (NSString* dans keyMap. llKeys) {
            NSString* brazeKey = keyMap[key];
            NSString* valeur = attribution[key];

            [Appboy. haredInstance.user setCustomAttributeWithKey:brazeKey andStringValue:value];
        }

        [Appboy. HaredInstance flushDataAndProcessRequestQueue] ;
    };

    [AirBridge getInstance:"VOTRE_APP_TOKEN" appName:"VOTRE_APP_NAME" withLaunchOptions:launchOptions];

    return YES;
}

@end
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Types de données intégrables

Airbridge peut envoyer sept types de données à Braze comme indiqué ci-dessous. Ces données sont utilisées pour l'installation de l'utilisateur Attribution et Attribution personnalisée. Ceci peut être consulté dans le tableau de bord Airbridge et est utilisé pour le filtrage.

En plus des quatre types de données de base (Source, Campagne, Groupe Ad et Ad) fournis par Braze, Airbridge propose trois types de données supplémentaires tels que `airbridge_ad_content`, `airbridge_sub_id`, et `airbridge_term` en tant qu'attribut personnalisé. Parmi ceux-ci, `airbirdge_search_keyword` livre un mot-clé à la valeur quand il provient de publicités de recherche.

{% alert important %}
Les points de données de Braze seront utilisés lorsque vous envoyez des données marquées comme facultatives car elles sont transmises comme un Attribut Utilisateur Personnalisé.
{% endalert %}

| Champ de données Airbridge                | Filtre de segment de Braze                   | Type de texte                       |
| ----------------------------------------- | -------------------------------------------- | ----------------------------------- |
| `attributedChannel`                       | Installer la source d'attribution            | Installer les données d'attribution |
| `Campagne attribuée`                      | Installer la campagne d'attribution          | Installer les données d'attribution |
| `groupe d'admins attribués`               | Installer le groupe d'annonces d'attribution | Installer les données d'attribution |
| `AdCreative attribuée`                    | Installer la pub d'attribution               | Installer les données d'attribution |
| `attributedContent` (facultatif)          | `Contenu de airbridge`                       | Attribut utilisateur personnalisé   |
| `attributedTerm` (facultatif)             | `terme "airbridge"`                          | Attribut utilisateur personnalisé   |
| `attributedSubPublisher` (facultatif)     | `airbridge_sub_id`                           | Attribut utilisateur personnalisé   |
| `attributedSubSubPublisher1` (facultatif) | `airbridge_sub_id_1`                         | Attribut utilisateur personnalisé   |
| `attributedSubSubPublisher2` (facultatif) | `airbridge_sub_id_2`                         | Attribut utilisateur personnalisé   |
| `attributedSubSubPublisher3` (facultatif) | `airbridge_sub_id_3`                         | Attribut utilisateur personnalisé   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## URL de suivi des clics Airbridge dans Braze (facultatif)

Utiliser les liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes conduisent des applications installées et de vous ré-engager. Résultat: vous serez en mesure de mesurer vos efforts de marketing plus efficacement et de prendre des décisions axées sur les données sur l'endroit où investir plus de ressources pour obtenir le meilleur retour sur investissement.

Pour commencer avec Airbridge, cliquez sur les liens de suivi, visitez la documentation trouvée [ici](https://help.airbridge.io/hc/en-us/articles/900001037886-Tracking-Link-Generation/). Une fois configuré, vous pouvez insérer les liens de suivi des clics Airbridge dans vos campagnes Braze directement. Airbridge utilisera alors ses [méthodologies d'attribution probabilistes](https://help.airbridge.io/hc/en-us/articles/900003300526-Airbridge-Identity-Matching-Logic) pour attribuer l'utilisateur qui a cliqué sur le lien. Pour améliorer la précision des attributions de vos campagnes Braze, nous vous recommandons d'ajouter vos liens de suivi Airbridge à l'aide d'un identifiant d'appareil. Ceci attribuera de façon déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs %}
{% tab Android %}
Pour Android, Braze permet aux clients d'opter pour la collecte [Google Advertising ID (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté nativement grâce à l’intégration de Airbridge SDK. Vous pouvez inclure le GAID dans vos liens de suivi des clics Airbridge en utilisant la logique Liquid ci-dessous :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Airbridge collectent automatiquement l'IDFV nativement à travers nos intégrations SDK. Ceci peut être utilisé comme identifiant de périphérique. Vous pouvez inclure l'IDFV dans vos liens de suivi des clics Airbridge en utilisant la logique Liquid ci-dessous :

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

__Cette recommandation est purement optionnelle__<br> Si vous n'utilisez actuellement aucun identificateur d'appareil - comme l'IDFV ou le GAID - dans vos liens de suivi de clics ou si vous ne prévoyez pas de le faire à l'avenir, Airbridge sera toujours en mesure d'attribuer ces clics grâce à la modélisation probabiliste.
