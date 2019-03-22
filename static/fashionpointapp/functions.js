		var inc = 0;
				function next(){
					inc+=3;
					$.ajax({
						type:"GET",
						url: "{% url 'updatePosts'%}",
						data: {'inc': inc}})
						.done(function(response) {
								document.getElementById("everything").innerHTML=response;
					});
				}
				function prev(){
					inc-=3;
					$.ajax({
						type:"GET",
						url: "{% url 'updatePosts'%}",
						data: {'inc': inc}})
						.done(function(response) {
								document.getElementById("everything").innerHTML=response;
					});
				}
				var inc2 = 0;
				function nextPolls(){
					inc2+=2;
					$.ajax({
						type:"GET",
						url: "{% url 'updatePolls'%}",
						data: {'inc': inc2}})
						.done(function(response) {
								document.getElementById("everything2").innerHTML=response;
					});
				}
				function prevPolls(){
					inc2-=2;
					$.ajax({
						type:"GET",
						url: "{% url 'updatePolls'%}",
						data: {'inc': inc2}})
						.done(function(response) {
								document.getElementById("everything2").innerHTML=response;
					});
				}
				function findStars(x){
var y = Math.round(x*2);
var a = ['star1','star2','star3','star4','star5'];
for(i = 0;i<parseInt(y/2);i++)
  a[i] = "<img style=\"animation: arrive 200ms ease-in-out 0s forwards;\" class=\"tie1\"  src=\"{% static 'images/54458077_364690717465481_2362712318992711680_n.png'%}\"/>";
if(y%2==1){
    a[i] = '<img style="animation: arrive 200ms ease-in-out 0s forwards;" class=\"tie1\"  src=\"{% static 'images/53856595_2337553366296088_1102890933814296576_n.png'%}\"/>';
     i++;
}
for(;i<5;i++)
  a[i] = '<img style=\"animation: arrive 200ms ease-in-out 0s forwards\" class=\"tie1\"  src=\"{% static 'images/54255324_381448649078050_8592250154898161664_n.png'%}\"/>';
var text= a[0]+"<div id=\"star2\" style=\"display:flex;flex-direction: row;\">"
+a[1]
                   + "<div  style=\"display:flex;flex-direction: row;\">"
                    +a[2]
                    + "<div style=\"display:flex;flex-direction: row;\">"
                     +a[3]
                    +"<div  style=\"display:flex;flex-direction: row;\">"
                    +a[4]
                   +"</div>"
                  +"</div>"
                 +"</div>"
                +"</div>"
                document.getElementById("star1").innerHTML=text;

}
function like(x,t,nol,nod){
    var type = 0;
    if((document.getElementById('dislike'+x).className === 'dislike')&&(document.getElementById('like'+x).className !== 'like')&&(t==0))
        type = 1;
    if((document.getElementById('dislike'+x).className !== 'dislike')&&(document.getElementById('like'+x).className === 'like')&&(t==0))
        type = 2;
    if((document.getElementById('dislike'+x).className === 'dislike')&&(document.getElementById('like'+x).className === 'like')&&(t!=0))
        type = 3;
    if((document.getElementById('dislike'+x).className === 'dislike')&&(document.getElementById('like'+x).className !== 'like')&&(t!=0))
        type = 4;
    if((document.getElementById('dislike'+x).className !== 'dislike')&&(document.getElementById('like'+x).className === 'like')&&(t!=0))
        type = 5;
     if(t==0){
        document.getElementById('dislike'+x).className = 'dislike';
        if(document.getElementById('like'+x).className === 'like')
                document.getElementById('like'+x).className = 'likeClicked';
        else
                document.getElementById('like'+x).className = 'like';
        }
     else{
      document.getElementById('like'+x).className = 'like';
        if(document.getElementById('dislike'+x).className === 'dislike')
                document.getElementById('dislike'+x).className = 'dislikeClicked';
        else
                document.getElementById('dislike'+x).className = 'dislike';
     }
     $.ajax({
                url: '{% url 'updateLike'  post %}',
                type: "POST",
                dataType: "json",
                data: {
                    comment: x,
                    type: type,
                    csrfmiddlewaretoken: '{{ csrf_token }}',
                    },
            }).always(function(){
                        showMore(50);
            });
}
function showStars(x){
var a =['cursor:default	;  animation: arrive 200ms ease-in-out 0s forwards;','cursor:default;  animation: arrive 400ms ease-in-out 0s forwards;','cursor:default;  animation: arrive 600ms ease-in-out 0s forwards;','cursor:default;  animation: arrive 800ms ease-in-out 0s forwards;','cursor:default;  animation: arrive 1000ms ease-in-out 0s forwards;'];

for(var i = 0;i<=x;i++)
a[i-1]+="filter:brightness(200%);"
text = "<label style=\"margin-right:45px;\">You Rated:</label> "
        +"<div style=\"display:flex;flex-direction: row; margin:10px 20px 10px 80px;\" >"
        +"        <img style=\""+a[0]+"\" class=\"tie1\" src=\"{% static 'images/54255324_381448649078050_8592250154898161664_n.png'%}\"/>"
        +"        <div style=\"display:flex;flex-direction: row;\">"
        +"            <img style=\""+a[1]+"\" class=\"tie1\" src=\"{% static 'images/54255324_381448649078050_8592250154898161664_n.png'%}\"/>"
        +"            <div style=\"display:flex;flex-direction: row;\">"
        +"                <img style=\""+a[2]+"\" class=\"tie1\" src=\"{% static 'images/54255324_381448649078050_8592250154898161664_n.png'%}\"/>"
        +"                <div style=\"display:flex;flex-direction: row;\">"
        +"                    <img style=\""+a[3]+"\" class=\"tie1\" src=\"{% static 'images/54255324_381448649078050_8592250154898161664_n.png'%}\"/>"
        +"                    <div style=\"display:flex;flex-direction: row;\">"
		+"		                <img style=\""+a[4]+"\" class=\"tie1\" src=\"{% static 'images/54255324_381448649078050_8592250154898161664_n.png'%}\"/>"
        +"                    </div>"
        +"                </div>"
        +"            </div>"
        +"        </div>"
        +"    </div>"
   document.getElementById("stars").innerHTML=text ;
}


