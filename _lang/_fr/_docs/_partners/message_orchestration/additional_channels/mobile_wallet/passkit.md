---
nav_title: PassKit
article_title: PassKit
alias: /fr/partners/passkit/
description: "Cet article décrit le partenariat entre Braze et Passkit. Ce partenariat vous permet d'étendre votre portée mobile en intégrant les passes Apple Wallet et Google Pay à l'expérience de votre client."
page_type: partenaire
search_tag: Partenaire
---

# PassKit

> PassKit vous permet d’étendre votre portée mobile en intégrant Apple Wallet, et Google Pay passe à l’expérience de votre client. Créez, gérez, distribuez et analysez facilement les performances des coupons numériques, des cartes de fidélité, des cartes de membre, des billets et bien plus encore; sans que vos clients aient besoin d'une autre application.

L’intégration de Braze et PassKit vous permet d’augmenter et de mesurer l’engagement de vos campagnes en ligne en fournissant instantanément des passes personnalisées Apple Wallet et Google Pay. Vous pouvez ensuite analyser votre utilisation et effectuer des ajustements en temps réel pour augmenter le trafic en magasin en déclenchant des messages basés sur la localisation et en personnalisant, mises à jour dynamiques du portefeuille mobile de votre client.


## Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                                                                                                              |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte PassKit                  | Vous devrez avoir un compte PassKit et un gestionnaire de compte PassKit.                                                                                                                                                                                                                            |
| `ID utilisateur`                | Pour mettre à jour correctement les événements personnalisés et les attributs personnalisés à vos utilisateurs entre PassKit et Braze, vous devrez définir l'ID externe Braze comme le `userDefinedID`. Cet `userDefinedID` sera utilisé lors des appels API vers les points de terminaison PassKit. |
| Braze clé API REST              | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le **tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API**                                                                                         |
| Point de terminaison REST Braze | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance][6].                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

Pour enrichir davantage les expériences de portefeuille mobile de vos clients, à partir de votre tableau de bord PassKit, vous pouvez choisir de passer des données à Braze à travers le [point de terminaison de Braze/piste][7].

Des exemples de données à partager à partir de PassKit comprennent:
- **Mot de passe créé**: lorsqu'un client clique sur un lien de passe et apparaît d'abord un mot de passe.
- **Le mot de passe installe**: lorsque le client ajoute et enregistre le mot de passe dans l'application de son portefeuille.
- **Passer mise à jour**: quand un passe est mis à jour.
- **Pass delete**: lorsqu'un client supprime le pass de son application portefeuille.

Une fois que les données sont transmises au Brésil, vous pouvez créer des audiences, personnaliser du contenu via Liquid, et déclencher des campagnes ou des Cavanses une fois que ces actions ont été effectuées.

## Connectez Passkit à Braze

Pour passer les données de PassKit, veuillez vous assurer que vous avez défini votre ID externe Braze comme un `externalId` de PassKit.

1. Dans **Paramètres**, sous **Intégrations** dans votre projet de passes PassKit ou votre programme cliquez sur **Connectez** sous l'onglet **Braze** .<br>!\[Settings Button\]\[5\]{: style="max-width:80%"}<br><br>
2. Remplissez votre clé API Braze, votre URL de terminaison et fournissez un nom pour votre connecteur.<br><br>
3. Activer/désactiver **Activer l'intégration** et quels que soient les événements que vous voulez dans Braze pour déclencher ou personnaliser vos messages.<br>!\[Connect to Braze\]\[4\]{: style="max-width:70%"}

## Créer une passe en utilisant un lien SmartPass

À l'intérieur du Brésil, vous pouvez configurer un lien SmartPass pour générer une URL unique pour que vos clients installent leur passe sur Android ou iOS. Pour ce faire, vous devez définir une charge utile de données SmartPass chiffrée qui peut être appelée à partir d'un bloc de contenu Braze. Ce [bloc de contenu][9] peut ensuite être réutilisé pour les passes et bons de réduction futurs. Les éléments suivants seront utilisés lors de votre intégration :

- **URL PassKit**: Votre URL PassKit est une URL unique pour votre programme PassKit.<br>Chaque programme a une URL unique, et vous pouvez le trouver dans l'onglet **Distribution** de votre programme ou projet PassKit. (par exemple, https://pub1.pskt.io/c/ww0jir)<br><br>
- **PassKit secret**: En plus de l'URL, vous aurez besoin de la clé PassKit pour ce programme pratique.<br>Ceci peut être trouvé sur la même page que votre URL PassKit.<br><br>
- **ID du programme (ou du projet)**: Votre identifiant de programme PassKit sera requis pour créer l'URL SmartPass. <br>Vous pouvez le trouver dans l'onglet **Paramètres** de votre projet ou programme.

