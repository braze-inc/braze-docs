---
nav_title: Changer votre toile après le lancement
article_title: Changer votre toile après le lancement
page_order: 1
description: "Cet article de référence couvre les différents aspects d'une toile qui peut être modifiée après le lancement initial."
page_type: Référence
tool:
  - Toile
---

# Changement de Canvas après le lancement

> Cet article de référence couvre les différents aspects d'une toile qui peut être modifiée après le lancement initial.

## Conditions initiales

| **Modifiable**                 | **Non modifiable**       |
| ------------------------------ | ------------------------ |
| Nom et description de la toile | Événements de conversion |
| Équipes et Tags                |                          |
| Type d'entrée                  |                          |
| Calendrier des entrées         |                          |
| Contrôles d'entrée             |                          |
| Statut de l'abonnement         |                          |
| Limitation des taux            |                          |
| Plafond de fréquence           |                          |
| Heures silencieuses            |                          |
| Public cible                   |                          |
{: .reset-td-br-1 .reset-td-br-2}

## Graphique en toile

| **Modifiable**                                                | **Non modifiable**         |
| ------------------------------------------------------------- | -------------------------- |
| Arrêt / Reprendre l'exécution de toutes les étapes du canevas | Suppression des étapes     |
| Insérer des marches de toile                                  | Suppression des variantes  |
| Ajouter de nouvelles connexions                               | Suppression des connexions |
| Ajouter de nouvelles variantes                                |                            |
| Distribution de variants*                                     |                            |
{: .reset-td-br-1 .reset-td-br-2}

*La distribution de variantes de contrôle ne peut être réduite qu'après le lancement.

## Étape individuelle

| **Modifiable**                              | **Non modifiable**                                     |
| ------------------------------------------- | ------------------------------------------------------ |
| Nom                                         | Type de planification (passer du délai au déclencheur) |
| Contenu du message                          | Contrôler les pourcentages                             |
| Étape Message Platforms (ajouter/supprimer) |                                                        |
| Déclencheurs                                |                                                        |
| Audience                                    |                                                        |
| Événements d'exception                      |                                                        |
| Délai / Windows                             |                                                        |
{: .reset-td-br-1 .reset-td-br-2}

## Réalisation du lancement des publications de modification

Il y a un certain nombre de choses à savoir si vous prévoyez de modifier ou ajouter d'autres étapes à une autre étape de Canvas après le lancement :

- Les utilisateurs qui ne sont pas encore entrés dans Canvas seront admissibles aux étapes nouvellement créées.
- Les utilisateurs qui ont déjà franchi les étapes nouvellement créées seront éligibles la prochaine fois qu'ils entreront à nouveau dans les paramètres d'entrée de Canvas si vous avez autorisé les utilisateurs à entrer à nouveau dans le Canvas dans les paramètres.
- Utilisateurs qui sont actuellement dans un Canvas, mais n'ont pas atteint les points où de nouvelles étapes sont ajoutées sera éligible pour recevoir ces nouvelles étapes.
- Vous ne pouvez pas modifier ou supprimer des connexions existantes, pas plus que vous ne pouvez insérer une étape entre les étapes connectées existantes une fois qu'un Canvas est lancé.
- Si vous mettez à jour le délai ou la fenêtre pour une étape, Seuls les nouveaux utilisateurs qui entrent dans le Canvas et les utilisateurs qui n'ont pas encore été mis en file d'attente pour cette étape recevront le message au délai mis à jour.

{% alert note %}
Arrêt d'une Canvas n'effacera pas les utilisateurs qui attendent de recevoir des messages. Si vous réactivez le Canvas et que les utilisateurs attendent toujours le message, ils le recevront (sauf si le temps qu’il leur faut pour être envoyés, le message est passé, alors ils ne le recevront pas).
{% endalert %}

## Pourcentages de variantes de la toile

Dans Canvas, si un pourcentage de variante est modifié, vous constaterez que les utilisateurs peuvent être redistribués à d'autres variantes.

Au départ, une variante particulière est assignée aléatoirement aux utilisateurs avant de recevoir une campagne pour la première fois. À partir de là, chaque fois que la campagne est reçue (ou que l'utilisateur entre à nouveau dans une variante de Canvas) — ils recevront la même variante à moins que les pourcentages de variantes ne soient modifiés.

Si les pourcentages de variante changent, les utilisateurs peuvent être redistribués à d'autres variantes. Les utilisateurs restent dans ces variantes jusqu'à ce que les pourcentages soient à nouveau modifiés.

### Groupes de contrôle

Les groupes de contrôle restent cohérents si le pourcentage de variante est inchangé. Les utilisateurs qui ont déjà reçu des messages ne peuvent pas entrer dans le groupe de contrôle lors d'un envoi ultérieur, et aucun utilisateur du groupe de contrôle ne peut recevoir de message.

## Heure d'envoi locale

Les Canvases à l'heure locale d'envoi peuvent être modifiées jusqu'à 24 heures avant l'envoi des horaires. Cette fenêtre s'appelle "zone sûre". Notez que si vous avez l'intention d'apporter des changements à votre Canvas qui vous obligent à faire un nouveau Canvas entièrement, N'oubliez pas d'exclure les utilisateurs qui ont reçu le premier Canvas et de réajuster les horaires de Canvas pour permettre l'envoi du fuseau horaire.
