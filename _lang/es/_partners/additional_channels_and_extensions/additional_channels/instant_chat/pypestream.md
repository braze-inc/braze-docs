---
nav_title: Pypestream
article_title: Pypestream
description: "Este artículo de referencia describe la asociación entre Braze y Pypestream, una plataforma de IA conversacional de pila completa que le permite mejorar el compromiso digital con su marca."
alias: /partners/pypestream/
page_type: partner
search_tag: Partner

---

# Pypestream

> [Pypestream](https://www.pypestream.com) es una plataforma de IA conversacional de stack completo que ofrece mensajería en la nube patentada y todo en uno para transformar las marcas en entidades digitales "siempre activas". Con Pypestream, las marcas ahora pueden entablar conversaciones omnicanal a escala con cada cliente mientras aprovechan una experiencia de usuario inmersiva, capacidades avanzadas de NLU e integraciones en tiempo real con sistemas backend.

_Esta integración está mantenida por Pypestream._

## Sobre la integración

La integración de Braze y Pypestream te permite orquestar fácilmente el ciclo de vida del cliente de extremo a extremo, desde la captación inicial hasta el seguimiento omnicanal a través de la reorientación inteligente. 

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Pypestream | Se requiere una [cuenta Pypestream](https://www.pypestream.com/contact-us/) para beneficiarse de esta asociación.<br><br>Una vez suscrito, el equipo de Pypestream le ayudará a configurar su entorno dedicado para empezar a crear su solución de IA conversacional para integrarla con Braze. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze  | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/api/basics/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

La asociación entre Braze y Pypestream puede utilizarse en tus Canvases para lograr casos de uso comunes como:
* **Redireccionamiento inteligente**: Vuelva a dirigirse a los usuarios con Braze Canvas después de su interacción conversacional con su marca aprovechando todos los puntos de datos enriquecidos recopilados a través de Pypestream.
* **Orientación dinámica**: Llegue a los clientes actuales y potenciales en función de sus cohortes y segmentos específicos, ofreciéndoles experiencias conversacionales personalizadas a través de Pypestream.
* **Información contextual sobre el cliente**: Después de que un usuario final (cliente existente o potencial) acceda a su sitio web, combine las etiquetas de la página web recibidas de Pypestream Event Listener con los datos del cliente almacenados en Braze para proporcionar una interacción conversacional totalmente personalizada y contextual.

## Integración

Pypestream aprovecha una capa de integración sin servidor para realizar integraciones personalizadas en diversas plataformas. Esta capa se utiliza para interactuar con los servicios o sistemas para apoyar los requisitos de datos del flujo conversacional que se está construyendo. Estas integraciones, denominadas integraciones de Action Node, se escriben normalmente en Python y se despliegan utilizando la plataforma Pypestream. Una vez instanciado un nodo de acción, ofrece la flexibilidad de integrarse en cualquier punto final de la API Braze y permite evaluar los resultados de muchas maneras. 

{% alert note %}
Visita este [artículo de Pypestream](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) para obtener una visión general y los pasos de configuración de los nodos de acción de Pypestream. Debe ser cliente de Pypestream para acceder a esta documentación.
{% endalert %}

### Paso 1: Establecer configuraciones de punto final

Los valores de configuración principales, como la URL del punto final REST de Braze y las claves de la API de Braze, deben establecerse en el archivo `app.py` de la solución: 

```
import os

NAME = '{ CUSTOMER NAME }'
BOTS = []
CSV_BOTS = ['{ SOLUTION NAME }']
PATH = os.path.dirname(__file__)

PARAMS = {
    'sandbox': {
        #Braze
        'braze_url': '{ BRAZE ENDPOINT URL }',
        'braze_api_key': '{ BRAZE API KEY }',
        'braze_user_track': 'users/track'
    },
    'prod': {

        #Braze
        'braze_url': '{ BRAZE ENDPOINT URL }',
        'braze_api_key': '{ BRAZE API KEY }',
        'braze_user_track': 'users/track'
    },
}
```

### Paso 2: Desarrollar una plantilla de nodos de acción

Los nodos de acción aprovechan el entorno con el que se despliega la solución para interactuar, con los respectivos puntos finales Braze establecidos en el paso anterior. Este paso desarrolla un nodo de acción para integrar puntos finales Braze específicos. Utilice la siguiente plantilla como guía para desarrollar las integraciones: 

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
Action Node Script for Braze Integration

Parameters
----------
POST Request to the User Track Braze Endpoint (users/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "users/track",
  "req_method": "POST",
  "req_headers": {
    "Authorization": "{YOUR-REST-API-KEY}"
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributes": [{
                "external_id": "{HOLDER_EMAIL}",
                ...
        }],
        "events": [
            ...
        ]
}

Returns
-------
Creates and/or Updates User Details within Braze dashboard

'''
import requests
from .. import app

class BrazeExample:
    def execute(self, log, payload=None, context=None):
        try:
            # initialize payload variables
            app_params = app.PARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    # include add'tl user details in this section
                    # refer to the Braze API Documentation for User Track REST API Endpoint for more details
                }],
                "events": [],
                "partner" : 'pypestream'
            }
            req_url = '{}/{}'.format(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests.post(req_url,
                                params=req_params,
                                headers=req_headers)
            
            log('BrazeExample API response: {}'.format(resp.text))

            if resp.status_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'.format(err))

        return {'success': 'error'}
```
### Paso 3: Actualizar los diseños de las soluciones

El paso final de la integración con la API REST de Braze consiste en configurar los flujos dentro de [Design Studio](https://platform.pypestream.com/design-studio/) de Pypestream para utilizar el nodo de acción que se desarrolló en el paso anterior. 

{% alert note %}
Visita este [artículo de Pypestream](https://pypestream.atlassian.net/servicedesk/customer/kb/view/669352070) para obtener un resumen sobre cómo configurar los modos en Design Studio. Debe ser cliente de Pypestream para acceder a esta documentación.
{% endalert %}

## Caso de uso de integración

Una vez cumplidos los requisitos previos y creada una estructura de nodos de acción, el desarrollador dispone de un lienzo en blanco desde el que trabajar cuando interactúa con los puntos finales de la API Braze. Este ejemplo muestra los pasos necesarios para integrar un nodo de acción en el [punto final `/user/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze, concretamente para crear un perfil de usuario que permita realizar un seguimiento de un usuario específico que entra en un flujo conversacional de Pypestream.

### Paso 1: Recoger datos del usuario en una conversación

Cuando un usuario entra en una sesión de Pypestream, los detalles de los datos recogidos dependen totalmente del caso de uso que se esté llevando a cabo. Para poder crear un perfil de usuario en Braze, la conversación debe recoger los campos necesarios
requerido por el punto final deseado.

Por ejemplo, si la solución recopiló la siguiente información del usuario durante la conversación para el punto final Braze `/user/track`: 

* Nombre
* Apellido
* Dirección de correo electrónico
* Fecha de nacimiento
* Ciudad de residencia
* Sistema operativo

Estos datos pueden enviarse ahora a la plataforma Braze para realizar un seguimiento de la participación de este usuario con la posibilidad de volver a dirigirse a él en el futuro. Consulte la [lista de casos de uso](#use-cases) para ver las aplicaciones más comunes.

### Paso 2: Rellenar datos en la estructura del nodo de acción

Aprovechando la misma estructura para desarrollar nodos de acción, los datos recopilados del usuario pueden rellenarse en el nodo de acción para enviarse a Braze a través de nuestro endpoint `/user/track`.

```
# -*- coding: utf-8 -*-
r'''
    ______  ______  _____________________  _________    __  ___
   / __ \ \/ / __ \/ ____/ ___/_  __/ __ \/ ____/   |  /  |/  /
  / /_/ /\  / /_/ / __/  \__ \ / / / /_/ / __/ / /| | / /|_/ /
 / ____/ / / ____/ /___ ___/ // / / _, _/ /___/ ___ |/ /  / /
/_/     /_/_/   /_____//____//_/ /_/ |_/_____/_/  |_/_/  /_/
Action Node Script for Braze Integration

Parameters
----------
POST Request to the User Track Braze Endpoint (users/track)

{
  "api_base_url": "{env.braze_url}",
  "req_endpoint_path": "users/track",
  "req_method": "POST",
  "req_headers": {
    "Content-Type": "application/json"
  },
  "req_body": {
        "api_key": "{env.braze_api_key}",
        "attributes": [{
                "external_id": "{HOLDER_EMAIL}",
                ...
        }],
        "events": [
            ...
        ],
        "partner" : 'pypestream'
}

Returns
-------
Creates and/or Updates User Details within Braze dashboard

'''
import requests
from .. import app

class BrazeExample:
    def execute(self, log, payload=None, context=None):
        try:
            # initialize payload variables
            app_params = app.PARAMS[context['env']]
            req_params = {
                "attributes": [{
                    "external_id": "{ USER_ID }",
                    "first_name": "{ FIRST_NAME }",
                    "last_name": "{ LAST_NAME }",
                    "email": "{ EMAIL_ADDRESS }",
                    "dob": "{ DATE_OF_BIRTH }",
                    "home_city": "{ CITY_OF_RESIDENCE }",
                    "operating_system": "{ OPERATING_SYSTEM }" #custom attributes can be added here as well
                    # include add'tl user details in this section
                    # refer to the Braze API Documentation for User Track REST API Endpoint for more details
                }],
                "events": [{
                    "external_id": "{ USER_ID }",
                    "name": "{ NAME_OF_EVENT }",
                    "time": "{ EVENT_TIME }"
                }],
                "partner" : 'pypestream'
            }
            req_url = '{}/{}'.format(
                app_params['braze_url'],
                app_params['braze_user_track']
            )
            req_headers = {
                "Authorization": app_params['braze_api_key']
                "Content-Type": "application/json"
            }

            resp = requests.post(req_url,
                                params=req_params,
                                headers=req_headers)
            
            log('BrazeExample API response: {}'.format(resp.text))

            if resp.status_code == 400:
                return {'success': 'error'}

            return {'success': 'true'}

        except Exception as err:
            log('BrazeExample Exception error: {}'.format(err))

        return {'success': 'error'}
```

### Paso 3: Actualizar los flujos de soluciones para redirigirlos en caso de éxito/fracaso del nodo de acción.

Por último, en el diseño de cada solución, puede dirigir a los usuarios a los nodos en función de si la llamada a la API del nodo de acción se ha realizado correctamente. Si el nodo de acción recibe un mensaje de error, el usuario final debe ser tratado con cuidado. 

