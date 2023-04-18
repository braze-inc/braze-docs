---
nav_title: Envoi en grand volume
article_title: Envoi de SMS en grand volume
page_order: 4
description: "Le présent article de référence couvre les meilleures pratiques d’envoi en grand volume pour la messagerie SMS."
page_type: reference
channel:
  - SMS
  
---

# Envoi en grand volume

> Prévoyez-vous un envoi en grand volume ? Cet article de référence énumère quelques bonnes pratiques pour vous assurer qu’il fonctionne correctement

- Ajustez les limites de débit de livraison pour votre campagne/Canvas si nécessaire, en fonction de la taille cible du public. Cela assurera que (1) vous atteindrez le volume d’envoi dont vous avez besoin et (2) Braze enverra les messages à la vitesse que les numéros de téléphone que vous avez provisionnés peuvent gérer
- Assurez-vous de coller à la limite de 160 caractères et soyez attentifs aux caractères spéciaux qui comptent double (c.-à-d., \ ^ &#126;). Les messages plus longs que 160 caractères créeront plusieurs messages, ce qui divise effectivement par deux la vitesse d’envoi.
