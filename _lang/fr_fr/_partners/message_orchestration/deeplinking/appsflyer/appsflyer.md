---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "Cet article de référence décrit le partenariat entre Braze et AppsFlyer, une plateforme d'analyse et d'attribution de marketing mobile qui vous aide à analyser et optimiser vos applications."
page_type: partner
search_tag: Partner

---

# AppsFlyer

{% multi_lang_include video.html ID="gQ9y2DA2LuQ" align="right" %}

> Appsflyer est une plateforme d'analyse et d'attribution de marketing mobile qui vous aide à analyser et optimiser vos applications grâce à l'analyse marketing, l'attribution mobile et la création de liens profonds.

L'intégration de Braze et Appsflyer vous permet de mieux comprendre comment optimiser et créer des campagnes plus holistiques en tirant parti des données d'attribution d'installation mobile d'Appsflyer. 

Vous pouvez également transmettre vos audiences AppsFlyer (cohortes) directement à Braze avec l'intégration [AppsFlyer Audiences]({{site.baseurl}}/partners/data_and_analytics/cohort_import/appsflyer_audiences/), vous permettant de créer des campagnes d'engagement client puissantes ciblant les bons utilisateurs au bon moment. 

## Conditions préalables

| Condition | Description |
|---|---|
| Compte AppsFlyer | Un compte AppsFlyer est nécessaire pour bénéficier de ce partenariat. |
| Application iOS ou Android | Cette intégration prend en charge les applications iOS et Android. En fonction de votre plateforme, des extraits de code peuvent être requis dans votre application. Vous trouverez des informations détaillées sur ces exigences à l'étape 1 du processus d'intégration. |
| SDK AppsFlyer | Outre le SDK Braze requis, vous devez installer le [SDK Appsflyer](https://dev.appsflyer.com/hc/docs/getting-started).
| Configuration du domaine de l'e-mail terminée | Vous devez avoir terminé l'étape de [configuration IP et domaine]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/) de la configuration de votre e-mail lors de l'onboarding de Braze. |
| certificat SSL | Votre [certificat SSL]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#acquiring-an-ssl-certificate) doit être configuré. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Mapper l’ID de l'appareil

{% tabs local %}
{% tab Android %}
Si vous avez une application Android, vous devez transmettre un ID d'appareil Braze unique à Appsflyer. 

Assurez-vous que les lignes de code suivantes sont insérées au bon endroit, après le lancement du SDK Braze et avant le code d'initialisation du SDK Appsflyer. Consultez le guide d'intégration SDK Android [Appsflyer](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk) pour plus d'informations.

```kotlin
val customData = HashMap<String, Any>()
Braze.getInstance(context).getDeviceIdAsync { deviceId ->
   customData["brazeCustomerId"] = deviceId
   setAdditionalData(customData)
}
```
{% endtab %}

{% tab ios %}
{% alert important %}
Avant février 2023, notre intégration d'attribution Appsflyer utilisait l'IDFV comme identifiant principal pour faire correspondre les données d'attribution iOS. Il n'est pas nécessaire pour les clients de Braze utilisant Objective-C de récupérer le Braze `device_id` et de l'envoyer à Appsflyer lors de l'installation, car il n'y aura aucune interruption de service.
{% endalert%}

Pour ceux qui utilisent le SDK Swift v5.7.0+, si vous souhaitez continuer à utiliser l'IDFV comme identifiant mutuel, vous devez confirmer que le champ `useUUIDAsDeviceId` Braze est défini sur `false` pour éviter toute interruption de l'intégration. 

Si ce champ est défini sur `true`, vous devez mettre en œuvre le mappage de l'ID de l'appareil iOS pour Swift afin de transmettre le  champ `device_id` à Appsflyer lors de l'installation de l'application afin que Braze puisse correspondre correctement aux attributions iOS.

{% subtabs local %}
{% subtab Swift %}

```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
AppsFlyerLib.shared().customData = ["brazeDeviceId": braze.deviceId]
```
{% endsubtab %}

{% subtab Objective-C %}
```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[[AppsFlyerLib shared] setAdditionalData:@{
    @"brazeDeviceId": braze.deviceId
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Unity %}
Pour mapper l'ID de l'appareil dans Unity, procédez comme suit :

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```
{% endtab %}
{% endtabs %}

