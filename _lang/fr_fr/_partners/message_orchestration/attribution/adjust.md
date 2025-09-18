---
nav_title: Adjust
article_title: Adjust
alias: /partners/adjust/
description: "Cet article de référence décrit le partenariat entre Braze et Adjust, une société d'attribution mobile et d'analyse qui vous permet d'importer des données d'attribution d'installation non organiques pour segmenter plus intelligemment vos campagnes de cycle de vie."
page_type: partner
search_tag: Partner

---

# Adjust

> [Adjust](https://www.adjust.com/) est une entreprise d'attribution mobile et d'analyse qui combine l'attribution des sources publicitaires avec des analyses avancées pour une vue d'ensemble complète de l'aide à la décision.

_Cette intégration est assurée par Adjust._

## À propos de l'intégration

L'intégration de Braze et Adjust vous permet d'importer des données d'attribution d'installation non organiques pour segmenter plus intelligemment vos campagnes de cycle de vie.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Adjust | Un compte Adjust est nécessaire pour bénéficier de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. En fonction de votre plateforme, des extraits de code peuvent être requis dans votre application. Vous trouverez des informations détaillées sur ces exigences à l'étape 1 du processus d'intégration. |
| SDK Adjust | Outre le SDK Braze requis, vous devez installer le [SDK Adjust](https://dev.adjust.com/en/sdk). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Mapper les ID des appareils

#### Android

Si vous disposez d'une application Android, vous devez transmettre un ID unique de l'appareil Braze à Adjust.  

```
Adjust.addGlobalPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getDeviceId()););
```

#### iOS

<!--
{% alert important %}
Prior to February 2023, our Adjust attribution integration used the IDFV as the primary identifier to match iOS attribution data. Braze customers don't need to use Objective-C to fetch the Braze `device_id` and send it to Adjust upon installation as there will be no service disruption. 
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration. 

If set to `true`, you must implement the iOS device ID mapping for Swift to pass the Braze `device_id` to Adjust upon app installation in order for Braze to match iOS attributions appropriately.
--->

{% tabs local %}
{% tab Objective-C %}

Si vous avez une application iOS, votre IDFV sera collecté par Adjust et envoyé à Braze. Cet ID sera ensuite mappé à un ID d'appareil unique dans Braze.

Braze conservera les valeurs IDFA pour les utilisateurs qui ont opté pour l'abonnement si vous collectez l'IDFA avec Braze, comme décrit dans notre [Guide de mise à jour iOS]({{site.baseurl}}/developer_guide/platforms/swift/ios_18/). Sinon, l'IDFV sera utilisé comme identifiant de secours pour mapper les utilisateurs.

{% endtab %}
{% tab Swift %}

Si vous utilisez une application iOS, vous pouvez choisir de collecter l'IDFV en définissant le champ `useUUIDAsDeviceId` sur `false`. Si elle n'est pas définie, l'attribution iOS ne sera probablement pas mappée avec précision d'Adjust à Braze. Pour plus d'informations, consultez la section [Collecter l'IDFV]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift).

{% endtab %}
{% endtabs %}

