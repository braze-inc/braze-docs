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

> La boîte de réception Vision vous permet de visualiser vos e-mails depuis différents clients de messagerie et appareils mobiles. Par exemple, vous pouvez tester les différences entre les modes sombre et clair afin de vérifier que vos e-mails s'affichent correctement.

{% alert important %}
La boîte de réception peut ne pas fonctionner si le contenu de vos e-mails repose sur des informations provenant de modèles, telles que les données du profil utilisateur. Braze crée un modèle d'utilisateur vide lors de l'envoi d'e-mails pour cette fonctionnalité.<br><br>Veuillez ajouter des valeurs par défaut à tout Liquid dans votre message d'e-mail. Sans valeurs par défaut, vous pourriez obtenir un faux positif ou le test pourrait échouer.
{% endalert %}

## Considérations

En règle générale, votre e-mail ne fonctionnera pas avec Inbox Vision si son contenu repose sur des informations provenant de modèles, telles que les informations de profil utilisateur. En effet, Braze crée un modèle d'utilisateur vide lorsque nous envoyons des e-mails à l'aide de cette fonctionnalité.

Vous pouvez résoudre ce problème en ajoutant des valeurs par défaut ou n'importe quelle autre valeur au Liquid dans votre e-mail avant d'exécuter Inbox Vision. Une fois les tests terminés dans Inbox Vision, le message électronique d'origine s'affiche. Si aucune valeur n'est fournie, le test pourrait ne pas réussir à afficher correctement les aperçus.

Votre entreprise a fixé une limite au nombre d'e-mails que vous pouvez prévisualiser avec la boîte de réception Inbox Vision. Vous pouvez surveiller cela dans l'onglet **Aperçus des e-mails** de la boîte de réception Inbox Vision.

Veuillez inclure une ligne d'objet et un domaine d'envoi valide pour afficher les aperçus. Veuillez tenir compte des différences de rendu entre les ordinateurs de bureau et les appareils mobiles. Veuillez utiliser les aperçus pour vérifier que l'e-mail s'affiche correctement.

Pour tester votre message d'e-mail dans Inbox Vision :

1. Allez dans votre éditeur par glisser-déposer ou dans votre éditeur d'e-mails HTML.
2. Dans votre éditeur, veuillez sélectionner **Aperçu&  Test**.
3. Sélectionnez **Boîte de réception**.
4. Sélectionnez **Exécuter la vision de la boîte de réception**. Cela peut prendre jusqu'à dix minutes.
5. Ensuite, sélectionnez une tuile pour afficher l'aperçu plus en détail. Ces aperçus sont regroupés dans les sections suivantes : **Clients web**, **clients applicatifs** et **clients mobiles**.