Pour plus d'informations sur la création de liens SmartPass chiffrés, consultez cet article [PassKit][8].

### Étape 1 : Définir la charge utile de vos données de passe {#passkit-integrations}

Tout d'abord, vous devez définir le coupon ou la charge utile du membre.

Il y a beaucoup de composants différents que vous pouvez inclure dans votre charge utile, mais ici comme deux éléments importants à noter:

| Composant        | Requis    | Type de texte        | Libellé                                                                                                                                                                                                                                                     |
| ---------------- | --------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ID externe`     | Requis    | Chaîne de caractères | Définir comme ID externe de Braze, c'est crucial pour que les callbacks de PassKit de retour à Braze fonctionnent, permettant aux utilisateurs de Braze d'avoir des coupons pour de multiples offres en une seule campagne. Non appliqué en tant qu'unique. |
| `Membre externe` | Optionnel | Chaîne de caractères | Définir comme ID externe de Braze, vous pouvez utiliser votre ID externe pour mettre à jour la passe d'abonnement. Définir ce champ impose à l'utilisateur comme unique dans le programme d'adhésion.                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

Pour une liste complète des champs disponibles, leurs types et leurs descriptions utiles, jetez un œil à la documentation [PassKit Github][10].

#### Exemple de charge utile
{% raw %}
```liquid
{
  "members.member.externalId": "{{${user_id}}}",
  "members.member.points": "100",
  "members.tier.name": "current_customer",
  "personne. isplayName": "{{${first_name}}} {{${last_name}}}",
  "person.externalId": "{{${user_id}}}",
  "universal. xpiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"
}
```
{% endraw %}

### Étape 2 : Créer et encoder une variable de charge utile non définie

Créez et nommez un nouveau bloc de contenu en naviguant vers `Modèles & Médias` dans le tableau de bord Braze. Ici vous pouvez trouver l’onglet `Bibliothèque de blocs de contenu`. Sélectionnez `Créer un bloc de contenu` pour commencer.

Ensuite, vous devez définir votre **Content Block Liquid Tag**. Après avoir enregistré ce bloc de contenu, cette balise Liquid peut être référencée lors de la rédaction de messages. Dans cet exemple, nous avons assigné la balise Liquid comme {% raw %}`{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %}.

Dans ce bloc de contenu, nous n'inclurons pas directement le bloc écrit ci-dessus, mais le référencerons dans une variable {% raw %}`{{passData}}`{% endraw %}. Le premier extrait de code que vous devez ajouter à votre bloc de contenu capture un encodage Base64 de la variable {% raw %}`{{passData}}`{% endraw %}.
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passdata|base64_encode}}{% endcapture %}
```
{% endraw %}

### Étape 3 : Créez votre signature de chiffrement à l'aide d'un hachage HMAC SHA1

Ensuite, vous allez créer votre signature de chiffrement à l'aide d'un hachage [SHA1 HMAC][16] de l'URL du projet et de la charge utile.

Le deuxième extrait de code que vous devez ajouter à votre bloc de contenu capture l'URL à utiliser pour le hachage.
{% raw %}
```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```
{% endraw %}

Ensuite, vous devez générer une signature en utilisant ce hachage et votre `Secret du projet`. Cela peut être fait en incluant un troisième extrait de code, affiché ci-dessous.
{% raw %}
```liquid
{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}
```
{% endraw %}

Enfin, ajoutez la signature à l'URL complète en utilisant le cinquième extrait de code, affiché ci-dessous.
{% raw %}
```liquid
{% capture longUrl %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}{% endcapture %}
```
{% endraw %}

### Étape 4 : Imprimer votre URL

Enfin, assurez-vous d'appeler votre URL finale pour qu'elle imprime votre URL SmartPass dans votre message.
{% raw %}
```liquid
{{longURL}}
```
{% endraw %}

À ce stade, vous aurez créé un bloc de contenu qui ressemble à ceci :

{% raw %}
```liquid
{% capture base64JsonPayload %}{{passdata|base64_encode}}{% endcapture %}

