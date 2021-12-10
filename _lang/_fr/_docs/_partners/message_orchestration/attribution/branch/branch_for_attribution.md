---
nav_title: Branche pour Attribution
article_title: Branche pour Attribution
alias: /fr/partners/branch_pour_attribution/
description: "Cet article décrit le partenariat entre Braze et la succursale, une plateforme de liaison mobile qui vous aide à acquérir, engagez et mesurez sur tous les appareils, canaux et plates-formes."
page_type: partenaire
search_tag: Partenaire
---

# Branche pour l'attribution {#branch}

{% include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branche](https://docs.branch.io/pages/integrations/braze/), une plateforme mobile de liaison, vous aide à acquérir, engager, et mesurer sur tous les appareils, canaux et plates-formes en fournissant une vue globale de tous les points de contact de l'utilisateur. Cet article vous guidera à travers la façon d'utiliser la Branche avec Braze pour répondre à vos besoins d'attribution.

Branche et Braze vous aident à comprendre exactement quand et où les utilisateurs ont été acquis, ainsi que comment personnaliser leurs voyages grâce à une attribution robuste et [un lien profond]({{site.baseurl}}/partners/channel_extensions/deep_linking/branch_for_deeplinking/).

## Intégration

### Étape 1 : Exigences d'intégration

* Cette intégration prend en charge iOS et Android.
* Votre application aura besoin du SDK de Braze et du SDK de Branche installés.

{% tabs %}
{% tab Android %}
* Si vous avez une application Android, vous devrez inclure le code snippet ci-dessous, qui transmet un identifiant unique de l'appareil Braze à la branche. Vous devez définir la bonne clé avant d'appeler `initSession`. Vous devez également initialiser le Braze SDK avant de définir les métadonnées de la requête dans le SDK de la Branche.

```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).getInstallTrackingId());

...

Branch.initSession(...);
```
{% endtab %}
{% tab iOS %}

Si vous avez une application iOS, votre IDFV sera collecté par Branche et envoyé à Braze. Cet ID sera ensuite mappé à un identifiant unique de périphérique en Brésil.

Braze va toujours stocker les valeurs IDFA pour les utilisateurs qui ont opté si vous collectez l'IDFA avec Braze, comme décrit dans notre [Guide de mise à jour iOS 14]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Sinon, l'IDFV sera utilisé comme identifiant de secours pour cartographier les utilisateurs.

{% endtab %}
{% endtabs %}

### Étape 2 : Obtenir la clé d'importation de données Braze

Dans votre compte Braze, accédez à "Attribution" sous "Partenaires technologiques" et sélectionnez "Branche". Ici, vous trouverez le point de terminaison REST et générez votre clé d'importation de données de Braze. Une fois généré, vous serez en mesure de créer une nouvelle clé ou d'invalider une clé existante si nécessaire. La clé d'importation de données et le point de terminaison REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord de la branche.<br><br>!\[Branch Image\]\[4\]{: style="max-width:70%;"}

### Étape 3 : Mettre en place un webhook à partir de la branche

Suivez [ces instructions][22] pour ajouter un webhook dans le tableau de bord de la branche. On vous demandera la clé et le point de terminaison REST que vous avez trouvé dans le tableau de bord de Braze à l'étape 2.

### Étape 4 : Confirmation de l'intégration

Une fois que Braze a reçu des données d'attribution de la succursale, l'indicateur de connexion sur "Partenaires technologiques", alors "Attribution" passera en vert et un horodatage de la dernière requête réussie sera inclus. Notez que cela ne se produira pas jusqu'à ce que nous recevions des données sur une installation de __attribuée__. Les installations biologiques sont ignorées par notre API et ne sont pas comptées pour déterminer si une connexion réussie a été établie.

## Données d'attribution Facebook et Twitter

Les données d'attribution pour les campagnes Facebook et Twitter sont __indisponibles via nos partenaires__. Ces sources médiatiques ne permettent pas à leurs partenaires de partager des données d'attribution avec des tiers et, par conséquent, nos partenaires __ne peuvent pas envoyer ces données à Braze__.

## URL de suivi des clics de la branche dans Braze (facultatif)

Utiliser les liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes conduisent des applications installées et de vous ré-engager. Résultat: vous serez en mesure de mesurer vos efforts de marketing plus efficacement et de prendre des décisions axées sur les données sur l'endroit où investir plus de ressources pour obtenir le meilleur retour sur investissement.

Pour commencer avec la succursale cliquez sur les liens de suivi, visitez leur [documentation](https://help.branch.io/using-branch/docs/ad-links). Vous pouvez insérer directement les liens de suivi des clics de la succursale dans vos campagnes de Braze. La branche utilisera alors leurs [méthodologies d'attribution probabilistes](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings) pour attribuer l'utilisateur qui a cliqué sur le lien. Pour améliorer la précision des attributions de vos campagnes Braze, nous vous recommandons d'ajouter vos liens de suivi de la branche à l'aide d'un identifiant d'appareil. Ceci attribuera de façon déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs %}
{% tab Android %}
Pour Android, Braze permet aux clients d'opter pour la collecte [Google Advertising ID (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également recueilli nativement grâce à l'intégration de la succursale SDK. Vous pouvez inclure le GAID dans votre succursale en cliquant sur les liens de suivi en utilisant la logique Liquid ci-dessous :

{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et la branche collectent automatiquement l'IDFV nativement à travers nos intégrations SDK. Ceci peut être utilisé comme identifiant de périphérique. Vous pouvez inclure l'IDFV dans votre succursale cliquer sur les liens de suivi en utilisant la logique Liquid ci-dessous:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
user_data_idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

__Cette recommandation est purement optionnelle__<br> Si vous n'utilisez actuellement aucun identificateur d'appareil - comme l'IDFV ou le GAID - dans vos liens de suivi de clic, ou ne prévoient pas à l'avenir, la branche sera toujours en mesure d'attribuer ces clics à travers leur modélisation probabiliste.
[4]: {% image_buster /assets/img/attribution/branch.png %}

[22]: https://docs.branch.io/pages/exports/ua-webhooks/ "Branch Webhooks"

