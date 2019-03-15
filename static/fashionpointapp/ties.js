function printTies(n,x){
	var text="";
	for (var i = 0; i < n; i++) {
		if(i%2==1){
	 		text+="	<img class=\"tie\" src=\"/static/images/54458077_364690717465481_2362712318992711680_n.png\"/> ";
		 }
	}
	if(n%2==1){
		text+="<img class='tie' src=\"/static/images/53856595_2337553366296088_1102890933814296576_n.png\" //> \n";
	}
	n = 10-n
	for(var i = 0; i< n;i++){
		if(i%2==1){
	 			text+="<img class='tie' src=\"/static/images/54255324_381448649078050_8592250154898161664_n.png\"//> \n";
		 	}
	}
	document.getElementById(x).innerHTML=text;
}