---
nav_title: "Préférences en matière d'e-mail"
article_title: "Préférences en matière d'e-mail"
page_type: reference
page_order: 14
description: "Cet article de référence couvre les préférences d'e-mail dans le tableau de bord de Braze, y compris les configurations d'envoi, les pixels de suivi d'ouverture, la page et les pieds de page d'abonnement, et plus encore."
tool: Dashboard
channel: email

---

# Préférences en matière d'e-mail

> Les préférences d'e-mail vous permettent de définir des paramètres spécifiques pour les e-mails sortants, tels que des pieds de page personnalisés, des pages d'abonnement et de désabonnement personnalisées, et bien d'autres choses encore. Inclure ces options dans vos e-mails sortants permet d'offrir une expérience fluide et cohérente à vos utilisateurs.

Les **préférences en matière d'e-mail** se trouvent sous **Paramètres** dans le tableau de bord.

## Envoi de la configuration

Les paramètres d'e-mail de la section **Configuration de l'envoi** déterminent les détails à inclure dans vos campagnes d'e-mail. En particulier, ces paramètres sont principalement liés à ce que votre utilisateur voit lorsqu'il reçoit un e-mail de Braze.

### Paramètres de l'e-mail sortant

Lors de la configuration de vos paramètres d'e-mail, vos paramètres d'e-mail sortant identifient le nom et les adresses e-mail utilisés lorsque Braze envoie des e-mails à vos utilisateurs.

{% tabs local %}
{% tab Display Name Address %}

Dans cette section, vous pouvez ajouter les noms et les adresses e-mail qui peuvent être utilisés lorsque Braze envoie des e-mails à vos utilisateurs. Les noms d'affichage et les adresses e-mail seront disponibles dans les options **Modifier les informations d'envoi** lorsque vous composerez votre campagne d'e-mail. Notez que les mises à jour apportées aux paramètres des e-mails sortants n'ont pas d'effet rétroactif sur les envois existants.

!section "Paramètres de l'e-mail sortant" avec des champs pour différents noms d'affichage et domaines.]({% image_buster /assets/img/email_settings/display_name_address.png %})

#### Personnalisation avec du liquide

Vous pouvez également utiliser [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) dans les champs **From Display Name** et **Local Part** pour modeler dynamiquement l'e-mail d'envoi en fonction d'attributs personnalisés. Par exemple, vous pouvez utiliser une logique conditionnelle pour envoyer depuis différentes marques ou régions :

{% raw %}
```liquid
{% if ${language} == 'en' %} 
English Display Name 
{% elsif ${language} == 'de' %} 
German Display Name 
{% else %} 
Default to English Display Name
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab Reply-To Address %}

L'ajout d'une adresse e-mail dans cette section vous permet de la sélectionner comme adresse de réponse pour votre campagne d'e-mail. Vous pouvez également faire d'une adresse e-mail l'adresse par défaut en sélectionnant **Rendre par défaut.** Ces adresses e-mail seront disponibles dans les options **Modifier les informations d'envoi** lorsque vous composerez votre campagne d'e-mail.

\!["Section "Adresse de réponse" avec des champs permettant de saisir plusieurs adresses de réponse.]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

#### Personnalisation avec du liquide

Vous pouvez également utiliser [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) dans le champ **Adresse de réponse** pour modeler dynamiquement l'adresse de réponse en fonction d'attributs personnalisés. Par exemple, vous pouvez utiliser une logique conditionnelle pour envoyer des réponses à différentes régions ou départements :

{% raw %}
```liquid
{% if {{custom_attribute.${region}}} == 'US' %}
us-support@company.com
{% elsif {{custom_attribute.${region}}} == 'EU' %}
eu-support@company.com
{% else %}
global-support@company.com
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab BCC Address %}

Cette section vous permet d'ajouter et de gérer les adresses CCI qui peuvent être ajoutées aux messages e-mail sortants envoyés depuis Braze. Les adresses CCI ne sont disponibles que pour SendGrid et SparkPost. Comme alternative aux adresses CCI, nous vous recommandons d'utiliser l'[archivage des messages]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving/) pour enregistrer une copie des messages envoyés aux utilisateurs à des fins d'archivage ou de conformité.

