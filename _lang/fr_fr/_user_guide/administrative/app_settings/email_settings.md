---
nav_title: "Préférences en matière d'e-mail"
article_title: Préférences des e-mails
page_type: reference
page_order: 14
description: "Cet article de référence couvre les préférences d'e-mail dans le tableau de bord de Braze, y compris les configurations d'envoi, les pixels de suivi d'ouverture, la page et les pieds de page d'abonnement, et plus encore."
tool: Dashboard
channel: email
toc_headers: h2

---

# Préférences des e-mails

> Les préférences de messagerie sont l'endroit où vous pouvez définir des paramètres spécifiques pour les emails sortants, comme des pieds de page personnalisés, des pages de souscription et de désinscription personnalisées, et plus encore. Inclure ces options dans vos e-mails sortants permet d'offrir une expérience fluide et cohérente à vos utilisateurs.

Les **Préférences de messagerie** se trouvent sous **Paramètres** dans le tableau de bord.

## Configuration de l’envoi

Les paramètres de messagerie sous la section **Configuration d'envoi** déterminent quels détails sont inclus dans vos campagnes par e-mail. Ces paramètres concernent notamment ce que vos utilisateurs voient quand ils reçoivent un e-mail de Braze.

### Paramètres d’e-mail sortant

Lorsque vous configurez vos paramètres de messagerie, vos paramètres d’e-mails sortants identifient le nom et les adresses utilisées quand Braze envoient des courriers électroniques à vos utilisateurs.

{% tabs local %}
{% tab Display Name Address %}

Dans cette section, vous pouvez ajouter les noms et les adresses e-mail à utiliser lorsque Braze envoie des e-mails à vos utilisateurs. Les noms d'affichage et les adresses e-mail sont disponibles dans les options **Modifier les informations d'envoi** lorsque vous composez votre campagne d'e-mail. Notez que les mises à jour apportées aux paramètres des e-mails sortants n'affectent pas rétroactivement les envois existants.

![Section "Paramètres de l'e-mail sortant" avec des champs pour différents noms d'affichage et domaines.]({% image_buster /assets/img/email_settings/display_name_address.png %})

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

L’ajout d’une adresse e-mail dans cette section vous permet de la sélectionner en tant qu’adresse de réponse pour votre campagne d’e-mails. Vous pouvez également définir une adresse e-mail par défaut en sélectionnant **Définir par défaut**. Ces adresses e-mail seront disponibles dans les options **Edit Sending Info** lorsque vous rédigerez votre campagne par e-mail.

![Section "Adresse de réponse" avec des champs permettant de saisir plusieurs adresses de réponse.]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

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

Cette section vous permet de gérer les adresses CCI que vous pouvez ajouter aux messages e-mail sortants envoyés depuis Braze. L'ajout d'une adresse CCI à un envoi e-mail envoie une copie identique du message que votre utilisateur reçoit dans votre boîte de réception CCI. Cet outil est utile pour conserver des copies des messages que vous avez envoyés à vos utilisateurs pour des raisons de conformité ou d'assistance à la clientèle. Les e-mails en copie cachée ne sont pas inclus dans les rapports et les analyses des e-mails.

Les adresses CCI ne sont disponibles que pour SendGrid et SparkPost. Comme alternative aux adresses CCI, nous vous recommandons d'utiliser l'[archivage des messages]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving/) pour enregistrer une copie des messages envoyés aux utilisateurs à des fins d'archivage ou de conformité.

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

![La section Adresse CCI de l'onglet Paramètres de l'e-mail.]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

Une fois que vous avez ajouté une adresse, celle-ci sera disponible pour être sélectionnée lors de la composition d'un e-mail dans les campagnes ou les étapes du canvas. Sélectionnez **Définir par défaut** à côté d'une adresse pour définir cette adresse comme étant sélectionnée par défaut lors du lancement d'une nouvelle campagne par e-mail ou d'un composant Canvas. Pour remplacer cela au niveau du message, vous pouvez sélectionner **Pas de CCI** lors de la configuration de votre message.

Si vous exigez que tous les messages électroniques envoyés depuis Braze incluent une adresse BCC, vous pouvez sélectionner le bouton **Exiger une adresse BCC pour toutes vos campagnes par e-mail**. Pour ce faire, vous devrez sélectionner une adresse par défaut, qui sera automatiquement sélectionnée lors de nouvelles campagnes d'e-mail ou étapes du canvas. L’adresse par défaut sera également automatiquement ajoutée à tous les messages déclenchés via notre API REST. Il n’est pas nécessaire de modifier la demande API existante pour inclure l’adresse.

