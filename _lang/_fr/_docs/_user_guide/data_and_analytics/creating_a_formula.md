---
nav_title: Création d'une formule
article_title: Création d'une formule
page_order: 1.2
page_type: Référence
description: "Cet article de référence couvre la création et la gestion de formules qui vous aident à comprendre facilement les relations complexes qui existent dans vos données."
tool: Rapports
---

# Création d'une formule

## Que sont les formules ?

Les vues analytiques de Braze vous permettent maintenant de combiner plusieurs points de données ensemble pour fournir des informations précieuses sur vos données utilisateur. Les formules vous permettront de normaliser vos données de séries temporelles en fonction de votre nombre total de MAU/DAU ainsi que de comprendre facilement les relations complexes qui existent dans vos données. Par exemple, vous pouvez comparer combien d'événements personnalisés ont été complétés par des utilisateurs quotidiens actifs qui se qualifient pour un segment particulier par rapport à la population générale (ou par rapport à un autre segment).

## Où accéder à vos formules

Les formules peuvent être consultées dans les panneaux "Statistiques détaillées" sur la [Vue d'ensemble][9], [Pages de revenus][10] et [Événements personnalisés][11] dans le tableau de bord. Pour afficher ce panneau, changez la liste déroulante **Afficher les statistiques** à "Formulaires KPI".

!\[Choix de formule\]\[16\]

## Comment créer une nouvelle formule

Pour créer une nouvelle formule, accédez au tableau de bord approprié (Aperçu, Revenu, ou Événements personnalisés) et cliquez sur **Gérer les formules** dans la section statistiques détaillées. À partir de là, entrez un nom pour votre formule et sélectionnez les numérateurs et les dénominateurs concernés. Enregistrez votre formule.

## Numérateurs et dénominateurs disponibles

### Tableau de bord d'utilisation de l'application
Les numérateurs disponibles sont :

* DAU
* Sessions

Les dénominateurs disponibles sont :

* MAU
* DAU
* Taille du segment

### Tableau de bord des revenus
Les numérateurs disponibles sont :

* Achats (tous)
* Sélectionnez Achats (par exemple une carte cadeau ou un identifiant de produit)

Les dénominateurs disponibles sont :

* DAU
* MAU

### Tableau de bord de l'événement personnalisé
Les numérateurs disponibles sont :

* Nombre d'événements personnalisés

Les numérateurs disponibles sont :

* MAU
* DAU
* Taille du segment (seuls les segments qui ont [le suivi d'analyse][17] activé peuvent être utilisés)

## Cas d'utilisation
Les formulaires, en particulier lorsqu'ils sont combinés avec des événements personnalisés, vous permettent de mieux comprendre les comportements des utilisateurs dans votre application. Les formules peuvent également donner un aperçu plus approfondi des modèles d'achat de segments, même si votre entreprise utilise des médias payés en collaboration avec Braze, . - Google Annonces ou TV. Voici quelques exemples de modèles de comportement qui peuvent être détectés en utilisant les formules :

* Applications de partage de trajets : Si vous avez un événement personnalisé lorsque l'utilisateur annule une course, configurer une fonction pour les courses annulées / DAU peut être utilisé pour trouver si certains segments d'utilisateurs ont tendance à annuler plus de courses que d'autres.
* Applications E-commerce : En configurant une fonction pour les achats d'un certain ID de produit / MAU, vous pouvez, par exemple, comparer la popularité d'un produit récemment promu entre les segments, même si toutes les promotions ne peuvent pas être suivies en utilisant Braze.
* Applications de médias utilisant des publicités : Si l'expérience des utilisateurs est interrompue par des publicités entre des clips vidéo ou audio, l'enregistrement des sorties de milieu de la publicité comme un événement personnalisé et le calcul du ratio des sorties de milieu publicitaire / DAU peut aider à trouver les meilleurs segments à cibler avec une campagne pour les abonnements premium sans publicité.
[16]: {% image_buster /assets/img_archive/kpi_forms.png %}

[9]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/understanding_your_app_usage_data/
[10]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[17]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/viewing_and_understanding_segment_data/#viewing-and-understanding-segment-data
