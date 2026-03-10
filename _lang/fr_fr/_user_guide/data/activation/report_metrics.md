---
nav_title: Glossaire d'indicateurs de rapport
article_title: Glossaire d'indicateurs de rapport
layout: report_metrics
page_order: 0.5
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

{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

### Ouvertures AMP

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

### Audience

{% apitags %}
Tous
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Calcul : (Nombre de destinataires dans la variante) / (Destinataires uniques)</span>

{% endapi %}

{% api %}

### Rebonds

{% apitags %}
E-mail, Web Push, iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} Cela peut se produire parce qu'il n'y a pas de jeton de notification push valide, que l'utilisateur s'est désabonné après le lancement de la campagne, ou que l'adresse e-mail est inexacte ou désactivée.

|Canal|Informations supplémentaires|
|-------|-----------------------|
|E-mail|Pour les clients utilisant Sendgrid, un rebond d'e-mail se compose d'échecs d'envoi définitifs, de spam (`spam_report_drops`) et d'e-mails envoyés à des adresses non valides (`invalid_emails`).<br><br>Pour l'e-mail, le *taux de rebond* est le pourcentage de messages qui ont été envoyés sans succès ou désignés comme « renvoyés » ou « non reçus » par les services d'envoi utilisés ou qui n'ont pas été reçus par les utilisateurs visés par l'e-mail.|
|Notification push|Ces utilisateurs ont été automatiquement désabonnés de toutes les notifications push futures.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Rebonds</i> : Total</li>
        <li><i>Taux de rebond (Bounce %)</i> ou <i>taux de rebond (Bounce Rate %)</i> : (Rebonds) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Body Click

{% apitags %}
Push iOS, Push Android
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Click' %}

<span class="calculation-line">Calcul : (Clics sur le corps du message) / (Impressions)</span>

{% endapi %}

{% api %}

### Clics sur le corps du message

{% apitags %}
Message in-app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %} Pour plus de détails, reportez-vous aux journaux des modifications du SDK pour [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) et [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

<span class="calculation-line">Calcul : (Clics sur le corps du message) / (Impressions)</span>

{% endapi %}

{% api %}

### Clics Bouton 1

{% apitags %}
Message in-app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} L'envoi de rapports pour les _clics sur le bouton 1_ ne fonctionne que si vous indiquez que l'**identifiant pour l'envoi de rapports** est « 0 » dans le message in-app.

<span class="calculation-line">Calcul : (Clics du bouton 1) / (Impressions)</span>

{% endapi %}

{% api %}

### Clics Bouton 2

{% apitags %}
Message in-app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} L'envoi de rapports pour les _clics sur le bouton 2_ ne fonctionne que si vous indiquez que l'**identifiant pour l'envoi de rapports** est « 1 » dans le message in-app.

<span class="calculation-line">Calcul : (Clics du bouton 2) / (Impressions)</span>

{% endapi %}

{% api %}

### Analyse de campagne

{% apitags %}
Indicateurs de fonctionnalité
{% endapitags %}

La performance du message sur les différents canaux. Les indicateurs affichés dépendent du canal de communication sélectionné et du fait que l'[expérience d'indicateur de fonctionnalité]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/#campaign-analytics) est un test multivarié.

{% endapi %}

{% api %}

### Choix soumis

{% apitags %}
Message in-app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

### Taux de clic par ouverture

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Calcul : (Clics uniques) / (Ouvertures uniques) (pour l'e-mail)</span>

{% endapi %}

{% api %}

### Réceptions confirmées RCS ou réceptions confirmées SMS

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} En tant que client de Braze, les réceptions sont imputées sur votre allocation SMS. 

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Réceptions confirmées</i> : Total</li>
        <li><i>Taux de réception confirmée</i> : (Réceptions confirmées) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confiance

{% apitags %}
Cartes de contenu, E-mail, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Bouton de page de confirmation

{% apitags %}
Message in-app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

### Rejets de la page de confirmation

{% apitags %}
Message in-app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

### Conversions (B, C, D)

