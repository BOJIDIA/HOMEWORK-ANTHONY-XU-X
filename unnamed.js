const butn = document.getElementById("addItemButton");
const item = document.getElementById("itemlist");
const lstItem = document.getElementById("itemInput");
const nameBox = document.getElementById("name"); // for name checking
const emailBox = document.getElementById("email"); // for email checking
const passwordBox = document.getElementById("password"); // for password checking 
const repeatPasswordBox = document.getElementById("repeatPassword"); // for repeat password checking
const submitBtn =  document.getElementById("submitButton"); // for submit button checking
const nameError = document.getElementById("nameError");

function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+.[^\s@]+$/;
    return emailRegex.test(email);
  }

butn.onclick = function(){
    if (lstItem.value  !== ""){
        const txt = document.createTextNode(lstItem.value);
        const lstElement = document.createElement("li");
        lstElement.appendChild(txt)
        const ulElement = document.getElementById("itemList");
        ulElement.appendChild(lstElement);
        lstItem.value = "";
    }
}

lstItem.addEventListener("keyup", function (event) {
    if (event.code === "Enter") {
        butn.onclick();
    }
});

submitBtn.onclick = function() {
    // check if name field is not empty
    if (nameBox.value === "") {
        nameError.innerHTML = "Name Field is Empty";
    }
    else {
        nameError.innerHTML = "";
    }

    // check if email is a valid email format
    if (!validateEmail(emailBox.value)) {
        // display the error
    }
    
    // check if password is >= 8 characters
    // check if password has at least one uppercase
    // check if password has at least one lowercase
    // check if password has at least one digit

    

    // check if repeat password is the same as password
    if (repeatPasswordBox.value !== passwordBox.value) {
        // display the error message
    }

    // if everything passes then display success message
}
