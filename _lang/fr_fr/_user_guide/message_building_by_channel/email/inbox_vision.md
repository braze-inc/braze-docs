---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 9
description: "Cette page explique comment configurer Inbox Vision, une fonctionnalité qui permet aux marketeurs de visualiser leurs e-mails du point de vue de divers clients de messagerie et appareils mobiles."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision

> Inbox Vision vous permet de visualiser vos e-mails du point de vue de différents clients de messagerie et appareils mobiles. Par exemple, vous pouvez tester les différences entre les modes sombre et lumineux pour confirmer que vos e-mails s'affichent comme prévu.

{% alert important %}
Inbox Vision peut ne pas fonctionner si le contenu de votre e-mail repose sur des données de modélisation telles que les données du profil utilisateur. Braze crée un modèle d'utilisateur vide lors de l'envoi d'e-mails pour cette fonctionnalité.<br><br>Ajoutez des valeurs par défaut à n'importe quel liquide de votre message e-mail. En l'absence de valeurs par défaut, vous risquez de recevoir un faux positif ou de voir le test échouer.
{% endalert %}

## Considérations

En général, votre e-mail ne fonctionnera pas avec Inbox Vision si le contenu de votre e-mail repose sur des informations de modélisation, telles que les informations du profil utilisateur. En effet, Braze crée un modèle d'utilisateur vide lorsque nous envoyons des e-mails à l'aide de cette fonctionnalité.

Vous pouvez résoudre ce problème en ajoutant des valeurs par défaut ou des valeurs quelconques au Liquid dans votre message e-mail avant d'exécuter Inbox Vision. Lorsque vous avez terminé le test dans Inbox Vision, le message e-mail original s'affiche. Si aucune valeur n'est fournie, le test peut échouer dans le rendu des aperçus.

Votre entreprise a fixé une limite au nombre d'e-mails que vous pouvez prévisualiser avec Inbox Vision. Vous pouvez contrôler cela dans l'onglet " **Aperçu des e-mails"** de la boîte de réception.

Incluez une ligne d'objet et un domaine d'envoi valide pour voir les aperçus. Tenez compte des différences de rendu entre les ordinateurs de bureau et les téléphones portables. Utilisez les aperçus pour confirmer que l'e-mail apparaît comme prévu.

Pour tester votre message e-mail dans la boîte de réception Vision :

1. Allez dans votre éditeur par glisser-déposer ou dans votre éditeur d'e-mails HTML.
2. Dans votre éditeur, sélectionnez **Aperçu & Test.**
3. Sélectionnez **Boîte de réception**.
4. Sélectionnez **Exécuter la vision de la boîte de réception**. Cette opération peut durer jusqu'à dix minutes.
5. Ensuite, sélectionnez une tuile pour afficher l'aperçu plus en détail. Ces aperçus sont regroupés dans les sections suivantes : **Clients web**, **clients applicatifs** et **clients mobiles**.

