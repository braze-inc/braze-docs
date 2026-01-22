{% if include.metric == "AMP Clicks" %}
Le terme <i>Clics AMP</i> désigne le nombre total de clics dans votre e-mail HTML AMP, nombre cumulé des versions HTML, texte brut et HTML AMP de l'e-mail.
{% endif %}

{% if include.metric == "AMP Opens" %}
Le terme <i>Ouvertures AMP</i> désigne le nombre total d’ouvertures dans votre e-mail HTML AMP et dans les versions HTML AMP de l'e-mail.
{% endif %}

{% if include.metric == "Audience" %}
L'<i>audience</i> est le pourcentage d'utilisateurs qui ont reçu un message particulier. Ce chiffre est envoyé par Braze.
{% endif %}

{% if include.metric == "Bounces" %}
<i>Les rebonds</i> correspondent au nombre total d'envois de messages qui n'ont pas été remis à leurs destinataires.
{% endif %}

{% if include.metric == "Estimated Real Opens" %}
L'<i>estimation des ouvertures réelles</i> est une estimation du nombre d'ouvertures uniques qu'il y aurait si les ouvertures de machines n'existaient pas, et est le résultat d'un modèle statistique propriétaire de Braze.
{% endif %}

{% if include.metric == "Help" %}
On parle d'<i>aide</i> lorsqu'un utilisateur a répondu à votre message avec un <a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">mot-clé AIDE</a> et qu'une réponse automatique AIDE lui a été envoyée.
{% endif %}

{% if include.metric == "Hard Bounce" %}
On parle d'échec <i>d'envoi</i> définitif lorsqu'un e-mail ne parvient pas au destinataire en raison d'une erreur de réception/distribution permanente. Un échec d'envoi définitif peut se produire parce que le nom de domaine n’existe pas ou parce que le destinataire est inconnu.
{% endif %}

{% if include.metric == "Soft Bounce" %}
Un <i>échec provisoire d'envoi</i> survient lorsqu'un e-mail ne parvient pas au destinataire en raison d'une erreur de distribution temporaire, bien que l'adresse e-mail du destinataire soit valide. Un soft bounce peut se produire parce que la boîte de réception du destinataire est pleine, que le serveur était en panne ou que le message était trop volumineux pour la boîte de réception du destinataire.
{% endif %}

{% if include.metric == "Deferral" %}
On parle de <i>report</i> lorsqu'un e-mail n'a pas été livré immédiatement, mais que Braze relance l'e-mail jusqu'à 72 heures après cet échec temporaire de la réception/distribution afin de maximiser les chances de réussite avant l'arrêt des tentatives pour cette campagne spécifique.
{% endif %}

{% if include.metric == "Body Click" %}
Les notifications Push Story enregistrent un <i>clic du corps</i> lorsque la notification est cliquée. Aucun body click ne sera enregistré quand un message est développé ou lors de clics sur des boutons d’action.
{% endif %}

{% if include.metric == "Body Clicks" %}
Il y a <i>clic sur le corps</i> lorsqu'un utilisateur clique sur un message qui n'a pas de boutons (bouton 1, bouton 2) et qui a été créé avec l'éditeur traditionnel, et lorsqu'un message créé avec l'éditeur HTML ou l'éditeur glisser-déposer utilise <code>brazeBridge.logClick()</code> sans arguments.
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
Le terme <i>Clics du bouton 1</i> désigne le nombre total de clics sur le bouton 1 du message.
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
<i>Clics sur le bouton 2</i> est le nombre total de clics sur le bouton 2 du message.
{% endif %}

{% if include.metric == "Choices Submitted" %}
<i>Choix soumis</i> est le nombre total de choix sélectionnés lorsque l'utilisateur clique sur le bouton de soumission sur la page des questions d'une <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>enquête simple</a>.
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
Le <i>taux de clics d'ouverture</i> est le pourcentage d'e-mails ouverts qui ont été cliqués au moins une fois par un seul utilisateur ou une seule machine. Il n'est disponible que dans le <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>générateur de rapports.</a>
{% endif %}

