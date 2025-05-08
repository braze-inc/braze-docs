---
nav_title: PassKit
article_title: PassKit
alias: /partners/passkit/
description: "Cet article de référence décrit le partenariat entre Braze et Passkit. Ce partenariat vous permet d'étendre votre portée mobile en intégrant les pass Apple Wallet et Google Pay à l'expérience de vos clients."
page_type: partner
search_tag: Partner

---

# PassKit

> PassKit vous permet d'étendre votre portée mobile en intégrant les pass Apple Wallet et lGoogle Pay à l'expérience de vos clients. Créez, gérez, distribuez et analysez facilement les performances des coupons numériques, des cartes de fidélité, des cartes de membre, des billets et bien plus encore, sans que vos clients aient besoin d'une autre application.

_Cette intégration est maintenue par Passkit._

## À propos de l'intégration

L'intégration de Braze et PassKit vous permet d'augmenter et de mesurer l'engagement de vos campagnes en ligne en fournissant instantanément des passes Apple Wallet et Google Pay personnalisées. Vous pouvez ensuite analyser l'utilisation et effectuer des ajustements en temps réel pour augmenter le trafic en magasin en déclenchant des messages géolocalisés et des mises à jour personnalisées et dynamiques sur le portefeuille mobile de votre client. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte PassKit | Vous devez disposer d'un compte PassKit et d'un gestionnaire de compte PassKit. |
| `userDefinedID` | Pour mettre à jour de manière appropriée les événements personnalisés et les attributs personnalisés destinés à vos utilisateurs entre PassKit et Braze, vous devez définir l'ID externe de Braze comme. `userDefinedID` Ce paramètre `userDefinedID` sera utilisé lors des appels d'API vers les endpoints PassKit. |
| Clé d'API REST Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST Braze  | L'URL de votre endpoint REST. Votre endpoint dépendra de l'URL [Braze] de votre instance. ][6] |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration

Pour enrichir davantage les expériences de portefeuille mobile de vos clients, depuis votre tableau de bord PassKit, vous pouvez choisir de transmettre des données à Braze via le point d'extrémité Braze [`/users/track`][7] . 

Voici des exemples de données à partager à partir de PassKit :
- **Pass créé** : lorsqu'un client clique sur le lien d'un pass et qu'un pass lui est présenté pour la première fois.
- **Installation du pass** : lorsque le client ajoute et enregistre le pass dans son application de portefeuille.
- **Mises à jour du pass** : lorsqu'un pass est mis à jour.
- **Suppression du pass** : lorsqu'un client supprime le pass de son application de portefeuille.

Une fois les données transmises à Braze, vous pouvez créer des audiences, personnaliser le contenu via Liquid et déclencher des campagnes ou des Canvas une fois ces actions effectuées.

## Connectez Passkit à Braze

Pour transmettre des données depuis PassKit, assurez-vous d'avoir défini votre ID externe Braze sur le paramètre `externalId` de PassKit.

1. Dans **Paramètres**, sous **Intégrations** de votre projet ou programme PassKit Pass, cliquez sur **Connect** sous l'onglet **Braze**.<br>![La vignette d'intégration Braze dans la plateforme PassKit.][5]{: style="max-width:80%"}<br><br>
2. Renseignez votre clé API Braze, l'URL de votre endpoint et donnez un nom à votre connecteur.<br><br>
3. **Activez l'intégration** et tous les événements que vous souhaitez dans Braze pour déclencher ou personnaliser vos messages.<br>![La vignette d'intégration PassKit Braze a été étendue pour accepter la clé API, l'URL de l’endpoint, le nom de l'intégration, les paramètres d'activation, les paramètres d'adhésion et les paramètres de pass.][4]{: style="max-width:70%"}

## Créer un pass à l'aide d'un lien SmartPass

Dans Braze, vous pouvez configurer un lien SmartPass pour générer une URL unique permettant à vos clients d'installer leur pass sur Android ou iOS. Pour ce faire, vous devez définir une charge utile de données SmartPass cryptée qui peut être appelée depuis un Braze Content Block. Ce [Bloc de contenu][9] peut ensuite être réutilisé pour de futurs pass et coupons. Les éléments suivants seront utilisés lors de votre intégration :

