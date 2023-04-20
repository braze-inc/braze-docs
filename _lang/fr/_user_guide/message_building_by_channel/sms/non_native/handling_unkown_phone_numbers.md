---
nav_title: Gestion des numéros de téléphone inconnus
article_title: Traitement des numéros de téléphone inconnus pour SMS non natif
page_order: 1
description: "Le présent article de référence traite de la façon dont Braze va gérer les numéros de téléphone inconnus pour les utilisateurs SMS non natifs."
page_type: reference
channel:
  - SMS

---

# Gestion des numéros de téléphone inconnus - nouveaux utilisateurs

> Vous pouvez constater qu’après avoir activé les SMS dans Braze, vous recevez des messages d’utilisateurs inconnus. L’article suivant donne les étapes par lesquelles un utilisateur et un numéro non identifiés sont traités.

Braze peut créer automatiquement un utilisateur lorsqu’un utilisateur avec un nouveau numéro de téléphone répond par `START` ou `STOP` (ou une autre variante de ces mots-clés).  Lors de la création de l’utilisateur, Braze définit son champ téléphone avec le numéro [E.164][e.164] fourni par notre fournisseur SMS.  En outre, l’[alias utilisateur][ualink] (« téléphone ») sera défini avec la même valeur.<br><br>Les clients peuvent utiliser l’ [objet attributs d’utilisateur][uaolink] en tandem avec l’[endpoint de suivi utilisateur][telink] pour trouver des utilisateurs en fonction de leur alias et définir une `external_id`.

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

{% alert important %}
Si vous souhaitez activer cette fonctionnalité, contactez votre gestionnaire d’onboarding ou le gestionnaire du succès des clients.
{% endalert %}

[ualink]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[telink]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[uaolink]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[e.164]: https://en.wikipedia.org/wiki/E.164
