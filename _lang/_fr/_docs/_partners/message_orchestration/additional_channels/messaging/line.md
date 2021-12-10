---
nav_title: Lignes
article_title: Lignes
alias: /fr/partners/line/
description: "Cet article décrit le partenariat entre Braze et Line, l'une des plateformes de messagerie instantanée les plus populaires au monde."
page_type: partenaire
search_tag: Partenaire
---

# Lignes

> [La ligne](https://line.me/en/) est l'une des plateformes de messagerie instantanée les plus populaires au monde, utilisée par des centaines de millions d'utilisateurs actifs mensuels. Grâce à cette plate-forme, les marques peuvent communiquer avec leurs clients avec des messages riches et bidirectionnels.

L'intégration de la ligne et de Braze vous permet d'exploiter les webhooks de Braze, la segmentation avancée, la personnalisation, et des fonctionnalités de déclenchement pour envoyer des messages à vos utilisateurs en ligne via l'API de messagerie en ligne [](https://developers.line.biz/en/docs/messaging-api/overview/). Le modèle de Webhook en ligne se trouve sur la plateforme Braze listée sous __Modèles & Médias__.

## Pré-requis

La ligne permet aux utilisateurs de recevoir des messages promotionnels et non promotionnels tant que les marques ont obtenu le consentement des utilisateurs. Pour commencer à envoyer par Line, vous devrez enregistrer votre entreprise auprès de Ligne et créer un Compte Entreprise de Ligne. Ci-dessous nous passons en revue les exigences pour envoyer des messages de ligne par l'intermédiaire de Braze.

| Exigences                    | Origine | Accès                                                                                                                                         | Libellé                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Entreprise de Ligne   | Lignes  | [https://www.linebiz.com/jp-fr/](https://www.linebiz.com/jp-en/)                                                                              | Les marques devront mettre en place un compte officiel d'entreprise pour utiliser l'API de messagerie de Ligne.<br><br>Lors de l'envoi de messages en ligne, vos messages seront tous associés à votre compte officiel en ligne, ce qui fait que les utilisateurs voient votre nom de compte et votre page.                      |
| Canal API de Messagerie      | Lignes  | [Utilisation de la documentation de la ligne OA Manager](https://developers.line.biz/en/docs/messaging-api/getting-started/#using-oa-manager) | Lorsque vous activez l'utilisation de l'API de messagerie dans le Gestionnaire de compte officiel de LIGNE, un canal API de messagerie est créé. Ce sera le canal que vous utiliserez pour communiquer avec vos clients.                                                                                                                     |
| Jetons d'accès au canal      | Lignes  | [Documentation de ligne de jeton d'accès au canal](https://developers.line.biz/en/docs/messaging-api/channel-access-tokens/)                  | Le jeton d'accès au canal vous permettra d'envoyer des messages aux utilisateurs qui ont ajouté votre compte officiel en tant qu'ami. Il peut être trouvé dans votre __console de développement en ligne__ sous l'onglet __API de messagerie__.                                                                                              |
| ID d'utilisateur de la ligne | Lignes  | [Obtenir la documentation de la ligne des identifiants de suivi](https://developers.line.biz/en/reference/messaging-api/#get-follower-ids)    | Vous devez avoir les identifiants de ligne des utilisateurs (cet identifiant est différent de celui des utilisateurs) pour envoyer des messages en ligne.<br><br>Une fois qu'un utilisateur a ajouté votre Compte Officiel en tant qu'ami, vous pouvez accéder à l'ID de Ligne de l'utilisateur via l'API Utilisateurs de Ligne. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Pour envoyer des messages aux utilisateurs, ils doivent remplir l'une des deux conditions :
- Utilisateurs qui ont ajouté votre compte officiel en tant qu'ami
- Les utilisateurs qui n'ont pas ajouté votre compte officiel en ligne en tant qu'ami mais qui ont envoyé un message à votre compte officiel en ligne (excluant les utilisateurs qui ont bloqué votre compte officiel)

## Détails de l'intégration

### Étape 1 : Récupérez les identifiants de la ligne de vos clients

Pour envoyer des messages sur la messagerie en ligne, vous devez collecter les identifiants de ligne de vos utilisateurs pour identifier votre utilisateur et interagir avec eux de manière cohérente.

__Qu'est-ce qu'un ID de ligne ?__<br> Les identifiants de ligne ne sont pas les mêmes que les noms d'utilisateur de la ligne de l'utilisateur. Il s'agit d'un ID généré par ligne qui peut être utilisé lors de l'interaction avec les API de Ligne.

__Où la trouverez-vous ? _<br> Pour obtenir une liste des identifiants de ligne de vos clients, utilisez l' [API d'identifiant d'utilisateur](https://developers.line.biz/en/reference/messaging-api/#get-follower-ids) qui vous est proposée. L'API retournera une liste d'ID de ligne pour tous les utilisateurs qui ont ami votre compte officiel en ligne ou qui vous ont envoyé un message à votre compte et qui ne vous ont pas bloqué. Lorsque vous faites une requête GET au point de terminaison `https://api.line.me/v2/bot/followers/ids`, vous obtiendrez les éléments suivants :


```json
{
   "userIds":[
      "U4af4980629...",
      "U0c229f96c4...",
      "U95afb1d4df..."
   ],
   "next":"yANU9IA..."
}
```

__Que dois-je faire avec ça ? _<br> Une fois que vous avez une liste d'ID de ligne, envoyez-le à Braze sous la forme d'un attribut personnalisé appelé `line_id`.

### Étape 2 : Envoyer à Braze en tant qu'attribut personnalisé

Coordonnez et partagez ceci avec vos développeurs pour envoyer les ID de ligne à Braze en tant qu'attribut [personnalisé]({{site.baseurl}}/user_guide/Data_and_Analytics/Custom_Data/Custom_Attributes/#custom-attributes). Les identifiants de ligne sont des chaînes auxquelles on peut accéder en faisant un [appel à l'API](https://developers.line.biz/en/reference/messaging-api/#get-follower-ids).

### Étape 3 : Définir votre jeton d'accès au canal en tant que bloc de contenu

Pour que les modèles de ligne de Braze puissent fonctionner, vous devrez entrer vos comptes officiels de ligne [Jeton d'accès au canal](https://developers.line.biz/en/docs/messaging-api/channel-access-tokens/) dans Braze en tant que [bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks). Une fois que vous avez défini le jeton d'accès au canal à l'intérieur d'un bloc de contenu, vous pourrez utiliser les modèles de Webhook en ligne pour envoyer des messages aux utilisateurs qui ont ajouté votre compte officiel en tant qu'ami.

#### Trouvez votre jeton d'accès au canal
Votre jeton d'accès au canal peut être trouvé dans la `Console développeur en ligne` sous l'onglet `Messaging API`.

!\[Jeton d'accès au canal de ligne\]\[1\]

#### Créer un bloc de contenu
Une fois que vous avez saisi votre jeton d'accès aux canaux de ligne, vous devrez créer un [Bloc de contenu Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks) et le nommer `LINE_Channel_AccessToken`. Copiez et collez votre jeton d'accès à la chaîne dans le bloc de contenu et enregistrez-le. Pour accéder aux blocs de contenu, allez dans l'onglet __Bibliothèque de blocs de contenu__ dans la section __Modèles & Médias__ du tableau de bord Braze.

!\[Jeton de bloc de contenu de ligne\]\[2\]

## Usage

Braze prend actuellement en charge les types de messages de lignes suivants :
- `Texte du texte`
- `Autocollant`
- `Image`
- `Carousel`

### Types de messages de ligne

Voici à quoi ressemblera chaque type de message de ligne pour vos utilisateurs.

{% tabs %}
{% tab Text %}
[`Texte`](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages): Les messages de la ligne texte sont des messages textuels qui supportent les émojis. <br><br> ![Text Type]({% image_buster /assets/img_archive/line_text_type.png %}){: style="border:0px;"}
{% endtab %}
{% tab Sticker %}
[`Sticker`](https://developers.line.biz/en/docs/messaging-api/message-types/#sticker-messages): Les autocollants peuvent être utilisés pour rendre votre application de bot plus expressive et plus engageante pour vos utilisateurs. Pour envoyer un autocollant, indiquez l'ID du paquet de l'autocollant et l'ID de l'autocollant dans un objet de message. Pour une liste des autocollants qui peuvent être envoyés avec l'API Messagerie, voir la [Liste des autocollants disponibles](https://developers.line.biz/en/docs/messaging-api/sticker-list/). <br><br> ![Sticker Type]({% image_buster /assets/img_archive/line_sticker_type.png %}){: style="border:0px;"}
{% endtab %}
{% tab Image %}
[`Image`](https://developers.line.biz/en/docs/messaging-api/message-types/#image-messages): Pour envoyer des images, inclure les URL de l'image d'origine et une image de prévisualisation plus petite dans l'objet de message. L'image de prévisualisation est affichée dans le chat, et l'image entière est ouverte lorsque l'image est tapée. Notez que les URLs doivent utiliser HTTPS sur TLS 1.2 ou supérieur. <br><br> ![Type d'image]({% image_buster /assets/img_archive/line_image_type.png %})
{% endtab %}
{% tab Carousel %}
[`Carrousel`](https://developers.line.biz/en/docs/messaging-api/message-types/#carousel-template): Utilisez le modèle de carrousel pour envoyer un message avec des objets en colonne multiples que les utilisateurs peuvent traverser. En plus d'avoir des boutons, vous pouvez également indiquer dans chaque objet de colonne une action unique à exécuter lorsqu'un utilisateur clique n'importe où dans l'image, titre ou zone de texte. <br><br> ![Carousel Type]({% image_buster /assets/img_archive/line_carousel_type.png %}){: style="border:0px;"}
{% endtab %}
{% endtabs %}

Dans __Modèles & Média__, allez dans __Modèles de Webhook__ et choisissez le __Modèle de Webhook Messenger Ligne__.

1. Entrez votre nom de modèle, ajoutez des équipes et ajoutez des étiquettes.
2. Entrez votre message, l'identifiant de l'autocollant ou l'image en fonction du type de modèle de ligne que vous avez sélectionné.
3. L'attribut personnalisé `ID de ligne` doit être modèle dans le champ `À :` du corps du message. Sinon, inclure l'identifiant de ligne comme attribut personnalisé. Cela peut être fait en utilisant le bouton bleu et blanc + + dans le coin de la boîte __Corps de requête__.

### Aperçu et test de votre Webhook

Avant d'envoyer votre message, testez votre webhook. Assurez-vous que votre ID de ligne est enregistré dans Braze (ou le trouver et tester en tant qu'utilisateur personnalisé), et utilisez l'aperçu pour envoyer le message de test :

!\[Envoi d'un message à vous-même\]\[3\]

Si vous recevez le message avec succès, vous pouvez commencer à configurer ses paramètres de livraison.

### Utilisateurs de ligne de ciblage

Vous devriez [créer un segment][62] pour tous les utilisateurs pour lesquels l' `ID de ligne` existe en tant qu'attribut personnalisé et activer [Suivi Analytics][61] pour suivre vos taux d'abonnement Messenger au fil du temps. Si vous choisissez de ne pas créer de segment spécifique pour les abonnés de Messenger, assurez-vous d'inclure un filtre pour `ID de ligne` existant pour éviter les erreurs :

!\[Filtre de Segment pour ID de ligne\]\[63\]

Vous pouvez également utiliser une autre segmentation pour cibler vos campagnes en ligne et le reste du processus de création de campagne, comme toute autre campagne.
[1]: {% image_buster /assets/img_archive/line_channel_access_token.png %} [2]: {% image_buster /assets/img_archive/line_content_block_token. ng %} [3]: {% image_buster /assets/img_archive/line_preview.png %} [63]: {% image_buster /assets/img_archive/fbm-segmentation.png %}

[61]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/viewing_and_understanding_segment_data/#viewing-and-understanding-segment-data
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment