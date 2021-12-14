---
nav_title: Lignes directrices & Conseils
article_title: Lignes directrices & Conseils
page_order: 1
page_type: Référence
description: "Cet article couvre le contenu spécifique, le style et les astuces techniques pour divers cas d'utilisation de courriels."
channel: Email
---

# Directives et astuces pour les e-mails

> Cet article traite des trucs et astuces techniques, du style et du contenu spécifiques à divers cas et sujets d'utilisation des courriels.

## Directives techniques

### Généraux

- Si vous souhaitez un modèle de courrier électronique à la fois pour mobile et pour bureau, gardez la largeur inférieure à 500 pixels.
- Utilisez des feuilles de style en ligne pour formater votre courriel en tant que CSS ou il ne sera pas reconnu par les fournisseurs de services de messagerie (ESP).
- Les images téléchargées vers le modèle d'email doivent être inférieures à 5 Mo et soit PNG, JPG, GIF.
- Toujours utiliser les alt-tags pour les images si elles n'apparaissent pas dans l'email (bloqué, ne pas charger, etc.)
- Ne définissez pas les hauteurs et les largeurs des images car cela provoquera des espaces inutiles dans un courriel dégradé.
- Les balises `div` ne doivent pas être utilisées car la plupart des clients de messagerie ne supportent pas leur utilisation. Utilisez plutôt des tables imbriquées.
- N'utilisez pas JavaScript car il ne fonctionne pas avec ESP.
- Braze améliore les temps de chargement en utilisant un CDN global pour héberger toutes les images de courriel.

### Validation de l'adresse e-mail

Braze ajuste automatiquement les adresses e-mail saisies pour supprimer tous les espaces. Les adresses e-mail ciblées via les serveurs Braze doivent être validées selon les normes de la [RFC 2822][24]. En plus de ces normes, Braze n'accepte pas certains caractères (indiqués ci-dessous) et les reconnaît comme non valides.

Si un e-mail est rebondi, Braze marque l'email comme non valide et le statut de l'abonnement n'est pas changé.
{% details Unaccepted characters outside of RFC Standards %}
- *
- /
- ?
- !
- $
- #
- %
- &#94;
- &
- (
- )
- {
- }
- [
- ]
- ~
- ,
{% enddetails %}

### Balises HTML interdites

Les balises HTML suivantes sont interdites car elles peuvent potentiellement permettre l'exécution de code malveillant dans le navigateur. En conséquence, les clients de messagerie des utilisateurs finaux filtrent souvent les courriels qui les contiennent.
- `<!doctype>`
- `<applet>`
- `<bgsound>`
- `<embed>`
- `<frameset>`
- `<iframe>`
- `<ilayer>`
- `<layer>`
- `<link>`
- `<meta>`
- `<object>`
- `<script>`
- `<title>`
- `<xml>`
- `<svg>`

Les attributs HTML suivants sont également interdits :

