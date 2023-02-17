---
nav_title: LINE
article_title: LINE
alias: /partners/line/
description: "Cet article présente le partenariat entre Braze et LINE, l’une des plateformes d’envoi de messages instantané les plus populaires au monde."
page_type: partner
search_tag: Partenaire

---

# LINE

> [LINE](https://line.me/en/) est l’une des plateformes d’envoi de messages instantané les plus populaires au monde, utilisée par des centaines de millions d’utilisateurs actifs par mois. Grâce à cette plateforme, les marques peuvent interagir avec leurs clients avec des messages riches et bidirectionnels.

L’intégration de Braze et LINE vous permet d’exploiter les webhooks de Braze, la segmentation avancée, la personnalisation et les fonctionnalités de déclenchement pour envoyer des messages à vos utilisateurs dans LINE par le biais de l’[API d’envoi de messages de LINE](https://developers.line.biz/en/docs/messaging-api/overview/)..

## Conditions préalables

LINE autorise l’envoi de messages promotionnels et non promotionnels aux utilisateurs, pour autant que votre marque ait obtenu le consentement des utilisateurs. Pour envoyer des messages aux utilisateurs, vous devez remplir l’une des deux conditions suivantes :
- Utilisateurs ayant ajouté votre compte officiel LINE en tant qu’ami.
- Utilisateurs qui n’ont pas ajouté votre compte officiel LINE en tant qu’ami, mais qui ont envoyé un message à votre compte officiel LINE (à l’exclusion des utilisateurs qui ont bloqué votre compte officiel LINE).
<br><br>

| Configuration requise | Description |
| ----------- | ----------- | 
| Compte professionnel LINE | Un [compte professionnel LINE](https://www.linebiz.com/jp-en/) est requis pour profiter de ce partenariat.<br><br>Lors de l’envoi de messages LINE, vos messages seront tous associés à votre compte officiel LINE, ce qui permet aux utilisateurs de voir le nom et la page de votre compte.|
| Canal de l’API de messagerie | Lorsque vous activez l’utilisation de l’API de messagerie dans le [gestionnaire de compte officiel](https://developers.line.biz/en/docs/messaging-api/getting-started/#using-oa-manager) LINE, un canal d’API de messagerie est créé. C’est le canal que vous utiliserez pour communiquer avec vos clients. |
| Jetons d’accès au canal |Le [jeton d’accès au canal](https://developers.line.biz/en/docs/messaging-api/channel-access-tokens/) vous permettra d’envoyer des messages aux utilisateurs qui ont ajouté votre compte officiel LINE en tant qu’ami. Ce jeton est disponible dans la **LINE Developer Console (Developer Console de LINE)** sous l’onglet **Messaging API** (API d’envoi de messages).
| ID utilisateur de LINE  | Vous devez disposer des identifiants utilisateur de LINE (cet ID est différent des noms d’utilisateur) pour envoyer des messages sur LINE.<br><br>Une fois qu’un utilisateur ajoute votre compte officiel LINE en tant qu’ami, vous pouvez accéder à l’ID LINE de l’utilisateur via l’API utilisateur de LINE. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

### Étape 1 : Collecter les ID client de LINE

Pour envoyer des messages dans LINE, vous devez collecter les identifiants de LINE de vos utilisateurs pour les identifier et interagir avec eux de manière cohérente. L’ID de LINE n’est pas identique aux noms d’utilisateur LINE de l’utilisateur. Les ID de LINE sont générés par LINE et peuvent être utilisés lors de l’interaction avec les API de LINE.

Les ID de LINE peuvent être obtenus à l’aide de l’[API d’ID utilisateur](https://developers.line.biz/en/reference/messaging-api/#get-follower-ids) de LINE. Cet endpoint renvoie une liste d’ID de LINE de tous les utilisateurs amis de votre compte officiel LINE ou de ceux qui ont envoyé un message à votre compte et ne vous ont pas bloqué. 

Lorsque vous faites une demande GET à l’endpoint `https://api.line.me/v2/bot/followers/ids`, vous obtiendrez les éléments suivants :
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
Une fois que vous avez obtenu une liste des ID de LINE, vous les enverrez à Braze en tant qu’attribut personnalisé `line_id`.

### Étape 2 : Envoyer des ID à Braze en tant qu’attributs personnalisés

Coordonnez le contenu et partagez-le avec vos développeurs pour envoyer les `line_id` à Braze en tant qu’[attributs personnalisés]({{site.baseurl}}/user_guide/Data_and_Analytics/Custom_Data/Custom_Attributes/#custom-attributes).

### Étape 3 : Définir votre jeton d’accès au canal comme bloc de contenu

Dans Braze, accédez à **Templates & Media (Modèles et médias) > Content Blocks Library (Bibliothèque de bloc de contenu) > + Create Content Block (Créer un bloc de contenu)** et créez un [Bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks) Braze. Nommez ce bloc de contenu `LINE_Channel_AccessToken`. 

Collez ensuite votre jeton d’accès au canal dans le corps du bloc de contenu et enregistrez-le.

![Image du bloc de contenu affichant le nom du bloc de contenu, la balise Liquid et le jeton d’accès au canal censuré.][2]

Une fois que vous avez défini le jeton d’accès au canal à l’intérieur d’un bloc de contenu, vous pourrez utiliser le modèle de webhook LINE pour envoyer des messages aux utilisateurs.

### Étape 4 : Sélectionner un modèle de webhook

Dans **Templates & Media** (Modèles et médias), accédez à **Webhook Templates** (Modèles de webhook) et sélectionnez l’un des modèles de webhook de LINE Messenger suivants : 

![Sélection de modèles de webhook prêts à l’emploi disponibles.]({% image_buster /assets/img_archive/line_templates.png %}){: style="border:0px;"}

{% tabs %}
{% tab Texte de LINE %}
Le modèle de webhook [texte](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages) de LINE vous permet d’envoyer des messages texte qui prennent en charge les émoticônes.

![IU d’envoi de messages de Line avec deux exemples de message texte sur la plateforme.]({% image_buster /assets/img_archive/line_text_type.png %}){: style="max-width:70%;border:0px;"}
{% endtab %}
{% tab Sticker de LINE %}
Le modèle [sticker](https://developers.line.biz/en/docs/messaging-api/message-types/#sticker-messages) de LINE vous permet d’envoyer des messages autocollants. Les autocollants peuvent être utilisés pour rendre votre application bot plus expressive et plus attrayante pour vos utilisateurs. 

Pour envoyer un autocollant, incluez l’ID de package de l’autocollant et l’ID de l’autocollant dans l’objet du message. Reportez-vous à la [liste des autocollants disponibles](https://developers.line.biz/en/docs/messaging-api/sticker-list/) qui peuvent être envoyés avec l’API de messagerie.

![IU de messagerie de Line avec plusieurs exemples de message autocollant. Ces exemples comprennent un ours qui fait la fête, un lapin avec le pouce en l’air et un canard jaune.]({% image_buster /assets/img_archive/line_sticker_type.png %}){: style="max-width:70%;border:0px;"}
{% endtab %}
{% tab Image de LINE %}
Le modèle [image](https://developers.line.biz/en/docs/messaging-api/message-types/#image-messages) de LINE vous permet d’envoyer des images à vos utilisateurs LINE.

Pour envoyer des images, incluez les URL de l’image d’origine et une image d’aperçu plus petite dans l’objet du message. L’image d’aperçu s’affiche dans la discussion et l’image complète est ouverte lorsque l’image est sélectionnée. Notez que les URL doivent utiliser HTTPS sur TLS 1.2 ou version ultérieure.

![IU d’envoi de messages de Line avec message contenant une image sur la plateforme.]({% image_buster /assets/img_archive/line_image_type.png %})
{% endtab %}
{% tab Carrousel de LINE %}
Le modèle [carrousel](https://developers.line.biz/en/docs/messaging-api/message-types/#carousel-template) de LINE vous permet d’envoyer des messages avec plusieurs objets colonne que les utilisateurs peuvent parcourir. En plus d’avoir des boutons, vous pouvez également indiquer dans chaque objet colonne une action unique à exécuter lorsqu’un utilisateur clique n’importe où dans l’image, le titre ou la zone de texte.

![UI de messagerie de Line affichant un message de type carousel. Ce message inclut une zone de contenu que vous pouvez parcourir qui inclut une image, une description, un bouton de réserve et un bouton d’appel. ]({% image_buster /assets/img_archive/line_carousel_type.png %}){: style="max-width:70%;border:0px;"}
{% endtab %}
{% endtabs %}

### Étape 5 : Configurer votre modèle de webhook

Dans votre modèle de webhook, fournissez un nom de modèle et ajoutez des équipes et des balises, si nécessaire. Ensuite, saisissez votre message, votre ID d’autocollant ou votre image en fonction du type de modèle de LINE que vous avez sélectionné.

L’attribut personnalisé `LINE ID` doit être inclus dans le champ `To:` du corps du message. Si ce n’est pas le cas, incluez l’ID de LINE comme attribut personnalisé. Pour cela, utilisez le bouton + bleu et blanc dans le coin de la zone **Request Body** (Corps de la demande).

#### Prévisualisation et test de votre webhook

Avant d’envoyer votre message, testez votre webhook. Assurez-vous que votre ID de LINE est enregistré dans Braze (ou trouvez-le et testez-le en tant qu’utilisateur personnalisé), et utilisez l’aperçu pour envoyer le message de test :

![Onglet Test du générateur de webhook de Braze qui affiche l’aperçu du message en l’envoyant à un utilisateur existant.][3]

Si vous recevez le message avec succès, vous pouvez commencer à configurer les paramètres de livraison.

## Comment utiliser cette intégration

Une fois configurée, utilisez cette intégration pour cibler les utilisateurs LINE. Tout d’abord, [créez un segment][62] pour tous les utilisateurs pour qui `LINE ID` existe comme attribut personnalisé et activez le [suivi analytique][61] pour suivre l’évolution de vos taux d’inscription à Messenger. 

![Filtre de segment « line_id » défini sur « n’est pas vide ».][63]

Si vous choisissez de ne pas créer un segment spécifique pour les abonnés de Messenger, assurez-vous d’inclure un filtre pour `LINE ID` existant pour éviter les erreurs.

Vous pouvez également utiliser d’autres segmentations pour cibler vos campagnes de LINE et le reste du processus de création de campagnes, comme c’est le cas avec toute autre campagne.

[1]: {% image_buster /assets/img_archive/line_channel_access_token.png %}
[2]: {% image_buster /assets/img_archive/line_content_block_token.png %}
[3]: {% image_buster /assets/img_archive/line_preview.png %}
[61]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#viewing-and-understanding-segment-data
[62]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[63]: {% image_buster /assets/img_archive/line_segment.png %}
