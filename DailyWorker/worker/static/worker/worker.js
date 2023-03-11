// alert("connected")
document.addEventListener('DOMContentLoaded', function() {

document.querySelector('#workshop').addEventListener('click', () => load_data('workshop'));
document.querySelector('#worker-link').addEventListener('click', () => load_data('worker'));
document.querySelector('#rent-link').addEventListener('click', () => load_data('rent'));


});


function load_data(link) {
	if (link == "workshop") {
		fetch("/")
	.then(response => response.text())
	.then(response =>{
		document.querySelector('body').innerHTML = response;
	})
	}
	else if (link == "worker") {
		fetch("/worker")
	.then(response => response.text())
	.then(response =>{
		document.querySelector('body').innerHTML = response;
	})
	}
	else if (link == "rent") {
		fetch("/rent")
	.then(response => response.text())
	.then(response =>{
		document.querySelector('body').innerHTML = response;
	})
	}




}