---
nav_title: Modification de Canvas après le lancement
article_title: Modification de Canvas après le lancement
page_order: 1
description: "Cet article de référence aborde les différents aspects d’un Canvas, pouvant être modifié après le lancement initial."
page_type: reference
tool:
  - Canvas

---

# Modification de Canvas après le lancement

> Cet article de référence aborde les éléments qui peuvent être modifiés sur un Canvas après le lancement initial.

## Overview

Il y a un certain nombre de choses à savoir si vous prévoyez de modifier ou d’ajouter des étapes supplémentaires à n’importe quelle autre étape d’un Canvas, après le lancement.

- Les utilisateurs qui n’ont pas encore accédé au Canvas seront éligibles pour les étapes créées.
- Les utilisateurs ayant déjà réussi les étapes créées seront éligibles lors du prochain accès, si vous les autorisez à accéder à nouveau au Canvas dans les options Entrée de Canvas.
- Les utilisateurs actuellement dans un Canvas, mais n’ayant pas atteint les points en cas d’ajouts de nouvelles étapes, seront éligibles pour recevoir ces nouvelles étapes. 
- Vous ne pouvez pas modifier ou supprimer des connexions existantes ni insérer une étape entre des étapes existantes reliées une fois qu’un Canvas est lancé.
- Si vous mettez à jour les options **Délai** ou **Fenêtre** pour une étape, seuls les nouveaux utilisateurs accédant au Canvas et les utilisateurs n’ayant pas été mis en file d’attente pour cette étape recevront les messages une fois le délai mis à jour.
- Si une étape de délai est la dernière étape du Canvas, les utilisateurs atteignant cette étape sont automatiquement sortis du Canvas et ne recevront plus les étapes créées. 

{% alert note %}
L’arrêt d’un Canvas n’entraînera pas la suppression des utilisateurs en attente de messages. Si vous activez à nouveau le Canvas et que des utilisateurs attendent toujours le message, ils le recevront (à moins que le délai dont ils disposent pour l’envoi du message soit écoulé).
{% endalert %}

## Conditions initiales

Le tableau suivant décrit les éléments pouvant être modifiés et ceux qui ne peuvent pas l’être après le lancement d’un Canvas.

| **Modifiable**                     | **Non modifiable**  |
|----------------------------------|-------------------|
| Nom et description du Canvas      | Événements de conversion |
| Teams et Tags                   |                   |
| Type d’entrée                       |                   |
| Planification d’entrée                   |                   |
| Contrôles d’entrée                   |                   |
| Statut d’abonnement              |                   |
| Limitation du taux                    |                   |
| Limite de fréquence                |                   |
| Heures calmes                      |                   |
| Audience cible                  |                   |
{: .reset-td-br-1 .reset-td-br-2}

## Graphique de Canvas

Le tableau suivant décrit les aspects d’un Canvas pouvant être modifiés et ceux qui ne peuvent pas l’être après le lancement.

| **Modifiable**                                   | **Non modifiable**     |
|------------------------------------------------|----------------------|
| Arrêt/Reprise de l’exécution de toutes les étapes de Canvas    | Suppression d’étapes       |
| Insertion d’étapes de Canvas                            | Suppression de variantes    |
| Ajouter de nouvelles connexions                            | Suppression de connexions |
| Ajouter de nouvelles variantes                               |                      |
| Répartition de variante*                          |                      |
{: .reset-td-br-1 .reset-td-br-2}

_*La répartition de variante de contrôle peut être uniquement réduite après le lancement._

## Étape individuelle

Le tableau suivant décrit les détails d’étapes individuelles de Canvas pouvant être modifiés et ceux qui ne peuvent pas l’être après le lancement.

| **Modifiable**                        | **Non modifiable**                             |
|-------------------------------------|----------------------------------------------|
| Nom                                | Type de planification (passer de délai à déclencheur) |
| Contenu du message                     | Pourcentages de contrôle                          |
| Plateformes de message d’étape (ajouter/supprimer) |                                              |
| Déclencheurs                            |                                              |
| Public                            |                                              |
| Événements d’exception                    |                                              |
| Délais/Fenêtres                    |                                              |
{: .reset-td-br-1 .reset-td-br-2}

## Pourcentages Canvas Variant

Dans Canvas, si un pourcentage de variante est modifié, vous pouvez voir que les utilisateurs peuvent être répartis sur d’autres variantes.

Initialement, une variante spécifique est affectée de manière aléatoire aux utilisateurs, avant qu’ils reçoivent une campagne pour la première fois. À partir de ce moment-là, à chaque réception de campagne (ou lorsque l’utilisateur entre à nouveau une Canvas Variant), ils recevront la même variante à moins que les pourcentages de variante soient modifiés.

Si les pourcentages de variante changent, les utilisateurs peuvent être répartis sur d’autres variantes. Les utilisateurs restent dans ces variantes jusqu’à ce que les pourcentages soient à nouveau modifiés. Notez que pour des Canvas utilisant un raccord aux filtres `NOT` avec des numéros de compartiment aléatoires, il est possible que les utilisateurs ne reçoivent pas la même branche chaque fois dans leur parcours utilisateur lorsqu’ils accèdent à nouveau au Canvas.

### Groupes de contrôles

Les groupes de contrôles restent uniformes si le pourcentage de variantes est inchangé. Les utilisateurs ayant précédemment reçu des messages ne peuvent pas accéder à un groupe de contrôle lors d’un envoi ultérieur, tout comme un utilisateur du groupe de contrôle ne peut recevoir un message.

## Heure locale d’envoi

L’heure locale d’envoi Canvas peut être modifiée jusqu’à 24 heures avant l’heure d’envoi planifiée. On appelle cette fenêtre « Zone sécurisée ». Notez que si vous prévoyez d’apporter des modifications à votre Canvas, nécessitant la création intégrale d’un Canvas, vous devez exclure les utilisateurs qui ont reçu le premier Canvas et ajuster à nouveau les heures de planification de Canvas pour permettre l’envoi pour le fuseau horaire.
