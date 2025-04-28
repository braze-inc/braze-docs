---
nav_title: Glossaire analytique pour l’e-mail
article_title: Glossaire analytique pour l’e-mail
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire inclut les termes que vous trouverez dans la section d’analyse de votre campagne par e-mail ou de Canvas, après son lancement. Ce glossaire n’inclut pas les indicateurs Currents."
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
Total
{% endapitags %}

{% multi_lang_include metrics.md metric='Variation' %}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Emailable

{% apitags %}
Total
{% endapitags %}

{% multi_lang_include metrics.md metric='Emailable' %}

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### % d’audience

{% apitags %}
Pourcentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Audience' %}

<span class="calculation-line">Calcul : (Nombre de destinataires dans la variante) / (Destinataires uniques)</span>

{% endapi %}

{% api %}

### Destinataires uniques

{% apitags %}
Total
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Recipients' %} Ce numéro est reçu de Braze.

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Envois

{% apitags %}
Total
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends' %} Cette métrique est fournie par Braze.

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Messages envoyés

{% apitags %}
Total
{% endapitags %}

{% multi_lang_include metrics.md metric='Messages Sent' %} Cette métrique est fournie par Braze.

<span class="calculation-line">Calcul : Total</span>

{% endapi %}

{% api %}

### Réceptions

{% apitags %}
Total
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries' %} Pour les e-mails, *Deliveries* est le nombre total de messages (Sends) envoyés et reçus avec succès par les destinataires de l'e-mail.

<span class="calculation-line">Calcul : (Envoie) - (Rebondit) </span>

{% endapi %}

{% api %}

### % de livraisons

{% apitags %}
Pourcentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries %' %}

<span class="calculation-line">Calcul : (Envois - Rebonds) / (Envois) </span>

{% endapi %}

{% api %}

### Rebonds

{% apitags %}
Nombre, pourcentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Bounces' %} 

Pour l'e-mail, le *taux de* *rebond* est le pourcentage de messages qui ont été envoyés sans succès ou désignés comme "renvoyés" ou "non reçus" par les services d'envoi utilisés ou qui n'ont pas été reçus par les utilisateurs visés par l'e-mail.

Pour les clients utilisant SendGrid, un échec d'e-mail se compose d'un échec définitif, de spam (`spam_report_drops`) et d'e-mails envoyés à des adresses non valides (`invalid_emails`).

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Rebonds</i>:</b> Total</li>
        <li><b><i>Taux de rebond (Bounce %</i> ) ou <i>taux de rebond (Bounce Rate %)</i>:</b> (Bounces)/(Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Échec d'envoi définitif

{% apitags %}
Total
{% endapitags %}

{% multi_lang_include metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">Calcul : Compter </span>

{% endapi %}

{% api %}

### Échec provisoire de livraison

{% apitags %}
Total
{% endapitags %}

{% multi_lang_include metrics.md metric='Soft Bounce' %} Si un e-mail reçoit un échec provisoire d'envoi, nous effectuons généralement une nouvelle tentative dans les 72 heures, mais le nombre de tentatives varie d'un destinataire à l'autre.

<span class="calculation-line">Calcul : Compter </span>

{% endapi %}

{% api %}
  
### Spam

{% apitags %}
Nombre, pourcentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Spam</i>:</b> Total</li>
        <li><b><i>Spam %</i> ou <i>Spam Rate % :</i></b> (Marqué comme spam) / (Envois)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Ouvertures uniques

{% apitags %}
Nombre, pourcentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Opens' %} Pour les e-mails, le suivi se fait sur une période de 7 jours.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Ouverture unique</i>:</b> Total</li>
        <li><b><i>Pourcentage d'ouvertures uniques</i> ou <i>taux d'ouvertures uniques</i>:</b> (Ouvertures uniques) / (Livraisons)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Clics uniques

{% apitags %}
Nombre, pourcentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Clicks' %} Ce suivi est effectué sur une période de sept jours pour les e-mails et mesuré par <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. Cela inclut les clics sur les liens de désinscription fournis par Braze.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Clics uniques</i>:</b> Total</li>
        <li><b><i>Pourcentage de clics uniques</i> ou <i>taux de clics</i>:</b> (Clics uniques) / (Réceptions/distributions)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Désabonnés

{% apitags %}
Nombre, pourcentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Désabonnés</i> ou <i>désabonnés</i>:</b> Total</li>
        <li><b><i>Pourcentage de désabonnements</i> ou <i>taux de désabonnement</i>:</b> (Désinscriptions)/(Livraisons)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Revenue

{% apitags %}
Total
{% endapitags %}

{% multi_lang_include metrics.md metric='Revenue' %}

<span class="calculation-line">Calcul : Compter </span>

{% endapi %}

{% api %}

### Conversions principales (A) ou événement de conversion principal

{% apitags %}
Nombre, pourcentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Pour les e-mails, les pushs et les webhooks, nous commençons à suivre les conversions après l'envoi initial.

{::nomarkdown}
<span class="calculation-line">
    Calcul :
    <ul>
        <li><b><i>Conversions principales (A)</i> ou <i>événement de conversion principal</i>:</b> Total</li>
        <li><b><i>Conversions primaires (A) %</i> ou <i>taux d'événement de conversion principal</i>:</b> (Conversions principales)/(Destinataires uniques)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confiance

{% apitags %}
Total
{% endapitags %}

{% multi_lang_include metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Ouverture automatique
  
{% multi_lang_include metrics.md metric='Machine Opens' %} This metric is tracked starting November 11, 2021 for SendGrid and December 2, 2021 for SparkPost.

<span class="calculation-line">Calcul : Compter </span>

{% endapi %}

{% api %}

### Autre ouverture

{% apitags %}
Total
{% endapitags %}

{% multi_lang_include metrics.md metric='Other Opens' %} Note that a user can also open an email (such as the open counts toward <i>Other Opens</i>) before a <i>Machine Opens</i> count is logged. Si un utilisateur ouvre un e-mail une fois (ou plus) après un événement d'ouverture automatique à partir d'une boîte de réception autre qu'Apple Mail, le nombre de fois où l'utilisateur ouvre l'e-mail est calculé pour les <i>autres ouvertures</i> et une seule fois pour les <i>ouvertures uniques</i>.

<span class="calculation-line">Calcul : Compter </span>

{% endapi %}

{% api %}

### Taux de Click-to-Open

{% apitags %}
Pourcentage
{% endapitags %}

{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Calcul : (Clics uniques) / (Ouvertures uniques) (pour l'e-mail)</span>

{% endapi %}