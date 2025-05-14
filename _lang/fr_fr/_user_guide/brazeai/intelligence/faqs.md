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

---

## Timing intelligent

### Généralités

#### Que prédit le timing intelligent ?

Le timing intelligent se concentre sur la prédiction du moment où un utilisateur est le plus susceptible d'ouvrir ou de cliquer sur vos messages pour s'assurer que vos messages atteignent les utilisateurs à des moments d'engagement optimaux.

#### Le timing intelligent est-il calculé séparément pour chaque jour de la semaine ?

Non, le timing intelligent n'est pas lié à des jours spécifiques. Au lieu de cela, il personnalise les heures d'envoi en fonction des modèles d'engagement uniques de chaque utilisateur et du canal que vous utilisez, comme l'e-mail ou les notifications push. Ainsi, vos messages parviennent aux utilisateurs au moment où ils sont le plus réceptifs.

### Calculs

#### Quelles sont les données utilisées pour calculer l'heure optimale pour chaque utilisateur ?

Pour calculer l'heure optimale, utilisez la fonction Timing intelligent :

1. Analyse les données d'interaction de chaque utilisateur enregistrées par le SDK de Braze. Ceci comprend :
  - Horaires des sessions
  - Ouvertures directes de notification push
  - Ouvertures influencées de notification push
  - Clics des e-mails
  - Ouvertures d'e-mail (à l'exclusion des ouvertures de machines)
2. Regroupe ces événements par heure, en identifiant l'heure d'envoi optimale pour chaque utilisateur.

#### Les Opens Machine sont-ils pris en compte dans le calcul du temps optimal ?

Non, les [ouvertures de machines]({{site.baseurl}}/user_guide/data/report_metrics#machine-opens) sont exclues des calculs du temps optimal. Cela signifie que les heures d'envoi sont basées uniquement sur l'engagement réel des utilisateurs, offrant un timing plus précis pour vos campagnes.

#### Quelle est la précision de la durée optimale ?

Le timing intelligent planifie les messages pendant l'heure où l'utilisateur est le plus engagé, en fonction de ses débuts de session et des événements d'ouverture des messages. Au cours de cette heure, l'heure du message est arrondie aux cinq minutes les plus proches. Par exemple, si l'heure optimale d'un utilisateur est calculée comme étant 16 h 58, le message sera planifié pour 17 h 00. Il peut y avoir de légers retards dans la réception/distribution en raison de l'activité du système pendant les périodes d'affluence.

#### Quels sont les calculs de secours en cas de manque de données ?

S'il y a moins de cinq événements pertinents pour un utilisateur, le timing intelligent utilise l'[heure de repli][1] indiquée dans les paramètres de votre message. 

### Gestion des campagnes

#### Combien de temps à l’avance dois-je lancer une campagne de timing intelligent pour la livrer avec succès à tous les utilisateurs de tous les fuseaux horaires ?

Braze calcule le moment optimal à minuit, heure des Samoa, un des premiers fuseaux horaires du monde. Un seul jour couvre environ 48 heures. Par exemple, une personne dont le temps optimal est 12 h 01 qui vit en Australie a déjà dépassé cette heure optimale et il est donc « trop tard » pour leur envoyer la campagne. Pour ces raisons, vous devez planifier 48 heures à l'avance pour réussir à livrer toutes les personnes qui utilisent votre application dans le monde.

#### Pourquoi ma campagne de timing intelligent affiche-t-elle aucun ou peu d’envois ?

Braze a besoin d’un nombre de points de données de référence pour réaliser une bonne estimation. S'il n'y a pas assez de données de session ou si les utilisateurs ciblés ont peu ou pas de clics ou d'ouvertures d'e-mails (comme les nouveaux utilisateurs), le timing intelligent peut prendre par défaut l'heure la plus populaire de l'espace de travail pour ce jour de la semaine. Si les informations sont insuffisantes concernant l’espace de travail, nous passons à 17 h, l’heure de secours par défaut. Vous pouvez également choisir de fixer un [délai de repli]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options) spécifique.

#### Pourquoi ma campagne de timing intelligent est-elle envoyée après la date planifiée ?

Votre campagne de timing intelligent peut être envoyée après la date planifiée parce que vous tirez parti des tests A/B. Les campagnes utilisant les tests A/B peuvent envoyer automatiquement la variante gagnante une fois le test A/B terminé, ce qui augmente la durée d'envoi de la campagne. Par défaut, les campagnes de timing intelligent sont planifiées pour envoyer la variante gagnante aux utilisateurs restants le lendemain, mais vous pouvez modifier cette date d'envoi.

