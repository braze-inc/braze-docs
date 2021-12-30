---
nav_title: Ajuster
article_title: Ajuster
alias: /fr/partners/ajustement/
description: "Cet article décrit le partenariat entre Braze et Adjust, une société d’attribution et d’analyse mobile qui vous permet d’importer des données d’attribution non organiques d’installation pour segmenter plus intelligemment vos campagnes de cycle de vie."
page_type: partenaire
search_tag: Partenaire
---

# Ajuster

> [Ajuster](https://www.adjust.com/) est une entreprise mobile d'attribution et d'analyse qui combine l'attribution de sources publicitaires à des analytiques avancées pour une image complète de l'intelligence commerciale.

L'intégration de Braze et Ajuster vous permet d'importer des données d'attribution non organiques d'installation pour les segmenter plus intelligemment dans vos campagnes de cycle de vie.

## Pré-requis

| Exigences                  | Libellé                                                                                                                                                                                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ajuster le compte          | Un compte d'ajustement est requis pour profiter de ce partenariat.                                                                                                                                                                             |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plate-forme, des extraits de code peuvent être requis dans votre application. Les détails sur ces exigences se trouvent à l'étape 1 du processus d'intégration. |
| Ajuster le SDK             | En plus du Braze SDK requis, vous devez installer le [Ajuster SDK](https://docs.adjust.com/en/getting-started/#integrate-the-adjust-sdk).                                                                                                      |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Carte ID du périphérique

#### Android

Si vous avez une application Android, vous devrez passer un ID unique d'appareil Braze à Adjust. Cet ID peut être défini dans la méthode d'ajustement du SDK `addSessionPartnerParameter()`. Le code snippet suivant doit être inclus avant d'initialiser le SDK sur `Adjust.onCreate.`

```
Adjust.addSessionPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getInstallTrackingId()););
```

#### iOS

Si vous avez une application iOS, votre IDFV sera collecté par Ajuster et envoyé à Braze. Cet ID sera ensuite mappé à un identifiant unique de périphérique en Brésil.

Braze va toujours stocker les valeurs IDFA pour les utilisateurs qui ont opté si vous collectez l'IDFA avec Braze, comme décrit dans notre [Guide de mise à jour iOS 14]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Sinon, l'IDFV sera utilisé comme identifiant de secours pour cartographier les utilisateurs.

{% alert note %}
Si vous prévoyez d'envoyer des événements de post-installation depuis Adjust vers Braze, vous aurez besoin de: <br><br>1) Assurez-vous d'ajouter `external_id` en tant que paramètre session et événement dans le SDK. Pour le transfert d'événements, vous devrez également configurer `product_id` comme paramètre pour les événements. Visitez la documentation de [Ajuster](https://github.com/adjust/sdks) pour plus d'informations sur la définition des paramètres du partenaire pour le transfert d'événements.<br><br>2) Générer une nouvelle clé API pour entrer dans Adjust. Cela peut être fait en sélectionnant le bouton __Générer la clé API__ dans la page d'ajustement du partenaire dans le tableau de bord de Braze.<br><br>![Adjust Image]({% image_buster /assets/img/attribution/adjust2.png %}){: style="max-width:80%;"}
{% endalert %}

### Étape 2 : Obtenir la clé d'importation de données Braze

Au Brésil, accédez aux **partenaires technologiques** et sélectionnez **Ajuster**. Ici, vous trouverez le point de terminaison REST et générez votre clé d'importation de données Braze. Une fois généré, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation de données et le point de terminaison REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord d'Adjust.<br><br>!\[Ajuster l'Image\]\[1\]{: style="max-width:90%;"}

### Étape 3 : Configurer Braze dans Ajuster

1. Dans le tableau de bord d'Adjust, accédez à __Paramètres de l'application__ et accédez à __Configuration des partenaires__, puis __Ajouter des partenaires__.
2. Sélectionnez __Braze (anciennement Appboy)__ et fournissez la clé d'importation de données et le point de terminaison Braze REST.
3. Cliquez sur __Enregistrer & Fermer__.

### Étape 4 : Confirmer l'intégration

Une fois que Braze aura reçu des données d'attribution de la part d'Adjust, l'indicateur de connexion d'état sur la page Ajuster les partenaires technologiques à Braze passera au vert. Un horodatage de la dernière requête réussie sera également inclus.

Notez que cela ne se produira pas tant que nous ne recevrons pas de données sur une installation attribuée. Installation organique, qui devrait être exclue du retour postback d'ajustement, sont ignorés par notre API et ne sont pas comptés lors de la détermination d'une connexion réussie.

## Champs de données disponibles

En supposant que vous configurez votre intégration telle que suggérée ci-dessus, Braze associera les données d'ajustement aux filtres de segment décrits ci-dessous.

| Ajuster le champ de données | Filtre de segment de braze |
| --------------------------- | -------------------------- |
| `{network_name}`            | Source attribuée           |
| `{campaign_name}`           | Campagne attribuée         |
| `{adgroup_name}`            | Adgroup Attribué           |
| `{creative_name}`           | Annonces attribuées        |
{: .reset-td-br-1 .reset-td-br-2}

## Données d'attribution Facebook et Twitter

Les données d’attribution pour les campagnes Facebook et Twitter ne sont pas disponibles auprès de nos partenaires. Ces sources médiatiques ne permettent pas à leurs partenaires de partager des données d'attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données au Brésil.

## Ajuster les URL de suivi des clics dans Braze (facultatif)

Utiliser les liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes conduisent des applications installées et de vous ré-engager. Résultat: vous serez en mesure de mesurer vos efforts de marketing plus efficacement et de prendre des décisions axées sur les données sur l'endroit où investir plus de ressources pour obtenir le meilleur retour sur investissement.

Pour commencer avec Ajuster cliquez sur les liens de suivi, visitez leur [documentation](https://help.adjust.com/tracking/attribution/tracker-urls). Vous pouvez insérer directement le lien Ajuster cliquez sur les liens de suivi dans vos campagnes Braze. Ajuster utilisera alors leurs [méthodologies d'attribution probabilistes](https://www.adjust.com/blog/attribution-compatible-with-ios14/) pour attribuer l'utilisateur qui a cliqué sur le lien. Nous vous recommandons d'ajouter vos liens de suivi d'ajustement avec un identifiant d'appareil pour améliorer la précision des attributions de vos campagnes Braze. Ceci attribuera de façon déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs %}
{% tab Android %}
Pour Android, Braze permet aux clients d'opter pour la collecte [Google Advertising ID (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté nativement grâce à l’intégration Adjust SDK. Vous pouvez inclure le GAID dans votre Ajuster cliquez sur les liens de suivi en utilisant la logique Liquid ci-dessous:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Ajuster collectent automatiquement l'IDFV nativement à travers nos intégrations SDK. Ceci peut être utilisé comme identifiant de périphérique. Vous pouvez inclure l'IDFV dans votre Ajuster cliquer sur les liens de suivi en utilisant la logique Liquid ci-dessous:

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
__Cette recommandation est purement optionnelle__<br> Si vous n'utilisez actuellement aucun identificateur d'appareil - comme l'IDFV ou le GAID - dans vos liens de suivi de clic, ou ne prévoient pas à l'avenir, Ajuster sera toujours en mesure d'attribuer ces clics à travers leur modélisation probabiliste.
{% endalert %}
[1]: {% image_buster /assets/img/attribution/adjust.png %} [2]: {% image_buster /assets/img/attribution/adjust2.png %}