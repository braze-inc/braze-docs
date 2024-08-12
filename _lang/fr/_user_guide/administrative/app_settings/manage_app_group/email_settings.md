---
nav_title: Paramètres d’e-mail
article_title: Paramètres d’e-mail
page_type: reference
page_order: 3
description: "Cet article de référence couvre les paramètres d’e-mail dans le tableau de bord de Braze, y compris les configurations d’envoi, les pixels de suivi d’ouverture, la page et les pieds de page d’abonnement, etc."
tool: Dashboard
channel: email

---

# Paramètres d’e-mail

> Les paramètres d’e-mail sont disponibles dans la page **Manage Settings (Gérer les paramètres)** du tableau de bord. Braze vous permet ici de définir des paramètres d’e-mail sortants spécifiques comme les pieds de page personnalisés, les pages d’abonnement et de désabonnement personnalisées, etc. Inclure ces options dans vos e-mails sortants permet d’offrir une expérience client fluide et cohérente.

## Configuration de l’envoi

Les paramètres de messagerie dans la section **Sending Configuration (Configuration d’envoi)** déterminent les détails qui seront inclus dans vos campagnes d’e-mails. Ces paramètres concernent notamment ce que vos utilisateurs voient quand ils reçoivent un e-mail de Braze.

### Paramètres d’e-mail sortant

Lorsque vous configurez vos paramètres de messagerie, vos paramètres d’e-mails sortants identifient le nom et les adresses utilisées quand Braze envoient des courriers électroniques à vos utilisateurs.

{% tabs local %}
{% tab Display Name Address %}

Dans cette section, vous pouvez ajouter les noms et adresses e-mail à utiliser quand Braze envoie des e-mails à vos utilisateurs. Les noms et adresses mail affichés seront disponibles dans les options **Edit Sending Info (Modifier les informations d’envoi)** quand vous définirez votre campagne d’envoi d’e-mails.

![]({% image_buster /assets/img/email_settings/display_name_address.png %})

Lorsque vous définissez vos adresses d’expéditeur, assurez-vous que votre domaine d’e-mail « De » correspond à votre domaine d’envoi (c.-à-d., marketing.yourdomain.com). Le non-respect de cette consigne peut entraîner un mauvais alignement SPF et DKIM. Tous les e-mails Reply-to (Répondre à) peuvent être définis sur votre domaine racine.

{% endtab %}
{% tab Reply-To Address %}

L’ajout d’une adresse e-mail dans cette section vous permet de la sélectionner en tant qu’adresse de réponse pour votre campagne d’e-mails. Vous pouvez également définir une adresse e-mail comme adresse par défaut en sélectionnant **Make Default (Par défaut)**. Ces adresses seront disponibles lors de la création de votre campagne via les options **Edit Sending Info (Modifier les informations d’envoi)** disponibles lorsque vous composez votre campagne d’e-mails.

![]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab BCC Address %}

Cette section vous permet d’ajouter et de gérer des adresses CCI pouvant être ajoutées aux messages e-mail sortants envoyés par Braze. L’ajout d’une adresse CCI à un message e-mail enverra une copie identique du message que votre utilisateur reçoit dans votre boîte de réception CCI. Il s’agit d’un outil utile pour conserver des copies des messages que vous avez envoyés à vos utilisateurs pour les exigences de conformité ou les problèmes de support client.

{% alert important %} 
Les paramètres **BCC Address** (Adresse CCI) sont actuellement en accès privilégié. L’ajout d’une adresse CCI à votre campagne ou à votre Canvas aura pour effet de doubler vos e-mails facturables pour la campagne ou le composant de Canvas puisque Braze enverra un message à votre utilisateur et un autre à votre adresse CCI. Contactez votre gestionnaire du succès des clients ou créez un [ticket d’assistance]({{site.baseurl}}/braze_support/) pour activer cette fonctionnalité.
{% endalert %}

![Section BCC Address (Adresse CCI) de l’onglet Email Settings (Paramètres d’e-mail).]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

Une fois que vous avez ajouté une adresse, celle-ci sera disponible pour être sélectionnée lors de la composition d’un e-mail dans les campagnes ou les Canvas steps. Sélectionnez **Make Default (Définir par défaut)** à côté d’une adresse pour définir cette adresse comme adresse par défaut lors du lancement d’une nouvelle campagne d’e-mail ou d’un nouveau composant Canvas. Si vous souhaitez changer cela au niveau du message, vous pouvez sélectionner **No BCC (Pas de CCI)** lors de la configuration de votre message.