{% apitags %}
Cartes de contenu, E-mail, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} Cet événement défini est déterminé par vous lorsque vous créez la campagne. 

|Canal|Informations supplémentaires|
|-------|-----------------------|
|E-mail, Push, Webhooks|Les conversions sont suivies après l'envoi initial.|
|Cartes de contenu|Les conversions sont comptabilisées lorsque l'utilisateur consulte une carte de contenu pour la première fois.|
|Messages in-app|Une conversion est comptabilisée si l'utilisateur a reçu et visualisé la campagne de messages in-app, puis effectue l'événement de conversion spécifique dans la fenêtre de conversion définie, qu'il ait cliqué ou non sur le message.<br><br>Les conversions sont attribuées au dernier message reçu. Si la rééligibilité est activée, la conversion sera attribuée au dernier message in-app reçu, à condition qu'elle intervienne dans la fenêtre de conversion définie. Toutefois, si une conversion a déjà été attribuée au message in-app, la nouvelle conversion ne peut pas être enregistrée pour ce message spécifique. Cela signifie que chaque distribution de message in-app est associée à une seule conversion.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### Conversions totales

{% apitags %}
Message in-app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

Lorsqu'un utilisateur ne consulte qu'une seule fois une campagne de messages in-app, une seule conversion est comptabilisée, même s'il effectue l'événement de conversion plusieurs fois par la suite. Toutefois, si la rééligibilité est activée et que l'utilisateur voit la campagne de messages in-app plusieurs fois, le *nombre total de conversions* peut augmenter une fois pour chaque fois que l'utilisateur enregistre une impression pour une nouvelle instance de la campagne de messages in-app. 

Par exemple, si un utilisateur déclenche un message in-app deux fois et convertit après chaque impression de message in-app (ce qui donne lieu à deux conversions), le *nombre total de conversions* augmentera de deux. Toutefois, s'il n'y a eu qu'une seule impression de message in-app suivie de deux événements de conversion, une seule conversion sera enregistrée et le *nombre total de conversions* augmentera d'une unité.

{% endapi %}

{% api %}

### Fermer le message

{% apitags %}
Message in-app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

### Taux de conversion

{% apitags %}
Cartes de contenu, E-mail, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

|Canal|Informations supplémentaires|
|-------|-----------------------|
|Messages in-app|L'indicateur du nombre total d'<i>impressions uniques</i> quotidiennes est utilisé pour calculer le <i>taux de conversion</i> des messages in-app.<br><br>Les impressions pour les messages in-app ne peuvent être comptabilisées qu'une fois par jour. D'autre part, le nombre de fois qu'un utilisateur accomplit une action souhaitée (une « conversion ») peut augmenter au cours d'une période de 24 heures. Si les conversions peuvent se produire plusieurs fois par jour, ce n'est pas le cas des impressions. Par conséquent, si un utilisateur effectue une conversion plusieurs fois dans la journée, le <i>taux de conversion</i> peut augmenter en conséquence, mais les impressions ne seront comptabilisées qu'une seule fois.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b>Messages in-app</b> : (Conversions principales) / (Impressions uniques)</li>
        <li><b>Autres canaux</b> : (Conversions principales) / (Destinataires uniques)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Fenêtre de conversion

{% apitags %}
Tous
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

### Réceptions

{% apitags %}
E-mail, Web Push, iOS Push, Android Push, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %}

|Canal|Informations supplémentaires|
|-------|-----------------------|
|E-mail|Il s'agit du nombre total de messages (Envois) envoyés et reçus avec succès par les destinataires pouvant recevoir des e-mails.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Réceptions</i> : Total</li>
        <li><i>Réceptions %</i> : (Envois - Rebonds) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Échecs de réception RCS ou SMS

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

Contactez l'<a href="/docs/braze_support/">assistance Braze</a> pour vous aider à comprendre les raisons des échecs de réception.