{% capture url %}{{projectUrl}}? ata={{base64JsonPayload}}{% endcapture %}

{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}

{% capture longUrl %}{{projectUrl}}? ata={{base64JsonPayload}}&sig={{sig}}&utm_source=braze&utm_campaign={{campaign.${name}}}{% endcapture %}{% capture longUrl %}{{longUrl | url_encode}}{% endcapture %}

{{longURL}}
```
{% endraw %}

Dans cet exemple, des paramètres UTM ont été ajoutés pour retracer la source de ces installations à Braze et cette campagne.

{% alert important %}
N'oubliez pas d'enregistrer votre bloc de contenu avant de quitter la page.
{% endalert %}

### Étape 5 : Mettre tout ensemble

Une fois ce bloc de contenu créé, il peut être réutilisé à l'avenir.

Vous pouvez remarquer qu'il reste deux variables indéfinies dans le bloc de contenu ci-dessus.<br>
{% raw %}`{{passData}}`{% endraw %} - Votre bloc de données JSON passe défini à [étape 1](#passkit-integrations) <br>
{% raw %}`{{projectUrl}}`{% endraw %} - L'URL de votre projet ou programme que vous trouvez sur l'onglet de distribution de votre projet Passkit.

Cette décision était intentionnelle et assure la réutilisabilité du bloc de contenu. Comme ces variables sont seulement référencées, non créées dans le bloc de contenu, ces variables peuvent changer sans refaire le bloc de contenu.

Par exemple, peut-être souhaiteriez-vous modifier l'offre d'introduction pour inclure plus de points initiaux dans votre programme de fidélisation, ou peut-être voulez-vous créer une carte de membre secondaire ou un bon de réduction. Ces scénarios nécessiteraient des `URLs de projet Passkit différentes` ou des blocs de passes différents, que vous définiriez par campagne au Brésil.

#### Composer le corps du message

Vous voudrez capturer ces deux variables dans le corps de votre message puis appeler votre bloc de contenu. Capturez votre bloc JSON minifié depuis l'étape [1](#passkit-integrations) ci-dessus :

**Assigner l'URL du projet**
{% raw %}
```liquid
{% assigner projectUrl = "https://pub1.pskt.io/c/ww0jir" %}
```
{% endraw %}

**Capturer le JSON**
{% raw %}
```liquid
{% capture passData %}{"members.member.externalId": "{{${user_id}}}","members.member.points": "100","members.tier.name": "current_customer","person.displayName": "{{${first_name}}} {{${last_name}}}","personne. xternalId": "{{${user_id}}}","universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"}{% endcapture %}
```
{% endraw %}

**Référez le bloc de contenu que vous venez de créer**
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

Le corps de votre message devrait ressembler à ceci : !\[Message Body\]\[1\]{: style="max-width:70%"}

L'URL de sortie pour l'exemple ci-dessus est : !\[URL de sortie\]\[2\]{: style="max-width:70%"}

L'URL de sortie ci-dessus sera longue. La raison en est qu'il contient toutes les données de passe et intègre la meilleure sécurité de la classe pour assurer l'intégrité des données et ne pas les tremper par la modification d'URL. Si vous utilisez des SMS pour distribuer cette URL, vous pouvez l'exécuter à travers un processus de raccourcissement de lien tel que [bit.ly][3]. Cela peut être fait par le biais d'un appel de contenu connecté à un point de terminaison bit.ly !

## Passer à la mise à jour en utilisant le webhook PassKit

Au sein de Braze, vous pouvez mettre en place une campagne de webhook ou un webhook dans un Canvas pour mettre à jour une passe existante en fonction du comportement de votre utilisateur. Consultez les liens ci-dessous pour obtenir des informations sur les points de terminaison PassKit utiles.
- [Projets membres][12]
- [Projets Coupon][13]
- [Projets de vols][14]

### Paramètres de charge utile

Avant de commencer, voici les paramètres de charge utile JSON que vous pouvez inclure dans votre création et mise à jour des webhooks vers PassKit.

| Donnée                                                            | Type de texte        | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `externalId`                                                      | Chaîne de caractères | Permet d'ajouter un identifiant unique à l'enregistrement de passe pour assurer la compatibilité avec un système existant en utilisant des identifiants clients uniques (par exemple, les numéros de membre). Vous pouvez récupérer des données de passe en utilisant ce point de terminaison via `userDefinedId` et `campaignName` au lieu de pass ID. Cette valeur doit être unique dans une campagne, et une fois cette valeur définie, elle ne peut pas être modifiée.<br><br>Pour l'intégration de Braze, nous vous recommandons d'utiliser l'ID externe de Braze : {% raw %}{{${user_id}}}{% endraw %} |
| `campaignId` (coupon) <br><br> `programId` (adhésion) | Chaîne de caractères | L'ID de la campagne ou du modèle de programme que vous avez créé dans PassKit. Pour trouver cela, allez dans l'onglet **Paramètres** de votre projet PassKit .                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `expiryDate`                                                      | IO8601 datetime      | La date d'expiration du mot de passe. Après la date d'expiration, le pass est automatiquement annulé (voir `isVoided`). Cette valeur remplacera le modèle et la date de fin de la campagne.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `statuts`                                                         | Chaîne de caractères | Le statut actuel d'un coupon, tel que `REDEEMED` ou `UNREDEEMED`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Étape 1 : Créez votre modèle de webhook Braze

Créer un modèle de webhook PassKit à utiliser dans de futures campagnes ou Canvases, accédez à la section **Modèles & Médias** de la plateforme Braze. Si vous souhaitez créer une campagne de webhook PassKit unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d'une nouvelle campagne.

Une fois que vous avez sélectionné le modèle de webhook PassKit, vous devriez voir ce qui suit :
- **URL du Webhook**: `https://api-pub1.passkit.io/coupon/singleUse/coupon`
- **Corps de la requête**: Texte brut

