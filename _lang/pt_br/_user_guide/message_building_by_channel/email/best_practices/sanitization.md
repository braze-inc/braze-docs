---
nav_title: Sanitização
article_title: Sanitização
page_order: 4
description: "Este artigo define a sanitização e sua finalidade para o envio de mensagens de e-mail no Braze."
channel:
  - email

---

# Sobre a higienização

> A sanitização é um processo que ocorre quando o Braze detecta um tipo específico de JavaScript em sua mensagem de e-mail.

## Por que realizamos a higienização?

O principal objetivo da sanitização é impedir que agentes mal-intencionados acessem os dados de sessão de outros usuários do dashboard do Braze. Sem sanitização, um agente mal-intencionado com acesso básico somente para leitura pode criar um e-mail usando o CKEditor com JavaScript que "envia a sessão atual do navegador" para qualquer lugar que o agente mal-intencionado desejar usando uma solicitação de rede.

Quando outro usuário do dashboard abrir esse modelo de e-mail, o JavaScript será executado e enviará os dados da sessão do usuário atual para o malfeitor.

Como nota, a maioria dos provedores de caixa de entrada de e-mail não processa JavaScript, portanto, essa medida também se destina a remover o inchaço desnecessário dos e-mails, reduzindo seu tamanho. 

## Como o Braze higieniza as mensagens?

Se o Braze detectar um JavaScript que represente um risco à segurança, antes de acessar a guia **Pré-visualização e teste** ou o editor de HTML para visualizar a mensagem de e-mail, solicitaremos que você confirme se o Braze pode remover o JavaScript da mensagem antes de prosseguir.

![]({% image_buster /assets/img/email_sanitization.png %})

## Quando as higienizações são mantidas?

Tanto no editor de arrastar e soltar quanto no editor de HTML, higienizamos, mas não mantemos os resultados higienizados nos seguintes cenários:

* O e-mail é processado nas seguintes áreas:
    * Seção **Inbox Vision** e guia **Spam Testing** 
    * Seção **Preview & Heatmap (Prévia e mapa de calor** ) no painel **Email Performance (Desempenho de e-mail)** 
* O e-mail é enviado em um envio de teste

Para o editor de arrastar e soltar, sanitizamos e também persistimos a sanitização na mensagem quando o
O editor é fechado e a campanha é salva. Para o editor de HTML, higienizamos e também mantemos a higienização na mensagem quando um usuário alterna entre os tipos de editor e a campanha é salva.

Em todos esses casos, uma mensagem é exibida se a sanitização modificou o HTML. O usuário deve aceitar isso antes que a sanitização seja concluída.