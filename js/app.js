console.log("Script carregado!");  // Testar se o arquivo está sendo carregado corretamente

let lista = [];

function criaLista() {
    // Verifique se os elementos já existem no DOM
    let verifica_caixa_entrada = document.getElementById('input_cria_lista_inteiros');
    let verifica_btn_add_numero = document.getElementById('btn_add_numero');
    let verifica_p_lista = document.getElementById('lista_numeros');

    let texto_orientacao = document.getElementById('texto_orientacao');
    texto_orientacao.remove();


    if (verifica_caixa_entrada == null && verifica_btn_add_numero == null) {
        let caixa_entrada = document.createElement('input');
        caixa_entrada.type = 'text';
        caixa_entrada.id = 'input_cria_lista_inteiros';

        let btn_add_numero = document.createElement('button');
        btn_add_numero.type = 'button';
        btn_add_numero.id = 'btn_add_numero';
        btn_add_numero.textContent = 'Adicionar numero';

        // Verifica se o parágrafo já existe, senão cria
        if (!verifica_p_lista) {
            let p_lista = document.createElement('p');
            p_lista.id = 'lista_numeros';
            p_lista.textContent = 'Lista: ' + lista.join(', ');  // Inicializa o parágrafo com a lista vazia
            let container = document.getElementById('container_exercicios');
            container.appendChild(p_lista);  // Adiciona o parágrafo no container
        }

        let container = document.getElementById('container_exercicios');
        container.appendChild(caixa_entrada);
        container.appendChild(btn_add_numero);

        btn_add_numero.onclick = function() { // para esse ecercicio em especifico achei melhor usar o onclick no lugar do eventlistener
            let numero = parseInt(caixa_entrada.value.trim());
        
            if (isNaN(numero)) {
                alert('O texto não é um número');
            } else if (!lista.includes(numero)) {
                lista.unshift(numero);
                caixa_entrada.value = '';  // Limpar a caixa de entrada
                console.log(lista);
        
                // Atualizar o parágrafo com a lista atualizada
                let p_lista = document.getElementById('lista_numeros');
                p_lista.textContent = 'Lista: ' + lista.join(', ');  // Atualiza o conteúdo do parágrafo
            } 
            //else {
              //  alert(`Lista já contém o número ${numero}`);
                //caixa_entrada.value = '';  // Limpar a caixa de entrada
            //}
        };
    }
}

function maior_da_lista(){
    //Descobrindo maior numero
    let maior = 0;
    for (let i=0; i < lista.length;i++){
        if (lista[i]> maior){
            maior = lista[i];
        }
    }

    //Colocando o maior no dom.
    let caixa_resultado = document.getElementById('caixa_resultado');
    
    if (lista.length === 0){
        alert('A lista esta vazia');
    }
    else if (caixa_resultado == null){
        let caixa_resultado = document.createElement('p');
        caixa_resultado.id = 'caixa_resultado';
        caixa_resultado.textContent = `O maior numero é ${maior}`
        let container = document.getElementById('container_exercicios');
        container.appendChild(caixa_resultado);
    }
    else{
        caixa_resultado.textContent = `O maior numero é ${maior}`
        let container = document.getElementById('container_exercicios');
        container.appendChild(caixa_resultado);
    }
}

function menor_da_lista() {
    if (lista.length === 0) {
        alert('A lista está vazia');
    }

    let menor = lista[0];
    for (let i = 0; i < lista.length; i++) {
        if (lista[i] < menor) {
            menor = lista[i];
        }
    }
    
    let caixa_resultado = document.getElementById('caixa_resultado');
    if (caixa_resultado == null) {
        caixa_resultado = document.createElement('p');
        caixa_resultado.id = 'caixa_resultado';
        caixa_resultado.textContent = `O menor número é ${menor}`;

        let container = document.getElementById('container_exercicios');
        container.appendChild(caixa_resultado);
    } else {
        let container = document.getElementById('container_exercicios');
        caixa_resultado.textContent = `O menor número é ${menor}`;
        container.appendChild(caixa_resultado);
    }
}


function soma_todos_elementos(){
    let soma = 0;

    if (lista.length === 0){
        alert('A lista esta vazia');
    }
    else{        
        for (let i=0 ; i < lista.length; i++){
            soma += lista[i];
        }
    }
    let caixa_resultado = document.getElementById('caixa_resultado');
    
    if((caixa_resultado == null)&&(lista.length > 0)){
        caixa_resultado = document.createElement('p');
        caixa_resultado.id = 'caixa_resultado';
        caixa_resultado.textContent = `A soma dos numeros: ${soma}`;
        let container = document.getElementById('container_exercicios');
        container.appendChild(caixa_resultado);
    }
    else{
        let container = document.getElementById('container_exercicios');
        caixa_resultado.textContent=`A soma dos numeros: ${soma}`;
        container.appendChild(caixa_resultado);
    }
}

function media(){
    let soma = 0;
    let media = 0;

    if (lista.length === 0){
        alert('A lista esta vazia');
        return;
    }
    else{        
        for (let i=0 ; i < lista.length; i++){
            soma += lista[i];
        }
    }

    media = soma/(lista.length)

    caixa_resultado = document.getElementById('caixa_resultado');
    if((caixa_resultado == null)&&(lista.length > 0)){
        caixa_resultado = document.createElement('p');
        caixa_resultado.id = 'caixa_resultado';
        caixa_resultado.textContent = `A média é: ${media}`;
        let container = document.getElementById('container_exercicios');
        container.appendChild(caixa_resultado);
    }
    else{
        let container = document.getElementById('container_exercicios');
        caixa_resultado.textContent = `A média é: ${media}`;
        container.appendChild(caixa_resultado);
    }
}

function contem() {
    if (lista.length === 0) {
        alert('A lista está vazia');
        return; // Se a lista estiver vazia, não prossegue com o código
    }

}
