---
nav_title: PERGUNTAS FREQUENTES
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

Não, o mesmo nível de percepção será fornecido ao enviar uma mensagem MMS.

### Posso controlar a ordem em que a imagem e o corpo da mensagem de um MMS são entregues?

O Braze não tem controle sobre a ordem de exibição quando o corpo da mensagem e as imagens são incluídos em uma mensagem MMS. Isso depende de vários fatores, incluindo, mas não se limitando a:

- A operadora que está recebendo a mensagem
- O dispositivo que está recebendo a mensagem
- O tamanho total da mensagem

### Os preços de MMS e SMS são diferentes?

MMS e SMS têm custos diferentes e são cobrados separadamente com base no volume. Entre em contato com a equipe do Braze Onboarding para obter informações sobre preços.

### O MMS exige um processo de integração separado?

Não! O MMS agora está incluído em nosso processo de integração de SMS. Os clientes existentes que já passaram pelo processo de integração podem começar a enviar campanhas MMS depois de concluir as etapas a seguir:

1. Comprar MMS.
2. Entre em contato com a equipe de integração do Braze para solicitar que o recurso MMS seja ativado. Isso ativará o MMS e um grupo de assinatura de SMS/MMS será criado ou atualizado para você.

Em seguida, a equipe de integração do Braze garantirá que seus códigos curtos e longos estejam habilitados (nos EUA e no Canadá) para MMS. Eles também atualizarão seus grupos de assinatura para mostrar os números atuais que foram adicionados ou ativados para MMS. Depois que essas etapas forem concluídas, você poderá enviar mensagens MMS imediatamente a partir do nosso compositor de SMS nativo.

### Por que não consigo encontrar o MMS em meu painel, mesmo que o recurso esteja ativado?

O MMS só é exibido no painel de controle do Braze quando um grupo de assinaturas é considerado "habilitado para MMS". Isso é refletido por uma tag MMS ao selecionar o grupo de assinatura no compositor de uma mensagem SMS/MMS. Isso significa que pelo menos um número no grupo de assinaturas é capaz de enviar uma mensagem MMS.

Além disso, determinadas situações exigirão que a Twilio aprove novamente a ativação de códigos curtos que originalmente não tinham o MMS ativado. Esse processo de aprovação pode levar semanas.