- **URL de PassKit** : L'URL de votre PassKit est une URL unique pour votre programme PassKit.<br>Chaque programme possède une URL unique, que vous trouverez dans l'onglet **Distribution** de votre programme ou projet PassKit. (par exemple,https://pub1.pskt.io/c/ww0jir)<br><br>
- **Secret PassKit** : Outre l'URL, vous devez disposer de la clé PassKit de ce programme.<br>Elle est disponible sur la même page que l'URL de PassKit.<br><br>
- **ID du programme (ou du projet)** : Votre ID de programme PassKit sera requis pour créer l'URL SmartPass. <br>Vous pouvez le trouver dans l'onglet **Paramètres** de votre projet ou programme.

Pour plus d'informations sur la création de liens SmartPass cryptés, consultez cet article [PassKit]][8]

### Étape 1 : Définissez la charge utile des données de votre pass {#passkit-integrations}

Tout d'abord, vous devez définir le coupon ou la charge utile du membre. 

Vous pouvez inclure de nombreux composants dans votre charge utile, mais voici deux éléments importants à noter :

| Composant | Nécessaire | Type | Description |
| --------- | -------- | ---- | ----------- |
|`person.externalId` | Nécessaire | Chaîne de caractères | Défini comme l'ID externe de Braze, il est crucial pour que les rappels de PassKit à Braze fonctionnent, car il permet aux utilisateurs de Braze d'obtenir des coupons pour plusieurs offres au cours d'une seule campagne. Non imposé car unique. |
| `members.member.externalId` | Facultatif | Chaîne de caractères | Défini comme identifiant externe Braze, vous pouvez utiliser votre identifiant externe pour mettre à jour le pass de membre. La définition de ce champ permet de définir l'utilisateur comme étant unique au sein du programme d'adhésion.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

Pour une liste complète des champs disponibles, leurs types et leurs descriptions, consultez la documentation [PassKit] de GitHub. ][10]

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

### Étape 2 : Création et encodage d'une variable de charge utile non définie

Créez et nommez un nouveau bloc de contenu en accédant à **Modèles** > **Blocs de contenu** dans le tableau de bord de Braze.

Sélectionnez **Créer un bloc de contenu** pour commencer.

Ensuite, vous devez définir votre **balise Liquid de bloc de contenu**. Après avoir enregistré ce bloc de contenu, cette balise Liquid peut être référencée lors de la rédaction de messages. Dans cet exemple, nous avons attribué à la balise Liquid la valeur {% raw %} `{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %}. 

Dans ce bloc de contenu, nous n'inclurons pas directement la charge utile, mais la référencerons dans une variable {% raw %} `{{passData}}` {% endraw %}. Le premier extrait de code que vous devez ajouter à votre bloc de contenu capture un encodage Base64 de la variable {% raw %} `{{passData}}` {% endraw %}.
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passDatapassData|base64_encode}}{% endcapture %}
```
{% endraw %}

### Étape 3 : Créez votre signature de chiffrement à l'aide d'un hachage HMAC SHA1

Vous allez ensuite créer votre signature de chiffrement à l'aide d'un ][16] hachage HMAC [SHA1] de l'URL du projet et de la charge utile. 

Le deuxième extrait de code que vous devez ajouter à votre bloc de contenu capture l'URL à utiliser pour le hachage.
{% raw %}
```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```
{% endraw %}

Ensuite, vous devez générer une signature à l'aide de ce hachage et de votre`Project Secret`. Cela peut être fait en incluant un troisième extrait de code :
{% raw %}
```liquid
{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}
```
{% endraw %}

Enfin, ajoutez la signature à l'URL complète à l'aide du cinquième extrait de code :
{% raw %}
```liquid
{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}{% endcapture %}
```
{% endraw %}

### Étape 4 : Imprimez votre URL

Enfin, assurez-vous d'appeler votre URL finale afin qu'elle imprime votre URL SmartPass dans votre message.
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

Dans cet exemple, des paramètres UTM ont été ajoutés pour suivre la source de ces installations jusqu'à Braze et cette campagne.

{% alert tip %}
N'oubliez pas d'enregistrer votre bloc de contenu avant de quitter la page.
{% endalert %}

