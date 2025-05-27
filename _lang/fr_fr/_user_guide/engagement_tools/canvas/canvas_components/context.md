---
nav_title: Contexte 
article_title: Contexte 
alias: /context/
page_order: 1.5
page_type: reference
description: "Cet article de référence explique comment créer et utiliser des étapes contextuelles dans votre Canvas."
tool: Canvas

---

# Contexte

> Utilisez les étapes Contexte pour créer ou mettre à jour un ensemble de variables qui conseillent le contexte d'un utilisateur (ou des informations sur le comportement de cet utilisateur) au fur et à mesure qu'il se déplace dans un Canvas. Chaque variable de contexte comprend un nom, un type de données et une valeur qui peut inclure Liquid. En définissant le contexte dans le cadre de votre parcours utilisateur, vous pouvez par exemple retarder les messages ou filtrer les utilisateurs en fonction de variables contextuelles.

{% alert important %}
Les étapes du contexte sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

## Fonctionnement

Chaque étape du canvas est composée d'un nom de variable et d'un type de données associé, ou variables de contexte (précédemment appelées propriétés d'entrée du canvas). Ces variables suivent l'utilisateur tout au long du canvas et sont accessibles à l'aide de Liquid `context`.

![Une étape du Contexte est la première étape d'un Canvas.][1]{: style="float:right;max-width:40%;margin-left:15px;"}

Il existe deux façons de définir des variables de contexte :

- **A l'entrée de la toile :** Les variables des événements ou des appels API qui déclenchent l'entrée d'un utilisateur dans un canvas sont stockées en tant que variables de contexte.
- **Utilisation d'une étape contextuelle :** Vous pouvez créer ou mettre à jour des variables contextuelles dans l'éditeur d'étapes.

Notez que les variables incluses dans la variable de contexte ne sont pas automatiquement stockées dans le profil utilisateur.

## Création d'une étape contextuelle

Pour créer une étape contextuelle, ajoutez une étape à votre canvas. Ensuite, glissez-déposez le composant depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus au bas d'une étape et sélectionnez **Contexte**.

### Définition des variables de contexte

1. Donnez un nom à votre variable Contexte.
2. Sélectionnez un type de données.
3. Saisissez une expression liquide ou sélectionnez le bouton **Ajouter une personnalisation**. Cela génère un extrait de code Liquid à utiliser dans votre expression Liquid.
4. Sélectionnez **Aperçu** pour visualiser la variable contextuelle.
5. Sélectionnez **Terminé** pour enregistrer l'étape.

Vous pouvez utiliser les variables de contexte partout où vous pouvez utiliser Liquid, comme dans les étapes Message et Mise à jour de l'utilisateur, avec le bouton **Ajouter une personnalisation**.

## Types de variables contextuelles

Canvas Les variables contextuelles créées ou mises à jour au cours de l'étape peuvent se voir attribuer des types. Notez que si l'expression Liquid renvoie une valeur qui ne correspond pas au type, la variable contextuelle ne sera pas mise à jour.

Par exemple, si le type de données de la variable contextuelle est défini sur **Date** mais que la valeur n'est pas une date, la variable ne sera pas mise à jour. Cela signifie que les choses suivantes se produiront :

- L'utilisateur passe à l'étape suivante ou quitte le canvas s'il s'agit de la dernière étape du canvas.
- Dans votre analyse/analytique de l'étape du canvas, cela sera considéré comme *non mis à jour.*

Braze sortira un utilisateur à l'étape si :

- La variable contextuelle ne renvoie aucune valeur.
- L'appel à un contenu connecté intégré échoue.
- Les types de variables contextuelles ne correspondent pas.

### Types JSON et réponses au contenu connecté

Braze évalue les variables de contexte censées être de type JSON (ou Object) à partir des réponses du contenu connecté en chaînes de caractères. Pour éviter que les variables de contexte ne soient évaluées comme des chaînes de caractères, entrez ces résultats dans ce filtre Liquid : `as_json_string`. Voici un exemple :

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Utilisation de variables contextuelles avec des étapes de temporisation

Vous pouvez ajouter des [options de retard personnalisées]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) avec les informations de l'étape Contexte, ce qui signifie que vous pouvez sélectionner la variable qui retarde les utilisateurs.

[1]: {% image_buster /assets/img/context_step3.png %}
