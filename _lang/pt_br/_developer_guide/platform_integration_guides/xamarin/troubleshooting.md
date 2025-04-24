---
nav_title: Solução de problemas
article_title: Solução de problemas para Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 6
description: "Este artigo aborda a solução de problemas do iOS e do Android para a plataforma Xamarin."

---

# Solução de problemas

> Este artigo fornece vários cenários de solução de problemas do Xamarin.

## Android

### O push não aparece depois que o app é fechado no alternador de tarefas

Se observar que as notificações por push não aparecem mais depois que o aplicativo é fechado no alternador de tarefas, é provável que seu app esteja no modo de depuração. O Xamarin adiciona estruturações no modo de depuração que impedem que os apps recebam push depois que seu processo é encerrado. Se você executar seu app no modo de lançamento, deverá ver o push mesmo depois que o app for fechado no alternador de tarefas.

### A fábrica de notificações personalizadas não está sendo definida corretamente

Os fatos de notificação personalizados (e todos os delegates) devem estender [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) para funcionar corretamente na divisão entre C# e Java. Para saber mais, consulte [Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces) sobre a implementação de interfaces Java.

