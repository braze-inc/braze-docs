---
nav_title: PassKit
article_title: PassKit
alias: /fr/partners/passkit/
description: "Cet article décrit le partenariat entre Braze et Passkit. Ce partenariat vous permet d’étendre votre portée mobile en intégrant les passes Apple Wallet et Google Pay à l’expérience de vos clients."
page_type: partenaire
search_tag: Partenaire
---

# PassKit

> PassKit vous permet d’étendre votre portée mobile en intégrant les passes Apple Wallet et Google Pay à l’expérience de votre client. Créez, gérez, distribuez et analysez facilement les performances des coupons numériques, des cartes de fidélité, des cartes de membre, des billets et bien plus encore; sans que vos clients aient besoin d'une autre application.

Offrez une connexion transparente et connectée en ligne aux expériences des clients hors ligne avec Braze et PassKit. Augmentez et mesurez l'engagement de vos campagnes en ligne en fournissant instantanément des passes Apple Wallet et Google Pay. Analyser l'utilisation et effectuer des ajustements en temps réel pour augmenter le trafic en magasin en déclenchant des messages basés sur la localisation et des mises à jour personnalisées et dynamiques du portefeuille mobile de votre client.

## Pré-requis

| Exigences                            | Origine | Libellé                                                                                                                                                                                                                                                                                       |
| ------------------------------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte PassKit                       | PassKit | Vous devrez avoir un compte PassKit et un gestionnaire de compte PassKit.                                                                                                                                                                                                                     |
| ID utilisateur                       | Client  | Pour mettre à jour correctement les événements personnalisés et les attributs personnalisés à vos utilisateurs entre PassKit et Braze, vous devrez définir l'ID externe Braze comme userDefinedID. Cet userDefinedID sera utilisé lors des appels API vers les points de terminaison PassKit. |
| Clé API Braze                        | Brasero | Vous devrez créer une nouvelle clé d'API.<br><br>Ceci peut être créé dans la __Console Développeur -> Paramètres API -> Créer une nouvelle clé API__ avec __utilisateurs. permissions__ de rack.                                                                                  |
| [Point de terminaison REST Braze][6] | Brasero | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL de Braze pour votre instance.                                                                                                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration de l'API

