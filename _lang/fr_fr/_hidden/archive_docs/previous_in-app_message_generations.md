---
nav_title: Générations précédentes
article_title: Générations précédentes de messages in-app
page_order: 20
page_type: reference
description: "Le présent article analyse des informations précédentes sur les messages in-app dans Braze."
channel: in-app messages
noindex: true
hidden : true
---

# Générations précédentes de messages in-app

{% alert important %}
Cette page analyse des informations précédentes sur nos messages in-app. Pour voir les informations les plus à jour sur notre génération actuelle de messages intégrés, consultez notre documentation actuelle sur les [messages intégrés]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/).
{% endalert %}

## Universel

Ceci analyse des informations précédentes sur nos messages in-app. Pour voir les informations les plus récentes sur notre génération actuelle de messages intégrés à l'application, consultez notre [documentation de présentation des messages intégrés à l'application]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/).

{% details Plein écran %}
Ils sont les plus attrayants, mais aussi les plus intrusifs, car ils occupent tout l’écran de votre utilisateur. Ils sont parfaits pour afficher de grandes images riches, et ils s’avèrent utiles pour transmettre des informations cruciales, telles que de nouvelles fonctionnalités clés et des promotions arrivant à terme. Sachant qu’ils perturbent davantage l’expérience utilisateur, utilisez-les avec modération pour le contenu prioritaire.

![Message en plein écran]({% image_buster /assets/img_archive/braze_fullscreen.png %}){: style="max-width:80%;"}

**Fonctionnalités personnalisables**

- En-tête et texte du corps
- Une grande image
- Jusqu'à deux boutons d'appel à l'action avec un comportement au clic et des liens profonds distincts.
- Des couleurs différentes pour l’en-tête et le texte du corps, les boutons et l’arrière-plan
- Paires clé-valeur

{% enddetails %}
{% details  Modal %}
Ces messages ne sont pas aussi intrusifs que ceux en plein écran, car ils permettent toujours aux utilisateurs de voir une partie de l’interface de votre application. Comme ils contiennent toujours des boutons et des images, les messages modaux peuvent constituer une option preferable aux slideups pour une campagne visuelle plus interactive. Ils sont parfaits pour le contenu de priorité moyenne, comme les mises à jour d’applications et les offres et événements non urgents.

![Message Modal]({% image_buster /assets/img_archive/braze_modal.png %}){: style="max-width:80%;"}

**Fonctionnalités personnalisables**

- En-tête et texte du corps
- Une icône d’image ou de badge personnalisable
- Jusqu'à deux boutons d'appel à l'action avec un comportement au clic et des liens profonds distincts.
- Des couleurs différentes pour l’en-tête et le texte du corps, les boutons et l’arrière-plan
- Paires clé-valeur

{% enddetails %}

{% details Diapositive traditionnelle %}
Il s’agit du type de message le moins intrusif, bien qu’il puisse attirer l’attention selon les couleurs et les icônes de badge employées. Cela peut être le format de message à utiliser lors de l'intégration de nouveaux utilisateurs et de les diriger vers des fonctionnalités spécifiques de l'application, car ils ne suspendent pas l'expérience de l'application et permettent une exploration continue.

![Message de glissement vers le haut]({% image_buster /assets/img_archive/stopwatch_slideup_IAM.gif %}){: style="max-width:50%;"}

**Fonctionnalités personnalisables**

- Texte du corps
- Une icône d’image ou de badge personnalisable
- Couleurs différentes pour l’arrière-plan, le texte et l’icône du slideup
- Comportement de fermeture du message
- Position du slideup (haut ou bas de l’écran de l’application)
- Paires clé-valeur

{% enddetails %}

<br>

## Web

Ceci analyse des informations précédentes sur des messages in-app plus personnalisés. Pour voir les informations les plus à jour sur notre génération actuelle de messages intégrés, consultez notre [documentation de personnalisation]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/).

{% details Message de capture d’e-mail %}
Les messages de capture d’e-mail vous permettent d’inviter facilement les utilisateurs de votre site à soumettre leur adresse e-mail, après quoi vous en disposerez dans le système Braze pour l’ensemble de vos campagnes de communication.

