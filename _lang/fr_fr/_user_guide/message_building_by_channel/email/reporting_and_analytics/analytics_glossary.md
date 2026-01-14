---
nav_title: "Glossaire de l'analyse/analytique des e-mails (si utilisé comme adjectif)"
article_title: "Glossaire de l'analyse/analytique des e-mails (si utilisé comme adjectif)"
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire comprend les termes que vous trouverez dans la section analyse/analytique de votre campagne e-mail ou Canvas, après le lancement. Ce glossaire ne comprend pas les indicateurs de Currents."
channel: 
  - email
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Variation

{% apitags %}
Compter
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Calcul : Compter</span>

{% endapi %}

{% api %}

### Disponible par e-mail

{% apitags %}
Compter
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Calcul : Compter</span>

{% endapi %}

{% api %}

### % de l'audience

{% apitags %}
Pourcentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Calcul : (Nombre de destinataires dans la variante) / (Destinataires uniques)</span>

{% endapi %}

{% api %}

### Destinataires uniques

{% apitags %}
Compter
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} Ce numéro est reçu de Braze.

<span class="calculation-line">Calcul : Compter</span>

{% endapi %}

{% api %}

### Envoie

{% apitags %}
Compter
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  Ces indicateurs sont fournis par Braze.

<span class="calculation-line">Calcul : Compter</span>

{% endapi %}

{% api %}

### Envois de messages

{% apitags %}
Compter
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Ces indicateurs sont fournis par Braze.

<span class="calculation-line">Calcul : Compter</span>

{% endapi %}

{% api %}

### Réceptions/distributions

{% apitags %}
Compter
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} Pour les e-mails, la *réception/distribution* est le nombre total de messages (envois) envoyés et reçus avec succès par les destinataires de l'e-mail.

<span class="calculation-line">Calcul : (Envoie) - (Rebondit) </span>

{% endapi %}

{% api %}

### Réceptions/distributions en %.

{% apitags %}
Pourcentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">Calcul : (Envois - Rebonds) / (Envois) </span>

{% endapi %}

{% api %}

### Rebonds

{% apitags %}
Nombre, pourcentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} 

Pour l'e-mail, le *taux de* *rebond* est le pourcentage de messages qui ont été envoyés sans succès ou désignés comme "renvoyés" ou "non reçus" par les services d'envoi utilisés ou qui n'ont pas été reçus par les utilisateurs visés par l'e-mail.

Pour les clients utilisant SendGrid, un échec d'e-mail se compose d'un échec définitif, de spam (`spam_report_drops`) et d'e-mails envoyés à des adresses non valides (`invalid_emails`).

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Rebonds</i>:</b> Compter</li>
        <li><b><i>Taux de rebond (Bounce %</i> ) ou <i>taux de rebond (Bounce Rate %)</i>:</b> (Rebonds) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### échec d'envoi définitif

{% apitags %}
Compter
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">Calcul : Compter </span>

{% endapi %}

{% api %}

### Échappée provisoire d'envoi

{% apitags %}
Compter
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Si un e-mail reçoit un échec provisoire d'envoi, nous effectuons généralement une nouvelle tentative dans les 72 heures, mais le nombre de tentatives varie d'un destinataire à l'autre. 

Bien que les échecs provisoires ne soient pas suivis dans l'analyse/analytique de votre campagne, vous pouvez surveiller les échecs provisoires dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) ou exclure ces utilisateurs de vos envois à l'aide du [filtre de segmentation des échecs provis]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced)oires. Dans le journal d'activité des messages, vous pouvez également voir la raison des échecs provisoires et comprendre les écarts éventuels entre les "envois" et les "réception/distributions" de vos campagnes de communication par e-mail.

<span class="calculation-line">Calcul : Compter </span>

{% endapi %}

{% api %}
  
### Spam

{% apitags %}
Nombre, pourcentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Spam</i>:</b> Compter</li>
        <li><b><i>Spam %</i> ou <i>Spam Rate % :</i></b> (Marqué comme spam) / (Envoyé)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Ouvertures uniques

{% apitags %}
Nombre, pourcentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Pour les e-mails, le suivi se fait sur une période de 7 jours.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Ouverture unique</i>:</b> Compter</li>
        <li><b><i>Pourcentage d'ouvertures uniques</i> ou <i>taux d'ouvertures uniques</i>:</b> (Ouvertures uniques) / (Réceptions/distributions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Clics uniques

{% apitags %}
Nombre, pourcentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Ce suivi est effectué sur une période de sept jours pour les e-mails et mesuré par <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. Cela inclut les clics sur les liens de désinscription fournis par Braze.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Clics uniques</i>:</b> Compter</li>
        <li><b><i>Pourcentage de clics uniques</i> ou <i>taux de clics</i>:</b> (Clics uniques) / (Réceptions/distributions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Désabonnés ou désabonnement

{% apitags %}
Nombre, pourcentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Désabonnés</i> ou <i>désabonnés</i>:</b> Compter</li>
        <li><b><i>Pourcentage de désabonnements</i> ou <i>taux de désabonnement</i>:</b> (Désabonnements) / (Réceptions/distributions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Chiffre d'affaires

{% apitags %}
Compter
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">Calcul : Compter </span>

{% endapi %}

{% api %}

### Conversions principales (A) ou événement de conversion principal

{% apitags %}
Nombre, pourcentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Pour les e-mails, les push et les webhooks, nous commençons à suivre les conversions après l'envoi initial.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Conversions principales (A)</i> ou <i>événement de conversion principal</i>:</b> Compter</li>
        <li><b><i>Conversions primaires (A) %</i> ou <i>taux d'événement de conversion principal</i>:</b> (Conversions primaires) / (Destinataires uniques)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confiance

{% apitags %}
Compter
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### La machine s'ouvre
  
{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Cette mesure est suivie à partir du 11 novembre 2021 pour SendGrid et du 2 décembre 2021 pour SparkPost.

<span class="calculation-line">Calcul : Compter </span>

{% endapi %}

{% api %}

### Autres ouvertures

{% apitags %}
Compter
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Notez qu'un utilisateur peut également ouvrir un e-mail (comme les comptes d'ouverture vers <i>Autres ouvertures</i>) avant qu'un compte d'<i>ouvertures machine</i> ne soit enregistré. Si un utilisateur ouvre un e-mail une fois (ou plus) après un événement d'ouverture automatique à partir d'une boîte de réception autre qu'Apple Mail, le nombre de fois où l'utilisateur ouvre l'e-mail est calculé pour les <i>autres ouvertures</i> et une seule fois pour les <i>ouvertures uniques</i>.

<span class="calculation-line">Calcul : Compter </span>

{% endapi %}

{% api %}

### Taux de clics d'ouverture

{% apitags %}
Pourcentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Calcul : (Clics uniques) / (Ouvertures uniques) (pour l'e-mail)</span>

{% endapi %}