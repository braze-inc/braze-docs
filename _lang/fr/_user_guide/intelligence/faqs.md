---
nav_title: FAQ Intelligence
article_title: FAQ Intelligence
page_order: 19
description: "Le présent article fournit des réponses aux questions fréquemment posées sur le canal intelligent, la sélection intelligente et le timing intelligent."
---

# FAQ Intelligence

> Le présent article fournit des réponses aux questions fréquemment posées l’Intelligence Suite.

## Sélection intelligente

### Pourquoi la rééligibilité n’est-elle pas disponible lorsqu’elle est associée à une sélection intelligente ?

Nous ne permettons pas aux campagnes de sélection intelligentes d’avoir une rééligibilité activée car cela affecterait l’intégrité de la variante de contrôle.

Normalement, les campagnes avec rééligibilité amèneront les utilisateurs à saisir de nouveau la même variante qu’auparavant. Avec une sélection intelligente, il n’est pas possible de garantir qu’un utilisateur recevra la même Campaign Variant parce que la distribution de la variante aurait changé en raison de l’aspect d’allocation optimal pour cette fonction. 

Par exemple, si une campagne utilise les variantes A (20 %)/B (20 %)/Contrôle (60 %), la distribution de la variante pourrait être A (15 %)/B (25 %)/Contrôle (60 %) pour la seconde partie.

### Pourquoi mes variantes de sélection intelligente affichent-elles des envois égaux pendant les premières étapes de ma campagne ?

La sélection intelligente alloue les variantes à envoyer en fonction du statut actuel de conversion de la campagne. Elle détermine uniquement les attributions de variantes finales après une période de formation durant laquelle les envois sont réalisés de manière uniforme entre les variantes. Si vous ne souhaitez pas que la sélection intelligente soit envoyée de manière uniforme pendant les premières étapes de votre campagne, utilisez des variantes fixes pour un test A/B traditionnel. 

### La sélection intelligente cessera-t-elle d’optimiser sans choisir un gagnant clair ? 

La sélection intelligente cessera d’optimiser lorsqu’elle sera sûre à 95 % que la poursuite de l’expérience n’améliorera pas le taux de conversion de plus de 1 % par rapport à son taux actuel.

### Pourquoi ne puis-je pas activer la sélection intelligente dans mon Canvas ou ma campagne (grisé) ?

La sélection intelligente ne sera pas disponible si :
- Vous n’avez pas ajouté d’événements de conversion à votre campagne ou Canvas
- Vous créez une campagne à envoi unique.
- Votre Canvas est composé d’une seule variante sans ajout de variantes supplémentaires ou de groupes de contrôle.
- Votre Canvas est composé d’un seul groupe de contrôle sans ajout de variantes.

## Timing Intelligent

### Est-ce que le timing intelligent prédit quand un utilisateur est le plus susceptible de se convertir ou seulement quand il est le plus susceptible d’ouvrir ou de cliquer ?

Le timing intelligent prédit quand un utilisateur est le plus susceptible d’ouvrir ou de cliquer. 

### Comment est-ce que le moment le plus populaire pour l’application est-il déterminé ?

Le moment le plus populaire pour l’application est déterminé par l’heure de début de session moyenne pour le groupe d’apps (en heure locale). Cette métrique se trouve dans le tableau de bord lors de la prévisualisation des temps de synchronisation pour une campagne, affichée en rouge. 

### Combien de temps à l’avance dois-je lancer une campagne de timing intelligent pour la livrer avec succès à tous les utilisateurs de tous les fuseaux horaires ?

Braze calcule le moment optimal à minuit, heure des Samoa, le premier fuseau horaire du monde. En un seul jour, il couvre environ 48 heures. Par exemple, une personne dont le temps optimal est 12 h 01 qui vit en Australie a déjà dépassé cette heure et il est donc « trop tard » pour leur envoyer la campagne. Pour ces raisons, vous devez planifier 48 heures à l’avance pour vous assurer que toutes les personnes qui utilisent votre application dans le monde seront livrées avec succès. 

