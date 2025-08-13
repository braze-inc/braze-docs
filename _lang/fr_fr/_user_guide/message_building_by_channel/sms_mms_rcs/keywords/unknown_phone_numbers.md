---
nav_title: Gestion des numéros de téléphone inconnus
article_title: Gestion des numéros de téléphone inconnus
page_order: 4
description: "Cet article de référence explique comment Braze traite les numéros de téléphone inconnus des nouveaux utilisateurs."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
  
---

# Gestion des numéros de téléphone inconnus - nouveaux utilisateurs

> Il se peut qu'après avoir mis en service les SMS, MMS et RCS avec Braze, vous receviez des messages d'utilisateurs inconnus. Les étapes suivantes décrivent comment un utilisateur et un numéro non identifiés sont traités.

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

