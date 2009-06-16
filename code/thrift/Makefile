clean:
	rm -rf gen-py/ gen-php/
	rm "*.pyc"

run-server:
	python py/server.py

thrift: clean
	thrift --gen php --gen py:new_style service.thrift
