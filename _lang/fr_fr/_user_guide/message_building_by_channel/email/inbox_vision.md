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

> Inbox Vision vous permet de visualiser vos e-mails du point de vue de différents clients de messagerie et appareils mobiles. Par exemple, vous pouvez utiliser Inbox Vision pour tester les différences entre les modes sombre et lumineux afin de confirmer que vos e-mails sont parfaitement adaptés.

{% alert important %}
En général, votre e-mail ne fonctionnera pas avec Inbox Vision si le contenu de votre e-mail repose sur des informations de modélisation, telles que les informations du profil utilisateur. En effet, Braze modélise un utilisateur vide lorsque nous envoyons des e-mails à l’aide de cette fonctionnalité.<br><br>Assurez-vous d'avoir ajouté des valeurs par défaut à tous les liquides de votre message e-mail. Si aucune valeur par défaut n'est fournie, vous risquez de recevoir un faux positif ou de ne pas pouvoir exécuter le test.
{% endalert %}

## Tester votre e-mail dans Inbox Vision

Votre e-mail doit inclure une ligne d’objet et un domaine d’envoi valide afin de voir ces aperçus. Prenez garde au fait que votre e-mail peut s’afficher différemment sur les ordinateurs de bureau que sur les appareils mobiles. En affichant ces prévisualisations, vous pouvez vous assurer que le contenu de vos e-mails s’affiche comme vous le désirez.

Pour tester votre message e-mail dans Inbox Vision, procédez comme suit :

1. Allez dans votre éditeur par glisser-déposer ou dans votre éditeur d'e-mails HTML.
2. Dans votre éditeur, sélectionnez **Prévisualiser et tester**.
3. Sélectionnez **Boîte de réception**.
4. Sélectionnez **Exécuter la vision de la boîte de réception**. Cela peut prendre de deux à dix minutes.
5. Ensuite, sélectionnez une tuile pour afficher l'aperçu plus en détail. Ces aperçus sont regroupés dans les sections suivantes : **Clients web**, **clients applicatifs** et **clients mobiles**.

![Aperçu de la boîte de réception Vision pour l'éditeur HTML.]({% image_buster /assets/img_archive/inboxvision1.png %})

{: start="6"}
6\. Apportez des modifications à un modèle, si nécessaire.
7\. Sélectionnez **Ré-exécuter le test** pour voir les aperçus mis à jour.

{% alert note %}
Inbox Vision n'est pas pris en charge si votre message e-mail comprend une [logique d'abandon]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages), car ces e-mails sont affichés en tant que contenu statique.
{% endalert %}

### Prévisualisation en tant qu'utilisateur

Lorsque vous prévisualisez l'e-mail en tant qu'utilisateur aléatoire, les paramètres ou attributs spécifiques associés à un utilisateur, tels que son nom ou ses préférences, ne sont pas enregistrés pour les prévisualisations actuelles ou futures. Lorsque vous sélectionnez un utilisateur personnalisé, l'aperçu affiché dans Vision Boîte de réception peut différer de l'aperçu du message affiché ailleurs, car cette option utilise des données d'utilisateur spécifiques pour créer l'aperçu

## Analyse des codes

L’analyse des codes est un moyen pour Braze de mettre en évidence les problèmes qui peuvent exister avec votre HTML, indiquant le nombre d’occurrences de chaque problème et fournissant des informations sur les éléments HTML non pris en charge.

### Visualisation des informations relatives à l'analyse du code

Vous trouverez ces informations dans l'onglet **Vision de la boîte de réception** en sélectionnant <i class="fas fa-list"></i> **List view.** Cette vue de liste n'est disponible que pour les modèles d'e-mail HTML. Si vous utilisez des modèles d'e-mail à glisser-déposer, vérifiez plutôt les aperçus pour résoudre les éventuels problèmes.

