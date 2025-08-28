---
nav_title: Distribuições com atributos personalizados
article_title: Distribuições com atributos personalizados com Voucherify
page_order: 3
alias: /partners/voucherify/custom_attributes/
description: "Este artigo de referência descreve a integração do Braze com o Voucherify. A integração com a Braze permite enviar códigos Voucherify nas suas mensagens da Braze."
page_type: partner
search_tag: Partner
---

# Distribuições com atributos personalizados

> A integração com a Braze permite enviar códigos Voucherify nas suas mensagens da Braze. Este artigo de referência aborda como usar os atributos personalizados do Braze com as distribuições do Voucherify.

_Essa integração é mantida pela Voucherify._

{% alert tip %}
Antes de usar os atributos personalizados do Braze nas distribuições do Voucherify, é necessário adicionar seus usuários do Braze ao dashboard do Voucherify. Você pode usar o conteúdo conectado da Braze para sincronizar usuários ou importar seus clientes por CSV ou API. Visite [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers) para saber mais.
{% endalert %}

Os atributos personalizados do Braze ativam a atribuição de códigos Voucherify a atributos personalizados em perfis de usuário no Braze. Você pode usar cupons exclusivos, cartões-presente, cartões de fidelidade e códigos de referência. Primeiro, conecte a Voucherify à Braze, crie uma distribuição na Voucherify e, por fim, crie uma campanha na Braze com o snippet de atributo personalizado no seu modelo de mensagem.

## Etapa 1: Conectando sua conta Voucherify ao Braze

Primeiro, conecte sua conta Voucherify ao Braze.

1. Copie a chave da API REST de sua conta do Braze.
2. Acesse o diretório **Integrações** em seu dashboard do Voucherify, encontre o Braze e selecione **Conectar.**  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_integrations.png %}){: style="margin-top:15px;margin-left:25px;margin-bottom:15px;"}
    
3. Cole a chave de API do Braze e selecione **Connect (Conectar**):  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_enter_API_key.png %}){: style="max-width:60%;margin-top:15px;margin-left:25px;margin-bottom:15px;"}


## Etapa 2: Distribuição de códigos

Quando conectado, é possível iniciar uma nova [distribuição](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work) do Voucherify que atribui um código ao atributo personalizado no perfil do usuário no Braze. Posteriormente, você poderá usar as atribuições recebidas com códigos em suas campanhas do Braze.

Antes de configurar a distribuição, é necessário adicionar seus usuários do Braze ao dashboard do Voucherify. Visite [Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers) para saber mais.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_distribution.png %})

Você pode distribuir códigos para o Braze usando dois modos:

- **Modo manual**
- Defina um **fluxo de trabalho automatizado** que dispara a entrega de código em resposta a uma ação tomada por seus usuários.

Nos modos manual e automático, o Voucherify envia códigos exclusivos com suas atribuições e os atribui aos atributos personalizados do Braze nos perfis dos usuários.

![Mapear campos para atributos personalizados]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_fields_mapping.png %})

{% tabs %}
{% tab Distribuição manual %}

O modo manual é uma ação única que atribui códigos a um público escolhido. Acesse as **Distribuições** em seu dashboard, execute o gerenciador de distribuição com o sinal de mais e escolha **Mensagem manual**.

1.  Dê um nome à sua distribuição.

    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}<br>  
    
    Escolha uma campanha que será uma fonte de códigos exclusivos **(1)** e selecione um segmento de usuários ou um único cliente como seus receptores **(2)**. Visite [Voucherify](https://support.voucherify.io/article/51-customer-segments) para saber mais sobre segmentos de clientes.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution_choose_segment.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  

2.  Em seguida, adicione as permissões de marketing. Se você não coleta permissões do seu público, desative a verificação de consentimento.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_consents.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
3.  Escolha o Braze como um canal e mapeie os campos personalizados que serão adicionados ao perfil do usuário no Braze. Você precisa adicionar o campo que representa o código do voucher publicado; os demais campos são opcionais.  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_channel.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
4.  Quando concluído, você poderá ver um resumo da distribuição. Clique em **Salvar e enviar** para entregar os códigos aos perfis de usuário no Braze.  

_Note que todas as distribuições manuais são enviadas com uma postergação de 10 minutos._

{% endtab %}
{% tab Fluxo de trabalho automático %}

A Voucherify pode enviar códigos para a Braze automaticamente em resposta aos seguintes disparos:

- **O cliente entrou/saiu de um segmento específico do Voucherify**
- **Publicação de código bem-sucedida** \- a mensagem é enviada quando o código de uma campanha é publicado (atribuído) a um cliente no Voucherify.
- **Status do pedido alterado** (pedido criado, pedido atualizado, pedido pago, pedido cancelado)
- **Créditos de presente adicionados** \- a mensagem é enviada quando créditos de cartão-presente são adicionados ao cartão do cliente.
- **Pontos de fidelidade adicionados** \- a mensagem é enviada quando pontos de fidelidade são adicionados ao perfil do cliente.
- **Voucher resgatado** \- a mensagem é enviada aos clientes que resgataram vouchers com sucesso.
- **Reversão do resgate do voucher** – a mensagem é enviada ao cliente cujo resgate foi revertido com sucesso.
- **Resgate de recompensas** \- a mensagem é enviada quando um cliente resgata uma recompensa de fidelidade ou de indicação.
- **O evento personalizado foi registrado para um cliente** \- a mensagem é disparada quando o Voucherify registra um evento personalizado específico.

Para configurar um fluxo de trabalho automático com a Braze e a Voucherify, [confira o tutorial de distribuições](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work).

{% endtab %}
{% endtabs %}

## Etapa 3: Use os atributos personalizados do Voucherify em sua campanha no Braze

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_code.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Depois que o atributo personalizado com o código for adicionado aos atributos personalizados do cliente no Braze, você poderá usá-lo em suas campanhas.

Edite o corpo da mensagem e adicione o atributo personalizado definido na distribuição do Voucherify. Coloque {% raw %}`{{custom_attribute.${custom_attribute_with_code}}}`{% endraw %} para exibir o código exclusivo.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_body.png %}){: style="max-width:75%;"}

Quando estiver com tudo pronto, você poderá ver o código na prévia da mensagem.

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_preview.png %})