{% alert note %}
Si vous prévoyez d'envoyer des événements post-installation d'Adjust vers Braze, vous devez : <br><br>1) Vous assurer d'ajouter `external_id` en tant que paramètre de session et d'événement dans le SDK Adjust. Pour le transfert d'événements de chiffre d'affaires, vous devrez également configurer `product_id` comme paramètre pour les événements. Visitez [la documentation d'Adjust](https://github.com/adjust/sdks) pour plus d'informations sur la définition des paramètres des partenaires pour le transfert d'événements.<br><br>2) Générer une nouvelle clé API à entrer dans Adjust. Cela peut être fait en sélectionnant le bouton **Générer une clé API** qui figure dans la page partenaire Adjust dans le tableau de bord de Braze.
{% endalert %}

### Étape 2 : Obtenez la clé d'importation des données Braze

Dans Braze, accédez à **Intégrations** > **Partenaires technologiques** et sélectionnez **Adjust**. 

Ici, vous trouverez l’endpoint REST et générerez votre clé d'importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation des données et l'endpoint REST sont utilisés dans l'étape suivante lors de la configuration d'un postback dans le tableau de bord d'Adjust.<br><br>![Cette image montre la boîte "Importation de données pour attribution d'installation" disponible dans la page de la technologie Adjust. 

### Étape 3 : Configurer Braze dans Adjust

1. Dans le tableau de bord d'Adjust, accédez à **Paramètres de l'application** et accédez à **Configuration des partenaires**, puis **Ajouter des partenaires**.
2. Sélectionnez **Braze (anciennement Appboy)** et fournissez la clé d'importation des données et l'endpoint REST de Braze.
3. Cliquez sur **enregistrer et fermer**.

### Étape 4 : Confirmez l'intégration

Une fois que Braze reçoit les données d'attribution d’Adjust, l'indicateur d’état de connexion de la page des partenaires technologiques d’Adjust dans Braze passera de "Non connecté" à "Connecté". Un horodatage de la dernière requête réussie sera également inclus. 

Notez que cela ne se produira pas tant que nous n'aurons pas reçu les données relatives à une installation attribuée. Les installations organiques, qui doivent être exclues du système de communication automatisé d’Adjust, sont ignorées par notre API et ne sont pas comptabilisées pour déterminer si une connexion a été établie avec succès.

## Champs de données disponibles

En supposant que vous configurez votre intégration comme suggéré, Braze mappera les données d'Adjust aux filtres de segment comme décrit dans le tableau suivant.

| Champ de données Adjust | Filtre de segments Braze |
| --- | --- |
| `{network_name}` | Source attribuée |
| `{campaign_name}` | Campagne attribuée |
| `{adgroup_name}` | Groupe d'annonces attribué |
| `{creative_name}` | Annonce attribuée |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Données d'attribution sur Facebook et X (anciennement Twitter)

Les données d'attribution pour les campagnes Facebook et X (anciennement Twitter) ne sont pas disponibles auprès de nos partenaires. Ces sources médiatiques n'autorisent pas leurs partenaires à partager les données d'attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.

## URL de suivi des clics Adjust dans Braze (facultatif)

L'utilisation de liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes génèrent des installations d'applications et un réengagement. Ainsi, vous serez en mesure de mesurer vos efforts marketing de manière plus efficace et de prendre des décisions fondées sur des données pour investir davantage de ressources pour un retour sur investissement maximal.

Pour commencer avec les liens de suivi de clics Adjust, visitez leur [documentation](https://help.adjust.com/tracking/attribution/tracker-urls). Vous pouvez insérer les liens de suivi des clics Adjust directement dans vos campagnes Braze. Adjust utilisera ensuite ses [méthodologies d'attribution probabiliste](https://www.adjust.com/blog/attribution-compatible-with-ios14/) pour attribuer l'utilisateur qui a cliqué sur le lien. Nous recommandons d'ajouter vos liens de suivi Adjust avec un identifiant d'appareil pour améliorer la précision des attributions de vos campagnes Braze. Cela attribuera de manière déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs local %}
{% tab Android %}
Pour Android, Braze permet aux clients de s'abonner à la [collecte d'identifiants publicitaires de Google (GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id)). Le GAID est également collecté nativement via l'intégration SDK Adjust. Vous pouvez inclure le GAID dans vos liens de suivi de clics Adjust en utilisant la logique Liquid suivante :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Adjust collectent automatiquement l'IDFV de manière native via nos intégrations SDK. Cela peut être utilisé comme identifiant de l'appareil. Vous pouvez inclure l'IDFV dans vos liens de suivi de clics Adjust en utilisant la logique Liquid suivante :

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
Si vous n'utilisez pas actuellement d'identifiants d'appareil (tels que l'IDFV ou le GAID) dans vos liens de suivi des clics, ou si vous n'envisagez pas de le faire à l'avenir, Adjust sera toujours en mesure d'attribuer ces clics par le biais de sa modélisation probabiliste.
{% endalert %}


