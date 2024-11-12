---
nav_title: Configuración de ID de usuario
article_title: Configuración de ID de usuario para Roku
platform: Roku
page_order: 0
page_type: reference
description: "En este artículo de referencia se cubren los métodos para identificar y establecer ID de usuario para Roku, así como las mejores prácticas y consideraciones importantes."
 
---

# Configuración de los ID de usuario

> En este artículo de referencia se cubren los métodos para identificar y establecer ID de usuario para Roku, así como las mejores prácticas y consideraciones importantes.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

Debes realizar la siguiente llamada en cuanto se identifique el usuario (generalmente después de iniciar la sesión) para establecer el ID de usuario:

```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```

## Convención de nomenclatura de ID de usuario sugerida

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Prácticas recomendadas y notas sobre la integración del ID de usuario

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

