---
nav_title: Gestion des numéros de téléphone inconnus
article_title: Gestion du numéro de téléphone non natif SMS inconnu
page_order: 1
description: "Cet article de référence décrit comment Braze va gérer les numéros de téléphone inconnus pour les utilisateurs non natifs de SMS."
page_type: Référence
channel:
  - SMS
---

# Gestion des numéros de téléphone inconnus - nouveaux utilisateurs

Une fois que vous aurez mis en place un SMS avec Braze, vous pourrez recevoir des messages d'utilisateurs inconnus. Noté ci-dessous les étapes par lesquelles un utilisateur et un numéro non identifiés sont traités.

Braze peut créer automatiquement un utilisateur lorsqu'un utilisateur avec un nouveau numéro de téléphone répond avec un `START` ou `STOP` (ou toute autre variation de ces mots-clés).  Lors de la création de l'utilisateur, Braze définira son champ de téléphone avec le numéro [E.164][e.164] fourni par notre fournisseur de SMS.  De plus, l'alias d'utilisateur [][ualink] ('phone') sera défini avec la même valeur.<br><br>Les clients peuvent utiliser l'objet [Attributs utilisateur][uaolink] en tandem avec le [Point d'extrémité de traquage][telink] pour trouver des utilisateurs en fonction de leur alias et définir un `external_id`.

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

{% alert important %}
Si vous souhaitez activer cette fonctionnalité, veuillez contacter votre Responsable d'intégration ou Responsable du Service Clientèle.
{% endalert %}

[ualink]: {{site.baseurl}}/api/objects_filters/user_alias_object/

[ualink]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[telink]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[uaolink]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[e.164]: https://en.wikipedia.org/wiki/E.164
