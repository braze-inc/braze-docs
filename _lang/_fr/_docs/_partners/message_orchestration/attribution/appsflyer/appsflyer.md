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

Construisez des campagnes de marketing plus holistiques en exploitant les données d’attribution d’installation mobile à partir d’AppsFlyer. Avec AppsFlyer et Braze, vous pouvez passer des données d'attribution d'installation à Braze pour mieux comprendre comment optimiser vos campagnes.

## Intégration

### Étape 1 : Exigences d'intégration

{% alert important %}
AppsFlyer exige que le bouton Activer le partenaire soit activé "allumé" pour chaque partenaire intégré, y compris Braze. Vérifiez que votre interrupteur est activé depuis votre tableau de bord AppsFlyer.
{% endalert %}

* Cette intégration prend en charge les applications iOS et Android.
* Votre application aura besoin du SDK de Braze et du SDK d'AppsFlyer installé.

{% tabs local %}
{% tab Android %}

Si vous avez une application Android, vous devrez inclure le code snippet ci-dessous, qui transmet un id unique de l'appareil Braze à AppsFlyer. Pour la plupart des configurations, ce code devrait être inclus avec tous les appels à `AppsFlyerLib.Instance.StartTracking`, généralement dans le callback `onCreate` d'une activité.

```java
HashMap<String, Object> customData = new HashMap<String,Object>();
String deviceId = Braze.getInstance(context).getInstallTrackingId();
customData.put("customData", deviceId);
AppsFlyerLib.setAdditionalData(customData);
```
{% endtab %}
{% tab iOS %}

Si vous avez une application iOS, votre IDFV sera collecté par AppsFlyer et envoyé à Braze. Cet ID sera ensuite mappé à un identifiant unique de périphérique en Brésil.

Braze va toujours stocker les valeurs IDFA pour les utilisateurs qui ont opté si vous collectez l'IDFA avec Braze, comme décrit dans notre [Guide de mise à jour iOS 14]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Sinon, l'IDFV sera utilisé comme identifiant de secours pour cartographier les utilisateurs.

{% endtab %}
{% tab Unity %}

```
CopiedAppboy.AppboyBinding.GetInstallTrackingId()
Dictionnaire<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.GetInstallTrackingId());
AppsFlyer.setAdditionalData(customData);
```

{% endtab %}
{% endtabs %}

### Étape 2 : Obtenir la clé d'importation de données Braze

Dans votre compte Braze, accédez à __Attribution__ sous __Partenaires Technologiques__ et sélectionnez __AppsFlyer__. Ici, vous trouverez le point de terminaison REST et générez votre clé d'importation de données de Braze. Une fois généré, vous serez en mesure de créer une nouvelle clé ou d'invalider une clé existante. La clé d'importation de données et le point de terminaison REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord de AppsFlyer.<br><br>!\[Image AppsFlyer\]\[4\]{: style="max-width:70%;"}

### Étape 3 : Configurer Braze dans le tableau de bord de AppsFlyer

Dans le tableau de bord d'AppsFlyer, accédez à la page __Partenaires intégrés__ sur la barre de gauche. De là, recherchez __Braze__ et cliquez sur le logo de Braze pour ouvrir une fenêtre de configuration. !\[AppsFlyer\]\[1\]{: style="float:right;max-width:30%;margin-left:15px;margin-bottom:15px;margin-top:15px"}

Dans l’onglet __Intégration__ , activez __Activer le partenaire__, copier la clé d'import de données dans le champ `API_key` ajoutez votre URL Braze REST Endpoint dans le champ `REST Endpoint`. Il y aura également une option pour activer/désactiver la confidentialité avancée, assurez-vous que cette bascule est désactivée. Enfin, enregistrez votre configuration.

Des informations supplémentaires sur ces instructions sont disponibles dans la documentation de [AppsFlyer][16].

Une fois que vous avez enregistré la configuration, AppsFlyer envoie les données suivantes à Braze pour chaque installation organique et non organique. Ci-dessous, vous pouvez voir comment Braze fait correspondre les champs de données d'AppsFlyer à des filtres de segment spécifiques.

| Champ de données AppsFlyer | Filtre de segment de Braze |
| -------------------------- | -------------------------- |
| `source_média`             | Source attribuée           |
| `campagne`                 | Campagne attribuée         |
| `af_adset`                 | Adgroup Attribué           |
| `af_ad`                    | Annonces attribuées        |
{: .reset-td-br-1 .reset-td-br-2}

### Étape 4 : Confirmation de l'intégration

