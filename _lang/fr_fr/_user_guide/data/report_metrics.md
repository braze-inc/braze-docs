---
nav_title: Glossaire d’indicateurs de rapport
article_title: Glossaire d’indicateurs de rapport
layout: report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire définit les termes que vous trouverez dans vos rapports sur votre compte Braze."
tool: Reports
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Clics AMP

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

### Ouvertures AMP

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

### Audience

{% apitags %}
Tous
{% endapitags %}

{% multi_lang_include metrics.md metric='Audience' %}

<span class="calculation-line">Calcul : (Nombre de destinataires dans la variante) / (Destinataires uniques)</span>

{% endapi %}

{% api %}

### Rebonds

{% apitags %}
E-mail, Web Push, iOS Push
{% endapitags %}

{% multi_lang_include metrics.md metric='Bounces' %} Cela peut se produire parce qu'il n'y a pas de jeton de poussée valide, que l'utilisateur s'est désabonné après le lancement de la campagne, ou que l'adresse e-mail est inexacte ou désactivée.

|Canal|Informations supplémentaires|
|-------|-----------------------|
|E-mail|Pour les clients utilisant SendGrid, un échec d'e-mail se compose d'un échec définitif, de spam (`spam_report_drops`) et d'e-mails envoyés à des adresses non valides (`invalid_emails`).<br><br>Pour l'e-mail, le *taux de* *rebond* est le pourcentage de messages qui ont été envoyés sans succès ou désignés comme "renvoyés" ou "non reçus" par les services d'envoi utilisés ou qui n'ont pas été reçus par les utilisateurs visés par l'e-mail.|
|Notification push|Ces utilisateurs ont été automatiquement désabonnés de toutes les notifications push futures.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Rebonds</i> : Total</li>
        <li><i>Taux de rebond (Bounce %</i> ) ou <i>taux de rebond (Bounce Rate %)</i>: (Rebonds)/(Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Body Click

{% apitags %}
Push iOS, Push Android
{% endapitags %}

{% multi_lang_include metrics.md metric='Body Click' %}

<span class="calculation-line">Calcul : (Clics sur le corps du message) / (Impressions)</span>

{% endapi %}

{% api %}

### Clics sur le corps du message

{% apitags %}
in-app Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Body Clicks' %} Pour plus de détails, reportez-vous aux journaux des modifications du SDK pour [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) et [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

<span class="calculation-line">Calcul : (Clics sur le corps du message) / (Impressions)</span>

{% endapi %}

{% api %}

### Clics Boutons 1

{% apitags %}
in-app Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Button 1 Clicks'  %} L'envoi de messages pour les _clics sur le bouton 1_ ne fonctionne que si vous indiquez que **l' identifiant pour l'envoi de messages** est "0" dans le message in-app.

<span class="calculation-line">Calcul : (Clics du bouton 1) / (Impressions)</span>

{% endapi %}

{% api %}

### Clics Boutons 2

{% apitags %}
in-app Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Button 2 Clicks' %} L'envoi de messages pour _Button 2 Clicks_ ne fonctionne que si vous spécifiez l' **identificateur de** message in-app comme étant "1".

<span class="calculation-line">Calcul : (Clics du bouton 2) / (Impressions)</span>

{% endapi %}

{% api %}

### Analyse de campagne

{% apitags %}
Indicateurs de fonctionnalité
{% endapitags %}

La performance du message sur les différents canaux. Les indicateurs affichés dépendent du canal de communication sélectionné et du fait que l'[expérience Feature Flag]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/#campaign-analytics) est un test multivarié.

{% endapi %}

{% api %}

### Choix soumis

{% apitags %}
in-app Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

### Taux de Click-to-Open

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Calcul : (Clics uniques) / (Ouvertures uniques) (pour l'e-mail)</span>

{% endapi %}

{% api %}

### Livraisons confirmées par RCS ou livraisons confirmées par SMS

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmed Deliveries' %} En tant que client de Braze, les livraisons sont imputées sur votre quota de SMS. 

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Réceptions/distributions confirmées</i>: Total</li>
        <li><i>Taux de réception/distribution confirmé</i>: (Réceptions/distributions confirmées) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confiance

{% apitags %}
Cartes de contenu, Email, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, MMS.
{% endapitags %}

{% multi_lang_include metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Bouton de page de confirmation

{% apitags %}
in-app Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

### Rejets Page de Confirmation

{% apitags %}
in-app Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

### Conversions (B, C, D)

{% apitags %}
Cartes de contenu, e-mail, message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %} Cet événement défini est déterminé par vous lorsque vous créez la campagne. 

|Canal|Informations supplémentaires|
|-------|-----------------------|
|E-mail, Push, Webhooks|Les conversions sont suivies après l'envoi initial.|
|Cartes de contenu|Les conversions sont comptabilisées lorsque l'utilisateur consulte une carte de contenu pour la première fois.|
|in-app Messages|Une conversion est comptabilisée si l'utilisateur a reçu et visualisé la campagne de messages in-app, puis effectue l'événement de conversion spécifique dans la fenêtre de conversion définie, qu'il ait cliqué ou non sur le message.<br><br>Les conversions sont attribuées au dernier message reçu. Si la rééligibilité est activée, la conversion sera attribuée au dernier message in-app reçu, à condition qu'il intervienne dans la fenêtre de conversion définie. Toutefois, si une conversion a déjà été attribuée au message in-app, la nouvelle conversion ne peut pas être enregistrée pour ce message spécifique. Cela signifie que chaque réception/distribution de messages in-app est associée à une seule conversion.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### Conversions totales

{% apitags %}
in-app Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Conversions' %}

Lorsqu'un utilisateur ne consulte qu'une seule fois une campagne de messages in-app, une seule conversion est comptabilisée, même s'il effectue l'événement de conversion plusieurs fois par la suite. Toutefois, si la rééligibilité est activée et que l'utilisateur voit la campagne de messages in-app plusieurs fois, le *nombre total de conversions* peut augmenter une fois pour chaque fois que l'utilisateur enregistre une impression pour une nouvelle instance de la campagne de messages in-app. 

Par exemple, si un utilisateur déclenche un message in-app deux fois et se convertit après chaque impression de message in-app (ce qui donne lieu à deux conversions), le *nombre total de conversions* augmentera de deux. Toutefois, s'il n'y a eu qu'une seule impression de message in-app suivie de deux événements de conversion, une seule conversion sera enregistrée et le *nombre total de conversions* augmentera d'une unité.

{% endapi %}

{% api %}

### Fermer le message

{% apitags %}
in-app Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

### Taux de conversion

{% apitags %}
Cartes de contenu, e-mail, message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversion Rate' %}

|Canal|Informations supplémentaires|
|-------|-----------------------|
|in-app Messages|La métrique du nombre total d'<i>impressions uniques</i> quotidiennes est utilisée pour calculer le <i>taux de conversion</i> des messages in-app.<br><br>Les impressions pour les messages in-app ne peuvent être comptabilisées qu'une fois par jour. D'autre part, le nombre de fois qu'un utilisateur accomplit une action souhaitée (une "conversion") peut augmenter au cours d'une période de 24 heures. Si les conversions peuvent se produire plusieurs fois par jour, ce n'est pas le cas des impressions. Par conséquent, si un utilisateur effectue une conversion plusieurs fois dans la journée, le <i>taux de conversion</i> peut augmenter en conséquence, mais les impressions ne seront comptabilisées qu'une seule fois.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b>Messages in-app</b>: (Conversions primaires) / (Impressions uniques)</li>
        <li><b>Autres canaux</b>: (Conversions principales)/(Destinataires uniques)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Période de conversion

{% apitags %}
Tous
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

### Réceptions

{% apitags %}
E-mail, notification push Web, notification push iOS, notification push Android, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries' %}

|Canal|Informations supplémentaires|
|-------|-----------------------|
|E-mail|Il s'agit du nombre total d'envois de messages (Sends) envoyés et reçus avec succès par les parties concernées par l'e-mail.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Réceptions/distributions</i>: Total</li>
        <li><i>Réception/distribution %</i>: (Envoi - Bounces) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Défauts de réception/distribution de RCS ou de SMS

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Delivery Failures' %}

Contactez le <a href="/docs/braze_support/">service d'assistance de Braze</a> pour obtenir de l'aide afin de comprendre les raisons des échecs de réception/distribution.

<span class="calculation-line">Calcul : (Envoie) - (Envoie au transporteur)</span>

{% endapi %}

{% api %}

### Échecs de réception

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include metrics.md metric='Delivery Failures RCS' %}

Contactez le <a href="/docs/braze_support/">service d'assistance de Braze</a> pour obtenir de l'aide afin de comprendre les raisons des échecs de réception/distribution.

<span class="calculation-line">Calcul : (Envoie) - (Envoie au transporteur)</span>

{% endapi %}

{% api %}

### Taux de réceptions échouées

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Failed Delivery Rate' %}

Contactez le <a href="/docs/braze_support/">service d'assistance de Braze</a> pour obtenir de l'aide afin de comprendre les raisons des échecs de réception/distribution.

<span class="calculation-line">Calcul : (échecs de réception/distribution) / (envois)</span>

{% endapi %}

{% api %}

### Ouvertures directes

{% apitags %}
Notification push iOS
{% endapitags %}

{% multi_lang_include metrics.md metric='Direct Opens' %}

<span class="calculation-line">Calcul : (Ouvertures directes) / (Livraisons)</span>

{% endapi %}

{% api %}

### Emailable

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Emailable' %}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Erreurs

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include metrics.md metric='Errors' %} Les erreurs sont incluses dans le décompte des <i>envois</i> mais ne sont pas incluses dans le décompte des <i>destinataires uniques</i>.

