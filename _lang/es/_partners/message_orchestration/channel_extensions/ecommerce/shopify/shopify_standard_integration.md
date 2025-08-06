---
nav_title: ""
article_title: ""
description: ""
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration/
page_order: 1
---

# 

>  

## Paso 1: Conecta tu tienda Shopify

1. En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y busca "Shopify".

{% alert note %}

{% endalert %}

{: start="2"}
2\. <br><br><br><br> 
3\. <br><br>

{% alert note %}

{% endalert %}

{: start="4"}
4\.   <br><br>

{: start="5"}
5\. <br><br>

## Paso 2: 





 
- 
    - 
- 
    - Rastrear solo a los usuarios identificados
    - 

## Paso 3: 

### 







|  | Shopify eventos personalizados | Atributos personalizados de Shopify |
| --- | --- | --- |
| {::nomarkdown}<ul><li>Producto visto</li><li></li><li></li><li></li></ul>{:/}  | {::nomarkdown}<ul><li></li><li></li><li></li><li></li><li></li><li></li></ul>{:/} | {::nomarkdown}<ul><li></li><li></li><li></li><li></li><li></li><li></li><li></li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}



### 

  





|  | Shopify eventos personalizados | Atributos estándar Braze |  |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li></li></ul>{:/}  | {::nomarkdown}<ul><li></li><li></li><li></li><li></li><li></li><li></li></li></ul>{:/} | {::nomarkdown}<ul><li>Correo electrónico</li><li>Nombre</li><li>Apellido</li><li>Teléfono</li><li>Localidad</li><li>País</li></ul>{:/} | {::nomarkdown}<ul><li></li><li></li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

 

{% alert note %}

{% endalert %}

### 

 

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="width: 50%;">Eventos personalizados</th>
      <th style="width: 50%;">Atributos personalizados</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Usar un código de descuento personalizado</li>
          <li>Interactuar con una recomendación de productos personalizada</li>
          <li>Añadir un mensaje de regalo a su pedido</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Marcas o productos favoritos</li>
          <li>Categorías de compra preferidas</li>
          <li>Membresía o estado de fidelización</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

  

Por ejemplo, el siguiente fragmento de código de JavaScript rastrea si el usuario actual se suscribe a un boletín de noticias y lo registra como un evento personalizado en su perfil de Braze:

```json
braze.logCustomEvent(
  “subscribed_to_newsletter”,
  {
    newsletterName: ‘News and Offers’,
    customerEmail: ‘customer_1@gmail.com’,
    sendOffers: true
  }
);

```

 

## Paso 4: 

 



{% alert important %}
 <br><br>

-  Las direcciones de correo electrónico son fáciles de adivinar, lo que las hace vulnerables a los ataques.
-  Si un usuario malintencionado altera su navegador web para enviar la dirección de correo electrónico de otra persona como ID externo, podría acceder potencialmente a mensajes confidenciales o a información de la cuenta.
{% endalert %}

 

  



{% alert note %}
  <br><br>
-  
-  
{% endalert %}

## Paso 5: 

  



## Paso 6: 





### 



#### 

  

#### 

 



## Paso 7: Configuración de acabado

1. Después de configurar tu configuración, selecciona **Finalizar configuración**.
2.   



{: start="3"}
3\. 
 <br><br>

[1]: {% image_buster /assets/img/Shopify/begin_setup.png %}
[2]: {% image_buster /assets/img/Shopify/confirm_workspace1.png %}
[3]: {% image_buster /assets/img/Shopify/sdk_setup.png %}
[4]: {% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %}
[5]: {% image_buster /assets/img/Shopify/shopify_log_in.png %}
[6]: {% image_buster /assets/img/Shopify/tracking_shopify_data.png %}
[7]: {% image_buster /assets/img/Shopify/open_shopify.png %}
[8]: {% image_buster /assets/img/Shopify/install_complete.png %}
[9]: {% image_buster /assets/img/Shopify/choose_account.png %}
[10]: {% image_buster /assets/img/Shopify/collect_email_subscribers.png %}
[11]: {% image_buster /assets/img/Shopify/sync_products_step1.png %}
[12]: {% image_buster /assets/img/Shopify/configure_settings.png %}
[13]: {% image_buster /assets/img/Shopify/collect_email_subscribers_2.png %}