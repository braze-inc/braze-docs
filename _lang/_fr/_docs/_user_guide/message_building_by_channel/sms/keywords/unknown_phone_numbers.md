---
nav_title: Gestion des numéros de téléphone inconnus
article_title: Gestion des numéros de téléphone SMS inconnus
page_order: 2
description: "Cet article de référence décrit comment Braze traite les numéros de téléphone SMS inconnus des nouveaux utilisateurs."
page_type: Référence
channel:
  - SMS
---

# Gestion des numéros de téléphone inconnus - nouveaux utilisateurs

Une fois que vous aurez mis en place un SMS avec Braze, vous pourrez recevoir des messages d'utilisateurs inconnus. Noté ci-dessous les étapes par lesquelles un utilisateur et un numéro non identifiés sont traités.

{% alert important %}
Êtes-vous actuellement un client SMS non-natif ? Si c'est le cas, veuillez visiter le [documentaion SMS non-natif](/docs/user_guide/message_building_by_channel/sms/non_native/) pour la gestion de votre numéro de téléphone correspondant à l'article des numéros de téléphone inconnus.
{% endalert %}

## Opt-in/out et le workflow personnalisé de mots clés pour les numéros inconnus

Braze adresse automatiquement un numéro inconnu de l'une des trois façons suivantes :

1. Si un mot clé opt-in est texté :
  * Braze crée un profil anonyme
  * Notre système définit l'attribut du téléphone
  * Inscrit l'utilisateur au groupe d'abonnement correspondant en fonction du mot clé opt-in reçu par Braze.<br><br>
2. Si un mot clé opt-out est texté :
  * Braze crée un profil anonyme
  * Notre système définit l'attribut du téléphone
  * Désabonne l'utilisateur du groupe d'abonnement correspondant en fonction du mot clé opt-out reçu par Braze.<br><br>
3. Si un autre mot clé personnalisé est texté :
  * Braze ignore le message texte et ne fait rien.