### Étape 2 : Obtenez la clé d'importation des données Braze

Dans Braze, accédez à **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **AppsFlyer**. 

Ici, vous trouverez l’endpoint REST et générerez votre clé d'importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation des données et l'endpoint REST sont utilisés dans l'étape suivante lors de la configuration d'un postback dans le tableau de bord d'Appsflyer.<br><br>![La boîte de dialogue "Importation de données pour l'attribution d'installation" disponible sur la page Technologie d'Appsflyer. Cette boîte contient la clé d'importation des données et l'endpoint REST.]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### Étape 3 : Configurez Braze dans le tableau de bord d'Appsflyer

1. Dans Appsflyer, accédez à la page **Partenaires Intégrés** dans la barre de gauche. Ensuite, recherchez **Braze** et sélectionnez le logo Braze pour ouvrir une fenêtre de configuration.
2. Dans l'onglet **intégration**, activez **Activer le partenaire**.
3. Indiquez la clé d'importation des données et le point de terminaison REST que vous avez trouvés dans le tableau de bord de Braze. 
4. Basculer **Advanced Privacy** off et enregistrer votre configuration.

Des informations supplémentaires sur ces instructions sont disponibles dans la [documentation d'AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration).

### Étape 4 : Confirmez l'intégration

Une fois que Braze reçoit les données d'attribution d'Appsflyer, l'indicateur d’état de la connexion sur la page des partenaires technologiques d'Appsflyer dans Braze passera de "Non connecté" à "Connecté". Un horodatage de la dernière requête réussie sera également inclus. 

Notez que cela ne se produira pas tant que nous n'aurons pas reçu de données sur une installation attribuée. Les installations organiques, qui doivent être exclues du système automatisé de communication Appsflyer, sont ignorées par notre API et ne sont pas comptabilisées lors de la détermination de l'établissement d'une connexion réussie.

### Étape 5: Affichage des données d'attribution des utilisateurs

#### Champs de données disponibles

En supposant que vous configurez votre intégration comme suggéré, Braze mappera toutes les données d'installation non organiques aux filtres de segment.

| Champ de données Appsflyer | Filtre de segments Braze |
| -------------------- | --------------------- |
| `media_source` | Source attribuée |
| `campaign` | Campagne attribuée |
| `af_adset` | Groupe d'annonces attribué |
| `af_ad` | Annonce attribuée |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Votre base d'utilisateurs peut être segmentée par les données d'attribution dans le tableau de bord de Braze en utilisant les filtres d'attribution d'installation.

![Quatre filtres disponibles. Le premier est « la source d'attribution d'installation est network_val_0 ». Le second est "La source d'attribution d'installation est campagne_val_0". Le troisième est « La source d'attribution d'installation est adgroup_val_0 ». Le quatrième est « La source d'attribution d'installation est creative_val_0 ». Outre les filtres répertoriés, vous pouvez voir comment ces sources d'attribution seront ajoutées au profil utilisateur. Dans la case "Attribution d'installation" de la page d'information d'un utilisateur, la source d'installation est indiquée comme network_val_0, la campagne est indiquée comme campaign_val_0, etc.]({% image_buster /assets/img/braze_attribution.png %})

De plus, les données d'attribution pour un utilisateur particulier sont disponibles sur le profil de chaque utilisateur dans le tableau de bord de Braze.

{% alert note %}
Les données d'attribution pour les campagnes Facebook et X (anciennement Twitter) ne sont pas disponibles via nos partenaires. Ces sources médiatiques ne permettent pas à leurs partenaires de partager les données d'attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.
{% endalert %}

## Intégrez Appsflyer à un fournisseur de services de messagerie pour la création de liens profonds

Appsflyer s'intègre à la fois avec Sendgrid et SparkPost en tant que fournisseurs de services de messagerie (ESP) pour prendre en charge la création de liens profonds et le suivi des clics. Suivez les instructions ci-dessous pour intégrer le fournisseur de services de messagerie de votre choix.

{% alert tip %}
Les liens profonds—liens qui dirigent les utilisateurs vers une page ou un endroit spécifique au sein d'une application ou d'un site web—sont utilisés pour créer une expérience utilisateur sur mesure. Bien que largement utilisé, des problèmes peuvent survenir lors de l'utilisation de liens profonds envoyés par e-mail avec le suivi des clics, une autre fonctionnalité importante utilisée dans la collecte de données utilisateur. Ces problèmes sont dus aux fournisseurs de services de messagerie qui placent les liens profonds dans un domaine d'enregistrement de clics, brisant le lien d’origine. À ce titre, la prise en charge des liens profonds nécessite une configuration supplémentaire. En intégrant Appsflyer avec Sendgrid ou SparkPost, vous évitez ces problèmes. En savoir plus sur ce sujet dans [Liens universels et liens d'application]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).
{% endalert %}

### Étape 1 : Configurer OneLink dans Appsflyer

1. Dans Appsflyer, sélectionnez un modèle OneLink pour vos campagnes d’e-mails. Assurez-vous que le modèle prend en charge les liens universels (iOS) ou les liens d'application (Android). 
2. Configurez votre application pour prendre en charge la création de liens profonds avec OneLink. Consultez la [documentation d'Appsflyer](https://dev.appsflyer.com/hc/docs/dl_work_flow#initial-setup) pour plus de détails sur la configuration de votre application pour prendre en charge OneLink.

### Étape 2 : Configurez votre application pour prendre en charge les liens universels et les liens d'application

Les liens universels (iOS) ou les liens d'application (Android) sont autorisés par le système d'exploitation de l'appareil pour ouvrir une application spécifiée lorsqu'ils sont cliqués.

Effectuez les étapes suivantes pour prendre en charge les liens universels et les liens d'application.

{% tabs local %}
{% tab Sendgrid %}
{% subtabs %}
{% subtab iOS %}
Configurez l'hébergement du fichier Apple App Site Association (AASA) pour activer les liens universels dans vos e-mails.

1. Obtenez un fichier AASA de l'une des manières suivantes :
    * Si vous avez configuré OneLink avec des liens universels, vous avez peut-être déjà un fichier AASA associé à OneLink. Pour obtenir le fichier AASA, effectuez ce qui suit :
        * Copiez le sous-domaine OneLink de votre modèle OneLink. Assurez-vous que le modèle prend en charge les liens universels.
        * Collez-le à la place de la marque substitutive dans l'URL suivante : `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * Pour télécharger le fichier AASA, collez l'URL OneLink dans la barre d'adresse de votre navigateur et appuyez sur **Entrée**. Le fichier sera ensuite téléchargé sur votre ordinateur, et vous pourrez l'ouvrir et en consulter le contenu à l'aide de n'importe quel éditeur de texte.
    * [Le guide d'Apple sur les liens universels](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content) explique comment créer le fichier AASA.
2. Hébergez le fichier AASA dans le serveur de domaine de votre enregistrement de clics. Le fichier doit être hébergé dans le chemin : `click.example.com/.well-known/apple-app-site-association`. 

Consultez la [documentation Sendgrid](https://docs.sendgrid.com/ui/sending-email/universal-links) pour apprendre à configurer le fichier AASA pour Sendgrid et configurer les services de réseau de diffusion de contenu pour héberger le fichier AASA.

{% alert important %}
Une fois le fichier AASA hébergé, toute modification de votre configuration OneLink (modification ou remplacement) nécessite la génération d'un nouveau fichier AASA.
{% endalert %}
{% endsubtab %}
{% subtab Android %}
Configurez l'hébergement de fichiers de liens d'actifs numériques pour activer les liens d'application dans vos e-mails.

1. Obtenez un fichier de liens de ressources numériques en utilisant l'une des méthodes suivantes :
    * Si vous avez configuré OneLink avec des liens d'application, vous avez peut-être déjà un fichier de liens de ressources numériques associé à OneLink. Pour obtenir le fichier, effectuez ce qui suit :
        * Copiez le sous-domaine OneLink de votre modèle OneLink. Assurez-vous que le modèle prend en charge les liens d'application.
        * Ajoutez `/.well-known/assetlinks.json` à la fin de l'URL OneLink.
        * Pour télécharger le fichier de liens de ressources numériques, collez l'URL OneLink dans la barre d'adresse de votre navigateur et appuyez sur **Entrée**. Par exemple, `https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json`. Le fichier sera ensuite téléchargé sur votre ordinateur, et vous pourrez l'ouvrir et en consulter le contenu à l'aide de n'importe quel éditeur de texte.
    * [Le guide d'Android sur les liens d'application](https://developer.android.com/studio/write/app-link-indexing) explique comment créer le fichier de liens de ressource numérique.
2. Hébergez le fichier de liens d'actifs numériques dans le serveur de domaine d'enregistrement de clics. Le fichier doit être hébergé dans le chemin : `click.example.com/.well-known/apple-app-site-association`.

Consultez la [documentation Sendgrid](https://docs.sendgrid.com/ui/sending-email/universal-links) pour savoir comment configurer le fichier de liens de ressources numériques pour Sendgrid et configurer les services de réseau de diffusion de contenu pour héberger le fichier de liens de ressources numériques.

{% alert important %}
Une fois le fichier de liens de ressources numériques hébergé, toute modification de votre configuration OneLink (modification ou remplacement) nécessite la génération d'un nouveau fichier.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab SparkPost %}
{% subtabs %}
{% subtab iOS %}
#### Étape 2a: Configurer l'hébergement de fichiers AASA
Configurez l'hébergement du fichier Apple App Site Association (AASA) pour activer les liens universels dans vos e-mails.

1. Obtenez un fichier AASA de l'une des manières suivantes :
    * Si vous avez configuré OneLink avec des liens universels, vous avez peut-être déjà un fichier AASA associé à OneLink. Pour obtenir le fichier AASA, effectuez ce qui suit :
        * Copiez le sous-domaine OneLink de votre modèle OneLink. Assurez-vous que le modèle prend en charge les liens universels.
        * Collez-le à la place de la marque substitutive dans l'URL suivante : `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * Pour télécharger le fichier AASA, collez l'URL OneLink dans la barre d'adresse de votre navigateur et appuyez sur **Entrée**. Le fichier sera ensuite téléchargé sur votre ordinateur, et vous pourrez l'ouvrir et en consulter le contenu à l'aide de n'importe quel éditeur de texte.
    * [Le guide d'Apple sur les liens universels](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content) explique comment créer le fichier AASA.
2. Hébergez le fichier AASA dans le serveur de domaine de votre enregistrement de clics. Le fichier doit être hébergé dans le chemin : `click.example.com/.well-known/apple-app-site-association`. 

Consultez la [documentation SparkPost](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve) pour apprendre à configurer le fichier AASA pour SparkPost et définir des sous-chemins de lien personnalisés.

{% alert important %}
Une fois le fichier AASA hébergé, toute modification de votre configuration OneLink (modification ou remplacement) nécessite la génération d'un nouveau fichier AASA.
{% endalert %}

#### Étape 2b: Redirigez votre domaine de suivi des clics vers votre hôte de fichier AASA
Lors de la [configuration de l'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/), vous avez créé un enregistrement CNAME dans votre serveur DNS. Effectuez les étapes suivantes après avoir vérifié votre domaine de suivi des clics dans Braze. 

1. Supprimez l'enregistrement CNAME qui redirige votre sous-domaine vers le domaine SparkPost.
2. Créez un enregistrement CNAME qui redirige votre domaine de suivi des clics vers le réseau de diffusion de contenu hébergeant votre fichier AASA d'application, au lieu de l'enregistrement que vous avez supprimé ci-dessus.
{% endsubtab %}
{% subtab Android %}
#### Étape 2a: Configurer l'hébergement de fichiers de liens de ressources numériques
Configurez l'hébergement de fichiers de liens d'actifs numériques pour activer les liens d'application dans vos e-mails.

1. Obtenez un fichier de liens de ressources numériques en utilisant l'une des méthodes suivantes :
    * Si vous avez configuré OneLink avec des liens d'application, vous avez peut-être déjà un fichier de liens de ressources numériques associé à OneLink. Pour obtenir le fichier, effectuez ce qui suit :
        * Copiez le sous-domaine OneLink de votre modèle OneLink. Assurez-vous que le modèle prend en charge les liens d'application.
        * Ajoutez `/.well-known/assetlinks.json` à la fin de l'URL OneLink.
        * Pour télécharger le fichier de liens de ressources numériques, collez l'URL OneLink dans la barre d'adresse de votre navigateur et appuyez sur **Entrée**. Par exemple, `https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json`. Le fichier sera ensuite téléchargé sur votre ordinateur, et vous pourrez l'ouvrir et en consulter le contenu à l'aide de n'importe quel éditeur de texte.
    * [Le guide d'Android sur les liens d'application](https://developer.android.com/studio/write/app-link-indexing) explique comment créer le fichier de liens de ressource numérique.
2. Hébergez le fichier de liens d'actifs numériques dans le serveur de domaine d'enregistrement de clics. Le fichier doit être hébergé dans le chemin : `click.example.com/.well-known/apple-app-site-association`.

Consultez la [documentation SparkPost](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve) pour savoir comment configurer le fichier de liens de ressources numériques pour SparkPost et définir des sous-chemins de liens personnalisés.

{% alert important %}
Une fois le fichier de liens de ressources numériques hébergé, toute modification de votre configuration OneLink (modification ou remplacement) nécessite la génération d'un nouveau fichier.
{% endalert %}

#### Étape 2b: Redirigez votre domaine de suivi des clics vers votre hôte de fichier de liens de ressources numériques
Lors de la [configuration de l'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/), vous avez créé un enregistrement CNAME dans votre serveur DNS. Effectuez les étapes suivantes après avoir vérifié votre domaine de suivi des clics dans Braze. 

1. Supprimez l'enregistrement CNAME qui redirige votre sous-domaine vers le domaine SparkPost.
2. Créez un enregistrement CNAME qui redirige votre domaine de suivi des clics vers le réseau de diffusion de contenu hébergeant le fichier de liens d'actifs numériques de votre application, au lieu de l'enregistrement que vous avez supprimé ci-dessus.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Étape 3 : Configurez votre SDK AppsFlyer pour prendre en charge la création de liens profonds

{% tabs local %}
{% tab Sendgrid %}
{% subtabs %}
{% subtab iOS %}
#### Étape 3a: Configurez votre SDK pour prendre en charge le fichier AASA
Après avoir hébergé le fichier AASA dans votre domaine d'enregistrement de clics, configurez votre SDK AppsFlyer pour prendre en charge le fichier AASA.

1. Dans Xcode, sélectionnez votre projet.
2. Sélectionnez **Capacités.**
3. Activez **les domaines associés.**
4. Cliquez sur **+** et entrez votre domaine de clics. Par exemple, `applinks:click.example.com`.
Un clic sur le lien universel a pour effet d’ouvrir votre application et d’initier le SDK. Pour permettre à l'application d'extraire le lien OneLink associé au domaine de clics et de résoudre le lien profond, procédez comme suit :

#### Étape 3b: Gérer les données de lien profond
1. Fournissez le domaine d'enregistrement des clics à l'API SDK [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls). Cette API doit être appelée avant l'initialisation du SDK. `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
2. Utilisez l'[`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution) API pour obtenir les paramètres du lien profond et gérer les données du lien profond.

{% endsubtab %}
{% subtab Android %}
#### Étape 3a: Configurez votre SDK pour prendre en charge le fichier de liens de ressources numériques

Après avoir hébergé le fichier Digital Asset Links dans votre domaine d'enregistrement de clics à l'étape précédente, configurez votre SDK pour prendre en charge le fichier.

Dans votre manifeste Android, ajoutez l'hôte du domaine de clic et tout préfixe dans la balise de l'activité dans laquelle vous souhaitez créer un lien profond.

```xml
<activity android:name=".DeepLinkActivity">
    <intent-filter android:autoVerify="true">
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />
      <data
        android:scheme="https"
        android:host="click.example.com"
        android:pathPrefix="/campaign"
      />
    </intent-filter>
  </activity>
```

#### Étape 3b: Gérer les données de lien profond
Un clic sur un lien d’application a pour effet d’ouvrir votre application et d’initier le SDK.  Pour permettre à l'application d'extraire le lien OneLink associé au domaine de clics et de résoudre le lien profond, répertoriez les domaines de clics dans la méthode SDK [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls). Cette propriété doit être définie avant l'initialisation du SDK. `AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "anotherclickdomain.com");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab SparkPost %}
{% subtabs %}
{% subtab iOS %}
#### Étape 3a: Configurez votre SDK pour prendre en charge le fichier AASA
Après avoir hébergé le fichier AASA dans votre domaine d'enregistrement de clics, configurez votre SDK pour prendre en charge le fichier AASA.

1. Dans Xcode, sélectionnez votre projet.
2. Sélectionnez **Capacités.**
3. Activez **les domaines associés.**
4. Cliquez sur **+** et entrez votre domaine de clics. Par exemple, `applinks:click.example.com`.

#### Étape 3b: Gérer les données de lien profond
Un clic sur le lien universel a pour effet d’ouvrir votre application et d’initier le SDK. Pour permettre au SDK d'extraire le lien OneLink associé au domaine de clics, procédez comme suit :
1. Répertoriez les domaines de clics dans la propriété SDK [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls). Assurez-vous de définir cette propriété avant l'initialisation du SDK.
2. Assurez-vous que la liste <em>spgo.io</em> est l'un des domaines répertoriés. SparkPost possède ce domaine et il fait partie du flux de redirection. `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
3. Utilisez l'[`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution) API pour obtenir les paramètres du lien profond et gérer les données du lien profond.
{% endsubtab %}
{% subtab Android %}
#### Étape 3a: Configurez votre SDK pour prendre en charge le fichier de liens de ressources numériques

Après avoir hébergé le fichier Digital Asset Links dans votre domaine d'enregistrement de clics à l'étape précédente, configurez votre SDK pour prendre en charge le fichier.

Dans votre manifeste Android, ajoutez l'hôte du domaine de clic et tout préfixe dans la balise de l'activité dans laquelle vous souhaitez créer un lien profond.

```xml
<activity android:name=".DeepLinkActivity">
    <intent-filter android:autoVerify="true">
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />
      <data
        android:scheme="https"
        android:host="click.example.com"
        android:pathPrefix="/campaign"
      />
    </intent-filter>
  </activity>
```

#### Étape 3b: Gérer les données du lien d'application
Un clic sur un lien d’application a pour effet d’ouvrir votre application et d’initier le SDK. Pour permettre à l'application d'extraire le lien OneLink associé au domaine de clics et de résoudre le lien profond, procédez comme suit :

1. Répertoriez les domaines de clics dans la méthode SDK [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls). Cette propriété doit être définie avant l'initialisation du SDK.
2. Assurez-vous que la liste *spgo.io* est l'un des domaines répertoriés. SparkPost possède ce domaine et il fait partie du flux de redirection. `AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "spgo.io");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

Une fois que vous avez terminé les étapes d'intégration, vous pouvez effectuer l'assurance qualité et la résolution des problèmes en envoyant un lien profond à l'aide de OneLink. Consultez la [documentation d'Appsflyer](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a) pour plus de détails sur l'utilisation de OneLink.

### URLs de suivi de clics Appsflyer dans Braze (facultatif)

Vous pouvez utiliser les [liens d'attribution OneLink](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) d'Appsflyer dans les campagnes Braze sur les notifications push, les e-mails, et plus encore. Cela vous permet de renvoyer les données d'attribution d'installation ou de réengagement de leurs campagnes Braze dans Appsflyer. En conséquence, vous serez en mesure de mesurer vos efforts marketing plus efficacement et de prendre des décisions basées sur les donnée.

Vous pouvez simplement créer votre URL de suivi OneLink dans Appsflyer et l'insérer directement dans vos campagnes Braze. Appsflyer utilisera ensuite ses [méthodologies d'attribution probabiliste](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) pour attribuer l'utilisateur qui a cliqué sur le lien. Nous recommandons d'ajouter vos liens de suivi AppsFlyer avec un identifiant d'appareil pour améliorer la précision des attributions de vos campagnes Braze. Cela attribuera de manière déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs local %}
{% tab Android %}
Braze permet aux clients Android de s'abonner à la [collecte de l'ID publicitaire Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). Le GAID est également collecté nativement via l'intégration du SDK d'Appsflyer. Vous pouvez inclure le GAID dans vos liens de suivi de clics Appsflyer en utilisant la logique liquid suivante :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Appsflyer collectent automatiquement l'IDFV nativement via nos intégrations SDK. Cela peut être utilisé comme identifiant de l'appareil. Vous pouvez inclure l'IDFV dans vos liens de suivi de clics Appsflyer en utilisant la logique Liquid suivante :

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}



