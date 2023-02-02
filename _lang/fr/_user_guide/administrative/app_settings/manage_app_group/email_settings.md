---
nav_title: Paramètres d’e-mail
article_title: Paramètres d’e-mail
page_type: reference
page_order: 3
description: "Cet article de référence couvre les paramètres d’e-mail du tableau de bord de Braze."
tool: Tableau de bord
channel: e-mail

---

# Paramètres d’e-mail

Les paramètres d’e-mail sont disponibles dans la page **Manage Settings** (Gérer les paramètres) du tableau de bord. Braze vous permet ici de définir des paramètres d’e-mail sortants spécifiques comme le nom d’affichage, l’adresse de réponse, les pieds de page personnalisés, les pages d’abonnement et de désabonnement personnalisées, etc. L’intégration de telles fonctionnalités dans vos e-mails sortants permet d’offrir une expérience client fluide et cohérente.

## Paramètres d’e-mail sortant

### Envoi multiple d’e-mails

Utilisez les paramètres d’e-mails sortants suivants pour modifier le nom et l’adresse e-mail utilisés lorsque Braze envoie des e-mails à vos utilisateurs. En utilisant ces paramètres, vous pouvez également inclure des adresses d’envoi et de réponse supplémentaires. Ces adresses seront disponibles lors de la création de votre campagne par le biais des options **Edit Sending Info** (Modifier les informations d’envoi) disponibles lorsque vous composez votre e-mail de campagne.

Ici, vous pouvez également exclure l’e-mail « Reply-To » (Répondre à) et envoyer exclusivement les réponses à l’adresse « From » (De).

![Section Paramètres d’e-mail sortant de l’onglet Paramètres d’e-mail.][1]

Cette fonction vous permet de :

- Configurer plusieurs adresses e-mail d’envoi et de réponse
- Définir une adresse d’envoi et de réponse par défaut
- Exclure l’option de réponse et envoyer les réponses à l’adresse « From » (De)

Lorsque vous définissez vos adresses d’expéditeur, assurez-vous que votre domaine d’e-mail « From » (De) correspond à votre domaine d’envoi (c.-à-d. marketing.yourdomain.com). Le non-respect de cette consigne peut entraîner un mauvais alignement SPF et DKIM. Tous les e-mails Reply-to (Répondre à) peuvent être définis sur votre domaine racine.

### Adresses CCI

Les paramètres **BCC Address** (Adresse CCI) vous permettent d’ajouter et de gérer des adresses CCI pouvant être ajoutées aux messages e-mail sortants envoyés par Braze. L’ajout d’une adresse CCI à un message e-mail enverra une copie identique du message que votre utilisateur reçoit dans votre boîte de réception CCI. Il s’agit d’un outil utile pour conserver des copies des messages que vous avez envoyés à vos utilisateurs pour les exigences de conformité ou les problèmes de support client.

{% alert important %} 
Les paramètres **BCC Address** (Adresse CCI) sont actuellement en accès privilégié. L’ajout d’une adresse CCI à votre campagne ou à votre Canvas aura pour effet de doubler vos e-mails facturables pour la campagne ou le composant de Canvas puisque Braze enverra un message à votre utilisateur et un autre à votre adresse CCI. Contactez votre gestionnaire du succès des clients ou créez un [ticket d’assistance]({{site.baseurl}}/braze_support/).
{% endalert %}

![Section Adresse CCI de l’onglet Paramètres d’e-mail.][11]

Une fois que vous avez ajouté une adresse, celle-ci sera disponible pour être sélectionnée lors de la composition d’un e-mail dans les campagnes ou les Canvas steps. Sélectionnez **Définir par défaut** à côté d’une adresse pour définir cette adresse à sélectionner par défaut lors du lancement d’une nouvelle campagne d’e-mail ou composant de Canvas. Si vous souhaitez remplacer cela au niveau du message, vous pouvez sélectionner **No BCC** (Pas de CCI) lors de la configuration de votre message.

Si vous exigez que tous les messages d’e-mail envoyés par Braze aient une adresse CCI, vous pouvez cocher l’option **Require a BCC address for all your email campaigns** (Exiger une adresse CCI pour toutes vos campagnes d’e-mail). Vous devrez alors sélectionner une adresse par défaut qui sera automatiquement sélectionnée sur les nouvelles campagnes d’e-mail ou les Canvas steps. L’adresse par défaut sera également automatiquement ajoutée à tous les messages déclenchés via notre API REST. 

Il n’est pas nécessaire de modifier la demande API existante pour inclure l’adresse. Si vous cochez la case CCI dans le tableau de bord de Braze, l’adresse sera définie au moment de l’envoi.  

![][12]

### Pied de page personnalisé