<span class="calculation-line">Calcul : (Envois) - (Envois à l'opérateur)</span>

{% endapi %}

{% api %}

### Échecs de réception

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

Contactez l'<a href="/docs/braze_support/">assistance Braze</a> pour vous aider à comprendre les raisons des échecs de réception.

<span class="calculation-line">Calcul : (Envois) - (Envois à l'opérateur)</span>

{% endapi %}

{% api %}

### Taux d'échec de réception

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

Contactez l'<a href="/docs/braze_support/">assistance Braze</a> pour vous aider à comprendre les raisons des échecs de réception.

<span class="calculation-line">Calcul : (Échecs de réception) / (Envois)</span>

{% endapi %}

{% api %}

### Ouvertures directes

{% apitags %}
iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">Calcul : (Ouvertures directes) / (Réceptions)</span>

{% endapi %}

{% api %}

### Emailable

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Erreurs

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Errors' %} Les erreurs sont incluses dans le décompte des <i>envois</i> mais ne sont pas incluses dans le décompte des <i>destinataires uniques</i>.

{% endapi %}

{% api %}

### Estimation des ouvertures réelles

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

### Échecs

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failures' %} Les échecs sont inclus dans le décompte des <i>envois</i> mais pas dans celui des <i>réceptions</i>.</td>

<span class="calculation-line">Calcul (<i>taux d'échec</i>) : (Échecs) / (Envois)</span>

{% endapi %}

{% api %}

### Performance de l'expérience d'indicateur de fonctionnalité

{% apitags %}
Indicateurs de fonctionnalité
{% endapitags %}

Indicateurs de performance pour le message dans une expérience d'indicateur de fonctionnalité. Les indicateurs spécifiques affichés varient en fonction du canal de communication et du fait que l'expérience était ou non un test multivarié.

{% endapi %}

{% api %}

### Échec d'envoi définitif

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

Lorsque cela se produit, Braze marque l'adresse e-mail comme invalide mais ne met pas à jour le [statut d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) de l'utilisateur. Si un e-mail reçoit un échec d'envoi définitif, nous cesserons toute demande future à cette adresse e-mail.

{% endapi %}

{% api %}

### Aide

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} Une réponse d'utilisateur est mesurée chaque fois qu'un utilisateur envoie un message entrant dans les quatre heures suivant la réception de votre message.

{% endapi %}

{% api %}

### Ouvertures influencées

{% apitags %}
Push iOS, Push Android
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Calcul : (Ouvertures influencées) / (Réceptions)</span>

{% endapi %}

{% api %}

### Revenus à vie

{% apitags %}
Cartes de contenu, E-mail, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### Valeur vie client par utilisateur

{% apitags %}
Cartes de contenu, E-mail, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### Chiffre d'affaires quotidien moyen

{% apitags %}
Cartes de contenu, E-mail, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### Achats quotidiens

{% apitags %}
Cartes de contenu, E-mail, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### Revenus quotidiens par utilisateur

{% apitags %}
Cartes de contenu, E-mail, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### Ouvertures automatiques

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Cet indicateur est suivi à partir du 11 novembre 2021 pour Sendgrid et du 2 décembre 2021 pour SparkPost. Pour Amazon SES, l'analytique s'affichera sous forme d'_ouvertures_. Toutefois, le filtrage des clics par les robots sera pris en charge.

{% endapi %}

{% api %}

### Ouvertures

{% apitags %}
Web Push, iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### Désabonnement

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} Une réponse d'utilisateur est mesurée chaque fois qu'un utilisateur envoie un message entrant dans les quatre heures suivant la réception de votre message.

{% endapi %}

{% api %}

### Autres ouvertures

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Notez qu'un utilisateur peut également ouvrir un e-mail (comptabilisé dans les Autres ouvertures) avant qu'une ouverture automatique ne soit enregistrée. Si un utilisateur ouvre un e-mail une fois (ou plus) après un événement d'ouverture automatique à partir d'une boîte de réception autre qu'Apple Mail, le nombre de fois où l'utilisateur ouvre l'e-mail est comptabilisé dans les Autres ouvertures et une seule fois dans les Ouvertures uniques.

{% endapi %}

{% api %}

### En attente de nouvelle tentative

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

### Conversions principales (A) ou événement de conversion principal

{% apitags %}
Cartes de contenu, E-mail, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 

|Canal|Informations supplémentaires|
|-------------|----------------------|
|E-mail, Push, Webhooks|Après l'envoi initial.|
|Cartes de contenu, Messages in-app|Lorsque l'utilisateur visualise la carte de contenu ou le message pour la première fois.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Conversions principales (A) ou événement de conversion principal</i> : Total</li>
        <li><i>Conversions principales (A) %</i> ou <i>taux d'événement de conversion principal</i> : (Conversions principales) / (Destinataires uniques)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Lectures

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Reads' %}

{% endapi %}

{% api %}

### Taux de lecture

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Read Rate' %}

<span class="calculation-line">Calcul : (Lectures avec accusés de réception) / (Envois)</span>

{% endapi %}

{% api %}

### Reçu

{% apitags %}
E-mail, Cartes de contenu, Message in-app, Web Push, iOS Push, Android Push, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %} 