function shine(ID,x){
    var ids = ['tie1','tie2','tie3','tie4','tie5'];
    for( var i = 1; i<=ID;i++)
        document.getElementById(ids[i-1]).style.filter = "brightness("+x+"%)" ;
}

         function select(x) {
             $.ajax({
                url: "update_avg/",
                type: "POST",
                dataType: "json",
                data: {
                    value: x,
                    csrfmiddlewaretoken: '{{ csrf_token }}',
                    },
                error : function(xhr,errmsg,err) {
                    alert("Could not send URL to Django. Error: " + xhr.status + ": " + xhr.responseText);
                }
            }).always(function(){
                        showStars(x);
            });
         }
         var ind = 0;
         function showMore(x){
         if(x==1)
          ind+=5;
          $.ajax({
					type:"GET",
					url: "{% url 'showMore' post %}",
					data: {'ind': ind}})
					.done(function(response) {
					$("#commentstab").html(response);
			});

         }
        function comment() {
        ind = 4565465;
        var comment = document.getElementById("AcutalComment").value;
        if(comment){
         $.ajax({
                url: '{% url 'makeComment'  post %} ',
                type: "POST",
                dataType: "json",
                data: {
                    comment: comment ,
                    csrfmiddlewaretoken: '{{ csrf_token }}',
                },
            }).always(function () {
               $.ajax({
                url: '{% url 'update_comments'  post %} ' ,
                type: "GET",}).done(function (response) {
					$("#commentstab").html(response);
                  });
         });
         document.getElementById("AcutalComment").value = "";
         }
         }
         function likePoll(x,t,nol,nod){
    var type = 0;
    if((document.getElementById('dislike'+x).className === 'dislike')&&(document.getElementById('like'+x).className !== 'like')&&(t==0))
        type = 1;
    if((document.getElementById('dislike'+x).className !== 'dislike')&&(document.getElementById('like'+x).className === 'like')&&(t==0))
        type = 2;
    if((document.getElementById('dislike'+x).className === 'dislike')&&(document.getElementById('like'+x).className === 'like')&&(t!=0))
        type = 3;
    if((document.getElementById('dislike'+x).className === 'dislike')&&(document.getElementById('like'+x).className !== 'like')&&(t!=0))
        type = 4;
    if((document.getElementById('dislike'+x).className !== 'dislike')&&(document.getElementById('like'+x).className === 'like')&&(t!=0))
        type = 5;
     if(t==0){
        document.getElementById('dislike'+x).className = 'dislike';
        if(document.getElementById('like'+x).className === 'like')
                document.getElementById('like'+x).className = 'likeClicked';
        else
                document.getElementById('like'+x).className = 'like';
        }
     else{
      document.getElementById('like'+x).className = 'like';
        if(document.getElementById('dislike'+x).className === 'dislike')
                document.getElementById('dislike'+x).className = 'dislikeClicked';
        else
                document.getElementById('dislike'+x).className = 'dislike';
     }
     $.ajax({
                url: '{% url 'updateLikeP'  poll %}',
                type: "POST",
                dataType: "json",
                data: {
                    comment: x,
                    type: type,
                    csrfmiddlewaretoken: '{{ csrf_token }}',
                    },
            }).always(function(){
                        showMoreP(50);
            });
}
     function clicking(c1,c2,type){
       $.ajax({
                url: '{% url 'click'  poll %} ',
                type: "POST",
                dataType: "json",
                data: {
                    csrfmiddlewaretoken: '{{ csrf_token }}',
                    picture:type
                 }
         });
         if(type == 1)
            c1++;
         else
            c2++;
         var x = parseInt(c2/(c1+c2)*100);
         document.getElementById("cc").innerHTML = "<div class=\"pie\" style=\"--segment1: "+ x +"; --segment2: 100;\"></div>"
         +"<span class=\"dot\" style=\"background-color: #398AD7;\"></span> <label style=\"margin-right:10px;\">left picture</label>"
         +"<span class=\"dot\" ></span> <label>right picture</label>";
         document.getElementById("p1").innerHTML ="<img id=\"image1\"class = \"pollimage\" src=\"/media/{{ poll.picture1 }}\">";
         document.getElementById("p2").innerHTML ="<img id=\"image2\" class = \"pollimage\" src=\"/media/{{ poll.picture2 }}\">";
     }
     var ind = 0;
     function showMoreP(x){
         if(x==1)
          ind+=5;
          $.ajax({
					type:"GET",
					url: "{% url 'showMoreP' poll %}",
					data: {'ind': ind}})
					.done(function(response) {
					$("#commentstab").html(response);
			});

         }
     function newCommentP(event) {
        ind = 55465456;
        var comment = document.getElementById("AcutalComment").value ;
         $.ajax({
                url: '{% url 'makepollComment' poll %} ',
                type: "POST",
                dataType: "json",
                data: {
                    comment: comment ,
                    csrfmiddlewaretoken: '{{ csrf_token }}',
                    },
            }).always(function () {
               showMoreP(50);
         });
         document.getElementById("AcutalComment").value = "";
     }