- `<animationend>`
- `<animationiteration>`
- `<animationstart>`
- `<data-bind>`
- `<fscommand>`
- `<onabort>`
- `<onabort>`
- `<onactivate>`
- `<onafterprint>`
- `<onafterupdate>`
- `<onbeforeactivate>`
- `<onbeforecopy>`
- `<onbeforecut>`
- `<onbeforedeactivate>`
- `<onbeforeeditfocus>`
- `<onbeforepaste>`
- `<onbeforeprint>`
- `<onbeforeunload>`
- `<onbeforeupdate>`
- `<onbegin>`
- `<onblur>`
- `<onbounce>`
- `<oncanplay>`
- `<oncanplaythrough>`
- `<oncellchange>`
- `<onchange>`
- `<onclick>`
- `<oncontextmenu>`
- `<oncontrolselect>`
- `<oncopy>`
- `<oncut>`
- `<ondataavailable>`
- `<ondatasetchanged>`
- `<ondatasetcomplete>`
- `<ondblclick>`
- `<ondeactivate>`
- `<ondrag>`
- `<ondragdrop>`
- `<ondragend>`
- `<ondragenter>`
- `<ondragleave>`
- `<ondragover>`
- `<ondragstart>`
- `<ondrop>`
- `<ondurationchange>`
- `<onemptied>`
- `<onend>`
- `<onended>`
- `<onerror>`
- `<onerror>`
- `<onerrorupdate>`
- `<onfilterchange>`
- `<onfinish>`
- `<onfocus>`
- `<onfocusin>`
- `<onfocusout>`
- `<onhashchange>`
- `<onhelp>`
- `<oninput>`
- `<oninvalid>`
- `<onkeydown>`
- `<onkeypress>`
- `<onkeyup>`
- `<onlayoutcomplete>`
- `<onload>`
- `<onloadeddata>`
- `<onloadedmetadata>`
- `<onloadstart>`
- `<onlosecapture>`
- `<onmediacomplete>`
- `<onmediaerror>`
- `<onmessage>`
- `<onmousedown>`
- `<onmouseenter>`
- `<onmouseleave>`
- `<onmousemove>`
- `<onmouseout>`
- `<onmouseover>`
- `<onmouseup>`
- `<onmousewheel>`
- `<onmove>`
- `<onmoveend>`
- `<onmovestart>`
- `<onoffline>`
- `<ononline>`
- `<onopen>`
- `<onoutofsync>`
- `<onpagehide>`
- `<onpageshow>`
- `<onpaste>`
- `<onpause>`
- `<onplay>`
- `<onplaying>`
- `<onpopstate>`
- `<onprogress>`
- `<onpropertychange>`
- `<onratechange>`
- `<onreadystatechange>`
- `<onredo>`
- `<onrepeat>`
- `<onreset>`
- `<onresize>`
- `<onresizeend>`
- `<onresizestart>`
- `<onresume>`
- `<onreverse>`
- `<onrowdelete>`
- `<onrowexit>`
- `<onrowinserted>`
- `<onrowsenter>`
- `<onscroll>`
- `<onsearch>`
- `<onseek>`
- `<onseeked>`
- `<onseeking>`
- `<onselect>`
- `<onselectionchange>`
- `<onselectstart>`
- `<onshow>`
- `<onstalled>`
- `<onstart>`
- `<onstop>`
- `<onstorage>`
- `<onsubmit>`
- `<onsuspend>`
- `<onsyncrestored>`
- `<ontimeerror>`
- `<ontimeupdate>`
- `<ontoggle>`
- `<ontouchcancel>`
- `<ontouchend>`
- `<ontouchmove>`
- `<ontouchstart>`
- `<ontrackchange>`
- `<onundo>`
- `<onunload>`
- `<onurlflip>`
- `<onvolumechange>`
- `<onwaiting>`
- `<onwheel>`
- `<seeksegmenttime>`
- `<transitionend>`

### Implémentation des balises 'alt'

Puisque les filtres anti-spam surveillent à la fois une version HTML et une version texte d'un message, Utiliser des alternatives en texte brut est un excellent moyen de réduire votre score de spam. De plus, Les textes ALT peuvent servir à compléter et, dans certains cas, remplacer les images incluses dans votre corps de courrier électronique qui peuvent avoir été filtrées par le fournisseur de messagerie d'un utilisateur.

### Paramétrage et adresse de réponse

Lorsque vous définissez vos adresses "De", assurez-vous que votre domaine de messagerie "De" corresponde à votre domaine d'envoi (c'est-à-dire `marketing.yourdomain.com`). Si vous ne le faites pas, cela peut entraîner un déséquilibre entre SPF et DKIM. Tous les e-mails de réponse peuvent être configurés sur votre domaine racine.

## Astuces de style

### Style d'adresse

- La **Ligne de Sujet** est l'une des premières choses que les destinataires verront après réception de votre message.
  - Le maintien de 6 à 10 mots donnera les taux d'ouverture les plus élevés.
  - Il y a également différentes approches pour créer une bonne ligne de sujet, de poser une question à pique l’intérêt du lecteur ou d’être plus direct, à la personnalisation de sa clientèle.
  - Ne restez pas avec une seule ligne de sujet, essayez de nouvelles lignes et évaluez leur efficacité.
  - La ligne du sujet ne doit pas contenir plus de 35 caractères à afficher correctement sur mobile.

