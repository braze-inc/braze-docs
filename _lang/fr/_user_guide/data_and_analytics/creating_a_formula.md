---
nav_title: Création d’une formule
article_title: Création d’une formule
page_order: 1.2
page_type: reference
description: "Cet article de référence couvre la création et la gestion des formules pour vous aider à comprendre facilement les relations complexes entre vos données."
tool: Reports

---
# Création d’une formule

## A quoi servent les formules ?

Les vues analytiques de Braze vous permettent désormais de combiner plusieurs points de données pour obtenir des informations précieuses sur vos données utilisateur. Les formules vous permettront de normaliser vos données de séries temporelles en fonction de votre nombre total de MAU/Utilisateurs actifs par jour, et de comprendre facilement les relations complexes entre vos données. Par exemple, vous pouvez comparer combien d’événements personnalisés ont été effectués par des utilisateurs actifs quotidiens qualifiés pour un segment spécifique, par rapport à l’ensemble des clients (ou par rapport à un autre segment).

## Pour accéder à vos formules

Les formules sont accessibles sur les panneaux « Statistiques détaillées » des pages [Overview][9], [Chiffre d’affaires][10] et [Événements personnalisés][11] du tableau de bord. Pour afficher ce panneau, modifiez la liste déroulante « **Afficher les statistiques pour** »  sur « Formules d’indicateurs clés de performance».

![Afficher les statistiques des formules d’indicateurs clés de performance sur le tableau de bord de Braze][16]

## Comment créer une nouvelle formule

Pour créer une nouvelle formule, naviguez jusqu’au tableau de bord approprié (Overview, Revenus ou Événements personnalisés) et cliquez sur **Gérer les formules** dans la section Statistiques Détaillées. À partir de là, entrez un nom pour votre formule et sélectionnez les numérateurs et dénominateurs appropriés. Enregistrez votre formule.

## Numérateurs et dénominateurs disponibles

### Tableau de bord d’utilisation de l’application
Les numérateurs disponibles sont :

* Utilisateurs actifs quotidiens (DAU)
* Sessions

Les dénominateurs disponibles sont :

* MAU
* Utilisateurs actifs quotidiens (DAU)
* Taille du segment

### Tableau de bord des revenus
Les numérateurs disponibles sont :

* Achats (tous)
* Sélectionnez Achats (par ex. une carte-cadeau ou un ID Produit)

Les dénominateurs disponibles sont :

* Utilisateurs actifs quotidiens (DAU)
* MAU

### Tableau de bord des événements personnalisés
Les numérateurs disponibles sont :

* Nombre d’événements personnalisés

Les numérateurs disponibles sont :

* MAU
* Utilisateurs actifs quotidiens (DAU)
* Taille du segment (seuls les segments avec [suivi analytique][17] activé peuvent être utilisés)

## Cas d’utilisation
Les formules, en particulier lorsqu’elles sont associées à des événements personnalisés, vous permettent de mieux comprendre les comportements des utilisateurs dans votre application. Les formules peuvent également donner des informations plus approfondies sur les tendances d’achat de vos segments, même si votre entreprise utilise des médias payants en même temps que Braze, comme Google Ads ou des publicités télévisées. Voici quelques exemples de types de comportements qui peuvent être détectés grâce aux Formules :

* Applications de co-voiturage : Si vous avez défini un événement personnalisé quand l’utilisateur annule un trajet, la configuration d’une fonction Trajets Annulés / Utilisateurs actifs par jour peut être utilisée pour déterminer si certains segments d’utilisateur ont plus tendance que d’autres à annuler leur taxi.
* Applications de commerce électronique : En configurant une fonction pour les achats d’un certain ID Produit/MAU, vous pouvez, par exemple, comparer la popularité entre les segments d’un produit qui a fait l’objet d’une promotion récente, même si toutes les promotions n’étaient pas suivies dans Braze.
* Applications média utilisant des publicités : Si l’expérience des utilisateurs est interrompue par des publicités entre des clips vidéo ou audio, enregistrer en tant qu’événement personnalisé les sorties pendant la publicité et calculer le ratio Sorties mi-publicité/Utilisateurs actifs par jour peut aider à identifier les meilleurs segments à cibler avec une campagne pour des abonnements premium sans publicité.

[9]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/understanding_your_app_usage_data/
[10]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[16]: {% image_buster /assets/img_archive/kpi_forms.png %}
[17]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/viewing_and_understanding_segment_data/#viewing-and-understanding-segment-data