![L'option permettant de sélectionner les clients de e-mail à prévisualiser.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5\. Sélectionnez **Exécuter la vision de la boîte de réception**. Cela peut prendre de deux à dix minutes.

{% alert note %}
La boîte de réception ne prend pas en charge les e-mails qui incluent [une logique d'interruption,]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) car ces e-mails sont affichés en tant que contenu statique.
{% endalert %}

### Prévisualisation en tant qu'utilisateur

Lorsque vous effectuez un aperçu en tant qu'utilisateur aléatoire, Inbox Vision n'enregistre pas les paramètres ou attributs spécifiques à l'utilisateur (tels que le nom ou les préférences). Lorsque vous sélectionnez un utilisateur personnalisé, l'aperçu de la boîte de réception peut différer des autres aperçus, car il utilise des données utilisateur spécifiques.

## Analyse des codes

L'analyse du code met en évidence les problèmes HTML potentiels, affiche le nombre d'occurrences et indique les éléments HTML non pris en charge.

### Visualisation des informations relatives à l'analyse du code

Veuillez trouver ces informations dans l'onglet **Vision de la** **boîte de réception** en sélectionnant <i class="fas fa-list"></i>**l'affichage Liste**. La vue en liste est uniquement disponible pour les modèles d'e-mails HTML. Pour les modèles glisser-déposer, veuillez utiliser les aperçus pour résoudre les problèmes.

![Exemple d’analyse de code sur l’aperçu d’Inbox Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
L'analyse du code peut apparaître plus rapidement que l'aperçu pour un client particulier, car Braze attend que l'e-mail arrive avant de prendre la capture d'écran.
{% endalert %}

## Tests de courrier indésirable

Les tests de courrier indésirable permettent de déterminer si votre e-mail sera classé dans les dossiers spam ou dans les boîtes de réception. Braze effectue des tests sur les principaux filtres anti-spam (IronPort, SpamAssassin, Barracuda) et les principaux filtres des FAI (Gmail.com, Outlook.com).

### Consultation des résultats des tests courrier indésirable

Pour consulter les résultats de votre test de courrier indésirable :

1. Sélectionnez l'onglet **Tests courrier indésirable** dans la section **Vision de la boîte de réception**. Le tableau **Résultat du test de courrier** indésirable répertorie le nom, l'état et le type du filtre anti-spam.
2. Veuillez examiner ces résultats et apporter les ajustements nécessaires à votre campagne par e-mail.
3. Sélectionnez **Réexécuter le test** pour recharger les résultats de votre test de courrier indésirable.

## Tests d'accessibilité

Les tests d'accessibilité mettent en évidence les problèmes d'accessibilité potentiels dans votre e-mail et indiquent les éléments qui ne sont pas conformes aux normes. Braze analyse le contenu par rapport à certaines directives d'accessibilité du contenu Web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), un ensemble de normes internationalement reconnues développées par le W3C afin de rendre le contenu Web plus accessible.

### Fonctionnement

Lorsque vous exécutez Inbox Vision, Braze vérifie automatiquement les problèmes d'accessibilité courants dans l'[ensemble de règles WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (tels que le texte alternatif manquant, le contraste de couleurs insuffisant, la structure des en-têtes inappropriée) et classe les problèmes par niveau de gravité afin de vous aider à hiérarchiser les corrections. 

{% alert important %}
Les tests d'accessibilité peuvent être utilisés pour aider le Client à se conformer à des réglementations ou lois telles que la [loi européenne sur l'accessibilité](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers) ; toutefois, le Client reconnaît que Braze ne fait aucune déclaration et n'offre aucune garantie quant à la conformité des tests d'accessibilité aux obligations du Client en matière de conformité, et décline toute responsabilité à cet égard.
{% endalert %}

### Visualisation des résultats des tests d'accessibilité

Les tests d'accessibilité génèrent des résultats pour chaque règle, indiquant si elle est conforme, non conforme ou nécessite une révision dans l'onglet **Tests d'accessibilité**. Braze classe chaque règle selon le modèle POUR (Perceptible, Utilisable, Compréhensible, Robuste), les quatre principes qui sous-tendent les WCAG.

#### Catégories de POUR

La boîte de réception classe les problèmes selon les quatre [principes](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility) fondamentaux [POUR](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility) : Perceptible, exploitable, compréhensible et robuste.

| Principe | Définition |
| --- | --- |
| Perceptible | Les informations et les composants de l'interface utilisateur doivent être présentés aux utilisateurs de manière à ce qu'ils puissent les percevoir.<br><br>Les utilisateurs doivent être en mesure de percevoir les informations présentées (elles ne doivent pas être invisibles pour tous leurs sens). |
| Opérationnel | Les composants de l'interface utilisateur et la navigation doivent être opérationnels.<br><br>Les utilisateurs doivent être en mesure d'utiliser l'interface (l'interface ne peut pas exiger une interaction qu'un utilisateur ne peut pas réaliser). |
| Compréhensible | Les informations et le fonctionnement de l'interface utilisateur doivent être compréhensibles.<br><br>Les utilisateurs doivent être en mesure de comprendre les informations ainsi que le fonctionnement de l'interface utilisateur (le contenu ou le fonctionnement ne doit pas être hors de leur portée). |
| Robuste | Le contenu doit être suffisamment robuste pour pouvoir être interprété de manière fiable par une grande variété d'agents utilisateurs, y compris les technologies d'assistance.<br><br>Les utilisateurs doivent pouvoir accéder au contenu au fur et à mesure de l'avancement des technologies (au fur et à mesure que les technologies et les agents utilisateurs évoluent, le contenu doit rester accessible). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Niveaux de gravité

Inbox Vision classe les problèmes d'accessibilité par niveau de gravité afin de vous aider à hiérarchiser les mesures correctives.

| État | Définition |
| --- | --- |
| Critical (Critique) | Les problèmes qui peuvent bloquer l'accès au contenu ou aux fonctionnalités pour les utilisateurs handicapés. Ces problèmes sont les plus graves et doivent être résolus en priorité. |
| Grave | Les problèmes qui peuvent causer des obstacles importants, mais qui ne bloquent pas complètement l'accès. Ces questions doivent être traitées rapidement. |
| Modéré | Les problèmes qui peuvent entraîner des difficultés pour les utilisateurs handicapés, mais qui sont moins susceptibles de bloquer complètement l'accès. |
| Mineur | Problèmes ayant un impact relativement faible sur l’accessibilité et pouvant entraîner seulement des désagréments mineurs. |
| Besoin de révision | Impossible de détecter s'il y a un problème ou non. Cela peut se produire lorsque nous ne sommes pas en mesure de déterminer le rapport de contraste alors que le texte est placé sur une image de fond. Il est nécessaire de procéder à une vérification manuelle, car cela ne peut être déterminé automatiquement. |
| Réussi(s) | Répond aux normes WCAG A, AA ou aux meilleures pratiques en matière d'accessibilité. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
L'éditeur par glisser-déposer ne prend pas en charge la configuration d'un élément de`<title>` document, de sorte que le scanner d'accessibilité échoue systématiquement à cette vérification.<br><br>Cette limitation est prise en compte pour de futures améliorations. Si cela affecte vos flux de travail ou vos utilisateurs, [veuillez nous faire part de vos commentaires]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) afin que nous puissions prioriser les corrections les plus importantes.
{% endalert %}

### Comprendre les tests d'accessibilité automatisés

{% multi_lang_include accessibility/automated_testing.md %}

## Bonnes pratiques

### Veuillez examiner votre liste d'utilisateurs abonnés à la newsletter.

Veuillez consulter le [tableau de bord des informations sur les e-mails]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard#email-insights-dashboard) afin de déterminer les types d'appareils et les fournisseurs les plus populaires auprès de vos utilisateurs abonnés. Si vous avez besoin d'informations plus détaillées, telles que le navigateur, le modèle d'appareil, etc., vous pouvez utiliser vos données [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ou [le générateur de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder) pour obtenir ce niveau de détail sur l'engagement récent de vos utilisateurs en matière d'e-mails.

Dans le cas contraire, Braze affiche par défaut les 20 aperçus les plus populaires, basés sur des données générales du secteur et des experts, qui couvrent la majorité des domaines dans lesquels vos utilisateurs abonnés interagissent avec vos e-mails. Si votre analyse des données indique d'autres aperçus plus populaires, vous pouvez définir un ensemble d'aperçus par défaut à chaque fois que vous exécutez Inbox Vision.

### Sélectionner les aperçus significatifs et les aperçus affectés

Si votre entreprise est principalement basée aux États-Unis, il peut exister des aperçus spécifiques, tels que des aperçus internationaux,GMX.de qui ne sont utilisés que par un nombre restreint d'utilisateurs. Nous vous recommandons de donner la priorité et d'optimiser les boîtes de réception ayant un impact considérable sur les utilisateurs abonnés et de réserver vos aperçus aux boîtes de réception à fort impact.

Lorsque vous effectuez des corrections qui affectent des aperçus spécifiques, veuillez vous assurer de ne sélectionner que les aperçus concernés afin d'éviter de consommer des aperçus inutilisés.

### Veuillez exécuter Inbox Vision sur la version finale de l'e-mail.

Nous vous recommandons d'utiliser Inbox Vision lorsque le message d'e-mail est prêt à être envoyé ou presque. Cela vous permet de réduire le nombre d'aperçus générés, car l'e-mail subit plusieurs itérations avant d'être finalisé et prêt à être envoyé aux utilisateurs.

L'exécution de Inbox Vision à chaque fois que vous modifiez ou changez quelque chose peut rapidement épuiser les aperçus. Nous vous recommandons d'effectuer d'abord toutes les modifications nécessaires à l'e-mail, puis d'exécuter Inbox Vision afin de prévisualiser l'impact de ces modifications sur le rendu de votre e-mail dans différents environnements.

Braze effectue des tests à l'aide de clients de e-mail réels et veille à ce que les rendus soient précis. Si vous rencontrez régulièrement un problème avec un client, veuillez ouvrir un [ticket d'assistance]({{site.baseurl}}/braze_support/).
