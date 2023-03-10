---
nav_title: Campagnes en plusieurs langues
article_title: Campagnes en plusieurs langues
page_order: 4
page_type: tutorial
description: "Le présent article pratique vous expliquera comment envoyer des messages dans plusieurs langues au sein des campagnes."
tool: Campagnes

---

# Campagnes en plusieurs langues

> Le présent article pratique décrira comment envoyer des messages dans plusieurs langues au sein des campagnes.
> <br>
> <br>
> Être capable d’envoyer des messages en plusieurs langues permet aux utilisateurs d’interagir et d’atteindre leurs clients de manière véritablement personnalisée. 

Braze vous permet d’envoyer des messages dans différentes langues depuis notre tableau de bord. Lors de la création d’une campagne, notre fonctionnalité de modélisation de la langue vous permet de créer facilement un message qui apparaît dans différentes langues en fonction des paramètres du téléphone de l’utilisateur.

Voici comment configurer un message en plusieurs langues :

## Étape 1 : Abonnement à la fonctionnalité

Lors de la composition de votre campagne, cliquez sur **Ajouter des langues**.

![][1]{: style="max-width:60%;" }

## Étape 2 : Sélectionner les langues {#select-language}

Sélectionnez les langues dans lesquelles votre message sera envoyé. Les sélections proposées dans le menu déroulant seront toutes les langues que vos utilisateurs ont actuellement. Braze suit automatiquement la langue dans les paramètres de l’appareil des utilisateurs et inclut ces informations dans le profil de chaque utilisateur. 

Une fois que vous avez sélectionné vos langues, la boîte d’extrait de code va se modifier pour afficher un modèle que vous pouvez copier et coller dans le contenu de votre message. Ce modèle utilise la [logique conditionnelle][3] pour gérer plusieurs langues au sein d’une campagne unique.

![][2]

## Étape 3 : Sélectionner les champs

Sélectionnez les champs que vous souhaitez afficher dans différentes langues. Ces champs varient selon le canal de communication :

- E-mail : Sujet et corps
- Notification push pour Android : Message, titre, résumé du texte, son et URL personnalisée
- Notification push pour iOS : Message, son et URL personnalisée
- Message in-app : Message (éditeur HTML uniquement)

Un avertissement s’affiche si vous avez déjà saisi du contenu dans l’un des champs sélectionnés. Vous pouvez choisir de remplacer le contenu existant par le texte modélisé ou insérer le texte modélisé après le texte existant.

![][4]

## Étape 4 : Insérer des champs

En utilisant les boutons au bas de la boîte de dialogue, choisissez la façon dont vous souhaitez insérer le texte modélisé dans le composeur de message, ou copiez-collez le modèle à l’emplacement souhaité.

## Étape 5 : Ajouter des variantes de langue

Après avoir inséré votre texte modélisé dans les champs souhaités, saisissez différentes variantes pour chaque langue. Pour chaque champ pour lequel il existe une modélisation, vous devez entrer les variations après le segment entre crochets pour modélisation. La variation doit correspondre au code de langue référencé entre crochets avant lui. Par exemple, dans le corps du message, cela peut ressembler à :

{% raw %}

```liquid
{% if ${language} == 'en' %}
Hello!
{% elsif ${language} == 'fr' %}
Bonjour!
{% else %}
Hello!
{% endif %}
```

Pour le titre d’une notification push Android, cela peut ressembler à :

```liquid
{% if ${language} == 'en' %}Hello!{% elsif ${language} == 'fr' %}Bonjour!{% else %}Hello!{% endif %}
```

Le texte que vous entrez après `{% else %}` sera affiché aux utilisateurs qui :

- Ont une langue qui n’a pas été sélectionnée dans l’[étape 2](#select-language).
- Ont une langue qui n’est pas prise en charge par Braze. Braze prend en charge les langues représentées par les codes ISO 639-1 à deux lettres, ainsi que quelques autres qui n’en font pas partie. Pour obtenir une liste complète, consultez notre [Page de localisation iOS][8].
- Disposent d’un appareil pour lequel la langue est indétectable. (Cela est très peu probable).

Nous vous recommandons d’y saisir un texte que vos utilisateurs sont le plus susceptibles de comprendre selon vous. Pour assurer un envoi sans heurts, vous devez toujours saisir du contenu après `{% else %}`.

{% endraw %}

Tout ce qui est saisi en dehors du bloc de modèle se comportera comme du contenu normal et s’affichera pour tous les utilisateurs.

![][6]

## Étape 6 : Aperçu du message

Cliquez sur le bouton **Personalized Preview (Aperçu personnalisé)** et saisissez l’ID ou l’e-mail d’un utilisateur pour voir comment le message s’affiche pour cette personne, selon sa langue. Vous pourrez également voir à quoi ressemble globalement vitre message entier et décider si vous souhaitez ajouter des langues à plus de champs que ceux que vous aviez déjà choisis.

![][7]

## Étape 7 : Terminer la campagne

Effectuez les étapes restantes pour [créer votre campagne][9].

[1]: {% image_buster /assets/img_archive/languages_1.png %}
[2]: {% image_buster /assets/img_archive/languages_2.png %}
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[4]: {% image_buster /assets/img_archive/languages_3.png %}
[6]: {% image_buster /assets/img_archive/languages_5.png %}
[7]: {% image_buster /assets/img_archive/languages_6.png %}
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/localization/
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/
