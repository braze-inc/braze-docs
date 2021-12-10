---
nav_title: Paramètres de messagerie
article_title: Paramètres de messagerie
page_type: Référence
page_order: 3
description: "Cet article de référence couvre les paramètres de messagerie dans le tableau de bord de Braze."
tool: Tableau de bord
channel: Email
---

# Paramètres de l'e-mail

Les paramètres de messagerie peuvent être trouvés dans la page **Gérer les paramètres** du tableau de bord. Ici, Braze vous permet de définir des paramètres spécifiques d'e-mail sortant tels que le nom de l'affichage, l'adresse de réponse, les pieds de page personnalisés, les pages d'opt-in et d'opt-out, et plus encore. Inclure des fonctionnalités comme celles-ci dans vos courriels sortants est une expérience client fluide et cohérente.

## Paramètres de messagerie sortante

### E-mails d'envoi multiple

Utilisez les paramètres des courriels sortants ci-dessous pour changer le nom et l'adresse e-mail utilisés lorsque Braze envoie des courriels à vos utilisateurs. En utilisant ces paramètres, vous pouvez également inclure des adresses d'envoi et de réponse supplémentaires. Ces adresses seront disponibles lors de la création de votre campagne par le biais des options **Modifier les infos d'envoi** disponibles au fur et à mesure que vous écrivez votre e-mail de campagne.

Ici, vous pouvez également exclure l'e-mail "Répondre à" et envoyer exclusivement des réponses à l'adresse "De".

!\[Courriel sortant\]\[1\]

Cette fonctionnalité vous permet de :

- Configurer plusieurs adresses e-mail d'envoi et de réponse
- Définir une adresse d'envoi et de réponse par défaut
- Exclure l'option de réponse et envoyer les réponses à l'adresse "De"

Lorsque vous définissez vos adresses "De", assurez-vous que votre domaine de messagerie "De" correspond à votre domaine d'envoi (c.-à-d. marketing.yourdomain.com). Si vous ne le faites pas, cela peut entraîner un déséquilibre entre SPF et DKIM. Tous les e-mails de réponse peuvent être configurés sur votre domaine racine.

### Adresses BCC

Les paramètres d'adresse **BCC** vous permettent d'ajouter et de gérer les adresses BCC qui peuvent être ajoutées aux messages envoyés depuis Braze. L'ajout d'une adresse BCC à un message électronique enverra une copie identique du message que votre utilisateur reçoit à votre boîte de réception BCC. Il s'agit d'un outil utile pour conserver des copies des messages que vous avez envoyés à vos utilisateurs pour des problèmes de conformité ou d'assistance à la clientèle.

{% alert important %}
Les paramètres d'adresse **BCC** sont actuellement en accès anticipé. L'ajout d'une adresse BBC à votre campagne ou à Canvas entraînera le doublement de vos courriels de billabe pour l'étape de la campagne ou de Canvas puisque Braze enverra un message à votre utilisateur et un message à votre adresse BCC. Veuillez contacter votre Customer Success Manager ou ouvrir un [ticket de support]({{site.baseurl}}/braze_support/) pour activer cette fonctionnalité.
{% endalert %}

!\[Adresse BCC\]\[11\]

Une fois que vous ajoutez une adresse, l'adresse sera mise à votre disposition pour la sélection lors de la rédaction d'un courriel dans les étapes des campagnes ou des étapes de Canvas . Sélectionnez **Faire la valeur par défaut** à côté d'une adresse pour définir cette adresse à sélectionner par défaut lors du lancement d'une nouvelle campagne d'email ou d'une étape de Canvan. Si vous souhaitez remplacer cela au niveau du message, vous pouvez sélectionner **No BCC** lors de la configuration de votre message.

Si vous avez besoin que tous les courriels envoyés depuis Braze contiennent une adresse BCC, vous pouvez vérifier **Nécessite une adresse BCC pour toutes vos campagnes e-mail**. Cela vous demandera de sélectionner une adresse par défaut qui sera automatiquement sélectionnée pour les nouvelles campagnes de courriel ou les étapes de Canvas . L'adresse par défaut sera également automatiquement ajoutée à tous les messages déclenchés par notre API REST.

Il n'est pas nécessaire de modifier la requête API existante pour inclure l'adresse. Cocher la case dans le tableau de bord de Braze pour exiger la BCC définira l'adresse au moment de l'envoi.

!\[Require BCC\]\[12\]

### Pied de page personnalisé