{% if include.metric == "Close Message" %}
<i>Fermer le message</i> est le nombre total de clics sur le bouton de fermeture du message. Cela n'existe que pour les messages in-app créés dans l'éditeur par glisser-déposer, et non dans l'éditeur traditionnel.
{% endif %}

{% if include.metric == "Confirmed Deliveries" %}
On parle de <i>réceptions confirmées</i> lorsque l'opérateur a confirmé que le message a été délivré au numéro de téléphone cible.
{% endif %}

{% if include.metric == "Confidence" %}
La <i>confiance</i> est le pourcentage de certitude qu'une certaine variante d'un message donne de meilleurs résultats que le groupe de contrôle.
{% endif %}

{% if include.metric == "Confirmation Page Button" %}
<i>Bouton de la page</i> de confirmation est le nombre total de clics sur le bouton d'appel à l'action de la page de confirmation d'une <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>enquête simple</a>.
{% endif %}

{% if include.metric == "Confirmation Page Dismissals" %}
Le terme <i>Rejets Page de confirmation</i> désigne le nombre total de clics sur le bouton de fermeture (x) de la page de confirmation d'une <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>enquête simple</a>.
{% endif %}

{% if include.metric == "Conversion Rate" %}
Le <i>taux de conversion</i> est le pourcentage de fois où un événement défini s'est produit par rapport à l'ensemble des destinataires d'un message. Cet événement défini est déterminé lors de la création de la campagne.
{% endif %}

{% if include.metric == "Conversion Window" %}
La <i>fenêtre de conversion</i> est le nombre de jours suivant la réception du message pendant lesquels les actions de l'utilisateur sont suivies et attribuées à un événement de conversion. Les conversions survenant après cette période ne sont pas attribuées à l’événement de conversion.
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
Les conversions <i>(B, C, D)</i> sont des événements de conversion supplémentaires ajoutés après l'événement de conversion principal. Il s'agit du nombre de fois qu'un événement défini s'est produit après avoir interagi avec un message reçu d'une campagne Braze ou après l'avoir visualisé.
{% endif %}

{% if include.metric == "Total Conversions" %}
Le <i>nombre total de conversions</i> correspond au nombre total de fois où un utilisateur réalise un événement de conversion spécifique après avoir consulté une campagne de messages in-app.
{% endif %}

{% if include.metric == "Deliveries" %}
<i>Réception/distribution</i> est le nombre total d'envois de messages acceptés par le serveur de réception. Ceci ne signifie pas que le message a été distribué sur un appareil, mais seulement qu'il a été accepté par le serveur.
{% endif %}

{% if include.metric == "Deliveries %" %}
Le <i>% de livraisons</i> est le pourcentage du nombre total de messages (envois) qui ont été envoyés et reçus avec succès par les utilisateurs qui ont consenti à recevoir des e-mails.
{% endif %}

{% if include.metric == "Delivery Failures" %}
On parle d'<i>échec de réception/distribution</i> lorsque le SMS n'a pas pu être envoyé en raison d'un débordement des files d'attente (envoi de SMS à un débit supérieur à celui que vos codes longs ou courts peuvent supporter).
{% endif %}

{% if include.metric == "Delivery Failures RCS" %}
Les <i>échecs de réception/distribution</i> se produisent lorsque le RCS n'a pas pu être envoyé en raison d'un débordement des files d'attente (envoi de RCS à un rythme supérieur à celui que votre expéditeur vérifié peut gérer).
{% endif %}

{% if include.metric == "Failed Delivery Rate" %}
Le <i>taux de réception/distribution échouée</i> est le pourcentage d'envois qui ont échoué parce que le message n'a pas pu être envoyé. Cela peut se produire pour diverses raisons, notamment des débordements de file d'attente, des suspensions de compte et des erreurs de support dans le cas des MMS.
{% endif %}

{% if include.metric == "Direct Opens" %}
Le nombre d'<i>ouvertures directes</i> est le nombre total d'utilisateurs qui ont ouvert votre application ou votre site web en appuyant directement sur la notification.
{% endif %}

{% if include.metric == "Emailable" %}
<i>Emailable</i> est le nombre total d'utilisateurs qui ont une adresse e-mail dans leurs dossiers et qui ont explicitement opté pour un abonnement ou se sont abonnés.
{% endif %}