|Canal|Informations supplémentaires|
|-------|-------|
|Cartes de contenu|Reçu lorsque les utilisateurs visualisent la carte dans l'application.|
|Notification push|Reçu lors de l'envoi de messages du serveur Braze vers le fournisseur de push.|
|E-mail|Reçu lorsque les messages sont envoyés du serveur Braze au fournisseur de services d'e-mailing.|
|SMS/MMS|« Livré » après que le fournisseur de SMS a reçu la confirmation de l'opérateur en amont et de l'appareil de destination.|
|Message in-app|Reçu au moment de l'affichage en fonction de l'action de déclenchement définie.|
|WhatsApp|Reçu au moment de l'affichage en fonction de l'action de déclenchement définie.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### Rejets RCS ou rejets SMS

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Rejections' %} En tant que client de Braze, les rejets sont imputés sur votre allocation SMS.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Rejets</i> : Total</li>
        <li><i>Taux de rejet</i> : (Rejets) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Chiffre d'affaires

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

### Envoyé

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Envois

{% apitags %}
Cartes de contenu, E-mail, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} Cet indicateur est fourni par Braze. Notez qu'au lancement d'une campagne planifiée, cet indicateur inclura tous les messages envoyés, qu'ils aient été effectivement envoyés ou non en raison d'une limite de débit.

{% alert tip %}
Pour les cartes de contenu, cet indicateur est calculé différemment en fonction de ce que vous avez sélectionné pour la [création de la carte]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) :

- **Au moment du lancement ou de l'entrée dans l'étape :** Le nombre de cartes créées et disponibles pour être vues. Le fait que les utilisateurs aient consulté ou non la carte n'est pas comptabilisé.
- **À la première impression :** Le nombre de cartes affichées aux utilisateurs.
{% endalert %}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Messages envoyés

{% apitags %}
Cartes de contenu, E-mail, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Cet indicateur est fourni par Braze. Notez qu'au lancement d'une campagne planifiée, cet indicateur inclura tous les messages envoyés, qu'ils aient été effectivement envoyés ou non en raison d'une limite de débit.

{% alert tip %}
Pour les cartes de contenu, cet indicateur est calculé différemment en fonction de ce que vous avez sélectionné pour la [création de la carte]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) :

- **Au moment du lancement ou de l'entrée dans l'étape :** Le nombre de cartes créées et disponibles pour être vues. Le fait que les utilisateurs aient consulté ou non la carte n'est pas comptabilisé.
- **À la première impression :** Le nombre de cartes affichées aux utilisateurs.
{% endalert %}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Envois à l'opérateur

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} 

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Envois à l'opérateur</i> : Total</li>
        <li><i>Taux d'envoi à l'opérateur</i> : (Envois à l'opérateur) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Échec provisoire d'envoi

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Notez que les _échecs provisoires d'envoi_ diffèrent des _reports_. Si aucun e-mail n'a été livré avec succès pendant cette période de nouvelle tentative, Braze enverra un événement d'échec provisoire d'envoi par tentative de campagne envoyée. Avant le 25 février 2025, ces nouvelles tentatives étaient comptabilisées comme plusieurs échecs provisoires d'envoi pour une même campagne.

Bien que les échecs provisoires d'envoi ne soient pas pris en compte dans l'analytique de votre campagne, vous pouvez les surveiller dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/). Vous pouvez également exclure ces utilisateurs de vos envois ou examiner le nombre d'échecs provisoires d'envoi des 30 derniers jours à l'aide du [filtre de segment des échecs provisoires d'envoi]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced). Dans le journal d'activité des messages, vous pouvez également voir la raison des échecs provisoires d'envoi et comprendre les écarts éventuels entre les « envois » et les « réceptions » de vos campagnes e-mail.

