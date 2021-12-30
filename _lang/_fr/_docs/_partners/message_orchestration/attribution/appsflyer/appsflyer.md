---
nav_title: Flyer des applications
article_title: Flyer des applications
alias: /fr/partners/appsflyer/
description: "Cet article décrit le partenariat entre Braze et AppsFlyer, une plateforme d'analyse et d'attribution de marketing mobile qui vous aide à analyser et optimiser vos applications."
page_type: partenaire
search_tag: Partenaire
---

# Flyer des applications

{% include video.html id="gQ9y2DA2LuQ" align="right" %}

> AppsFlyer est une plateforme d’analyse et d’attribution de marketing mobile qui vous aide à analyser et optimiser vos applications par le biais d’analyses marketing, d’attributions mobiles et de liens profonds.

L'intégration de Braze et AppsFlyer vous permet de mieux comprendre comment optimiser et construire des campagnes plus holistiques en exploitant les données d'attribution d'installation mobile depuis AppsFlyer.

## Pré-requis

| Exigences                  | Libellé                                                                                                                                                                                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte AppsFlyer           | Un compte AppsFlyer est requis pour profiter de ce partenariat.                                                                                                                                                                                |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plate-forme, des extraits de code peuvent être requis dans votre application. Les détails sur ces exigences se trouvent à l'étape 1 du processus d'intégration. |
| SDK AppsFlyer              | En plus du Braze SDK requis, vous devez installer le [SDK AppsFlyer](https://support.appsflyer.com/hc/en-us/categories/201114756-SDK-integration-).                                                                                            |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : ID de périphérique de carte

#### Android

Si vous avez une application Android, vous devrez passer un ID unique d'appareil Braze à AppsFlyer. Le code snippet suivant doit être inclus en même temps que tous les appels vers `AppsFlyerLib.Instance.StartTracking`, généralement dans le callback `onCreate` d'une activité.

```java
HashMap<String, Object> customData = new HashMap<String,Object>();
String deviceId = Braze.getInstance(context).getInstallTrackingId();
customData.put("customData", deviceId);
AppsFlyerLib.setAdditionalData(customData);
```

#### iOS

Si vous avez une application iOS, votre IDFV sera collecté par AppsFlyer et envoyé à Braze. Cet ID sera ensuite mappé à un identifiant unique de périphérique en Brésil.

Braze va toujours stocker les valeurs IDFA pour les utilisateurs qui ont opté si vous collectez l'IDFA avec Braze, comme décrit dans notre [Guide de mise à jour iOS 14]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Sinon, l'IDFV sera utilisé comme identifiant de secours pour cartographier les utilisateurs.

#### Unité

```
CopiedAppboy.AppboyBinding.GetInstallTrackingId()
Dictionnaire<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.GetInstallTrackingId());
AppsFlyer.setAdditionalData(customData);
```

### Étape 2 : Obtenir la clé d'importation de données Braze

Au Brésil, accédez aux **partenaires technologiques** et sélectionnez **AppsFlyer**. Ici, vous trouverez le point de terminaison REST et générez votre clé d'importation de données Braze. Une fois généré, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation de données et le point de terminaison REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord de AppsFlyer.<br><br>!\[Image AppsFlyer\]\[4\]{: style="max-width:70%;"}

### Étape 3 : Configurer Braze dans le tableau de bord de AppsFlyer

1. Dans AppsFlyer, accédez à la page **Partenaires intégrés** sur la barre de gauche. Ensuite, recherchez **Braze** et cliquez sur le logo de Braze pour ouvrir une fenêtre de configuration.
2. Dans l’onglet **Intégration** , activez **Activer le partenaire**.
3. Fournissez la clé d'importation de données et le point de terminaison REST que vous avez trouvé dans le tableau de bord de Brase.
4. Désactivez/désactivez la **Protection Avancée** et enregistrez votre configuration.

Des informations supplémentaires sur ces instructions sont disponibles dans la documentation de [AppsFlyer][16].

### Étape 4 : Confirmer l'intégration

Une fois que Braze a reçu des données d'attribution de AppsFlyer, l'indicateur de connexion sur la page des partenaires de la technologie AppsFlyer à Braze passera au vert. Un horodatage de la dernière requête réussie sera également inclus.

Notez que cela ne se produira pas tant que nous ne recevrons pas de données sur une installation attribuée. Installation organique, qui devrait être exclue du postback AppsFlyer, sont ignorés par notre API et ne sont pas comptés lors de la détermination d'une connexion réussie.

### Étape 5 : Visualisation des données d'attribution de l'utilisateur

#### Champs de données disponibles

En supposant que vous configurez votre intégration telle que suggérée ci-dessus, Braze associera toutes les données d'installation organiques et non organiques aux filtres de segments, comme décrit ci-dessous.

| Champ de données AppsFlyer | Filtre de segment de braze |
| -------------------------- | -------------------------- |
| `source_média`             | Source attribuée           |
| `campagne`                 | Campagne attribuée         |
| `af_adset`                 | Adgroup Attribué           |
| `af_ad`                    | Annonces attribuées        |
{: .reset-td-br-1 .reset-td-br-2}

Votre base d'utilisateurs peut être segmentée par des données d'attribution dans le tableau de bord Braze en utilisant les filtres Installer Attribution.

!\[Attributs de l'utilisateur\]\[2\]

De plus, des données d’attribution pour un utilisateur particulier sont disponibles sur le profil de chaque utilisateur dans le tableau de bord de Braze.

## Données d'attribution Facebook, Snapchat et Twitter

Les données d’attribution pour les campagnes Facebook et Twitter ne sont pas disponibles auprès de nos partenaires. Ces sources médiatiques ne permettent pas à leurs partenaires de partager des données d'attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données au Brésil.

## Envoyer un lien profond par email et cliquer sur Suivi

Des liens profonds, des liens qui dirigent les utilisateurs vers une page spécifique ou un lieu dans une application ou un site Web, sont cruciaux pour créer une expérience utilisateur personnalisée. Bien que largement utilisés, des problèmes apparaissent souvent lors de leur utilisation avec le suivi des clics, une autre fonctionnalité vitale utilisée dans la collecte de données utilisateur. Ces problèmes sont dus aux ESP (Email Service Providers) enveloppant des liens profonds dans leur propre domaine d'enregistrement de clic, cassant le lien original.

Il y a cependant des ESP comme Sendgrid qui supportent à la fois la liaison universelle et le suivi des clics. Braze recommande d'intégrer [les liens d'attribution basés sur OneLink][3] dans votre système de messagerie SendGrid pour un lien de fond et transparent à partir des e-mails.

### URL de suivi des clics de l'AppsFlyer dans Braze (facultatif)

Vous pouvez utiliser les [liens d'attribution OneLink d'AppsFlyer](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) dans les campagnes Braze à travers les push, les e-mails et plus encore. Cela vous permet de renvoyer des données d'attribution d'installation ou de réengagement à partir de leurs campagnes Braze vers AppsFlyer. Résultat: vous serez en mesure de mesurer vos efforts de marketing plus efficacement et de prendre des décisions axées sur les données sur l'endroit où investir plus de ressources pour obtenir le meilleur retour sur investissement.

Vous pouvez simplement créer votre URL de suivi OneLink dans AppsFlyer et l'insérer directement dans vos campagnes Braze. AppsFlyer utilisera ensuite leurs méthodologies d'attribution probabilistes [](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) pour attribuer l'utilisateur qui a cliqué sur le lien. Nous vous recommandons d'ajouter vos liens de suivi AppsFlyer avec un identifiant d'appareil pour améliorer la précision des attributions de vos campagnes Braze. Ceci attribuera de façon déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs %}
{% tab Android %}
Pour Android, Braze permet aux clients d'opter pour la collecte [Google Advertising ID (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté nativement grâce à l'intégration du SDK AppsFlyer. Vous pouvez inclure le GAID dans vos liens de suivi de clics AppsFlyer en utilisant la logique Liquid ci-dessous:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et AppsFlyer récupèrent automatiquement l'IDFV nativement grâce à nos intégrations SDK. Ceci peut être utilisé comme identifiant de périphérique. Vous pouvez inclure l'IDFV dans vos liens de suivi des clics AppsFlyer en utilisant la logique Liquid ci-dessous:

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
**Cette recommandation est purement facultative**<br> Si vous n'utilisez actuellement aucun identifiant de périphérique - comme l'IDFV ou le GAID - dans vos liens de suivi de clic, ou ne prévoient pas à l'avenir, AppsFlyer sera toujours en mesure d'attribuer ces clics à travers leur modèle probabiliste.
{% endalert %}
[1]: {% image_buster /assets/img/braze_integration.png %} [2]: {% image_buster /assets/img/braze_attribution.png %} [4]: {% image_buster /assets/img/attribution/appsflyer.png %}

[3]: https://support.appsflyer.com/hc/en-us/articles/360001294118
[16]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration "AppsFlyer Push API"