L'ajout d'une adresse CCI à un envoi e-mail enverra une copie identique du message reçu par votre utilisateur dans votre boîte de réception CCI. Cet outil est utile pour conserver des copies des messages que vous avez envoyés à vos utilisateurs pour des raisons de conformité ou d'assistance à la clientèle. Les e-mails CCI ne sont pas pris en compte dans les rapports et analyses d'e-mails.

{% alert important %}
L'ajout d'une adresse CCI à votre campagne ou Canvas aura pour effet de doubler vos e-mails facturables pour la campagne ou le composant Canvas puisque Braze enverra un message à votre utilisateur et un autre à votre adresse CCI.
{% endalert %}

\![Adresse CCI de l'onglet Paramètres de l'e-mail.]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

Une fois que vous avez ajouté une adresse, celle-ci sera disponible pour être sélectionnée lors de la composition d'un e-mail dans les campagnes ou les étapes du canvas. Sélectionnez **Rendre par défaut** en regard d'une adresse pour que cette adresse soit sélectionnée par défaut lors du lancement d'une nouvelle campagne d'e-mail ou d'un composant Canvas. Pour annuler cette option au niveau du message, vous pouvez sélectionner **Pas de CCI** lors de la configuration de votre message.

Si vous souhaitez que tous les messages envoyés par Braze contiennent une adresse CCI, vous pouvez basculer sur l'option **Exiger une adresse CCI pour toutes vos campagnes de communication par e-mail**. Pour ce faire, vous devrez sélectionner une adresse par défaut, qui sera automatiquement sélectionnée lors de nouvelles campagnes d'e-mail ou étapes du canvas. L'adresse par défaut sera également ajoutée automatiquement à tous les messages déclenchés via notre API REST. Il n'est pas nécessaire de modifier la demande d'API existante pour inclure l'adresse.

{% endtab %}
{% endtabs %}

## Ouvrez le pixel de suivi

[!cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

Le pixel de suivi d'ouverture d'e-mail est une image invisible de 1 x 1 px qui est automatiquement insérée dans le code HTML de votre e-mail. Ce pixel aide Braze à détecter si les utilisateurs finaux ont ouvert votre e-mail. Les informations sur l'ouverture des e-mails peuvent être très utiles, car elles aident les utilisateurs à déterminer des stratégies de marketing efficaces en comprenant les taux d'ouverture correspondants.

### Placement du pixel de suivi

Le comportement par défaut dans Braze est d'ajouter le pixel de suivi au bas de votre e-mail. Pour la majorité des utilisateurs, c'est l'endroit idéal pour placer le pixel. Bien que le pixel soit déjà stylisé pour provoquer le moins de changements visuels possible, toute modification visuelle involontaire serait la moins visible au bas d'un e-mail. C'est également la valeur par défaut pour les fournisseurs d'e-mails tels que SendGrid et SparkPost.

### Modification de l'emplacement/localisation du pixel de suivi

Braze prend actuellement en charge le remplacement de l'emplacement par défaut du pixel de suivi de l'ouverture de l'ESP (la dernière étiquette dans le site `<body>` d'un e-mail) pour le déplacer vers la première étiquette dans le site `<body>`.
  