![L'option permettant de sélectionner les clients d'e-mail à prévisualiser.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5\. Sélectionnez **Exécuter la vision de la boîte de réception**. Cela peut prendre de deux à dix minutes.

{% alert note %}
La boîte de réception Vision ne prend pas en charge les messages e-mail comportant une [logique d'abandon]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages), car ces e-mails s'affichent sous forme de contenu statique.
{% endalert %}

### Prévisualisation en tant qu'utilisateur

Lorsque vous effectuez une prévisualisation en tant qu'utilisateur aléatoire, Vision Boîte de réception n'enregistre pas les paramètres ou attributs spécifiques à l'utilisateur (tels que le nom ou les préférences). Lorsque vous sélectionnez un utilisateur personnalisé, l'aperçu de Vision Boîte de réception peut différer des autres aperçus car il utilise des données utilisateur spécifiques.

## Analyse des codes

L'analyse du code met en évidence les problèmes HTML potentiels, indique le nombre d'occurrences et signale les éléments HTML non pris en charge.

### Visualisation des informations relatives à l'analyse du code

Vous trouverez ces informations dans l'onglet **Vision de la boîte de réception** en sélectionnant <i class="fas fa-list"></i> **Vue de la liste**. La vue en liste n'est disponible que pour les modèles d'e-mail HTML. Pour les modèles glisser-déposer, utilisez plutôt les aperçus pour résoudre les problèmes.

![Exemple d’analyse de code sur l’aperçu d’Inbox Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
L'analyse du code peut apparaître plus rapidement que l'aperçu pour un client donné, car Braze attend l'arrivée de l'e-mail pour effectuer la capture d'écran.
{% endalert %}

## Tests de courrier indésirable

Les tests de courrier indésirable prédisent si votre e-mail atterrit dans les dossiers de spam ou dans les boîtes de réception. Braze effectue des tests sur les principaux filtres anti-spam (IronPort, SpamAssassin, Barracuda) et sur les principaux filtres des FAI (Gmail.com, Outlook.com).

### Consultation des résultats des tests courrier indésirable

Pour vérifier les résultats de votre test courrier indésirable :

1. Sélectionnez l'onglet **Tests courrier indésirable** dans la section **Vision de la boîte de réception**. Le tableau **Résultat du test de courrier** indésirable répertorie le nom, l'état et le type du filtre anti-spam.
2. Examinez ces résultats et apportez les ajustements nécessaires à votre campagne d'e-mail.
3. Sélectionnez **Réexécuter le test** pour recharger les résultats de votre test de courrier indésirable.

## Tests d'accessibilité

Les tests d'accessibilité mettent en évidence les problèmes d'accessibilité potentiels dans votre e-mail et indiquent les éléments qui ne répondent pas aux normes. Braze analyse le contenu en fonction de certaines directives d'accessibilité au contenu Web[(WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/), un ensemble de normes internationalement reconnues développées par le W3C pour rendre le contenu Web plus accessible.

### Fonctionnement

Lorsque vous exécutez Inbox Vision, Braze vérifie automatiquement les problèmes d'accessibilité courants dans l'[ensemble de règles WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (tels que l'absence de texte alt, le contraste insuffisant des couleurs, la structure incorrecte des titres) et classe la gravité pour vous aider à prioriser les correctifs. 

{% alert important %}
Les tests d'accessibilité peuvent être utilisés pour soutenir les efforts de conformité du client aux réglementations ou aux lois telles que la [loi européenne sur l'accessibilité](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers); toutefois, le client reconnaît que Braze ne fait aucune déclaration ni ne donne aucune garantie quant au fait que l'utilisation des tests d'accessibilité satisfasse ou non les obligations de conformité du client, et décline toute responsabilité à cet égard.
{% endalert %}

### Visualisation des résultats des tests d'accessibilité

Les tests d'accessibilité génèrent des résultats pour chaque règle (réussite, échec ou besoin de révision) dans l'onglet **Tests d'accessibilité.**  Braze classe chaque règle à l'aide de POUR (Perceivable, Operable, Understandable, Robust), les quatre principes qui sous-tendent les WCAG.

#### Catégories de POUR

La boîte de réception Vision classe les problèmes selon les quatre [principes](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility) fondamentaux du [POUR :](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility) Perceptible, exploitable, compréhensible et robuste.

| Principe | Définition |
| --- | --- |
| Perceptible | Les informations et les composants de l'interface utilisateur doivent être présentés aux utilisateurs de manière à ce qu'ils puissent les percevoir.<br><br>Les utilisateurs doivent être en mesure de percevoir les informations présentées (elles ne doivent pas être invisibles pour tous leurs sens). |
| Opérationnel | Les composants de l'interface utilisateur et la navigation doivent être opérationnels.<br><br>Les utilisateurs doivent être en mesure d'utiliser l'interface (l'interface ne peut pas exiger une interaction qu'un utilisateur ne peut pas réaliser). |
| Compréhensible | Les informations et le fonctionnement de l'interface utilisateur doivent être compréhensibles.<br><br>Les utilisateurs doivent être en mesure de comprendre les informations ainsi que le fonctionnement de l'interface utilisateur (le contenu ou le fonctionnement ne doit pas être hors de leur portée). |
| Robuste | Le contenu doit être suffisamment robuste pour pouvoir être interprété de manière fiable par une grande variété d'agents utilisateurs, y compris les technologies d'assistance.<br><br>Les utilisateurs doivent pouvoir accéder au contenu au fur et à mesure de l'avancement des technologies (au fur et à mesure que les technologies et les agents utilisateurs évoluent, le contenu doit rester accessible). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Niveaux de gravité

Inbox Vision classe les problèmes d'accessibilité par degré de gravité pour vous aider à hiérarchiser les mesures correctives.

| État | Définition |
| --- | --- |
| Critical (Critique) | Les problèmes qui peuvent bloquer l'accès au contenu ou aux fonctionnalités pour les utilisateurs handicapés. Ces problèmes sont les plus graves et doivent être résolus en priorité. |
| Grave | Les problèmes qui peuvent causer des obstacles importants, mais qui ne bloquent pas complètement l'accès. Ces questions doivent être traitées rapidement. |
| Modéré | Les problèmes qui peuvent entraîner des difficultés pour les utilisateurs handicapés, mais qui sont moins susceptibles de bloquer complètement l'accès. |
| Mineur | Problèmes ayant un impact relativement faible sur l’accessibilité et pouvant entraîner seulement des désagréments mineurs. |
| Besoin de révision | Impossible de détecter s'il y a un problème ou non. Cela peut se produire lorsque nous ne sommes pas en mesure de déterminer le rapport de contraste alors que le texte est placé sur une image de fond. Vous devez procéder à un examen manuel car il ne peut pas être déterminé automatiquement. |
| Réussi(s) | Répond aux normes WCAG A, AA ou aux meilleures pratiques en matière d'accessibilité. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
L'éditeur par glisser-déposer ne prend pas en charge la définition d'un élément de document `<title>`, de sorte que l'analyseur d'accessibilité échoue toujours à cette vérification.<br><br>Cette limitation fait l'objet d'un suivi en vue d'améliorations futures. Si cela affecte vos flux de travail ou vos utilisateurs, [faites-nous part de vos commentaires]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) afin que nous puissions prioriser les correctifs ayant un impact.
{% endalert %}

### Comprendre les tests d'accessibilité automatisés

{% multi_lang_include accessibility/automated_testing.md %}

## Bonnes pratiques

### Révisez votre liste d'utilisateurs abonnés à l'e-mail

Consultez le [tableau de bord des informations sur les e-mails]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard#email-insights-dashboard) pour déterminer le type d'appareil et les fournisseurs les plus populaires sur lesquels vos abonnés s'engagent. Si vous avez besoin de plus de granularité, comme le navigateur, le modèle d'appareil, et plus encore, vous pouvez exploiter vos données [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ou [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder) pour récupérer ce niveau de détail sur l'engagement récent de vos utilisateurs dans les e-mails.

Sinon, Braze propose par défaut les 20 meilleurs aperçus basés sur les données générales du secteur et des experts, ce qui couvre la majorité des endroits où vos abonnés s'engagent avec vos e-mails. Si votre analyse de données pointe vers d'autres aperçus plus populaires, vous pouvez définir un ensemble d'aperçus par défaut à chaque fois que vous exécutez Inbox Vision.

### Sélectionnez des aperçus significatifs et des aperçus impactés

Si votre entreprise est principalement basée aux États-Unis, il peut y avoir des aperçus spécifiques, tels que des aperçus internationaux comme GMX.de, qui ne sont utilisés que par un nombre nominal d'utilisateurs. Nous vous recommandons de donner la priorité et d'optimiser les boîtes de réception dont l'impact sur les abonnés est important et de réserver vos aperçus aux boîtes de réception dont l'impact est plus important.

Lorsque vous effectuez des corrections qui affectent des aperçus spécifiques, veillez à ne sélectionner que les aperçus concernés afin d'éviter de consommer des aperçus inutilisés.

### Lancez Inbox Vision sur la version finale de l'e-mail.

Nous vous conseillons d'exécuter Inbox Vision lorsque le message e-mail est prêt pour la production ou presque. Cela vous permet de réduire le nombre d'aperçus générés, car l'e-mail passe par plusieurs itérations avant d'être finalisé et prêt à être envoyé aux utilisateurs.

L'exécution de Inbox Vision à chaque fois que vous modifiez quelque chose peut consommer rapidement les aperçus. Nous vous conseillons de commencer par apporter toutes les modifications nécessaires à l'e-mail, puis d'exécuter Inbox Vision pour voir comment toutes vos modifications peuvent affecter le rendu de votre e-mail dans les différents environnements.

Braze effectue des tests avec des clients d'e-mail réels et veille à ce que les rendus soient exacts. Si vous constatez systématiquement un problème avec un client, ouvrez un [ticket d'assistance.]({{site.baseurl}}/braze_support/)
