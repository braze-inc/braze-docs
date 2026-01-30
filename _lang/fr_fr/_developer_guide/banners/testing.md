---
nav_title: Bannières de test
article_title: Bannières de test
page_order: 2
description: "Découvrez comment tester votre message Banner avant de lancer votre campagne afin de vous assurer que tous les médias, le texte, la personnalisation et les attributs personnalisés s'affichent correctement."
channel:
  - banners
noindex: true
---

# Bannières de test

> Découvrez comment tester votre message Banner avant de lancer votre campagne afin de vous assurer que tous les médias, le texte, la personnalisation et les attributs personnalisés s'affichent correctement. Pour plus d'informations générales, reportez-vous à la section [À propos des bannières]({{site.baseurl}}/developer_guide/banners).

## Conditions préalables

Avant de pouvoir tester les messages des bannières dans Braze, vous devez créer une [campagne de communication dans Braze]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/). En outre, vérifiez que le placement que vous souhaitez tester est déjà [placé dans votre application ou votre site web.]({{site.baseurl}}/developer_guide/banners/placements) 

Pour envoyer un test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou à des utilisateurs individuels, la fonction push doit être activée sur vos appareils de test et des jetons push valides doivent être enregistrés pour l'utilisateur test avant l'envoi.

## Tester une bannière

{% multi_lang_include banners/testing.md page="testing" %}
