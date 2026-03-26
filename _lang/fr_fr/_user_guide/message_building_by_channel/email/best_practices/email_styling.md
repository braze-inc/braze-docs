---
nav_title: Style des e-mails
article_title: Style des e-mails
page_order: 2
page_type: reference
description: "Le présent article décrit les meilleures pratiques relatives au style des messages pour vos campagnes par e-mail."
channel: email

---

# Style des e-mails

## Style de l'adresse

La **ligne d'objet** est l'une des premières choses que les destinataires verront en recevant votre message. Les lignes d'objet de 6 à 10 mots génèrent les meilleurs taux d'ouverture. 

Il existe différentes approches pour créer une bonne ligne d'objet : poser une question pour susciter l'intérêt du lecteur, être plus direct, la personnaliser pour mieux engager votre clientèle… Ne vous contentez pas d'une seule ligne d'objet, tirez parti des [tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing/) pour en essayer de nouvelles et évaluer leur efficacité. Pour s'afficher correctement sur mobile, les lignes d'objet ne doivent pas dépasser 35 caractères.

Le champ « De » doit indiquer clairement qui est l'expéditeur. Évitez d'utiliser le nom d'une personne ou une abréviation peu courante. Privilégiez plutôt un nom reconnaissable, comme celui de votre marque. Si l'utilisation du nom d'une personne correspond aux méthodes de personnalisation des e-mails de votre marque, restez cohérent afin de développer une relation avec les destinataires. Pour s'afficher correctement sur mobile, le nom du champ « De » ne doit pas comporter plus de 25 caractères.

### Adresses « noreply »

Les adresses e-mail sans réponse sont généralement déconseillées pour plusieurs raisons, car elles peuvent dissuader vos lecteurs. De nombreux destinataires répondent à l'e-mail pour se désabonner : s'ils ne peuvent pas le faire, leur réaction suivante est le plus souvent de signaler l'e-mail comme spam.

Les réponses automatiques (de type « absent du bureau ») peuvent en réalité fournir des informations précieuses, améliorer les taux d'ouverture et diminuer les signalements de courrier indésirable (en retirant ceux qui ne souhaitent pas recevoir d'e-mails). Sur un plan plus personnel, une adresse « noreply » peut paraître impersonnelle aux destinataires et les dissuader de recevoir d'autres e-mails de votre entreprise.

## Texte d'accroche

Dans un e-mail, le texte d'accroche communique efficacement le point essentiel du message pour capter l'intérêt du lecteur et l'encourager à ouvrir l'e-mail. Le texte d'accroche est également souvent utilisé par les marketeurs pour fournir des informations supplémentaires sur le contenu d'un e-mail. L'accroche est le texte de prévisualisation affiché immédiatement après la ligne d'objet. Dans l'exemple suivant, l'accroche est `- Brand. New. Lounge Shorts`.

![Accroche dans une boîte de réception Gmail avec le texte « Brand. New. Lounge Shorts ».]({% image_buster /assets/img_archive/preheader_example.png %})

La quantité de texte d'accroche visible dépend du client e-mail de l'utilisateur et de la longueur de la ligne d'objet. En général, nous recommandons que les accroches fassent entre 50 et 100 caractères.

{% alert note %}
L'accroche peut faire référence à du Liquid dans le corps de l'e-mail, et le corps de l'e-mail peut faire référence à du Liquid dans l'accroche. En effet, le texte de l'accroche fait partie du corps du message lorsque vous envoyez des messages à vos destinataires.
{% endalert %}

Voici quelques bonnes pratiques à garder à l'esprit au moment de rédiger vos accroches :

1. Les appels à l'action interviennent une fois que les lecteurs ont ouvert votre e-mail.
  - Orientez vos lecteurs dans la bonne direction, que vous souhaitiez qu'ils s'abonnent, achètent un produit ou consultent votre site Internet.
  - Utilisez des mots percutants pour que le lecteur sache exactement ce que vous attendez de lui, tout en veillant à refléter la voix de votre marque et à ce que chaque appel à l'action apporte une valeur au consommateur.
  - L'accroche ne doit pas dépasser 85 caractères et doit contenir un appel à l'action descriptif en lien avec la ligne d'objet.