{% if include.metric == "Errors" %}
<i>Errors</i> est le nombre d'erreurs renvoyées par les événements webhook (incrémenté pendant le processus d'envoi).
{% endif %}

{% if include.metric == "Failures" %}
On parle d'<i>échec</i> lorsque le message WhatsApp n'a pas pu être envoyé parce que le fournisseur de services Internet a renvoyé un échec d’envoi définitif. Un échec d'envoi définitif est un échec permanent de la livrabilité.
{% endif %}

{% if include.metric == "Influenced Opens" %}
<i>Les ouvertures influencées</i> correspondent au nombre total (et au pourcentage) d'utilisateurs qui ont ouvert l'appli après l'envoi de la notification push, sans l'ouvrir directement.
{% endif %}

{% if include.metric == "Lifetime Revenue" %}
Le <i>revenu à vie</i> est la valeur <code>PurchaseEvents</code> totale (en USD) reçue depuis le début.
{% endif %}

{% if include.metric == "Lifetime Value Per User" %}
La <i>valeur vie par utilisateur</i> est le <i>chiffre vie d'affaires</i> divisé par le nombre total d'<i>utilisateurs</i> (situé sur votre page d'accueil).
{% endif %}

{% if include.metric == "Average Daily Revenue" %}
Le <i>chiffre d'affaires quotidien moyen</i> est la moyenne de la somme des chiffres d'affaires de la campagne et de Canvas pour un jour donné.
{% endif %}

{% if include.metric == "Daily Purchases" %}
Le terme <i>Achats quotidiens</i> désigne la moyenne du nombre total d’achats <code>PurchaseEvents</code> uniques au cours de la période.
{% endif %}

{% if include.metric == "Daily Revenue Per User" %}
Le <i>chiffre d'affaires quotidien par utilisateur</i> est le chiffre d'affaires quotidien moyen par utilisateur actif jour.
{% endif %}

{% if include.metric == "Machine Opens" %}
Les <i>ouvertures de machines</i> incluent la proportion d'"ouvertures" qui sont affectées par la protection de la confidentialité dans Mail (MPP) d'Apple pour iOS 15. Par exemple, si un utilisateur ouvre un e-mail à l'aide de l'application Mail sur un appareil Apple, cela sera enregistré comme une <i>ouverture de machine.</i>
{% endif %}

{% if include.metric == "Other Opens" %}
Les <i>autres ouvertures</i> comprennent les e-mails qui n'ont pas été identifiés comme des <i>ouvertures de machines.</i> Par exemple, lorsqu'un utilisateur ouvre un e-mail sur une autre plateforme (telle que l'application Gmail sur un téléphone, Gmail sur un navigateur de bureau), cela sera enregistré comme une <i>Autre ouverture.</i>
{% endif %}

{% if include.metric == "Opens" %}
Les <i>ouvertures</i> sont des instances incluant à la fois les <i>ouvertures directes</i> et les <i>ouvertures influencées</i> dans lesquelles le SDK de Braze a déterminé, à l'aide d'un algorithme propriétaire, qu'une notification push a incité un utilisateur à ouvrir l'appli.
{% endif %}

{% if include.metric == "Opt-Out" %}
On parle d'<i>abonnement</i> lorsqu'un utilisateur a répondu à votre message avec un <a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">mot-clé d'exclusion</a> et qu'il s'est désabonné de votre programme SMS ou RCS.
{% endif %}

{% if include.metric == "Pending Retry" %}
Le terme <i>En attente d’une nouvelle tentative</i> désigne le nombre de demandes qui ont été temporairement rejetées par le serveur destinataire, mais qui ont fait l'objet d'une nouvelle tentative de livraison par le fournisseur de services d’e-mailing. Le fournisseur de services de courrier électronique va réessayer jusqu’à ce qu’un délai soit atteint (généralement 72 heures).
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
Les <i>conversions principales (A)</i> ou <i>événement de conversion principal</i> correspondent au nombre de fois qu'un événement défini s'est produit après avoir interagi avec un message reçu dans le cadre d'une campagne de Braze ou après l'avoir visualisé. Cet événement défini est déterminé par vous lorsque vous créez la campagne.
{% endif %}

{% if include.metric == "Reads" %}
La <i>lecture</i> est le moment où l'utilisateur lit le message. Les reçus de lecture de l'utilisateur doivent être activés pour que Braze puisse assurer le suivi des lectures.
{% endif %}

{% if include.metric == "Read Rate" %}
Le <i>taux de lecture</i> est le pourcentage d'envois qui ont abouti à une lecture. Cette information n'est donnée que pour les utilisateurs qui ont activé les accusés de réception.
{% endif %}

{% if include.metric == "Received" %}
La <i>réception</i> est définie différemment selon les canaux et peut avoir lieu lorsque les utilisateurs consultent le message, lorsqu'ils effectuent une action de déclenchement définie ou lorsque le message est envoyé au fournisseur de messages.
{% endif %}

{% if include.metric == "Rejections" %}
Il y a <i>rejet</i> lorsque le SMS ou le RCS a été rejeté par l'opérateur. Cela peut se produire pour plusieurs raisons, notamment le filtrage du contenu par l'opérateur, la disponibilité de l'appareil de destination, le fait que le numéro de téléphone n'est plus en service, etc.
{% endif %}

{% if include.metric == "Revenue" %}
Le <i>chiffre d'affaires</i> est le chiffre d'affaires total, en dollars, réalisé par les destinataires de la campagne au cours de la <a href='/docs/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events'>fenêtre de conversion primaire</a> définie.
{% endif %}

{% if include.metric == "Messages Sent" %}
<i>Messages envoyés</i> est le nombre total de messages envoyés dans une campagne. Après avoir lancé une campagne planifiée, cette mesure inclura tous les messages envoyés, même s'ils n'ont pas encore été envoyés en raison de la limite de débit. Cela ne signifie pas que le message a été reçu ou remis à un appareil, mais seulement qu'il a été envoyé.
{% endif %}

{% if include.metric == "Sent" %}
<i>Envoyé</i>, c'est à chaque fois qu'une campagne ou une étape du canvas a été lancée ou déclenchée, et qu'un SMS ou un RCS a été envoyé depuis Braze. Il est possible que le SMS ou le RCS n'ait pas atteint l'appareil de l'utilisateur en raison d'erreurs.
{% endif %}

{% if include.metric == "Sends" %}
<i>Envois</i> est le nombre total de messages envoyés dans une campagne. Après avoir lancé une campagne planifiée, cette mesure inclura tous les messages envoyés, même s'ils n'ont pas encore été envoyés en raison de la limite de débit. Cela ne signifie pas que le message a été reçu ou remis à un appareil, mais seulement qu'il a été envoyé.
{% endif %}

{% if include.metric == "Sends to Carrier" %}
L'<i>envoi au transporteur</i> est obsolète, mais continuera d'être pris en charge par les utilisateurs qui en disposent déjà. Il s'agit de la somme des <i>livraisons/distributions confirmées</i>, des <i>rejets</i> et des <i>envois</i> dont la livraison ou le rejet n'a pas été confirmé par le transporteur. Ceci inclut les instances dans lesquelles les opérateurs ne fournissent pas de confirmation de livraison ou de rejet, car certains opérateurs ne proposent pas ce service ou ne peuvent pas le faire au moment de l'envoi.
{% endif %}

{% if include.metric == "Sends to Carrier Rate" %}
Le <i>taux d'envoi au transporteur</i> est le pourcentage du total des messages envoyés qui ont été classés comme étant des <i>envois au transporteur</i>. Cela inclut les instances où les transporteurs ne fournissent pas de confirmation de réception/distribution, car certains transporteurs ne fournissent pas cette confirmation ou ne peuvent pas le faire au moment de l'envoi. Ces indicateurs sont obsolètes mais continueront d'être pris en charge par les utilisateurs qui en disposent déjà.
{% endif %}

{% if include.metric == "Spam" %}
Le <i>spam</i> est le nombre total d'e-mails livrés qui ont été marqués comme "spam" par le destinataire. Bien que Braze ne modifie pas l'état de l'abonnement de ces utilisateurs, ceux-ci seront automatiquement exclus des futurs e-mails, à moins que vous n'envoyiez un e-mail transactionnel, qui est configuré pour "envoyer à tous les utilisateurs, y compris ceux qui se désabonnent".
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
Le terme <i>Rejets Page de sondage</i> désigne le nombre total de clics sur le bouton de fermeture (x) de la page de sondage d'une <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>enquête simple</a>.
{% endif %}

{% if include.metric == "Survey Submissions" %}
Le nombre de <i>soumissions à l'enquête</i> est le nombre total de clics sur le bouton de soumission d'une <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>enquête simple</a>.
{% endif %}

{% if include.metric == "Total Clicks" %}
Le <i>nombre total de clics</i> est le nombre de destinataires uniques qui ont cliqué sur un lien dans le message envoyé.
{% endif %}

{% if include.metric == "Total Dismissals" %}
Le terme <i>Total des rejets</i> désigne le nombre de fois où les cartes de contenu d'une campagne ont été rejetées.
{% endif %}

{% if include.metric == "Total Impressions" %}
Le <i>nombre total d'impressions</i> est le nombre de fois qu'un message est vu. Braze n'enregistre une impression que lorsque le message devient visible pour l'utilisateur sur son écran. Par exemple, si un message est placé au bas d'une page, l'impression n'est pas enregistrée tant que l'utilisateur n'a pas fait défiler la page vers le bas et que le message n'est pas visible. Si un utilisateur voit le même message deux fois, cela comptera comme deux impressions.
{% endif %}

{% if include.metric == "Total Opens" %}
Le terme <i>Nombre total d'ouvertures</i> désigne le nombre total d'envois de messages qui ont été ouverts.
{% endif %}

{% if include.metric == "Total Revenue" %}
Le <i>chiffre d'affaires</i> total est le chiffre d'affaires total, en dollars, réalisé par les destinataires de la campagne au cours de la fenêtre de conversion primaire définie.
{% endif %}

{% if include.metric == "Unique Clicks" %}
Le nombre de <i>clics uniques</i> est le nombre distinct de destinataires qui ont cliqué au moins une fois sur un lien dans un message et est mesuré par <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id.</a>
{% endif %}

{% if include.metric == "Unique Dismissals" %}
<i>Fermetures uniques</i> est le nombre de destinataires uniques qui ont renvoyé une carte de contenu d'une campagne. Un utilisateur qui rejette plusieurs fois une carte de contenu d’une campagne constitue un rejet unique.
{% endif %}

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

{% if include.metric == "Unique Impressions" %}
Le nombre d'<i>impressions uniques</i> est le nombre total d'utilisateurs qui ont vu un message d'une campagne donnée. Une impression n'est enregistrée que lorsque le message devient visible sur l'écran d'un utilisateur.
{% endif %}

{% if include.metric == "Unique Recipients" %}
<i>Destinataires uniques</i> est le nombre de destinataires uniques quotidiens, c'est-à-dire les utilisateurs qui ont reçu un nouveau message au cours d'une journée. Pour que ce compte s'incrémente plus d'une fois pour un utilisateur, celui-ci doit recevoir un nouvel envoi de messages un autre jour.
{% endif %}

{% if include.metric == "Unique Opens" %}
L'<i>ouverture unique</i> est le nombre total de messages envoyés qui ont été ouverts au moins une fois par un utilisateur unique et qui sont suivis sur une période de sept jours.
{% endif %}

{% if include.metric == "Unsubscribers or Unsub" %}
<i>Désabonnés</i> ou <i>Unsub</i> est le nombre de messages ayant donné lieu à un désabonnement. Les désabonnements se produisent lorsqu’un utilisateur clique sur le lien de désinscription de Braze.
{% endif %}

{% if include.metric == "Unsubscribes" %}
<i>Désabonnés</i> est le nombre de destinataires dont l'état d'abonnement est passé à désabonné après avoir cliqué sur l'URL de désabonnement fournie par Braze.
{% endif %}

{% if include.metric == "Variation" %}
La <i>variation</i> est le nombre de variantes d'une campagne, différentes selon la définition du créateur.
{% endif %}
