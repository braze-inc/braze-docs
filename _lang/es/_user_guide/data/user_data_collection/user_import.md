---
nav_title: Importación de usuarios
article_title: Importación de usuarios
page_order: 4
description: ""

---
# Importación de usuarios

> 

## 



Al importar datos a Braze destinados específicamente al uso de personalización en un navegador web, asegúrese de que estén desprovistos de HTML, JavaScript o cualquier otra etiqueta de secuencia de comandos que pueda ser aprovechada de forma malintencionada al visualizarse en un navegador web.

Alternativamente, para HTML, puedes utilizar los filtros Braze Liquid (`strip_html`) para escapar caracteres HTML del texto representado. Por ejemplo:

{% tabs local %}
{% tab Entrada %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Salida %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 

### 

 

|||||
|---|---|---|---|
|||||
|||||
|||||


### Importación de usuarios Lambda en CSV

 Esta solución funciona como un cargador de CSV en el que depositas tus CSV en un bucket de S3 y los scripts los cargan a través de nuestra API.

Los tiempos de ejecución estimados para un archivo con 1.000.000 de filas deberían rondar los cinco minutos. 

### API REST



### Ingesta de datos de Cloud



## 

{% multi_lang_include email-via-sms-warning.md %}
