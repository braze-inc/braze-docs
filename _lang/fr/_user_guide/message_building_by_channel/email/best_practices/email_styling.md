---
nav_title: Style des e-mails
article_title: Style des e-mails
page_order: 2
page_type: reference
description: "Le présent article décrit les meilleures pratiques relatives au style des messages pour vos campagnes par e-mail."
channel: E-mail

---

# Conseils pour le style de vos e-mails

## Style de l’adresse

La **Ligne d’Objet** est l’une des premières choses que les destinataires verront quand ils recevront votre message. Les lignes d’objet qui font 6 à 10 mots génèrent les meilleurs taux d’ouverture. 

Il y a différentes approches pour créer une bonne ligne d’objet : poser une question pour susciter l'intérêt du lecteur, être plus direct, la personnaliser pour mieux engager la clientèle… Ne vous contentez pas d’une seule ligne d’objet, utilisez les [Tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing/) pour en essayer plusieurs et déterminer leur efficacité. Pour s’afficher correctement sur mobile, les lignes d’objet ne doivent pas dépasser 35 caractères.

Le champ « De » doit indiquer clairement l’expéditeur. Essayez de ne pas utiliser le nom d’une personne ou une abréviation peu courante. Utilisez plutôt un nom reconnaissable, comme le nom de votre marque par exemple. Si l’utilisation du nom d’une personne correspond aux méthodes de personnalisation des e-mails de votre marque, restez cohérent pour développer une relation avec les destinataires. Pour s’afficher correctement sur mobile, le nom du champ « De » ne doit pas comporter plus de 25 caractères.

### Adresses « noreply »

Les adresses noreply ne sont généralement pas recommandées pour plusieurs raisons car elles désengagent vos clients. De nombreux destinataires répondent à l’e-mail pour se désabonner, donc s’ils ne sont pas autorisés à le faire, leur action suivant est souvent de marquer l’e-mail comme étant du spam. 

Les réponses automatiques (de type « absent du bureau ») peuvent en fait fournir des informations précieuses, améliorer les taux d’ouverture et diminuer les signalements de spam (en retirant ceux qui ne veulent pas recevoir d’e-mails). Au niveau personnel, un message avec « Ne pas répondre » peut paraitre impersonnel aux destinataires et les faire renoncer à recevoir d’autres e-mails de votre marque ou entreprise.

## Texte d’accroche

Dans un e-mail, le texte d’accroche doit communiquer efficacement le point essentiel du message pour capter l’intérêt du lecteur et l’encourager à ouvrir le message. Le texte d’accroche est également souvent utilisé par les marketeurs d’e-mail pour fournir des informations supplémentaires sur le contenu d’un e-mail. Le texte d’accroche est le texte de prévisualisation affiché immédiatement après l’objet de l’e-mail. Dans l’exemple suivant, l’accroche est `- Brand. New. Lounge Shorts`.

![accroche dans une boîte de réception Gmail avec le texte « Nouveaux Bermudas  confortables ».][61]

La quantité de texte d’accroche visible dépend du client d’e-mail de l’utilisateur et de la longueur de la ligne objet de l’e-mail. En général, nous recommandons que les accroches d’e-mail fassent entre 50 et 100 caractères.

Voici quelques bonnes pratiques à garder à l’esprit au moment de rédiger vos accroches :

1. Les CTA (appels à l’action) entrent en jeu une fois que les lecteurs ont ouvert votre e-mail.
  - Pointez vos lecteurs dans la bonne direction, que vous souhaitiez qu’ils s’abonnent, achètent un produit ou consultent votre site Internet.
  - Utilisez des mots forts pour que le lecteur sache exactement ce que vous lui demandez, mais veillez à refléter la voix de la marque de votre entreprise et faites en sorte que chaque appel à l’action fournisse une certaine valeur au consommateur.
  - L’accroche ne doit pas faire plus de 85 caractères, et elle doit avoir une sorte d’appel à l’action descriptif lié à la ligne Objet.

