docker run -v $(pwd):/workspace amitsaha/thrift-compiler thrift --gen py thrift/tutorial.thrift

docker run -v $(pwd):/workspace amitsaha/thrift-compiler thrift  --gen py thrift/shared.thrift