\!["Ouvrez la section "Pixel de suivi" avec les options à déplacer pour SendGrid, SparkPost, ou Amazon SES.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

Pour modifier l'emplacement/localisation :

1. Dans Braze, allez dans **Paramètres** > **Préférences e-mail.**
2. Sélectionnez l'une des options suivantes : **Passer à SendGrid**, **passer à SparkPost** ou **passer à Amazon SES**
3. Sélectionnez **Enregistrer**.

Une fois enregistré, Braze enverra des instructions spéciales à l'ESP afin de placer le pixel de suivi des ouvertures en haut de tous les e-mails HTML.
  
{% alert important %}
L'activation du SSL permet d'envelopper l'URL du pixel de suivi avec HTTPS au lieu de HTTP. Si votre SSL est mal configuré, cela peut affecter l'efficacité du pixel de suivi.
{% endalert %}

## En-tête de liste de désabonnement {#list-unsubscribe}

{% alert note %}
À partir du 15 février 2024, l'en-tête list-unsubscribe (avec désabonnement en un clic) sera activé par défaut pour les nouvelles entreprises.
{% endalert %}

L'utilisation d'un en-tête list-unsubscribe permet à vos destinataires de se désabonner facilement des e-mails marketing en affichant un bouton de **désabonnement** dans l'interface utilisateur de la boîte aux lettres, et non dans le corps du message.

\![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

Lorsqu'un destinataire clique sur **Se désabonner**, le fournisseur de boîtes aux lettres envoie la demande de désabonnement à la destination définie dans l'en-tête de l'e-mail.

L'activation de la fonction de désabonnement à la liste est une pratique exemplaire en matière de livrabilité et une exigence de certains des principaux fournisseurs de boîtes aux lettres. Il encourage les utilisateurs finaux à se débarrasser en toute sécurité des messages indésirables plutôt que d'appuyer sur le bouton "spam" d'un client e-mail, ce qui nuit à la réputation de l'envoi et à la livrabilité de l'e-mail.

### Soutien aux fournisseurs de boîtes aux lettres

Le tableau suivant résume la prise en charge par les fournisseurs de boîtes aux lettres de l'en-tête "mailto :", de l'URL de désabonnement à la liste et du désabonnement en un clic[(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)).

| En-tête de liste de désabonnement | Mailto : en-tête | URL de désabonnement à la liste | Désabonnement en un clic (RFC 8058) | 
| ----- | --- | --- | --- |
| Gmail | Soutenu* | Soutenu | Soutenu |
| Gmail Mobile | Non pris en charge | Non pris en charge | Non pris en charge |
| Apple Mail | Soutenu | Non pris en charge | Non pris en charge |
| Outlook.com | Soutenu | Non pris en charge | Non pris en charge |
| Yahoo ! Courrier | Soutenu* | Non pris en charge | Soutenu |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

_\*Yahoo et Gmail finiront par supprimer l'en-tête "mailto :" et ne prendront en charge qu'un seul clic._

L'affichage de l'en-tête est déterminé en dernier ressort par le fournisseur de la boîte aux lettres. Pour vérifier si l'en-tête list-unsubscribe est inclus dans l'e-mail brut (texte) du destinataire dans Gmail, procédez comme suit :

1. Sélectionnez **Afficher l'original** dans l'e-mail. Cela ouvre un nouvel onglet avec la version brute de l'e-mail et ses en-têtes.
2. Recherchez "List-Unsubscribe".

Si l'en-tête figure dans la version brute de l'e-mail mais n'est pas affiché, le fournisseur de la boîte aux lettres a décidé de ne pas afficher l'option de désabonnement, ce qui signifie que nous n'avons pas d'autres informations sur la raison pour laquelle le fournisseur de la boîte aux lettres n'affiche pas l'en-tête. L'affichage de l'en-tête list-unsubscribe est en fin de compte basé sur la réputation. Dans la plupart des cas, plus votre réputation d'expéditeur est bonne auprès du fournisseur de boîtes aux lettres, plus l'en-tête list-unsubscribe est susceptible d'apparaître.

### En-tête de désabonnement aux e-mails dans les espaces de travail

\![S'abonner aux "utilisateurs abonnés ou opt-in" pour savoir à quels utilisateurs envoyer.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Lorsque la fonctionnalité d'en-tête de désabonnement aux e-mails est activée, ce paramètre s'applique à l'ensemble de l'espace de travail, et non à l'entreprise. Il est ajouté aux campagnes et aux Canvas qui sont configurés pour envoyer aux utilisateurs qui sont abonnés ou opt-in, ou aux utilisateurs opt-in dans l'étape de l'**audience cible** des générateurs de campagnes et de Canvas.

Lorsque vous utilisez l'espace de travail par défaut, Braze n'ajoute pas l'en-tête de désabonnement en un clic pour les campagnes considérées comme transactionnelles, qui sont configurées pour "envoyer à tous les utilisateurs, y compris les utilisateurs désabonnés". Pour passer outre et ajouter l'en-tête de désabonnement en un clic lors de l'envoi aux utilisateurs désabonnés, vous pouvez sélectionner **Se désabonner globalement de tous les e-mails** dans les paramètres généraux des messages de la liste de désabonnement en un clic.

### En-tête list-unsubscribe par défaut

{% alert important %}
Gmail prévoit que les expéditeurs mettent en œuvre la désinscription en un clic pour tous leurs messages commerciaux, promotionnels sortants à partir du 1er juin 2024. Pour plus d'informations, consultez [les](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) [directives de Gmail relatives aux expéditeurs](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages) et la [FAQ sur les directives relatives aux expéditeurs d'e-mails de Gmail](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). Yahoo a annoncé un calendrier pour le début de l'année 2024 en ce qui concerne les exigences de mise à jour. Pour plus d'informations, consultez le site [Plus de sécurité, moins de spam : Appliquer les normes de l'e-mail pour une meilleure expérience](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Pour utiliser la fonctionnalité de désabonnement de Braze afin de traiter directement les désabonnements, sélectionnez **Inclure un en-tête de liste de désabonnement en un clic (mailto et HTTP) pour les e-mails envoyés aux utilisateurs abonnés ou ayant opté pour l'abonnement** et sélectionnez **Braze par défaut** comme URL et mail-to standard de Braze. 

!Option permettant d'inclure automatiquement un en-tête list-unsubscribe pour les e-mails envoyés aux utilisateurs abonnés ou ayant opté pour l'abonnement.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze prend en charge les versions suivantes de l'en-tête list-unsubscribe :

| Version de la liste de désabonnement | Description | 
| ----- | --- |
| En un clic (RFC 8058) | Offre aux destinataires un moyen simple de se désabonner des e-mails en un seul clic. Il s'agit d'une exigence de Yahoo et de Gmail pour les expéditeurs de masse. |
| URL de désabonnement à la liste ou HTTPS | Fournit aux destinataires un lien qui les dirige vers une page web où ils peuvent se désinscrire. |
| Mailto | Spécifie une adresse e-mail comme destination du message de demande de désabonnement à envoyer par le destinataire à la marque. <br><br> _Pour traiter les demandes de désabonnement par liste mailto, ces demandes de désabonnement doivent inclure l'adresse e-mail de l'utilisateur final qui se désabonne, telle qu'elle est stockée dans Braze. Cette information peut être fournie par l'adresse "from-address" de l'e-mail à partir duquel l'utilisateur final se désabonne, l'objet codé ou le corps codé de l'e-mail reçu par l'utilisateur final et dont il se désabonne. Dans des cas très limités, certains fournisseurs de boîtes de réception n'adhèrent pas au protocole [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368), ce qui fait que l'adresse e-mail n'est pas correctement transmise. Cela peut conduire à ce qu'une demande de désinscription ne puisse pas être traitée dans Braze._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Lorsque Braze reçoit une demande de désabonnement à une liste de la part d'un utilisateur via l'une des méthodes ci-dessus, l'état de l'abonnement global à l'e-mail de cet utilisateur est défini comme désabonné. S'il n'y a pas de correspondance, Braze ne traitera pas cette demande.

### Désinscription en un clic

L'utilisation de l'en-tête list-unsubscribe[(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)), qui permet de se désabonner en un seul clic, vise à offrir aux destinataires un moyen simple de se désabonner des e-mails.

### Liste de désabonnement en un clic au niveau du message

Le paramètre de désabonnement à la liste en un clic au niveau du message remplacera les fonctionnalités de l'en-tête de désabonnement à l'e-mail pour les espaces de travail. Appliquez le comportement de désabonnement en un clic par campagne ou étape du canvas pour les utilisations suivantes :

- Ajoutez une fonction de désabonnement en un clic de Braze pour un groupe d'abonnement spécifique afin de prendre en charge plusieurs marques/listes au sein d'un même espace de travail.
- Basculer entre l'URL de désinscription par défaut de Braze et l'URL personnalisée.
- Ajoutez votre URL personnalisée de désabonnement en un clic
- Omettre la désinscription en un clic sur ce message

{% alert note %}
Le paramètre de désabonnement à la liste en un clic au niveau du message n'est disponible que lors de l'utilisation de l'éditeur par glisser-déposer et de l'éditeur HTML mis à jour. Si vous utilisez l'ancien éditeur HTML, passez à l'éditeur HTML mis à jour pour utiliser cette fonctionnalité.
{% endalert %}

Dans votre éditeur d'e-mail, allez dans **Paramètres d'envoi** > **Informations d'envoi.** Sélectionnez l'une des options suivantes :

- **Utiliser l'espace de travail par défaut**: Utilise les paramètres de **l'en-tête de désabonnement à l'e-mail** définis dans **les préférences d'e-mail.** Toute modification apportée à ce paramètre s'appliquera à tous les messages.
- **Se désabonner globalement de tous les e-mails :** Utilise l'en-tête de désabonnement par défaut en un clic de Braze. Les utilisateurs qui cliquent sur le bouton de désabonnement verront l'état de leur abonnement global à l'e-mail passer à "Désabonné".
- **Se désabonner d'un groupe d'abonnement spécifique**: Utilise le groupe d'abonnement spécifié. Les utilisateurs qui cliquent sur le bouton de désabonnement seront désabonnés du groupe d'abonnement sélectionné.
    - Lorsque vous sélectionnez un groupe d'abonnement, ajoutez le filtre **Groupe d'abonnement** dans **Audiences cibles** pour ne cibler que les utilisateurs abonnés à ce groupe spécifique. Le groupe d'abonnement sélectionné pour le désabonnement en un clic doit correspondre au groupe d'abonnement que vous ciblez. En cas d'incohérence dans le groupe d'abonnement, vous risquez d'envoyer un message à un utilisateur qui tente de se désabonner d'un groupe d'abonnement dont il s'est déjà désabonné.

{% alert important %}
Le paramètre **Se désabonner d'un groupe d'abonnement spécifique** ne s'applique qu'à l'en-tête Désabonnement de **la** liste en un clic. L'en-tête mailto list-unsubscribe n'est pas affecté par cette option. Cela signifie qu'un destinataire qui se désabonne à l'aide de cette méthode enregistrera une désinscription globale, et non une désinscription du groupe d'abonnement spécifique. Pour exclure l'en-tête mailto list-unsubscribe de la désinscription globale des utilisateurs, lorsque vous sélectionnez ce paramètre, contactez l'[assistance.]({{site.baseurl}}/support_contact/)
{% endalert %}

- **Personnalisé :** Ajoute votre URL personnalisée de désabonnement en un clic pour que vous puissiez traiter directement les désabonnements.
- **Exclure le désabonnement**

{% alert important %}
L'exclusion du mécanisme de désabonnement en un clic ou de tout autre mécanisme de désabonnement ne devrait être appliquée qu'aux messages transactionnels, tels que les réinitialisations de mot de passe, les reçus et les courriels de confirmation.
{% endalert %}

Adjusting this setting will override the default behavior for one-click list unsubscribe in this e-mail.

\![]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### Exigences

Si vous envoyez des e-mails à l'aide de votre propre fonctionnalité de désabonnement personnalisée, vous devez respecter les exigences suivantes pour vous assurer que l'URL de désabonnement en un clic que vous avez définie est conforme à la RFC 8058 :

* L'URL doit être en mesure de traiter les demandes POST de désinscription.
* L'URL doit commencer par `https://`.
* L'URL ne doit pas renvoyer une redirection HTTPS ou un corps. Les liens de désabonnement en un clic qui renvoient à une page d'atterrissage ou à un autre type de page web ne sont pas conformes à la RFC 8058.
* Les requêtes POST ne doivent pas définir de cookies.

Sélectionnez **En-tête de liste de dés** abonnement personnalisé pour ajouter votre propre endpoint de désabonnement configuré en un clic, ainsi qu'un "mailto :" facultatif. Braze exige une entrée pour l'URL afin de prendre en charge un en-tête list-unsubscribe personnalisé car le désabonnement HTTP en un seul clic est une exigence de Yahoo et Gmail pour les expéditeurs en masse.

\![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## Ajouter des lignes d'objet aux e-mails

Utilisez le basculeur pour inclure "[TEST]" et "[SEED]" dans les lignes d'objet de vos e-mails de test et d'initiateur. Cela permet d'identifier les campagnes d'e-mail envoyées à titre de test.

\![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## Inline CSS sur les nouveaux e-mails par défaut

L'insertion CSS est une technique qui permet d'insérer automatiquement des styles CSS dans vos e-mails et dans les nouveaux e-mails. Pour certains clients d'e-mail, cela peut améliorer le rendu de vos e-mails.

La modification de ce paramètre n'affectera aucun de vos messages e-mail ou modèles existants. Vous pouvez modifier cette valeur par défaut à tout moment lors de la rédaction de messages ou de modèles. Pour plus d'informations, reportez-vous à l'[insertion CSS.]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/css_inline/)

## Réinscrire les utilisateurs en cas de changement d'e-mail

Vous pouvez réinscrire automatiquement les utilisateurs lorsqu'ils changent d'adresse e-mail. Par exemple, si un utilisateur de l'espace de travail précédemment désabonné change son adresse e-mail pour une adresse qui ne figure pas sur la liste de désabonnement de Braze, il sera automatiquement réabonné.

\![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Pages et pieds de page d'abonnement

{% tabs local %}
{% tab Custom Footer %}

Pour les e-mails commerciaux, la [loi CAN-SPAM](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) exige que tous les e-mails commerciaux comportent une option de désabonnement. Grâce aux paramètres de pied de page personnalisés, vous êtes en mesure de respecter les normes CAN-SPAM tout en personnalisant votre pied de page d'exclusion de l'e-mail. Pour rester conforme, vous devez ajouter votre pied de page personnalisé à tous les e-mails envoyés dans le cadre de campagnes pour cet espace de travail.

Tenez compte des exigences suivantes lors de la création d'un pied de page personnalisé pour votre envoi de messages e-mail :
- Vous devez inclure une adresse URL de désabonnement et une adresse postale.
- Elle doit être inférieure à 100 KB.

\![]({% image_buster /assets/img/email_settings/custom_footer.png %})

Pour en savoir plus sur le modèle de pied de page personnalisé Liquid, consultez notre documentation sur les [pieds de page personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

{% endtab %}
{% tab Custom Unsubscribe Page %}

Braze vous permet de créer une **page de désabonnement personnalisée** avec votre propre code HTML. Cette page s'affiche lorsqu'un utilisateur a choisi de se désabonner au bas d'un e-mail. Notez que cette page doit avoir une taille inférieure à 750 KB. 

\![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

Pour en savoir plus sur les meilleures pratiques en matière de gestion des [abonnements aux]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses) services d'e-mail, consultez la rubrique [Gestion des abonnements aux services d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% tab Custom Opt-In Page %}

Vous pouvez créer une page d'abonnement personnalisée en utilisant votre propre code HTML. L'inclure dans votre e-mail peut être particulièrement bénéfique si vous souhaitez que votre image de marque et votre message restent cohérents tout au long du cycle de vie de l'utilisateur. Notez que cette page doit avoir une taille inférieure à 750 KB. 

\![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

Pour en savoir plus sur les meilleures pratiques en matière de gestion des [abonnements aux]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses) services d'e-mail, consultez la rubrique [Gestion des abonnements aux services d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% endtabs %}

## Questions fréquemment posées

### Désinscription en un clic

{% details Can the one-click unsubscribe URL (via list-unsubscribe header) link to a preference center? %}
Non, cela n'est pas conforme à la norme RFC 8058, ce qui signifie que vous ne serez pas en conformité avec les exigences de Yahoo et de Gmail en matière de désabonnement en un seul clic.
{% enddetails %}

{% details Why do I receive the error message "Your email body does not include an unsubscribe link" when composing my preference center? %}
Un centre de préférences n'est pas considéré comme un lien de désinscription. Les destinataires de vos e-mails doivent avoir la possibilité de se désabonner de tout e-mail commercial pour rester conformes à la norme CAN-SPAM.
{% enddetails %}

{% details Will I need to edit past email campaigns and Canvases to apply the one-click unsubscribe setting after enabling it? %}
Si vous n'avez aucun des cas d'utilisation pour le paramètre de désabonnement à la liste en un clic au niveau du message, aucune action n'est requise tant que le paramètre est activé dans les **préférences d'e-mail.** Braze ajoutera automatiquement les en-têtes de désinscription en un clic à tous les messages marketing et promotionnels envoyés. Toutefois, si vous devez configurer le comportement de désabonnement en un clic au niveau de chaque message, vous devrez mettre à jour les campagnes précédentes et les étapes du canvas avec l'e-mail en conséquence.
{% enddetails %}

{% details I can see the list-unsubscribe and one-click unsubscribe header in the original message or raw data, but why don't I see the Unsubscribe button in Gmail or Yahoo? %}
Gmail et Yahoo décident en fin de compte d'afficher ou non l'en-tête "liste de désabonnement" ou "désabonnement en un seul clic". Pour les nouveaux expéditeurs ou les expéditeurs dont la réputation d'expéditeur est faible, il peut arriver que le bouton de désabonnement ne s'affiche pas.
{% enddetails %}

{% details Does the custom one-click unsubscribe header support Liquid? %}
Oui, les liquides et la logique conditionnelle sont pris en charge pour permettre la création d'URL de désabonnement dynamiques en un clic pour l'en-tête.
{% enddetails %}

{% alert tip %}
Si vous ajoutez une logique conditionnelle, évitez d'avoir des valeurs de sortie qui ajoutent des espaces à votre URL, car Braze ne supprime pas ces espaces.
{% endalert %}

### Liste de désabonnement en un clic au niveau du message

{% details If I add the email headers for one-click manually, and I have the email unsubscribe header turned on, what is the expected behavior? %}
Les en-têtes d'e-mail ajoutés pour la liste de désinscription en un clic seront appliqués à tous les envois ultérieurs de cette campagne.
{% enddetails %}

{% details Why do subscription groups have to match across message variants in order to launch? %}
Pour une campagne avec test A/B, Braze enverra au hasard à un utilisateur l'une des variantes. Si deux groupes d'abonnement différents sont définis pour la même campagne (la variante A est définie pour le groupe d'abonnement A et la variante B est définie pour le groupe d'abonnement B), nous ne pouvons pas garantir que les utilisateurs qui sont uniquement abonnés au groupe d'abonnement B recevront la variante B. Il peut arriver que des utilisateurs se désabonnent d'un groupe d'abonnement pour lequel ils se sont déjà désabonnés.
{% enddetails %}

{% details The email unsubscribe header setting is turned off in Email Preferences, but in my campaign's sending info, the one-click list-unsubscribe setting is set to "Use workspace default". Is this a bug? %}
Non. Si le paramètre de l'espace de travail est désactivé et que le paramètre d'envoi des messages est défini sur **Utiliser l'espace de travail par défaut**, Braze suivra ce qui est configuré dans **les Préférences de messagerie.** Cela signifie que nous n'ajouterons pas l'en-tête de désabonnement en un clic pour la campagne.
{% enddetails %}

{% details What happens if a subscription group is archived? Will this break the one-click unsubscribe on emails sent? %}
Si un groupe d'abonnement référencé dans les **informations d'envoi** pour un clic est archivé, Braze continuera à traiter les désabonnements à partir d'un clic. Le groupe d'abonnement ne sera plus affiché dans le tableau de bord (filtre de segmentation, profil utilisateur et autres zones similaires).
{% enddetails %}

{% details Is the one-click unsubscribe setting available for email templates? %}
Non, nous ne prévoyons pas actuellement d'ajouter cette fonctionnalité pour les modèles d'e-mail, car ces modèles ne sont pas assignés à un domaine d'envoi. Si vous êtes intéressé par cette fonctionnalité pour les modèles d'e-mail, soumettez vos [commentaires sur le produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% enddetails %}

{% details Does this feature check that the one-click unsubscribe URL added to the custom option is valid? %}
Non, nous ne vérifions ni ne validons aucun lien dans le tableau de bord de Braze. Veillez à tester correctement votre URL avant de la lancer.
{% enddetails %}


