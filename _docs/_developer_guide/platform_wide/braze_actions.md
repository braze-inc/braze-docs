---
nav_title: Braze Actions Deeplinks
article_title: Braze Actions Deeplink
page_order: 100
description: "Use the `brazeActions://` deeplinks to perform SDK actions within messaging channel buttons"
hidden: true
---


<div>Output:</div>
<textarea id="braze-actions-output"></textarea>
<div>Input:</div>
<textarea id="braze-actions-input"></textarea>
<style>
    #braze-actions-input, #braze-actions-output {
        width: 90%;
        border: solid 1px #1f1f1f !important;
        margin-top: 10px;
        border-radius: 4px;
        font-family: courier;
        font-size: 14px;
        padding: 4px;
    }
</style>
<script>
(function(){
    const input = document.getElementById('braze-actions-input');
    const output = document.getElementById('braze-actions-output');
    var debouncer;
    input.oninput = function(event){
        clearTimeout(debouncer);
        setTimeout(function(){
            try {
                const jsonString = toBinary(JSON.stringify(event.target.innerText));
                output.value = `brazeActions://v1/${toBinary(jsonString)}`
            } catch(e){
                output.value = `Invalid JSON`;
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
