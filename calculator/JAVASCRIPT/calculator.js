const lis = document.querySelectorAll("ul li");
/*dont forget the parentesis*/
lis.forEach((node)=>{
    node.addEventListener("mousedown", function(event){
        /*trim brings us more space between any node*/
        const value= node.innerText.trim();
        /*la parte de $result hace que en el cuadro de arriba
        se coloque el numero o simbolo, cuando lo ponemos
        commo innertext reemplaza al valor en el html*/
        const $result=document.querySelector(".result");
        /*$result.innerText=value;*/
        const resultText=$result.innerText.trim();
        /*si empieza en cero lo quita para que no ocupe espacio*/
        if(resultText=="0" || resultText.toLowerCase()=="undefined" || resultText.toLowerCase()=="infinity"){
            $result.innerText="";
        }
        if(value=="="){
            /*eval realiza los calculos e identifica que simbolo es*/
            let solution = eval(resultText);
            $result.innerText=solution;
            return true;
        }

        if(value.toLowerCase()=="c"){
            $result.innerText = "";
            return true;
        }
        /*append hace que se sigan colocalndo un numero tras
        el otro*/
        $result.append(value);
        console.log(value);
        })
})