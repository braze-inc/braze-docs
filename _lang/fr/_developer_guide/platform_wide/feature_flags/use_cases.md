---
nav_title: Exemples de cas d’utilisation
article_title: Exemples de cas d’utilisation
page_order: 30
description: "Cet article de référence couvre des exemples de cas d’utilisation d’indicateurs de fonctionnalité, y compris les déploiements progressifs, la configuration à distance, la coordination des messages et l’expérimentation."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# Exemple de cas d’utilisation

> Cet article décrit des exemples précis d’utilisation des indicateurs de fonctionnalité pour améliorer votre expérience utilisateur. Vous cherchez les étapes permettant de créer un indicateur de fonctionnalité dans Braze ? Consulter [Créer des indicateurs de fonctionnalité][8].

{% alert important %} 
Les indicateurs de fonctionnalité sont actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé. 
{% endalert %}

## Déploiements progressifs

Dans cet exemple, disons que nous avons décidé d’ajouter un nouveau lien « Assistance en direct » à notre application pour un service client plus rapide. Nous pourrions publier cette fonctionnalité à tous les clients en même temps. Cependant, une publication globale comporte des risques, tels que : 

* Notre équipe d’assistance est toujours en formation, et les clients pourront commencer des tickets d’assistance dès qu’ils seront publiés. Cela ne nous donne pas de marge de manœuvre au cas où l’équipe d’assistance aurait besoin de plus de temps.
* Nous ne sommes pas sûrs du volume réel de nouveaux cas d’assistance que nous obtiendrons, afin que nous ne puissions pas être employés de manière appropriée.
* Si notre équipe d’assistance est submergée, nous n’avons aucune stratégie à mettre en place rapidement pour désactiver cette fonctionnalité.
* Il peut y avoir des bogues introduits dans le widget chat et nous ne voulons pas que les clients aient une expérience négative.

Avec les indicateurs de fonctionnalité de Braze, nous pouvons progressivement déployer la fonction et atténuer tous ces risques :

* Nous allons activer la fonction « Assistance en direct » lorsque l’équipe d’assistance indique qu’elle est prête.
* Nous allons activer cette nouvelle fonctionnalité pour seulement 10 % des utilisateurs afin de déterminer si nos effectifs sont appropriés.
* En cas de bogues, nous pouvons rapidement désactiver la fonction au lieu de précipiter pour expédier une nouvelle version.

Pour déployer progressivement cette fonction, nous créons un indicateur de fonctionnalité appelé `enable_live_chat` dans le tableau de bord de Braze.

![Indicateur de fonctionnalité appelé "enable_live_chat"][7]

Dans notre code d’application, nous ne montrerons que le bouton **Démarrer la discussion en direct** lorsque l’indicateur de fonctionnalité de Braze est activé :

```javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Get the initial value from the Braze SDK
const featureFlag = braze.getFeatureFlag("enable_live_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(() => {
    const newValue = braze.getFeatureFlag("enable_live_chat").enabled;
    setLiveChatEnabled(newValue);
});

// Only show the Live Chat if the Braze SDK determines it is enabled
return (<>
  Need help? <button>Email Our Team</button>
  {liveChatEnabled && <button>Start Live Chat</button>}
</>)

```

## Configuration à distance

Disons que notre équipe Marketing souhaite répertorier nos ventes et promotions actuelles dans la navigation de notre application. Normalement, nos ingénieurs ont besoin d’un délai d’exécution d’une semaine pour tout changement et de trois jours pour un examen d’App Store. Mais avec Thanksgiving, Black Friday, Cyber Monday, Hanukah, Noël et New Years pendant deux mois, nous ne serons pas en mesure de faire ces délais serrés.

Avec des indicateurs de fonctionnalité, nous pouvons laisser Braze alimenter le contenu de notre lien de navigation de l’application, ce qui permet à notre gestionnaire marketing de changer en quelques minutes plutôt que de jours.

Pour configurer à distance cette fonctionnalité, nous allons créer un indicateur de fonctionnalité appelé `navigation_promo_link` et définissez les propriétés initiales suivantes :

![Indicateur de fonctionnalité affichant les propriétés « lien » et « texte » pointant vers une page de vente générique][1]

Dans notre application, nous utiliserons les méthodes getter de Braze pour récupérer les propriétés de cette entité et construire les liens de navigation en fonction de ces valeurs :

```javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// Read the "text" property
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
  <div>
    <a href="/">Home</a>
    { promoEnabled && <a href={promoLink}>{promoText}</a> }
    <a href="/products">Products</a>
    <a href="/categories">Categories
  </div>
</>)
```

Aujourd’hui, la veille de Thanksgiving, tout ce que nous devons faire est de modifier ces valeurs de propriété dans le tableau de bord de Braze :

![Indicateur de fonctionnalité affichant les propriétés « lien » et « texte » pointant vers une page de ventes de Thanksgiving][2]

Par conséquent, la prochaine fois que quelqu’un charge l’application, il verra les nouvelles offres de Thanksgiving.


## Coordination d’envoi de messages

{% alert important %} 
Cette fonctionnalité n’est pas encore prise en charge dans la version bêta.
{% endalert %}

Disons que nous lançons un nouveau programme de fidélité pour nos utilisateurs finaux. Il peut être difficile pour les équipes marketing et produit de coordonner parfaitement le calendrier des messages promotionnels avec le déploiement d’une entité. Les indicateurs de fonctionnalité du Canvas vous permettent d’appliquer une logique sophistiquée lorsqu’il s’agit d’activer une fonction pour un public sélectionné, et de contrôler l’envoi de messages associé à ces mêmes utilisateurs.

Pour coordonner efficacement le déploiement et l’envoi de messages des entités, nous allons créer un indicateur de fonctionnalité appelé `show_loyalty_program`. Pour notre première version progressive, nous allons laisser Canvas contrôler quand et pour qui l’indicateur de fonctionnalité est activé. Pour l’instant, nous allons laisser le pourcentage de déploiement à 0 % et ne sélectionner aucun segment cible.

![Un indicateur de fonctionnalité nommé "show_loyalty_program"][3]

Ensuite, dans Canvas Flow, nous allons créer une étape d’indicateur de fonctionnalité Canvas qui permet l’indicateur de fonctionnalité `show_loyalty_program` pour notre segment « Clients à valeur élevée » :

![Flux de Canvas montrant une répartition du public où les « clients de grande valeur » permettent un "show_loyalty_programIndicateur de fonctionnalité "][4]

Maintenant, les utilisateurs de ce segment commenceront à voir le nouveau programme de fidélité, et une fois qu’ils auront été activés, un e-mail et une enquête seront automatiquement envoyés pour aider notre équipe à recueillir des commentaires.


## Expérimentation

{% alert important %} 
Cette fonctionnalité n’est pas encore prise en charge dans la version bêta.
{% endalert %}

Un test A/B est un outil puissant qui compare les réponses des utilisateurs à plusieurs versions d’une variable.

Dans cet exemple, notre équipe a créé un nouveau flux de paiement pour notre application commerce électronique. Même si nous sommes convaincus que c’est une amélioration de l’expérience utilisateur, nous voulons exécuter un test A/B afin de mesurer son impact sur le chiffre d’affaires de notre application.

Pour commencer, nous allons créer un nouvel indicateur de fonctionnalité appelé `enable_checkout_v2`. Nous n’ajouterons pas de public ou de pourcentage de déploiement. Nous utiliserons plutôt Canvas pour diviser le trafic, activer la fonction et mesurer le résultat.

Dans notre application, nous vérifierons si l’indicateur de fonctionnalité est activé ou non et en annulant le flux de paiement en fonction de la réponse :

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
if (featureFlag.enabled) {
  return <NewCheckoutFlow />
} else {
  return <OldCheckoutFlow />
}
```

Dans Canvas, nous utiliserons [Chemin d’expérience][5] et une étape d’indicateur de fonctionnalité pour configurer notre test A/B.

À présent, 50 % des utilisateurs verront l’ancienne expérience, tandis que les autres 50 % voient la nouvelle expérience. Nous pouvons ensuite analyser les deux étapes pour déterminer quel flux de paiement a entraîné un taux de conversion plus élevé.

![Canvas avec un chemin d’expérience répartit le trafic en deux groupes 50 %][6]

Une fois que nous aurons déterminé notre gagnant, nous pouvons arrêter ce Canvas et augmenter le pourcentage de déploiement sur l’indicateur d’entité à 100 % pour tous les utilisateurs, tandis que notre équipe d’ingénierie code cela dans notre prochaine version de l’application.

[1]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %}
[2]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %}
[3]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %}
[4]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step
[6]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-experiment-step.png %}
[7]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %}
[8]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/
