---
nav_title: Ajuster
article_title: Ajuster
alias: /fr/partners/ajustement/
description: "Cet article décrit le partenariat entre Braze et Adjust, une société d’attribution et d’analyse mobile qui combine l’attribution de sources publicitaires."
page_type: partenaire
search_tag: Partenaire
---

# Ajuster

> [Ajuster](https://www.adjust.com/) est une entreprise mobile d'attribution et d'analyse qui combine l'attribution de sources publicitaires à des analytiques avancées pour une image complète de l'intelligence commerciale.

Ajustement vous permet d'importer des données d'attribution non organiques d'installation pour les segmenter plus intelligemment dans vos campagnes de cycle de vie.

## Exigences

Cette intégration prend en charge les applications iOS et Android.

| Exigences                     | Libellé                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SDK Braze                     | Assurez-vous d'activer le SDK adapté à vos besoins - soit [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) ou [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/).                                                             |
| Braze API Key & REST Endpoint | Dans votre compte Braze, accédez à des partenaires technologiques et recherchez Adjust. Là, vous pourrez trouver votre point de terminaison de repos et générer une clé d'importation de données. La clé d'importation de données et le point de terminaison REST seront utilisés pour configurer un postback dans le tableau de bord d'Adjust. |
| Ajuster le SDK                | Veuillez consulter la [Ajuster la documentation](https://docs.adjust.com/en/getting-started/#integrate-the-adjust-sdk) pour plus d'informations sur cette exigence.                                                                                                                                                                             |
{: .reset-td-br-1 .reset-td-br-2}

{% tabs %}
{% tab Android %}

Si vous avez une application Android, vous devrez inclure le code snippet ci-dessous, qui passe un ID unique de l'appareil Braze à Adjust. Vous devriez appeler ce qui suit avant d'initialiser le SDK sur `Adjust.onCreate.`:

```
Adjust.addSessionPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getInstallTrackingId()););
```
{% endtab %}
{% tab iOS %}

Si vous avez une application iOS, votre IDFV sera collecté par Ajuster et envoyé à Braze. Cet ID sera ensuite mappé à un identifiant unique de périphérique en Brésil.

Braze va toujours stocker les valeurs IDFA pour les utilisateurs qui ont opté si vous collectez l'IDFA avec Braze, comme décrit dans notre [Guide de mise à jour iOS 14]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_14/#idfa). Sinon, l'IDFV sera utilisé comme identifiant de secours pour cartographier les utilisateurs.

{% endtab %}
{% endtabs %}

{% alert note %}
Si vous prévoyez d'envoyer des événements de post-installation depuis Adjust vers Braze, vous aurez besoin de: <br><br>1) Assurez-vous d'ajouter `external_id` en tant que paramètre session et événement dans le SDK. Pour le transfert d'événements, vous devrez configurer `product_id` comme paramètre pour les événements. Pour plus d'informations sur la définition des paramètres du partenaire pour la réexpédition d'événements, voir la documentation de [Ajuster](https://github.com/adjust/sdks).<br><br>2) Générer une nouvelle clé API pour entrer dans Adjust. Cela peut être fait en sélectionnant le bouton __Générer la clé API__ dans la section Ajuster le partenaire du tableau de bord Braze.<br><br>![Adjust Image]({% image_buster /assets/img/attribution/adjust2.png %}){: style="max-width:70%;"}
{% endalert %}

## Intégration

Pour intégrer Braze avec Adjust, vous devez configurer Braze dans le tableau de bord d'Adjust.

1. Dans le tableau de bord d'Adjust, accédez à __Paramètres de l'application__ et accédez à __Configuration des partenaires__, puis __Ajouter des partenaires__.<br><br>
2. Sélectionnez __Braze (anciennement Appboy)__.<br><br>
3. Copiez la clé d'importation de données Braze dans le champ `Installer la clé d'API` .<br><br>Cette clé d'importation de données est disponible dans le tableau de bord de Braze. Ceci peut être trouvé en naviguant vers __Partenaires Technologiques__ sous __Intégrations__ et en sélectionnant __Ajuster__. Ici, vous pouvez générer une nouvelle clé ou invalider une clé existante. À partir d'ici, l'API dont vous avez besoin se trouve dans la section __Data Import for Install Attribution__ .<br><br>!\[Adjust Image\]\[1\]{: style="max-width:70%;"}<br><br>
4. Copiez votre point de terminaison spécifique Braze REST dans le champ `REST_endpoint`.<br><br>
5. Cliquez sur __Enregistrer & Fermer__.

### Paramètres d'attribution

En supposant que vous configurez votre intégration telle que suggérée ci-dessus, Braze associera les données d'ajustement aux filtres de segment décrits ci-dessous.

| Ajuster le paramètre d'attribution | Filtre de segment de Braze |
| ---------------------------------- | -------------------------- |
| {network_name}                     | Source attribuée           |
| {campaign_name}                    | Campagne attribuée         |
| {adgroup_name}                     | Adgroup Attribué           |
| {creative_name}                    | Annonces attribuées        |
{: .reset-td-br-1 .reset-td-br-2}


{% alert important %}
  En ce moment, Braze ne reçoit que des données d’attribution d’installation non organiques de ces partenaires d’attribution. Cela signifie que les données organiques **n'apparaîtront pas** comme une source attribuée au Brésil.
{% endalert %}

## Données d'attribution Facebook et Twitter

Les données d'attribution pour les campagnes Facebook et Twitter sont __indisponibles via nos partenaires__. Facebook et Twitter ne permettent pas à leurs partenaires de partager leurs données d'attribution avec des tiers et, par conséquent, nos partenaires __ne peuvent pas envoyer ces données à Braze__.

## Ajuster les URL de suivi des clics dans Braze (facultatif)

Utiliser les liens de suivi des clics dans vos campagnes Braze vous permettra de voir facilement quelles campagnes conduisent des applications installées et de vous ré-engager. Résultat: vous serez en mesure de mesurer vos efforts de marketing plus efficacement et de prendre des décisions axées sur les données sur l'endroit où investir plus de ressources pour obtenir le meilleur retour sur investissement.

Pour commencer avec Ajuster cliquez sur les liens de suivi, visitez leur [documentation](https://help.adjust.com/tracking/attribution/tracker-urls). Vous pouvez insérer directement le lien Ajuster cliquez sur les liens de suivi dans vos campagnes Braze. Ajuster utilisera alors leurs [méthodologies d'attribution probabilistes](https://www.adjust.com/blog/attribution-compatible-with-ios14/) pour attribuer l'utilisateur qui a cliqué sur le lien. Pour améliorer la précision des attributions de vos campagnes Braze, nous vous recommandons d'ajouter vos liens de suivi Ajuster avec un identifiant d'appareil. Ceci attribuera de façon déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs %}
{% tab Android %}
Pour Android, Braze permet aux clients d'opter pour la collecte [Google Advertising ID (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté nativement grâce à l’intégration Adjust SDK. Vous pouvez inclure le GAID dans votre Ajuster cliquez sur les liens de suivi en utilisant la logique Liquid ci-dessous:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
gps_adid={{most_recently_used_device.${google_ad_id}}}
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

__Cette recommandation est purement optionnelle__<br> Si vous n'utilisez actuellement aucun identificateur d'appareil - comme l'IDFV ou le GAID - dans vos liens de suivi de clic, ou ne prévoient pas à l'avenir, Ajuster sera toujours en mesure d'attribuer ces clics à travers leur modélisation probabiliste.
[1]: {% image_buster /assets/img/attribution/adjust.png %} [2]: {% image_buster /assets/img/attribution/adjust2.png %}

