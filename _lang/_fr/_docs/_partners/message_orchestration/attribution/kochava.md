---
nav_title: Kochava
article_title: Kochava
alias: /fr/partners/kochava/
description: "Cet article décrit le partenariat entre Braze et Kochava, une plateforme d'attribution mobile qui offre des informations d'attribution et d'analyse pour vous aider à exploiter vos données pour la croissance."
page_type: partenaire
search_tag: Partenaire
---

# Kochava

> Kochava propose une attribution et une analyse mobiles pour vous aider à exploiter vos données pour la croissance. La plateforme publique Kochava vous permet de planifier, de cibler, d'activer, de mesurer et d'optimiser vos campagnes d'applications.

L'intégration de Braze et de Kochava contribue à une compréhension plus holistique de vos campagnes en envoyant des données d'attribution à Braze pour mieux comprendre ce que les campagnes conduisent les installations, Activité dans l'application, et plus encore.

## Pré-requis

| Exigences                  | Libellé                                                                                                                                                                                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Kochava             | Un compte Kochava est requis pour profiter de ce partenariat.                                                                                                                                                                                  |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plate-forme, des extraits de code peuvent être requis dans votre application. Les détails sur ces exigences se trouvent à l'étape 1 du processus d'intégration. |
| SDK Kochava                | En plus du Braze SDK requis, vous devez installer le [SDK Kochava](https://support.kochava.com/sdk-integration/).                                                                                                                              |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Mappez les identifiants d'utilisateur

#### Android

Le SDK [Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) génère un GUID en tant que Braze ID au démarrage de la session. C'est l'identifiant que nous recommandons de passer à la méthode Kochava `IdentityLink` car elle permet à Braze de réconcilier les données avec le profil utilisateur correct. L'ID de Braze peut être récupéré en utilisant la méthode suivante :

```java
Apppboy.getInstance(context).getDeviceId();
```
#### iOS

Si vous avez une application iOS, votre IDFV sera collecté par Kochava et envoyé à Braze. Cet ID sera ensuite mappé à un identifiant unique de périphérique en Brésil.

Braze va toujours stocker les valeurs IDFA pour les utilisateurs qui ont opté si vous collectez l'IDFA avec Braze, comme décrit dans notre [Guide de mise à jour iOS 14]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Sinon, l'IDFV sera utilisé comme identifiant de secours pour cartographier les utilisateurs.

### Étape 2 : Obtenir la clé d'importation de données Braze

Au Brésil, accédez aux **partenaires technologiques** et sélectionnez **Kochava**. Ici, vous trouverez le point de terminaison REST et générez votre clé d'importation de données Braze. Une fois généré, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation de données et le point de terminaison REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord de Kochava.<br><br>!\[Image Kochava\]\[4\]{: style="max-width:90%;"}

### Étape 3 : Configurez un retour de Kochava

[Ajouter un postback][18] dans votre tableau de bord Kochava. On vous demandera la clé d'importation de données et le point de terminaison REST que vous avez trouvé dans le tableau de bord de Brase.

### Étape 4 : Confirmer l'intégration

Une fois que Braze a reçu des données d'attribution de Kochava, l'indicateur de connexion sur la page des partenaires technologiques de Kochava à Braze passera au vert. Un horodatage de la dernière requête réussie sera également inclus.

Notez que cela ne se produira pas tant que nous ne recevrons pas de données sur une installation attribuée. Installations organiques, qui devraient être exclues du postback Kochava, sont ignorés par notre API et ne sont pas comptés lors de la détermination d'une connexion réussie.

## Données d'attribution Facebook et Twitter

Les données d’attribution pour les campagnes Facebook et Twitter ne sont pas disponibles auprès de nos partenaires. Ces sources médiatiques ne permettent pas à leurs partenaires de partager des données d'attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données au Brésil.

## URL de suivi des clics Kochava dans Braze (facultatif)

Utiliser les liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes conduisent des applications installées et de vous ré-engager. Résultat: vous serez en mesure de mesurer vos efforts de marketing plus efficacement et de prendre des décisions axées sur les données sur l'endroit où investir plus de ressources pour obtenir le meilleur retour sur investissement.

Pour commencer avec Kochava cliquez sur les liens de suivi, visitez leur [documentation](https://support.kochava.com/reference-information/attribution-overview/). Vous pouvez insérer les liens de suivi des clics Kochava dans vos campagnes Braze directement. Kochava utilisera alors leurs [méthodologies d'attribution probabilistes](https://www.kochava.com/getting-prepared-for-ios-14/) pour attribuer l'utilisateur qui a cliqué sur le lien. Nous vous recommandons d'ajouter vos liens de suivi Kochava avec un identifiant de périphérique pour améliorer la précision des attributions de vos campagnes Braze. Ceci attribuera de façon déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs %}
{% tab Android %}
Pour Android, Braze permet aux clients d'opter pour la collecte [Google Advertising ID (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté nativement grâce à l'intégration de Kochava SDK. Vous pouvez inclure le GAID dans vos liens de suivi de clics Kochava en utilisant la logique Liquid ci-dessous:
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

{% alert note %}
__Cette recommandation est purement optionnelle__<br> Si vous n'utilisez actuellement aucun identificateur d'appareil - comme l'IDFV ou le GAID - dans vos liens de suivi de clic, ou ne prévoient pas à l'avenir, Kochava sera toujours en mesure d'attribuer ces clics à travers leur modélisation probabiliste.
{% endalert %}
[4]: {% image_buster /assets/img/attribution/kochava.png %}


[18]: https://support.kochava.com/campaign-management/create-a-kochava-certified-postback "Kochava Postbacks"