Pour les e-mails commerciaux, la [Loi CAN-SPAM][5] exige que tous les e-mails commerciaux comprennent une option de désabonnement. Grâce aux paramètres de pied de page personnalisés, vous pouvez rester conforme à la loi CAN-SPAM tout en personnalisant votre pied de page de désabonnement par e-mail. Afin de rester conforme, vous devez ajouter votre pied de page personnalisé à tous les e-mails envoyés dans le cadre des campagnes pour ce groupe d’apps.

![][0]

Pour en savoir plus sur les modèles Liquid de pied de page personnalisés, consultez notre documentation sur les [Pieds de page personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

Notez les exigences suivantes lors de la création d’un pied de page personnalisé pour votre messagerie électronique :

- Doit inclure une URL de désabonnement et une adresse postale.
- Doit être inférieur à 100 Ko.

Pour en savoir plus sur les meilleures pratiques par e-mail, consultez [Gestion des abonnements par e-mail][7].

## Pages personnalisées

### Se désabonner

Braze vous permet de définir une **page de désabonnement personnalisé** avec votre propre HTML. Cette page s’affiche une fois qu’un utilisateur a choisi de se désabonner du bas d’un e-mail.

![][3]

Notez que cette page doit être inférieure à 750 Ko. Pour en savoir plus sur les meilleures pratiques de gestion des listes d’e-mail, consultez [Gestion des abonnements par e-mail][7].

### Abonnement

Vous pouvez créer une page d’abonnement personnalisée à l’aide de votre propre HTML. Cette fonctionnalité est excellente si vous souhaitez que votre marque et votre message restent cohérents tout au long du cycle de vie de votre utilisateur.

![][4]

Notez que cette page doit être inférieure à 750 Ko. Pour en savoir plus sur les meilleures pratiques de gestion des listes d’e-mail, consultez [Gestion des abonnements par e-mail][7].

## Pixel de suivi de l’ouverture d’e-mail

[![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

Le pixel de suivi d’ouverture de messagerie est une image de 1 px par 1 px invisible qui est automatiquement insérée dans votre e-mail HTML. Ce pixel aide Braze à détecter si les utilisateurs finaux ont ouvert votre e-mail. Les informations sur l’ouverture des e-mails peuvent être très utiles, car elles aident les utilisateurs à déterminer des stratégies de marketing efficaces en comprenant les taux d’ouverture correspondants.

### Placement du pixel de suivi

Le comportement par défaut de Braze consiste à ajouter le pixel de suivi au bas de votre e-mail. Pour la grande majorité des utilisateurs, c’est l’endroit idéal pour positionner le pixel. Bien que le pixel soit déjà conçu pour provoquer le moins de différences visuelles possible, tout changement visuel involontaire sera le moins visible au bas de l’e-mail. C’est également la valeur par défaut pour les fournisseurs d’e-mail tels que SendGrid et SparkPost.

Toutefois, un petit nombre d’entreprises peuvent préférer que le pixel soit placé à un autre endroit. L’avantage de ne pas placer le pixel de suivi en bas évite les cas où il est coupé par des clients (p. ex., Gmail) qui tronquent les e-mails après une certaine quantité de kilo-octets.

### Modification de l’emplacement du pixel de suivi

Braze prend actuellement en charge le remplacement de l’emplacement par défaut du pixel de suivi d’ouverture par défaut de l’ESP (la dernière balise dans le <body> d’un e-mail) pour le déplacer vers la première balise dans le <body>.
  
![Paramètres de pixel de suivi ouverts personnalisés][13]

Pour modifier l’emplacement :
1. Allez à **Manage App Group** (Gérer le groupe d’apps), puis **Email Settings** (Paramètres d’e-mail) sur votre compte Braze.
2. Cocher la case sous **Custom Open Tracking Pixel Settings** (Paramètres de pixel de suivi ouverts personnalisés). 
3. Cliquer sur **Save** (Enregistrer).

Une fois enregistré, Braze enverra des instructions spéciales à l’ESP afin de placer le pixel de suivi ouvert en haut de tous les e-mails HTML.
  
{% alert important %} 
L’activation SSL enveloppera l’URL du pixel de suivi avec HTTPS au lieu de HTTP - si votre SSL est mal configuré, cela peut affecter l’efficacité du pixel de suivi. 
{% endalert %}
  
## Fonctions pouvant être activées par basculement

![][2]{: style="float:right;max-width:30%;margin-left:15px;"}

Les trois paramètres d’e-mail répertoriés sont des fonctions qui ne nécessitent aucune action autre que le basculement activé ou désactivé à l’aide du bouton correspondant. Lisez chaque paramètre pour plus de détails.

### Réabonnez les utilisateurs lorsque leurs e-mails changent

Vous pouvez réabonner automatiquement les utilisateurs lorsqu’ils changent leur adresse e-mail. Par exemple, si un utilisateur d’un groupe d’applications précédemment désabonné change son adresse électronique pour une adresse qui ne figure pas sur la liste de désabonnement de Braze, il sera automatiquement réabonné.

Pour en savoir plus sur les meilleures pratiques de gestion des listes d’e-mail, consultez [Gestion des abonnements par e-mail][7].

### Inclure un en-tête de désabonnement de liste

![][00]{: style="float:right;max-width:60%;margin-left:15px;"}

Cette fonction vous permet d’inclure automatiquement un en-tête de désabonnement de liste pour les e-mails envoyés aux utilisateurs abonnés ou ayant choisi de s’abonner. Cet en-tête permet aux fournisseurs d’e-mails d’inclure un bouton **Unsubscribe** (Se désabonner) lorsque vous affichez un e-mail.

Certains destinataires préfèrent disposer d’un lien de désabonnement disponible au même endroit pour tous les e-mails, au lieu de devoir trouver des liens dans chaque e-mail. Lorsque cette fonctionnalité est activée, un lien de désabonnement visible dans l’en-tête du client de messagerie apparaît, ce qui facilite le désabonnement et diminue ainsi le risque que les clients signalent votre e-mail comme spam. Cela a un impact significatif sur votre réputation et votre délivrabilité en tant qu’expéditeur de courrier électronique.

#### Disponibilité

Actuellement, seuls Windows Live Hotmail et Gmail prennent en charge l’en-tête de désabonnement de liste. De plus, ces fournisseurs de services d’e-mail peuvent ne pas vous proposer cette fonctionnalité si vous n’avez pas encore effectué de [réchauffement d’adresses IP]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/) ou si vous êtes un nouvel expéditeur. La raison en est que des fournisseurs comme Gmail n’incluront pas l’option de désabonnement s’ils n’ont pas confiance dans le fait que vous allez effectivement désinscrire l’utilisateur.

#### Fonctionnement de l’en-tête de désabonnement de la liste

Naviguer vers **Email Settings** (Paramètres d’e-mail) au sein de votre groupe d’apps. Basculer **List-Unsubscribe** (Liste-désabonnement) vers **ON** (Activé).

![Option pour inclure automatiquement un en-tête de désabonnement de liste pour les e-mails envoyés aux utilisateurs abonnés ou ayant choisi de s’abonner.] [59]

Lorsqu’elle est activée, cette fonction ajoute un en-tête standard de liste de désabonnement « mailto: » à tous les e-mails sortants admissibles. Après avoir reçu une demande de désabonnement de liste d’un utilisateur, Braze s’assurera que cet utilisateur est désabonné. S’il n’y a pas de correspondance, Braze ne traitera pas cette demande.

{% alert note %}
Cette fonction s’applique uniquement aux e-mails qui ciblent les utilisateurs qui sont « abonnés ou souhaitent s’abonner » ou « souhaitant s’abonner uniquement ».
{% endalert %}

L’en-tête n’est pas ajouté pour les messages ciblant tous les utilisateurs, y compris les utilisateurs non abonnés, car ceux-ci représentent des messages transactionnels qui n’ont pas besoin d’une fonction de désabonnement.

Notez qu’actuellement, seuls Windows Live Hotmail et Gmail prennent en charge cette fonctionnalité.

### Option par défaut Inlining CSS pour les nouveaux e-mails

L’inlining CSS est une technique qui intègre automatiquement les styles CSS pour vos e-mails et nouveaux e-mails. Pour certains clients de messagerie électronique, cela peut améliorer le rendu de vos e-mails.

La modification de ce paramètre n’affectera pas vos e-mails existants ou les modèles. Vous pouvez remplacer cette valeur par défaut à tout moment lors de la composition de vos messages ou modèles.

Pour plus d’informations, consultez l’[Insertion CSS][10].

[00]: {% image_buster /assets/img_archive/list_unsub_img1.png %}
[0]: {% image_buster /assets/img/email_settings/custom_footer.png %}
[1]: {% image_buster /assets/img/email_settings/outbound_email.png %}
[2]: {% image_buster /assets/img/email_settings/switch.gif %}
[3]: {% image_buster /assets/img/email_settings/custom_unsubscribe.png %}
[4]: {% image_buster /assets/img/email_settings/custom_opt_in.png %}
[5]: https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003
[6]: https://learning.braze.com/email-open-tracking-pixel
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/
[11]: {% image_buster /assets/img/email_settings/bcc_address.png %}
[12]: {% image_buster /assets/img/email_settings/require_bcc.png %}
[13]: {% image_buster /assets/img/open_pixel.png %}
[59]: {% image_buster /assets/img_archive/list_unsub_img3_new.png %}
