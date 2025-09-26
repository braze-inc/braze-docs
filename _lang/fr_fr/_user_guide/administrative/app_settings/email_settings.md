---
nav_title: Préférences des e-mails
article_title: Préférences des e-mails
page_type: reference
page_order: 14
description: "Cet article de référence couvre les préférences d'e-mail dans le tableau de bord de Braze, y compris les configurations d'envoi, les pixels de suivi d'ouverture, la page et les pieds de page d'abonnement, et plus encore."
tool: Dashboard
channel: email

---

# Préférences des e-mails

> Les préférences de messagerie sont l'endroit où vous pouvez définir des paramètres spécifiques pour les emails sortants, comme des pieds de page personnalisés, des pages de souscription et de désinscription personnalisées, et plus encore. Inclure ces options dans vos e-mails sortants permet d'offrir une expérience fluide et cohérente à vos utilisateurs.

Les **Préférences de messagerie** se trouvent sous **Paramètres** dans le tableau de bord.

## Configuration de l’envoi

Les paramètres de messagerie sous la section **Configuration d'envoi** déterminent quels détails sont inclus dans vos campagnes par e-mail. Ces paramètres concernent notamment ce que vos utilisateurs voient quand ils reçoivent un e-mail de Braze.

### Paramètres d’e-mail sortant

Lorsque vous configurez vos paramètres de messagerie, vos paramètres d’e-mails sortants identifient le nom et les adresses utilisées quand Braze envoient des courriers électroniques à vos utilisateurs.

{% tabs local %}
{% tab Afficher l'adresse du nom %}

Dans cette section, vous pouvez ajouter les noms et adresses e-mail à utiliser quand Braze envoie des e-mails à vos utilisateurs. Les noms d'affichage et les adresses e-mail seront disponibles dans les options **Edit Sending Info** lorsque vous composez votre campagne e-mail. Notez que les mises à jour apportées aux paramètres des e-mails sortants n'affectent pas rétroactivement les envois existants. 

![]({% image_buster /assets/img/email_settings/display_name_address.png %})

{% endtab %}
{% tab Adresse de réponse %}

L’ajout d’une adresse e-mail dans cette section vous permet de la sélectionner en tant qu’adresse de réponse pour votre campagne d’e-mails. Vous pouvez également définir une adresse e-mail par défaut en sélectionnant **Définir par défaut**. Ces adresses e-mail seront disponibles dans les options **Edit Sending Info** lorsque vous rédigerez votre campagne par e-mail.

![]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab Adresse CCI %}

Cette section vous permet d’ajouter et de gérer des adresses CCI pouvant être ajoutées aux messages e-mail sortants envoyés par Braze. Les adresses CCI ne sont disponibles que pour SendGrid et SparkPost. Comme alternative aux adresses CCI, nous vous recommandons d'utiliser l'[archivage des messages]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving/) pour enregistrer une copie des messages envoyés aux utilisateurs à des fins d'archivage ou de conformité.

L'ajout d'une adresse CCI à un envoi e-mail enverra une copie identique du message reçu par votre utilisateur dans votre boîte de réception CCI. Cet outil est utile pour conserver des copies des messages que vous avez envoyés à vos utilisateurs pour des raisons de conformité ou d'assistance à la clientèle. Les e-mails en copie cachée ne sont pas inclus dans les rapports et les analyses des e-mails.

{% alert important %}
L'ajout d'une adresse CCI à votre campagne ou Canvas aura pour effet de doubler vos e-mails facturables pour la campagne ou le composant Canvas puisque Braze enverra un message à votre utilisateur et un autre à votre adresse CCI.
{% endalert %}

![Section Adresse CCI de l’onglet Paramètres des e-mails.]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

