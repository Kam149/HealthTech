#!C:\Python37\python.exe

print("content-type:text/html")
print("")
import cgi,cgitb
from code import loadFile
from code import runQuery
from code import fetchRecords
import datetime

now = datetime.datetime.now()

frm = cgi.FieldStorage()

uid = frm.getvalue("uid")
msg = frm.getvalue("msg")
if uid is not None:
	date = str(now.day) + "/" +str(now.month) + "/" +str(now.year) 
	qu = "insert into post(post_msg,post_date,post_by) values('{msg}','{date}',{uid})".format(msg=msg,date=date,uid=uid)
	runQuery(qu)


post = fetchRecords("select user_name,post_msg,post_date from post,user where user.user_id=post.post_by order by post_id DESC")	

postdata = """
	<div class="row">
		<div class="col-md-2"></div>
			<div class="col-md-7">
				<p>
				{msg}
				</p>
			</div>
			<div class="col-md-3">
				<h5 class="text-info">{date}</h5>
				<h6 class="text-danger">{name}</h6>
			</div>
		<div class="col-md-2"></div>		
	</div>
	<hr>
"""

menu = loadFile("usermenu.html")
footer = loadFile("footer.html")

content="""
<div id="services">
  <div class="container">
		<h1>Hello User</h1>

		<form method="post">
			<input type="hidden" id="uid" name="uid">
			<div class="row">			
				<div class="col-md-2"></div>
				<div class="col-md-6 col-sm-10">
					<textarea name="msg" class="btn-info text-danger" cols="50" rows="4" required>
					</textarea>
				</div>				
				<div class="col-md-2 col-sm-2">
					<button type="submit" class="btn btn-warning">Send</button>
				</div>				
				<div class="col-md-2"></div>
			</div>			
		</form>

<h1>Previous Post</h1>		
"""
for p in post:
	content += postdata.format(msg=p[1],date=p[2],name=p[0])

content += """</div></div>


<script>
	uid = localStorage.getItem("user");
	if(uid==null)
	{
		window.location = "home.py";
	}else
	{
	document.getElementById("uid").value = uid;
	}
</script>
"""




data = menu + content +footer

print(data)