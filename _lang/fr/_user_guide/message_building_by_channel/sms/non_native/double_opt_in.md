---
nav_title: Processus d’abonnement double
article_title: Processus d’abonnement double SMS non natif
page_order: 5
description: "Le présent article de référence traite de la manière dont Braze traite certains mots clés pour les utilisateurs de SMS non-natif, ainsi que les bonnes pratiques lors de la création d’une campagne de webhook SMS."
page_type: reference
channel:
  - SMS
  - Webhooks

---

# Processus de double abonnement

Il se peut que certains utilisateurs qui envoient un texte à votre code court ou code long ne soient pas encore connectés à votre groupe d’abonnement SMS. Les réglementations exigent que vous obteniez le consentement explicite d’un utilisateur avant de lui envoyer des messages promotionnels ou informatifs. Nous recommandons fortement de mettre en œuvre un double abonnement pour assurer la conformité. 

![][IMAGE1]{: style="float:right;max-width:30%;margin-left:15px;"}
Nous suggérons de définir une entrée déclenchée dans Canvas chaque fois qu’il y a un événement entrant`sms_response_subscriptionGroupName_custom`. Consulter [Gestion de messagerie par mots-clés personnalisés][1] pour plus d’informations.

## Étape 1 : Créer un Webhook

Nous suggérons d’abord de créer une campagne Webhook qui fait une demande à l’endpoint [subscription/status/set][SSSendpoint] pour inscrire l’utilisateur dans ce groupe d’abonnement SMS.

## Étape 2 : Envoyer une campagne SMS

Puis nous vous recommandons d’envoyer une campagne SMS quelques secondes plus tard, avec des appels à l’action clairs comme :

![message SMS avec le texte « Braze : Merci de votre intérêt pour Deal Texts ! Attendez-vous à trois messages par mois ! Répondez OUI pour vous inscrire, STOP pour arrêter, HELP pour obtenir de l’aide. Des tarifs pour les messages et les données peuvent s’appliquer. »][IMAGE]{: style="border: 0"}

[SSSendpoint]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[IMAGE]: {% image_buster /assets/img/sms/sms_cta.png %}
[IMAGE1]: {% image_buster /assets/img/sms/sms_canvas.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/non_native/custom_keyword_handling#custom-keyword-messaging-handling
