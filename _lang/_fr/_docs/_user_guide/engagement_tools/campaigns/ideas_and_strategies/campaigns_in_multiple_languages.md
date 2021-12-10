---
nav_title: Campagnes en plusieurs langues
article_title: Campagnes en plusieurs langues
page_order: 4
page_type: tutoriel
description: "Cet article pratique vous guidera dans la façon d'envoyer des messages en différentes langues depuis les campagnes du tableau de bord de Braze."
tool: Campagnes
---

# Campagnes en plusieurs langues

> Cet article sur la façon d'envoyer des messages en différentes langues à partir des campagnes du tableau de bord de Braze. <br> <br> Être en mesure de livrer des messages en plusieurs langues permet aux utilisateurs d'interagir et d'atteindre leurs clients de manière vraiment personnalisée.

Braze vous permet d'envoyer des messages dans différentes langues depuis notre tableau de bord. Lors de la composition d'une campagne, notre fonction de template de langue vous permet de créer facilement un message qui apparaît dans différentes langues selon les paramètres du téléphone de l'utilisateur.

Voici comment configurer un message dans plusieurs langues :

## Étape 1 : Opt-in de la fonctionnalité

Lors de la rédaction de votre campagne, cliquez sur **Ajouter des langues**.

!\[Ajouter des langues\]\[1\]{: style="max-width:60%;" }

## Étape 2 : Sélectionnez les langues

Sélectionnez les langues dans lesquelles votre message sera envoyé. Les sélections proposées dans le menu déroulant seront toutes les langues que vos utilisateurs ont actuellement. Braze suit automatiquement la langue dans les paramètres de l'appareil des utilisateurs et inclut cette information dans le profil de chaque utilisateur. Après avoir sélectionné vos langues, la zone de texte du snippet sera modifiée pour mettre en vedette un modèle que vous pouvez copier et coller dans le contenu de votre message. Ce modèle utilise la [logique conditionnelle][3] pour gérer plusieurs langues dans une seule campagne.

!\[Select Languages\]\[2\]

## Étape 3: Sélectionnez les champs

Sélectionnez les champs que vous souhaitez afficher dans différentes langues. Ces champs seront différents en fonction du canal de message :

- E-mail: Sujet et Corps
- Push Android : Message, titre, texte sommaire, son et URL personnalisée
- Push iOS : Message, son et URL personnalisée
- Message In-App : Message
- Push universel Windows : Texte 1, Texte 2, Texte 3, et Nom de l'image

De plus, un avertissement s'affichera si vous avez déjà entré du contenu dans l'un des champs sélectionnés. Vous pouvez choisir de remplacer le contenu existant par le texte modèle ou d'insérer le texte modèle après le texte existant.

!\[Select Fields\]\[4\]

## Étape 4: Insérer des champs

En utilisant les boutons en bas de la boîte de dialogue, choisissez comment vous souhaitez insérer le texte du modèle dans le compositeur de messages. Ou copiez et collez le modèle à l'emplacement souhaité.

## Étape 5 : Ajouter des variations de langue

Après l'insertion de votre texte gabarit dans les champs souhaités, tapez différentes variations pour chaque langue. Pour chaque champ où il y a un modèle, vous devez entrer les variations après le segment entre parenthèses. La variation doit correspondre au code de langue référencé dans les crochets précédents. Par exemple, dans le corps du message, cela peut ressembler à :

{% raw %}

```liquid
{% if ${language} == 'en' %}
Bonjour !
{% elsif ${language} == 'fr' %}
Bonjour!
{% else %}
Bonjour !
{% endif %}
```

Dans le titre d'une poussée Android, cela peut ressembler à :

```liquid
{% if ${language} == 'en' %}Hello!{% elsif ${language} == 'fr' %}Bonjour!{% else %}Hello!{% endif %}
```

Le texte que vous entrez après `{% else %}` s'affichera aux utilisateurs qui :

- Ayez une langue qui n'a pas été sélectionnée à l'étape 2.
- Ayez une langue qui n'est pas prise en charge par le Brésil. Braze prend en charge les langues représentées par les codes à deux lettres ISO 639-1, ainsi que quelques autres langues qui ne sont pas incluses dans cet ensemble. Pour une liste complète, consultez notre [page de traduction iOS][8].
- Avoir un appareil où la langue n'est pas détectable. (C'est très peu probable).

Une meilleure pratique est d'entrer du texte ici que vous pensez que vos utilisateurs sont le plus susceptibles de comprendre. Pour assurer une livraison fluide, vous devez toujours entrer le contenu après `{% else %}`.

{% endraw %}

Tout ce qui est entré en dehors du bloc de gabarit se comportera comme du contenu normal et sera affiché pour tous les utilisateurs.

!\[Type Variations\]\[6\]

## Étape 6: Prévisualiser le message

Cliquez sur le bouton Aperçu personnalisé et entrez l'ID ou l'e-mail d'un utilisateur pour voir comment le message apparaîtrait, en fonction de leur langue. De plus, vous serez en mesure de voir à quoi ressemble votre message dans son ensemble et de décider si vous souhaitez ajouter des langues à plus de champs que ceux que vous aviez précédemment choisis.

!\[Prévisualiser le message\]\[7\]

## Étape 7 : Terminer la campagne

Continuez à travers les étapes restantes de la création du message. Cela inclut la fin de la rédaction du message (par exemple, la modification des paramètres avancés).
[1]: {% image_buster /assets/img_archive/languages_1.png %} [2]: {% image_buster /assets/img_archive/languages_2.png %} [4]: {% image_buster /assets/img_archive/languages_3. ng %} [6]: {% image_buster /assets/img_archive/languages_5.png %} [7]: {% image_buster /assets/img_archive/languages_6.png %}

[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/localization/