2. Les adresses e-mail et les sites vers lesquels vous dirigez vos utilisateurs doivent être optimisés pour le mobile :
  - Pas de message interstitiel
  - Grands champs sur le formulaire
  - Navigation facile
  - Grand texte
  - Beaucoup d’espace vide
  - Corps du message bref et concis
  - Appels à l’action clairs 

### Limites de caractères de l’accroche

  |   Client par e-mail mobile  |  Limite  |
  |:----------------------:|:-------:|
  | Outlook iOS            | 74      |
  | Android natif          | 43      |
  | Gmail Android          | 24      |
  | iOS Natif             | 82      |
  | Gmail iOS              | 30      |
  {: .reset-td-br-1 .reset-td-br-2}

  |  Client par e-mail Desktop  |  Limite  |
  |:----------------------:|:-------:|
  | Apple Mail             | 33      |
  | Outlook ’13            | 38      |
  | Outlook pour Mac ’15   | 53      |
  | Outlook ’16            | 50      |
  {: .reset-td-br-1 .reset-td-br-2}


  |  Client par e-mail Webmail  |  Limite  |
  |:----------------------:|:-------:|
  | AOL Mail               | 81      |
  | Gmail                  | 119     |
  | Outlook.com            | 49      |
  | Office 365             | 40      |
  | Mail.ru                | 64      |
  {: .reset-td-br-1 .reset-td-br-2}

## Taille e-mail

Assurez-vous de limiter la taille de vos e-mails. Les corps d’e-mails de plus de 102 Ko risquent de surcharger les serveurs de Braze et SendGrid, et ils sont en outre tronqués par Gmail et d’autres clients par e-mail. Essayez de garder la taille de votre e-mail inférieure à 25 Ko pour les messages « texte uniquement » et inférieure à 60 Ko pour les messages avec images. Nous vous encourageons fortement à utiliser le téléchargeur d’images de Braze pour héberger vos images et à référencer ces images par leur `href`.

|   Texte uniquement   | Texte avec images |     Largeur de l’e-mail    |
|:-------------:|:----------------:|:------------------:|
| 25 Ko maximum |   60 Ko maximum   | 600 pixels maximum |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Longueur du texte

Reportez-vous au tableau suivant pour connaître les longueurs de texte recommandées.

| **Spécifications du texte** | **Propriétés recommandées** |
| --- | --- |
| Longueur de la ligne d'objet | 35 caractères maximum (pour un affichage optimal sur mobile) (6 à 10 mots) |
| Longueur du nom de l’expéditeur | 25 caractères maximum (pour un affichage optimal sur mobile) |
| Longueur de l’accroche | 85 caractères maximum |
{: .reset-td-br-1 .reset-td-br-2}

## Taille de l’image

Reportez-vous au tableau suivant pour connaître les tailles d’images recommandées. Les images plus petites et de haute qualité se chargeront plus rapidement, donc utilisez la plus petite ressource possible pour obtenir le rendu souhaité.

|     Taille    | Largeur d’image de l’en-tête |  Largeur de l’image du corps  |   Types de fichiers  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| 5 Mo maximum | 600 pixels maximum | 480 pixels maximum | PNG, JPG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Création de liens profonds

Aujourd’hui, une grande partie des e-mails sont lus sur des appareils mobiles. L’utilisation du [« deep linking » (liens profonds)]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) est une bonne pratique pour engager les destinataires qui lisent leurs e-mails sur mobile Avec les notifications push et les messages in-app, un lien profond amène l’utilisateur directement à une destination spécifiée dans l’application. 

Cependant, les e-mails ne permettent pas de savoir si les destinataires ont installé l’application. Et donc éviter le lien profond permet d’empêcher les messages d’erreur pour les destinataires d’e-mails qui n’ont pas l’application.

[25]: {{site.baseurl}}/help/best_practices/user_onboarding/#user-onboarding
[61]: {% image_buster /assets/img_archive/preheader_example.png %}
