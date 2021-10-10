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
   var formData = new FormData();
   formData.append("file", this.files[0]);
   $.ajax({
      url:"http://127.0.0.1:8000/home/process",
      type: 'POST',
      async: false,
      data: formData,
      contentType: false,
      processData: false,
      dataType: "text",
      success: function(data)
      {
        
         document.getElementById('ans').value = data
         json_value=JSON.parse()
         alert("This will be printed on success"+data['type_'])
      }
      
      // (data, status, jqXHR)=> alert("This will be printed on success"+data)
   })
});

  

