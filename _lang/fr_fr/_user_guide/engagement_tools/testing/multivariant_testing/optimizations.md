---
nav_title: Optimisations
article_title: Optimisation des tests A/B avec une variante gagnante ou des variantes personnalisées
page_order: 1
page_type: reference
description: "Découvrez comment utiliser la variante gagnante ou la variante personnalisée lors de la création de tests multivariés et de tests A/B."
---

# Optimisation des tests A/B avec la variante gagnante ou les variantes personnalisées

Lors de la [création d'un test A/B][1] pour les campagnes e-mail, push, webhook, SMS et WhatsApp planifiées pour être envoyées une fois, vous pouvez sélectionner une optimisation. Il existe deux options d’optimisation : **Variante gagnante** et **Variante personnalisée**.

![Options d’optimisation présentées dans la section de test A/B lorsque vous choisissez votre audience cible. Trois options sont présentées : Pas d’optimisation, Variante gagnante et Variante personnalisée. La variante personnalisée est sélectionnée.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Les deux options fonctionnent en envoyant un test initial à un pourcentage de votre segment cible. Après la fin du test, les utilisateurs restants de votre audience sont envoyés soit à la variante la plus efficace (Variante gagnante) soit à la variante avec laquelle ils ont le plus de chance d’interagir (Variante personnalisée).

{% alert tip %}
Les optimisations sont situées dans l'étape **Audiences cibles** de la création de la campagne, sous **Test A/B**.
{% endalert %}

## Variante gagnante

L'envoi de la variante gagnante est similaire à un test A/B standard. Les utilisateurs de ce groupe recevront la variante gagnante lorsque le test initial sera terminé.

1. Sélectionnez **Variante gagnante**, puis indiquez quel pourcentage de l'audience de votre campagne doit être affecté au groupe Variante gagnante.
2. Configurez les paramètres supplémentaires suivants.

| Champ | Description |
| --- | --- | 
| Indicateurs d’optimisation | L’indicateur pour lequel il faut optimiser. Choisissez entre les *ouvertures uniques* ou les *clics* pour l'e-mail, les *ouvertures* pour le push, ou le *taux de conversion primaire* pour tous les canaux. Le choix du *nombre d'ouvertures* ou de *clics* pour déterminer le gagnant n'a aucune incidence sur les [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/) de la campagne. <br><br>Gardez à l'esprit que si vous utilisez un groupe de contrôle, les utilisateurs du groupe de contrôle ne peuvent pas effectuer d' *ouvertures* ou de *clics*, de sorte que les performances du groupe de contrôle sont garanties à l'adresse `0`. Par conséquent, le groupe de contrôle ne peut pas gagner le test A/B. Cependant, vous pouvez toujours utiliser un groupe de contrôle afin de suivre d’autres mesures pour les utilisateurs qui ne reçoivent pas de message. |
| Heure de départ du test d’origine | La date et l’heure du début du test d’origine. |
| Heure de fin du test d’origine | La date et l’heure de la fin du test d’origine. C'est à ce moment-là que la variante gagnante est envoyée aux utilisateurs restants.<br><br>En cas d'envoi à l'heure locale des utilisateurs ou avec le timing intelligent, la variante gagnante doit être envoyée au moins 24 heures après le test A/B pour garantir la réception/distribution à tous les utilisateurs du groupe de la variante gagnante. |
| Canal de secours | Ce qui se passe si aucune variante ne gagne par une marge statistiquement significative. Choisissez entre envoyer quand même à la variante la plus performante ou achever le test sans envoyer de messages supplémentaires. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Variante personnalisée

Utilisez des variantes personnalisées pour envoyer à chaque utilisateur de votre segmentation cible la variante avec laquelle il est le plus susceptible de s'engager.

Pour déterminer la meilleure variante pour chaque utilisateur, Braze enverra le test d’origine à une partie de votre audience cible pour chercher des associations entre les caractéristiques des utilisateurs et les préférences de message. Selon la réponse des utilisateurs à chaque variante dans le test d’origine, ces caractéristiques seront utilisées pour déterminer lesquels, parmi les utilisateurs restants, recevront chaque variante. Si aucune association n'est trouvée et qu'aucune personnalisation ne peut être effectuée, la variante gagnante est automatiquement envoyée aux utilisateurs restants. Pour en savoir plus sur la manière dont les variantes personnalisées sont déterminées, reportez-vous à la section [Analyses des tests A/B et multivariés]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#personalized-variant).

1. Sélectionnez **Variante personnalisée**, puis indiquez quel pourcentage de l'audience de votre campagne doit être affecté au groupe Variante personnalisée.
2. Configurez les paramètres supplémentaires suivants.

| Champ | Description |
| --- | --- | 
| Indicateurs d’optimisation | L’indicateur pour lequel il faut optimiser. Choisissez entre les *ouvertures uniques* ou les *clics* pour l'e-mail, les *ouvertures* pour le push, ou le *taux de conversion primaire* pour tous les canaux. Le choix du *nombre d'ouvertures* ou de *clics* pour déterminer le gagnant n'a aucune incidence sur les [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events) de la campagne. <br><br>Gardez à l'esprit que si vous utilisez un groupe de contrôle, les utilisateurs du groupe de contrôle ne peuvent pas effectuer d' *ouvertures* ou de *clics*, de sorte que les performances du groupe de contrôle sont garanties à l'adresse `0`. Par conséquent, le groupe de contrôle ne peut pas gagner le test A/B. Cependant, vous pouvez toujours utiliser un groupe de contrôle afin de suivre d’autres mesures pour les utilisateurs qui ne reçoivent pas de message. |
| Heure de départ du test d’origine | La date et l’heure du début du test d’origine. |
| Heure de fin du test d’origine | La date et l’heure de la fin du test d’origine. C'est à ce moment-là que les variantes personnalisées sont envoyées aux utilisateurs restants. Nous vous recommandons d’utiliser une ligne de base de 24 heures pour vous assurer d’obtenir des résultats significatifs et ayant un sens statistique. Plus la durée autorisée pour le test est longue, plus vous recevrez de réponses et plus Braze peut s’optimiser. Ceci est particulièrement important pour les campagnes par e-mail. Les tests initiaux pour les variantes personnalisées ne devraient pas durer moins de 4 heures.<br><br>Lors de l'envoi à l'heure locale des utilisateurs ou avec le timing intelligent, les variantes personnalisées doivent être envoyées au moins 24 heures après le test A/B pour garantir la réception/distribution à tous les utilisateurs du groupe de variantes personnalisées. |
| Canal de secours | Que se passe-t-il si aucune variante personnalisée n'est trouvée ? Vous avez le choix entre envoyer la variante gagnante à la place ou mettre fin au test et ne plus envoyer de messages. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Analyse

Pour en savoir plus sur les résultats de votre test A/B avec une optimisation, reportez-vous à la section [Analyses des tests A/B et multivariés][2].

[1]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/
[2]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/