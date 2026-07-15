function validateForm(){

    let inputs = document.querySelectorAll("input");

    for(let input of inputs){

        if(input.value === ""){

            alert("Please fill all fields");

            return false;
        }
    }

    return true;
}