### Pourquoi ma campagne de timing intelligent affiche-t-elle aucun ou peu d’envois ?

Braze a besoin d’un nombre de points de données de référence pour réaliser une bonne estimation. S’il n’y a pas assez de données de session ou que les utilisateurs ciblés ont peu ou pas de clics ou d’ouvertures d’e-mail (par ex., les nouveaux utilisateurs), un timing intelligent peut basculer par défaut sur l’heure la plus populaire du groupe d’apps ce jour de la semaine. Si les informations sont insuffisantes concernant le groupe d’applications, nous passerons à une heure de secours par défaut de 17 h. Notez qu’il existe également une option de réglage de l’heure de secours. 

### Pourquoi ma campagne de timing intelligent est-elle envoyée après la date planifiée ? 

Votre campagne de timing intelligent peut être envoyée après la date planifiée parce que vous tirez parti des tests A/B. Les campagnes utilisant des tests A/B peuvent envoyer automatiquement la variante gagnante après le test A/B, augmentant ainsi la durée d’envoi de la campagne. Par défaut, les campagnes de timing intelligent seront planifiées pour envoyer la variante gagnante aux utilisateurs restants le lendemain, mais les clients peuvent modifier cette date d’envoi. 

Nous recommandons aux utilisateurs ayant des campagnes de timing intelligent de laisser plus de temps pour que le test A/B s’achève et de planifier l’envoi de la variante gagnante pendant deux jours au lieu d’un. 

### Quand vérifions-nous les critères d’éligibilité pour les segments d’utilisateurs ou les filtres d’audience ?

Braze effectue deux vérifications lorsque des campagnes sont lancées. La première dès que la première plage horaire est identifiée, qui commence le processus de file d’attente des utilisateurs, et la seconde à l’heure planifiée pour voir si les utilisateurs sont toujours éligibles pour recevoir la campagne. 

Soyez prudent lorsque vous créez des campagnes qui filtrent à partir des envois d’autres campagnes. Par exemple, si vous deviez envoyer deux campagnes le même jour à des heures différentes et ajoutiez un filtre qui permet uniquement aux utilisateurs de recevoir la deuxième campagne s’ils ont reçu la première, les utilisateurs ne recevront pas la deuxième campagne car personne n’était éligible lorsque la campagne a été créée et que les segments ont été formés.

### Puis-je utiliser des heures calmes dans ma campagne de timing intelligent ?

Nous ne vous recommandons pas d’utiliser à la fois le timing intelligent et les heures calmes pour votre campagne ou votre Canvas car cela est contre-productif. Les heures calmes sont basées sur des hypothèses descendantes concernant le comportement des utilisateurs, tandis que le timing intelligent est basé sur l’activité de l’utilisateur.

### Puis-je utiliser un timing intelligent et une limitation du taux ?

Braze ne recommande pas d’utiliser un timing intelligent et une limitation du taux, car il n’y a aucune garantie quant à la date à laquelle le message sera livré. 

### Puis-je utiliser un timing intelligent pendant le réchauffement IP ?

Braze ne recommande pas d’utiliser un timing intelligent lorsque les utilisateurs commencent le réchauffement IP car certains de ses comportements peuvent causer des difficultés pour atteindre les volumes quotidiens. Cela est provoqué par un timing intelligent évaluant deux fois les segments de campagne. La première fois lorsque la campagne est créée et une seconde fois avant l’envoi aux utilisateurs, vérifier qu’ils se trouvent toujours bien dans ce segment. Cela peut entraîner des modifications et des changements de segments, entraînant souvent une sortie de certains utilisateurs du segment lors de la deuxième évaluation. Ces utilisateurs ne sont pas remplacés, ce qui a un impact sur la proximité du plafond utilisateur maximal que vous pouvez atteindre. 
