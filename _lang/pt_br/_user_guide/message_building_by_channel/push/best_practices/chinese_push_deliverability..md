---
nav_title: Entregabilidade para dispositivos Android chineses
article_title: Entregabilidade de push para dispositivos Android chineses
page_order: 10

page_type: reference
description: "Este artigo aborda as nuances da entregabilidade push que você deve conhecer ao direcionar usuários em dispositivos Android fabricados por OEMs chineses."
channel: push

---

# Entregabilidade de push para dispositivos Android chineses

> Alguns dispositivos Android fabricados por fabricantes de equipamentos originais (OEMs) chineses, como Xiaomi, OPPO e Vivo, otimizam a duração da bateria por meio de um gerenciamento agressivo do ciclo de vida dos apps. Essa otimização pode ter a consequência não intencional de encerrar o processamento de aplicativos em segundo plano, o que pode reduzir a entregabilidade de suas notificações por push.<br><br>Para garantir que o desempenho do envio de mensagens do seu app funcione conforme o esperado nesses dispositivos, suas equipes de marketing e engenharia devem colaborar e seguir as etapas descritas neste artigo.

## Etapas para desenvolvedores
Esses OEMs realizam suas otimizações eliminando agressivamente os aplicativos em segundo plano e impedindo que eles iniciem automaticamente a execução de tarefas em segundo plano. Como desenvolvedor, você precisará configurar seu app para pedir ao usuário que alivie essas restrições sempre que possível.

Isso pode ser feito fazendo com que seu aplicativo seja iniciado automaticamente no dispositivo do usuário final, o que lhe dá permissão para ser executado em segundo plano e ouvir as mensagens no app Braze. Infelizmente, como esse é um problema específico do OEM e não do Android, não há APIs documentadas para exibir o prompt de permissão de inicialização automática para cada OEM.

Para resolver isso, integre uma biblioteca como a [AutoStarter](https://github.com/judemanutd/AutoStarter) em seu aplicativo. O AutoStarter é compatível com vários fabricantes, oferecendo uma maneira fácil de chamar o gerenciador de permissões de inicialização em uma grande variedade de dispositivos. Depois de integrar o AutoStarter, chame `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` para abrir o gerenciador de permissões de inicialização no dispositivo do usuário final. Associe essa ação a um prompt que incentive o usuário final a ativar a "inicialização automática" do seu app. Sua equipe de marketing criará essa mensagem - veja a próxima seção!

## Etapas para profissionais de marketing
Depois que os usuários aceitam receber notificações por push, há etapas adicionais que eles podem realizar para melhorar a entrega de mensagens para esses dispositivos. Recomendamos que a [mensagem push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) seja seguida por uma mensagem no app direcionada aos usuários de dispositivos OEM chineses com estas etapas adicionais:

- Ativar a "inicialização automática" do aplicativo
- Desativar a otimização da bateria para o aplicativo

Para ampliar ainda mais sua mensagem, adicione outros canais para trazer à tona informações de notificações por push não abertas por meio de canais fora do aplicativo, como SMS, WhatsApp e LINE, e canais no app, como mensagens no app e cartões de conteúdo. Seus usuários poderão ver qualquer coisa que possam ter perdido na próxima vez que abrirem o app.