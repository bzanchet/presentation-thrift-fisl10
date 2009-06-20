# benchmaks

thrift-benchmark-php:
	time php -f php/client.php

thrift-benchmark-py:
	time python py/client.py


# plumbing

clean:
	rm -rf gen-py/ gen-php/ gen-java/ gen-rb/

run-server:
	python py/server.py

thrift: clean
	thrift --gen php --gen py:new_style service.thrift

thrift-examples: clean
	thrift --gen php --gen java --gen rb --gen py:new_style examples.thrift
