---
nav_title: FAQ sur l'intelligence
article_title: FAQ sur l'intelligence
page_order: 19
description: "Cet article fournit des réponses aux questions fréquemment posées sur le canal intelligent, la sélection intelligente et le timing intelligent."
---

# FAQ sur l'intelligence

> Cet article fournit des réponses aux questions fréquemment posées sur la suite de renseignements.

## Sélection intelligente

### Pourquoi la rééligibilité n'est-elle pas disponible si elle est combinée à une sélection intelligente?

Nous ne permettons pas que les campagnes de sélection intelligentes aient été rééligibles parce qu'elles affecteraient l'intégrité de la variante de contrôle.

Normalement, les campagnes avec rééligibilité entraîneront les utilisateurs à réinscrire la même variante qu'ils ont reçue auparavant. Avec sélection intelligente, il n'est pas possible de garantir qu'un utilisateur recevra la même variante de campagne parce que la distribution de variante aurait changé en raison de l'aspect d'allocation optimale pour cette fonctionnalité.

Par exemple, si une campagne utilise les variantes A(20%) / B(20%) / Control(60%), la distribution de variante pourrait être A(15%) / B(25%) / Control(60%) pour la deuxième manche.

### Pourquoi mes variantes intelligentes de sélection sont-elles égales lors des premiers stades de ma campagne?

La sélection intelligente alloue des variantes à envoyer en fonction du statut actuel de la conversion de campagne. Elle ne détermine que les allocations de variantes finales après une période de formation, où les envois sont envoyés équitablement entre les variantes. Si vous ne souhaitez pas que la sélection intelligente envoie uniformément pendant les premiers stades de votre campagne, utiliser des variantes fixes pour un test A/B traditionnel.

### Est-ce que la sélection intelligente cessera d'optimiser sans choisir un gagnant clair?

Une sélection intelligente cessera d'optimiser lorsqu'elle aura 95% de confiance que la poursuite de l'expérience n'améliorera pas le taux de conversion de plus de 1% de son taux actuel.

### Pourquoi ne puis-je pas activer la sélection intelligente dans mon Canvas ou ma campagne (grisée) ?

La sélection intelligente sera indisponible si :
- Vous n'avez pas ajouté d'événements de conversion à votre campagne ou à votre Canvas
- Vous êtes en train de créer une campagne pour un seul envoi.
- Votre Canvas est composée d'une seule variante sans ajout de variantes ou de groupes de contrôle.
- Votre Canvas est composée d'un groupe de contrôle unique, sans variantes ajoutées.

## Timing Intelligent

### Le timing intelligent prévoit-il quand un utilisateur est le plus susceptible de convertir, ou seulement quand un utilisateur est le plus susceptible d'ouvrir/cliquer?

Le timing intelligent prédit quand un utilisateur est le plus susceptible d'ouvrir/cliquer.

### Comment le temps d'application le plus populaire est-il déterminé ?

L'heure d'application la plus populaire est déterminée par l'heure de début moyenne de la session pour le groupe d'applications (en heure locale). Cette métrique peut être trouvée dans le tableau de bord lors de la prévisualisation des temps de synchronisation d'une campagne, affichée en rouge.

### Combien de temps à l'avance devrais-je lancer une campagne de synchronisation intelligente pour la livrer avec succès à tous les utilisateurs de tous les fuseaux horaires?

Braze calcule l'heure optimale à minuit à l'heure Samoan, le premier fuseau horaire au monde. En une seule journée, il y a environ 48 heures que cela couvre. Par exemple, quelqu'un dont le temps optimal est de 12:01 am qui vit en Australie a déjà eu son temps passé, et il est "trop tard" à leur envoyer. Pour ces raisons, vous devez planifier 48 heures à l'avance pour vous assurer que toutes les personnes qui utilisent votre application seront livrées avec succès.

### Pourquoi ma campagne de timing intelligente n'affiche-t-elle pas grand-chose à aucun envoie?

Braze a besoin d'un nombre de données de base de points pour faire une bonne estimation. S'il n'y a pas assez de données de session ou que les utilisateurs ciblés n'ont que peu à peu de clics ou s'ouvrent (par ex. les nouveaux utilisateurs), l'heure de synchronisation intelligente peut par défaut correspondre à l'heure la plus populaire du groupe d'applications le jour de la semaine. S'il n'y a pas assez d'informations sur le groupe d'applications, nous retombons à une heure par défaut de 17 heures. Notez qu'il y a aussi une option pour définir un temps de retard.

### Pourquoi ma campagne de timing intelligente envoye-t-elle au-delà de la date prévue ?

Votre campagne de timing intelligente peut être en train d'envoyer au-delà de la date prévue parce que vous explorez les tests A/B. Les campagnes utilisant des tests A/B peuvent automatiquement envoyer la variante gagnante après la fin du test A/B. Cela augmente la durée d'envoi de la campagne. Par défaut, des campagnes de timing intelligentes seront planifiées pour envoyer la variante gagnante aux utilisateurs restants pour le lendemain, mais les clients peuvent modifier cette date d'envoi.

Nous recommandons aux utilisateurs disposant de campagnes de timing intelligentes de laisser plus de temps au test A/B pour terminer et programmer la variante gagnante pour envoyer deux jours de sortie au lieu d'un seul.

### Quand vérifions-nous les critères d'admissibilité des utilisateurs et/ou des adaptateurs d'audience?

Braze effectue deux vérifications lorsque des campagnes sont lancées. Une fois, dès que le premier fuseau horaire est identifié, démarrez le processus de file d'attente de l'utilisateur, et le deuxième, à l'heure prévue pour voir si les utilisateurs sont toujours éligibles pour recevoir la campagne.

Soyez prudent lorsque vous créez des campagnes qui filtrent les envois d'autres campagnes. Par exemple, si vous deviez envoyer deux campagnes le même jour pour des heures différentes et ajouter un filtre qui ne permet aux utilisateurs de recevoir la deuxième campagne que s'ils ont reçu la première, les utilisateurs ne recevront pas la deuxième campagne car personne n'était éligible lorsque la campagne a été créée pour la première fois et que des segments ont été formés.

### Puis-je utiliser des heures silencieuses dans ma campagne de timing intelligente?

Nous ne recommandons pas d'utiliser à la fois des horaires intelligents et des heures silencieuses pour votre campagne ou Canvas car il est contre-productif. Les heures silencieuses sont basées sur des suppositions descendantes sur le comportement de l'utilisateur, tandis que le timing intelligent est basé sur l'activité de l'utilisateur.

### Puis-je utiliser un chronométrage intelligent et une limitation de taux ?

Braze ne recommande pas d'utiliser un calendrier et une limitation de taux intelligents, car il n'y a aucune garantie quant au moment où le message sera envoyé.

### Puis-je utiliser un timing intelligent lors du réchauffement de la propriété intellectuelle ?

Braze ne recommande pas d'utiliser un timing intelligent lorsque les utilisateurs sont les premiers réchauffeurs IP, car certains de ses comportements peuvent causer des difficultés à toucher les volumes quotidiens. Cela est dû à une évaluation intelligente des segments de campagne deux fois. Une fois, lorsque la campagne est construite pour la première fois, et une deuxième fois avant d'envoyer aux utilisateurs pour vérifier qu'ils doivent toujours être dans ce segment. Cela peut entraîner le déplacement et le changement des segments, entraînant souvent la chute de certains utilisateurs du segment lors de la deuxième évaluation. Ces utilisateurs ne sont pas remplacés, ce qui a un impact sur la proximité avec le plafond maximum que vous pouvez atteindre. 
