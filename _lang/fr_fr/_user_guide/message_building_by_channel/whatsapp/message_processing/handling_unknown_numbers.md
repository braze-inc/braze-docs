---
nav_title: Traiter les numéros de téléphone inconnus
article_title: Traitement des numéros de téléphone inconnus
description: "Cet article de référence explique comment Braze va s'y prendre pour gérer les numéros de téléphone inconnus des utilisateurs de WhatsApp."
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# Traiter les numéros de téléphone inconnus

> Il se peut qu'après avoir mis WhatsApp en service avec Braze, vous receviez des messages d'utilisateurs inconnus. Les étapes suivantes décrivent le traitement d'un utilisateur et d'un numéro non identifiés.

## Abonnement/refus et flux de mots-clés personnalisés pour les numéros inconnus

Braze tentera d'abord de trouver un utilisateur dont le numéro correspond. Si aucun numéro n'est trouvé, Braze adresse automatiquement un numéro inconnu de l'une des deux manières suivantes :

1. **Si un mot déclencheur avec un [canvas d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/) est mis en place :**
- Braze crée un profil anonyme
- Nous attribuons un alias d'utilisateur au profil avec les détails suivants :
  - Un `alias_name` dont la valeur est le numéro de téléphone fourni par l'utilisateur.
  - Un `alias_label` avec la valeur `phone`
- Notre système définit l'attribut téléphone
- L'utilisateur est abonné au groupe d'abonnement correspondant en fonction de la logique mise en place dans le Canvas.<br><br>
2. **Si aucun canvas d'abonnement n'est mis en place :**
- Braze crée un profil anonyme
- Nous attribuons un alias d'utilisateur au profil avec les détails suivants :
  - Un `alias_name` dont la valeur est le numéro de téléphone fourni par l'utilisateur.
  - Un `alias_label` avec la valeur `phone`
- Notre système définit l'attribut téléphone
- Le statut de l'abonnement de l'utilisateur sera par défaut `unsubscribed` pour tous les groupes d'abonnement WhatsApp.<br><br>