- Le **« De Champ»** devrait clairement montrer qui est l'expéditeur.
  - Essayez de ne pas utiliser le nom d'une personne inconnue ou une abréviation inhabituelle, plutôt essayez d'utiliser quelque chose de reconnaissable comme le nom de la société.
  - Si vous utilisez le nom d'une personne correspond aux méthodes de votre entreprise pour personnaliser l'e-mail, rester cohérent et conserver le même « De Nom » pour développer une relation avec le destinataire.
  -  Le nom « De » ne doit pas contenir plus de 25 caractères à afficher correctement sur mobile.

### Style du corps

- De nombreux utilisateurs utilisent **Aperçu du courrier électronique**, soit dans Gmail ou Outlook.
  - Ces zones d'aperçu permettent généralement d'afficher environ 300 pixels ou 85 caractères de contenu.
  - Il est recommandé que le courriel communique le point principal du message efficacement dans cet espace, en engageant l'intérêt du lecteur à encourager les ouvertures.

- **Les adresses e-mail** non répondues ne sont généralement pas recommandées pour plusieurs raisons car elles désengagent vos lecteurs.
  - De nombreux destinataires répondent à l'e-mail pour se désabonner, donc s'ils ne sont pas autorisés à le faire, la prochaine action est plus souvent que de ne pas marquer l'e-mail comme spam.
  - Sortir des réponses du bureau peut en fait fournir des informations précieuses, augmenter les taux d'ouverture et diminuer les rapports de spam (en supprimant ceux qui ne veulent pas être envoyés).
  - Sur un plan personnel, une non-réponse peut paraître impersonnelle, paresseuse et arrogante aux destinataires (suggérant “Vous ne valez pas mon temps”), et peut les désactiver de recevoir d'autres courriels de votre entreprise.

- **Le texte de préen-tête** est souvent utilisé par les vendeurs de courriels pour fournir des informations supplémentaires sur le contenu d'un courriel.
  - Un préen-tête est le texte de l'aperçu affiché immédiatement après un sujet d'e-mail. Dans l'exemple ci-dessous, le préen-tête est `- Marque. Nouveau. Shorts de salon`.

!\[Exemple\]\[61\]

  - La quantité de texte de préen-tête visible dépend du client de messagerie de l'utilisateur et de la longueur de la ligne d'objet de l'e-mail. Généralement, nous suggérons que les préen-têtes de courriel soient compris entre 50 et 100 caractères.

### Limites de caractères de préen-tête

  | Client de messagerie mobile | Limite |
  |:---------------------------:|:------:|
  |         Outlook iOS         |   74   |
  |       Natif d'Android       |   43   |
  |        Android Gmail        |   24   |
  |          Natif iOS          |   82   |
  |          Gmail iOS          |   30   |
  {: .reset-td-br-1 .reset-td-br-2}

  | Client de messagerie de bureau | Limite |
  |:------------------------------:|:------:|
  |           Mail Apple           |   33   |
  |          Outlook '13           |   38   |
  |      Outlook pour Mac '15      |   53   |
  |          Outlook '16           |   50   |
  {: .reset-td-br-1 .reset-td-br-2}


  | Webmail Email Client | Limite |
  |:--------------------:|:------:|
  |     Courrier AOL     |   81   |
  |        Gmail         |  119   |
  |     Outlook.com      |   49   |
  |      Bureau 365      |   40   |
  |       Mail.ru        |   64   |
  {: .reset-td-br-1 .reset-td-br-2}


  Source: [Email sur Acid][62]


- **Appel aux actions** entrent en jeu une fois que les lecteurs ont ouvert votre email.
  - Pointez vos lecteurs dans la bonne direction, que vous vouliez qu'ils s'abonnent, achètent un produit ou visitent votre site Web.
  - Utilisez des mots forts pour que le lecteur sache exactement ce que vous leur demandez, mais assurez-vous qu'il reflète la voix de la marque de votre entreprise et que chaque appel à l'action présente une sorte de valeur pour le consommateur.
  - Pré-en-tête ne doit pas contenir plus de 85 caractères et avoir une sorte d'appel descriptif à l'action qui prend en charge la ligne sujet.