{% endapi %}

{% api %}

### Spam

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
Les plaintes pour spam sont traitées directement par les fournisseurs de services d'e-mailing, puis transmises à Braze par le biais d'une boucle de rétroaction. La plupart des boucles de rétroaction ne signalent qu'une partie des plaintes réelles, de sorte que l'indicateur _Spam_ ne représente souvent qu'une fraction du total réel. Seuls les fournisseurs de services d'e-mailing peuvent connaître le volume réel des plaintes pour spam, ce qui signifie que _Spam_ doit être considéré comme un indicateur indicatif et non exhaustif.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Spam</i> : Total</li>
        <li><i>Spam %</i> ou <i>Spam Rate %</i> : (Marqué comme spam) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Rejets de la page de sondage

{% apitags %}
Message in-app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

### Soumissions de sondage

{% apitags %}
Message in-app
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

### Nombre total de clics

{% apitags %}
E-mail, Cartes de contenu, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}

|Canal|Informations supplémentaires|
|-------|-------|
|LINE|Suivi après qu'un seuil minimum de 20 messages par jour a été atteint. Les e-mails AMP comprennent les clics enregistrés à la fois dans les versions HTML et en texte brut. Ce chiffre peut être artificiellement gonflé par des outils anti-spam.|
|Bannières|Le nombre total (et le pourcentage) d'utilisateurs qui ont cliqué dans le message distribué, indépendamment du fait que le même utilisateur clique plusieurs fois.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b>E-mail :</b> (Nombre total de clics) / (Réceptions)</li>
        <li><b>Cartes de contenu :</b> (Nombre total de clics) / (Nombre total d'impressions)</li>
        <li><b>SMS :</b> (Ouvertures par clic) / (Réceptions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total des rejets

{% apitags %}
Cartes de contenu
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} Si un utilisateur reçoit deux cartes différentes de la même campagne et qu'il les ferme toutes les deux, ce nombre sera incrémenté de deux. La rééligibilité vous permet d'incrémenter le _total des rejets_ une fois chaque fois qu'un utilisateur reçoit une carte ; chaque carte est un message différent.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Total des rejets :</i> Total</li>
        <li><i>Taux de rejet total :</i> Total des rejets / Total des impressions</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Impressions totales

{% apitags %}
Message in-app, Cartes de contenu
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Ce nombre correspond à la somme des événements d'impression que Braze reçoit des SDK.

|Canal|Informations supplémentaires|
|-------|-----------------------|
|Cartes de contenu|Nombre total d'impressions enregistrées pour une carte de contenu donnée. Ce nombre peut être incrémenté plusieurs fois pour le même utilisateur.|
|Messages in-app|S'il y a plusieurs appareils et que la rééligibilité est désactivée, l'utilisateur ne devrait voir le message in-app qu'une seule fois. Même si l'utilisateur utilise plusieurs appareils, il ne le verra que sur le premier appareil ciblé. Cela suppose que le profil a consolidé les appareils et qu'un utilisateur dispose d'un ID utilisateur unique auquel il est connecté sur tous les appareils. Si la rééligibilité est activée, une impression est enregistrée chaque fois que l'utilisateur voit le message in-app.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Nombre total d'ouvertures

{% apitags %}
E-mail, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

|Canal|Informations supplémentaires|
|-------|-----------------------|
|LINE|Suivi après qu'un seuil minimum de 20 messages par jour a été atteint.|
|E-mails AMP|Le total des ouvertures pour les versions HTML et en texte brut.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b>E-mail <i>Nombre total d'ouvertures</i> :</b> Total</li>
        <li><b>E-mail <i>Taux d'ouverture total</i> :</b> (Ouvertures) / (Réceptions)</li>
        <li><b>Web push <i>Nombre total d'ouvertures</i> :</b> Nombre d'<i>ouvertures directes</i></li>
        <li><b>Web push <i>Taux d'ouverture total</i> :</b> (Ouvertures totales) / (Réceptions)</li>
        <li><b>iOS, Android et Kindle push <i>Nombre total d'ouvertures</i> :</b> (Ouvertures directes) + (Ouvertures influencées)</li>
        <li><b>iOS, Android et Kindle push <i>Taux d'ouverture total</i> :</b> (Ouvertures totales) / (Réceptions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Total des revenus

{% apitags %}
Cartes de contenu, E-mail, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} Cet indicateur n'est disponible que dans les rapports de comparaison de campagnes, via le <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>générateur de rapports.</a>