Pour les e-mails commerciaux, le [CAN-SPAM Act][5] exige que tous les e-mails commerciaux incluent une option de désinscription. Avec les paramètres de pied de page personnalisés, vous pouvez rester conforme à la norme CAN-SPAM tout en personnalisant le pied de page de votre boîte de réception. Afin de rester conforme, vous devez ajouter votre pied de page personnalisé à tous les e-mails envoyés dans le cadre de campagnes pour ce groupe d'applications. Pour en savoir plus sur le modèle Liquid de pied de page personnalisé, consultez notre [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

!\[Pied de page personnalisé\]\[0\]

Exigences:

- Doit inclure une URL de désinscription et une adresse d'envoi physique.
- Les pieds de page personnalisés doivent être inférieurs à 100 Ko.

En savoir plus sur les meilleures pratiques de messagerie [ici][7].

## Page de désinscription personnalisée

Dans les paramètres de l'e-mail, Braze vous permet de définir une **page de désinscription personnalisée**. Cette page sera visible une fois qu'un utilisateur aura choisi de se désabonner à partir du bas d'un e-mail. Cette fonctionnalité est idéale si vous voulez que votre image de marque et votre message restent cohérents tout au long du cycle de vie de votre utilisateur.

!\[Désinscription personnalisée\]\[3\]

Exigences:

- Vous devez fournir votre propre HTML pour cette fonctionnalité.
- Les pages de désinscription doivent être inférieures à 750KB.

En savoir plus sur les meilleures pratiques de gestion des listes d'e-mails [ici][7].

## Page opt-in personnalisée

Dans les paramètres de l'e-mail, Braze vous permet de définir une page d'activation personnalisée. Cette fonctionnalité est idéale si vous voulez que votre image de marque et votre message restent cohérents tout au long du cycle de vie de votre utilisateur.

![Opt-in personnalisé[4]

Exigences:

- Vous devez fournir votre propre HTML pour cette fonctionnalité.
- Les pages de désinscription doivent être inférieures à 750KB.

En savoir plus sur les meilleures pratiques de gestion des listes d'e-mails [ici][7].

## Envoyer un email à un pixel de suivi ouvert

Le pixel d'ouverture de courriel est une image invisible de 1px par 1px qui est automatiquement insérée dans votre email HTML. Ce pixel aide Braze à détecter si les utilisateurs finaux ont ouvert votre email. Les courriels ouverts peuvent être très utiles, aidant les utilisateurs à déterminer des stratégies de marketing efficaces en comprenant les taux d'ouverture correspondants.

### Placer le pixel de suivi

Le comportement par défaut de Braze est d'ajouter le pixel de suivi au bas de votre email. Pour la grande majorité des utilisateurs, c'est l'endroit idéal pour mettre le pixel. Alors que le pixel est déjà stylé pour causer le moins de changements visuels possible, tout changement visuel non intentionnel serait le moins visible au bas d'un courriel. C'est également la valeur par défaut pour les fournisseurs de messagerie tels que SendGrid et SparkPost.

Cependant, un petit sous-ensemble de sociétés peut préférer que le pixel soit modelé à un autre endroit. L'un des avantages de ne pas placer le pixel de suivi en bas est d'éviter les cas où il est coupé par les clients (e. ., Gmail) qui tronquent les courriels après une certaine quantité de kilo-octets.

### Changement de l'emplacement du pixel de suivi

Braze prend actuellement en charge le remplacement de l'emplacement par défaut du pixel de suivi d'ouverture de l'ESP (la dernière balise dans le  d'un email) pour le déplacer vers le premier tag dans le .</p>

!\[open_pixel\]\[13\]

Pour changer d'emplacement :
1. Allez dans __Gérer le groupe d'application__, puis __Paramètres de messagerie__ dans votre compte Braze.
2. Cliquez sur la case à cocher sous __Paramètres de Pixel Ouverture Personnalisée__.
3. Appuyez sur __Save__.

Une fois enregistré, Braze enverra des instructions spéciales à l'ESP afin de placer le pixel de suivi ouvert au sommet de tous les courriels HTML.

{% alert important %}
L'activation SSL va envelopper l'URL du pixel de suivi avec HTTPS au lieu de HTTP - si votre SSL est mal configuré, cela peut affecter l'efficacité du pixel de suivi.
{% endalert %}

## Fonctionnalités activables

!\[switch\]\[2\]{: style="float:right;max-width:30%;margin-left:15px;"}

