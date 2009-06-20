import cjson
import simplejson
import httplib
import urllib

def rest_benchmark():
    server = "localhost";
    get_url = "/service/user_get.php?user_id=27"
    post_url = "/service/user_post.php"
    
    
    for i in range(1000):
        conn = httplib.HTTPConnection(server)
        for j in range(9):
            conn.request("GET", get_url)
            response = conn.getresponse()
            data = response.read()
            #user = simplejson.loads(data)
            user = cjson.decode(data)
            assert(user["id"] == "27")
        conn.close()

        conn = httplib.HTTPConnection(server)
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        params = urllib.urlencode({'id': 27, 'name': 'luis inacio', 'style': 2})
        conn.request("POST", post_url, params, headers)
        response = conn.getresponse()
        data = response.read()
        assert(data == "OK")
        conn.close()
        
        if i % 100 == 0:
            print i

rest_benchmark()
