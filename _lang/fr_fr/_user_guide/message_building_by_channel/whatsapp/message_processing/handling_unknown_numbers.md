---
nav_title: Gestion des numéros de téléphone inconnus
article_title: Gestion des numéros de téléphone inconnus
description: "Cet article de référence explique comment Braze gérera les numéros de téléphone inconnus pour les utilisateurs de WhatsApp."
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# Gestion des numéros de téléphone inconnus

> Il se peut qu'après avoir configuré WhatsApp avec Braze, vous receviez des messages d'utilisateurs inconnus. Les étapes suivantes décrivent comment un utilisateur et un numéro non identifiés sont traités.

## Abonnement/désabonnement et workflow de mot-clé personnalisé pour les numéros inconnus

Braze va d'abord tenter de trouver un utilisateur avec un numéro correspondant. Si aucun utilisateur n'est trouvé, Braze traite automatiquement un nombre inconnu de l'une des deux manières suivantes :

1. **Si un mot déclencheur avec un [canvas sur abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/) a été configuré :**
- Braze crée un profil anonyme
- Nous attribuons un alias utilisateur au profil avec les détails suivants :
  - Un `alias_name` avec la valeur étant le numéro de téléphone fourni par l'utilisateur
  - Un `alias_label` avec la valeur `phone`
- Notre système définit l’attribut de téléphone
- L'utilisateur est abonné au groupe d'abonnement correspondant en fonction de la logique mise en place dans le Canvas<br><br>
2. **Si aucun canvas sur abonnement n’a été configuré :**
- Braze crée un profil anonyme
- Nous attribuons un alias utilisateur au profil avec les détails suivants :
  - Un `alias_name` avec la valeur étant le numéro de téléphone fourni par l'utilisateur
  - Un `alias_label` avec la valeur `phone`
- Notre système définit l’attribut de téléphone
- Le statut d'abonnement de l'utilisateur sera défini par défaut sur `unsubscribed` pour tous les groupes d'abonnement WhatsApp<br><br>

