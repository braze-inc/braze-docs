---
nav_title: PassKit
article_title: PassKit
alias: /partners/passkit/
description: "Cet article de référence présente le partenariat entre Braze et Passkit. Ce partenariat vous permet d’accroître votre portée sur mobile en intégrant les passes Apple Wallet et Google Pay à votre expérience client."
page_type: partner
search_tag: Partenaire

---

# PassKit

> PassKit vous permet d’accroître votre portée sur mobile en intégrant les passes Apple Wallet et Google Pay à votre expérience client. Il permet de créer, gérer, distribuer et analyser facilement et rapidement la performance de vos bons de réduction digitaux, de vos cartes de fidélité ou de membres, de vos coupons et plus encore, et ce sans que vos clients aient besoin d’une autre application.

L’intégration de Braze et PassKit permet d’améliorer et mesurer l’engagement de vos campagnes en ligne en fournissant instantanément des passes Apple Wallet et Google Pay personnalisés. Vous pouvez ensuite analyser l’utilisation et effectuer des ajustements en temps réel pour améliorer le trafic en magasin en déclenchant des messages basés sur la localisation ainsi que des mises à jour dynamiques et personnalisées du portefeuille mobile de vos clients. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte PassKit | Vous devrez disposer d’un compte PassKit et d’un gestionnaire de compte PassKit. |
| `userDefinedID` | Pour mettre à jour de manière appropriée les événements et attributs personnalisés de vos utilisateurs entre PassKit et Braze, vous devrez définir l’ID externe de Braze en tant que `userDefinedID`. Cette valeur `userDefinedID` sera utilisée lors de la réalisation des appels API aux endpoints PassKit. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze  | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance][6]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

Pour enrichir davantage l’expérience de vos clients en matière de portefeuille mobile, depuis votre tableau de bord PassKit, vous pouvez choisir de transmettre des données à Braze par le biais de l’[endpoint users/track][7] de Braze. 

Les exemples de données à partager dans PassKit incluent :
- **Création de passe** : lorsqu’un client clique sur un lien de passe et qu’il affiche d’abord un passe.
- **Installations de passe** : lorsque le client ajoute et enregistre le passe dans son application Wallet.
- **Mises à jour de passe** : lorsqu’un passe est mis à jour.
- **Suppression de passe** : lorsqu’un client supprime le passe de son application Wallet.

Une fois les données transmises à Braze, vous pouvez créer des audiences, personnaliser le contenu via Liquid et déclencher des campagnes ou des Canvas une fois que ces actions ont été effectuées.

## Connecter Passkit à Braze

Pour transmettre des données à partir de PassKit, assurez-vous que vous avez défini votre ID externe Braze comme étant l’`externalId` de PassKit.

1. Dans **Settings (Paramètres)**, sous **Integrations (Intégrations)** dans votre projet ou programme passe de PassKit, cliquez sur **Connect (Connexion)** sous l’onglet **Braze**.<br>![Mosaïque de l’intégration Braze dans la plateforme PassKit.][5]{: style="max-width:80%"}<br><br>
2. Remplissez votre clé d’API Braze, l’URL de l’endpoint et donnez un nom à votre connecteur.<br><br>
3. Cochez **Enable Integration (Activer l’intégration)** et les événements que vous voulez déclencher ou personnaliser avec vos messages dans Braze.<br>![La mosaïque d’intégration PassKit Braze développée pour accepter la clé d’API, l’URL de l’endpoint, le nom de l’intégration, les paramètres d’activation, les paramètres d’adhésion et les paramètres du passe.][4]{: style="max-width:70%"}

## Créer un passe à l’aide d’un lien SmartPass

Au sein de Braze, vous pouvez configurer un lien SmartPass pour générer une URL unique pour vos clients afin d’installer leur passe sur Android ou iOS. Pour ce faire, vous devez définir une charge utile de données SmartPass cryptée pouvant être appelée à partir d’un bloc de contenu dans Braze. Ce [bloc de contenu][9] peut ensuite être réutilisé pour de futurs passes et coupons. Les éléments suivants seront utilisés pendant votre intégration :

