## 문제 해결

### 작업 전환기에서 앱을 닫은 후 푸시가 나타나지 않음

작업 전환기에서 앱을 닫은 후 푸시 알림이 더 이상 표시되지 않는다면 앱이 디버그 모드일 가능성이 높습니다. Xamarin은 디버그 모드에서 프로세스가 종료된 후 푸시를 수신하지 못하도록 하는 스캐폴딩을 추가합니다. 릴리스 모드에서 앱을 실행하는 경우 작업 전환기에서 앱을 닫은 후에도 푸시가 표시되어야 합니다.

### 사용자 지정 알림 팩토리가 올바르게 설정되지 않음

커스텀 알림 팩토리(및 모든 위임)는 C#과 Java 부분에서 제대로 작동하려면 [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/)를 확장해야 합니다. 자세한 내용은 Java 인터페이스 구현의 [Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces)을 참조하세요.
