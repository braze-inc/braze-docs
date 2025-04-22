---
nav_title: Grupos internos
article_title: Grupo interno
page_order: 10
page_type: reference
description: ""

---

# Grupos internos

>   

{% alert tip %}

{% endalert %}

## 



## 

 

1. Acesse **Configurações** > **Grupos internos**.
2. 
3. 
4. 

|          | Descrição                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
|    | Usado para verificar eventos ou registros do seu dispositivo de teste.                                    |
|  | Pode ser usado em mensagens push, de e-mail e no app para enviar uma cópia renderizada da mensagem. |
|          | Envia automaticamente uma cópia do e-mail para todos os membros do grupo de teste após o envio.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



### Adição de usuários de teste

 

1. 
2. 

|                   | Descrição                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  |                                                                                                                                                            |
|   | Pesquise por endereço IP. Em seguida, forneça um nome para cada usuário teste adicionado. Esse é o nome ao qual todos os registros de eventos serão associados na página [Registro de usuários de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/). |
|       |  Só é possível adicionar usuários que já sejam conhecidos no dashboard.           |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



### Grupos de teste de conteúdo

Semelhante ao envio de um teste prévio de uma mensagem, o Grupo de teste de conteúdo economiza seu tempo e permite lançar testes para uma lista predefinida de usuários do Braze simultaneamente.  Somente os grupos marcados como Grupos de teste de conteúdo estarão disponíveis na seção de prévia de uma mensagem.

{% alert note %}
As mensagens de teste [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) só podem ser enviadas para números de telefone válidos no banco de dados.
{% endalert %}

 Se a sua mensagem incluir qualquer Liquid ou outra personalização dinâmica, o Braze usará as atribuições disponíveis para cada usuário para personalizar o conteúdo da mensagem. Para usuários que não têm atribuições, a Braze usará o valor padrão definido.

Além disso, se você visualizar a mensagem como um usuário aleatório, personalizado ou existente, poderá enviar essa versão prévia. Desmarcar a caixa de seleção permite enviar com base nas atribuições de cada usuário em relação à versão prévia.





### Grupos de teste

 

  

 

 

- 
-  
- 
- 

{% alert tip %}

{% endalert %}

#### Para campanhas



Os grupos de teste são enviados para cada variante de e-mail uma vez e são entregues na primeira vez que o usuário recebe essa variante específica. No caso de mensagens programadas, normalmente é a primeira vez que a campanha é lançada. Para campanhas baseadas em ações ou disparadas por API, esse será o momento em que o primeiro usuário receberá uma mensagem.

 

{% alert note %}

{% endalert %}



#### Para Canvas

Os grupos de teste no Canvas funcionam de forma semelhante à de qualquer campanha disparada. O Braze detecta automaticamente todas as etapas que contêm uma mensagem de e-mail e enviará para elas quando o usuário chegar a essa etapa específica de e-mail pela primeira vez.

Se uma etapa de e-mail tiver sido atualizada após o envio do grupo de teste, será apresentada a opção de enviar apenas para etapas atualizadas, todas as etapas ou desativar as sementes.

