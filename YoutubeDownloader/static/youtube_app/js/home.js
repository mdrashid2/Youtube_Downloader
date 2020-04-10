let result =  document.getElementById("result")
function ready_file(btnid){
	result.innerHTML='<center><h5 id="wait_msg">Loading...</h5></center>';
	let url = document.getElementById('url-field').value
	var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
	    	let data = JSON.parse(this.responseText)
		    result.innerHTML = data;
	    }
 	};
  xhttp.open("POST", "", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(`url=${url}&csrfmiddlewaretoken=${csrf_token}`)
}