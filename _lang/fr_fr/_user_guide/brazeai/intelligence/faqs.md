---
nav_title: FAQ
article_title: FAQ Intelligence
page_order: 191
description: "Le présent article fournit des réponses aux questions fréquemment posées sur le canal intelligent, la sélection intelligente et le timing intelligent."
---

# Foire aux questions

> Le présent article fournit des réponses aux questions fréquemment posées sur la suite d'outils Intelligence Suite.

## Sélection intelligente

### Pourquoi la rééligibilité dans moins de 24 heures n’est-elle pas disponible lorsqu’elle est associée à une sélection intelligente ?

Nous ne permettons pas aux campagnes de sélection intelligente d’activer la rééligibilité au cours d’une fenêtre trop courte car cela affecterait l’intégrité de la variante de contrôle. En créant un intervalle de 24 heures, nous aidons à garantir que l’algorithme disposera d’un ensemble de données valide statistiquement à partir duquel travailler.

Normalement, les campagnes avec rééligibilité amèneront les utilisateurs à saisir de nouveau la même variante qu’auparavant. Avec une sélection intelligente, Braze ne peut pas garantir qu’un utilisateur recevra la même variante de campagne parce que la distribution de la variante aurait changé en raison de l’aspect d’allocation optimal pour cette fonctionnalité. Si l’utilisateur était autorisé à rentrer à nouveau avant que la sélection intelligente ne réexamine la performance de la variante, les données pourraient être biaisées en raison des utilisateurs étant entrés à nouveau.

Par exemple, si une campagne utilise ces variantes :

- Variante A : 20%
- Variante B : 20%
- Contrôle : 60 %

La distribution de la variante pourrait alors être la suivante au deuxième tour :

- Variante A : 15%
- Variante B : 25 %
- Contrôle : 60 %

### Pourquoi mes variantes de sélection intelligente affichent-elles des envois égaux pendant les premières étapes de ma campagne ?

La sélection intelligente alloue les variantes à envoyer en fonction du statut actuel de conversion de la campagne. Elle détermine uniquement les attributions de variantes finales après une période de formation durant laquelle les envois sont réalisés de manière uniforme entre les variantes. Si vous ne voulez pas que la sélection intelligente soit envoyée de manière uniforme pendant les premières étapes de votre campagne, utilisez des variantes fixes pour un test A/B traditionnel.

### La sélection intelligente cessera-t-elle d’optimiser sans choisir un gagnant clair ?

La sélection intelligente cessera d’optimiser lorsqu’elle sera sûre à 95 % que la poursuite de l’expérience n’améliorera pas le taux de conversion de plus de 1 % par rapport à son taux actuel.

### Pourquoi ne puis-je pas activer la sélection intelligente dans mon canvas ou ma campagne (grisé) ?

La sélection intelligente ne sera pas disponible si :

- Vous n’avez pas ajouté d’événements de conversion à votre campagne ou Canvas
- Vous créez une campagne à envoi unique
- Vous avez activé la rééligibilité avec une fenêtre de moins de 24 heures
- Votre Canvas est composé d’une seule variante sans ajout de variantes supplémentaires ou de groupes de contrôle
- Votre Canvas est composé d’un seul groupe de contrôle sans ajout de variantes

## Timing intelligent

### Est-ce que le timing intelligent prédit quand un utilisateur est le plus susceptible de se convertir ou seulement quand il est le plus susceptible d’ouvrir ou de cliquer ?

Le timing intelligent prédit le moment où un utilisateur est le plus susceptible d'ouvrir ou de cliquer.

### Comment est-ce que le moment le plus populaire pour l’application est-il déterminé ?

L'heure de l'application la plus populaire est déterminée par l'heure moyenne de début de la session pour l'espace de travail (en heure locale). Cet indicateur se trouve dans le tableau de bord lors de la prévisualisation des temps de synchronisation pour une campagne, affiché en rouge.

### Le timing intelligent tient-il compte des ouvertures de machines ?

Oui, les ouvertures automatiques sont filtrées par le timing intelligent, de sorte qu'elles n'influencent pas son rendement.

### Comment puis-je m'assurer que le timing intelligent fonctionne le mieux possible ?

Le timing intelligent utilise l'historique individuel de l'engagement de chaque utilisateur dans les messages, quelle que soit l'heure à laquelle il les a reçus. Avant d'utiliser le timing intelligent, assurez-vous d'avoir envoyé aux utilisateurs des messages à différents moments de la journée. De cette façon, vous pouvez « échantillonner » le moment le plus propice pour chaque utilisateur. Un échantillonnage inadéquat des différents moments de la journée peut conduire le timing intelligent à choisir une heure d'envoi non optimale pour un utilisateur. 

