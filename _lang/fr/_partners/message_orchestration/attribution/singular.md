---
nav_title: Singular
article_title: Singular
alias: /partners/singular/
description: "Cet article de référence présente le partenariat entre Braze et Singular, une plateforme d’analyses de marketing unifiée qui vous permet d’importer des données d’attribution d’installations payantes."
page_type: partner
search_tag: Partenaire

---

# Singular

> Singular est une plateforme d’analyses de marketing unifiée qui fournit une attribution, une agrégation de coûts, des analytiques de marketing, un reporting créatif et une automatisation du flux de travail.

L’intégration entre Braze et Singular vous permet d’importer des données d’attribution d’installation payantes pour segmenter intelligemment dans vos campagnes basées sur le cycle de vie client.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Singular | Un compte Singular est requis pour profiter de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plateforme, les extraits de code peuvent être requis dans votre application. Vous trouverez des détails sur ces exigences à l’étape 1 du processus d’intégration. |
| SDK Singular | En plus du SDK Braze requis, vous devez installer le [SDK Singular](https://support.singular.net/hc/en-us/articles/360037640172-Getting-Started-with-the-Singular-SDK-S2S). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Mapper les ID utilisateur

#### Android

Si vous disposez d’une application Android, vous devez inclure l’extrait de code suivant, qui transmet un ID utilisateur Braze unique à Singular.

```java
String appboyDeviceId = Braze.getInstance(context).getDeviceId();
SingularConfig config = new SingularConfig("SDK KEY", "SDK SECRET")
  .withGlobalProperty(“brazeDeviceID”, appboyDeviceId, true);
```
#### iOS

{% alert important %}
Avant février 2023, notre intégration d’attribution Singular utilisait l’IDFV comme identifiant principal pour faire correspondre les données d’attribution iOS. Il n’est pas nécessaire que les clients de Braze utilisant Objective-C récupèrent le `device_id` de Braze et l’envoient à Singular lors de l’installation, car il n’y aura aucune interruption de service. 
{% endalert%}

Pour ceux qui utilisent le SDK Swift v5.7.0+, si vous souhaitez continuer à utiliser IDFV comme identifiant mutuel, vous devez vous assurer que le champ `useUUIDAsDeviceId` est défini sur `false` afin qu’il n’y ait aucune perturbation de l’intégration. 

Si cette option est définie sur `true`, vous devez implémenter le mappage d’ID d’appareil iOS pour Swift afin de transmettre le `device_id` de Braze à Singular lors de l’installation de l’application afin que Braze fasse corresponde correctement les attributions iOS.

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

### Étape 2 : Obtenir la clé d’importation des données Braze

Dans Braze, accédez à **Technology Partners (Partenaires technologiques)** et sélectionnez **Singular**. Ici, vous trouverez l’endpoint REST pour générer votre clé d’importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. 

Vous devrez fournir la clé d’importation des données et l’endpoint REST à votre gestionnaire de compte Singular pour compléter l’intégration.<br><br>![Cette image affiche la zone « Data Import for Install Attribution » (Importation de données pour l’attribution d’installation) située sur la page Technology de Singular. Dans cette zone, vous trouverez la clé d’importation des données et l’endpoint REST.][4]{: style="max-width:90%;"}

### Étape 3 : Confirmer l’intégration

Une fois que Braze aura reçu les données d’attribution de Singular, l’indicateur d’état de la connexion sur la page des partenaires de technologie de Singular dans Braze passera de « Not Connected » (Non connecté) à « Connected » (Connected). Un horodatage de la dernière demande réussie sera également inclus. 

Notez que cela ne se produira pas tant que nous ne recevrons pas de données sur une installation attribuée. Les installations organiques, qui doivent être exclues du postback Singular, sont ignorées par notre API et ne sont pas incluses dans le décompte des connexions réussies.

## Données d’attribution Facebook et Twitter

Les données d’attribution pour les campagnes Facebook et Twitter ne sont pas disponibles par l’intermédiaire de nos partenaires. Ces sources de médias ne permettent pas à leurs partenaires de partager des données d’attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.

## URL de suivi des clics de Singular dans Braze (facultatif)

L’utilisation des liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes stimulent les installations des applications et le réengagement. Par conséquent, vous serez en mesure de mesurer vos efforts marketing plus efficacement et de prendre des décisions axées sur les données pour investir davantage de ressources selon le retour sur investissement (ROI) maximal.

Pour commencer avec les liens Singular de suivi des clics, consultez la documentation disponible [ici](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true). Vous pouvez insérer directement les liens Singular de suivi des clics dans vos campagnes Braze. Singular utilisera ensuite ses [méthodologies d’attribution probabilistes](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true) pour attribuer l’utilisateur qui a cliqué sur le lien. Nous vous recommandons d’ajouter à vos liens de suivi Singular un identifiant d’appareil afin d’améliorer la précision des attributions de vos campagnes Braze. L’utilisateur ayant cliqué sur le lien sera attribué de manière déterministe.

{% tabs local %}
{% tab Android %}
Pour Android, Braze permet aux clients de s’abonner à la [collection d’ID publicitaires Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté de manière native par l’intégration SDK Singular. Vous pouvez inclure le GAID dans les liens Singular de suivi des clics en utilisant la logique Liquid suivante :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Singular collectent automatiquement l’IDFV de manière native via nos intégrations SDK. Cela peut être utilisé comme identifiant d’appareil. Vous pouvez inclure l’IDFV dans les liens Singular de suivi des clics en utilisant la logique Liquid suivante :

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
Si vous n’utilisez actuellement aucun identifiant d’appareil, comme IDFV ou GAID, dans vos liens de suivi de clic, ou si vous ne le prévoyez pas à l’avenir, Singular pourra toujours attribuer ces clics via ses modélisations probabilistes.
{% endalert %}

[4]: {% image_buster /assets/img/attribution/singular.png %}
