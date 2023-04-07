---
nav_title: DataGrail
article_title: DataGrail
description: "Cet article de référence décrit le partenariat entre Braze et DataGrail, une plateforme de gestion de la confidentialité qui vous permet de détecter les données des consommateurs recueillies et stockées dans Braze pour traiter rapidement les DSR."
alias: /partners/datagrail/
page_type: partner
search_tag: Partenaire

---

# DataGrail

> [DataGrail](https://www.datagrail.io/), une plateforme de gestion de la confidentialité, aide à renforcer la confiance des consommateurs et à éliminer les activités risquées. Grâce à la détection continue du système et au traitement automatisé des restitutions de données des personnes concernées (DSR), DataGrail alimente les programmes de confidentialité, en prenant en charge la conformité aux lois et réglementations en constante évolution, telles que RGPD, CCPA et CPRA. 

L’intégration Braze et DataGrail vous permet de détecter les données des consommateurs collectées et stockées dans Braze pour traiter rapidement les DSR (demandes d’accès, de suppression et de non-vente). Braze sera ajouté à un plan précis de l'emplacement des données des consommateurs dans votre organisation avec un mappage automatisé des données. Plus besoin d'enquêtes ou de feuilles de calcul pour maintenir un cadre de confidentialité ou produire un enregistrement des activités de traitement (RoPA). 

## Conditions préalables

| Conditions | Description |
|---|---|
| Compte DataGrail | Un compte DataGrail est requis pour profiter de ce partenariat.<br>Contactez votre administrateur ou envoyez un e-mail à support@datagrail.io pour tout problème ou question concernant l'intégration. |
| Clé API Braze | Une clé API REST Braze avec des autorisations `events.list`, `users.export.ids`, `users.delete` et autorisations `users.track`.<br><br>Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Instance de Braze | Votre instance Braze peut être obtenue auprès de votre gestionnaire d’onboarding Braze ou est disponible sur la [page API overview]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Connectez-vous au portail DataGrail et cliquez sur **Connect (Connecter)** sur la page d'intégration de Braze. Ensuite, entrez votre instance et la clé API Braze et cliquez sur **Connect Braze (Connecter Braze)**.

S'il y a des comptes Braze supplémentaires à intégrer :
1. Cliquez sur **Edit Connection (Modifier la connexion)** sur la page d'intégration de Braze.
2. Dans le menu déroulant, sélectionnez **+Add New Connection (Ajouter une nouvelle connexion)**.
3. Sous **Connection Name (Nom de connexion)**, entrez un nouveau nom pour identifier ce compte distinct (par exemple, Braze Training Account (Compte de formation Braze)).
4. Entrez une instance Braze et une clé API distinctes pour ce nouveau compte.
5. Cliquez sur **Connect (Connexion)**.

Envoyez un e-mail à DataGrail à support@datagrail.io pour tout problème ou question concernant votre intégration.
