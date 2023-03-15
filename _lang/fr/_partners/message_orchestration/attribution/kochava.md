---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "Cet article présente le partenariat entre Braze et Kochava, une plateforme d’attribution mobile qui offre des informations d’attribution et d’analytique pour vous aider à exploiter vos données pour la croissance de votre activité."
page_type: partner
search_tag: Partenaire

---

# Kochava

> Kochava propose une attribution et une analytique mobiles pour vous aider à exploiter vos données pour la croissance de votre activité. La plateforme Kochava Audience vous permet de planifier, cibler, activer, mesurer et optimiser vos campagnes d’applications.

L’intégration de Braze et de Kochava aide à mieux comprendre vos campagnes en envoyant des données d’attribution à Braze afin de mieux comprendre les campagnes qui augmentent les installations, l’activité in-app, etc.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Kochava | Un compte Kochava est requis pour profiter de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. Selon votre plateforme, les extraits de code peuvent être requis dans votre application. Vous trouverez des détails sur ces exigences à l’étape 1 du processus d’intégration. |
| SDK Kochava | En plus du SDK Braze requis, vous devez installer le [SDK Kochava](https://support.kochava.com/sdk-integration/). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Mapper les ID utilisateur

#### Android

Le SDK [Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) génère un GUID en tant qu’ID Braze lors du démarrage de session. Il s’agit de l’identifiant que nous recommandons de transmettre la méthode `IdentityLink` de Kochava permettant à Braze de rapprocher les données au bon profil utilisateur. L’ID Braze peut être récupéré en utilisant la méthode suivante :

```java
Apppboy.getInstance(context).getDeviceId();
```

#### iOS

{% alert important %}
Avant février 2023, notre intégration d’attribution Kochava utilisait l’IDFV comme identifiant principal pour faire correspondre les données d’attribution iOS. Il n’est pas nécessaire que les clients de Braze utilisant Objective-C récupèrent le `device_id` de Braze et l’envoient à Kochava lors de l’installation, car il n’y aura aucune interruption de service. 
{% endalert%}

Pour ceux qui utilisent le SDK Swift v5.7.0+, si vous souhaitez continuer à utiliser IDFV comme identifiant mutuel, vous devez vous assurer que le champ `useUUIDAsDeviceId` est défini sur `false` afin qu’il n’y ait aucune perturbation de l’intégration. Si cette option est définie sur `true`, vous devez implémenter le mappage d’ID d’appareil iOS pour Swift afin de transmettre le `device_id` de Braze à Kochava lors de l’installation de l’application afin que Braze fasse corresponde correctement les attributions iOS.

Braze dispose de deux API qui produiront la même valeur, l’une avec un gestionnaire d’achèvement et l’autre utilisant la nouvelle prise en charge de simultanéité Swift. Notez que vous devrez modifier les extraits de code suivants pour vous conformer aux instructions du [SDK iOS](https://support.kochava.com/sdk-integration/ios-sdk-integration/) de Kochava. Pour obtenir de l’aide supplémentaire, contactez l’assistance Kochava.

##### Gestionnaire d’achèvement
```
AppDelegate.braze?.deviceId(completion: { deviceId in
  // Use `deviceId`
})
```
##### Simultanéité Swift
```
let deviceId = await AppDelegate.braze?.deviceId()
```

### Étape 2 : Obtenir la clé d’importation des données Braze

Dans Braze, accédez à **Technology Partners (partenaires technologiques)** et sélectionnez **Kochava**. Ici, vous trouverez l’endpoint REST pour générer votre clé d’importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d’importation des données et l’endpoint REST sont utilisés dans l’étape suivante pour configurer un postback dans le tableau de bord de Kochava.<br><br>![Cette image affiche la zone « Data Import for Install Attribution » (Importation de données pour l’attribution d’installation) située sur la page Kochava Technology. Dans cette zone, vous trouverez la clé d’importation des données et l’endpoint REST.][4]{: style="max-width:90%;"}

### Étape 3 : Configurer un postback depuis Kochava

[Ajoutez un postback][18] dans votre tableau de bord Kochava. Une invite vous demandera de fournir la clé d’importation des données et l’endpoint REST que vous avez trouvés dans le tableau de bord de Braze.

### Étape 4 : Confirmer l’intégration

Lorsque Braze reçoit les données d’attribution de Kochava, l’indicateur de l’état de connexion sur la page des partenaires de technologie de Kochava dans Braze passe de « Not Connected » (Non connecté) à « Connected » (Connecté). Un timestamp de la dernière demande réussie sera également inclus. 

Notez que cela ne se produira pas tant que nous ne recevrons pas de données sur une installation attribuée. Les installations organiques, qui doivent être exclues du postback de Kochava, sont ignorées par notre API et ne sont pas comptées lors de la détermination si une connexion réussie a été établie.

## Données d’attribution Facebook et Twitter

Les données d’attribution pour les campagnes Facebook et Twitter ne sont pas disponibles par l’intermédiaire de nos partenaires. Ces sources de médias ne permettent pas à leurs partenaires de partager des données d’attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.

## URL de suivi des clics de Kochava dans Braze (optional)

L’utilisation des liens de suivi de vos campagnes Braze vous permettra de voir facilement quelles campagnes stimulent les installations des applications et le réengagement. Par conséquent, vous serez en mesure de mesurer vos efforts marketing plus efficacement et de prendre des décisions axées sur les données pour investir davantage de ressources selon le retour sur investissement (ROI) maximal.

Pour commencer avec les liens de suivi des clics de Kochava, consultez la [documentation](https://support.kochava.com/reference-information/attribution-overview/). Vous pouvez insérer directement les liens de suivi des clics de Kochava dans vos campagnes Braze. Kochava utilisera ensuite ses [méthodologies d’attribution probabilistes](https://www.kochava.com/getting-prepared-for-ios-14/) pour attribuer l’utilisateur qui a cliqué sur le lien. Nous vous recommandons d’associer vos liens de suivi de Kochava à un identifiant d’appareil pour améliorer la précision des attributions de vos campagnes Braze. L’utilisateur ayant cliqué sur le lien sera attribué de manière déterministe.

{% tabs local %}
{% tab Android %}
Pour Android, Braze permet aux clients de s’abonner à la [collection d’ID publicitaires Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté de manière native par l’intégration SDK Kochava. Vous pouvez inclure le GAID dans vos liens Kochava de suivi de clics en utilisant la logique Liquid suivante :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Kochava collectent automatiquement l’IDFV par l’intermédiaire de nos intégrations SDK. Cela peut être utilisé comme identifiant d’appareil. Vous pouvez inclure l’IDFV dans vos liens Kochava de suivi de clics en utilisant la logique Liquid suivante :

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
Si vous n’utilisez actuellement aucun identifiant d’appareil, comme IDFV ou GAID, dans vos liens de suivi de clic, ou si vous ne le prévoyez pas à l’avenir, Kochava pourra toujours attribuer ces clics via ses modélisations probabilistes.
{% endalert %}


[18]: https://support.kochava.com/campaign-management/create-a-kochava-certified-postback "Kochava Postbacks"
[29]: https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3
[30]: https://support.kochava.com/sdk-integration/windows-and-xbox-one-sdk-integration?scrollto=marker_8
[4]: {% image_buster /assets/img/attribution/kochava.png %}
