---
nav_title: Usuários de envio de mensagens
article_title: Usuários de envio de mensagens
description: "Este artigo de referência aborda como o Braze tratará as mensagens dos usuários."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /whatsapp_quick_replies/

---

# Envio de mensagens do usuário

> O WhatsApp é um canal de comunicação bidirecional. Sua marca não só pode enviar mensagens aos usuários, mas eles também podem se engajar em conversas usando campanhas de modelos e Canvas.  

## Gatilhos baseados em ações 

 

Certifique-se de que a palavra disparadora corresponda ao que você espera dos usuários.

**O que você deve saber:**
- Cada letra de sua palavra disparadora deve estar em letra maiúscula quando configurada. A Braze não exige que as palavras disparadas enviadas pelos usuários sejam em letras maiúsculas. Por exemplo, o envio de mensagens "jOin2023" ainda disparará o Canva ou a campanha.
- Se nenhuma palavra do acionador for especificada no acionador baseado em ação da agenda de entrada, a campanha ou o Canva será executado para TODAS as mensagens recebidas do WhatsApp. Isso inclui mensagens que tenham frases correspondentes em campanhas ativas e Canvas, caso em que o usuário receberá duas mensagens do WhatsApp.

{% tabs %}
{% tab Campanha %}



{% endtab %}
{% tab Canvas %}



{% endtab %}


## Respostas não reconhecidas

Recomendamos que você inclua uma opção para respostas não reconhecidas nas telas interativas. Isso orienta os usuários a entender quais são os prompts disponíveis e define as expectativas para o canal. O gerenciamento de expectativas pode ser especialmente útil se você tiver canais do WhatsApp com bate-papo de agente ao vivo. 
- Na etapa de ação, depois de criar os grupos de ação para as frases de filtro personalizadas, adicione um grupo de ação adicional para "Enviar mensagem do WhatsApp", mas **não verifique Onde o corpo da mensagem**. Isso capturará todas as respostas não reconhecidas do usuário, semelhante a uma cláusula "else". 
- Recomendamos o envio de uma mensagem pelo WhatsApp informando ao usuário que esse canal não tem pessoal e orientando-o para um canal de suporte, se necessário. 

## Respostas rápidas 



As respostas rápidas aparecem como opções de botões clicáveis na conversa, mas agem como se o usuário tivesse respondido com texto. Em seguida, o Braze processa essas mensagens como mensagens de entrada e pode enviar respostas definidas com base no botão clicado. Use a etapa "Ação de mensagem de entrada do WhatsApp" ao criar e filtrar respostas de seus usuários.



### 

#### Etapa 1: Crie CTAs

Primeiro, crie suas CTAs de resposta rápida no [Gerenciador de modelos de mensagens do WhatsApp](https://business.facebook.com/wa/manage/message-templates/) em um modelo de mensagem. 



Depois que seu modelo for enviado e aprovado pelo WhatsApp, você poderá usá-lo para criar um canva na Braze. 

{% alert tip %}
Você pode criar o Canva antes de receber a aprovação em seu modelo de mensagem.
{% endalert %}

#### Etapa 2: Crie seu canva

Em seguida, crie um canva com uma etapa de mensagens que inclua o modelo criado. 



Crie uma etapa de ação que siga a etapa da mensagem. Crie um grupo por opção de resposta rápida nessa etapa da ação.



Para cada grupo de opções de resposta rápida, especifique o texto exato como o botão que está correspondendo. Note que as palavras-chave devem estar em letras maiúsculas. 



Se quiser uma resposta padrão para os usuários que responderem à mensagem com texto em vez de respostas rápidas, crie um grupo adicional sem corpo de mensagem correspondente.

Continue construindo o canva como faria de outra forma deste ponto em diante.

### Respostas

Provavelmente, você desejará uma mensagem de resposta para cada resposta. Recomendamos ter uma opção abrangente para respostas fora dos limites das respostas rápidas (por exemplo, para clientes que respondem com uma mensagem geral em vez de uma solicitação predeterminada). Por exemplo, "Desculpe-nos, mas não reconhecemos sua resposta. Para questões de suporte, envie uma mensagem para <support channel>."



Note que você pode usar quaisquer ações subsequentes que o Braze Canvas oferece, como mensagens em resposta, atualizações de perfil de usuário ou webhooks Braze-to-Braze. 

## 

 



### 

#### Etapa 1: 



#### Etapa 2: 





 

-   
-  
-  







 

1. 
2. 
3. 





### 

 



## 

  

 

-  
  - 



- 
-  
  - 