{% endapi %}

{% api %}

### Estimation des ouvertures réelles

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

### Échecs

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Failures' %} Les échecs sont inclus dans le décompte des <i>envois</i> mais pas dans celui des <i>réception/distributions</i>.</td>

<span class="calculation-line">Calcul<i>(taux d'échec</i>) : (échecs) / (envois)</span>

{% endapi %}

{% api %}

### Fonctionnalité de l'expérience du drapeau

{% apitags %}
Indicateurs de fonctionnalité
{% endapitags %}

Indicateurs de performance pour l'expérience de l'envoi de messages dans une fonctionnalité. Les indicateurs spécifiques affichés varient en fonction du canal de communication et du fait que l'expérience était ou non un test multivarié.

{% endapi %}

{% api %}

### Échec d'envoi définitif

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Hard Bounce' %} 

Lorsque cela se produit, Braze marque l'adresse e-mail comme invalide mais ne met pas à jour le [statut d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) de l'utilisateur. Si un e-mail reçoit un échec d'envoi définitif, nous cesserons toute demande future à cette adresse e-mail.

{% endapi %}

{% api %}

### Aide

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include metrics.md metric='Help' %} Une réponse d'utilisateur est mesurée chaque fois qu'un utilisateur envoie un message entrant dans les quatre heures suivant la réception de votre message.

