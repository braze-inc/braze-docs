---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "Cet article de référence décrit le partenariat entre Braze et AppsFlyer, une plateforme d'analyse et d'attribution de marketing mobile qui vous aide à analyser et optimiser vos applications."
page_type: partner
search_tag: Partner

---

# AppsFlyer

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> [AppsFlyer](https://www.appsflyer.com/) est une plateforme d'analyse/analytique mobile qui vous aide à analyser et à optimiser vos applications grâce à l'analyse marketing, l'attribution mobile et les liens profonds.

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
Si vous avez une application Android, vous devez transmettre un ID d'appareil Braze unique à AppsFlyer. 

Assurez-vous que les lignes de code suivantes sont insérées au bon endroit - après le lancement du SDK Braze et avant le code d'initialisation du SDK AppsFlyer. Consultez le guide d'intégration SDK Android [Appsflyer](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk) pour plus d'informations.

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
Avant février 2023, notre intégration d'attribution AppsFlyer utilisait l'identifiant du fournisseur (IDFV) comme identifiant principal pour faire correspondre les données d'attribution iOS. Il n'est pas nécessaire pour les clients de Braze utilisant Objective-C de récupérer le site `device_id` de Braze et de l'envoyer à AppsFlyer lors de l'installation, car il n'y a pas d'interruption de service.
{% endalert%}

Pour ceux qui utilisent le SDK Swift v5.7.0+, si vous souhaitez continuer à utiliser l'IDFV comme identifiant mutuel, vous devez confirmer que le champ `useUUIDAsDeviceId` est défini sur `false` afin d'éviter une interruption de l'intégration. 

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

{% tab unity %}
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

Ici, vous trouvez le endpoint REST et vous générez votre clé d'importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation des données et l'endpoint REST sont utilisés dans l'étape suivante lors de la configuration d'un postback dans le tableau de bord d'Appsflyer.<br><br>![La boîte de dialogue "Importation de données pour l'attribution d'installation" disponible sur la page Technologie d'Appsflyer. Cette boîte contient la clé d'importation des données et l'endpoint REST.]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### Étape 3 : Configurez Braze dans le tableau de bord d'Appsflyer

1. Dans Appsflyer, accédez à la page **Partenaires Intégrés** dans la barre de gauche. Ensuite, recherchez **Braze** et sélectionnez le logo Braze pour ouvrir une fenêtre de configuration.
2. Dans l'onglet **intégration**, activez **Activer le partenaire**.
3. Indiquez la clé d'importation des données et le point de terminaison REST que vous avez trouvés dans le tableau de bord de Braze. 
4. Basculer **Advanced Privacy** off et enregistrer votre configuration.

Des informations supplémentaires sur ces instructions sont disponibles dans la [documentation d'AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration).

### Étape 4 : Confirmez l'intégration

Après que Braze a reçu des données d'attribution d'AppsFlyer, l'indicateur de connexion d'état sur la page des partenaires technologiques d'AppsFlyer dans Braze passe de " Non connecté " à " Connecté " et inclut un horodatage de la dernière demande réussie.

Ce statut ne change que lorsque Braze reçoit des données sur une attribution d'installation. Braze ignore les installations organiques (il les exclut du postback d'AppsFlyer) et ne les comptabilise pas lorsqu'il détermine si la connexion est réussie.

### Étape 5 : Affichage des données d'attribution des utilisateurs

#### Champs de données disponibles

Si votre intégration a réussi, Braze mappe toutes les données d'installation non organique aux filtres de segmentation.

| Champ de données Appsflyer | Filtre de segments Braze |
| -------------------- | --------------------- |
| `media_source` | Source attribuée |
| `campaign` | Campagne attribuée |
| `af_adset` | Groupe d'annonces attribué |
| `af_ad` | Annonce attribuée |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Vous pouvez segmenter votre base d'utilisateurs en fonction des données d'attribution dans le tableau de bord de Braze à l'aide des filtres d'attribution installation.

