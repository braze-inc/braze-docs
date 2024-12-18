---
nav_title: Recopilación de IDFV
article_title: Recopilación de IDFV
platform: Swift
page_type: reference
description: "En este artículo de referencia se describe cómo recoger el campo opcional IDFV para el SDK Swift."
page_order: 4

---

# Recopilación de IDFV 

## Fondo

En versiones anteriores del SDK de Braze para iOS, el campo IDFV (identificador del proveedor) se recogía automáticamente como ID del dispositivo del usuario. A partir de la versión 5.7.0 del SDK Swift, el campo IDFV podía desactivarse opcionalmente y, en su lugar, Braze establecería un UUID aleatorio como ID del dispositivo. A partir de la versión 7.0.0 del SDK Swift, el campo IDFV no se recogerá de manera predeterminada y, en su lugar, se establecerá un UUID como ID del dispositivo.

La característica `useUUIDAsDeviceId` configura el [SDK Swift](https://github.com/braze-inc/braze-swift-sdk) para establecer el ID del dispositivo como UUID. Tradicionalmente, el SDK de iOS asignaba el ID del dispositivo igual al valor IDFV generado por Apple. Con esta característica habilitada por defecto en tu aplicación para iOS, a todos los nuevos usuarios creados a través del SDK se les asignaría un ID de dispositivo igual a un UUID.

Si aún deseas recopilar el IDFV por separado, puedes hacerlo a través del SDK Swift, como se indica [aquí](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

## Consideraciones

### Versión del SDK

En la versión 7.0.0+ del SDK Swift, cuando `useUUIDAsDeviceId` está habilitado (predeterminado), a todos los nuevos usuarios creados se les asignará un ID de dispositivo aleatorio. Todos los usuarios existentes anteriormente mantendrán su mismo valor de ID de dispositivo, que puede haber sido IDFV.

Si esta característica no está habilitada, se seguirá asignando IDFV a los dispositivos al crearlos.

### Más adelante en el proceso 

**Socios tecnológicos**: Cuando se habilite esta característica, los socios tecnológicos que obtengan el valor IDFV del ID del dispositivo Braze dejarán de tener acceso a estos datos. Si el valor IDFV derivado del dispositivo es necesario para tu integración del socio, te recomendamos que configures esta característica como verdadero.

**Currents**: `useUUIDAsDeviceId` en verdadero significa que el ID del dispositivo enviado en Currents ya no será igual al valor de IDFV.

## Preguntas más frecuentes

#### ¿Este cambio afectará a mis usuarios actuales en Braze?
No. Cuando esté habilitada, esta característica no sobrescribirá ningún dato de usuario en Braze. Solo los dispositivos recién creados (o después de llamar a `wipedata()`) generarán nuevos ID de dispositivo UUID.

#### ¿Puedo desactivar esta característica después de encenderla?
Sí, esta característica se puede alternar entre activarla y desactivarla a tu discreción. Los ID de dispositivo almacenados anteriormente nunca se sobrescribirán.

#### ¿Puedo seguir recopilando el valor IDFV a través de Braze en otro lugar?
Sí, aún puedes recopilar opcionalmente el IDFV a través del SDK de Swift (la recopilación está desactivada por defecto). 