{% endapi %}

{% api %}

### Ouvertures influencées

{% apitags %}
Push iOS, Push Android
{% endapitags %}

{% multi_lang_include metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Calcul : (Ouvertures influencées) / (Livraisons)</span>

{% endapi %}

{% api %}

### Revenus à vie

{% apitags %}
Cartes de contenu, e-mail, message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### Valeur vie client par utilisateur

{% apitags %}
Cartes de contenu, e-mail, message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### Chiffre d'affaires quotidien moyen

{% apitags %}
Cartes de contenu, e-mail, message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### Achats quotidiens

{% apitags %}
Cartes de contenu, e-mail, message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### Revenus quotidiens par utilisateur

{% apitags %}
Cartes de contenu, e-mail, message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### Ouverture automatique

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Machine Opens' %} Cette métrique est suivie à partir du 11 novembre 2021 pour SendGrid et du 2 décembre 2021 pour SparkPost. Pour Amazon SES, l'analyse/analytique s'affichera sous forme d'_adjectifs_. Toutefois, le filtrage des clics par les robots sera pris en charge.

{% endapi %}

{% api %}

### Ouvertures

{% apitags %}
Web Push, iOS Push, Android Push
{% endapitags %}

{% multi_lang_include metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### Désabonnement

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include metrics.md metric='Opt-Out' %} Une réponse de l'utilisateur est mesurée chaque fois qu'un utilisateur envoie un message entrant dans les quatre heures suivant la réception de votre message.

{% endapi %}

{% api %}

### Autre ouverture

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Other Opens' %} Notez qu'un utilisateur peut également ouvrir un e-mail (comme les comptes d'ouverture vers Other Opens) avant qu'un compte de Machine Opens ne soit enregistré. Si un utilisateur ouvre un e-mail une fois (ou plus) après un événement d'ouverture automatique à partir d'une boîte de réception autre qu'Apple Mail, le nombre de fois où l'utilisateur ouvre l'e-mail est calculé pour les autres ouvertures et une seule fois pour les ouvertures uniques.

{% endapi %}

{% api %}

### En attente d’une nouvelle tentative

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

### Conversions principales (A) ou événement de conversion principal

{% apitags %}
Cartes de contenu, Email, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, MMS.
{% endapitags %}

{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 

|Canal|Informations supplémentaires|
|-------------|----------------------|
|E-mail, Push, Webhooks|Après l'envoi initial.|
|Cartes de contenu, messages in-app|Lorsque l'utilisateur visualise la carte de contenu ou le message pour la première fois.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Conversions principales (A) ou événement de conversion principal</i>: Total</li>
        <li><i>Conversions primaires (A) %</i> ou <i>taux d'événement de conversion principal</i>: (Conversions principales)/(Destinataires uniques)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Lectures

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Reads' %}

{% endapi %}

{% api %}

### Taux de lecture

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Read Rate' %}

<span class="calculation-line">Calcul : (lectures avec accusés de réception) / (envois)</span>

{% endapi %}

{% api %}

### Reçu

{% apitags %}
E-mail, cartes de contenu, message in-app, Web Push, iOS Push, Android Push, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Received' %} 

|Canal|Informations supplémentaires|
|-------|-------|
|Cartes de contenu|Reçu lorsque les utilisateurs visualisent la carte dans l'application.|
|Notification push|Reçu lors de l'envoi de messages du serveur Braze vers le fournisseur de push.|
|E-mail|Reçu lorsque les messages sont envoyés du serveur Braze au fournisseur de services e-mailing.|
|SMS/MMS|"Livré" après que le fournisseur de SMS a reçu la confirmation de l'opérateur en amont et de l'appareil de destination.|
|Message in-app|Reçu au moment de l'affichage en fonction de l'action de déclenchement définie.|
|WhatsApp|Reçu au moment de l'affichage en fonction de l'action de déclenchement définie.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### Rejets RCS ou rejets SMS

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include metrics.md metric='Rejections' %} En tant que client de Braze, les rejets sont imputés sur votre quota de SMS.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Rejets</i>: Total</li>
        <li><i>Taux de rejet</i>: (Rejets) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Revenue

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

### Envoyé

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Sent' %}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Envois

{% apitags %}
Cartes de contenu, Email, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends' %} Cette métrique est fournie par Braze. Notez qu’au lancement d’une campagne planifiée, cet indicateur inclura tous les messages envoyés, qu’ils aient été envoyés ou non en raison d’une limitation du taux.

{% alert tip %}
Pour les cartes de contenu, cette mesure est calculée différemment en fonction de ce que vous avez sélectionné pour la [création de la carte :]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)

- **Au moment du lancement ou de l'entrée d’étape :** Le nombre de cartes créées et disponibles pour être vues. Le fait que les utilisateurs aient consulté ou non la carte n’est pas comptabilisé.
- **À première vue :** Le nombre de cartes affichées aux utilisateurs.
{% endalert %}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Messages envoyés

{% apitags %}
Cartes de contenu, Email, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Messages Sent' %} Cette métrique est fournie par Braze. Notez qu’au lancement d’une campagne planifiée, cet indicateur inclura tous les messages envoyés, qu’ils aient été envoyés ou non en raison d’une limitation du taux.

{% alert tip %}
Pour les cartes de contenu, cette mesure est calculée différemment en fonction de ce que vous avez sélectionné pour la [création de la carte :]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)