### Étape 5 : Assembler tous les éléments

Une fois que ce bloc de contenu a été créé, il peut être réutilisé ultérieurement. 

Vous remarquerez peut-être que deux variables ne sont pas définies dans l'exemple de bloc de contenu.<br> 
{% raw %}`{{passData}}`{% endraw %} - Votre charge utile de données de passe JSON définie à l'[étape 1](#passkit-integrations) <br>
{% raw %}`{{projectUrl}}`{% endraw %} - L'URL de votre projet ou programme que vous trouverez dans l'onglet de distribution de votre projet Passkit.

Cette décision est intentionnelle et favorise la réutilisation du bloc de contenu. Comme ces variables sont uniquement référencées et ne sont pas créées dans le bloc de contenu, elles peuvent être modifiées sans avoir à recréer le bloc de contenu. 

Par exemple, vous souhaitez peut-être modifier l'offre de lancement pour inclure davantage de points initiaux dans votre programme de fidélité, ou peut-être souhaitez-vous créer une carte de membre ou un coupon secondaire. Ces scénarios nécessiteraient différents Passkits `projectURLs` ou différentes charges utiles de pass, que vous définiriez par campagne dans Braze.  

#### Composition du corps du message

Vous devez capturer ces deux variables dans le corps de votre message, puis appeler votre bloc de contenu.
Capturez votre charge utile JSON minifiée à partir de l'[étape 1](#passkit-integrations) :

**Attribuer l'URL du projet**
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

**Faites référence au bloc de contenu que vous venez de créer**
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

Le corps de votre message devrait ressembler à ceci :
![Image du compositeur de messages du bloc de contenu avec le JSON capturé et la référence du bloc de contenu affichée.][1]{: style="max-width:70%"}

L'URL de sortie de l'exemple est la suivante :
![URL de sortie qui inclut une longue chaîne de caractères alphanumériques générée de manière aléatoire.][2]{: style="max-width:70%"}

L'URL de sortie sera longue. La raison en est qu'il contient toutes les données d'accès et intègre une sécurité de premier ordre pour garantir l'intégrité des données et éviter toute modification d'URL. Si vous utilisez un SMS pour diffuser cette URL, vous souhaiterez peut-être l'exécuter via un processus de raccourcissement des liens tel que [bit.ly][3]. Cela peut se faire par le biais d'un appel de contenu connecté à un endpoint bit.ly.

## Mettez à jour le pass à l'aide du webhook PassKit

Dans Braze, vous pouvez configurer une campagne de webhook ou un webhook dans un Canvas pour mettre à jour un pass existant en fonction du comportement de votre utilisateur. Consultez les liens suivants pour obtenir des informations sur les endpoints PassKit utiles. 
- [Projets des membres][12]
- [Projets de coupons][13]
- [Projets de vols][14]

### Paramètres de charge utile

Avant de commencer, voici les paramètres de charge utile JSON courants que vous pouvez inclure dans la création et la mise à jour de webhooks vers PassKit.

| Données | Type | Description |
| ---- | ---- | ----------- |
| `externalId` | Chaîne de caractères | Permet d'ajouter un identifiant unique à la fiche d'accès pour assurer la compatibilité avec un système existant utilisant des identifiants clients uniques (par exemple, des numéros de membre). Vous pouvez récupérer les données de pass en utilisant cet endpoint via `userDefinedId` et `campaignName` à la place de l'ID de pass. Cette valeur doit être unique au sein d'une campagne, et une fois cette valeur définie, elle ne peut pas être modifiée.<br><br>Pour l'intégration de Braze, nous vous recommandons d'utiliser l'ID externe de Braze : {% raw %}`{{${user_id}}}`{% endraw %} |
| `campaignId` (bon de réduction) <br><br> `programId` (adhésion) | Chaîne de caractères | L'ID du modèle de campagne ou de programme que vous avez créé dans PassKit. Pour le trouver, rendez-vous dans l'onglet **Paramètres** de votre projet PassKit Pass. |
| `expiryDate` | Date/heure IO8601 | La date d'expiration du pass. Après la date d'expiration, le pass est automatiquement annulé (voir`isVoided`). Cette valeur remplacera le modèle et la valeur de la date de fin de campagne. |
| `status` | Chaîne de caractères | L'état actuel d'un coupon, tel que `REDEEMED` ou`UNREDEEMED`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Étape 1 : Créez votre modèle de webhook Braze