- **URL de PassKit** : Votre URL de PassKit est une URL unique pour votre programme PassKit.<br>Chaque programme a une URL unique, et vous pouvez la trouver sous l’onglet **Distribution** de votre programme ou projet PassKit. (p. ex., https://pub1.pskt.io/c/ww0jir)<br><br>
- **Secret de PassKit** : En plus de l’URL, vous devrez disposer de la clé de PassKit pour ce programme.<br>Vous pouvez l’afficher sur la même page que votre URL de PassKit.<br><br>
- **ID du programme (ou du projet)** : Votre ID de programme PassKit sera requis pour créer l’URL SmartPass. <br>Vous pouvez le trouver sous l’onglet **Settings (Paramètres)** de votre projet ou programme.

Pour plus d’informations sur la création de liens SmartPass cryptés, consultez cet [article de PassKit][8].

### Étape 1 : Définissez les charges utiles de données de votre passe {#passkit-integrations}

Tout d’abord, vous devez définir le coupon ou la charge utile du membre. 

Il existe de nombreux composants différents que vous pouvez inclure dans votre charge utile, mais voici deux éléments importants à noter :

| Composant | Requis | Type | Description |
| --------- | -------- | ---- | ----------- |
|`person.externalId` | Requis | String | Défini comme l’ID externe de Braze, il est crucial pour que les rappels de PassKit vers Braze fonctionnent, permettant aux utilisateurs de Braze d’avoir des coupons pour plusieurs offres dans une seule campagne. Non appliqué comme unique. |
| `members.member.externalId` | Facultatif | String | Défini comme l’ID externe de Braze, vous pouvez utiliser votre ID externe pour mettre à jour le passe d’adhésion. En définissant ce champ, l’utilisateur est considéré comme unique au sein du programme d’adhésion.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

Pour une liste complète des champs disponibles, leurs types et des descriptions utiles, reportez-vous à la [documentation GitHub de PassKit][10].

#### Exemple de charge utile
{% raw %}
```liquid
{
  "members.member.externalId": "{{${user_id}}}",
  "members.member.points": "100",
  "members.tier.name": "current_customer",
  "person.displayName": "{{${first_name}}} {{${last_name}}}",
  "person.externalId": "{{${user_id}}}",
  "universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"
}
```
{% endraw %}

### Étape 2 : Créer et encoder une variable de charge utile non définie

Créez et nommez un nouveau bloc de contenu en accédant à `Templates & Media` dans le tableau de bord de Braze. Vous y trouverez l’onglet `Content Block Library`. Sélectionnez `Create Content Block` pour commencer.

Ensuite, vous devez définir votre **balise liquide de bloc de contenu**. Après avoir enregistré ce bloc de contenu, cette balise Liquid peut être référencée lors de la composition des messages. Dans cet exemple, nous avons attribué la balise Liquid en tant que {% raw %}`{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %}. 

Dans ce bloc de contenu, nous n’inclurons pas directement la charge utile, mais nous y ferons référence dans une {% raw %}`{{passData}}`{% endraw %} variable. Le premier extrait de code que vous devez ajouter à votre bloc de contenu capture un encodage Base64 de la {% raw %}`{{passData}}`{% endraw %} variable.
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passDatapassData|base64_encode}}{% endcapture %}
```
{% endraw %}

### Étape 3 : Créer votre signature de chiffrement à l’aide d’un hachage HMAC SHA1

Ensuite, vous allez créer votre signature de chiffrement en utilisant un hachage [SHA1 HMAC][16] de l’URL du projet et de la charge utile. 

Le deuxième extrait de code que vous devez ajouter à votre bloc de contenu capture l’URL à utiliser pour le hachage.
{% raw %}
```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```
{% endraw %}

Ensuite, vous devez générer une signature à l’aide de ce hachage et de votre `Project Secret`. Ceci peut être fait en incluant un extrait de code tiers :
{% raw %}
```liquid
{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}
```
{% endraw %}

Enfin, ajoutez la signature à l’URL complète à l’aide du cinquième extrait de code :
{% raw %}
```liquid
{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}{% endcapture %}
```
{% endraw %}

### Étape 4 : Imprimer votre URL

Enfin, assurez-vous d’appeler votre URL finale de manière à ce qu’elle imprime votre URL SmartPass dans votre message.
{% raw %}
```liquid
{{longURL}}
```
{% endraw %}

À ce stade, vous aurez créé un bloc de contenu qui ressemble à ceci :

{% raw %}
```liquid
{% capture base64JsonPayload %}{{passData|base64_encode}}{% endcapture %}

{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}

{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}

{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}&utm_source=braze&utm_campaign={{campaign.${name}}}{% endcapture %}{% capture longURL %}{{longURL | url_encode}}{% endcapture %}

{{longURL}}
```
{% endraw %}

Dans cet exemple, des paramètres UTM ont été ajoutés pour suivre la source de ces installations jusqu’à Braze et cette campagne.

{% alert important %}
N’oubliez pas d’enregistrer votre bloc de contenu avant de quitter la page.
{% endalert %}

### Étape 5 : Tout mettre en place

Une fois que ce bloc de contenu a été généré, il peut être réutilisé à l’avenir. 

Vous remarquerez peut-être que deux variables sont laissées indéfinies dans l’exemple du bloc de contenu.<br> 
{% raw %}`{{passData}}`{% endraw %} - Votre charge utile de données de passe JSON dans l’[étape 1](#passkit-integrations) <br>
{% raw %}`{{projectUrl}}`{% endraw %} - L’URL de votre projet ou programme que vous trouvez sur l’onglet Distribution de votre projet Passkit.

Cette décision était intentionnelle et garantit la réutilisation du bloc de contenu. Étant donné que ces variables sont référencées de manière unique et non créées dans le bloc de contenu, elles peuvent être modifiées sans avoir à refaire le bloc de contenu. 

Par exemple, vous souhaitez peut-être modifier l’offre d’introduction pour inclure plus de points initiaux dans votre programme de fidélité, ou peut-être créer une carte ou un coupon de membre secondaire. Ces scénarios nécessiteraient différents `projectURLs` Passkit ou différentes charges utiles de passe, que vous définiriez par campagne dans Braze.  

#### Composition du corps du message

Vous devrez capturer ces deux variables dans votre corps de message, puis appeler votre bloc de contenu. 
Capturez votre charge utile JSON réduite à partir de l’[étape 1](#passkit-integrations) :

**Attribuez l’URL du projet**
{% raw %}
```liquid
{% assign projectUrl = "https://pub1.pskt.io/c/ww0jir" %}
```
{% endraw %}

**Capturez le JSON**
{% raw %}
```liquid
{% capture passData %}{"members.member.externalId": "{{${user_id}}}","members.member.points": "100","members.tier.name": "current_customer","person.displayName": "{{${first_name}}} {{${last_name}}}","person.externalId": "{{${user_id}}}","universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"}{% endcapture %}
```
{% endraw %}

**Faites référence au bloc de contenu que vous venez de générer**
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

Votre corps de message doit ressembler à ce qui suit :
![Image du compositeur de messages de bloc de contenu avec le JSON capturé et le bloc de contenu indiqué.][1]{: style="max-width:70%"}

L’URL de sortie de l’exemple est :
![L’URL de sortie qui comprend une longue chaîne de lettres et de chiffres générée de façon aléatoire.][2]{: style="max-width:70%"}

L’URL de sortie sera longue. La raison est qu’elle contient toutes les données du passe et qu’elle intègre la meilleure sécurité de sa catégorie pour garantir l’intégrité des données et la protection contre toute modification. Si vous utilisez le SMS pour distribuer cette URL, vous pouvez la faire passer par un processus de raccourcissement de lien tel que [bit.ly][3]. Cela peut se faire par le biais d’un appel de Contenu connecté à un endpoint bit.ly !

## Mettre à jour le passe à l’aide du webhook PassKit

Dans Braze, vous pouvez configurer une campagne de webhook ou un webhook au sein d’un Canvas pour mettre à jour un passe existant en fonction du comportement de votre utilisateur. Consultez les liens suivants pour plus d’informations sur les endpoints utiles de PassKit. 
- [Projets adhésion][12]
- [Projets coupon][13]
- [Projets vols][14]

### Paramètres de la charge utile

Avant de commencer, voici les paramètres courants des charges utiles JSON que vous pouvez inclure dans vos webhooks de création et de mise à jour vers PassKit.

| Data | Type | Description |
| ---- | ---- | ----------- |
| `externalId` | String | Permet d’ajouter un ID unique à l’enregistrement du passe pour assurer la compatibilité avec un système existant utilisant des identifiants uniques de clients (p. ex., des numéros d’adhésion). Vous pouvez récupérer les données du passe en utilisant cet endpoint via `userDefinedId` et `campaignName` au lieu de l’ID du passe. Cette valeur doit être unique dans une campagne et une fois cette valeur définie, elle ne peut pas être modifiée.<br><br>Pour l’intégration à Braze, nous recommandons d’utiliser l’ID externe de Braze : {% raw %}{{${user_id}}}{% endraw %} |
| `campaignId` (coupon) <br><br> `programId` (adhésion) | String | L’ID pour la campagne ou le modèle de programme que vous avez créé dans PassKit. Pour le trouver, accédez à l’onglet **Settings (Paramètres)** de votre projet de passe PassKit. |
| `expiryDate` | Horodatage IO8601 | La date d’expiration du passe. Après la date d’expiration, le passe est automatiquement annulé (voir `isVoided`). Cette valeur remplacera le modèle et la valeur de la date de fin de la campagne. |
| `status` | String | L’état actuel d’un coupon, comme `REDEEMED` ou `UNREDEEMED`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Étape 1 : Créer votre modèle de webhook Braze

Pour créer un modèle de webhook PassKit à utiliser dans les campagnes ou les Canvas, accédez à la section **Templates & Media (Modèles et médias)** dans la plateforme Braze. Si vous souhaitez créer une campagne de webhook PassKit unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d’une nouvelle campagne.

Une fois que vous avez sélectionné le modèle de webhook PassKit, vous affichez les éléments suivants :
- **URL du webhook** : `https://api-pub1.passkit.io/coupon/singleUse/coupon`
- **Corps de la demande** : Texte brut

#### En-têtes et méthode de la requête

PassKit nécessite un `HTTP Header` pour obtenir une autorisation qui inclut la clé d’API PassKit encodée dans la base 64. Les éléments suivants seront déjà inclus dans le modèle comme paire clé-valeur, mais dans l’onglet **Settings (Paramètres)**, vous devez remplacer le `<PASSKIT_LONG_LIVED_TOKEN>` avec votre jeton PassKit. Pour récupérer votre jeton, accédez à votre projet/programme PassKit, allez dans **Settings (Paramètres) > Integrations (Intégrations) > Long Lived Token (Jeton longue durée)**.

{% raw %}
- **Méthode HTTP** : PUT
- **En-tête de requête** :
  - **Autorisation** : Bearer `<PASSKIT_LONG_LIVED_TOKEN>`
  - **Corps de la demande** : application/json
{% endraw %}

#### Corps de la demande

Pour configurer le webhook, renseignez les détails du nouvel événement dans le corps de la demande, y compris les paramètres de la charge utile nécessaires à votre cas d’utilisation :

```json
{% raw %}{
  "externalId": "{{${user_id}}}",
  "campaignId": " 2xa1lRy8dBz4eEElBfmIz8",
  "expiryDate": "2020-05-10T00:00:00Z"
}{% endraw %}
```

### Étape 2 : Prévisualiser votre demande

Votre texte brut indiquera automatiquement s’il s’agit d’une balise Braze. 

Prévisualisez votre demande dans le volet **Preview (Prévisualiser)** ou accédez à l’onglet **Test** où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser votre propre test pour tester votre webhook.

{% alert important %}
N’oubliez pas d’enregistrer votre modèle avant de quitter la page ! <br>Des modèles de webhook mis à jour sont disponibles dans la liste **Saved Webhook Templates (Modèles de webhooks enregistrés)** lorsque vous créez une nouvelle [campagne de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
{% endalert %}

## Récupérer les détails du passe via le Contenu connecté

Outre la création et la mise à jour des passes, vous pouvez également récupérer les métadonnées de vos utilisateurs via le [Contenu connecté][15] de Braze pour incorporer des détails personnalisés du passe dans vos campagnes de communication.

**Appel de contenu connecté PassKit**

{% raw %}
```liquid
{% connected_content  https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer <PASSKIT_LONG_LIVED_TOKEN>","Content-Type": "application/json"} :save passes %}

{{passes.status}} 
```
{% endraw %}

**Exemples de réponses Liquid**

{% tabs local %}
{% tab passes.redemptionDetails %}

```json
{
    "redemptionDate": null,
    "redemptionCode": "",
    "lat": 0,
    "lon": 0,
    "alt": 0,
    "redemptionSource": "",
    "redemptionReference": "",
    "transactionReference": "",
    "transactionAmount": 0
}
```

{% endtab %}
{% tab passes.status %}
```
UNREDEEMED 
```
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/passkit/passkit1.png %}
[2]: {% image_buster /assets/img/passkit/passkit2.png %}
[3]: https://dev.bitly.com/v4/#operation/createFullBitlink
[4]: {% image_buster /assets/img/passkit/passkit4.png %}
[5]: {% image_buster /assets/img/passkit/passkit5.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[7]: {{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint
[8]: https://help.passkit.com/en/articles/3742778-hashed-smartpass-links
[9]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks
[10]: https://github.com/PassKit/smart-pass-link-from-csv-generator
[12]: https://docs.passkit.io/protocols/member/
[13]: https://docs.passkit.io/protocols/coupon/
[14]: https://docs.passkit.io/protocols/boarding/
[15]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/
[16]: https://en.wikipedia.org/wiki/HMAC
