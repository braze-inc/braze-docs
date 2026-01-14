---
nav_title: Lignes directrices de la marque
article_title: Lignes directrices de la marque
page_order: 1
page_type: reference
description: "Cet article de référence explique comment créer, gérer et utiliser des directives de marque qui peuvent être appliquées à vos messages grâce à l'assistant de rédaction de l'intelligence artificielle."
---

# Lignes directrices de la marque

> Adaptez le style de vos textes générés par l'intelligence artificielle à la voix, au ton et à la personnalité de votre marque grâce à des directives de marque personnalisées.

Vous pouvez créer et gérer vos directives de marque en allant dans **Paramètres** > **Directives de marque.** Vous pouvez également les créer dans l'[assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines/).

## Créer des lignes directrices pour la marque

### Étape 1 : Créer une ligne directrice pour la marque

Sur la page **Lignes directrices de la marque**, sélectionnez **Créer un nouveau**. Si vous souhaitez que cette directive de marque soit la directive par défaut de l'espace de travail, cochez la case **Utiliser comme directive de marque par défaut**. Vous ne pouvez avoir qu'une seule valeur par défaut par espace de travail.

### Étape 2 : Décrivez la personnalité de votre marque

Pour la **personnalité de la marque**, réfléchissez à ce qui rend votre marque unique. Incluez les caractéristiques, les valeurs, la voix et tous les archétypes qui définissent votre marque. Voici quelques caractéristiques à prendre en compte :

| **Caractéristique**       | **Définition**                                                                       | **Exemple**                                                        |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Réputation               | Comment vous voulez que votre marque soit perçue sur le marché.                               | Nous sommes connus pour être la marque la plus fiable et la plus orientée vers le client dans notre secteur. |
| Traits de personnalité       | Caractéristiques humaines qui décrivent le caractère de votre marque.                     | Notre marque est conviviale, accessible et toujours optimiste.          |
| Valeurs                   | Les valeurs fondamentales qui guident les actions et les décisions de votre marque.                           | Nous accordons de l'importance à la durabilité, à la transparence et à la communauté.            |
| Différenciation          | Les qualités uniques qui distinguent votre marque de ses concurrents.                         | Nous nous distinguons en offrant un service personnalisé à la clientèle qui va au-delà des attentes. |
| La voix de la marque              | Le ton et le style de communication de votre marque.                                 | Notre voix est décontractée mais informative, assurant la clarté sans être trop formelle. |
| Archétype de la marque          | L'archétype qui conseille la personne de votre marque (le héros, le créateur, etc.).    | Nous incarnons l'archétype de l'explorateur, toujours à la recherche de nouveaux défis et de nouvelles aventures. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Étape 3 : Définir les termes à éviter (facultatif)

Pour les **exclusions**, énumérez tout langage ou style qui ne correspond pas à votre marque. Par exemple, vous voudrez peut-être éviter les "sarcasmes", les "attitudes négatives" ou les tons "condescendants".

La fenêtre "Créer une ligne directrice de marque" avec des champs pour saisir le nom, la description, la personnalité, les exclusions et le ton.]({% image_buster /assets/img/guidelines_create.png %})

### Étape 4 : Testez vos lignes directrices

Testez vos lignes directrices pour voir comment elles fonctionnent. Développez **Testez vos lignes directrices** pour générer des exemples de textes et ajustez-les si nécessaire.

### Étape 5 : Enregistrez vos lignes directrices

Lorsque vous êtes satisfait de vos lignes directrices, sélectionnez **Enregistrer la ligne directrice de la marque**. Vos nouvelles lignes directrices seront enregistrées dans votre espace de travail pour une utilisation ultérieure.

{% alert important %}
Vous pouvez changer la langue de sortie quelle que soit la langue de votre copie, mais ni Braze ni OpenAI ne garantissent la qualité de la traduction. Testez et vérifiez toujours les traductions avant de les utiliser.
{% endalert %}

## Gérer les lignes directrices de la marque

Vous pouvez modifier les directives de marque en les sélectionnant sur la page **Directives de marque.**  Archivez une directive de marque pour la rendre inactive et la supprimer de l'assistant de rédaction de l'intelligence artificielle. Pour la rendre à nouveau active et sélectionnable, vous pouvez filtrer les directives de marque archivées et les désarchiver.

\![La page "Brand Guidelines" a filtré les directives de marque archivées.]({% image_buster /assets/img/unarchive_brand_guideline.png %})

## Utiliser les lignes directrices de la marque

Lors de la rédaction d'un message, ouvrez l'[assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/) et sélectionnez votre directive de marque dans le menu déroulant **Appliquer la directive de marque**. Si vous désignez une ligne directrice spécifique comme ligne par défaut, elle sera automatiquement sélectionnée dans la liste déroulante, mais vous pouvez choisir une autre ligne directrice. 

!Assistant de rédaction d'intelligence artificielle avec "Alertes importantes ! !!" sélectionné comme ligne directrice de la marque.]({% image_buster /assets/img/guidelines_ai_assistant.png %})

{% multi_lang_include brazeai/generative_ai/policy.md %}
