---
nav_title: ActionIQ
article_title: ActionIQ
description: "Este artigo de referência aborda a integração entre a Braze e a ActionIQ.  Esta integração permite que as marcas sincronizem e mapeiem seus dados ActionIQ diretamente para a Braze."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

>  



## Sobre a integração

 

- 
- Encaminhe os eventos rastreados pelo ActionIQ para a Braze em tempo real para disparar campanhas personalizadas e direcionadas
- 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta ActionIQ | Uma conta ActionIQ é necessária para aproveitar esta integração. |
| chave da API REST Braze |   <br><br> |
| Endpoint REST do Braze | [Seu URL do ponto de extremidade REST][1]. Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrações

### Participação do público

Esta integração é usada para sincronizar a associação de público do ActionIQ com o Braze, criando atributos personalizados que indicam se um perfil do Braze faz parte de um segmento. Cada público do ActionIQ corresponde a um atributo personalizado booleano único.

A convenção de nomenclatura padrão para o atributo personalizado criado é: `AIQ_<Audience ID>_<Split ID>`.


1. 
2. 
3. 
4.  
5. Depois que o segmento é criado, você pode selecioná-lo como um filtro de público ao criar uma campanha ou canva.



#### Solicitações

 Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. 

No ActionIQ, configure uma conexão da Braze fornecendo sua chave da API REST e o endpoint REST da Braze. 

Para corresponder aos consumidores na plataforma Braze, os seguintes identificadores devem ser incluídos na sua configuração de ativação:
- `braze_id`
- `external_id`

### Eventos

  

#### Solicitações

 Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. 

A integração de eventos envia as seguintes informações para a Braze:
- Nome do evento
- Identificador do consumidor (ou `braze_id` ou `external_id`)
- Data e hora
- Propriedades do evento, que são preenchidas por quaisquer atributos adicionais na configuração de exportação

### Campanhas disparadas

 

 

#### Solicitações

 Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**.


- Identificador do consumidor (ou `braze_id` ou `external_id`)
- ID da campanha


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/