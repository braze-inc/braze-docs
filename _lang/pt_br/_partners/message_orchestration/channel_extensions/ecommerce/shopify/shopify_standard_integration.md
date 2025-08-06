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

## Etapa 1: Conecte sua loja da Shopify

1. Na Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e depois procure "Shopify".

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

## Etapa 2: 





 
- 
    - 
- 
    - Rastreia apenas usuários identificados
    - 

## Etapa 3: 

### 







|  | Eventos personalizados da Shopify | Atributos personalizados da Shopify |
| --- | --- | --- |
| {::nomarkdown}<ul><li>Produto visualizado</li><li></li><li></li><li></li></ul>{:/}  | {::nomarkdown}<ul><li></li><li></li><li></li><li></li><li></li><li></li></ul>{:/} | {::nomarkdown}<ul><li></li><li></li><li></li><li></li><li></li><li></li><li></li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}



### 

  





|  | Eventos personalizados da Shopify | Atribuições padrão do Braze |  |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li></li></ul>{:/}  | {::nomarkdown}<ul><li></li><li></li><li></li><li></li><li></li><li></li></li></ul>{:/} | {::nomarkdown}<ul><li>E-mail</li><li>Nome</li><li>Sobrenome</li><li>Telefone</li><li>Cidade</li><li>País</li></ul>{:/} | {::nomarkdown}<ul><li></li><li></li></ul>{:/} |
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
          <li>Como usar um código de desconto personalizado</li>
          <li>Como interagir com uma recomendação personalizada de produto</li>
          <li>Como adicionar uma mensagem de presente ao pedido</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Marcas ou produtos favoritos</li>
          <li>Categorias de compras de preferência</li>
          <li>Status de cadastro ou fidelidade</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

  

Por exemplo, o snippet JavaScript a seguir rastreia se o usuário atual está inscrito em uma newsletter e registra essa informação como um evento personalizado no perfil de usuário na Braze:

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

 

## Etapa 4: 

 



{% alert important %}
 <br><br>

-  Os endereços de e-mail são facilmente adivinháveis, o que os torna vulneráveis a ataques.
-  Se um usuário mal-intencionado alterar seu navegador da Internet para enviar o endereço de e-mail de outra pessoa como sua ID externa, ele poderá acessar mensagens confidenciais ou informações de conta.
{% endalert %}

 

  



{% alert note %}
  <br><br>
-  
-  
{% endalert %}

## Etapa 5: 

  



## Etapa 6: 





### 



#### 

  

#### 

 



## Etapa 7: Concluir configuração

1. Depois de fazer as configurações, selecione **Finish Setup** (Concluir configuração).
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