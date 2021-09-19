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

   http.open("GET", "http://127.0.0.1:8000/home")
   http.send()
   
   http.onload = ()=>{
      console.log("Just inside the onLoad");
      // console.log(xhttp.responseText)
      // console.log("something  on the onload")
      // document.getElementById("ans").ans = xhttp.responseText;
      if (http.status != 200) { // analyze HTTP status of the response
      
         alert(`Error ${http.status}: ${http.statusText}`); // e.g. 404: Not Found
       } else { // show the result
         alert(`Done, got ${http.response.length} bytes`); // response is the server response
       }
   };
   
