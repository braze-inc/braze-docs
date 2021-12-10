---
nav_title: Kochava
article_title: Kochava
alias: /fr/partners/kochava/
description: "Cet article décrit le partenariat entre Braze et Kochava, qui offre l'attribution mobile et l'analyse pour vous aider à exploiter vos données pour la croissance."
page_type: partenaire
search_tag: Partenaire
---

# Kochava

> Kochava propose une attribution et une analyse mobiles pour vous aider à exploiter vos données pour la croissance. La plateforme publique Kochava vous permet de planifier, de cibler, d'activer, de mesurer et d'optimiser vos campagnes d'applications.

Kochava et Braze pouvoir une compréhension plus holistique des campagnes. Kochava envoie des données d'attribution à Braze pour mieux comprendre quelles campagnes conduisent les installations, l'activité dans l'application, et plus encore.

## Intégration

### Étape 1 : Exigences d'intégration

* Cette intégration prend en charge les applications iOS et Android.
* Votre application aura besoin du SDK de Braze et du SDK de Kochava installés.

### Étape 2 : Obtenir la clé d'importation de données Braze

Dans votre compte Braze, accédez à "Attribution" sous "Partenaires technologiques" et sélectionnez "Kochava". Ici, vous trouverez le point de terminaison REST et générez votre clé d'importation de données de Braze. Une fois généré, vous serez en mesure de créer une nouvelle clé ou d'invalider une clé existante si nécessaire. La clé d'importation de données et le point d'extrémité REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord de Kochava.<br><br>!\[Image Kochava\]\[4\]{: style="max-width:70%;"}

### Étape 3 : Mettre en place un postback depuis Kochava

Suivez [ces instructions][18] pour ajouter un postback dans le tableau de bord de Kochava. On vous demandera la clé et le point de terminaison REST que vous avez trouvé dans le tableau de bord de Braze à l'étape 2.

### Étape 4 : Confirmation de l'intégration

Une fois que Braze a reçu des données d'attribution de Kochava, l'indicateur de connexion sur "Partenaires technologiques", alors "Attribution" passera en vert et un horodatage de la dernière requête réussie sera inclus. Notez que cela ne se produira pas jusqu'à ce que nous recevions des données sur une installation de __attribuée__. Les installations biologiques sont ignorées par notre API et ne sont pas comptées pour déterminer si une connexion réussie a été établie. <br><br> __Note pour [Android][29] et [Windows][30] Support__:<br> Si vous prévoyez de tirer parti de l'intégration côté serveur entre Braze et Kochava, vous devrez vous assurer que vous utilisez la méthode `IdentityLink` du SDK Kochava pour capturer l'ID de Braze. Le 'Braze ID' peut être récupéré en utilisant la méthode suivante :

{% tabs local %}
{% tab JAVA %}
Le SDK [Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) génère un GUID en tant que Braze ID au démarrage de la session. C'est l'identifiant que nous recommandons d'utiliser pour passer à la méthode Kochava `IdentityLink` car elle permet à Braze de réconcilier les données avec le profil utilisateur correct. Veuillez vous assurer que vous utilisez cette méthode pour passer le « Braze ID » dans l'initialisation du SDK afin de vous assurer qu'il est disponible lorsque Kochava envoie vos données à Braze via l'intégration côté serveur.

```java
Apppboy.getInstance(context).getDeviceId();
```
{% endtab %}
{% tab iOS %}

Si vous avez une application iOS, votre IDFV sera collecté par Kochava et envoyé à Braze. Cet ID sera ensuite mappé à un identifiant unique de périphérique en Brésil.

Braze va toujours stocker les valeurs IDFA pour les utilisateurs qui ont opté si vous collectez l'IDFA avec Braze, comme décrit dans notre [Guide de mise à jour iOS 14]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Sinon, l'IDFV sera utilisé comme identifiant de secours pour cartographier les utilisateurs.

{% endtab %}
{% endtabs %}

## Données d'attribution Facebook, Twitter et Snapchat

Les données d'attribution pour les campagnes Facebook, Twitter et Snapchat ne sont __pas disponibles via nos partenaires__. Ces sources médiatiques ne permettent pas à leurs partenaires de partager des données d'attribution avec des tiers et, par conséquent, nos partenaires __ne peuvent pas envoyer ces données à Braze__.

## URL de suivi des clics Kochava dans Braze (facultatif)

Utiliser les liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes conduisent des applications installées et de vous ré-engager. Résultat: vous serez en mesure de mesurer vos efforts de marketing plus efficacement et de prendre des décisions axées sur les données sur l'endroit où investir plus de ressources pour obtenir le meilleur retour sur investissement.

Pour commencer avec Kochava cliquez sur les liens de suivi, visitez leur [documentation](https://support.kochava.com/reference-information/attribution-overview/). Vous pouvez insérer les liens de suivi des clics Kochava dans vos campagnes Braze directement. Kochava utilisera alors leurs [méthodologies d'attribution probabilistes](https://www.kochava.com/getting-prepared-for-ios-14/) pour attribuer l'utilisateur qui a cliqué sur le lien. Pour améliorer la précision des attributions de vos campagnes Braze, nous vous recommandons d'ajouter vos liens de suivi Kochava à l'aide d'un identifiant d'appareil. Ceci attribuera de façon déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs local %}
{% tab Android %}
Pour Android, Braze permet aux clients d'opter pour la collecte [Google Advertising ID (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté nativement grâce à l'intégration de Kochava SDK. Vous pouvez inclure le GAID dans votre Ajuster cliquez sur les liens de suivi en utilisant la logique Liquid ci-dessous:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Kochava collectent automatiquement l'IDFV nativement à travers nos intégrations SDK. Ceci peut être utilisé comme identifiant de périphérique. Vous pouvez inclure l'IDFV dans vos liens de suivi de clics Kochava en utilisant la logique Liquid ci-dessous:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

__Cette recommandation est purement optionnelle__<br> Si vous n'utilisez actuellement aucun identificateur d'appareil - comme l'IDFV ou le GAID - dans vos liens de suivi de clic, ou ne prévoient pas à l'avenir, Kochava sera toujours en mesure d'attribuer ces clics à travers leur modélisation probabiliste.
[4]: {% image_buster /assets/img/attribution/kochava.png %}

[18]: https://support.kochava.com/campaign-management/create-a-kochava-certified-postback "Kochava Postbacks"
[29]: https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3
[30]: https://support.kochava.com/sdk-integration/windows-and-xbox-one-sdk-integration?scrollto=marker_8
