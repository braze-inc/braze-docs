---
nav_title: Accessibilité
article_title: Accessibilité
platform: Web
page_order: 22
page_type: reference
description: "Cet article explique comment Braze favorise l'accessibilité."

---

# Accessibilité

> Cet article présente un aperçu de la manière dont Braze favorise l'accessibilité au sein de votre intégration.

Le SDK Web Braze est conforme aux normes définies par les [directives d'accessibilité du contenu Web (WCAG 2.1)](https://www.w3.org/TR/WCAG21/). Nous maintenons un [score Lighthouse de 100/100](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) pour les cartes de contenu et les messages in-app sur toutes nos nouvelles versions afin de respecter notre norme d'accessibilité.

## Conditions préalables

La version minimale du SDK conforme à la norme WCAG 2.1 est proche de la version 3.4.0. Cependant, nous recommandons de procéder à une mise à niveau vers la version 6.0.0 au minimum afin de bénéficier des corrections majeures apportées aux étiquettes d'image.

### Corrections notables en matière d'accessibilité

| Version | Type | Principaux changements |
|---------|------|-------------|
| **6.0.0** | **Major** | Images en tant que`<img>`tags ou`language`champs`imageAltText`, améliorations générales de l'accessibilité de l'interface utilisateur |
| **3.5.0** | Mineur | Améliorations apportées à l'accessibilité du texte défilable |
| **3.4.0** | Correctif | Carte de contenu  `article`Correction de rôle |
| **3.2.0** | Mineur | Cibles tactiles minimales de 45 x 45 pixels pour les boutons |
| **3.1.2** | Mineur | Texte alternatif par défaut pour les images |
| **2.4.1** | **Major** | HTML sémantique (`h1`ou `button`), attributs ARIA, navigation au clavier, gestion du focus |
| **2.0.5** | Mineur | Gestion du focus, navigation au clavier, étiquettes |
{: .reset-td-br-1, .reset-td-br-2 role="presentation" }

## Fonctionnalités d'accessibilité prises en charge

Nous prenons en charge les fonctionnalités suivantes pour les cartes de contenu et les messages in-app :

- Rôles et étiquettes ARIA
- Prise en charge de la navigation au clavier
- Gestion de la concentration
- Annonces du lecteur d'écran
- Prise en charge du texte alternatif pour les images

## Directives d'accessibilité pour les intégrations SDK

Veuillez vous référer à [la section Création de messages accessibles dans Braze]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/accessibility) pour obtenir des directives générales en matière d'accessibilité. Ce guide fournit des conseils et des bonnes pratiques pour optimiser l'accessibilité lors de l'intégration du SDK Web Braze dans votre application Web.

### Cartes de contenu

#### Définition d'une hauteur maximale

Afin d'éviter que les cartes de contenu n'occupent trop d'espace vertical et d'améliorer l'accessibilité, vous pouvez définir une hauteur maximale pour le conteneur du flux, comme dans l'exemple suivant :

{% raw %}
```css
/* Limit the height of the Content Cards feed */
.ab-feed {
  max-height: 600px; /* Adjust to your needs */
  overflow-y: auto;
}

/* For inline feeds (non-sidebar), you may want to limit individual cards */
.ab-card {
  max-height: 400px; /* Optional: limit individual card height */
  overflow: hidden;
}
```
{% endraw %}

#### Considérations relatives à la fenêtre d'affichage

Pour les cartes de contenu affichées en ligne, veuillez tenir compte des contraintes de la fenêtre d'affichage, comme dans cet exemple.

{% raw %}
```css
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
  body > .ab-feed {
    max-height: 80vh; /* Leave space for other content */
  }
}
```
{% endraw %}

### in-app Messages

{% alert warning %}
Veuillez éviter d'inclure des informations importantes dans les messages in-app, car ils ne sont pas accessibles aux lecteurs d'écran.
{% endalert %}

### Considérations relatives aux appareils mobiles

#### Conception réactive

Le SDK comprend des points d'arrêt réactifs. Veuillez vérifier que vos personnalisations s'adaptent à toutes les tailles d'écran, comme dans l'exemple suivant :

{% raw %}
```css
/* Mobile-specific accessibility considerations */
@media (max-width: 768px) {
  /* Ensure readable font sizes */
  .ab-feed {
    font-size: 14px; /* Minimum 14px for mobile readability */
  }
  
  /* Ensure sufficient touch targets */
  .ab-card {
    padding: 16px; /* Adequate padding for touch */
  }
}
```
{% endraw %}

### Évaluation de l'accessibilité

#### Liste de contrôle pour les tests manuels

Veuillez vérifier manuellement l'accessibilité en effectuant les tâches suivantes :

- Naviguez dans les cartes de contenu et les messages in-app à l'aide du clavier uniquement (Tabulation, Entrée, Espace)
- Veuillez tester avec un lecteur d'écran (NVDA, JAWS, VoiceOver).
- Veuillez vérifier que toutes les images disposent d'un texte alternatif.
- Vérifiez les rapports de contraste des couleurs (utilisez des outils tels que WebAIM Contrast Checker).
- Veuillez tester sur les appareils mobiles dotés d'un écran tactile.
- Veuillez vérifier que les indicateurs de mise au point sont bien visibles.
- Test du piégeage du focus des messages dans les fenêtres modales/boîtes de dialogue modales, etc.
- Veuillez vérifier que tous les éléments interactifs sont accessibles à l'aide d'un clavier.

### Problèmes courants d'accessibilité

Pour éviter les problèmes courants d'accessibilité, veuillez suivre les instructions suivantes :

1. **Conserver les styles de mise au point :** Les indicateurs de focus du SDK sont essentiels pour les utilisateurs de clavier.
2. **Veuillez utiliser uniquement`display: none` sur des éléments non interactifs :** Veuillez utiliser`visibility: hidden`  ou`opacity: 0`  pour masquer les éléments interactifs.
3. **Veuillez ne pas remplacer les attributs ARIA :** Le SDK définit les rôles et les étiquettes ARIA appropriés.
4. **Utilisez`tabindex`les attributs :** Ces touches contrôlent l'ordre de navigation au clavier.
5. **Veuillez fournir un défilement si vous définissez `overflow: hidden`:** Veuillez vérifier que le contenu déroulant reste accessible.
6. **Veuillez ne pas interférer avec les gestionnaires de clavier intégrés :** Veuillez vérifier que la navigation au clavier fonctionne correctement.