### Combien de temps à l’avance dois-je lancer une campagne de timing intelligent pour la livrer avec succès à tous les utilisateurs de tous les fuseaux horaires ?

Braze calcule le moment optimal à minuit, heure des Samoa, un des premiers fuseaux horaires du monde. Un seul jour couvre environ 48 heures. Par exemple, une personne dont le temps optimal est 12 h 01 qui vit en Australie a déjà dépassé cette heure optimale et il est donc « trop tard » pour leur envoyer la campagne. Pour ces raisons, vous devez planifier 48 heures à l’avance pour vous assurer que toutes les personnes qui utilisent votre application dans le monde seront livrées avec succès.

### Pourquoi ma campagne de timing intelligent affiche-t-elle aucun ou peu d’envois ?

Braze a besoin d’un nombre de points de données de référence pour réaliser une bonne estimation. S'il n'y a pas assez de données de session ou si les utilisateurs ciblés ont peu ou pas de clics ou d'ouvertures d'e-mails (comme les nouveaux utilisateurs), le timing intelligent peut prendre par défaut l'heure la plus populaire de l'espace de travail pour ce jour de la semaine. Si les informations sont insuffisantes concernant l’espace de travail, nous passons à 17 h, l’heure de secours par défaut. Vous pouvez également choisir de fixer un [délai de repli]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options) spécifique.

### Pourquoi ma campagne de timing intelligent est-elle envoyée après la date planifiée ?

Votre campagne de timing intelligent peut être envoyée après la date planifiée parce que vous tirez parti des tests A/B. Les campagnes utilisant les tests A/B peuvent envoyer automatiquement la variante gagnante une fois le test A/B terminé, ce qui augmente la durée d'envoi de la campagne. Par défaut, les campagnes de timing intelligent sont planifiées pour envoyer la variante gagnante aux utilisateurs restants le lendemain, mais vous pouvez modifier cette date d'envoi.

Nous vous recommandons, si vous avez des campagnes à timing intelligent, de laisser plus de temps pour que le test A/B se termine et de planifier l'envoi de la variante gagnante pour deux jours au lieu d'un. 

### Quand est-ce que Braze vérifie les critères d’éligibilité pour les segments ou les filtres d’audience ?

Braze effectue deux vérifications lorsqu’une campagne est lancée :

1. Dès que le premier fuseau horaire est identifié, le processus de mise en file d’attente débute et
2. À l’heure planifiée pour voir si les utilisateurs sont toujours éligibles à la réception de la campagne.

Soyez prudent lorsque vous créez des campagnes qui filtrent à partir des envois d’autres campagnes. Par exemple, si vous deviez envoyer deux campagnes le même jour à des heures différentes et ajoutiez un filtre qui permet uniquement aux utilisateurs de recevoir la deuxième campagne s’ils ont reçu la première, les utilisateurs ne recevront pas la deuxième campagne. La raison en est que personne n’était éligible lorsque la campagne a été créée et que les segments ont été formés.

### Puis-je utiliser des heures calmes dans ma campagne de timing intelligent ?

Nous ne vous recommandons pas d’utiliser à la fois le timing intelligent et les heures calmes pour votre campagne ou votre Canvas, car cela est contre-productif. Les heures calmes sont basées sur des hypothèses descendantes concernant le comportement des utilisateurs, tandis que le timing intelligent est basé sur l’activité de l’utilisateur.

### Puis-je utiliser un timing intelligent et une limitation du taux ?

Braze ne recommande pas l'utilisation du timing intelligent et de la limitation de débit car il n'y a aucune garantie quant au moment où le message sera délivré.

### Puis-je utiliser un timing intelligent pendant le réchauffement d’adresses IP ?

Braze ne recommande pas l'utilisation du timing intelligent lors du premier réchauffement IP, car certains de ses comportements peuvent entraîner des difficultés à atteindre les volumes quotidiens. Cela est provoqué par un timing intelligent évaluant deux fois les segments de campagne. La première fois lorsque la campagne est créée et une seconde fois avant l’envoi aux utilisateurs pour vérifier qu’ils se trouvent toujours bien dans ce segment. 

Cela peut entraîner des modifications et des changements de segments, entraînant souvent une sortie de certains utilisateurs du segment lors de la deuxième évaluation. Ces utilisateurs ne sont pas remplacés, ce qui a un impact sur la proximité du plafond utilisateur maximal que vous pouvez atteindre.
