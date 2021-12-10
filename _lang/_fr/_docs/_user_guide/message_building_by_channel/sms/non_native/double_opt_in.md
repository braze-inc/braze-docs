---
nav_title: Processus de double opt-in
article_title: Processus de double opt-in SMS non-natif
page_order: 5
description: "Cet article de référence décrit comment Braze traite certains mots-clés pour les utilisateurs non natifs de SMS, ainsi que les meilleures pratiques lors de la création d'une campagne de webhook SMS."
page_type: Référence
channel:
  - SMS
  - webhooks
---

# Processus double opt-in

Vous pouvez trouver que certains utilisateurs qui peuvent envoyer un texte à votre code court ou long ne sera pas encore pris en compte dans votre groupe d'abonnement SMS. Le règlement exige que vous obteniez le consentement explicite d’un utilisateur avant de lui envoyer tout message promotionnel ou informatif. Nous recommandons vivement la mise en œuvre d'un double opt-in pour garantir la conformité.

!\[picture\]\[IMAGE1\]{: style="float:right;max-width:30%;margin-left:15px;"} Nous vous suggérons de définir une __entrée déclenchée__ dans Canvas chaque fois qu'il y a un événement entrant `sms_response_subscriptionGroupName_custom`.

## Étape 1 : Créer un webhook

Nous suggérons tout d'abord de créer une campagne de webhook qui fait une demande à [abonnement/statut/point de terminaison][SSSendpoint] pour s'abonner à ce groupe d'abonnement SMS.

## Étape 2 : Envoyer une campagne SMS

Ensuite, nous vous recommandons d'envoyer une campagne de SMS quelques secondes plus tard, avec des appels clairs le long des lignes de :

!\[picture\]\[IMAGE\]{: style="border: 0"}
[IMAGE]: {% image_buster /assets/img/sms/sms_cta.png %} [IMAGE1]: {% image_buster /assets/img/sms/sms_canvas.png %}

[SSSendpoint]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
