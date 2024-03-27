const imageInput = document.querySelector("#id_image")
const imagePreview = document.querySelector("#cover-image")

imageInput.addEventListener('change', (e) => {
  
  if (!e.target.files[0]) return
  
  const reader = new FileReader()

  reader.onloadend = () => {
    const value = reader.result

    if (value) {
      imagePreview.setAttribute("src", value.toString())
    }
  }

  reader.readAsDataURL(e.target.files[0])
})