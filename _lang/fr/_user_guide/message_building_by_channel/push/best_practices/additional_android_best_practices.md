---
nav_title: Bonnes pratiques de notification push Android
article_title: Bonnes pratiques de notification push Android
page_order: 0
page_type: reference
description: "Le présent article couvre des bonnes pratiques supplémentaires concernant les messages de notification push Android, y compris la priorité, la catégorie et la visibilité."
channel: push
platform: Android

---

# Bonnes pratiques de notification push Android

## Priorité de notification push Android

Les notifications push Android permettent de dicter la localisation de l’affichage des notifications par rapport à celles des autres applications. Lors de la composition du message pour votre campagne de notification push, sélectionnez **Notification Display Priority** (Priorité d’affichage de notification) dans l’onglet **Settings** (Paramètres) pour définir une priorité pour votre notification.

![][41]

Les options fournies correspondent à différentes priorités selon lesquelles la notification s’affiche si un utilisateur destinataire a plusieurs notifications. Une explication plus approfondie de la priorité des notifications push Android et de ses options est disponible [ici][40].

## Catégorie de notification push Android

Les notifications push Android permettent de spécifier si votre notification tombe dans une catégorie prédéfinie. L’IU du système Android peut utiliser cette catégorie pour prendre des décisions de classement ou de filtrage concernant la localisation de la notification dans la zone de notification de l’utilisateur.

![Onglet Settings (Paramètres) avec la catégorie définie sur None (Aucun), qui est le paramètre par défaut.][52]

| Catégorie | Description |
|---|-------|
| Aucun | Option par défaut. |
| Alarme | Alarme ou minuterie. |
| Appel | Appel entrant (voix ou vidéo) ou demande de communication synchrone similaire. |
| E-mail | Message groupé asynchrone (e-mail). |
| Erreur | Erreur dans l’opération en arrière-plan ou du statut d’authentification. |
| Événement | Événements du calendrier. |
| Message | Message direct entrant (SMS, message instantané, etc.). |
| Progression | Progression d’une opération de longue durée en arrière plan. |
| Promotion | Promotion ou publicité. |
| Recommandation | Une recommandation spécifique et opportune pour une seule chose. |
| Rappel | Rappel planifié par l’utilisateur. |
| Service | Indication de l’exécution du service en arrière plan. |
| Social | Réseau social ou mise à jour de partage. |
| Statut | Informations continues sur l’appareil ou le statut contextuel. |
| Système | Mise à jour du statut du système ou de l’appareil. Réservé à l’utilisation par le système. |
| Transport | Contrôle du transport des médias pour la réécoute. |
{: .reset-td-br-1 .reset-td-br-2}

## Visibilité de la notification push Android

Les notifications push Android fournissent un champ facultatif pour déterminer comment une notification apparaît sur l’écran de verrouillage de l’utilisateur. Reportez-vous au tableau suivant pour des options de visibilité ainsi que des descriptions.

| Visibilité | Description |
|---|-----|
| Publique | La notification apparaît sur l’écran de verrouillage |
| Privée | La notification est affichée avec le message « Contenu masqué » |
| Secrète | La notification n’est pas affichée sur l’écran de verrouillage |
{: .reset-td-br-1 .reset-td-br-2}

De plus, les utilisateurs d’Android peuvent modifier la façon dont les notifications push apparaissent sur leur écran de verrouillage en changeant le paramètre de confidentialité des notifications sur leur appareil. Ce paramètre remplacera la visibilité de la notification push.

![L’emplacement de la priorité de la notification push sur le tableau de bord avec « Set Visibility » (Définir la visibilité) activé et défini sur Privé.][53]{: style="float:right;max-width:60%;margin-left:15px;"}

Quelle que soit la visibilité, toutes les notifications seront affichées sur l’écran de verrouillage de l’utilisateur si le paramètre de confidentialité de notification sur leur appareil est défini sur **Show all content** (Afficher tout le contenu) qui est le paramètre par défaut. De même, les notifications ne seront pas affichées sur leur écran de verrouillage si leur confidentialité de notification est définie sur **Do not show notifications** (Ne pas afficher les notifications). La visibilité n’a d’effet que si la confidentialité de notification est définie sur **Hide sensitive content** (Masquer le contenu sensible).

La visibilité n’a aucun effet sur les appareils antérieurs à Android Lollipop 5.0.0, ce qui signifie que toutes les notifications seront affichées sur ces périphériques.

Reportez-vous à notre [documentation Android][51] pour plus d’informations.

[40]: https://www.braze.com/blog/breakdown-android-lollipops-new-notification-priorities-push-flexibility/
[41]: {% image_buster /assets/img_archive/braze_default.png %}
[46]:{% image_buster /assets/img_archive/Push_Window8_Toast.png %}
[47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %}
[51]: https://developer.android.com/guide/topics/ui/notifiers/notifications
[52]: {% image_buster /assets/img_archive/braze_category.png %}
[53]: {% image_buster /assets/img_archive/braze_visibility.png %}
