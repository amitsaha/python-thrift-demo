docker run -v $(pwd):/workspace amitsaha/thrift-compiler thrift --gen py thrift/tutorial.thrift

docker run -v $(pwd):/workspace amitsaha/thrift-compiler thrift  --gen py thrift/shared.thrift

check http://paulosman.me/2011/12/12/services-with-apache-thrift.html

