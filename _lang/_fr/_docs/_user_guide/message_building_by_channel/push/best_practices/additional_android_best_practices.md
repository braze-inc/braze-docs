---
nav_title: Meilleures pratiques pour Android Push Additionnel
article_title: Meilleures pratiques pour Android Push Additionnel
page_order: 0
page_type: Référence
description: "Cet article couvre les meilleures pratiques pour les messages push Android, y compris la priorité, la catégorie et la visibilité."
channel: Pousser
platform: Android
---

# Meilleures pratiques de poussée d'Android supplémentaires

## Priorité de push Android

Les notifications push Android fournissent l'option de dicter où les notifications sont affichées par rapport aux notifications d'autres applications.  Lorsque vous composez le message pour votre campagne de push, sélectionnez « Priorité d'affichage des notifications » dans l'onglet paramètres pour définir une priorité pour votre notification.

!\[Lieu de priorité Push du tableau de bord\]\[41\]

Les options fournies correspondent à différentes priorités avec lesquelles la notification sera affichée si un utilisateur récepteur a plusieurs notifications. Une explication plus approfondie de la priorité Push d'Android et des options de priorité peut être trouvée [ici][40].

## Catégorie de push Android

Les notifications push Android fournissent l’option de spécifier si votre notification tombe dans une catégorie prédéfinie. L'interface utilisateur du système Android peut utiliser cette catégorie pour prendre des décisions de classement ou de filtrage quant à l'endroit où placer la notification dans la barre de notification de l'utilisateur.

!\[Lieu de priorité Push du tableau de bord\]\[52\]

| Catégorie       | Libellé                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------- |
| Aucun           | Par défaut                                                                               |
| Alarm           | Alarme ou minuteur                                                                       |
| Appel           | Appel entrant (voix ou vidéo) ou demande de communication synchrone similaire            |
| Courriel        | Message asynchrone en masse (email)                                                      |
| Erreur          | Erreur lors de l'opération en arrière-plan ou du statut d'authentification               |
| Evénement       | Événement du calendrier                                                                  |
| Message         | Message direct entrant (SMS, message instantané, etc.)                                   |
| Progrès         | Progression d'une opération d'arrière-plan longue durée                                  |
| Promotion       | Promotion ou publicité                                                                   |
| Recommandation  | Une recommandation spécifique et opportune pour une seule chose                          |
| Rappel          | Rappel programmé par l'utilisateur                                                       |
| Service         | Indication du service d'arrière-plan en cours d'exécution                                |
| Réseaux sociaux | Réseau social ou mise à jour de partage                                                  |
| Statut          | Informations en cours sur l'appareil ou l'état contextuel                                |
| Système         | Mise à jour du statut du système ou du périphérique. Réservé à l'utilisation du système. |
| Transport       | Contrôle du transport des médias pour la lecture                                         |
{: .reset-td-br-1 .reset-td-br-2}


[Voir la documentation Android pour plus d'infos][51]

## Visibilité push Android

Les notifications push Android fournissent un champ facultatif pour déterminer comment une notification apparaît sur l'écran de verrouillage de l'utilisateur. Les notifications peuvent être configurées pour apparaître sur l'écran de verrouillage *(Public)*, pour apparaître avec le message "Contenu caché" *(Privé)*, ou pour être caché entièrement *(secret)*.

De plus, les utilisateurs d'Android peuvent outrepasser la façon dont les notifications apparaissent sur leur écran de verrouillage en modifiant le paramètre de confidentialité des notifications sur leur appareil. Ce paramètre remplacera la visibilité de la notification push.

!\[Dashboard Push Priority Location\]\[53\]{: style="float:right;max-width:60%;margin-left:15px;"}

Notez que indépendamment de la Visibilité, toutes les notifications seront affichées sur l'écran de verrouillage de l'utilisateur si le paramètre de confidentialité de la notification sur son appareil est *Afficher tout le contenu* (paramètre par défaut). De même, les notifications ne seront pas affichées sur leur écran de verrouillage si leur confidentialité de notification est réglée sur *Ne pas afficher les notifications*. La visibilité n'a d'effet que si leur confidentialité de notification est réglée sur *Masquer le contenu sensible*. Dans ce cas, la notification sera affichée comme suit:

* *Public* - La notification est affichée sur l'écran de verrouillage
* *Privé* - La notification est affichée avec "Contenu caché" comme le message
* *Secret* - La notification est **non** affichée sur l'écran de verrouillage

La visibilité n'a aucun effet sur les appareils antérieurs à Android Lollipop 5.0.0. Toutes les notifications seront affichées sur ces appareils.

[Voir la documentation Android pour plus d'infos][51]
[41]: {% image_buster /assets/img_archive/braze_default.png %} [46]:{% image_buster /assets/img_archive/Push_Window8_Toast.png %} [47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast. ng %} [52]: {% image_buster /assets/img_archive/braze_category.png %} [53]: {% image_buster /assets/img_archive/braze_visibility.png %}

[40]: https://www.braze.com/blog/breakdown-android-lollipops-new-notification-priorities-push-flexibility/
[51]: https://developer.android.com/guide/topics/ui/notifiers/notifications