Une fois que vous avez ajouté une adresse, celle-ci sera disponible pour être sélectionnée lors de la composition d'un e-mail dans les campagnes ou les étapes du canvas. Sélectionnez **Définir par défaut** à côté d'une adresse pour définir cette adresse comme étant sélectionnée par défaut lors du lancement d'une nouvelle campagne par e-mail ou d'un composant Canvas. Pour remplacer cela au niveau du message, vous pouvez sélectionner **Pas de CCI** lors de la configuration de votre message.

Si vous exigez que tous les messages électroniques envoyés depuis Braze incluent une adresse BCC, vous pouvez sélectionner le bouton **Exiger une adresse BCC pour toutes vos campagnes par e-mail**. Pour ce faire, vous devrez sélectionner une adresse par défaut, qui sera automatiquement sélectionnée lors de nouvelles campagnes d'e-mail ou étapes du canvas. L’adresse par défaut sera également automatiquement ajoutée à tous les messages déclenchés via notre API REST. Il n’est pas nécessaire de modifier la demande API existante pour inclure l’adresse.

{% endtab %}
{% endtabs %}

## Pixel de suivi de l’ouverture d’e-mail

[![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

Le pixel de suivi d'ouverture des e-mails est une image invisible de 1 x 1 px qui est automatiquement insérée dans le HTML de votre e-mail. Ce pixel aide Braze à détecter si les utilisateurs finaux ont ouvert votre e-mail. Les informations sur l’ouverture des e-mails peuvent être très utiles, car elles aident les utilisateurs à déterminer des stratégies de marketing efficaces en comprenant les taux d’ouverture correspondants.

### Placement du pixel de suivi

Le comportement par défaut dans Braze est d'ajouter le pixel de suivi en bas de votre e-mail. Pour la grande majorité des utilisateurs, c’est l’endroit idéal pour placer le pixel. Bien que le pixel soit déjà conçu pour provoquer le moins de différences visuelles possible, tout changement visuel involontaire sera le moins visible au bas de l’e-mail. C’est également la valeur par défaut pour les fournisseurs d’e-mail tels que SendGrid et SparkPost.

### Modification de l’emplacement du pixel de suivi

Braze prend actuellement en charge le remplacement de l’emplacement par défaut du pixel de suivi d’ouverture par défaut de l’ESP (la dernière balise dans le `<body>` d’un e-mail) pour le déplacer vers la première balise dans le `<body>`.
  
![Section "Ouvrir le pixel de suivi" avec les options de déplacement pour SendGrid, SparkPost, ou Amazon SES.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

Pour modifier l’emplacement :

1. Dans Braze, allez à **Paramètres** > **Préférences de messagerie**.
2. Sélectionnez parmi les options suivantes : **Passer à SendGrid**, **passer à SparkPost** ou **passer à Amazon SES**
3. Sélectionnez **Enregistrer**.

Une fois enregistré, Braze enverra des instructions spéciales à l’ESP afin de placer le pixel de suivi ouvert en haut de tous les e-mails HTML.
  
{% alert important %}
L'activation du SSL permet d'envelopper l'URL du pixel de suivi avec HTTPS au lieu de HTTP. Si votre SSL est mal configuré, cela peut affecter l'efficacité du pixel de suivi.
{% endalert %}

## En-tête de désabonnement de liste {#list-unsubscribe}

{% alert note %}
À partir du 15 février 2024, l'en-tête de désabonnement de liste (avec désabonnement en un clic) sera activé par défaut pour les nouvelles entreprises.
{% endalert %}

L'utilisation d'un en-tête de désabonnement de liste permet à vos destinataires de se désabonner facilement des e-mails marketing en affichant un bouton **Désabonner** dans l'interface utilisateur de la boîte aux lettres, et non dans le corps du message.

![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

Lorsque le destinataire clique sur **Se désabonner**, le fournisseur de messagerie envoie la demande de désabonnement à la destination définie dans l'en-tête de l'e-mail.

L’activation du désabonnement de liste est une bonne pratique de livrabilité et une exigence chez certains des principaux fournisseurs de messagerie. Il encourage les utilisateurs finaux à se retirer en toute sécurité des messages indésirables plutôt que d'appuyer sur le bouton de spam dans un client de messagerie, ce qui est préjudiciable à la réputation de l'expéditeur et à la délivrabilité des e-mails.

### Support du fournisseur de messagerie

Le tableau suivant résume la prise en charge des fournisseurs de messagerie pour l'en-tête « mailto: », l'URL de désabonnement de liste et le désabonnement en un clic ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)).

| En-tête de désabonnement de liste | En-tête Mailto: | URL de désabonnement de liste | Désabonnement en un clic (RFC 8058) | 
| ----- | --- | --- | --- |
| Gmail | Pris en charge* | Pris en charge | Pris en charge |
| Gmail Mobile | Non pris en charge | Non pris en charge | Non pris en charge |
| Apple Mail | Pris en charge | Non pris en charge | Non pris en charge |
| Outlook.com | Pris en charge | Non pris en charge | Non pris en charge |
| Yahoo! Mail | Pris en charge* | Non pris en charge | Pris en charge |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

_\*Yahoo et Gmail finiront par abandonner l'en-tête « mailto: » pour prendre uniquement en charge le clic unique._

L'affichage de l'en-tête est déterminé par le fournisseur de messagerie. Pour vérifier si l'en-tête de désabonnement de liste est inclus dans l'e-mail brut (texte) pour le destinataire dans Gmail, procédez comme suit :

1. Sélectionnez **Afficher l'original** dans l'e-mail. Cela ouvre un nouvel onglet avec la version brute de l'e-mail et ses en-têtes.
2. Recherchez « List-Unsubscribe ».

Si l'en-tête figure dans la version brute de l'e-mail mais n'est pas affiché, le fournisseur de la boîte aux lettres a décidé de ne pas afficher l'option de désabonnement, ce qui signifie que nous n'avons pas d'autres informations sur la raison pour laquelle le fournisseur de la boîte aux lettres n'affiche pas l'en-tête. L’affichage de l'en-tête de désabonnement de liste est finalement basé sur la réputation. Dans la plupart des cas, meilleure est votre réputation d'expéditeur auprès de la boîte de réception, moins il est probable que l'en-tête de désabonnement de la liste apparaisse.

### En-tête de désabonnement par e-mail dans les espaces de travail

![Sélection des "utilisateurs abonnés ou ayant opté pour l'abonnement" pour savoir à quels utilisateurs envoyer.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Lorsque la fonctionnalité d'en-tête de désabonnement aux e-mails est activée, ce paramètre s'applique à l'ensemble de l'espace de travail, et non à l'entreprise. Il est ajouté aux campagnes et aux Canvas qui sont configurés pour envoyer aux utilisateurs qui sont abonnés ou opt-in, ou aux utilisateurs opt-in dans l'étape de l'**audience cible** des générateurs de campagnes et de Canvas.

Lorsque vous utilisez l'espace de travail par défaut, Braze n'ajoute pas l'en-tête de désabonnement en un clic pour les campagnes considérées comme transactionnelles, qui sont configurées pour "envoyer à tous les utilisateurs, y compris les utilisateurs désabonnés". Pour passer outre et ajouter l'en-tête de désabonnement en un clic lors de l'envoi aux utilisateurs désabonnés, vous pouvez sélectionner **Se désabonner globalement de tous les e-mails** dans les paramètres généraux des messages de la liste de désabonnement en un clic.

### En-tête de désabonnement de liste par défaut

{% alert important %}
Gmail souhaite que les expéditeurs mettent en œuvre le désabonnement en un seul clic pour tous leurs messages commerciaux et promotionnels sortants à compter du 1er juin 2024. Pour plus d'informations, consultez les [directives de Gmail relatives à l’expéditeur](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) et la [FAQ sur les directives de Gmail relatives aux expéditeurs d’e-mails](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). Yahoo a annoncé un calendrier début 2024 pour la mise à jour de ses exigences. Pour plus d'informations, consultez le site [Plus de sécurité, moins de spam : Application des normes en matière d’e-mails pour une meilleure expérience](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Pour utiliser la fonctionnalité de désabonnement de Braze afin de traiter directement les désabonnements, sélectionnez **Inclure un en-tête de liste de désabonnement en un clic (mailto et HTTP) pour les e-mails envoyés aux utilisateurs abonnés ou ayant opté pour l'abonnement** et sélectionnez **Braze par défaut** comme URL et mail-to standard de Braze. 

![Option permettant d'inclure automatiquement un en-tête "list-unsubscribe" dans les e-mails envoyés aux utilisateurs abonnés ou ayant opté pour l'abonnement.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze prend en charge les versions suivantes de l'en-tête de désabonnement de liste :

| Version de désabonnement de la liste | Description | 
| ----- | --- |
| Un clic (RFC 8058) | Offre aux destinataires un moyen simple de se désabonner des e-mails en un seul clic. Ceci est une exigence de Yahoo et Gmail pour les expéditeurs d’e-mails groupés. |
| URL de désabonnement de la liste ou HTTPS | Fournit aux destinataires un lien qui les dirige vers une page web où ils peuvent se désabonner. |
| Mailto | Spécifie une adresse e-mail comme destination du message de demande de désabonnement à envoyer par le destinataire à la marque. <br><br> _Pour traiter les demandes de désabonnement de liste de diffusion, ces demandes de désabonnement doivent inclure l'adresse e-mail telle qu'elle est stockée dans Braze pour l'utilisateur final qui se désabonne. Cette information peut être fournie par l'adresse "from-address" de l'e-mail à partir duquel l'utilisateur final se désabonne, l'objet codé ou le corps codé de l'e-mail reçu par l'utilisateur final et dont il se désabonne. Dans des cas très limités, certains fournisseurs de boîtes de réception n'adhèrent pas au protocole [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368), ce qui fait que l'adresse e-mail n'est pas correctement transmise. La demande de désabonnement risque alors de ne pas pouvoir être traitée dans Braze._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Lorsque Braze reçoit une demande de désabonnement de liste de la part d'un utilisateur via l'une des méthodes ci-dessus, l'état d'abonnement global de cet utilisateur est défini sur Désabonné. Si aucune correspondance n'est trouvée, Braze ne traitera pas cette demande.

### Désabonnement en un clic

L'utilisation de l'en-tête list-unsubscribe[(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)), qui permet de se désabonner en un seul clic, vise à offrir aux destinataires un moyen simple de se désabonner des e-mails.

### Désabonnement de liste en un clic au niveau du message

Le paramètre de désabonnement en un clic au niveau du message remplacera la fonctionnalité d'en-tête de désabonnement par e-mail définie pour les espaces de travail. Appliquez le comportement de désabonnement en un clic par campagne ou par étape de canvas pour les utilisations suivantes :

- Ajouter un désabonnement en un clic de Braze pour un groupe d'abonnement spécifique afin de prendre en charge plusieurs marques/listes au sein d'un même espace de travail
- Basculer entre le désabonnement par défaut de Braze ou l'URL personnalisée
- Ajouter votre URL de désabonnement en un clic personnalisée
- Ignorer le désabonnement en un clic sur ce message

{% alert note %}
Le paramètre de désabonnement à la liste en un clic au niveau du message n'est disponible que lors de l'utilisation de l'éditeur par glisser-déposer et de l'éditeur HTML mis à jour. Si vous utilisez l'éditeur HTML précédent, passez à l'éditeur HTML mis à jour pour utiliser cette fonctionnalité.
{% endalert %}

Dans votre éditeur d'e-mails, allez à **Paramètres d'envoi** > **Informations d'envoi**. Sélectionnez parmi les options suivantes :

- **Utiliser l'espace de travail par défaut**: Utilise les paramètres de **l'en-tête de désabonnement par e-mail** définis dans les **préférences de messagerie**. Toute modification apportée à ce paramètre sera appliquée à l’ensemble des messages.
- **Se désabonner de manière générale de tous les e-mails** : Utilise l’en-tête de désabonnement en un clic par défaut de Braze. Les utilisateurs qui cliquent sur le bouton de désabonnement verront leur état d'abonnement global aux e-mails défini sur "Désabonné".
- **Se désabonner d'un groupe d'abonnement spécifique**: Utilise le groupe d'abonnement spécifié. Les utilisateurs qui cliquent sur le bouton de désabonnement seront désabonnés du groupe d'abonnement sélectionné.
    - Lors de la sélection d'un groupe d'abonnement, ajoutez le filtre **Groupe d'abonnement** dans **Publics cibles** pour ne cibler que les utilisateurs abonnés à ce groupe spécifique. Le groupe d'abonnement sélectionné pour le désabonnement en un clic doit correspondre au groupe d'abonnement que vous ciblez. En cas d'incohérence dans le groupe d'abonnement, vous risquez d'envoyer un message à un utilisateur qui tente de se désabonner d'un groupe d'abonnement dont il s'est déjà désabonné.
- **Personnalisé :** Ajoute votre URL personnalisée de désabonnement en un clic vous permettant de traiter directement les demandes de désabonnement.
- **Exclure le désabonnement**

{% alert important %}
L’exclusion du désabonnement en un clic ou de tout mécanisme de désabonnement devrait uniquement être appliquée aux messages transactionnels, tels que les réinitialisations de mot de passe, les reçus et les e-mails de confirmation.
{% endalert %}

Le réglage de ce paramètre remplacera le comportement par défaut pour le désabonnement de liste en un clic dans cet e-mail.

![]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### Conditions

Si vous envoyez des e-mails en utilisant votre propre fonctionnalité de désabonnement personnalisée, vous devez respecter les exigences suivantes pour vous assurer que l'URL de désabonnement en un clic que vous avez configurée est conforme à la RFC 8058 :

* L'URL doit être capable de gérer les demandes POST de désabonnement.
* L'URL doit commencer par `https://`.
* L'URL ne doit pas renvoyer une redirection HTTPS ou un corps. Les liens de désabonnement en un clic qui mènent à une page de destination ou à un autre type de page web ne sont pas conformes à la RFC 8058.
* Les requêtes POST ne doivent pas définir de cookies.

Sélectionnez **En-tête de désabonnement de liste personnalisé** pour ajouter votre propre endpoint de désabonnement en un clic configuré, ainsi qu’un « mailto: » facultatif. Braze nécessite une entrée pour l'URL afin de prendre en charge un en-tête de désabonnement de liste personnalisé, car le HTTP de désabonnement en un clic est une exigence de Yahoo et Gmail pour les expéditeurs d’e-mails groupés.

![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## Ajout aux lignes d’objet de l’e-mail

Utilisez le bouton-bascule pour inclure [TEST] et [SEED] dans les lignes d'objet de vos e-mails de test et de seed. Cela peut vous aider à identifier les campagnes par e-mail envoyées en tant que tests.

![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## L'option par défaut de l'inclusion CSS des nouveaux e-mails est activée par défaut

L’inclusion CSS est une technique qui intègre automatiquement les styles CSS pour vos e-mails et nouveaux e-mails. Pour certains clients de messagerie électronique, cela peut améliorer le rendu de vos e-mails.

La modification de ce paramètre n’affectera pas vos e-mails existants ou les modèles. Vous pouvez remplacer cette valeur par défaut à tout moment lors de la composition de vos messages ou modèles. Pour plus d'informations, reportez-vous à l'[insertion CSS.]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/css_inline/)

## Réabonnez les utilisateurs lorsque leurs e-mails changent

Vous pouvez réabonner automatiquement les utilisateurs lorsqu’ils changent leur adresse e-mail. Par exemple, si un utilisateur de l'espace de travail précédemment désabonné change son adresse e-mail pour une adresse qui n'est pas sur la liste de désabonnement de Braze, il sera automatiquement réabonné.

![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Pages et pieds de page pour le désabonnement

{% tabs local %}
{% tab Pied de page personnalisé %}

Pour les courriels commerciaux, la [loi CAN-SPAM](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) exige que tous les courriels commerciaux incluent une option de désabonnement. Grâce aux paramètres de pied de page personnalisés, vous pouvez rester conforme à la loi CAN-SPAM tout en personnalisant votre pied de page de désabonnement par e-mail. Pour rester conforme, vous devez ajouter votre pied de page personnalisé à tous les e-mails envoyés dans le cadre des campagnes de cet espace de travail.

Notez les exigences suivantes lors de la création d’un pied de page personnalisé pour votre envoi de messages par e-mail :
- Doit inclure une URL de désabonnement et une adresse postale.
- Doivent faire moins de 100 Ko.

![]({% image_buster /assets/img/email_settings/custom_footer.png %})

Pour en savoir plus sur la personnalisation des pieds de page avec Liquid, consultez notre documentation sur les [pieds de page personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

{% endtab %}
{% tab Page de désabonnement personnalisée %}

Braze vous permet de définir une **page de désabonnement personnalisée** avec votre propre HTML. Cette page s’affiche une fois qu’un utilisateur a choisi de se désabonner depuis la partie inférieure d’un e-mail. Notez que cette page doit faire moins de 750 Ko. 

![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

En savoir plus sur les meilleures pratiques de gestion des listes de diffusion dans [Gestion des abonnements aux e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% tab Page d'inscription personnalisée %}

Vous pouvez créer une page d’abonnement personnalisée à l’aide de votre propre HTML. Inclure cela dans votre e-mail peut être particulièrement bénéfique si vous voulez que votre branding et vos messages soient cohérents pendant toute la durée de vie de votre client. Notez que cette page doit faire moins de 750 Ko. 

![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

En savoir plus sur les meilleures pratiques de gestion des listes de diffusion dans [Gestion des abonnements aux e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% endtabs %}

## Foire aux questions

### Désabonnement en un clic

{% details L'URL de désabonnement en un clic (via l'en-tête list-unsubscribe) peut-elle renvoyer vers un centre de préférences ? %}
Non, cela ne respecte pas le protocole RFC 8058, ce qui signifie que vous ne serez pas en conformité avec l'exigence de désabonnement en un clic de Yahoo et Gmail.
{% enddetails %}

{% details Pourquoi est-ce que je reçois le message d'erreur « Le corps de votre e-mail ne comprend pas de lien de désabonnement » lorsque je compose mon centre de préférences ? %}
Un centre de préférences n'est pas considéré comme un lien de désabonnement. Vos destinataires d'e-mails doivent avoir la possibilité de se désabonner de tout e-mail commercial pour rester conformes à la loi CAN-SPAM.
{% enddetails %}

{% details Devrai-je modifier les campagnes d'e-mails passées et les Canvases pour appliquer le paramètre de désabonnement en un clic après l'avoir activé ? %}
Si vous n'avez aucun des cas d'utilisation pour le paramètre de désabonnement en un clic au niveau du message, aucune action n'est requise tant que le paramètre est activé dans les **Préférences de messagerie**. Braze ajoutera automatiquement les en-têtes de désabonnement en un clic à tous les messages marketing et promotionnels sortants. Toutefois, si vous devez configurer le comportement de désabonnement en un clic au niveau de chaque message, vous devrez mettre à jour les campagnes précédentes et les étapes du canvas avec l'e-mail en conséquence.
{% enddetails %}

{% details Je peux voir l'en-tête de désabonnement de la liste et de désabonnement en un clic dans le message original ou les données brutes, mais pourquoi ne vois-je pas le bouton de désabonnement dans Gmail ou Yahoo ? %}
Au final, ce sont Gmail et Yahoo qui décident d'afficher ou non l'en-tête de désabonnement de liste ou de désabonnement en un clic. Pour les nouveaux expéditeurs ou les expéditeurs dont la réputation d'expéditeur est faible, il peut arriver que le bouton de désabonnement ne s'affiche pas.
{% enddetails %}

{% details L'en-tête de désabonnement en un clic personnalisé prend-il en charge Liquid ? %}
Oui, le Liquid et la logique conditionnelle sont pris en charge pour permettre des URL de désabonnement dynamiques en un clic pour l'en-tête.
{% enddetails %}

{% alert tip %}
Si vous ajoutez une logique conditionnelle, évitez d'avoir des valeurs de sortie qui ajoutent des espaces à votre URL, car Braze ne supprime pas ces espaces.
{% endalert %}

### Désabonnement de liste en un clic au niveau du message

{% details Si j'ajoute manuellement les en-têtes d'e-mail pour le clic unique et que l'en-tête de désabonnement à l'e-mail est activé, quel est le comportement attendu ? %}
Les en-têtes d'e-mail ajoutés pour la désinscription en un clic seront appliqués à tous les envois futurs de cette campagne.
{% enddetails %}

{% details Pourquoi les groupes d'abonnement doivent-ils correspondre entre les variantes de message pour être lancés ? %}
Pour une campagne avec des tests A/B, Braze enverra aléatoirement à un utilisateur l'une des variantes. Si deux groupes d'abonnement différents sont définis pour la même campagne (la variante A est définie pour le groupe d'abonnement A et la variante B est définie pour le groupe d'abonnement B), nous ne pouvons pas garantir que les utilisateurs qui sont uniquement abonnés au groupe d'abonnement B recevront la variante B. Il peut arriver que des utilisateurs se désabonnent d'un groupe d'abonnement pour lequel ils se sont déjà désabonnés.
{% enddetails %}

{% details Le paramètre d'en-tête de désabonnement par e-mail est désactivé dans les préférences de messagerie, mais dans les informations d'envoi de ma campagne, le paramètre de désabonnement en un clic est défini sur « Utiliser le paramètre par défaut de l'espace de travail ». Est-ce un bogue ? %}
Non. Si le paramètre de l'espace de travail est désactivé et que le paramètre de message est défini sur **Utiliser la valeur par défaut de l'espace de travail**, alors Braze suivra ce qui est configuré dans **Préférences de messagerie**. Cela signifie que nous n'ajouterons pas l'en-tête de désabonnement en un clic pour la campagne.
{% enddetails %}

{% details Que se passe-t-il si un groupe d'abonnement est archivé ? Ceci va-t-il casser le désabonnement en un clic sur les e-mails envoyés ? %}
Si un groupe d'abonnement référencé dans **Informations d'envoi** pour un clic est archivé, Braze traitera toujours les désabonnements d'un clic. Le groupe d'abonnement ne sera plus affiché sur le tableau de bord (filtre de segment, profil utilisateur et zones similaires).
{% enddetails %}

{% details Le paramètre de désabonnement en un clic est-il disponible pour les modèles d'e-mail ? %}
Non, nous ne prévoyons pas actuellement d'ajouter cette fonctionnalité pour les modèles d'e-mail, car ces modèles ne sont pas assignés à un domaine d'envoi. Si vous êtes intéressé par cette fonctionnalité pour les modèles d'e-mails, soumettez [des commentaires sur le produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% enddetails %}

{% details Cette fonctionnalité vérifie-t-elle que l'URL de désabonnement en un clic ajoutée à l'option personnalisée est valide ? %}
Non, nous ne vérifions ni ne validons aucun lien dans le tableau de bord Braze. Assurez-vous de bien tester votre URL avant le lancement.
{% enddetails %}


