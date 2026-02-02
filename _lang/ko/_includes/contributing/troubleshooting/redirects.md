전역 리디렉션 파일(`assets/js/broken_redirect_list.js`)에 설정한 [리디렉션]({{site.baseurl}}/contributing/content_management/redirecting_urls/)이 작동하지 않는 경우, 대문자 문자가 있는지 URL 문자열을 다시 확인하세요. 발견되면, `_docs` 디렉토리의 해당 파일 이름에 대문자가 포함되어 있더라도 소문자로 변환하세요.

{% tabs local %}
{% tab before %}
```javascript
validurls['/docs/hidden/WIP_Partnerships/WIP_Guidelines'] = '/docs/contributing/home/';
```
{% endtab %}

{% tab after %}
```javascript
validurls['/docs/hidden/wip_partnerships/wip_guidelines'] = '/docs/contributing/home/';
```
{% endtab %}
{% endtabs %}
