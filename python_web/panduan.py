login_information = [
{
	"email" :"2368898533@qq.com",
	"password":"12345678",
},

{
	"email" :"1494696665@qq.com",
	"password":"1245678",
},

{
	"email" :"lin1124qw@gmail.com",
	"password":"12345678",
}

]

def panduan_login(email, password):
	for item in login_information:
		if item["email"] == email and item["password"] == password:
			return "true"

def panduan_liebiao():
	a = login_information
	return a
