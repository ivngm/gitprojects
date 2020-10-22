const openBtn=document.querySelector(".js-open");
        const modalBg = document.getElementById("modal-bg");
        const modalBx = document.getElementById("modal-bx")
        
        openBtn.addEventListener("click", function(event){
            event.preventDefault();
            console.log("Hello this is a click");
            modalBg.classList.add("active");
            modalBx.classList.add("active");
        });

        const closeBtn=document.querySelectorAll(".js-close");
        console.log("Close Btn");
        closeBtn.forEach(node =>{
            console.log("node is", node);
            node.addEventListener("click", function(e){
                e.preventDefault();
                modalBg.classList.remove("active");
                modalBx.classList.remove("active");
            });
        });
        const acceptBtn=document.querySelectorAll(".js-close");
        console.log("Close Btn");
        closeBtn.forEach(node =>{
            console.log("node is", node);
            node.addEventListener("click", function(e){
                e.preventDefault();
                modalBg.classList.remove("active");
                modalBx.classList.remove("active");
            });
        });