#### En-têtes de requête et méthode

PassKit nécessite un `en-tête HTTP` pour être autorisé qui inclut votre clé API PassKit encodée en base 64. Les éléments suivants seront déjà inclus dans le modèle en tant que paire clé-valeur, mais dans l'onglet **Paramètres** , vous devez remplacer le `<PASSKIT_LONG_LIVED_TOKEN>` par votre jeton PassKit. Pour récupérer votre jeton, accédez à votre projet/programme PassKit, accédez à **Paramètres > Intégrations > Jeton à vie longue**.

{% raw %}
- **Méthode HTTP**: PUT
- **En-tête de la requête**:
  - **Autorisation**: Porteur `<PASSKIT_LONG_LIVED_TOKEN>`
  - **Corps de la requête**: application/json
{% endraw %}

#### Corps de la requête

Pour configurer le webhook, remplissez les nouveaux détails de l'événement dans le corps de la requête, y compris les paramètres de charge utile nécessaires pour votre cas d'utilisation :

```json
{% raw %}{
  “externalId”: “{{${user_id}}}”,
  “campaignId”: “ 2xa1lRy8dBz4eEElBfmIz8”,
  “expiryDate”: “2020-05-10T00:00:00Z”
}{% endraw %}
```

### Étape 2 : Aperçu de votre demande

Votre texte brut sera automatiquement mis en surbrillance s'il s'agit d'une balise Braze applicable.

Prévisualisez votre demande dans le panneau de gauche ou accédez à l’onglet `Test` où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant, ou personnaliser le vôtre pour tester votre webhook.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page! <br>Les modèles de webhook mis à jour peuvent être trouvés dans la liste **Modèles de Webhook enregistrés** lors de la création d'une nouvelle [campagne webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

## Récupérer les détails de passe via le contenu connecté

En plus de la création et de la mise à jour des passes, vous pouvez également récupérer les métadonnées de passe de vos utilisateurs via le [Contenu connecté][15] de Braze pour incorporer des détails de passes personnalisés dans vos campagnes de messagerie.

**Appel de contenu PassKit connecté**

{% raw %}
```liquid
{% connected_content https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer <PASSKIT_LONG_LIVED_TOKEN>","Content-Type": "application/json"} :save passes %}

{{passes.status}} 
```
{% endraw %}

**Exemples de réponses liquides**

{% tabs local %}
{% tab {{passes.redemptionDetails}} %}

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
{% tab {{passes.status}} %}
```
NON REDÉCOULÉ 
```
{% endtab %}
{% endtabs %}
[1]: {% image_buster /assets/img/passkit/passkit1.png %} [2]: {% image_buster /assets/img/passkit/passkit2. ng %} [4]: {% image_buster /assets/img/passkit/passkit4.png %} [5]: {% image_buster /assets/img/passkit/passkit5.png %}

[3]: https://dev.bitly.com/v4/#operation/createFullBitlink
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