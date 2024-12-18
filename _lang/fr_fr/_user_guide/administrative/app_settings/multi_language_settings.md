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

## Ajouter un paramètre régional

1. Allez dans **Paramètres** > **Prise en charge multilingue** sous **Paramètres de l'espace de travail**.
2. Sélectionnez **Ajouter un paramètre régional**.
3. Saisissez un nom pour le paramètre régional.
4. Pour les **attributs de l'utilisateur**, sélectionnez la langue à ajouter à l'aide du menu déroulant **Langue.** 
5. (facultatif) Sélectionnez le pays à associer à la langue.
6. Sélectionnez **Ajouter un paramètre régional**. 

![Exemple de français ajouté comme paramètre local pour les utilisateurs dont le pays est le Canada.][2]{: style="max-width:80%;"}

Pour connaître les étapes de l'utilisation de ces langues dans vos campagnes d'e-mail et dans Canvas, reportez-vous à la section [Utilisation des langues locales]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/).

## Foire aux questions

#### Combien de localités puis-je ajouter ?
Vous pouvez ajouter jusqu'à 200 paramètres régionaux.

#### Où sont stockés les fichiers de traduction dans Braze ?
Les fichiers de traduction sont stockés au niveau d'une campagne, ce qui signifie que des traductions doivent être chargées pour chaque variante de message.

#### Le nom de la locale doit-il suivre un modèle ou un format spécifique ?
Non. Vous pouvez utiliser la convention de dénomination de votre choix. Le nom du paramètre régional est utilisé lors de la sélection du paramètre régional dans l'éditeur et figurera dans les titres du fichier que vous téléchargez avec les ID de traduction.

#### Puis-je utiliser des attributs personnalisés pour définir une locale ?
Pas actuellement. Contactez votre gestionnaire de compte ou laissez un [commentaire sur le produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) avec plus de détails sur la façon dont vous définiriez les paramètres régionaux.

[2]: {% image_buster /assets/img/multi-language_support/add_locale.png %}