![Exemple d'analyse de code sur la boîte réception Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
Parfois, l’analyse de code s’affiche plus rapidement que l’aperçu d’un client par e-mail particulier. C’est parce que Braze attend que l’e-mail arrive dans la boîte de réception avant de prendre la capture d’écran.
{% endalert %}

## Tests de courrier indésirable

Les tests de courrier indésirable visent à prédire si votre e-mail s’affichera dans les dossiers de courrier indésirable ou dans les boîtes de réception de vos clients. Les tests de courrier indésirable portent sur les principaux filtres anti-spam, tels que IronPort, SpamAssassin et Barracuda, ainsi que sur les principaux filtres des fournisseurs de services Internet (FAI), tels que Gmail.com et Outlook.com.

### Consultation des résultats des tests courrier indésirable

Pour vérifier les résultats de votre test courrier indésirable, procédez comme suit :

1. Sélectionnez l'onglet **Tests courrier indésirable** dans la section **Vision de la boîte de réception**. Le tableau **Résultat du test de courrier** indésirable répertorie le nom, l'état et le type du filtre anti-spam.

![Tableau des résultats des tests de courrier indésirable à trois colonnes : Nom, État et Type. Il existe une liste de filtres anti-spam et de filtres ISP qui ont passé les tests de courrier indésirable, ce qui indique que la campagne e-mail n'atterrira pas dans le dossier des spams.]({% image_buster /assets/img_archive/email_spam_testing.png %})

{: start="2"}
2\. Examinez ces résultats et apportez d'éventuels ajustements à votre campagne d'e-mail.
3\. Sélectionnez **Réexécuter le test** pour recharger les résultats de votre test de courrier indésirable.

## Tests d'accessibilité

Les tests d'accessibilité réalisés dans Inbox Vision mettent en évidence les informations relatives à l'accessibilité de vos e-mails afin de déterminer les éléments qui ne respectent pas les normes d'accessibilité. Il analyse le contenu de vos e-mails en fonction de certaines directives d'accessibilité au contenu Web[(WCAG).](https://www.w3.org/WAI/standards-guidelines/wcag/) Les WCAG sont un ensemble de normes techniques internationalement reconnues, élaborées par le World Wide Web Consortium (W3C) pour rendre le contenu des sites web plus accessible aux personnes handicapées. 

### Fonctionnement

Lorsque vous effectuez un test Inbox Vision, l'outil vérifie automatiquement les problèmes courants d'accessibilité des e-mails dans l'[ensemble des règles WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa), tels que l'absence de texte alt, le contraste insuffisant des couleurs et la structure incorrecte des titres, puis il classe la gravité de chaque problème pour vous aider à hiérarchiser les correctifs. 

{% alert important %}
Les tests d'accessibilité peuvent être utilisés pour aider le client à se conformer à des réglementations ou à des lois telles que la [loi européenne sur l'accessibilité](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers), mais le client reconnaît que Braze ne fait aucune déclaration et ne donne aucune garantie quant au fait que l'utilisation des tests d'accessibilité satisfasse ou non aux obligations de conformité du client, et décline toute responsabilité à cet égard.
{% endalert %}

### Visualisation des résultats des tests d'accessibilité

Les tests d'accessibilité génèrent des résultats pour chaque règle (réussite, échec ou besoin de révision) dans l'onglet **Tests d'accessibilité**. Chaque règle est classée selon les principes POUR (Perceivable, Operable, Understandable, Robust), qui sont les quatre grands principes qui sous-tendent les WCAG.

#### Catégories de POUR

Les questions sont classées selon les quatre [principes fondamentaux du POUR](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility) : Perceptible, exploitable, compréhensible et robuste. Chaque principe aborde un aspect différent de la conception accessible.

| Principe | Définition |
| --- | --- |
| Perceptible | Les informations et les composants de l'interface utilisateur doivent être présentés aux utilisateurs de manière à ce qu'ils puissent les percevoir.<br><br>Les utilisateurs doivent être en mesure de percevoir les informations présentées (elles ne doivent pas être invisibles pour tous leurs sens). |
| Opérationnel | Les composants de l'interface utilisateur et la navigation doivent être opérationnels.<br><br>Les utilisateurs doivent être en mesure d'utiliser l'interface (l'interface ne peut pas exiger une interaction qu'un utilisateur ne peut pas réaliser). |
| Compréhensible | Les informations et le fonctionnement de l'interface utilisateur doivent être compréhensibles.<br><br>Les utilisateurs doivent être en mesure de comprendre les informations ainsi que le fonctionnement de l'interface utilisateur (le contenu ou le fonctionnement ne doit pas être hors de leur portée). |
| Robuste | Le contenu doit être suffisamment robuste pour pouvoir être interprété de manière fiable par une grande variété d'agents utilisateurs, y compris les technologies d'assistance.<br><br>Les utilisateurs doivent pouvoir accéder au contenu au fur et à mesure de l'avancement des technologies (au fur et à mesure que les technologies et les agents utilisateurs évoluent, le contenu doit rester accessible). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Niveaux de gravité

Inbox Vision classe les problèmes d'accessibilité par degré de gravité afin de vous aider à hiérarchiser les mesures correctives.

| État | Définition |
| --- | --- |
| Critical (Critique) | Les problèmes qui peuvent bloquer l'accès au contenu ou aux fonctionnalités pour les utilisateurs handicapés. Ces problèmes sont les plus graves et doivent être résolus en priorité. |
| Grave | Les problèmes qui peuvent causer des obstacles importants, mais qui ne bloquent pas complètement l'accès. Ces questions doivent être traitées rapidement. |
| Modéré | Les problèmes qui peuvent entraîner des difficultés pour les utilisateurs handicapés, mais qui sont moins susceptibles de bloquer complètement l'accès. |
| Mineur | Problèmes ayant un impact relativement faible sur l’accessibilité et pouvant entraîner seulement des désagréments mineurs. |
| Besoin de révision | Impossible de détecter s'il y a un problème ou non. Cela peut se produire lorsque nous ne sommes pas en mesure de déterminer le rapport de contraste alors que le texte est placé sur une image de fond. Ce point devra être vérifié manuellement car il ne peut être déterminé automatiquement. |
| Réussi(s) | Répond aux normes WCAG A, AA ou aux meilleures pratiques en matière d'accessibilité. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
L'éditeur par glisser-déposer d'e-mails ne prend pas actuellement en charge la définition d'un élément de document `<title>`. Par conséquent, le scanner d'accessibilité échouera toujours à cette vérification.<br><br>
Nous suivons cette limitation en vue d'améliorations futures. Si cela affecte vos flux de travail ou vos utilisateurs, [faites-nous part de vos commentaires]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) afin que nous puissions prioriser les correctifs les plus importants.
{% endalert %}

### Comprendre les tests d'accessibilité automatisés

{% multi_lang_include accessibility/automated_testing.md %}

## Précision du test

Tous nos tests sont exécutés à l’aide de clients par e-mail réels. Braze s'efforce de vérifier que tous les rendus sont aussi précis que possible. Si vous constatez systématiquement un problème avec un client e-mail, ouvrez un [ticket d'assistance.]({{site.baseurl}}/braze_support/)