Une fois que Braze a reçu des données d'attribution de AppsFlyer, l'indicateur de connexion sur __Partenaires de Technologie__, alors __Attribution__ passera en vert et un horodatage de la dernière requête réussie sera inclus. Notez que cela ne se produira pas jusqu'à ce que nous recevions des données sur une installation de __attribuée__. Installations organiques, qui devraient être exclues par l'intégration d'AppsFlyer, sont ignorés par notre API et ne sont pas comptés lors de la détermination d'une connexion réussie.

### Étape 5 : Visualisation des données d'attribution de l'utilisateur

Votre base d'utilisateurs peut être segmentée par des données d'attribution dans le tableau de bord Braze en utilisant les filtres Installer Attribution.

!\[Attributs de l'utilisateur 1\]\[2\]{: style="max-width:80%;margin-right:15px;"}

De plus, des données d’attribution pour un utilisateur particulier sont disponibles sur le profil de chaque utilisateur dans le tableau de bord de Braze.

## Données d'attribution Facebook, Snapchat et Twitter

Les données d’attribution pour les campagnes Facebook, Snapchat et Twitter ne sont pas disponibles auprès de nos partenaires. Ces sources médiatiques ne permettent pas à leurs partenaires de partager des données d'attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données au Brésil.

Pour plus d'informations, veuillez consulter la documentation [d'AppsFlyer][31].

## Envoyer un lien profond par email et cliquer sur Suivi

Des liens profonds, des liens qui dirigent les utilisateurs vers une page spécifique ou un lieu dans une application ou un site Web, sont cruciaux pour créer une expérience utilisateur personnalisée. Bien que largement utilisés, des problèmes apparaissent souvent lors de leur utilisation en tandem avec le suivi des clics, une autre fonctionnalité vitale utilisée dans la collecte des données utilisateur. Ces problèmes sont dus aux ESP (Email Service Providers) enveloppant des liens profonds dans leur propre domaine d'enregistrement de clic, cassant le lien original.

Il y a cependant des ESP comme Sendgrid qui supportent à la fois la liaison universelle et le suivi des clics. Braze recommande l'intégration de liens d'attribution basés sur OneLink dans votre système de messagerie SendGrid afin de créer un lien transparent et profond à partir des e-mails. Pour commencer, consultez la documentation [d'AppsFlyer][3].

### URL de suivi des clics dans Braze (facultatif)

Vous pouvez utiliser les [liens d'attribution OneLink d'AppsFlyer](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) dans les campagnes Braze à travers les push, les e-mails et plus encore. Cela vous permet de renvoyer des données d'attribution d'installation ou de réengagement à partir de leurs campagnes Braze vers AppsFlyer. En conséquence, vous serez en mesure de voir de manière holistique l'impact de vos chaînes payantes et détenues sur une seule plateforme.

Vous pouvez simplement créer votre URL de suivi OneLink dans AppsFlyer et l'insérer directement dans vos campagnes Braze. AppsFlyer utilisera ensuite leurs méthodologies d'attribution probabilistes [](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) pour attribuer l'utilisateur qui a cliqué sur le lien ou le lien profond. Pour améliorer la précision des attributions de vos campagnes Braze, nous vous recommandons d'ajouter vos liens de suivi AppsFlyer à l'aide d'un identifiant d'appareil. Ceci attribuera de façon déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs %}
{% tab Android %}
Pour Android, Braze permet aux clients d'opter pour la collecte [Google Advertising ID (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté nativement grâce à l'intégration du SDK AppsFlyer. Vous pouvez inclure le GAID dans vos liens de suivi de clics AppsFlyer en utilisant la logique Liquid ci-dessous:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
advertising_id={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et AppsFlyer récupèrent automatiquement l'IDFV nativement grâce à nos intégrations SDK. Ceci peut être utilisé comme identifiant de périphérique. Vous pouvez inclure l'IDFV dans vos liens de suivi des clics AppsFlyer en utilisant la logique Liquid ci-dessous:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
device_id={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

__Cette recommandation est purement optionnelle__<br> Si vous n'utilisez actuellement aucun identificateur d'appareil - comme l'IDFV ou le GAID - dans vos liens de suivi de clic, ou ne prévoient pas à l'avenir, AppsFlyer sera toujours en mesure d'attribuer ces clics à travers leur modèle probabiliste.
[1]: {% image_buster /assets/img/braze_integration.png %} [2]: {% image_buster /assets/img/braze_attribution.png %} [4]: {% image_buster /assets/img/attribution/appsflyer.png %}

[3]: https://support.appsflyer.com/hc/en-us/articles/360001294118
[16]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration "AppsFlyer Push API"
[31]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Braze-Formerly-Appboy-Integration

