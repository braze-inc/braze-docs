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

> [Branche](https://docs.branch.io/pages/integrations/braze/), une plateforme mobile de liaison, vous aide à acquérir, engager, et mesurer sur tous les appareils, canaux et plates-formes en fournissant une vue globale de tous les points de contact de l'utilisateur.

L'intégration de Braze et de la branche vous aidera à comprendre exactement quand et où les utilisateurs ont été acquis, ainsi que comment personnaliser leurs voyages grâce à une attribution robuste et un [lien profond]({{site.baseurl}}/partners/channel_extensions/deep_linking/branch_for_deeplinking/).

## Pré-requis

| Exigences                  | Libellé                                                                                                                                                                                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte de succursale       | Un compte de la Direction générale est requis pour profiter de ce partenariat.                                                                                                                                                                 |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plate-forme, des extraits de code peuvent être requis dans votre application. Les détails sur ces exigences se trouvent à l'étape 1 du processus d'intégration. |
| SDK de la branche          | En plus du Braze SDK requis, vous devez installer le [Branch SDK](https://help.branch.io/developers-hub/docs/native-sdks-overview).                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Carte ID du périphérique

#### Android

Si vous avez une application Android, vous devrez passer un ID unique d'appareil Braze à la Branche. This ID can be set in the Branch SDK's `setRequestMetadataKey()` method. Le code snippet suivant doit être inclus avant d'appeler `initSession`. Vous devez également initialiser le Braze SDK avant de définir les métadonnées de la requête dans le SDK de la Branche.

```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).getInstallTrackingId());

...

Branch.initSession(...);
```
#### iOS

Si vous avez une application iOS, votre IDFV sera collecté par Branche et envoyé à Braze. Cet ID sera ensuite mappé à un identifiant unique de périphérique en Brésil.

Braze va toujours stocker les valeurs IDFA pour les utilisateurs qui ont opté si vous collectez l'IDFA avec Braze, comme décrit dans notre [Guide de mise à jour iOS 14]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Sinon, l'IDFV sera utilisé comme identifiant de secours pour cartographier les utilisateurs.

### Étape 2 : Obtenir la clé d'importation de données Braze

Au Brésil, accédez aux **partenaires technologiques** et sélectionnez **succursale**. Ici, vous trouverez le point de terminaison REST et générez votre clé d'importation de données Braze. Une fois généré, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation de données et le point de terminaison REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord de la branche.<br><br>!\[Branch Image\]\[4\]{: style="max-width:90%;"}

### Étape 3 : Configurer les flux de données

1. Dans la succursale, sous la section **Exports** , cliquez sur **Flux de données**.
2. Sur la page **Gestionnaire de flux de données** , cliquez sur l'onglet **Intégrations de données** en haut de la page.
3. Sélectionnez Braze dans la liste des partenaires de données disponibles.
4. Sur la page d'exportation de Braze, fournissez la clé d'importation de données et le point de terminaison REST que vous avez trouvé dans le tableau de bord de Braze et cliquez sur **Activer**.

### Étape 4 : Confirmer l'intégration

Une fois que Braze a reçu des données d'attribution de la succursale, l'indicateur de connexion sur la page des partenaires technologiques de la succursale à Braze passera au vert. Un horodatage de la dernière requête réussie sera également inclus.

Notez que cela ne se produira pas tant que nous ne recevrons pas de données sur une installation attribuée. Installation organique, qui devrait être exclue du postback de la succursale, sont ignorés par notre API et ne sont pas comptés lors de la détermination d'une connexion réussie.

## Données d'attribution Facebook et Twitter

Les données d’attribution pour les campagnes Facebook et Twitter ne sont pas disponibles auprès de nos partenaires. Ces sources médiatiques ne permettent pas à leurs partenaires de partager des données d'attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données au Brésil.

## URL de suivi des clics de la branche dans Braze (facultatif)

Utiliser les liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes conduisent des applications installées et de vous ré-engager. Résultat: vous serez en mesure de mesurer vos efforts de marketing plus efficacement et de prendre des décisions axées sur les données sur l'endroit où investir plus de ressources pour obtenir le meilleur retour sur investissement.

Pour commencer avec la succursale cliquez sur les liens de suivi, visitez leur [documentation](https://help.branch.io/using-branch/docs/ad-links). Vous pouvez insérer directement les liens de suivi des clics de la succursale dans vos campagnes de Braze. La branche utilisera alors leurs [méthodologies d'attribution probabilistes](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings) pour attribuer l'utilisateur qui a cliqué sur le lien. Nous vous recommandons d'ajouter vos liens de suivi de la branche avec un identifiant de périphérique pour améliorer la précision des attributions de vos campagnes Braze. Ceci attribuera de façon déterministe l'utilisateur qui a cliqué sur le lien.

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

{% alert note %}
__Cette recommandation est purement optionnelle__<br> Si vous n'utilisez actuellement aucun identificateur d'appareil - comme l'IDFV ou le GAID - dans vos liens de suivi de clic, ou ne prévoient pas à l'avenir, la branche sera toujours en mesure d'attribuer ces clics à travers leur modélisation probabiliste.
{% endalert %}
[4]: {% image_buster /assets/img/attribution/branch.png %}
