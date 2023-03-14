---
nav_title: Adjust
article_title: Adjust
alias: /partners/adjust/
description: "Cet article présente le partenariat entre Braze et Adjust, une société d’attribution et d’analytique mobile qui vous permet d’importer des données d’attribution d’installation non organiques pour segmenter plus intelligemment dans vos campagnes basées sur le cycle de vie client."
page_type: partner
search_tag: Partenaire

---

# Adjust

> [Adjust](https://www.adjust.com/) est une société d’attribution et d’analytique mobile qui associe l’attribution à des sources publicitaires avec des analytiques avancées pour une vision complète de l’aide à la décision.

L’intégration Braze et Adjust vous permet d’importer des données d’attribution d’installation non organiques pour segmenter plus intelligemment dans vos campagnes basées sur le cycle de vie client.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Adjust | Un compte Adjust est requis pour profiter de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plateforme, les extraits de code peuvent être requis dans votre application. Vous trouverez des détails sur ces exigences à l’étape 1 du processus d’intégration. |
| SDK Adjust | En plus du SDK Braze requis, vous devez installer le [SDK Adjust](https://docs.adjust.com/en/getting-started/#integrate-the-adjust-sdk). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Mapper les ID d’appareil

#### Android

Si vous disposez d’une application Android, vous devez transmettre un ID d’appareil Braze unique à Adjust. Cet ID peut être défini dans la méthode `addSessionPartnerParameter()` du SDK Adjust. L’extrait de code suivant doit être inclus avant d’initialiser le SDK sur `Adjust.onCreate.`

```
Adjust.addSessionPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getDeviceId()););
```

#### iOS

<!--
{% alert important %}
Prior to February 2023, our Adjust attribution integration used the IDFV as the primary identifier to match iOS attribution data. It is not necessary for Braze customers using Objective-C to fetch the Braze `device_id` and sent to Adjust upon install as there will be no disruption of service. 
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration. 

If set to `true`, you must implement the iOS device ID mapping for Swift in order to pass the Braze `device_id` to Adjust upon app install in order for Braze to appropriately match iOS attributions.
--->

{% tabs local %}
{% tab Objective-C %}

Si vous disposez d’une application iOS, votre IDFV sera collecté par Adjust et envoyé à Braze. Cet ID sera ensuite mappé à un ID d’appareil unique dans Braze.

Braze conservera toujours les valeurs IDFA pour les utilisateurs qui ont choisi de collecter l’IDFA avec Braze, comme décrit dans notre [Guide de mise à niveau vers iOS 14]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Sinon, l’IDFV sera utilisé comme identifiant de secours pour mapper les utilisateurs.

{% endtab %}
{% tab Swift %}

Si vous avez une appli iOS, vous pouvez choisir de collecter l’IDFV en définissant le champ `useUUIDAsDeviceId` sur `false`. S’il n’est pas configuré, l’attribution iOS ne sera probablement pas bien définie entre Adjust et Braze. Pour plus d’informations, consultez [Recueillir les IDFV]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/swift_idfv/).

{% endtab %}
{% endtabs %}

{% alert note %}
Si vous prévoyez d’envoyer des événements post-installation d’Adjust à Braze, vous devrez : <br><br>1) Vous assurer d’ajouter `external_id` comme paramètre de session et d’événement dans le SDK Adjust. Pour le transfert d’un événement Revenue, vous devrez également configurer `product_id` comme paramètre pour les événements. Pour plus d’informations sur la définition des paramètres de partenaire pour le transfert d’événements, reportez-vous à la [documentation d’Adjust](https://github.com/adjust/sdks).<br><br>2) Générer une nouvelle clé d’API à envoyer vers Adjust. Pour ce faire, cliquez sur le bouton **Generate API Key (Générer une clé d’API)** situé sur la page partenaire d’Adjust dans le tableau de bord de Braze.
{% endalert %}

### Étape 2 : Obtenir la clé d’importation des données Braze

Dans Braze, accédez à **Technology Partners (partenaires technologiques)** et sélectionnez **Adjust**. Ici, vous trouverez l’endpoint REST pour générer votre clé d’importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d’importation des données et l’endpoint REST sont utilisés dans l’étape suivante lors de la configuration d’un postback dans le tableau de bord d’Adjust.<br><br>![Cette image affiche la zone « Data Import for Install Attribution » (Importation de données pour l’attribution d’installation) située sur la page Adjust Technology. Dans cette zone, vous trouverez la clé d’importation des données et l’endpoint REST.][1]{: style="max-width:90%;"}

### Étape 3 : Configurer Braze dans Adjust

1. Dans le tableau de bord d’Adjust, accédez à **App Settings (Paramètres App)** puis à **Partner Setup (Configuration d’un partenaire)**, puis à **Add Partners (Ajouter des partenaires)**.
2. Sélectionnez **Braze (anciennement Appboy)** et fournissez la clé d’importation des données et l’endpoint REST de Braze.
3. Cliquez sur **Save & Close (Enregistrer et Fermer)**.

### Étape 4 : Confirmer l’intégration

Lorsque Braze reçoit les données d’attribution d’Adjust, l’indicateur de l’état de connexion sur la page des partenaires de technologie d’Adjust dans Braze passe de « Not connected » (Non connecté) à « Connected » (Connecté). Un timestamp de la dernière demande réussie sera également inclus. 

Notez que cela ne se produira pas tant que nous ne recevrons pas de données sur une installation attribuée. Les installations organiques, qui doivent être exclues du postback d’Adjust, sont ignorées par notre API et ne sont pas comptées lors de la détermination si une connexion réussie a été établie.

## Champs de données disponibles

En supposant que vous configurez votre intégration comme indiqué, Braze mappera toutes les données d’Adjust aux filtres de segment comme décrit dans le tableau suivant.

| Champ de données Adjust | Filtre de segment Braze |
| --- | --- |
| `{network_name}` | Source attribuée |
| `{campaign_name}` | Campagne attribuée |
| `{adgroup_name}` | Groupe d’annonces attribué |
| `{creative_name}` | Annonce attribuée |
{: .reset-td-br-1 .reset-td-br-2}

## Données d’attribution Facebook et Twitter

Les données d’attribution pour les campagnes Facebook et Twitter ne sont pas disponibles par l’intermédiaire de nos partenaires. Ces sources de médias ne permettent pas à leurs partenaires de partager des données d’attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.

## URL de suivi des clics d’Adjust dans Braze (optional)

L’utilisation des liens de suivi de vos campagnes Braze vous permettra de voir facilement quelles campagnes stimulent les installations des applications et le réengagement. Par conséquent, vous serez en mesure de mesurer vos efforts marketing plus efficacement et de prendre des décisions axées sur les données pour investir davantage de ressources selon le retour sur investissement (ROI) maximal.

Pour commencer avec les liens de suivi des clics d’Adjust, consultez la [documentation](https://help.adjust.com/tracking/attribution/tracker-urls). Vous pouvez insérer directement les liens de suivi des clics d’Adjust dans vos campagnes Braze. Adjust utilisera ensuite ses [méthodologies d’attribution probabilistes](https://www.adjust.com/blog/attribution-compatible-with-ios14/) pour attribuer l’utilisateur qui a cliqué sur le lien. Nous vous recommandons d’associer vos liens de suivi d’Adjust à un identifiant d’appareil pour améliorer la précision des attributions de vos campagnes Braze. L’utilisateur ayant cliqué sur le lien sera attribué de manière déterministe.

{% tabs local %}
{% tab Android %}
Pour Android, Braze permet aux clients de s’abonner à la [collection d’ID publicitaires Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté de manière native par l’intégration du SDK Adjust. Vous pouvez inclure le GAID dans vos liens Adjust de suivi de clics en utilisant la logique Liquid suivante :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Adjust collectent automatiquement l’IDFV par l’intermédiaire de nos intégrations SDK. Cela peut être utilisé comme identifiant d’appareil. Vous pouvez inclure l’IDFV dans vos liens Adjust de suivi de clics en utilisant la logique Liquid suivante :

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
Si vous n’utilisez actuellement aucun identifiant d’appareil, comme IDFV ou GAID, dans vos liens de suivi de clic, ou si vous ne le prévoyez pas à l’avenir, Adjust pourra toujours attribuer ces clics via ses modélisations probabilistes.
{% endalert %}

[1]: {% image_buster /assets/img/attribution/adjust.png %}
[2]: {% image_buster /assets/img/attribution/adjust2.png %}
