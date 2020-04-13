let result =  document.getElementById("result");
let load = document.getElementById('load');
load.style.display='none';
let response_data = null
function ready_file(btnid){
	result.innerHTML='<center><h5 id="wait_msg">Loading...</h5></center>';
	let url = document.getElementById('url-field').value
	var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
		    result.innerHTML = '';
		    response_data = JSON.parse(this.responseText);
		    if (response_data.status == 1)
		    	download_ready(response_data);
		    else result.innerHTML = `<font color=red>${response_data.message}</font>`;
	    }
 	};
  xhttp.open("POST", "", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(`url=${url}&csrfmiddlewaretoken=${csrf_token}`)
}


function download_ready(data){

	element = new ElementCreator();

	element.add_attribute(element.img,{
		'src' :data.thumbnail_url,
		'id' : 'thumb_image',
		'class' : 'mb-2'
	});
	
	element.add_attribute(element.select,{
		'id' : 'select_video_option',
		'class' : 'form-control m-1',
	});

	element.add_attribute(element.button,{
		'class' : 'btn btn-success',
		'onclick' : 'download_video()',
		'id' : 'download_btn',
	});

	element.create_element('result',element.img);
	element.create_element('result',element.line_break);
	element.create_element('result',element.select);

	for (let i=0; i<data.video_avilable.length;i++){
		let temp_obj = new ElementCreator()
		temp_obj.add_attribute(temp_obj.option,{
			'value' : data.video_avilable[i],
		});
		temp_obj.create_element(
			'select_video_option',
			 temp_obj.option, 
			 child_innerHTML =`Resolution: ${data.video_avilable[i]}`
		);
	}

	element.create_element('result',element.button,child_innerHTML='Get this');
	
}


class ElementCreator {
	constructor (){
		this.div = document.createElement('div');
		this.select = document.createElement('select');
		this.option = document.createElement('option');
		this.img = document.createElement('img')
		this.button = document.createElement('button');
		this.line_break = document.createElement('br');
	}

	create_element(parrent_id,child,child_innerHTML=null){
		this.parrent_obj = document.getElementById(parrent_id)
		this.parrent = this.parrent_obj.appendChild(child)
		if (child_innerHTML != null)
			child.innerHTML = child_innerHTML
	}
	add_attribute(child,attr){
		for (let [attribute, value] of Object.entries(attr)) {
  				child.setAttribute(`${attribute}`,`${value}`)
		}
	}
}

function download_video(){
	load.style.display='block';
	setTimeout(function(){ 
		location.href = "#load";
	}, 1000);
	let resolution = document.getElementById('select_video_option').value;
	var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
		    let responseText_d = JSON.parse(this.responseText)
		    let video_url = '/media/temp/' + responseText_d.path
		    load.innerHTML=`<font color=#05C22D>Your file is ready</font><br><a href="${video_url}" class='btn btn-success' download>Download Now</a>`;
	    }
 	};
  xhttp.open("POST", download_url, true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send(`url=${response_data.url}&res=${resolution}&csrfmiddlewaretoken=${csrf_token}`);
}