- **Emails et sites d'atterrissage** vers lesquels vous dirigez vos utilisateurs doivent être optimisés pour mobile :
  - Pas de boîtes interstitielles
  - Champs de formulaire volumineux
  - Navigation facile
  - Texte volumineux
  - « Doigts amicaux»
  - Espace blanc généreux
  - Copie courte et concise du corps
  - Effacer les appels à l'action

### Taille de l'e-mail

| Texte uniquement | Texte avec des images | Largeur de l'e-mail |
|:----------------:|:---------------------:|:-------------------:|
|   25Ko maximum   |     60 Ko maximum     | 600 pixels maximum  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Assurez-vous de limiter votre **taille de corps**: les gros corps de courrier électronique (plus de 102kb) ne sont pas seulement extrêmement taxables sur les serveurs de Braze et SendGrid, mais sont également coupées par Gmail et d'autres clients E-Mail. Nous vous recommandons de garder la taille de votre e-mail sous 25kb pour juste du texte, ou 60kb avec des images.

Si vous recevez cette erreur dans l'éditeur, vous avez probablement des images encodées en base64 qui ont été intégrées dans le courriel lui-même. Ce n'est pas un moyen efficace d'envoyer des courriels avec des images. Nous vous encourageons vivement à utiliser le chargeur d'images de Braze pour héberger des images et les référencer par href.

### Longueur du texte

| **Caractéristiques du texte**   | **Propriétés recommandées**                                            |
| ------------------------------- | ---------------------------------------------------------------------- |
| Longueur de la ligne du sujet   | 35 caractères maximum (pour un affichage mobile optimal) (6 à 10 mots) |
| Longueur du nom de l'expéditeur | 25 caractères maximum (pour un affichage mobile optimal)               |
| Longueur du pré-en-tête         | 85 caractères maximum                                                  |
{: .reset-td-br-1 .reset-td-br-2}

### Taille de l'image

|    Taille    | Largeur de l'image de l'en-tête | Largeur de l'image du corps | Types de fichiers |
|:------------:|:-------------------------------:|:---------------------------:|:-----------------:|
| 5 Mo maximum |       600 pixels maximum        |     480 pixels maximum      |   PNG, JPG, GIF   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

Des images plus petites et de haute qualité se chargeront plus rapidement. Il est donc recommandé d'utiliser le plus petit actif possible pour atteindre la sortie souhaitée.

### Liaison profonde

Un pourcentage élevé des courriels sont lus sur les appareils mobiles. L’utilisation de liens profonds est une excellente pratique pour s’engager avec ces destinataires de courriels mobiles. Avec les notifications push et les messages dans l'application, un lien profond mène l'utilisateur directement à une destination spécifiée dans une application. Par contre, le courrier électronique ne donne aucun moyen de savoir si les destinataires ont installé l'application. En tant que tel, fournir un lien profond vers l'application pourrait être lié à un message d'erreur pour ces destinataires qui n'ont pas l'application.

## Conseils et astuces spécifiques au contenu

### Embarquement

- fournir des conseils pour aider les utilisateurs à commencer.
- Ne montrer que les fonctionnalités les plus essentielles - trop d'informations peuvent être accablantes et potentiellement déroutantes si l'utilisateur n'est toujours pas familier avec votre application.
- Fournissez des liens vers votre documentation et indiquez aux utilisateurs comment ils peuvent obtenir de l'aide.
- Essayez de toujours envoyer un e-mail de bienvenue après l'inscription d'un utilisateur. Ci-dessous est un exemple de LivingSocial qui contient des appels simples mais clairs à l'action et permet aux utilisateurs de connaître une affaire :

!\[LivingSocial email\]\[26\]{: style="max-width:70%;"}

### Ventes et promotions

