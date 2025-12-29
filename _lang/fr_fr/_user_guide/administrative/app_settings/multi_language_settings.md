---
nav_title: Paramètres multilingues
article_title: Paramètres multilingues
alias: "/multi_language_support/"
page_order: 5.5
description: "Cet article donne un aperçu des paramètres multilingues du tableau de bord de Braze et explique comment utiliser les locales dans vos messages."
---

# Paramètres multilingues

> En ajustant les paramètres multilingues, vous pouvez cibler les utilisateurs dans différentes langues et emplacements avec des messages différents, le tout dans un seul et même e-mail.

## Conditions préalables

Pour modifier et gérer la prise en charge multilingue, vous devez disposer du droit d'utilisateur "Gérer les paramètres multilingues". Pour ajouter les paramètres linguistiques à un message, vous devez disposer des autorisations nécessaires pour modifier les campagnes.

{% alert important %}
La prise en charge du multilinguisme est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

## Ajouter une locale

1. Allez dans **Paramètres** > **Prise en charge multilingue** sous **Paramètres de l'espace de travail**.
2. Sélectionnez **Ajouter des paramètres linguistiques**, puis sélectionnez **Paramètres linguistiques par défaut** ou **Attributs personnalisés**.<br><br>\![La liste déroulante "Add locale" avec des options pour sélectionner les paramètres linguistiques par défaut ou des attributs personnalisés.]({% image_buster /assets/img/multi-language_support/add_locale_options.png %}){: style="max-width:40%;"}
3. Saisissez un nom pour les paramètres régionaux.
4. Sélectionnez les attributs de l'utilisateur correspondant à l'option locale que vous avez choisie.

{% tabs %}
{% tab Default locale %}

Pour la rubrique **Localité par défaut**, utilisez les menus déroulants pour sélectionner la langue à ajouter et, éventuellement, le pays à associer à la langue.<br><br>\![Une fenêtre intitulée "Add locale - Default Language and Country" pour spécifier la langue et le pays.]({% image_buster /assets/img/multi-language_support/default_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Custom attributes %}

Pour les **attributs personnalisés**, utilisez le menu déroulant pour sélectionner l'attribut personnalisé associé et dans le champ de texte, saisissez la valeur.<br><br>\![Une fenêtre intitulée "Add locale - Custom Attributes" pour spécifier l'attribut personnalisé et la valeur.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

{: start="5"}
5\. Sélectionnez **Ajouter un paramètre local**. 

Pour connaître les étapes de l'utilisation de ces langues dans vos campagnes d'e-mail et dans Canvas, reportez-vous à la section [Utilisation des langues]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/).

## Considérations

- Lors de la configuration d'une locale, vous pouvez sélectionner des langues à partir des attributs utilisateur par défaut ou des attributs personnalisés. Vous ne pouvez pas choisir entre les deux.
- Vous pouvez sélectionner jusqu'à deux attributs personnalisés dans une même locale, ou jusqu'à deux langues d'attribut par défaut. Dans les deux cas, le deuxième attribut est facultatif.
- Lorsque vous modifiez les valeurs traduites dans le fichier CSV, évitez de modifier les valeurs par défaut du fichier.
- La clé locale de votre fichier téléchargé doit correspondre à celle de vos paramètres multilingues.

### Soutien et hiérarchisation

- Les utilisateurs qui correspondent à un attribut personnalisé locale sont prioritaires par rapport aux utilisateurs qui correspondent à un attribut par défaut.
- La prise en charge des attributs personnalisés est limitée aux chaînes de caractères et à la clé de comparaison `equals`.
- Si un attribut personnalisé est supprimé ou si son type est modifié, l'utilisateur ne peut plus appartenir à cette locale et descendra dans la liste prioritaire des locales dont il relève ou recevra des traductions marketing par défaut.
- Si une locale n'est pas valide (l'attribut personnalisé a changé ou est supprimé), l'erreur apparaîtra sur la page **Support multilingue**.

## Questions fréquemment posées

#### Combien de localités puis-je ajouter ?

Vous pouvez ajouter jusqu'à 200 localités.

#### Où sont stockés les fichiers de traduction dans Braze ?

Les fichiers de traduction sont stockés au niveau d'une campagne, ce qui signifie que chaque variante de message doit avoir des traductions téléchargées.

#### Le nom de la locale doit-il suivre un modèle ou un format spécifique ?

Non. Vous pouvez utiliser la convention de dénomination de votre choix. Le nom de la locale est utilisé lors de la sélection de la locale dans l'éditeur et figurera dans les titres du fichier que vous téléchargez avec les ID de traduction.

