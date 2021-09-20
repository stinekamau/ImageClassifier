const image_input = document.querySelector("#image_input");
console.debug("Outside the function")
image_input.addEventListener("change", function() {
   
   


   const reader = new FileReader();
   reader.addEventListener("load", () => {
   const uploaded_image = reader.result;

   // document.getElementById('ans').value = 40;
   document.querySelector("#display_image").style.backgroundImage = `url(${uploaded_image})`;
});
   reader.readAsDataURL(this.files[0]);
});

   const http = new XMLHttpRequest()

   http.open("GET", "http://127.0.0.1:8000/home");
   http.send();
   
   http.onreadystatechange = function() {
            
      if(http.readyState == 4) {
         console.log("Value of response is hehe  : "+http.response)
         document.getElementById('ans').value = http.response;

        
      }
   }
   
   http.onload = function() {
      let responseObj = http.response;
      alert(responseObj.message); 
      console.log("Value of responseObj "+responseObj)
      // Hello, world!
    };
    console.log("End of the function");
   
