---
nav_title: Braze Actions Deeplinks
article_title: Braze Actions Deeplink
page_order: 100
description: "Use the `brazeActions://` deeplinks to perform SDK actions within messaging channel buttons"
hidden: true
---


<pre id="braze-actions-output"></pre>
<pre id="braze-actions-input"></pre>
<script>
(function(){
    const input = document.getElementById('braze-actions-input');
    const output = document.getElementById('braze-actions-output');
    var debouncer;
    input.onchange = function(event){
        clearTimeout(debouncer);
        setTimeout(function(){
            try {
            const jsonString = toBinary(JSON.stringify(event.target.innerText));
            output.innerText = `brazeActions://v1/${toBinary(jsonString)}`
            } catch(e){
                output.innerText = `Invalid JSON`;
            }
        }, 100);
    }

    function toBinary(string) {
        const codeUnits = new Uint16Array(string.length);
        for (let i = 0; i < codeUnits.length; i++) {
            codeUnits[i] = string.charCodeAt(i);
        }
        return btoa(String.fromCharCode(...new Uint8Array(codeUnits.buffer)));
    }
})();
</script>
