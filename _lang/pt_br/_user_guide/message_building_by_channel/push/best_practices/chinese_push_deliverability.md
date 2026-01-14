---
nav_title: Entregabilidade para dispositivos Android chineses
article_title: Entregabilidade de push para dispositivos Android chineses
page_order: 10

page_type: reference
description: "Este artigo cobre as nuances da entregabilidade de push que você deve estar ciente ao direcionar usuários em dispositivos Android fabricados por OEMs chineses."
channel: push

---

# Entregabilidade de push para dispositivos Android chineses

> Alguns dispositivos Android fabricados por Fabricantes de Equipamentos Originais da China (OEMs), como Xiaomi, OPPO e Vivo, otimizam para uma vida útil da bateria mais longa através de uma gestão agressiva do ciclo de vida do aplicativo. Essa otimização pode ter a consequência não intencional de desligar o processamento de aplicativos em segundo plano, o que pode reduzir a entregabilidade das suas notificações push.<br><br>Para garantir que o desempenho de mensagens do seu aplicativo funcione como esperado nesses dispositivos, suas equipes de marketing e engenharia devem colaborar e seguir os passos descritos neste artigo.

## Passos para desenvolvedores
Esses OEMs realizam suas otimizações através do fechamento agressivo de aplicativos em segundo plano e bloqueando-os de iniciar automaticamente para executar tarefas em segundo plano. Como desenvolvedor, você precisará configurar seu aplicativo para pedir ao usuário que alivie essas restrições sempre que possível.

Isso pode ser alcançado fazendo com que seu aplicativo inicie automaticamente no dispositivo do usuário final, o que dá ao seu aplicativo permissão para rodar em segundo plano e ouvir mensagens do Braze. Infelizmente, como este é um problema específico de OEM e não um problema do Android, não existem APIs documentadas para trazer o prompt de permissão de auto-início para cada OEM.

Para resolver isso, integre uma biblioteca como [AutoStarter](https://github.com/judemanutd/AutoStarter) em sua aplicação. AutoStarter suporta múltiplos fabricantes, oferecendo uma maneira fácil de chamar o gerenciador de permissões de inicialização em uma ampla gama de dispositivos. Depois de integrar o AutoStarter, chame `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` para abrir o gerenciador de permissões de inicialização no dispositivo do usuário final. Combine essa ação com um prompt incentivando o usuário final a habilitar "auto-início" para seu aplicativo. Sua equipe de marketing elaborará essa mensagem—veja a próxima seção!

## Passos para profissionais de marketing
Depois que seus usuários optarem por receber notificações push, existem etapas adicionais que eles podem seguir para melhorar a entrega de mensagens para esses dispositivos. Recomendamos que você siga sua [mensagem introdutória de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) com uma mensagem no aplicativo direcionada a usuários em dispositivos OEM chineses com essas etapas adicionais:

- Ative "início automático" para o aplicativo
- Desative a otimização da bateria para o aplicativo

Para amplificar ainda mais sua mensagem, adicione outros canais para ressurgir informações de notificações push não abertas através de canais fora do aplicativo, como SMS, WhatsApp e LINE, e canais dentro do aplicativo, como mensagens no aplicativo e Cartões de Conteúdo. Seus usuários poderão ver qualquer coisa que possam ter perdido na próxima vez que abrirem o aplicativo.