Pour créer un modèle de webhook PassKit à utiliser dans de futures campagnes ou Canvases, accédez à **la section Modèles et médias du** tableau de bord de Braze. Si vous souhaitez créer une campagne webhook PassKit unique ou utiliser un modèle existant, sélectionnez Webhook **in** Braze lors de la création d'une nouvelle campagne.

Une fois que vous avez sélectionné le modèle de webhook PassKit, vous devriez voir ce qui suit :
- **URL du webhook** : `https://api-pub1.passkit.io/coupon/singleUse/coupon`
- **Corps de la requête** : Texte brut

#### En-têtes de requête et méthode

PassKit requiert un `HTTP Header` pour l'autorisation qui inclut votre clé API PassKit encodée en base 64. Les éléments suivants seront déjà inclus dans le modèle en tant que paire clé-valeur, mais dans l'**onglet** Paramètres, vous devez les remplacer par `<PASSKIT_LONG_LIVED_TOKEN>` votre jeton PassKit. Pour récupérer votre jeton, accédez à votre projet/programme PassKit, puis accédez à **Paramètres > Intégrations > Jeton de longue durée**.

{% raw %}
- **Méthode HTTP**: PUT
- **En-tête de la requête** :
  - **Autorisation**: Porteur `<PASSKIT_LONG_LIVED_TOKEN>`
  - **Content-Type**: application/json
{% endraw %}

#### Corps de la requête

Pour configurer le webhook, renseignez les nouveaux détails de l'événement dans le corps de la requête, y compris les paramètres de charge utiles nécessaires à votre cas d'utilisation :

```json
{% raw %}{
  "externalId": "{{${user_id}}}",
  "campaignId": " 2xa1lRy8dBz4eEElBfmIz8",
  "expiryDate": "2020-05-10T00:00:00Z"
}{% endraw %}
```

### Étape 2 : Prévisualiser la requête

Votre texte brut sera automatiquement mis en évidence s'il s'agit d'une balise Braze applicable. 

Prévisualisez votre requête dans le panneau **Aperçu** ou accédez à l'onglet **Test**, où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser le vôtre pour tester votre webhook.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page ! <br>Les modèles de webhook mis à jour se trouvent dans la liste **Modèles de webhook enregistrés** lors de la création d'une nouvelle [campagne webhook.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)
{% endalert %}

## Récupérez les détails du pass via du contenu connecté

Outre la création et la mise à jour des laissez-passer, vous pouvez également récupérer les métadonnées des laissez-passer de vos utilisateurs via Braze [Connected Content][15] ] afin d'incorporer les détails des laissez-passer personnalisés dans vos campagnes d'envoi de messages.

**Appel de contenu connecté PassKit**

{% raw %}
```liquid
{% connected_content  https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer <PASSKIT_LONG_LIVED_TOKEN>","Content-Type": "application/json"} :save passes %}

{{passes.status}} 
```
{% endraw %}

**Exemples de réponses Liquid**

{% tabs local %}
{% tab passes redemptionDetails %}

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
{% tab passe le statut %}
```
UNREDEEMED 
```
{% endtab %}
{% endtabs %}


[1]: {% image_buster /assets/img/passkit/passkit1.png %}
[2]: {% image_buster /assets/img/passkit/passkit2.png %}
Il y a [3]: https://dev.bitly.com/v4/#operation/createFullBitlink
[4]: {% image_buster /assets/img/passkit/passkit4.png %}
[5]: {% image_buster /assets/img/passkit/passkit5.png %}
[6]: {{site.baseurl}}/api/basics/#endpoints
[7]: {{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint
[8]: https://help.passkit.com/en/articles/3742778-hashed-smartpass-links
[9]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks
[10]: https://github.com/PassKit/smart-pass-link-from-csv-generator
Il y a [12]: https://docs.passkit.io/protocols/member/
Il y a [13]: https://docs.passkit.io/protocols/coupon/
[14]: https://docs.passkit.io/protocols/boarding/
[15]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/
[16]: https://en.wikipedia.org/wiki/HMAC