2. Les e-mails et les pages de destination vers lesquels vous redirigez vos utilisateurs doivent être optimisés pour les appareils mobiles :
  - Pas de message interstitiel
  - Grands champs de formulaire
  - Navigation facile
  - Texte de grande taille
  - Beaucoup d'espace blanc
  - Corps de texte court et concis
  - Appels à l'action clairs

### Limites de caractères de l'accroche

  |   Client e-mail mobile  |  Limite  |
  |:----------------------:|:-------:|
  | Outlook iOS            | 74      |
  | Android natif         | 43      |
  | Gmail Android          | 24      |
  | iOS natif             | 82      |
  | Gmail iOS              | 30      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

  |  Client e-mail desktop  |  Limite  |
  |:----------------------:|:-------:|
  | Apple Mail             | 33      |
  | Outlook '13            | 38      |
  | Outlook pour Mac '15   | 53      |
  | Outlook '16            | 50      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }


  |  Client e-mail webmail  |  Limite  |
  |:----------------------:|:-------:|
  | AOL Mail               | 81      |
  | Gmail                  | 119     |
  | Outlook.com            | 49      |
  | Office 365             | 40      |
  | Mail.ru                | 64      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Taille de l'e-mail

Veillez à limiter la taille de vos e-mails. Les corps d'e-mails de plus de 102&nbsp;Ko sollicitent fortement les serveurs de Braze et sont également tronqués par Gmail et d'autres clients de messagerie. Essayez de maintenir la taille de votre e-mail en dessous de 25&nbsp;Ko pour du texte seul, ou de 60&nbsp;Ko avec des images. Nous vous recommandons vivement d'utiliser notre outil de chargement d'images pour héberger vos images et d'y faire référence via la balise `href`.

|   Texte uniquement   | Texte avec images |     Largeur de l'e-mail    |
|:-------------:|:----------------:|:------------------:|
| 25&nbsp;Ko maximum |   60&nbsp;Ko maximum   | 600 pixels maximum |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Pour enregistrer votre campagne ou votre modèle d'e-mail, assurez-vous que le corps de votre e-mail ne dépasse pas 400&nbsp;Ko.
{% endalert %}

## Longueur du texte

Reportez-vous au tableau suivant pour connaître les longueurs de texte recommandées.

| Spécifications du texte | Propriétés recommandées |
| --- | --- |
| Longueur de la ligne d'objet | 35 caractères maximum (pour un affichage optimal sur mobile) (6 à 10 mots) |
| Longueur du nom de l'expéditeur | 25 caractères maximum (pour un affichage optimal sur mobile) |
| Longueur de l'accroche | 85 caractères maximum |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Taille des images

Reportez-vous au tableau suivant pour connaître les tailles d'images recommandées. Les images plus petites et de haute qualité se chargent plus rapidement : utilisez donc la plus petite ressource possible pour obtenir le rendu souhaité.

|     Taille    | Largeur de l'image d'en-tête |  Largeur de l'image du corps  |   Types de fichiers  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| 5&nbsp;Mo maximum | 600 pixels maximum | 480 pixels maximum | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Création de liens profonds

Avec les notifications push et les messages in-app, un [lien profond]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) amène l'utilisateur directement vers une destination spécifique dans l'application. Cependant, les liens profonds nécessitent que l'application soit installée, et les e-mails ne permettent pas de savoir si les destinataires disposent de l'application. Les liens profonds dans les e-mails peuvent donc générer des erreurs pour les destinataires qui n'ont pas installé l'application.

Utilisez plutôt les [liens universels et App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links), qui fonctionnent comme des URL standard. Vous pouvez les configurer pour ouvrir l'application ou diriger les utilisateurs vers une page spécifique. Ils peuvent également rediriger vers l'app store ou afficher une page web de secours lorsque l'application n'est pas installée.