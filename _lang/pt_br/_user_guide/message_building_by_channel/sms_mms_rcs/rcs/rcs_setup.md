---
nav_title: "Configuração do RCS"
article_title: Configuração do RCS
page_order: 1
alias: /rcs_setup/
description: "Este artigo de referência cobre os requisitos necessários para configurar o RCS."
page_type: reference
channel:
  - RCS
---

# Configurando o RCS

> Este artigo cobre os requisitos necessários para colocar seu canal RCS em funcionamento.

Configurar o RCS é tão simples quanto configurar o SMS. Continue lendo para aprender como você pode começar a enviar mensagens ricas e interativas.

## Etapa 1: Atenda aos critérios de elegibilidade

Para ser elegível para enviar RCS com a Braze, sua empresa deve atender a três critérios previamente:

1. Seu contrato atual com a Braze deve incluir Créditos de Mensagem. 
2. Você deve enviar suas mensagens RCS para um dos seguintes países suportados pela Braze:
- Estados Unidos
- Reino Unido
- Alemanha
- México
- Suécia
- Espanha
- Singapura
- Brasil
- França
- Itália
- Colômbia
3. Você deve adquirir um SKU(s) RCS de $0 em seu contrato.

## Etapa 2: Registre um remetente verificado de RCS

Antes de enviar mensagens RCS, você deve registrar um remetente verificado de RCS. Esta é a representação da sua marca que os usuários verão em seus dispositivos móveis, que inclui o nome da sua marca, logotipo, um selo de verificação e um slogan opcional. O remetente verificado de RCS reforça a confiança do cliente e confirma que suas mensagens vêm de uma fonte autenticada. 

![Um exemplo de remetente verificado de RCS em uma mensagem RCS chamada "Cat Failz Cafe".]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

Depois de adicionar os SKU(s) de RCS ao seu formulário de pedido, a Braze será notificada e entrará em contato com você com informações sobre o registro do remetente de RCS. O formato destes dependerá dos países para os quais você deseja enviar mensagens RCS. 

Quando você tiver enviado seus formulários completos para a Braze, nós completaremos o processo de registro em seu nome. 

### Etapa 2.1: Configure alternativas de SMS para grupos de inscrição RCS

Como a cobertura atual das operadoras varia de país para país, e o suporte de hardware e software dos usuários varia de indivíduo para indivíduo, o fallback de SMS é um componente chave para ter um programa RCS bem-sucedido hoje. Recomendamos configurar o fallback de SMS. Se uma operadora não suportar RCS ou o dispositivo de um usuário não conseguir receber mensagens RCS, o fallback de SMS enviará sua mensagem de qualquer forma, para que você nunca perca um momento importante com seus usuários.

Recomendamos fortemente revisar sua experiência atual de aceitação de SMS, grupos de inscrição e segmentação de público antes de implantar sua primeira campanha RCS. Se necessário, seu gerente de sucesso do cliente está sempre disponível para fornecer orientação e ajudá-lo a navegar pelo processo de configuração.

### Cronograma para aprovação da operadora

O cronograma para aprovação da operadora varia de país para país e também pode variar dentro de um país. Tenha em mente que o mercado de RCS ainda está em sua infância, portanto, os processos de operadoras e agregadores estão evoluindo rapidamente. Nos Estados Unidos, a Braze estima que o tempo de resposta para aprovação da operadora para um remetente verificado por RCS geralmente fica na faixa de 4 a 6 semanas, com um remetente de teste geralmente aprovado em uma semana.

Quando seu remetente verificado por RCS for aprovado, nossa equipe de operações atualizará seus grupos de inscrição conforme necessário para confirmar que eles têm o remetente RCS incluído. 

## Etapa 3: Configurar grupos de inscrição

O RCS é tipicamente usado de duas maneiras: 
- Para fazer upgrade do tráfego de SMS existente 
- Para ativar novos casos de uso que só são possíveis com a funcionalidade mais rica fornecida pelo RCS

Dependendo da sua integração, a Braze pode adicionar remetentes verificados por RCS aos seus grupos de inscrição de SMS existentes ou configurar novos grupos de inscrição para você. Em qualquer um dos casos, sua equipe da Braze o guiará por um upgrade de tráfego de SMS sem interrupções e em conformidade. Para saber mais, consulte [grupos de inscrição de SMS e RCS]({{site.baseurl}}/sms_rcs_subscription_groups/).

Para novos casos de uso que não são possíveis com SMS, considere configurar grupos de inscrição RCS dedicados para alinhar com os objetivos do seu programa.