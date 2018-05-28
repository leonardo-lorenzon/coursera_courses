function press() {
	console.log("Start");
	var name = prompt("What is you name?");
	alert("Hi "+name);
	document.write("Hi "+name);
	document.write(Date());
	document.write(window.location);
	console.log("Finish");
}