- **Au moment du lancement ou de l'entrée d’étape :** Le nombre de cartes créées et disponibles pour être vues. Le fait que les utilisateurs aient consulté ou non la carte n’est pas comptabilisé.
- **À première vue :** Le nombre de cartes affichées aux utilisateurs.
{% endalert %}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Envois à l’opérateur

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends to Carrier' %} 

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Envoi au transporteur</i>: Total</li>
        <li><i>Envoie à Carrier Rate :</i> (Envoie au transporteur) / (Envoie)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Échec provisoire de livraison

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Soft Bounce' %} Si un e-mail reçoit un échec provisoire d'envoi, nous effectuons généralement une nouvelle tentative dans les 72 heures, mais le nombre de tentatives varie d'un destinataire à l'autre.

Bien que les échecs provisoires ne soient pas pris en compte dans l'analyse/analytique de votre campagne, vous pouvez surveiller les échecs provisoires dans le [journal d'activité du message.]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) Vous pouvez également exclure ces utilisateurs de vos envois ou examiner le nombre d'échecs provisoires d'envois des 30 derniers jours à l'aide du [filtre du segment des échecs provisoires d']({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced)envois. Dans le journal d'activité des messages, vous pouvez également voir la raison des échecs provisoires et comprendre les écarts éventuels entre les "envois" et les "réception/distributions" de vos campagnes de communication par e-mail.

{% endapi %}

{% api %}

### Spam

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Spam' %}

{% alert note %}
Les plaintes pour spam sont traitées directement par les fournisseurs de services d'e-mailing, puis transmises à Braze par le biais d'une boucle de rétroaction. La plupart des boucles de rétroaction ne signalent qu'une partie des plaintes réelles, de sorte que la mesure du _courrier indésirable_ ne représente souvent qu'une fraction du total réel. Seuls les fournisseurs de services e-mailing peuvent connaître le volume réel des plaintes pour spam, ce qui signifie que _le spam_ doit être considéré comme une mesure indicative et non exhaustive.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Spam</i>: Total</li>
        <li><i>Spam %</i> ou <i>Spam Rate % :</i> (Marqué comme spam) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Rejets Page de Sondage

{% apitags %}
in-app Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

### Soumissions de sondage

{% apitags %}
in-app Message
{% endapitags %}

{% multi_lang_include metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

### Nombre total de clics

{% apitags %}
E-mail, cartes de contenu, SMS/MMS, MMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Clicks' %}

|Canal|Informations supplémentaires|
|-------|-------|
|LINE|Suivi après qu'un seuil minimum de 20 messages par jour a été atteint. Les e-mails AMP comprennent les clics enregistrés à la fois dans les versions HTML et en texte clair. Ce chiffre peut être artificiellement gonflé par des outils anti-spam.|
|Bannières|Le nombre total (et le pourcentage) d'utilisateurs qui ont cliqué dans le message diffusé, indépendamment du fait que le même utilisateur clique plusieurs fois.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b>E-mail :</b> (nombre total de clics) / (réception/distribution)</li>
        <li><b>Cartes de contenu (Content cards) :</b> (Nombre total de clics) / (Nombre total d'impressions)</li>
        <li><b>SMS :</b> (Ouvertures par clic) / (Livraisons)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total des rejets

{% apitags %}
Cartes de contenu
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Dismissals' %} Si un utilisateur reçoit deux cartes différentes de la même campagne et les rejette toutes les deux, ce nombre sera multiplié par deux. La réadmissibilité vous permet d'incrémenter le _nombre total de renvois_ une fois chaque fois qu'un utilisateur reçoit une carte ; chaque carte est un message différent.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Total des licenciements :</i> Total</li>
        <li><i>Taux de licenciement total :</i> Total des rejets / Total des impressions</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Impressions totales

{% apitags %}
Message in-app, cartes de contenu
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Impressions' %} Ce nombre est une somme du nombre d'événements d'impression que Braze reçoit des SDK.

|Canal|Informations supplémentaires|
|-------|-----------------------|
|Cartes de contenu|Nombre total d’impressions enregistrées pour une carte de contenu donnée. Ce nombre peut être incrémenté plusieurs fois pour le même utilisateur.|
|in-app Messages|S'il y a plusieurs appareils et que la rééligibilité est désactivée, l'utilisateur ne devrait voir le message in-app qu'une seule fois. Même si l'utilisateur utilise plusieurs appareils, il ne la verra que sur le premier appareil ciblé. Cela suppose que le profil a consolidé les appareils et qu'un utilisateur dispose d'un ID unique auquel il est connecté sur tous les appareils. Si la rééligibilité est activée, une impression est enregistrée chaque fois que l'utilisateur voit le message in-app.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Nombre total d’ouvertures

{% apitags %}
E-mail, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Opens' %}

|Canal|Informations supplémentaires|
|-------|-----------------------|
|LINE|Suivi après qu'un seuil minimum de 20 messages par jour a été atteint.|
|Les e-mails AMP|Le total des ouvertures pour les versions HTML et en texte clair.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b>Email <i>Nombre total d'ouvertures</i>:</b> Total</li>
        <li><b><i>Taux d'ouverture total des</i> e-mails :</b> (Ouvertures) / (Livraisons)</li>
        <li><b>Web push <i>Nombre total d'ouvertures</i>:</b> Nombre d'<i>ouvertures directes</i> </li>
        <li><b>Web push <i>Taux d'ouverture total :</i></b> (Ouvertures totales) / (Réceptions/distributions)</li>
        <li><b>iOS, Android et Kindle push <i>Nombre total d'ouvertures</i>:</b> (Ouvertures directes) + (Ouvertures influencées)</li>
        <li><b>iOS, Android et Kindle push <i>Taux d'ouverture total :</i></b> (Ouvertures totales) / (Réceptions/distributions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total des revenus

{% apitags %}
Cartes de contenu, Email, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, MMS.
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Revenue' %} Ce chiffre n'est disponible que dans les rapports de comparaison de campagnes via le <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>générateur de rapports.</a>

{% endapi %}

{% api %}

### Clics uniques

{% apitags %}
E-mail, cartes de contenu, LINE
{% endapitags %}

{% multi_lang_include metrics.md indicateurs='Clics uniques' %}

Cela inclut les clics sur les liens de désinscription fournis par Braze.

|Canal|Informations supplémentaires|
|-------|-----------------------|
|E-mail|Suivi sur une période de sept jours.|
|LINE|Suivi après qu'un seuil minimum de 20 messages par jour a été atteint.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Clics uniques</i>: Total</li>
        <li><b>Carte de contenu</b> <i>% de clics uniques</i> ou <i>taux de clics uniques</i>: (Clics uniques) / (Impressions uniques)</li>
        <li><i>Pourcentage de clics uniques par</i> <b>e-mail</b> ou <i>taux de clics uniques</i>: (Clics uniques) / (Réceptions/distributions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Rejets uniques

{% apitags %}
Cartes de contenu
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">Calcul : (Rejets uniques) / (Impressions uniques)</span>

{% endapi %}

{% api %}

### Impressions uniques

{% apitags %}
Message in-app, cartes de contenu
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Impressions' %} 

|Canal|Informations supplémentaires|
|-------|-----------------------|
|in-app Messages|Les impressions uniques peuvent être à nouveau incrémentées après 24 heures si la rééligibilité est activée et qu'un utilisateur effectue l'action déclencheur. Si la rééligibilité est activée, <i>Impressions uniques</i> = <i>Destinataires uniques</i>.|
|Cartes de contenu|Le décompte ne doit pas être incrémenté la deuxième fois qu'un utilisateur consulte une carte.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Ouvertures uniques

{% apitags %}
E-mail, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Ouvertures uniques' %}

|Canal|Informations supplémentaires|
|-------|-----------------------|
|E-mail|Suivi sur une période de 7 jours.|
|LINE|Suivi après qu'un seuil minimum de 20 messages par jour a été atteint.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Ouverture unique</i>: Total</li>
        <li><i>Pourcentage d'ouvertures uniques</i> ou <i>taux d'ouvertures uniques</i>: (Ouvertures uniques) / (Livraisons)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Destinataires uniques

{% apitags %}
Tous
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Recipients' %}

Étant donné qu'un spectateur peut être un destinataire unique chaque jour, vous devriez vous attendre à ce que ce chiffre soit plus élevé que celui des <i>impressions uniques.</i> Pour les cartes de contenu, chaque carte de contenu ne peut être reçue qu'une seule fois, de sorte que la consultation de la même carte de contenu une deuxième fois, quel que soit le jour, n'augmentera pas ce décompte.<br><br>Ce numéro est reçu de Braze et est basé sur le site `user_id`. Les destinataires uniques sont comptabilisés au niveau de la campagne ou de l'étape du canvas, et non au niveau de l'<a href='https://braze.com/docs/api/identifier_types/#send-identifier'>identifiant d'envoi.</a>

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Désabonnés

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Désabonnés</i> ou <i>désabonnés</i>: Total</li>
        <li><i>Pourcentage de désabonnements</i> ou <i>taux de désabonnement</i>: (Désinscriptions)/(Livraisons)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Se désabonne

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Unsubscribes' %}

<span class="calculation-line">Calcul : (Désabonnements) / (Livraisons)</span>

{% endapi %}

{% api %}

### Variation

{% apitags %}
Cartes de contenu, Email, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, MMS.
{% endapitags %}

{% multi_lang_include metrics.md metric='Variation' %}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}