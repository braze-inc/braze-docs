---
nav_title: Messages de droite à gauche
article_title: Créer des messages de droite à gauche
page_order: 1
page_type: reference
description: "Cette page présente les meilleures pratiques pour l'envoi de messages dans Braze qui se lisent de droite à gauche."
---

# Création d'envois de messages de droite à gauche

> L'aspect final des messages de droite à gauche dépend en grande partie de la manière dont les fournisseurs de services (tels qu'Apple, Android et Google) les restituent. Cette page présente les meilleures pratiques pour rédiger des messages de droite à gauche afin que vos messages s'affichent avec le plus de précision possible.

## L'envoi de messages

Lorsque vous créez un message de droite à gauche, gardez à l'esprit les points suivants :

- **Tableau de bord de Braze :** Lorsqu'un message s'affiche sur l'appareil d'un utilisateur, son apparence est largement déterminée par le système d'exploitation et les paramètres linguistiques de l'appareil, ce qui signifie que ce que vous voyez dans le tableau de bord n'est pas toujours exact à 100 %.
- **Apparition sur l'appareil :** Apple et Android exercent un contrôle important sur la manière dont les messages sont rendus, tandis que les fournisseurs de services d'e-mailing (ESP) ont un certain contrôle. La personnalisation des e-mails HTML dans Braze peut être plus flexible ; cependant, le même message peut toujours s'afficher différemment sur différents appareils en fonction des paramètres de l'utilisateur.

En outre, vérifiez la ponctuation et les emojis pour déterminer si votre message est rendu de manière standard ou de droite à gauche.

| Rendu occidental standard | Rendu de droite à gauche |
|------------------|------------------------|
| Affiche le point d'exclamation et l'emoji à la **fin** des phrases. | Affiche le point d'exclamation et l'emoji au **début de** la phrase. |
| ![Exemple d'un message standard de droite à gauche.]({% image_buster /assets/img/right-to-left/standard.png %}) | ![Exemple d'envoi de messages de gauche à droite.]({% image_buster /assets/img/right-to-left/right-to-left.png %}) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Créer un message de droite à gauche

Pour créer votre message de droite à gauche dans Braze :

1. Rédigez votre message standard dans l'éditeur de Braze.
2. Copiez le texte du message depuis Braze, puis utilisez un outil de communication individualisée pour le convertir en un message de droite à gauche.
3. Collez votre message converti dans Braze.
4. Vérifiez la mise en forme et l'alignement du texte. Si vous créez un message e-mail glisser-déposer ou HTML, vous pouvez le faire dans le compositeur. Sinon, vous devrez utiliser un autre traitement de texte.<br><br>![Menu de l'éditeur par glisser-déposer de l'e-mail avec bouton permettant de basculer l'alignement du texte de droite à gauche ou de gauche à droite.]({% image_buster /assets/img/rtl_button.png %}){: style="max-width:50%;"}

## Considérations
 
### Notifications push longues

La méthode du copier-coller pour les messages push peut s'avérer difficile à utiliser avec des notifications push plus longues, car un contenu plus long peut s'afficher sur plusieurs lignes sur un appareil mobile. Si vous copiez le texte de votre message en dehors de Braze (par exemple dans un document Word) et que vous le collez directement dans Braze, l'alignement des phrases et l'emplacement des mots peuvent changer. Pour éviter ce scénario, copiez et collez en plusieurs fois et ajoutez un saut de ligne. Par exemple, copiez et collez les cinq premiers mots, ajoutez un saut de ligne, copiez les cinq mots suivants, ajoutez un saut de ligne, etc.

Les fonctions de prévisualisation et de test sont créées pour les messages allant de gauche à droite. Les messages allant de droite à gauche ne s'afficheront donc pas correctement dans la section de **prévisualisation et de test**, mais s'afficheront correctement sur les appareils des utilisateurs si leurs paramètres sont configurés à cet effet. Nous vous conseillons de vous envoyer des messages dans un environnement en ligne/en production/instantané pour confirmer qu'ils s'affichent correctement en fonction des paramètres de l'appareil.

### Texte bidirectionnel

De nombreux utilisateurs qui écrivent dans des langues allant de droite à gauche utilisent en fait un texte bidirectionnel : une combinaison de langues allant de gauche à droite et de droite à gauche. Par exemple, un marketeur peut envoyer un message en hébreu avec un nom de société en anglais. Braze ne peut pas gérer le formatage du texte bidirectionnel. Pour éviter les problèmes de formatage, vous pouvez soit éviter complètement le texte bidirectionnel, soit séparer le texte de gauche à droite du texte de droite à gauche à l'aide de sauts de ligne. 

{% alert tip %}
Une mise en forme correcte du texte bidirectionnel est particulièrement importante lorsque vous rédigez des messages contenant des codes promotionnels ; les codes promotionnels sont souvent présentés de gauche à droite parce que les mêmes codes peuvent être utilisés sur plusieurs marchés. Pour les codes promo, vous pouvez soit utiliser une image pour le code promo, soit ajouter le code promo à la fin du message après un saut de ligne.
{% endalert %}

### Caractères spéciaux, chiffres et émojis

Les caractères spéciaux (tels que la ponctuation, les symboles mathématiques et les devises), les chiffres, les puces et les émojis peuvent "sauter" lors de l'envoi de messages de droite à gauche dans Braze. Pour contourner ce problème, rédigez votre copie avec une mise en forme correcte dans un traitement de texte externe, puis collez la copie dans Braze. Il peut également être utile d'éviter de placer les emojis au début de votre texte et de les séparer (ainsi que les caractères spéciaux et les chiffres) du texte par des sauts de ligne afin d'éviter les problèmes d'alignement.

### Envois de messages en arabe

Lorsque vous rédigez des messages en arabe, utilisez des tailles de caractères nettement plus élevées pour obtenir la même lisibilité qu'avec d'autres langues. Nous vous conseillons d'utiliser une taille de police supérieure d'environ 20 % à votre taille habituelle pour les langues utilisant l'alphabet latin ou romain. En effet, les polices de caractères arabes sont réduites pour tenir compte de l'espace vertical occupé par les diacritiques (marques d'accent).
