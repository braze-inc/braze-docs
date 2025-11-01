---
nav_title: FAQ
article_title: FAQ sur les tests multivariés et les tests A/B
page_order: 21
page_type: reference
toc_headers: h2
description: "Cet article couvre les FAQ pour les tests multivariés et les tests A/B avec Braze."
---

# FAQ sur les tests multivariés et les tests A/B

## Les bases du test

### Quelle est la différence entre les tests A/B et les tests multivariés ?

#### Test A/B

Dans les tests A/B, le marketeur expérimente une seule variable au sein de la campagne (comme les lignes d'objet d'un e-mail ou l'heure d'envoi du message). Il s'agit de diviser au hasard un sous-ensemble de l'audience en deux groupes ou plus, de présenter à chaque groupe une variante différente et d'observer quelle variante présente le taux de conversion le plus élevé. En général, la variante la plus performante est ensuite envoyée au reste de l'audience.

#### Test multivarié 

Le test multivarié est une extension du test A/B, qui permet au marketeur de tester plusieurs variables à la fois afin de déterminer la combinaison la plus efficace. Par exemple, vous pouvez tester la ligne d'objet de votre message e-mail, l'image qui accompagne votre texte et la couleur du bouton CTA. Ce type de test vous permet d'explorer davantage de variables et de combinaisons de variations au sein d'une même expérience, et d'obtenir des informations plus rapidement et de manière plus complète que les tests A/B. Cependant, tester plus de variables et de combinaisons au sein d'une même expérience nécessite une audience plus importante pour obtenir une signification statistique.

### Comment les résultats des tests A/B sont-ils calculés ?

Braze teste toutes les variantes les unes par rapport aux autres à l'aide de tests du chi-carré de Pearson, qui permettent de déterminer si une variante est statistiquement plus performante que toutes les autres à un niveau de signification de p < 0,05, ou ce que nous appelons une signification à 95 %. Parmi toutes les variantes qui dépassent ce seuil d'importance, la variante la plus performante est désignée comme "gagnante".

Il s'agit d'un test distinct du score de confiance, qui décrit uniquement la performance d'une variante par rapport au contrôle avec une valeur numérique comprise entre 0 et 100 %. Plus précisément, il représente notre confiance dans le fait que la différence standardisée du taux de conversion entre la variante et le contrôle est significativement plus grande que le hasard.

### Pourquoi la répartition des variantes n'est-elle pas uniforme ?

{% multi_lang_include multivariant_testing.md section='Variant distribution' %}

## Exécution et conclusion des tests

### Quand le test initial sera-t-il terminé ?

Lorsque vous utilisez la variante gagnante pour des campagnes à envoi unique, le test est terminé lorsque l'heure d'envoi de la variante gagnante arrive. Braze considérera qu'une variante est gagnante si elle affiche le taux de conversion le plus élevé avec une marge statistiquement significative.

Pour les campagnes récurrentes, basées sur des actions et déclenchées par l'API, vous pouvez utiliser la sélection intelligente pour suivre en permanence les données de performance de chaque variante et optimiser continuellement le trafic de la campagne vers les variantes les plus performantes. Avec la sélection intelligente, plutôt que de définir explicitement un groupe d'expérimentation où les utilisateurs reçoivent des variantes aléatoires, l'algorithme de Braze affinera en permanence son estimation de la variante la plus performante, ce qui pourrait permettre une sélection plus rapide de la variante la plus performante.

### Comment Braze traite-t-il les utilisateurs qui ont reçu une variante de message dans le cadre d'une campagne récurrente ou d'une étape du canvas ? 

Les utilisateurs sont affectés de manière aléatoire à une variante particulière avant de recevoir la campagne pour la première fois. Chaque fois que la campagne est reçue (ou que l'utilisateur entre à nouveau dans une variante du canvas), il recevra la même variante, à moins que les pourcentages de variante ne soient modifiés. Si les pourcentages des variantes changent, les utilisateurs peuvent être redistribués vers d'autres variantes. Les utilisateurs restent dans ces variantes jusqu'à ce que les pourcentages soient à nouveau modifiés. Les utilisateurs ne seront redistribués que pour les variantes qui ont été modifiées.

Par exemple, disons que nous avons une campagne ou un Canvas avec trois variantes. Si seules les variantes A et B sont modifiées ou mises à jour, les utilisateurs de la variante C ne seront pas redistribués car le pourcentage de variante de la variante C n'a pas été modifié. Les groupes de contrôle restent cohérents si le pourcentage de variante est inchangé. Les utilisateurs qui ont déjà reçu des messages ne peuvent pas entrer dans le groupe de contrôle lors d'un envoi ultérieur, et aucun utilisateur du groupe de contrôle ne peut jamais recevoir de message.

#### Qu'en est-il des chemins d'expérience ?

Il en va de même parce que les chemins de Canvas qui suivent une expérience sont également des variantes.

#### Puis-je prendre des mesures pour redistribuer les utilisateurs dans les campagnes et les canevas ?

La seule façon de redistribuer les utilisateurs dans les Canvas est d'utiliser les [Chemins Randomisés dans les Chemins d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#step-1-choose-the-number-of-paths-and-audience-distribution), ce qui randomisera toujours les affectations de chemin lorsque les utilisateurs réintègrent le Canvas. Cependant, il ne s'agit pas d'une expérience standard et cela pourrait invalider les résultats de l'expérience car le groupe de contrôle peut être contaminé par les utilisateurs du traitement.

## Confiance et partialité

### La confiance augmente-t-elle avec le temps ?

La confiance augmente avec le temps si toutes les autres choses restent constantes. Le maintien d'une constante signifie qu'il n'y a pas d'autres facteurs marketeurs susceptibles d'influencer les variantes, comme la variante A qui parle d'une vente de 25 % qui se termine à mi-parcours du test.

La confiance est une mesure du degré de confiance de Braze dans le fait que la variante est différente du contrôle. Plus le nombre de messages envoyés est important, plus la puissance statistique du test augmente, ce qui accroît la certitude que les différences de performances mesurées ne sont pas dues au hasard. En règle générale, un échantillon plus important augmente notre confiance dans l'identification de petites différences de performance entre les variantes et le contrôle.

### Les groupes de contrôle et de test peuvent-ils introduire des biais dans les tests ?

Il n'existe aucun moyen pratique pour que les attributs ou les comportements d'un utilisateur avant la création d'une campagne ou d'un Canvas particulier puissent varier systématiquement entre les variantes et le contrôle. 

Pour affecter les utilisateurs aux variantes de message, aux variantes Canvas ou à leurs groupes de contrôle respectifs, nous commençons par relier leur ID utilisateur généré de manière aléatoire à l'ID de campagne ou Canvas généré de manière aléatoire. Ensuite, nous appliquons un algorithme de hachage sha256 et divisons le résultat par 100, puis conservons le reste (également connu sous le nom de module avec 100). Enfin, nous classons les utilisateurs dans des tranches qui correspondent aux affectations en pourcentage des variantes (et du contrôle optionnel) choisies dans le tableau de bord.

### Pourquoi ne puis-je pas utiliser la limite de débit avec un groupe de contrôle ?

Actuellement, Braze ne prend pas en charge la limite de débit avec les tests A/B comportant un groupe de contrôle. En effet, la limitation du débit ne s'applique pas au groupe de contrôle de la même manière qu'aux variantes, ce qui introduit un biais. Envisagez plutôt d'utiliser la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), qui ajuste automatiquement le pourcentage d'utilisateurs qui recevront chaque variante en fonction des analyses et des performances de la campagne.
