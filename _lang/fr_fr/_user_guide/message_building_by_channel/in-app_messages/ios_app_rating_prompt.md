---
nav_title: "Demande d'évaluation dans l'application pour iOS"
article_title: "Invitation à la notation dans l'application pour iOS"
page_order: 6
description: "Cet article décrit les approches et les implications de l'utilisation de Braze pour demander aux utilisateurs d'évaluer votre appli."
channel:
  - in-app messages

---

# Demande d'évaluation in-app pour iOS

> Cet article décrit les approches et les implications de l'utilisation de Braze pour demander aux utilisateurs d'évaluer votre appli. Pour obtenir des conseils sur la manière de mener une campagne d'évaluation d'applis efficace, consultez [Les choses à faire et à ne pas faire en matière d'évaluation d'applis par les clients.](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings)

Apple propose une invite native, introduite avec iOS 10.3, qui permet aux utilisateurs de noter les applications à partir de l'application elle-même. Si vous souhaitez demander des évaluations d'apps aux utilisateurs à l'aide d'un message in-app sur iOS, vous devez utiliser l'invite native, car Apple n'autorise pas les invites d'évaluation personnalisées (voir [les directives d'évaluation de l'App Store](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct), section 5.6.1).

Selon les directives d'Apple, les invites d'évaluation d'applications peuvent être affichées à un utilisateur jusqu'à trois fois par an, de sorte que toute campagne d'évaluation d'applications devrait tirer parti de la [limite de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/). Les utilisateurs peuvent également choisir de ne pas voir les demandes d'abonnement dans les paramètres de l'application. Pour en savoir plus sur les évaluations de l'App Store, consultez l'article d'Apple sur les [évaluations, les avis et les réponses.](https://developer.apple.com/app-store/ratings-and-reviews/)

## Utiliser Braze pour demander aux utilisateurs de donner leur avis sur l'application

Bien qu'Apple exige que vous utilisiez l'invite native, vous pouvez toujours tirer parti des campagnes Braze pour demander aux utilisateurs de noter et d'évaluer votre app au bon moment. Vous pouvez adopter deux approches principales.

### Approche 1 : Création de liens profonds vers l'App Store

Avec cette approche, vous souhaitez encourager les utilisateurs à se rendre sur l'App Store pour ajouter un commentaire. Pour ce faire, créez une campagne de messages in-app qui comporte des [liens profonds]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) vers l'App Store.

Deux écrans mobiles côte à côte. Le premier est un message in-app qui demande à l'utilisateur de noter l'application sur l'App Store. La seconde est la page de l'App Store iOS pour cette application.]({% image_buster /assets/img_archive/app_store_app_review.png %})

### Approche 2 : Amorçage doux

Si vous ne voulez pas que les utilisateurs quittent votre application, vous pouvez d'abord leur envoyer un message in-app. L'amorçage est un moyen de demander l'autorisation aux utilisateurs avant de leur envoyer l'invite d'évaluation native de l'App Store. Pour ce faire, créez une campagne de messages in-app et ajoutez un lien profond personnalisé qui appelle la méthode `requestReview` lorsqu'il est cliqué. 

Pour connaître les étapes détaillées, reportez-vous à l'[invite de révision personnalisée de l'App Store]({{site.baseurl}}/developer_guide/in_app_messages/customization/#swift_customizing-the-app-store-review-prompt).

Deux messages in-app côte à côte. La première incite l'utilisateur à évaluer l'application en lui demandant s'il a un moment pour le faire. Le second est le message in-app natif de l'App Store d'iOS, affichant une échelle de cinq étoiles que l'utilisateur peut sélectionner pour évaluer l'application.]({% image_buster /assets/img_archive/prime_app_review.png %})

Les utilisateurs soumettront une évaluation par le biais de l'invite d'évaluation native de l'App Store, et pourront rédiger et soumettre une évaluation sans quitter l'application.

### Considérations

Comme alternative à l'amorçage doux, vous pourriez également afficher directement l'invite de notation de l'app iOS sans aucun message d'amorçage doux de Braze affiché auparavant. L'avantage est que si l'utilisateur a choisi de ne pas recevoir de demande d'abonnement, il n'aura pas l'expérience sous-optimale d'essayer d'évaluer l'application sans qu'aucune demande n'apparaisse pour le faire.

{% alert important %}
Ne créez pas de messages in-app personnalisés en HTML qui imitent une invite d'évaluation d'une application iOS native, car cela va à l'encontre des directives d'Apple.
{% endalert %}

