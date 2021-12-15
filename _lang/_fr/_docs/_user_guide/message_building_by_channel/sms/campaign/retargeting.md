---
nav_title: Reciblage des utilisateurs
article_title: Reciblage des utilisateurs SMS
page_order: 5
description: "Cet article de référence couvre la façon dont les utilisateurs peuvent redimensionner leurs messages par les interactions SMS des utilisateurs."
page_type: Référence
tool:
  - Campagnes
channel:
  - SMS
---

# Remise en attente de SMS

En plus de changer l'état d'abonnement de l'utilisateur et d'envoyer des réponses automatiques basées sur des mots clés entrants, Braze enregistrera également les interactions avec le profil de l'utilisateur pour le filtrage et le déclenchement des messages. Ces filtres et déclencheurs vous permettent de filtrer les utilisateurs qui ont reçu des SMS, a reçu des messages SMS d'une campagne SMS spécifique, et déclenche des messages lorsque les utilisateurs reçoivent des messages SMS d'une campagne SMS spécifique.

{% alert tip %}
Pour en savoir plus sur les mots-clés personnalisés et comment mettre en place des messages bidirectionnels pour tirer parti de ces options de repositionnement, visitez notre article [mot-clé personnalisé]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/).
{% endalert %}

## Options de redistribution

### Filtrer les utilisateurs par SMS

Les utilisateurs peuvent être filtrés quand ils ont reçu un SMS pour la dernière fois ou s'ils ont reçu un SMS d'une campagne SMS spécifique. Les filtres peuvent être définis dans l'étape Utilisateurs cibles du constructeur de campagne.

__Filtrer par le dernier SMS reçu__<br> !\[Filtre 1\]\[2\]

__Filtrer par les messages reçus de la campagne SMS__<br> Filtre les utilisateurs qui ont reçu un message d'une campagne SMS spécifique. Avec ce filtre, vous avez également la possibilité de filtrer ceux qui n'ont pas reçu les messages d'une campagne SMS. <br> !\[Filtre 2\]\[1\]

### Déclencher les messages lorsque les utilisateurs reçoivent des SMS

Pour déclencher des messages en tant qu'utilisateurs reçoivent des messages SMS d'une campagne spécifique, sélectionnez __Interact with Campaign__ comme action de déclenchement. Ensuite, sélectionnez __Recevoir des SMS__ et la campagne SMS que vous souhaitez utiliser. <br><br> !\[Trigger\]\[3\]

## Reciblage par catégorie de mots clés

En plus des trois catégories de mots clés par défaut (opt-in, opt-out et aide), vous pouvez également créer jusqu'à 10 de vos propres catégories de mots clés, ce qui vous permet d'identifier des mots-clés et des réponses arbitraires. Ces catégories peuvent être utilisées pour le filtrage et le repositionnement. Pour en savoir plus sur les catégories de mots clés SMS et comment les configurer, visitez notre documentation [ici]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/).

### Filtrer par récurrence

Filtrer pour la récurrence d'un utilisateur répondant à votre programme SMS. Ce filtre évaluera la date de DERNIÈRE qu'un utilisateur a envoyé un SMS entrant qui se trouve dans une des catégories de mots-clés.

!\[picture\]\[6\]

### Déclencher les messages par mot clé

Les messages peuvent être déclenchés lorsque les utilisateurs envoient des messages entrants en fonction de catégories de mots clés (l'utilisateur a envoyé n'importe lequel des mots-clés) ou d'autres mots-clés (l'utilisateur a envoyé un mot clé qui ne tombe pas dans l'une des catégories existantes). Ces déclencheurs sont définis dans l'étape de livraison du constructeur de campagne.

__Déclencher par mot clé entrant__<br> !\[picture\]\[7\]{: style="margin-top:10px;"}

__Trigger by arbitrary keywords__<br> Note when triggering a message on an "Other" keyword response, you will have the opportunity to evaluate the keyword body on an exact text match. Cette correspondance suit les mêmes règles que celles indiquées ci-dessus : seul le message __exact, à mot unique__ sera traité (cas _insensible_). Un mot clé envoyé de `Bonjour le Brésil !` ne correspond pas aux critères indiqués dans l'exemple ci-dessous. !\[picture\]\[8\]{: style="margin-top:10px;"}

__Mots clés du modèle__<br> Lors du déclenchement d'une campagne ou d'une étape de Canvas sur un SMS ou un MMS entrants, vous pouvez éventuellement modéliser le texte et/ou les pièces jointes que votre utilisateur a envoyées dans le corps de votre campagne ou Canvas avec Liquid. Cela vous permettra d'accéder à la réponse de l'utilisateur que vous pourrez ensuite inclure dans votre réponse, appliquer la logique conditionnelle à ou à tout autre chose que vous pouvez faire avec Liquid.

\[picture\]\[16\]{: style="max-width:80%;"} <br><br> !\[picture\]\[17\]{: style="max-width:80%;"}
[1]: {% image_buster /assets/img/sms/filter1.png %} [2]: {% image_buster /assets/img/sms/filter2. ng %} [3]: {% image_buster /assets/img/sms/trigger.png %} [6]: {% image_buster /assets/img/sms/retargeting1. ng %} [7]: {% image_buster /assets/img/sms/retargeting2.png %} [8]: {% image_buster /assets/img/sms/retargeting3. ng %} [16]: {% image_buster /assets/img/keyword_example1.jpg %} [17]: {% image_buster /assets/img/keyword_example2.jpg %}