Pour enrichir davantage les expériences de portefeuille mobile de vos clients, à partir de votre tableau de bord PassKit, vous pouvez choisir de passer des données à Braze à travers le [point d'extrémité][7] de Braze.

Des exemples de données à partager à partir de PassKit comprennent:
- __Passe Créé__: lorsqu'un client clique sur un lien de passe et apparaît d'abord un mot de passe.
- __Pass Installe__: lorsque le client ajoute/enregistre le passe dans l'application de son portefeuille.
- __Mises à jour de passe__: lorsqu'une passe est mise à jour.
- __Pass Delete__: lorsqu'un client supprime le passe de l'application de son portefeuille.

Une fois que les données sont transmises au Brésil, vous pouvez créer des audiences, personnaliser du contenu via Liquid, et déclencher des campagnes ou des Cavanses une fois que ces actions ont été effectuées.

### Connectez Passkit à Braze

Pour passer les données de PassKit, assurez-vous que vous avez défini votre ID externe Braze comme ID externe de PassKit.

1. Dans les paramètres, sous Intégrations dans votre projet PassKit Pass ou Programme cliquez sur Se connecter sous l'onglet Braze.<br>!\[Bouton Paramètres\]\[5\]{: style="max-width:60%"}
2. Remplissez votre clé API Braze, URL de terminal, et fournissez un nom pour votre connecteur.
3. Activer/désactiver l’intégration, et quels que soient les événements que vous voulez dans Braze pour déclencher ou personnaliser vos messages.<br>!\[Connect to Braze\]\[4\]{: style="max-width:50%"}

## Créer une passe en utilisant un lien SmartPass

Au sein de Braze, vous pouvez configurer un lien SmartPass pour générer une URL unique pour que vos clients installent leur passe sur Android ou iOS.

### Pré-requis

| Exigences                          | Origine | Libellé                                                                                                                                                                                                                  | Exemple                       |
| ---------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| __PassKit URL__                    | PassKit | Votre URL PassKit est une URL unique pour votre programme Passkit.  <br><br>Chaque programme a une URL unique, et vous pouvez la trouver sous l'onglet __Distribution__ de votre programme PassKit / projet. | https://pub1.pskt.io/c/ww0jir |
| __Secret PassKit__                 | PassKit | En plus de l'URL, vous aurez besoin de la clé PassKit pour ce programme pratique.  <br><br>Ceci peut être trouvé sur la même page que votre URL PassKit.                                                     | 5AuNonZoFHejGXmHNATz4l        |
| __ID du programme (ou du projet)__ | PassKit | Votre identifiant de programme PassKit sera requis pour créer l'URL SmartPass. <br><br>Vous pouvez le trouver dans l'onglet __Paramètres__ de votre projet ou programme.                                     | 1x3j9vWjSGx2UwUblYlcue        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### Intégrations PassKit

Pour plus d'informations sur la création de liens SmartPass chiffrés, consultez cet [Article PassKit][8].

Pour commencer à créer une URL SmartPass, vous devez créer ce chiffrement dans un [bloc de contenu Braze][9]. La création de cette façon vous permettra de réutiliser le bloc pour les passes et bons de réduction futurs.

#### Étape 1 : Définir la charge utile de vos données de passe
Tout d'abord, vous devez définir le coupon ou la charge utile du membre.

Il y a beaucoup de composants différents que vous pouvez inclure dans votre charge utile, mais ici comme deux éléments importants à noter:

| Composant                  | Requis    | Type de texte        | Libellé                                                                                                                                                                                                                                                     |
| -------------------------- | --------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ID externe`               | Requis    | Chaîne de caractères | Définir comme ID externe de Braze, c'est crucial pour que les callbacks de PassKit de retour à Braze fonctionnent, permettant aux utilisateurs de Braze d'avoir des coupons pour de multiples offres en une seule campagne. Non appliqué en tant qu'unique. |
| `membre.membre.id externe` | Optionnel | Chaîne de caractères | Définir comme ID externe de Braze, vous pouvez utiliser votre ID externe pour mettre à jour la passe d'abonnement. Définir ce champ impose à l'utilisateur comme unique dans le programme d'adhésion.                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

Pour une liste complète des champs disponibles, leurs types et leurs descriptions utiles, jetez un coup d'œil à la [documentation sur le Github PassKit][10].

Exemple de charge utile
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

#### Étape 2 : Créer et encoder une variable de charge utile non définie

Premièrement, créez et nommez un nouveau bloc de contenu en naviguant vers `Modèles & Médias` dans le tableau de bord de Braze. Ici vous pouvez trouver l’onglet de la bibliothèque de blocs de contenu, sélectionnez `Créer un bloc de contenu` pour commencer.

Ensuite, vous devez définir votre __Content Block Liquid Tag__. Après avoir enregistré ce bloc de contenu, cette balise Liquid peut maintenant être référencée lors de la rédaction de messages. Dans cet exemple, nous avons assigné la balise Liquid comme {% raw %}`{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %}.

Dans ce bloc de contenu, nous n'inclurons pas directement le bloc écrit ci-dessus, mais le référencerons dans une variable {% raw %}`{{passData}}`{% endraw %}. Le premier extrait de code que vous devez ajouter à votre bloc de contenu capture un encodage Base64 de la variable {% raw %}`{{passData}}`{% endraw %}.
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passdata|base64_encode}}{% endcapture %}
```
{% endraw %}

#### Étape 3 : Créez votre signature de chiffrement à l'aide d'un hachage HMAC SHA1

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

#### Étape 4 : Imprimer votre URL

Enfin, assurez-vous d'appeler votre URL finale pour qu'elle imprime votre URL SmartPass dans votre message.
{% raw %}
```liquid
{{longURL}}
```
{% endraw %}

À ce stade, tu auras créé un bloc de contenu qui ressemble à ceci :

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
N'oubliez pas d'enregistrer votre bloc de contenu avant de quitter la page!
{% endalert %}

#### Étape 5 : Mettre tout ensemble

Une fois ce bloc de contenu réalisé, il peut être réutilisé à l'avenir.

Vous pouvez remarquer qu'il reste deux variables indéfinies dans le bloc de contenu ci-dessus.<br>
{% raw %}`{{passData}}`{% endraw %} - Votre bloc de données JSON passe défini à [étape 1](#passkit-integrations) <br>
{% raw %}`{{projectUrl}}`{% endraw %} - L'URL de votre projet ou programme que vous trouvez sur l'onglet de distribution de votre projet Passkit.

Cette décision était résolue et assure la réutilisabilité du bloc de contenu. Comme ces variables sont seulement référencées, non créées dans le bloc de contenu, il permet à ces variables de changer sans refaire le bloc de contenu.

Par exemple, peut-être souhaiteriez-vous modifier l'offre d'introduction pour inclure plus de points initiaux dans votre programme de fidélisation, ou peut-être voulez-vous créer une carte de membre secondaire ou un bon de réduction. Ces scénarios nécessiteraient des URL de projet Passkit différentes ou une charge utile différente que vous définiriez par campagne au Brésil.

### Composer le corps du message

Dans le corps de votre message, vous voudrez capturer ces deux variables puis appeler votre bloc de contenu. Capturez votre bloc JSON minifié depuis l'étape [1](#passkit-integrations) ci-dessus :

__1.__ Assigner l'URL du projet
{% raw %}
```liquid
{% assigner projectUrl = "https://pub1.pskt.io/c/ww0jir" %}
```
{% endraw %}

__2.__ Capturez le JSON créé à l'étape 1.
{% raw %}
```liquid
{% capture passData %}{"members.member.externalId": "{{${user_id}}}","members.member.points": "100","members.tier.name": "current_customer","person.displayName": "{{${first_name}}} {{${last_name}}}","personne. xternalId": "{{${user_id}}}","universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"}{% endcapture %}
```
{% endraw %}

__3.__ Référez le bloc de contenu que vous venez de faire.
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

Votre Corps de Message devrait ressembler à ceci : !\[Corps de Message\]\[1\]{: style="max-width:70%"}

L'URL de sortie pour l'exemple ci-dessus est : !\[URL de sortie\]\[2\]{: style="max-width:70%"}

Cela n’a pas l’air long ? La raison en est qu'il contient toutes les données de passage, en plus de l'incorporer le mieux dans la sécurité de la classe pour assurer l'intégrité des données et pas de trempage par la modification d'URL. Si vous utilisez des SMS pour distribuer cette URL, vous pouvez l'exécuter à travers un processus de raccourcissement de lien tel que [bit.ly][3]. Cela peut être fait par le biais d'un appel de contenu connecté à un point de terminaison bit.ly !

## Passer à la mise à jour en utilisant le webhook PassKit

Au sein de Braze, vous pouvez configurer une campagne de webhook ou un webhook dans un Canvas pour mettre à jour une passe existante en fonction du comportement de votre utilisateur. Consultez les liens ci-dessous pour obtenir des informations sur les points de terminaison PassKit utiles.
- [Projets membres][12]
- [Projets promotionnels][13]
- [Projets de vols][14]

### Pré-requis
Avant de commencer, voici les paramètres JSON Payload que vous pouvez inclure dans vos webhooks de création et de mise à jour de PassKit.

| Donnée                                                            | Type de texte        | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `externalId`                                                      | Chaîne de caractères | Cela permet d'ajouter un Id unique à l'enregistrement de passe qui peut fournir une compatibilité avec un système existant en utilisant des identifiants clients uniques (e. . - numéros d’adhésion). Vous pouvez récupérer des données de passe en utilisant ce point de terminaison via userDefinedId et campaignName au lieu de pass ID. Cette valeur doit être unique dans une campagne, et une fois cette valeur définie, elle ne peut pas être modifiée.<br><br>Pour l'intégration de Braze, nous vous recommandons d'utiliser l'ID externe de Braze : {% raw %}{{${user_id}}}{% endraw %} |
| `campaignId` (coupon) <br><br> `programId` (adhésion) | Chaîne de caractères | Ceci est l'ID du modèle de campagne/programme que vous avez créé dans PassKit. Pour trouver cela, allez dans l'onglet __Paramètres__ de votre projet PassKit .                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `expiryDate`                                                      | IO8601 DateTime      | Il s'agit de la date d'expiration du mot de passe. Après la date d'expiration, la passe est automatiquement annulée (voir isVoided). Cette valeur remplacera le modèle et la date de fin de la campagne.                                                                                                                                                                                                                                                                                                                                                                                                     |
| `statuts`                                                         | Chaîne de caractères | Il s’agit du statut actuel d’un coupon, tel que « REDEEMED » ou « UNREDEEMED ».                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Intégration de Webhook

#### Étape 1 : Créer un modèle de webhook dans Braze

Vous pouvez créer ceci à partir de la section `Modèles & Médias` ou créer une nouvelle campagne de webhook ou Canvas au Brésil. Ensuite, sélectionnez le modèle de webhook PassKit - Update Pass, vous devriez voir ce qui suit dans le compositeur :

__URL Webhook__ (Composer Tab) : https://api-pub1.passkit.io/coupon/singleUse/coupon<br> __Corps de requête__ (Onglet composé) : application/json<br> __Méthode HTTP__ (Onglet Paramètres) : PUT

#### Étape 2 : Remplissez votre modèle
Pour configurer le webhook, remplissez les détails du nouvel événement dans le corps de la requête :
{% raw %}
```liquid
{
  “externalId”: “{{${user_id}}}”,
  “campaignId”: “ 2xa1lRy8dBz4eEElBfmIz8”,
  “expiryDate”: “2020-05-10T00:00:00Z”
}
```
{% endraw %}

#### Étape 3: Remplissez les en-têtes de votre requête

| En-tête HTTP    | Définition                                 |
| --------------- | ------------------------------------------ |
| Autorisation    | Porteur [INSERT_YOUR_LONG_LIVED_TOKEN] |
| Type de contenu | application/json                           |
{: .reset-td-br-1 .reset-td-br-2}

Assurez-vous que votre `méthode HTTP` est définie à **PUT**.

__Récupérez votre jeton PassKit Long Lived Token__<br> Pour récupérer votre jeton, accédez à votre projet/programme PassKit dans le compte Admit de PassKit. De là, allez dans Integrations dans Settings, et sélectionnez "Love Lived Integration Token" dans la barre latérale de gauche. Ici, vous trouvez votre jeton de longue durée.

#### Étape 4 : Aperçu de votre demande

Vous verrez que votre texte brut met automatiquement en évidence s'il s'agit d'une balise Braze applicable.

Vous pouvez prévisualiser votre demande dans le panneau de gauche ou accéder à l’onglet `Test` où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant, ou personnaliser le vôtre pour tester votre webhook.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page!
{% endalert %}

## Récupérer les détails de passe via le contenu connecté

En plus de la création et de la mise à jour des passes, vous pouvez également récupérer les métadonnées de votre passe utilisateur via le Contenu connecté de Braze afin d’incorporer des détails de passes personnalisés dans vos campagnes de messagerie. Pour plus d'informations sur la façon d'exécuter des appels de contenu connecté, consultez notre [documentation][15].

__Appel de contenu PassKit connecté__

{% raw %}
```liquid
{% connected_content https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer [INSERT_YOUR_LONG_LIVED_TOKEN]","Content-Type": "application/json"} :save passes %}

{{passes.status}} 
```
{% endraw %}

__Exemple de réponses liquides :__

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
