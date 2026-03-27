---
nav_title: "Listes et adresses e-mail"
article_title: Endpoints des listes et adresses e-mail
search_tag: Endpoint
page_order: 1
layout: dev_guide

description: "Cette page d'accueil explique et répertorie les endpoints Braze de listes et adresses e-mail."
page_type: landing

guide_top_header: "Endpoints des listes et adresses e-mail"
guide_top_text: "Grâce à cet ensemble d'endpoints, vous pouvez mettre à jour l'état d'abonnement e-mail d'un utilisateur et utiliser l'API Braze pour mettre en place une synchronisation bidirectionnelle entre Braze et d'autres systèmes d'e-mail ou votre propre base de données."

guide_featured_title: ""
guide_featured_list:
  - name: "GET : Répertorier les échecs d'envoi définitifs"
    link: /docs/api/endpoints/email/get_list_hard_bounces/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET : Rechercher les adresses e-mail désabonnées"
    link: /docs/api/endpoints/email/get_query_unsubscribed_email_addresses/
    image: /assets/img/braze_icons/mail-01.svg
  - name: "POST : Modifier l'état d'abonnement aux e-mails"
    link: /docs/api/endpoints/email/post_email_subscription_status/
    image: /assets/img/braze_icons/at-sign.svg
  - name: "POST : Supprimer les échecs d'envoi définitifs"
    link: /docs/api/endpoints/email/post_remove_hard_bounces/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "POST : Supprimer les spams"
    link: /docs/api/endpoints/email/post_remove_spam/
    image: /assets/img/braze_icons/mail-04.svg
  - name: "POST : Ajouter un e-mail à la liste de blocage"
    link: /docs/api/endpoints/email/post_blocklist/
    image: /assets/img/braze_icons/mail-04.svg
---
{% comment %}
redirect from email_sync.md
{% endcomment %}