---
nav_title: Gestion des numéros de téléphone inconnus
article_title: Gestion des numéros de téléphone SMS inconnus
page_order: 4
description: "Cet article de référence explique comment Braze traite les numéros de téléphone SMS inconnus de nouveaux utilisateurs."
page_type: reference
channel:
  - SMS
  
---

# Gestion des numéros de téléphone inconnus - nouveaux utilisateurs

> Vous pouvez constater qu'après avoir activé les SMS avec Braze, vous recevez des messages d'utilisateurs inconnus. Les étapes suivantes décrivent comment un utilisateur et un numéro non identifiés sont traités.

{% alert important %}
Êtes-vous actuellement un client SMS non natif ? Si c'est le cas, consultez la [documentation SMS non native]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) pour votre article correspondant sur la gestion des numéros de téléphone inconnus.
{% endalert %}

## Abonnement/désabonnement et workflow de mot-clé personnalisé pour les numéros inconnus

Braze traite automatiquement un numéro inconnu de trois manières :

1. Si un mot-clé d’abonnement est envoyé par SMS :
  * Braze crée un profil anonyme
  * Notre système définit l’attribut de téléphone
  * Il abonne l’utilisateur au groupe d’abonnement correspondant selon le mot-clé d’abonnement reçu par Braze.<br><br>
2. Si un mot-clé de désabonnement est envoyé par SMS :
  * Braze crée un profil anonyme
  * Notre système définit l’attribut de téléphone
  * Il désabonne l’utilisateur du groupe d’abonnement correspondant selon le mot-clé de désabonnement reçu par Braze.<br><br>
3. Si un autre mot-clé personnalisé est envoyé par SMS :
  * Braze ignore le message texte et ne fait rien.

[ualink]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[telink]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[uaolink]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[e.164]: https://en.wikipedia.org/wiki/E.164