Nous vous recommandons, si vous avez des campagnes à timing intelligent, de laisser plus de temps pour que le test A/B se termine et de planifier l'envoi de la variante gagnante pour deux jours au lieu d'un. 

### Considérations techniques

#### Quand est-ce que Braze vérifie les critères d’éligibilité pour les segments ou les filtres d’audience ?

Braze effectue deux vérifications lorsqu’une campagne est lancée :

1. **Vérification initiale :** A minuit dans le premier fuseau horaire le jour de l'envoi.
2. **Vérification de l'heure planifiée :** Juste avant l'envoi, à l'heure de la sélection intelligente choisie par l'utilisateur.

Soyez prudent lorsque vous filtrez sur la base d'autres envois de campagne afin d'éviter de cibler des segments inéligibles. Par exemple, si vous envoyez deux campagnes le même jour à des heures différentes et que vous ajoutez un filtre qui n'autorise les utilisateurs à recevoir la deuxième campagne que s'ils ont reçu la première, les utilisateurs ne recevront pas la deuxième campagne. La raison en est que personne n’était éligible lorsque la campagne a été créée et que les segments ont été formés.

#### Puis-je utiliser des heures calmes dans ma campagne de timing intelligent ?

Les heures calmes peuvent être utilisées dans le cadre d'une campagne utilisant le timing intelligent. L'algorithme de timing intelligent évitera les heures calmes afin d'envoyer le message à tous les utilisateurs éligibles. Cela dit, nous vous recommandons de désactiver les heures calmes, à moins qu'il n'y ait des implications en termes de politique, de conformité ou d'autres implications légales quant au moment où les messages peuvent ou ne peuvent pas être envoyés.

#### Que se passe-t-il si le moment optimal pour un utilisateur se situe pendant les heures calmes ? 

Si l'heure optimale déterminée tombe pendant les heures calmes, Braze trouve le bord le plus proche des heures calmes et planifie le message pour la prochaine heure autorisée avant ou après les heures calmes. Le message est mis en file d'attente pour être envoyé à la limite la plus proche des heures calmes par rapport à l'heure optimale.

#### Puis-je utiliser un timing intelligent et une limitation du taux ?

La limite de débit peut être utilisée dans le cadre d'une campagne utilisant le timing intelligent. Toutefois, en raison de la nature de la limitation du débit, certains utilisateurs peuvent recevoir leur message à un moment qui n'est pas optimal, en particulier si un grand nombre d'utilisateurs par rapport à la taille de la limite de débit sont planifiés au moment du repli en raison d'un manque de données. 

Nous vous recommandons de n'utiliser la limite de débit sur une campagne de timing intelligent que lorsque des exigences techniques doivent être respectées à l'aide de la limite de débit.

#### Puis-je utiliser un timing intelligent pendant le réchauffement d’adresses IP ?

Braze ne recommande pas l'utilisation du timing intelligent lors du premier réchauffement IP, car certains de ses comportements peuvent entraîner des difficultés à atteindre les volumes quotidiens. Cela est provoqué par un timing intelligent évaluant deux fois les segments de campagne. La première fois lorsque la campagne est créée et une seconde fois avant l’envoi aux utilisateurs pour vérifier qu’ils se trouvent toujours bien dans ce segment.

Cela peut entraîner des modifications et des changements de segments, entraînant souvent une sortie de certains utilisateurs du segment lors de la deuxième évaluation. Ces utilisateurs ne sont pas remplacés, ce qui a un impact sur la proximité du plafond utilisateur maximal que vous pouvez atteindre.

#### Comment est-ce que le moment le plus populaire pour l’application est-il déterminé ?

L'heure de l'application la plus populaire est déterminée par l'heure moyenne de début de la session pour l'espace de travail (en heure locale). Cet indicateur se trouve dans le tableau de bord lors de la prévisualisation des temps de synchronisation pour une campagne, affiché en rouge.

#### Le timing intelligent tient-il compte des ouvertures de machines ?

Oui, les ouvertures automatiques sont filtrées par le timing intelligent, de sorte qu'elles n'influencent pas son rendement.

#### Comment puis-je m'assurer que le timing intelligent fonctionne le mieux possible ?

Le timing intelligent utilise l'historique individuel de l'engagement de chaque utilisateur dans les messages, quelle que soit l'heure à laquelle il les a reçus. Avant d'utiliser le timing intelligent, assurez-vous d'avoir envoyé aux utilisateurs des messages à différents moments de la journée. De cette manière, vous pouvez "échantillonner" le moment le plus propice pour chaque utilisateur. Un échantillonnage inadéquat des différents moments de la journée peut conduire le timing intelligent à choisir une heure d'envoi non optimale pour un utilisateur.


[1]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing#fallback-time