#### CCI dynamique

Avec la CCI dynamique, vous pouvez utiliser du liquide dans votre adresse de CCI. Notez que cette fonctionnalité n'est disponible que dans les **préférences d'e-mail** et ne peut pas être définie dans la campagne elle-même. Une seule adresse CCI est autorisée par destinataire de l'e-mail.

{% raw %}`{{custom_attribute.${support_agent}}}`{% endraw %} Par exemple, vous pouvez ajouter Teams comme adresse CCI pour les e-mails de votre équipe d'assistance.

![La section Adresse CCI de l'onglet Paramètres de l'e-mail avec une adresse CCI à l'aide de Liquid.]({% image_buster /assets/img/email_settings/dynamic_bcc.png %}){: style="max-width:90%;" }

{% endtab %}
{% endtabs %}

## Pixel de suivi de l’ouverture d’e-mail

[![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

Le pixel de suivi d'ouverture d'e-mail est une image invisible de 1 x 1 px qui est automatiquement insérée dans le code HTML de votre e-mail. Ce pixel permet à Braze de détecter si vos utilisateurs ont ouvert votre e-mail. Lorsque le client e-mail d'un utilisateur fait une demande à notre pixel de suivi, la demande peut contenir des informations telles que l'adresse IP, l'agent utilisateur et l'horodatage. Les informations sur l'ouverture des e-mails peuvent être très utiles, vous aidant à déterminer des stratégies de marketing efficaces en comprenant les taux d'ouverture correspondants.

### Placement du pixel de suivi

Le comportement par défaut dans Braze est d'ajouter le pixel de suivi en bas de votre e-mail. Pour la grande majorité des utilisateurs, c’est l’endroit idéal pour placer le pixel. Bien que le pixel soit déjà conçu pour provoquer le moins de différences visuelles possible, tout changement visuel involontaire sera le moins visible au bas de l’e-mail. C’est également la valeur par défaut pour les fournisseurs d’e-mail tels que SendGrid et SparkPost.

### Modification de l’emplacement du pixel de suivi

Braze prend actuellement en charge le remplacement de l’emplacement par défaut du pixel de suivi d’ouverture par défaut de l’ESP (la dernière balise dans le `<body>` d’un e-mail) pour le déplacer vers la première balise dans le `<body>`.
  
!["Ouvrir la section Pixel de suivi" avec les options de déplacement pour SendGrid, SparkPost, ou Amazon SES.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

Pour modifier l’emplacement :

1. Dans Braze, allez à **Paramètres** > **Préférences de messagerie**.
2. Sélectionnez parmi les options suivantes : **Passer à SendGrid**, **passer à SparkPost** ou **passer à Amazon SES**
3. Sélectionnez **Enregistrer**.

Après avoir enregistré, Braze envoie des instructions spéciales à l'ESP pour qu'il place le pixel de suivi des ouvertures en haut de tous les e-mails HTML.
  
{% alert important %}
L'activation du SSL enveloppe l'URL du pixel de suivi avec HTTPS au lieu de HTTP. Si votre SSL est mal configuré, cela peut affecter l'efficacité du pixel de suivi.
{% endalert %}

## En-tête de désabonnement de liste {#list-unsubscribe}

{% alert note %}
Depuis le 15 février 2024, l'en-tête list-unsubscribe (avec désabonnement en un clic) est activé par défaut pour les nouvelles entreprises.
{% endalert %}

L'utilisation d'un en-tête de désabonnement de liste permet à vos destinataires de se désabonner facilement des e-mails marketing en affichant un bouton **Désabonner** dans l'interface utilisateur de la boîte aux lettres, et non dans le corps du message.

![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

Lorsqu'un destinataire sélectionne **Se désabonner**, le fournisseur de la boîte aux lettres envoie la demande de désabonnement à la destination définie dans l'en-tête de l'e-mail.

L’activation du désabonnement de liste est une bonne pratique de livrabilité et une exigence chez certains des principaux fournisseurs de messagerie. Il encourage les utilisateurs finaux à se débarrasser en toute sécurité des messages indésirables, au lieu d'appuyer sur le bouton "spam" d'un client e-mail, ce qui nuit à la réputation de l'envoi et à la livrabilité de l'e-mail.

Lorsque vous [gérez vos abonnements dans Gmail](https://support.google.com/mail/answer/15621070?sjid=2292320204527911296-NC), Gmail peut également récupérer le lien de désabonnement dans le corps du message, mais donne la priorité à la liste de désabonnement s'il est présent dans l'en-tête.

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

_\*Yahoo et Gmail finiront par supprimer l'en-tête "mailto :" et n'autoriseront que le simple clic._

L'affichage de l'en-tête est déterminé par le fournisseur de messagerie. Pour vérifier si l'en-tête de désabonnement de liste est inclus dans l'e-mail brut (texte) pour le destinataire dans Gmail, procédez comme suit :

1. Sélectionnez **Afficher l'original** dans l'e-mail. Cela ouvre un nouvel onglet avec la version brute de l'e-mail et ses en-têtes.
2. Recherchez « List-Unsubscribe ».

Si l'en-tête figure dans la version brute de l'e-mail mais n'est pas affiché, le fournisseur de la boîte aux lettres a décidé de ne pas afficher l'option de désabonnement, ce qui signifie que nous n'avons pas d'autres informations sur la raison pour laquelle le fournisseur de la boîte aux lettres n'affiche pas l'en-tête. L’affichage de l'en-tête de désabonnement de liste est finalement basé sur la réputation. Dans la plupart des cas, plus votre réputation d'expéditeur est bonne auprès du fournisseur de boîtes aux lettres, plus l'en-tête list-unsubscribe est susceptible d'apparaître.

### En-tête de désabonnement par e-mail dans les espaces de travail

![S'abonner aux "utilisateurs abonnés ou ayant opté pour l'abonnement" pour savoir à quels utilisateurs envoyer le message.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Lorsque la fonctionnalité d'en-tête de désabonnement aux e-mails est activée, ce paramètre s'applique à l'ensemble de l'espace de travail, et non à l'entreprise. Il est ajouté aux campagnes et aux Canvas qui sont configurés pour envoyer aux utilisateurs qui sont abonnés ou opt-in, ou aux utilisateurs opt-in dans l'étape de l'**audience cible** des générateurs de campagnes et de Canvas.

Lorsque vous utilisez l'espace de travail par défaut, Braze n'ajoute pas l'en-tête de désabonnement en un clic pour les campagnes considérées comme transactionnelles, qui sont configurées pour "envoyer à tous les utilisateurs, y compris les utilisateurs désabonnés". Pour passer outre et ajouter l'en-tête de désabonnement en un clic lors de l'envoi aux utilisateurs désabonnés, vous pouvez sélectionner **Se désabonner globalement de tous les e-mails** dans les paramètres généraux des messages de la liste de désabonnement en un clic.

### En-tête de désabonnement de liste par défaut

{% alert important %}
Gmail souhaite que les expéditeurs mettent en œuvre le désabonnement en un seul clic pour tous leurs messages commerciaux et promotionnels sortants à compter du 1er juin 2024. Pour plus d'informations, consultez les [directives de Gmail relatives à l’expéditeur](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) et la [FAQ sur les directives de Gmail relatives aux expéditeurs d’e-mails](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). Yahoo a annoncé un calendrier début 2024 pour la mise à jour de ses exigences. Pour plus d'informations, consultez le site [Plus de sécurité, moins de spam : Application des normes en matière d’e-mails pour une meilleure expérience](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Pour utiliser la fonctionnalité de désabonnement de Braze afin de traiter directement les désabonnements, sélectionnez **Inclure un en-tête de liste de désabonnement en un clic (mailto et HTTP) pour les e-mails envoyés aux utilisateurs abonnés ou ayant opté pour l'abonnement** et sélectionnez **Braze par défaut** comme URL et mail-to standard de Braze. 

![Option pour inclure automatiquement un en-tête de désabonnement de liste pour les e-mails envoyés aux utilisateurs abonnés ou inscrits.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze prend en charge les versions suivantes de l'en-tête de désabonnement de liste :

| Version de désabonnement de la liste | Description | 
| ----- | --- |
| Un clic (RFC 8058) | Offre aux destinataires un moyen simple de se désabonner des e-mails en un seul clic. Ceci est une exigence de Yahoo et Gmail pour les expéditeurs d’e-mails groupés. |
| URL de désabonnement de la liste ou HTTPS | Fournit aux destinataires un lien qui les dirige vers une page web où ils peuvent se désabonner. |
| Mailto | Spécifie une adresse e-mail comme destination du message de demande de désabonnement à envoyer par le destinataire à la marque. <br><br> _Pour traiter les demandes de désabonnement de liste de diffusion, ces demandes de désabonnement doivent inclure l'adresse e-mail telle qu'elle est stockée dans Braze pour l'utilisateur final qui se désabonne. Cette information peut être fournie par l'adresse "from-address" de l'e-mail à partir duquel l'utilisateur final se désabonne, l'objet codé ou le corps codé de l'e-mail reçu par l'utilisateur final et dont il se désabonne. Dans des cas très limités, certains fournisseurs de boîtes de réception n'adhèrent pas au protocole [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368), ce qui fait que l'adresse e-mail n'est pas correctement transmise. La demande de désabonnement risque alors de ne pas pouvoir être traitée dans Braze._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Lorsque Braze reçoit une demande de désabonnement de liste de la part d'un utilisateur via l'une des méthodes ci-dessus, l'état d'abonnement global de cet utilisateur est défini sur Désabonné. S'il n'y a pas de correspondance, Braze ne traite pas cette demande.

### Désabonnement en un clic

L'utilisation de l'en-tête list-unsubscribe[(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)), qui permet de se désabonner en un seul clic, vise à offrir aux destinataires un moyen simple de se désabonner des e-mails.

### Désabonnement de liste en un clic au niveau du message

Le paramètre de désabonnement à la liste en un clic au niveau du message remplace les fonctionnalités de l'en-tête de désabonnement à l'e-mail pour les espaces de travail. Appliquez le comportement de désabonnement en un clic par campagne ou par étape de canvas pour les utilisations suivantes :

- Ajouter un désabonnement en un clic de Braze pour un groupe d'abonnement spécifique afin de prendre en charge plusieurs marques/listes au sein d'un même espace de travail
- Basculer entre le désabonnement par défaut de Braze ou l'URL personnalisée
- Ajouter votre URL de désabonnement en un clic personnalisée
- Ignorer le désabonnement en un clic sur ce message

{% alert note %}
Le paramètre de désabonnement à la liste en un clic au niveau du message n'est disponible que lors de l'utilisation de l'éditeur par glisser-déposer et de l'éditeur HTML mis à jour. Si vous utilisez l'éditeur HTML précédent, passez à l'éditeur HTML mis à jour pour utiliser cette fonctionnalité.
{% endalert %}

Dans votre éditeur d'e-mails, allez à **Paramètres d'envoi** > **Informations d'envoi**. Sélectionnez parmi les options suivantes :

- **Utiliser l'espace de travail par défaut**: Utilise les paramètres de **l'en-tête de désabonnement par e-mail** définis dans les **préférences de messagerie**. Toute modification apportée à ce paramètre s'applique à tous les messages.
- **Se désabonner de manière générale de tous les e-mails** : Utilise l’en-tête de désabonnement en un clic par défaut de Braze. Les utilisateurs qui cliquent sur le bouton de désabonnement ont leur abonnement global à l'e-mail réglé sur "Désabonné".
- **Se désabonner d'un groupe d'abonnement spécifique**: Utilise le groupe d'abonnement spécifié. Braze désabonne les utilisateurs qui cliquent sur le bouton de désabonnement du groupe d'abonnement sélectionné.
    - Lors de la sélection d'un groupe d'abonnement, ajoutez le filtre **Groupe d'abonnement** dans **Publics cibles** pour ne cibler que les utilisateurs abonnés à ce groupe spécifique. Le groupe d'abonnement sélectionné pour le désabonnement en un clic doit correspondre au groupe d'abonnement que vous ciblez. En cas d'incohérence dans le groupe d'abonnement, vous risquez d'envoyer un message à un utilisateur qui tente de se désabonner d'un groupe d'abonnement dont il s'est déjà désabonné.

{% alert important %}
Le paramètre **Se désabonner d'un groupe d'abonnement spécifique** ne s'applique qu'à l'en-tête Désabonnement de **la** liste en un clic. L'en-tête mailto list-unsubscribe n'est pas affecté par cette option. Cela signifie qu'un destinataire qui se désabonne à l'aide de cette méthode enregistre une désinscription globale, et non une désinscription du groupe d'abonnement spécifique. Pour exclure l'en-tête mailto list-unsubscribe de la désinscription globale des utilisateurs, lorsque vous sélectionnez ce paramètre, contactez l'[assistance.]({{site.baseurl}}/support_contact/)
{% endalert %}

- **Personnalisé :** Ajoute votre URL personnalisée de désabonnement en un clic vous permettant de traiter directement les demandes de désabonnement.
- **Exclure le désabonnement**

{% alert important %}
L’exclusion du désabonnement en un clic ou de tout mécanisme de désabonnement devrait uniquement être appliquée aux messages transactionnels, tels que les réinitialisations de mot de passe, les reçus et les e-mails de confirmation.
{% endalert %}

Adjust this setting overrides the default behavior for one-click list unsubscribe in this e-mail.

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

Utilisez le basculeur pour inclure "[TEST]" et "[SEED]" dans les lignes d'objet de vos e-mails de test et d'initiateur. Cela peut vous aider à identifier les campagnes par e-mail envoyées en tant que tests.

![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## L'option par défaut de l'inclusion CSS des nouveaux e-mails est activée par défaut

L’inclusion CSS est une technique qui intègre automatiquement les styles CSS pour vos e-mails et nouveaux e-mails. Pour certains clients de messagerie électronique, cela peut améliorer le rendu de vos e-mails.

La modification de ce paramètre n'affecte aucun de vos messages e-mail ou modèles existants. Vous pouvez remplacer cette valeur par défaut à tout moment lors de la composition de vos messages ou modèles. Pour plus d'informations, reportez-vous à l'[insertion CSS.]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/css_inline/)

## Réabonnez les utilisateurs lorsque leurs e-mails changent

Vous pouvez réabonner automatiquement les utilisateurs lorsqu’ils changent leur adresse e-mail. Par exemple, si un utilisateur de l'espace de travail précédemment désabonné change son adresse e-mail pour une adresse qui ne figure pas sur la liste de désabonnement de Braze, il est automatiquement réabonné.

![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Pages et pieds de page pour le désabonnement

{% tabs local %}
{% tab Custom Footer %}

Pour les courriels commerciaux, la [loi CAN-SPAM](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) exige que tous les courriels commerciaux incluent une option de désabonnement. Grâce aux paramètres de pied de page personnalisés, vous pouvez rester conforme à la loi CAN-SPAM tout en personnalisant votre pied de page de désabonnement par e-mail. Pour rester conforme, vous devez ajouter votre pied de page personnalisé à tous les e-mails envoyés dans le cadre des campagnes de cet espace de travail.

Notez les exigences suivantes lors de la création d’un pied de page personnalisé pour votre envoi de messages par e-mail :
- Doit inclure une URL de désabonnement et une adresse postale.
- Doivent faire moins de 100 Ko.

![]({% image_buster /assets/img/email_settings/custom_footer.png %})

Pour en savoir plus sur la personnalisation des pieds de page avec Liquid, consultez notre documentation sur les [pieds de page personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

{% endtab %}
{% tab Custom Unsubscribe Page %}

Braze vous permet de définir une **page de désabonnement personnalisée** avec votre propre HTML. Cette page apparaît après qu'un utilisateur a choisi de se désabonner au bas d'un e-mail. Notez que cette page doit faire moins de 750 Ko. 

![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

En savoir plus sur les meilleures pratiques de gestion des listes de diffusion dans [Gestion des abonnements aux e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% tab Custom Opt-In Page %}

Vous pouvez créer une page d’abonnement personnalisée à l’aide de votre propre HTML. Inclure cela dans votre e-mail peut être particulièrement bénéfique si vous voulez que votre branding et vos messages soient cohérents pendant toute la durée de vie de votre client. Notez que cette page doit faire moins de 750 Ko. 

![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

En savoir plus sur les meilleures pratiques de gestion des listes de diffusion dans [Gestion des abonnements aux e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% endtabs %}

{% alert tip %}
Dans la section **Aperçu** d'une page ou d'un pied de page d'abonnement, sélectionnez **Copier le lien d'aperçu** pour générer et copier un lien d'aperçu partageable qui montre à quoi ressemble le pied de page de l'e-mail, la page de désabonnement ou la page d'abonnement pour un utilisateur aléatoire. Le lien dure sept jours avant de devoir être régénéré.
{% endalert %}

## Foire aux questions

### Désabonnement en un clic

{% details Can the one-click unsubscribe URL (via list-unsubscribe header) link to a preference center? %}
Non, cela ne respecte pas le protocole RFC 8058, ce qui signifie que vous ne serez pas en conformité avec l'exigence de désabonnement en un clic de Yahoo et Gmail.
{% enddetails %}

{% details Why do I receive the error message "Your email body does not include an unsubscribe link" when composing my preference center? %}
Un centre de préférences n'est pas considéré comme un lien de désabonnement. Vos destinataires d'e-mails doivent avoir la possibilité de se désabonner de tout e-mail commercial pour rester conformes à la loi CAN-SPAM.
{% enddetails %}

{% details Do I need to edit past email campaigns and Canvases to apply the one-click unsubscribe setting after enabling it? %}
Si vous n'avez aucun des cas d'utilisation pour le paramètre de désabonnement en un clic au niveau du message, aucune action n'est requise tant que le paramètre est activé dans les **Préférences de messagerie**. Braze ajoute automatiquement les en-têtes de désabonnement en un clic à tous les messages marketing et promotionnels sortants. Toutefois, si vous devez configurer le comportement de désabonnement en un clic au niveau de chaque message, vous devrez mettre à jour les campagnes précédentes et les étapes du canvas avec l'e-mail en conséquence.
{% enddetails %}

{% details I can see the list-unsubscribe and one-click unsubscribe header in the original message or raw data, but why don't I see the Unsubscribe button in Gmail or Yahoo? %}
Au final, ce sont Gmail et Yahoo qui décident d'afficher ou non l'en-tête de désabonnement de liste ou de désabonnement en un clic. Pour les nouveaux expéditeurs ou les expéditeurs dont la réputation d'expéditeur est faible, il peut arriver que le bouton de désabonnement ne s'affiche pas.
{% enddetails %}

{% details Does the custom one-click unsubscribe header support Liquid? %}
Oui, le Liquid et la logique conditionnelle sont pris en charge pour permettre des URL de désabonnement dynamiques en un clic pour l'en-tête.
{% enddetails %}

{% alert tip %}
Si vous ajoutez une logique conditionnelle, évitez d'avoir des valeurs de sortie qui ajoutent des espaces à votre URL, car Braze ne supprime pas ces espaces.
{% endalert %}

### Désabonnement de liste en un clic au niveau du message

{% details If I add the email headers for one-click manually, and I have the email unsubscribe header turned on, what is the expected behavior? %}
Les en-têtes d'e-mail ajoutés pour le désabonnement à la liste en un clic s'appliquent à tous les envois ultérieurs de cette campagne.
{% enddetails %}

{% details Why do subscription groups have to match across message variants in order to launch? %}
Pour une campagne avec test A/B, Braze envoie au hasard à un utilisateur l'une des variantes. Si deux groupes d'abonnement différents sont définis pour la même campagne (la variante A est définie pour le groupe d'abonnement A et la variante B est définie pour le groupe d'abonnement B), nous ne pouvons pas garantir que les utilisateurs abonnés uniquement au groupe d'abonnement B recevront la variante B. Il peut arriver que des utilisateurs se désabonnent d'un groupe d'abonnement dont ils se sont déjà désabonnés.
{% enddetails %}

{% details The email unsubscribe header setting is turned off in Email Preferences, but in my campaign's sending info, the one-click list-unsubscribe setting is set to "Use workspace default". Is this a bug? %}
Non. Si le paramètre de l'espace de travail est désactivé et que le paramètre d'envoi des messages est défini sur **Utiliser l'espace de travail par défaut**, Braze suit alors ce qui est configuré dans **les Préférences de messagerie.** Cela signifie que nous n'ajoutons pas l'en-tête de désabonnement en un clic pour la campagne.
{% enddetails %}

{% details What happens if a subscription group is archived? Does this break the one-click unsubscribe on emails sent? %}
Si un groupe d'abonnement référencé dans les **informations d'envoi** pour un clic est archivé, Braze continue à traiter les désabonnements à partir d'un clic. Le groupe d'abonnement n'apparaît plus dans le tableau de bord (filtre de segmentation, profil utilisateur et autres zones similaires).
{% enddetails %}

{% details Is the one-click unsubscribe setting available for email templates? %}
Non, nous ne prévoyons pas actuellement d'ajouter cette fonctionnalité pour les modèles d'e-mail, car ces modèles ne sont pas assignés à un domaine d'envoi. Si vous êtes intéressé par cette fonctionnalité pour les modèles d'e-mails, soumettez [des commentaires sur le produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% enddetails %}

{% details Does this feature check that the one-click unsubscribe URL added to the custom option is valid? %}
Non, nous ne vérifions ni ne validons aucun lien dans le tableau de bord Braze. Assurez-vous de bien tester votre URL avant le lancement.
{% enddetails %}