Les trois paramètres de messagerie énumérés ci-dessous sont des fonctionnalités qui ne nécessitent aucune autre action que de l'activer ou de le désactiver en utilisant le commutateur correspondant. Veuillez lire chaque paramètre pour plus de détails.

### Reprendre les utilisateurs quand leur adresse e-mail change

Vous pouvez réinscrire automatiquement les utilisateurs lorsqu'ils changent leur adresse e-mail. Par exemple, si un utilisateur d'un groupe d'applications précédemment désabonné change son adresse e-mail à une autre qui n'est pas sur la liste de désinscription de Braze, ils seront automatiquement réabonnés.

En savoir plus sur les meilleures pratiques de gestion des listes d'e-mails [ici][8].

### Inclure un en-tête de désinscription de la liste

!\[list_unsub_1\]\[00\]{: style="float:right;max-width:60%;margin-left:15px;"}

Cette fonctionnalité vous permet d'inclure automatiquement un en-tête de désabonnement pour les e-mails envoyés aux utilisateurs abonnés ou optés. Cet en-tête de désinscription permet aux fournisseurs de courriels d'inclure un bouton "Se désabonner" lors de l'affichage d'un courriel.

#### Avantages de l'en-tête de désinscription de la liste

Certains destinataires préfèrent avoir un lien de désinscription disponible au même endroit pour tous les e-mails, plutôt que d'avoir à trouver des liens dans chaque mailing. Lorsqu'elle est activée, cette fonctionnalité met un lien de désinscription visible dans l'en-tête du client de messagerie, en facilitant la désinscription et donc moins de chances que les clients marquent votre e-mail comme Spam. Cela a un impact significatif sur votre réputation et votre livrabilité en tant qu'expéditeur de courriel.

#### Comment fonctionne l'en-tête de désinscription de la liste

Naviguez vers **Paramètres de messagerie** dans votre groupe d'applications. Activer/désactiver la désinscription à la liste **ON**.

!\[list_unsub_3\] \[59\]

Lorsque cette option est activée, cette fonctionnalité ajoutera un en-tête standard de désabonnement de la liste 'mailto:' à tous les e-mails sortants éligibles.  Dès réception d'une demande de désinscription de la liste des utilisateurs finaux, Braze s'assurera que la même personne qui a été envoyée se désabonne.  S'il n'y a pas de correspondance, nous ne traiterons pas cette requête.

> Cette fonctionnalité ne s'applique qu'aux courriels auxquels les utilisateurs ciblés sont « abonnés ou optés » ou « opted in only ».

L'en-tête n'est pas ajouté pour les messages ciblant "tous les utilisateurs, y compris les utilisateurs désabonnés", car ils représentent des messages transactionnels qui n'ont pas besoin d'une fonction de désinscription.

*Actuellement, ‘Windows Live Hotmail’ et ‘Gmail’ prennent en charge cette fonctionnalité.*

{% alert note %}
Si vous utilisez Mailjet, vous n'avez pas la flexibilité de choisir on/off pour cette fonctionnalité - elle sera `ON` par défaut.
{% endalert %}

### CSS en ligne sur les nouveaux e-mails par défaut

L'inlining CSS est une technique qui intègre automatiquement les styles CSS de vos e-mails. Pour certains clients de messagerie, cela peut améliorer la façon dont vos e-mails affichent. Cette fonctionnalité insère automatiquement les CSS sur les nouveaux e-mails par défaut.

La modification de ce paramètre n'affectera aucun de vos e-mails ou modèles existants. Vous pouvez remplacer cette valeur par défaut à tout moment lors de la rédaction de messages ou de modèles.

Pour plus d'informations, consultez notre [Documentation CSS Inlining][10]
[00]: {% image_buster /assets/img_archive/list_unsub_img1.png %} [0]: {% image_buster /assets/img/email_settings/custom_footer.png %} [1]: {% image_buster /assets/img/email_settings/outbound_email. ng %} [2]: {% image_buster /assets/img/email_settings/switch.gif %} [3]: {% image_buster /assets/img/email_settings/custom_unsubscribe. ng %} [4]: {% image_buster /assets/img/email_settings/custom_opt_in.png %} [11]: {% image_buster /assets/img/email_settings/bcc_address. ng %} [12]: {% image_buster /assets/img/email_settings/require_bcc.png %} [13]: {% image_buster /assets/img/open_pixel. ng %} [59]: {% image_buster /assets/img_archive/list_unsub_img3_new.png %}

[5]: https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/
