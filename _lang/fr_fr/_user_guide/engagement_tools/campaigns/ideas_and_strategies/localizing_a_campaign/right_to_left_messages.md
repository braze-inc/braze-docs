---
nav\_title : Messages de droite à gauche article\_title : Création de messages de droite à gauche page\_order : 1 page\_type : référence description : "Cette page couvre les meilleures pratiques pour rédiger des messages dans Braze qui se lisent de droite à gauche."
---

# Création d'envois de messages de droite à gauche

> L'aspect final des messages de droite à gauche dépend en grande partie de la manière dont les fournisseurs de services (tels qu'Apple, Android et Google) les restituent. Cette page présente les meilleures pratiques pour rédiger des messages de droite à gauche afin que vos messages s'affichent avec le plus de précision possible.

## Fonctionnement

Il y a trois domaines clés à prendre en compte lors de la création d'un message de droite à gauche : - La façon dont le message apparaît dans votre tableau de bord de Braze - La façon dont le message apparaît lors de sa réception/distribution - Ce qui se passe entre la création et la réception/distribution.

Lorsqu'un message apparaît sur l'appareil d'un utilisateur, son aspect est largement déterminé par la manière dont les fournisseurs (comme Apple et Microsoft) le traitent, qui dépend des paramètres linguistiques de l'appareil. Par exemple, un message en arabe aura un aspect différent si l'appareil est réglé sur l'anglais au lieu de l'arabe. 

Apple et Android exercent un contrôle important sur la manière dont les messages sont rendus, tandis que les fournisseurs de services d'e-mailing (ESP) ont un certain contrôle. La personnalisation des e-mails HTML dans Braze peut être plus flexible ; cependant, le même message peut toujours s'afficher différemment sur différents appareils en fonction des paramètres de l'utilisateur.

Bien que Braze n'ait qu'un contrôle limité sur l'aspect final des envois de droite à gauche, notre objectif est de faciliter autant que possible l'obtention de résultats exacts. Utilisez les conseils et astuces suivants pour vous guider dans la création d'envois de messages de droite à gauche.

## Créer un message de droite à gauche

La manière la plus courante d'élaborer des messages de droite à gauche dans Braze est la suivante :

1. Créez un message de gauche à droite dans un éditeur Braze.
2. Copiez le texte du message depuis Braze, puis utilisez un outil de communication individualisée pour le localiser et en faire un message de droite à gauche.
3. Confirmez que l'alignement est correctement formaté en utilisant un traitement de texte (tel que Word).
- Vous pouvez sauter cette étape si vous créez un message e-mail par glisser-déposer ou en HTML. L'éditeur par glisser-déposer vous permet de changer la direction du texte en sélectionnant un bouton, et l'éditeur HTML vous permet de personnaliser l'alignement de droite à gauche. <br><br>\![Menu de l'éditeur par glisser-déposer avec bouton pour basculer l'alignement du texte de droite à gauche et de gauche à droite.]\[1]{ : style="max-width:50% ;"}

{ : start="4"} 4. Collez le texte formaté dans Braze.

### Comparaison des messages de gauche à droite et de gauche à droite

La ponctuation permet souvent de savoir si les paramètres de droite à gauche sont corrects. Dans l'image de gauche, le point d'exclamation et l'emoji se trouvent à droite du texte, ce qui correspond au début de la phrase dans les langues allant de droite à gauche. Dans l'image de droite, formatée de droite à gauche, le message affiche correctement les points d'exclamation et l'emoji à la fin des phrases.

Comparaison de deux messages en arabe pour montrer comment apparaissent les messages de droite à gauche et de gauche à droite]\[2].

## Considérations particulières pour les envois de messages de droite à gauche
 
### Notifications push longues

La méthode du copier-coller pour les messages push peut s'avérer difficile à utiliser avec des notifications push plus longues, car un contenu plus long peut s'afficher sur plusieurs lignes sur un appareil mobile. Si vous copiez le texte de votre message en dehors de Braze (par exemple dans un document Word) et que vous le collez directement dans Braze, l'alignement des phrases et l'emplacement des mots peuvent changer. Pour éviter ce scénario, copiez et collez en plusieurs fois et ajoutez un saut de ligne. Par exemple, copiez et collez les cinq premiers mots, ajoutez un saut de ligne, copiez les cinq mots suivants, ajoutez un saut de ligne, etc.

Les fonctions de prévisualisation et de test sont créées pour les messages allant de gauche à droite. Les messages allant de droite à gauche ne s'afficheront donc pas correctement dans la section de **prévisualisation et de test**, mais s'afficheront correctement sur les appareils des utilisateurs si leurs paramètres sont configurés à cet effet. Nous vous conseillons de vous envoyer des messages dans un environnement en ligne/en production/instantané pour confirmer qu'ils s'affichent correctement en fonction des paramètres de l'appareil.

### Texte bidirectionnel

De nombreux utilisateurs qui écrivent dans des langues allant de droite à gauche utilisent en fait un texte bidirectionnel : une combinaison de langues allant de gauche à droite et de droite à gauche. Par exemple, un marketeur peut envoyer un message en hébreu avec un nom de société en anglais. Braze ne peut pas gérer le formatage du texte bidirectionnel. Pour éviter les problèmes de formatage, vous pouvez soit éviter complètement le texte bidirectionnel, soit séparer le texte de gauche à droite du texte de droite à gauche à l'aide de sauts de ligne. 

{% alert tip %} Une mise en forme correcte du texte bidirectionnel est particulièrement importante lorsque vous rédigez des messages contenant des codes promotionnels ; les codes promotionnels sont souvent présentés de gauche à droite car les mêmes codes peuvent être utilisés sur plusieurs marchés. Pour les codes promo, vous pouvez soit utiliser une image pour le code promo, soit ajouter le code promo à la fin du message après un saut de ligne. {% endalert %}

### Caractères spéciaux, chiffres et émojis

Les caractères spéciaux (tels que la ponctuation, les symboles mathématiques et les devises), les chiffres, les puces et les émojis peuvent "sauter" lors de l'envoi de messages de droite à gauche dans Braze. Pour contourner ce problème, rédigez votre copie avec une mise en forme correcte dans un traitement de texte externe, puis collez la copie dans Braze. Il peut également être utile d'éviter de placer les emojis au début de votre texte et de les séparer (ainsi que les caractères spéciaux et les chiffres) du texte par des sauts de ligne afin d'éviter les problèmes d'alignement.

### Envois de messages en arabe

Lorsque vous rédigez des messages en arabe, utilisez des tailles de caractères nettement plus élevées pour obtenir la même lisibilité qu'avec d'autres langues. Nous vous conseillons d'utiliser une taille de police supérieure d'environ 20 % à votre taille habituelle pour les langues utilisant l'alphabet latin ou romain. En effet, les polices de caractères arabes sont réduites pour tenir compte de l'espace vertical occupé par les diacritiques (marques d'accent).

\[1] : {% image\_buster /assets/img/rtl\_button.png %} \[2] : {% image\_buster /assets/img/rtl\_comparison.png %}