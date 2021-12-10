---
nav_title: Singulier
article_title: Singulier
alias: /fr/partners/singular/
description: "Cet article décrit le partenariat entre Braze et Singular, une plate-forme d'analyse marketing unifiée."
page_type: partenaire
search_tag: Partenaire
---

# Singulier

> Singular est une plate-forme d'analyse marketing unifiée qui offre des attributions, une agrégation des coûts, des rapports créatifs et une automatisation des flux de travail.

Singular vous permet d'importer des données d'attribution d'installation payantes pour les segmenter plus intelligemment dans vos campagnes de cycle de vie.

## Intégration

### Étape 1 : Exigences d'intégration

* Cette intégration prend en charge les applications iOS et Android.
* Votre application aura besoin du SDK de Braze et du SDK de Singular installé.

{% tabs %}
{% tab Android %}
Si vous avez une application Android, vous devrez inclure le code snippet ci-dessous, qui passe un identifiant utilisateur unique de Braze à Singular. Pour la plupart des configurations, 2 lignes de code doivent être ajoutées dans la méthode `onCreate()` d'une application immédiatement après la méthode `init` ou le démarrage de la session. Le `device_id de Braze` doit être disponible lorsque le premier événement « App Open» est envoyé à Singular.

```java
@Override
protégé void onCreate(Bundle savedInstanceState)
{
    // Autre code
    // Init Singular SDK
   Singular. nit(context config); // context is Application Context
   // Code For Braze
   String appboyDeviceId = Braze. etInstance(context).getInstallTrackingId();
   Singular.event("App Open", "appboyUserID", appboyDeviceId);
}
```
{% endtab %}
{% tab iOS %}

Si vous avez une application iOS, votre IDFV sera collecté par Singular et envoyé à Braze. Cet ID sera ensuite mappé à un identifiant unique de périphérique en Brésil.

Braze va toujours stocker les valeurs IDFA pour les utilisateurs qui ont opté si vous collectez l'IDFA avec Braze, comme décrit dans notre [Guide de mise à jour iOS 14]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Sinon, l'IDFV sera utilisé comme identifiant de secours pour cartographier les utilisateurs.

{% endtab %}
{% endtabs %}

### Étape 2 : Obtenir la clé d'importation de données Braze

Dans votre compte Braze, accédez à "Attribution" sous "Partenaires technologiques" et sélectionnez "Singular". Ici, vous trouverez le point de terminaison REST et générez votre clé d'importation de données de Braze. Une fois généré, vous serez en mesure de créer une nouvelle clé ou d'invalider une clé existante si nécessaire. Vous devrez fournir la clé d'importation de données et votre point de terminaison REST à votre gestionnaire de compte Singular pour que l'intégration soit terminée.<br><br>!\[Image Singulaire\]\[4\]{: style="max-width:70%;"}

### Étape 3: Confirmation de l'intégration

Une fois que Braze a reçu des données d'attribution de Singular, l'indicateur de connexion sur "Partenaires technologiques", alors "Attribution" passera en vert et un horodatage de la dernière requête réussie sera inclus. Notez que cela ne se produira pas jusqu'à ce que nous recevions des données sur une installation de __attribuée__. Installations organiques, qui devraient être exclues du postback Singulaire, sont ignorés par notre API et ne sont pas comptés lors de la détermination d'une connexion réussie.

## Données d'attribution Facebook et Twitter

Les données d'attribution pour les campagnes Facebook et Twitter sont __indisponibles via nos partenaires__. Ces sources médiatiques ne permettent pas à leurs partenaires de partager des données d'attribution avec des tiers et, par conséquent, nos partenaires __ne peuvent pas envoyer ces données à Braze__.

## URL de suivi des clics singuliers dans Braze (facultatif)

Utiliser les liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes conduisent des applications installées et de vous ré-engager. Résultat: vous serez en mesure de mesurer vos efforts de marketing plus efficacement et de prendre des décisions axées sur les données sur l'endroit où investir plus de ressources pour obtenir le meilleur retour sur investissement.

Pour commencer avec les liens de suivi des clics Singulaires, visitez leur [documentation](https://support.singular.net/hc/en-us/articles/360030934212-Singular-Links-FAQ?navigation_side_bar=true). Vous pouvez insérer directement les liens de suivi des clics Singular dans vos campagnes Braze. Singular utilisera alors leurs [méthodologies d'attribution probabilistes](https://support.singular.net/hc/en-us/articles/115000526963-Understanding-Singular-Mobile-App-Attribution?navigation_side_bar=true) pour attribuer l'utilisateur qui a cliqué sur le lien. Pour améliorer la précision des attributions de vos campagnes Braze, nous vous recommandons d'ajouter vos liens de suivi singulier à l'aide d'un identifiant d'appareil. Ceci attribuera de façon déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs %}
{% tab Android %}
Pour Android, Braze permet aux clients d'opter pour la collecte [Google Advertising ID (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté nativement grâce à l'intégration Singular SDK. Vous pouvez inclure le GAID dans votre Ajuster cliquez sur les liens de suivi en utilisant la logique Liquid ci-dessous:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Singular collectent automatiquement l'IDFV nativement à travers nos intégrations SDK. Ceci peut être utilisé comme identifiant de périphérique. Vous pouvez inclure l'IDFV dans vos liens de suivi de clics Singular en utilisant la logique Liquid ci-dessous:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

__Cette recommandation est purement optionnelle__<br> Si vous n'utilisez actuellement aucun identificateur d'appareil - comme l'IDFV ou le GAID - dans vos liens de suivi de clic, ou ne prévoient pas à l'avenir, Singular sera toujours en mesure d'attribuer ces clics à travers leur modélisation probabiliste.
[4]: {% image_buster /assets/img/attribution/singular.png %}


