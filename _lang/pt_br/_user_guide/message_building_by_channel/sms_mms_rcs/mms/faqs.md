---
nav_title: Perguntas frequentes
article_title: PERGUNTAS FREQUENTES SOBRE MMS
page_order: 4
description: "Este artigo aborda algumas das perguntas mais frequentes sobre MMS."
page_type: FAQ
alias: /mms_faq/
channel:
  - MMS
  
---

# Perguntas frequentes

> Nesta página, tentaremos responder às suas perguntas mais rigorosas sobre MMS.

### Há alguma alteração nos dados do Currents ao enviar um MMS?

Não, o mesmo nível de insight será fornecido ao enviar uma mensagem MMS.

### Posso controlar a ordem em que a imagem e o corpo da mensagem de um MMS são entregues?

O Braze não tem controle sobre a ordem de exibição quando o corpo da mensagem e as imagens são incluídos em uma mensagem MMS. Isso depende de vários fatores, incluindo, entre outros:

- A operadora que está recebendo a mensagem
- O dispositivo que está recebendo a mensagem
- O tamanho total da mensagem

### O preço do MMS e do SMS é diferente?

MMS e SMS têm custos diferentes e são cobrados separadamente com base no volume. Entre em contato com a equipe de integração da Braze para obter informações sobre preços.

### O MMS requer um processo de integração separado?

Não! O MMS agora está incluído em nosso processo de integração de SMS. Os clientes existentes que já passaram pela integração podem começar a enviar campanhas MMS depois de concluir as etapas a seguir:

1. Comprar MMS.
2. Entre em contato com a equipe de integração da Braze para solicitar que o recurso MMS seja ativado. Isso ativará o MMS e um grupo de inscrições de SMS/MMS será criado ou atualizado para você.

Em seguida, a equipe de integração da Braze garantirá que seus códigos curtos e longos estejam ativados (nos EUA e no Canadá) para MMS. Eles também atualizarão seus grupos de inscrições para mostrar os números atuais que foram adicionados ou ativados para MMS. Depois que essas etapas forem concluídas, você poderá enviar mensagens MMS imediatamente a partir do nosso criador de mensagens SMS nativo.

### Por que não consigo encontrar o MMS em meu dashboard, embora o recurso esteja ativado?

O MMS só é exibido no dashboard da Braze quando um grupo de inscrições é considerado "MMS ativado". Isso é refletido por uma tag MMS ao selecionar o grupo de inscrições no criador de uma mensagem SMS/MMS. Isso significa que pelo menos um número no grupo de inscrições é capaz de enviar uma mensagem MMS.

Além disso, em determinadas situações, o Twilio precisará aprovar novamente a capacitação de códigos curtos que originalmente não tinham o MMS ativado. Esse processo de aprovação pode levar semanas.
