---
nav_title: Invitation à l’évaluation in-app pour iOS
article_title: Invitation à l’évaluation in-app pour iOS
page_order: 6
description: "Cet article décrit les approches et les implications de l’utilisation de Braze pour demander aux utilisateurs d’évaluer votre application."
channel:
  - in-app messages

---

# Invitation à l’évaluation in-app pour iOS

> Cet article décrit les approches et les implications de l’utilisation de Braze pour demander aux utilisateurs d’évaluer votre application. Pour des conseils sur la façon de mener une campagne de notation d'application efficace, consultez [Les choses à faire et à ne pas faire pour les évaluations des applications clients](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings).

Apple propose une invitation native, mise en place avec iOS 10.3, qui permet aux utilisateurs d’évaluer l’application depuis l’application elle-même. Si vous souhaitez demander des évaluations d'applications aux utilisateurs via un message intégré à l'application sur iOS, vous devez utiliser l'invite native, car Apple interdit les invites de révision personnalisées (voir [Directives de révision de l'App Store](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct), section 5.6.1).

Conformément aux directives d'Apple, les invites de révision d'application peuvent être affichées à un utilisateur jusqu'à trois fois par an, de sorte que toute campagne de révision d'application devrait tirer parti de [la limitation du taux]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/). Les utilisateurs peuvent également se désabonner des invitations à l’évaluation de l’application directement dans leurs paramètres d’application. Pour plus d'informations sur les évaluations de l'App Store, consultez l'article d'Apple sur les [évaluations, avis et réponses](https://developer.apple.com/app-store/ratings-and-reviews/).

## Utiliser Braze pour demander une évaluation de l’application aux utilisateurs

Même si Apple exige que vous utilisiez l’invite native, vous pouvez cependant toujours tirer parti des campagnes Braze pour demander au bon moment aux utilisateurs d’évaluer et de laisser un commentaire sur votre application. Vous pouvez suivre deux approches principales.

### Première approche : Créer un lien profond vers l’App Store

Avec cette approche, vous voulez encourager les utilisateurs à se rendre sur l’App Store pour ajouter un commentaire. Pour ce faire, créez une campagne de messages in-app qui inclut un [lien profond]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) vers l'App Store.

![Deux écrans de mobile côte à côte. Le premier est un message in-app demandant à l’utilisateur d’évaluer l’application sur l’App Store. La seconde est la page de l'App Store iOS pour cette application.]({% image_buster /assets/img_archive/app_store_app_review.png %})

### Deuxième approche : Sensibilisation douce

Si vous ne voulez pas que vos utilisateurs quittent votre application, vous devez d’abord sensibiliser vos utilisateurs avec un message in-app séparé. La sensibilisation est une manière de demander la permission à vos utilisateurs avant de leur envoyer l’invite d’évaluation sur l’App Store native. Pour ce faire, créez une campagne de communication in-app et ajoutez un lien profond personnalisé qui appelle la méthode `requestReview` lorsqu’ils sont cliqués. 

Pour connaître les étapes détaillées, consultez la section [Invite personnalisée d’évaluation dans l’App Store]({{site.baseurl}}/developer_guide/in_app_messages/customization/#swift_customizing-the-app-store-review-prompt).

![Deux messages in-app côte à côte. Le premier sensibilise l’utilisateur à l’évaluation de l’application en leur demandant s’ils ont le temps d’évaluer l’application. Le second est le message d'évaluation natif de l'App Store d'iOS, affichant une échelle de cinq étoiles que l'utilisateur peut sélectionner pour évaluer l'application.]({% image_buster /assets/img_archive/prime_app_review.png %}).

Les utilisateurs soumettront l’évaluation à l’aide de l’invite à l’évaluation dans l’App Store native et peuvent écrire et soumettre une évaluation sans quitter l’application.

### Considérations

Une alternative à la sensibilisation douce peut être d’afficher l’invite à l’évaluation de l’application iOS directement, sans afficher au préalable de message de sensibilisation douce de Braze. L’avantage de cette mesure est que, si l’utilisateur est désabonné des invites à l’évaluation de l’application, l’utilisateur ne subirait pas l’expérience désagréable de vouloir essayer d’évaluer l’application sans avoir d’invite qui s’affiche pour le faire.

{% alert important %}
Ne créez pas de messages in-app HTML personnalisés qui imitent l’invitation à l’évaluation de l’application iOS native, étant donné que le faire violerait les directives d’Apple.
{% endalert %}

