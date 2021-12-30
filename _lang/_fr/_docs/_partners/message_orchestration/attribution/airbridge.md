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

L'intégration de Braze et Airbridge vous permet de passer toutes les données d'attribution d'installations organiques et non organiques à Braze pour construire des campagnes de marketing personnalisées et comprendre exactement où les utilisateurs ont été acquis.

## Pré-requis

| Exigences                  | Libellé                                                                                                                                                                                                               |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Airbridge           | Un compte Airbridge est requis pour profiter de ce partenariat.                                                                                                                                                       |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plate-forme, des extraits de code peuvent être requis dans votre application. Vous trouverez ci-dessous des détails sur ces exigences. |
| SDK Airbridge              | En plus du Braze SDK requis, vous devez installer le SDK Airbridge [Android](https://developers.airbridge.io/v1.0-en-us/docs/android-sdk) ou [iOS](https://developers.airbridge.io/v1.0-en-us/docs/ios-sdk).          |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

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

## Champs de données disponibles

Airbridge peut envoyer sept types de données à Braze comme indiqué ci-dessous. Ces données peuvent être vues dans le tableau de bord Airbridge et sont utilisées pour l'attribut d'installation de l'utilisateur, l'attribut personnalisé et le filtrage.

En plus des quatre types de données de base (Source, Campagne, Groupe Ad et Ad) fournis par Braze, Airbridge propose trois types de données supplémentaires tels que `airbridge_content`, `airbridge_sub_id`, et `airbridge_term` en tant qu'attribut personnalisé. Parmi ceux-ci, `airbridge_sub_id` livre un mot clé à la valeur quand il provient de publicités de recherche.

{% alert important %}
Les points de données de Braze seront utilisés lorsque vous envoyez des données marquées comme facultatives car elles sont transmises comme un attribut utilisateur personnalisé.
{% endalert %}

| Champ de données Airbridge                          | Filtre de segment de braze                   | Type de texte                       | Libellé                                                    |
| --------------------------------------------------- | -------------------------------------------- | ----------------------------------- | ---------------------------------------------------------- |
| `attributedChannel`                                 | Installer la source d'attribution            | Installer les données d'attribution | Nom de la chaîne d'annonce payante                         |
| `Campagne attribuée`                                | Installer la campagne d'attribution          | Installer les données d'attribution | Nom de la campagne                                         |
| `groupe d'admins attribués`                         | Installer le groupe d'annonces d'attribution | Installer les données d'attribution | Nom du groupe d'annonce                                    |
| `AdCreative attribuée`                              | Installer la pub d'attribution               | Installer les données d'attribution | Nom de l'adCreative                                        |
| `attributedContent` <br>(facultatif)          | `Contenu de airbridge`                       | Attribut utilisateur personnalisé   | Nom de la copie de l'annonce, du slogan et de la promotion |
| `attributedTerm` <br>(facultatif)             | `terme "airbridge"`                          | Attribut utilisateur personnalisé   | Type de médium                                             |
| `attributedSubPublisher` <br>(facultatif)     | `airbridge_sub_id`                           | Attribut utilisateur personnalisé   | Mot-clé de recherche d'annonce                             |
| `attributedSubSubPublisher1` <br>(facultatif) | `airbridge_sub_id_1`                         | Attribut utilisateur personnalisé   |                                                            |
| `attributedSubSubPublisher2` <br>(facultatif) | `airbridge_sub_id_2`                         | Attribut utilisateur personnalisé   |                                                            |
| `attributedSubSubPublisher3` <br>(facultatif) | `airbridge_sub_id_3`                         | Attribut utilisateur personnalisé   |                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## URL de suivi des clics Airbridge dans Braze (facultatif)

Utiliser les liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes conduisent des applications installées et de vous ré-engager. Résultat: vous serez en mesure de mesurer vos efforts de marketing plus efficacement et de prendre des décisions axées sur les données sur l'endroit où investir plus de ressources pour obtenir le meilleur retour sur investissement.

Pour commencer avec Airbridge, cliquez sur les liens de suivi, visitez la documentation trouvée [ici](https://help.airbridge.io/hc/en-us/articles/900001037886-Tracking-Link-Generation/). Une fois configuré, vous pouvez directement insérer les liens de suivi des clics d'Airbridge dans vos campagnes de Braze. Airbridge utilisera alors ses [méthodologies d'attribution probabilistes](https://help.airbridge.io/hc/en-us/articles/900003300526-Airbridge-Identity-Matching-Logic) pour attribuer l'utilisateur qui a cliqué sur le lien. Nous vous recommandons d'ajouter vos liens de suivi Airbridge à l'aide d'un identifiant de périphérique pour améliorer la précision des attributions de vos campagnes de Braze. Ceci attribuera de façon déterministe l'utilisateur qui a cliqué sur le lien.

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

{% alert note %}
__Cette recommandation est purement optionnelle__<br> Si vous n'utilisez actuellement aucun identificateur d'appareil - comme l'IDFV ou le GAID - dans vos liens de suivi de clic, ou ne prévoient pas à l'avenir, Airbridge sera toujours en mesure d'attribuer ces clics à travers leur modélisation probabiliste.
{% endalert %}