![Message de capture d'email]({% image_buster /assets/img_archive/web-email-capture.png %}){: style="max-width:60%;"}

>  Pour activer les messages in-app de capture d’e-mail via le SDK Web, vous devez fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze, par exemple, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Pour des raisons de sécurité, les messages in-app HTML peuvent en effet exécuter du JavaScript, d’où le besoin d’un responsable de site pour les activer.

**Fonctionnalités personnalisables**

- Texte de l’en-tête, du corps et du bouton Soumettre
- Une image facultative
- Un lien facultatif aux conditions de service
- Des couleurs différentes pour l’en-tête et le texte du corps, les boutons et l’arrière-plan
- Paires clé-valeur

{% enddetails %}

{% details Message HTML personnalisé %}

Bien que les messages in-app Braze soient personnalisés de diverses façons, vous pouvez contrôler encore davantage l’apparence et l’impression de vos campagnes à l’aide de messages conçus et élaborés avec HTML, CSS et JavaScript. Via à une composition simple, vous pouvez débloquer des fonctionnalités et des marques personnalisées pour répondre à vos besoins. Les messages in-app HTML offrent un contrôle accru de l’apparence et de l’impression d’un message, et tout ce qui est pris en charge par HTML5 l’est également par Braze.

**JavaScript Bridge (appboyBridge)**

Les messages in-app HTML prennent en charge une interface de pont Javascript vers le SDK Web Braze, ce qui vous permet de déclencher des actions Braze personnalisées lorsque les utilisateurs cliquent sur des éléments avec des liens ou montrent un engagement avec votre contenu. Les méthodes Javascript suivantes sont prises en charge dans les messages in-app HTML Braze :

{% multi_lang_include archive/appboyBridge.md platform="web" %}

En outre, pour le suivi des analyses, tous les éléments `<a>` ou `<button>` dans votre HTML enregistrent automatiquement une action de clic sur la campagne associée au message in-app. Pour enregistrer un "clic de bouton" au lieu d'un "clic de corps", fournissez soit une valeur de chaîne de requête de abButtonId sur le href de votre lien (par exemple, `<a href="http://mysite.com?abButtonId=0">click me</a>`), soit un identifiant sur l'élément HTML (par exemple, `<a id="0" href="http://mysite.com">click me</a>`). Notez que seuls les identifiants de bouton « 0 » et « 1 » sont actuellement acceptés. Un lien avec un identifiant de bouton de 0 sera représenté comme "Bouton 1" sur le tableau de bord, tandis qu'un lien avec un identifiant de bouton de 1 sera représenté comme "Bouton 2."

>  Pour activer les messages in-app HTML, votre intégration SDK doit fournir l’option d’initialisation à Braze `allowUserSuppliedJavascript`, par exemple, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Pour des raisons de sécurité, les messages in-app HTML peuvent en effet exécuter du JavaScript, d’où le besoin d’un responsable de site pour les activer.

{% enddetails %}

{% details Modèles de messages intégrés en HTML %}

Nous avons conçu un ensemble de modèles de messages in-app HTML5 pour vous aider à démarrer. Découvrez notre [répertoire GitHub](https://github.com/braze-inc/in-app-message-templates) qui contient des instructions détaillées sur la façon d'utiliser et de personnaliser ces modèles selon vos besoins.

**Fonctionnalités personnalisables**

- Polices
- Styles
- Images et vidéos
- Comportements lors du clic
- Composants interactifs

{% enddetails %}

<br>

## Spécifications

Cela examinera les informations précédentes concernant nos spécifications créatives de messages intégrés. Pour voir les informations les plus récentes sur notre génération actuelle de messages intégrés, consultez notre [documentation des spécifications créatives]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Limites de caractères et d’image

Pour tous les types de messages in-app répertoriés dans le tableau suivant, les directives supplémentaires suivantes s’appliquent :

- **Dimensions d'image recommandées :** 500 Ko 
- **Taille maximale de l'image :** 5 MO
- **Types de fichiers pris en charge :** PNG, JPEG, GIF

| Type                               | Rapport hauteur/largeur | Nombre max. de caractères |
| :--------------------------------- | :----------: | :-----------------: |
| Portrait plein écran (image uniquement)  |    10:16     |         240         |
| Portrait plein écran (avec texte)   |     5:4      |         240         |
| Paysage Plein écran (avec texte)  |     16:5     |         240         |
| Paysage plein écran (image uniquement) |    16:10     |         240         |
| Fenêtre contextuelle                            |     1:1      |         140         |
| Modal (Image uniquement)                 |     1:1      |         140         |
| Modal (avec texte)                  |    29:10     |         140         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Conservation de petites tailles de fichiers de messages in-app

Braze vous recommande de conserver les zips de vos images et ressources HTML aussi petits que possible pour plusieurs raisons :

- Les charges utiles HTML et d’images plus petites se téléchargent et s’affichent plus vite et de manière plus fiable pour vos clients.
- Les charges utiles HTML et d’images plus petites permettent également de réduire les coûts des données de vos clients. Les messages in-app Braze sont téléchargés en arrière-plan au début de la session pour pouvoir être déclenchés en temps réel selon les critères sélectionnés. Par conséquent, si vous avez 10 messages HTML in-app de 1 Mo chacun, vos clients devront tous payer 10 Mo de données, même s'ils n'ont jamais déclenché tous ces messages. La somme peut rapidement augmenter avec le temps, même si les messages in-app sont mis en cache et ne sont pas téléchargés à nouveau à chaque session.

Les stratégies suivantes sont utiles pour conserver de petites tailles de fichiers :

- Les polices de référence intégrées dans votre application ou site Web permettent de personnaliser vos messages in-app HTML au lieu de les inclure dans votre dossier ZIP de ressources HTML.
- Assurez-vous qu’aucun CSS ou Javascript superflu ou dupliqué ne figure dans vos zips de ressources HTML.
- Utilisez [ImageOptim][25] sur toutes les images pour les compresser à leur taille minimale possible sans réduction de qualité.

### Spécifications de l’iPhone 5

![Spécifications de l’iPhone 5][18]

### Spécifications de l’iPhone 6

![Spécifications de l’iPhone 6][19]


[18]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_05.png %}

[19]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_06.png %}

[25]: https://imageoptim.com/