Si vous avez besoin que tous les messages d’e-mail envoyés par Braze aient une adresse CCI, vous pouvez cocher l’option **Require a BCC address for all your email campaigns (Adresse CCI obligatoire pour toutes les campagnes d’e-mail).** Vous devrez alors sélectionner une adresse par défaut qui sera automatiquement sélectionnée sur les nouvelles campagnes d’e-mail ou les Canvas steps. L’adresse par défaut sera également automatiquement ajoutée à tous les messages déclenchés via notre API REST. Il n’est pas nécessaire de modifier la demande API existante pour inclure l’adresse.

{% endtab %}
{% endtabs %}

## Pixel de suivi de l’ouverture d’e-mail

[![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

Le pixel de suivi d’ouverture de messagerie est une image de 1 px par 1 px invisible qui est automatiquement insérée dans votre e-mail HTML. Ce pixel aide Braze à détecter si les utilisateurs finaux ont ouvert votre e-mail. Les informations sur l’ouverture des e-mails peuvent être très utiles, car elles aident les utilisateurs à déterminer des stratégies de marketing efficaces en comprenant les taux d’ouverture correspondants.

### Placement du pixel de suivi

Le comportement par défaut de Braze consiste à ajouter le pixel de suivi au bas de votre e-mail. Pour la grande majorité des utilisateurs, c’est l’endroit idéal pour placer le pixel. Bien que le pixel soit déjà conçu pour provoquer le moins de différences visuelles possible, tout changement visuel involontaire sera le moins visible au bas de l’e-mail. C’est également la valeur par défaut pour les fournisseurs d’e-mail tels que SendGrid et SparkPost.

### Modification de l’emplacement du pixel de suivi

Braze prend actuellement en charge le remplacement de l’emplacement par défaut du pixel de suivi d’ouverture par défaut de l’ESP (la dernière balise dans le `<body>` d’un e-mail) pour le déplacer vers la première balise dans le `<body>`.
  
![][13]{: style="max-width:80%;" }

Pour modifier l’emplacement :
1. Allez à **Manage App Group (Gérer le groupe d’apps)**, puis **Email Settings (Paramètres d’e-mail)** sur votre compte Braze.
2. Cocher la case sous **Custom Open Tracking Pixel Settings (Paramètres de pixel de suivi ouverts personnalisés)**. 
3. Cliquer sur **Save (Enregistrer)**.

Une fois enregistré, Braze enverra des instructions spéciales à l’ESP afin de placer le pixel de suivi ouvert en haut de tous les e-mails HTML.
  
{% alert important %} 
L’activation SSL enveloppera l’URL du pixel de suivi avec HTTPS au lieu de HTTP. Si votre SSL est mal configuré, cela peut affecter l’efficacité du pixel de suivi. 
{% endalert %}

## Inclure un en-tête de désabonnement de liste

![][00]{: style="float:right;max-width:60%;margin-left:15px;"}

Cette fonctionnalité vous permet d’inclure automatiquement un en-tête de désabonnement de liste pour les e-mails envoyés aux utilisateurs abonnés ou ayant choisi de s’abonner. Cet en-tête permet aux fournisseurs d’e-mails d’inclure un bouton **Unsubscribe (Se désabonner)** lorsque vous affichez un e-mail.

Certains destinataires préfèrent disposer d’un lien de désabonnement disponible au même endroit pour tous les e-mails, au lieu de devoir trouver des liens dans chaque e-mail. Lorsque cette fonctionnalité est activée, un lien de désabonnement visible dans l’en-tête du client de messagerie apparaît, ce qui facilite le désabonnement et diminue ainsi le risque qu’un utilisateur signale votre e-mail comme étant un spam. Cela peut avoir un impact significatif sur votre réputation et votre délivrabilité en tant qu’expéditeur de courrier électronique.

### Fonctionnement de l’en-tête de désabonnement de la liste

Quand elle est activée, cette fonctionnalité s’applique à l’ensemble du Groupe d’Apps. Braze ajoutera un en-tête « mailto: » standard pour se désabonner de la liste à tous les e-mails sortants admissibles. Cet en-tête de désabonnement n’est pas personnalisable. Après avoir reçu une demande de désabonnement de liste d’un utilisateur, Braze s’assurera que cet utilisateur est désabonné. S’il n’y a pas de correspondance, Braze ne traitera pas cette demande. 

![Option pour inclure automatiquement un en-tête de désabonnement de liste pour les e-mails envoyés aux utilisateurs abonnés ou ayant choisi de s’abonner.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %}){: style="max-width:70%;" }

Notez que l’en-tête n’est pas ajouté pour les messages ciblant tous les utilisateurs, y compris les utilisateurs non abonnés, car ce sont des messages transactionnels qui ne nécessitent pas de fonction de désabonnement.

### Disponibilité

Actuellement, seuls Windows Live Hotmail et Gmail prennent en charge l’en-tête de désabonnement de liste. De plus, ces fournisseurs de services d’e-mail peuvent ne pas vous proposer cette fonctionnalité si vous n’avez pas encore effectué de [réchauffement d’adresses IP]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/) ou si vous êtes un nouvel expéditeur. La raison en est que des fournisseurs comme Gmail n’incluront pas l’option de désabonnement s’ils n’ont pas confiance dans le fait que vous allez effectivement désinscrire l’utilisateur.