- Quelques secondes après l'ouverture de votre e-mail, les utilisateurs doivent connaître la valeur de la promotion (ce que sont les remises et ce qui est en vente) et combien de temps l'offre durera.
- Fournissez des graphiques pour illustrer tous les produits que vous promouvez.
- Gardez votre copie concise et simple pour ne pas encombrer votre e-mail et distraire les utilisateurs du contenu essentiel.
- Faites votre appel à l'action claire et donnez aux bénéficiaires un moyen facile de participer immédiatement à la promotion.
- Si vous recommandez certains produits, essayez de les présenter comme supervisés, des suggestions personnelles que l'utilisateur pourrait aimer.
- Utilisez la preuve sociale pour promouvoir vos produits. Afficher aux utilisateurs les objets que leurs amis ont aimés ou achetés.
- Si vous faites la promotion d'une offre de temps limité, n'oubliez pas de faire savoir aux utilisateurs ! Ideeli fait un excellent travail pour transmettre l'urgence dans cet e-mail:

!\[Ideeli email\]\[27\]{: style="max-width:70%;"}

### Transactionnel

- Si l'utilisateur a récemment fait un achat dans l'application, vous devriez les remercier et fournir tous les conseils qui peuvent les aider à tirer le meilleur parti de cet achat.
- Si l'utilisateur a récemment fait un achat hors application, fournissez-lui une confirmation d'expédition et un moyen de poser des questions sur son envoi.
- Demander aux utilisateurs de donner des commentaires après un achat est un bon moyen de solliciter des commentaires sans être pushy. Parce que vous venez de fournir un service aux utilisateurs, ils sont plus susceptibles de partager leurs pensées. Voici un exemple de courrier électronique de Restaurant.com

!\[Email du restaurant\]\[28\]{: style="max-width:80%;"}

### Rétention

- Gardez votre ton convivial.
- Ceci peut être votre dernière chance de gagner des utilisateurs, alors assurez-vous d'inclure du contenu qui montre la valeur de votre application.
- Si l'utilisateur a été relativement inactif depuis l'installation, offrez des conseils utiles pour commencer.
- Pour les applications sociales, gardez les utilisateurs à jour sur les activités de leurs amis.
- Offrez des réductions ou toute autre incitation susceptible de ramener les utilisateurs.
- Essayez de rendre votre message personnel pour montrer à l'utilisateur qu'il est toujours valorisé. Rue La La, par exemple, encadre son e-mail de rétention comme une note de son PDG :

!\[Ruelala email\]\[29\]{: style="max-width:80%;"}

### Réseaux sociaux

- Les courriels peuvent vous aider à construire une base de fans en dirigeant les destinataires vers votre Facebook, Twitter, Instagram, Pinterest, chaîne YouTube, etc.
- Inclure des liens vers vos comptes de réseaux sociaux dans l'e-mail pour faciliter la connexion des utilisateurs.
- Rends-le amusant! Essayez de lancer un concours photo, de promouvoir un hashtag ou de faire un cadeau. Ci-dessous se trouve un e-mail de Hailo qui offre une récompense pour avoir participé aux défis photo:

!\[Hailo social email\]\[30\]{: style="max-width:70%;"}

### Mises à jour

- Envoyez des mises à jour des fonctionnalités nouvelles ou améliorées à tous vos utilisateurs.
- Mettre à jour les utilisateurs sur de nouvelles fonctionnalités est également un outil de réengagement car il rappelle aux utilisateurs en perte de valeur de votre application.
- Si votre fonctionnalité nécessite une explication ou une démo, incluez un lien dans le message. Voici un exemple de Allrecipes.com :

!\[Toutes recettes email\]\[31\]{: style="max-width:70%;"}
[26]: {% image_buster /assets/img_archive/Livingsocial_email.png %} [27]: {% image_buster /assets/img_archive/Ideeli_email.png %} [28]: {% image_buster /assets/img_archive/Restaurant_email.png %} [29]: {% image_buster /assets/img_archive/Ruelala_email.png %} [30]: {% image_buster /assets/img_archive/Hailo_social_email.png %} [31]: {% image_buster /assets/img_archive/Allrecipes_email.png %}
[61]: {% image_buster /assets/img_archive/preheader_example.png %}


[24]: http://tools.ietf.org/html/rfc2822
[62]: https://www.emailonacid.com/blog/article/email-marketing/preview-vs-preheader-text-how-long-should-preheader-text-be/