{% endapi %}

{% api %}

### Clics uniques

{% apitags %}
E-mail, Cartes de contenu, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

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
        <li><i>Clics uniques</i> : Total</li>
        <li><b>Cartes de contenu</b> <i>% de clics uniques</i> ou <i>taux de clics uniques</i> : (Clics uniques) / (Impressions uniques)</li>
        <li><b>E-mail</b> <i>% de clics uniques</i> ou <i>taux de clics uniques</i> : (Clics uniques) / (Réceptions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Rejets uniques

{% apitags %}
Cartes de contenu
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">Calcul : (Rejets uniques) / (Impressions uniques)</span>

{% endapi %}

{% api %}

### Impressions uniques

{% apitags %}
Message in-app, Cartes de contenu
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} 

|Canal|Informations supplémentaires|
|-------|-----------------------|
|Messages in-app|Les impressions uniques peuvent être à nouveau incrémentées après 24 heures si la rééligibilité est activée et qu'un utilisateur effectue l'action de déclenchement. Si la rééligibilité est activée, <i>Impressions uniques</i> = <i>Destinataires uniques</i>.|
|Cartes de contenu|Le décompte ne doit pas être incrémenté la deuxième fois qu'un utilisateur consulte une carte.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Ouvertures uniques

{% apitags %}
E-mail, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %}

|Canal|Informations supplémentaires|
|-------|-----------------------|
|E-mail|Suivi sur une période de 7 jours.|
|LINE|Suivi après qu'un seuil minimum de 20 messages par jour a été atteint.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Ouvertures uniques</i> : Total</li>
        <li><i>% d'ouvertures uniques</i> ou <i>taux d'ouvertures uniques</i> : (Ouvertures uniques) / (Réceptions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Destinataires uniques

{% apitags %}
Tous
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}

Étant donné qu'un utilisateur peut être un destinataire unique chaque jour, vous devriez vous attendre à ce que ce chiffre soit plus élevé que celui des <i>impressions uniques</i>. Pour les cartes de contenu, chaque carte de contenu ne peut être reçue qu'une seule fois, de sorte que la consultation de la même carte de contenu une deuxième fois, quel que soit le jour, n'incrémentera pas ce décompte.<br><br>Ce nombre est fourni par Braze et est basé sur le `user_id`. Les destinataires uniques sont comptabilisés au niveau de la campagne ou de l'étape du canvas, et non au niveau de l'<a href='https://braze.com/docs/api/identifier_types/#send-identifier'>identifiant d'envoi</a>.

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Désabonnés

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><i>Désabonnés</i> ou <i>Désab.</i> : Total</li>
        <li><i>% de désabonnements</i> ou <i>taux de désabonnement</i> : (Désinscriptions) / (Réceptions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Désinscriptions

{% apitags %}
E-mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribes' %}

<span class="calculation-line">Calcul : (Désinscriptions) / (Réceptions)</span>

{% endapi %}

{% api %}

### Variante

{% apitags %}
Cartes de contenu, E-mail, Message in-app, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}