## Ajout aux lignes d’objet de l’e-mail

Utilisez la bascule pour inclure « [TEST] » et « [SEED] » dans les lignes d’objet de vos e-mails de test et de seed. Cela peut vous aider à identifier les campagnes par e-mail envoyées en tant que tests.

![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;" }

## Option par défaut Inlining CSS pour les nouveaux e-mails

L’inlining CSS est une technique qui intègre automatiquement les styles CSS pour vos e-mails et nouveaux e-mails. Pour certains clients de messagerie électronique, cela peut améliorer le rendu de vos e-mails.

La modification de ce paramètre n’affectera pas vos e-mails existants ou les modèles. Vous pouvez remplacer cette valeur par défaut à tout moment lors de la composition de vos messages ou modèles. Pour plus d’informations, consultez [Inlining CSS][10].

## Réabonnez les utilisateurs lorsque leurs e-mails changent

Vous pouvez réabonner automatiquement les utilisateurs lorsqu’ils changent leur adresse e-mail. Par exemple, si un utilisateur d’un groupe d’apps précédemment désabonné change son adresse e-mail pour une adresse qui ne figure pas sur la liste de désabonnement de Braze, il sera automatiquement réabonné.

![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Pages et pieds de page pour le désabonnement

{% tabs local %}
{% tab Custom Footer %}

Pour les e-mails commerciaux, la [CAN-SPAM Act (Loi CAN-SPAM)](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) exige que tous les e-mails commerciaux comprennent une option de désabonnement. Grâce aux paramètres de pied de page personnalisés, vous pouvez rester conforme à la loi CAN-SPAM tout en personnalisant votre pied de page de désabonnement par e-mail. Afin de rester conforme, vous devez ajouter votre pied de page personnalisé à tous les e-mails envoyés dans le cadre des campagnes pour ce groupe d’apps.

Notez les exigences suivantes lors de la création d’un pied de page personnalisé pour votre envoi de messages par e-mail :
- Doit inclure une URL de désabonnement et une adresse postale.
- Doivent faire moins de 100 Ko.

![]({% image_buster /assets/img/email_settings/custom_footer.png %})

Pour en savoir plus sur les modèles Liquid de pied de page personnalisés, consultez notre documentation sur les [Pieds de page personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

{% endtab %}
{% tab Custom Unsubscribe Page %}

Braze vous permet de définir une **page de désabonnement personnalisé** avec votre propre HTML. Cette page s’affiche une fois qu’un utilisateur a choisi de se désabonner du bas d’un e-mail. Notez que cette page doit faire moins de 750 Ko. 

![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

Pour en savoir plus sur les meilleures pratiques de gestion des listes d’e-mail, consultez la [Gestion des abonnements par e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% tab Custom Opt-In Page %}

Vous pouvez créer une page d’abonnement personnalisée à l’aide de votre propre HTML. Inclure cela dans votre e-mail peut être particulièrement bénéfique si vous voulez que votre branding et vos messages soient cohérents pendant toute la durée de vie de votre client. Notez que cette page doit faire moins de 750 Ko. 

![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

Pour en savoir plus sur les meilleures pratiques de gestion des listes d’e-mail, consultez la [Gestion des abonnements par e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% endtabs %}

[00]: {% image_buster /assets/img_archive/list_unsub_img1.png %}
[1]: {% image_buster /assets/img/email_settings/outbound_email.png %}
[2]: {% image_buster /assets/img/email_settings/switch.gif %}
[6]: https://learning.braze.com/email-open-tracking-pixel
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/
[13]: {% image_buster /assets/img/open_pixel.png %}
