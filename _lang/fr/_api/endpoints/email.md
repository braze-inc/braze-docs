---
nav_title: "Listes et adresses e-mail"
article_title: Endpoints des listes et adresses e-mail
search_tag: Endpoint
page_order: 1
layout: dev_guide

description: "Cette page d’accueil explique et répertorie les endpoints Braze de listes et adresses e-mail."
page_type: landing

guide_top_header: "Endpoints des listes et adresses e-mail"
guide_top_text: "Le statut de l’abonnement aux e-mails des utilisateurs peut être mis à jour et récupéré via Braze à l’aide d’une API RESTful. Vous pouvez utiliser l’API pour configurer une synchronisation bidirectionnelle entre Braze et d’autres systèmes de messagerie ou votre propre base de données."

guide_featured_title: ""
guide_featured_list:
  - name: "GET : répertorier les taux de rebonds élevés"
    link: /docs/api/endpoints/email/get_list_hard_bounces/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET : demander les adresses e-mail désinscrites"
    link: /docs/api/endpoints/email/get_query_unsubscribed_email_addresses/
    image: /assets/img/braze_icons/mail-01.svg
  - name: "POST : modifier le statut de l’abonnement aux e-mails"
    link: /docs/api/endpoints/email/post_email_subscription_status/
    image: /assets/img/braze_icons/at-sign.svg
  - name: "POST : supprimer les rebonds élevés"
    link: /docs/api/endpoints/email/post_remove_hard_bounces/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "POST : supprimer les courriers indésirables"
    link: /docs/api/endpoints/email/post_remove_spam/
    image: /assets/img/braze_icons/mail-04.svg
  - name: "POST : ajouter l’e-mail à la liste de blocage"
    link: /docs/api/endpoints/email/post_blocklist/
    image: /assets/img/braze_icons/mail-04.svg
---
{% comment %}
rediriger depuis email_sync.md
{% endcomment %}