![Quatre filtres disponibles. La première est "Install Attribution Source is network_val_0". " La deuxième est "Install Attribution Source is campaign_val_0". " La troisième est "Install Attribution Source is adgroup_val_0". " La quatrième est "Install Attribution Source is creative_val_0". " À côté des filtres listés, vous pouvez voir comment ces sources d'attribution seront ajoutées au profil utilisateur. Dans la case "Attribution de l'installation" de la page d'information d'un utilisateur, la source d'installation est répertoriée comme network_val_0, la campagne est répertoriée comme campaign_val_0, etc.]({% image_buster /assets/img/braze_attribution.png %})

De plus, les données d'attribution pour un utilisateur particulier sont disponibles sur le profil de chaque utilisateur dans le tableau de bord de Braze.

{% alert note %}
Les données d'attribution pour les campagnes Facebook et X (anciennement Twitter) ne sont pas disponibles via nos partenaires. Ces sources médiatiques n'autorisent pas leurs partenaires à partager les données d'attribution avec des tiers et, par conséquent, nos partenaires ne peuvent pas envoyer ces données à Braze.
{% endalert %}

## Intégration d'AppsFlyer avec Braze pour la création de liens profonds

Les liens profonds—liens qui dirigent les utilisateurs vers une page ou un endroit spécifique au sein d'une application ou d'un site web—sont utilisés pour créer une expérience utilisateur sur mesure. 

Bien qu'ils soient largement utilisés, des problèmes peuvent survenir lors de l'utilisation de liens profonds envoyés par e-mail avec le suivi des clics#8212une autre fonctionnalité importante utilisée dans la collecte de données sur les utilisateurs. Ces problèmes sont dus au fait que les fournisseurs de services d'e-mailing (ESP) enveloppent les liens profonds dans un domaine d'enregistrement de clics, ce qui rompt le lien original. À ce titre, la prise en charge des liens profonds nécessite une configuration supplémentaire.

AppsFlyer propose un [service](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer) qui évite ces problèmes, en permettant à AppsFlyer de servir d'intermédiaire entre le serveur ESP et votre nom de domaine.  Son rôle de proxy permet de fournir des fichiers d'association (liens AASA/asset), ce qui facilite la création de liens profonds. 

## Étape 1 - Créer un domaine de suivi des clics 

En suivant les premiers éléments du [guide de configuration des e-mails de Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate), créez un domaine d'envoi d'e-mails et un domaine de suivi des clics. Pour obtenir de l'aide, vous pouvez créer un ticket via le tableau de bord de Braze pour initier la configuration du nouveau CTD avec l'équipe Braze Email.

![L'interface utilisateur de Braze montre le bouton "Obtenir de l'aide", qui se trouve sous le bouton "Support" dans le coin supérieur droit.]({% image_buster /assets/img/attribution/appsflyer/1.png %})

La création d'un nouveau CTD est obligatoire, même si vous utilisez déjà un CTD existant. Cela permet de s'assurer qu'il n'y a pas d'impact sur le trafic des campagnes d'e-mail en ligne/instantanées en cours. 

{% alert important%}
AppsFlyers crée le certificat SSL. À ce stade, les liens des e-mails ne sont probablement pas sécurisés, ce qui signifie que le préfixe de l'URL est HTTP au lieu de HTTPS. Ce problème est résolu dans les étapes suivantes.	
{%endalert%}

## Étape 2 - Créer un modèle OneLink dans AppsFlyer
Créez un [modèle OneLink](https://support.appsflyer.com/hc/en-us/articles/207032246-Create-a-OneLink-template#procedures) et configurez Universal Links/App Links sous "When app is installed". Ce modèle est utilisé ultérieurement pour créer des liens OneLink pour vos campagnes d'e-mail.

{% alert note%} Si vous disposez déjà d'un modèle OneLink configuré qui active les liens universels/liens d'application, vous pouvez l'utiliser.
{%endalert%}

## Étape 3 - Mettre en place votre intégration Braze dans Appsflyer
Il est maintenant temps de paramétrer votre intégration Braze dans AppsFlyer. Cette étape et la suivante ("Configurer votre application") peuvent être mises en place en même temps.
Pour paramétrer l'intégration de Braze dans AppsFlyer :

### 1\. Dans AppsFlyer, dans le menu latéral, sélectionnez Engage > ESP integration.
![L'interface utilisateur d'Appsflyer montre le bouton "Intégration ESP", qui se trouve dans le menu de gauche.]({% image_buster /assets/img/attribution/appsflyer/2.png %})

 
### 2\. Sélectionnez Braze.
![L'interface utilisateur d'Appsflyer montre la liste des intégrations ESP, y compris Braze.]({% image_buster /assets/img/attribution/appsflyer/3.png %})

 
### 3\. Sélectionnez le modèle OneLink que vous souhaitez utiliser pour les campagnes d'e-mail, puis cliquez sur Suivant.
![L'interface utilisateur d'Appsflyer montre le menu déroulant permettant aux utilisateurs de sélectionner leur modèle.]({% image_buster /assets/img/attribution/appsflyer/4.png %})

 
### 4\. Saisissez votre domaine de suivi des clics et la valeur "endpoint Braze", qui a été fournie avec le nouveau CTD créé à l'étape 1, puis cliquez sur Valider la connexion.

Cela permet de valider que le domaine de suivi des clics pointe vers l'endpoint que vous avez saisi.

![L'interface utilisateur d'Appsflyer met en évidence l'endroit où les clients doivent ajouter leur domaine de suivi des clics et les détails associés.]({% image_buster /assets/img/attribution/appsflyer/5.png %})

Par "Braze Endpoint", AppsFlyer demande les détails fournis par Braze à l'étape 1 de ce guide, en particulier le nouveau CTD. 

Cliquez ensuite sur **Valider la connexion**, ce qui permet de valider que le domaine de suivi des clics pointe vers l'endpoint que vous avez saisi.
Lorsque vous avez terminé, cliquez sur **Suivant.**

### 5\. Acheminez le trafic des liens vers AppsFlyer :

#### a. Copiez et envoyez les instructions personnalisées préfabriquées dans AppsFlyer à votre administrateur informatique ou de domaine. 

Votre administrateur doit réacheminer le trafic de votre campagne e-mail des serveurs ESP vers les serveurs AppsFlyer en mettant à jour vos enregistrements DNS CNAME avec le nouveau domaine fourni par AppsFlyer.

Par conséquent, à chaque fois qu'un lien est cliqué, le clic est redirigé vers AppsFlyer, qui le redirige à son tour vers l'endpoint ESP.

![Diagramme illustrant comment les données de clics sont passées de votre domaine à AppsFlyer, puis à votre endpoint esp.]({% image_buster /assets/img/attribution/appsflyer/6.png %})

#### b. Après avoir copié et envoyé les instructions, cliquez sur Terminé.
Votre intégration à Braze a été créée.

{%alert important%}
L'état de votre intégration à Braze est en attente et ne commence à fonctionner qu'une fois l'enregistrement CNAME mappé. Il peut s'écouler jusqu'à 24 heures après le mappage pour qu'une nouvelle intégration commence à fonctionner et devienne active.
{%endalert%}

## Étape 4 : Configurer votre application (tâche du développeur)
Appsflyer [propose des conseils](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer#step-2-configure-your-app-developer-task) sur la configuration correcte des apps, qui doivent être suivis par vos équipes web ou apps afin de prendre en charge le lien universel. 

## Étape 5 : Confirmez que le suivi des clics par SSL est activé avec Braze

A ce stade, après avoir partagé et validé les détails du CTD dans Appsflyer, nous vous recommandons d'effectuer un envoi test pour confirmer que votre domaine d'envoi Onelink dispose d'un certificat SSL. Ceci est conforme à notre guide de [configuration de l'e-mail.](https://www.braze.com/docs/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate) 

Vous pouvez procéder à l'assurance qualité et à la résolution des problèmes en envoyant un lien profond à l'aide de OneLink. Consultez la [documentation d'Appsflyer](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a) pour plus de détails sur l'utilisation de OneLink.

Si les liens CTD sont identifiés comme HTTP, contactez l'équipe Email Ops de Braze pour activer le suivi des clics SSL. Cela garantit que tous les liens HTTP sont automatiquement convertis en HTTPS.
Vous pouvez utiliser l'exemple de texte de message suivant lorsque vous contactez votre gestionnaire de la satisfaction client, ou en soulevant à nouveau un ticket dans le tableau de bord de Braze, comme à l'étape 1 : 

```
Hi Team,
Could you please enable SSL click tracking for CTD XXX? It is currently set to HTTP instead of HTTPS. 
```

### URLs de suivi de clics Appsflyer dans Braze (facultatif)

Vous pouvez utiliser les [liens d'attribution OneLink](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) d'Appsflyer dans les campagnes Braze sur les notifications push, les e-mails, et plus encore. Cela vous permet de renvoyer les données d'attribution d'installation ou de réengagement de vos campagnes Braze dans AppsFlyer. Vous pouvez ainsi mesurer plus efficacement vos efforts de marketing et prendre des décisions fondées sur des données.

Vous pouvez simplement créer votre URL de suivi OneLink dans Appsflyer et l'insérer directement dans vos campagnes Braze. AppsFlyer utilise ensuite ses [méthodologies d'attribution probabiliste](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) pour attribuer l'utilisateur qui a cliqué sur le lien. Nous recommandons d'ajouter vos liens de suivi AppsFlyer avec un identifiant d'appareil pour améliorer la précision des attributions de vos campagnes Braze. Cela permet d'attribuer de manière déterministe l'utilisateur qui a cliqué sur le lien.

{% tabs local %}
{% tab Android %}
Pour Android, Braze permet à ses clients d'opter pour la [collecte de l'ID publicitaire de Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). L'intégration SDK d'AppsFlyer collecte également le GAID. Vous pouvez inclure le GAID dans vos liens de suivi de clics AppsFlyer en utilisant la logique Liquid suivante :
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Pour iOS, Braze et Appsflyer collectent automatiquement l'IDFV nativement via nos intégrations SDK. Vous pouvez utiliser l'IDFC comme identifiant de l'appareil. Vous pouvez inclure l'IDFV dans vos liens de suivi de clics AppsFlyer en utilisant la logique Liquid suivante :

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}
