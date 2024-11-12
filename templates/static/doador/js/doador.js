
const cep = document.querySelector('#cep');
const endereco = document.querySelector('#endereco');
const bairro = document.querySelector('#bairro');
const cidade = document.querySelector('#cidade');
const estado = document.querySelector('#estado');
const message = document.querySelector('#message');
const botao = document.querySelector('#submit');



cep.addEventListener("focusout", async()=>{
    
    try {
        const onlynumbers = /^[0-9]+$/;
        const cepvalido =  /^[0-9]{8}$/;

        if(!onlynumbers.test(cep.value) || !cepvalido.test(cep.value)){
            throw{cep_erro:'Cep inválido'};
        }

        const response = await fetch('https://viacep.com.br/ws/${cep.value}/json');

        if(!response.ok){
            throw await response.json();
        }

        const responseCep = await response.json();
        endereco.value = 'aqui caraio';
        bairro.value = responseCep.bairro;
        cidade.value=responseCep.localidade;
        estado.value= responseCep.estado;

    } catch (error) {
        if (error?.cep_erro){
            message.textContent=error.cep_erro
            setTimeout(()=>{
                message.textContent=""
            },5000);
        }
        console.log(error);
    }
});



function materialselecionado(){
    matselecionado = document.getElementById('matselecionado')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    matvalue = matselecionado.value

    data = new FormData()
    data.append('id_matvalue',matvalue)

    fetch("doador/pesquisamaterial/", {
        method: {
            'X-CSRFToken':csrf_token,
        },
        body: data
    }).then(function(result){
        return result.json()
    
    }).then(function(data){

        console.log('teste')
    })


}


