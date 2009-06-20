import cjson
import simplejson
import httplib
import urllib

def rest_benchmark():
    server = "localhost";
    get_url = "/service/user_get.php?user_id=27"
    post_url = "/service/user_post.php"
    
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    params = urllib.urlencode({'id': 27, 'name': 'luis inacio', 'style': 2})
    
    conn = httplib.HTTPConnection(server)
    for i in range(1000):
        for j in range(9):
            conn.request("GET", get_url)
            response = conn.getresponse()
            data = response.read()
            #user = simplejson.loads(data)
            user = cjson.decode(data)
            assert(user["id"] == "27")

        conn.request("POST", post_url, params, headers)
        response = conn.getresponse()
        data = response.read()
        assert(data == "OK")
        
        if i % 100 == 0:
            print i
    conn.close()

rest_benchmark()
