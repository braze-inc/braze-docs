---
nav_title: Traiter les numéros de téléphone inconnus
article_title: Traitement des numéros de téléphone inconnus
page_order: 4
description: "Cet article de référence explique comment Braze traite les numéros de téléphone inconnus des nouveaux utilisateurs."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
  
---

# Traitement des numéros de téléphone inconnus - nouveaux utilisateurs

> Il se peut qu'après avoir mis en service les SMS, MMS et RCS avec Braze, vous receviez des messages d'utilisateurs inconnus. Les étapes suivantes décrivent le traitement d'un utilisateur et d'un numéro non identifiés.

## Abonnement/refus et flux de mots-clés personnalisés pour les numéros inconnus

Braze s'adresse automatiquement à un numéro inconnu de l'une des trois manières suivantes :

1. Si un mot-clé d'abonnement est envoyé par SMS :
  * Braze crée un profil anonyme
  * Notre système définit l'attribut téléphone
  * Abonne l'utilisateur au groupe d'abonnement correspondant en fonction du mot-clé d'abonnement reçu par Braze.<br><br>
2. Si un mot-clé d'abonnement est envoyé :
  * Braze crée un profil anonyme
  * Notre système définit l'attribut téléphone
  * Désabonne l'utilisateur du groupe d'abonnement correspondant en fonction du mot-clé de désabonnement reçu par Braze.<br><br>
3. Si un autre mot-clé personnalisé est envoyé :
  * Braze ignore le message et ne fait rien.

