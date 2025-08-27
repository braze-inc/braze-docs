---
nav_title: Paramètres multilingues
article_title: Paramètres multilingues
alias: "/multi_language_support/"
page_order: 5.5
description: "Cet article donne un aperçu des paramètres multilingues du tableau de bord de Braze et explique comment utiliser les paramètres régionaux dans vos messages."
---

# Paramètres multilingues

> En ajustant les paramètres multilingues, vous pouvez cibler les utilisateurs dans différentes langues et emplacements avec des messages différents dans un seul e-mail.

## Conditions préalables

Pour modifier et gérer la prise en charge multilingue, vous devez disposer de l’autorisation « Gérer les paramètres multilingues ». Pour ajouter le paramètre régional à un message, vous devez disposer des autorisations nécessaires pour modifier les campagnes.

{% alert important %}
La prise en charge du multilinguisme est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

## Ajouter un paramètre régional

1. Allez dans **Paramètres** > **Prise en charge multilingue** sous **Paramètres de l'espace de travail**.
2. Sélectionnez **Ajouter des paramètres régionaux**, puis sélectionnez **Paramètres régionaux par défaut** ou **Attributs personnalisés**.<br><br>![Le menu déroulant "Ajouter un paramètre local" permet de sélectionner le paramètre local par défaut ou des attributs personnalisés.]({% image_buster /assets/img/multi-language_support/add_locale_options.png %}){: style="max-width:40%;"}
3. Saisissez un nom pour le paramètre régional.
4. Sélectionnez les attributs de l'utilisateur correspondant à l'option locale que vous avez choisie.

{% tabs %}
{% tab Paramètres régionaux par défaut %}

Pour les **Paramètres régionaux par défaut**, utilisez les menus déroulants pour sélectionner la langue à ajouter et, éventuellement, le pays à associer à la langue.<br><br>![Une fenêtre intitulée "Ajouter des paramètres régionaux - Langue et pays par défaut" permet de spécifier la langue et le pays.]({% image_buster /assets/img/multi-language_support/default_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Attributs personnalisés %}

Pour les **attributs personnalisés**, utilisez le menu déroulant pour sélectionner l'attribut personnalisé associé et dans le champ de texte, saisissez la valeur.<br><br>![Une fenêtre intitulée "Ajouter des paramètres régionaux - Attributs personnalisés" permet de spécifier l'attribut personnalisé et sa valeur.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

{: start="5"}
5\. Sélectionnez **Ajouter des paramètres régionaux**. 

Pour connaître les étapes de l'utilisation de ces langues dans vos campagnes d'e-mail et dans Canvas, reportez-vous à la section [Utilisation des langues locales]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/).

## Considérations

- Lors de la configuration de paramètres régionaux, vous pouvez sélectionner des langues à partir des attributs utilisateur par défaut ou des attributs personnalisés. Vous ne pouvez pas choisir depuis les deux sources.
- Vous pouvez sélectionner jusqu'à deux attributs personnalisés pour un même paramètre régional, ou jusqu'à deux langues d'attribut utilisatuer par défaut. Dans les deux cas, le deuxième attribut est facultatif.
- Lorsque vous modifiez les valeurs traduites dans le fichier CSV, évitez de modifier les valeurs par défaut du fichier.
- La clé locale de votre fichier téléchargé doit correspondre à celle de vos paramètres multilingues.

### Assistance et hiérarchisation

- Les utilisateurs qui correspondent à des paramètres régionaux personnalisés sont prioritaires par rapport aux utilisateurs qui correspondent à un attribut par défaut.
- La prise en charge des attributs personnalisés est limitée aux chaînes de caractères et à la clé de comparaison `equals`.
- Si un attribut personnalisé est supprimé ou si son type est modifié, l'utilisateur ne peut plus appartenir à cette locale et descendra dans la liste prioritaire des locales dont il relève ou recevra des traductions marketing par défaut.
- Si un paramètre régional n'est pas valide (l'attribut personnalisé a changé ou est supprimé), l'erreur apparaîtra sur la page **Support multilingue**.

## Foire aux questions

#### Combien de localités puis-je ajouter ?

Vous pouvez ajouter jusqu'à 200 paramètres régionaux.

#### Où sont stockés les fichiers de traduction dans Braze ?

Les fichiers de traduction sont stockés au niveau d'une campagne, ce qui signifie que des traductions doivent être chargées pour chaque variante de message.

#### Le nom de la locale doit-il suivre un modèle ou un format spécifique ?

Non. Vous pouvez utiliser la convention de dénomination de votre choix. Le nom du paramètre régional est utilisé lors de la sélection du paramètre régional dans l'éditeur et figurera dans les titres du fichier que vous téléchargez avec les ID de traduction.

