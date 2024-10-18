NOTE: 

1. each time you run pip, you need to restart the kernel
2. matplotlib can only render in svg for some reason
3. commands to build jupyterhub and spark integrations
    1. minikube start --cpus=4 --memory=16384
    2. minikube addons enable registry
    3. build and push docker images(pyspark, spark, singleuser) to minikube registry:
        a. docker build -t $(minikube ip):5000/pyspark:test -f kubernetes/dockerfiles/pyspark/Dockerfile .
        b. docker push --tls-verify=false $(minikube ip):5000/pyspark:test
    4. apply spark resources
        a. kubectl apply -f spark_ns.yaml
        b. kubectl apply -f spark_sa.yaml
        c. kubectl apply -f spark_sa_role.yaml
    5. test with spark-submit
        a. /opt/spark/bin/spark-submit --master k8s://https://$(minikube ip):8443 --deploy-mode cluster --driver-memory 1g --conf spark.kubernetes.memoryOverheadFactor=0.5 --name sparkpi-test1 --class org.apache.spark.examples.SparkPi --conf spark.kubernetes.container.image=spark:latest  --conf spark.kubernetes.driver.pod.name=spark-test1-pi  --conf spark.kubernetes.namespace=spark --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark  --verbose  local:///opt/spark/examples/jars/spark-examples_2.12-3.5.3.jar 1000
    6. apply spark driver resource
        a. kubectl apply -f driver_service.yaml
    7. apply jupyterhub resource
        a. kubectl apply -f jupyterhub_ns.yaml
        b. kubectl apply -f jupyperhub_sa.yaml
        c. kubectl apply -f jupyterhub_sa_role.yaml
    8. install jupyterhub using jhub_values.yaml
        a. helm upgrade --cleanup-on-fail --install jupyterhub jupyterhub/jupyterhub --namespace jupyterhub --create-namespace --version=3.3.8 --values jhub_values.yaml
    9. test using pyspark_k8s_example.ipynb
    10. issues:
        1. unable to read downloaded files
        2. it seems like it wants a hadoop like system to work with files

4. commands to run working local node
    1. su - hadoop
    2. start hadoop and yarn
        1. ~/hadoop-3.3.4/sbin/start-dfs.sh
        2. ~/hadoop-3.3.4/sbin/start-yarn.sh
    3. commands to interact with hdfs
        1. hadoop-3.3.4/bin/hdfs namenode -format
        1. hadoop-3.3.4/bin/hdfs dfs -ls /user/hadoop
        2. hadoop-3.3.4/bin/hdfs dfs -put rossmann-store-sales/train.csv
    4. commands related with ms sql server instance
        1. kubectl exec -it mssql-0 -- bash
        2. /opt/mssql-tools18/bin/sqlcmd -No -U sa
    5. jdbc driver error is solved by using mssql-jdbc-12.8.1.jre8.jar place it in $SPARK_HOME/jars folder. Note the jre8 part because we are using openjdk 8
    6. commands to start spark
        1. spark-3.5.3-bin-hadoop3/bin/spark-shell --master yarn --name interactive
        2. spark-3.5.3-bin-hadoop3/bin/pyspark --master yarn --name interactive
        3. spark-3.5.3-bin-hadoop3/bin/spark-submit --master yarn --name interactive test-mssql.py
        4. spark-3.5.3-bin-hadoop3/bin/spark-submit --class MSSQLStoredProcedureCall --master yarn ~/scala_work_dir/mssql_sp_demo/target/scala-2.12/mssql-store-procedure_2.12-1.0.jar
    7. scala commands
        1. after testing scala in spark-shell, build dir structure like scala_work_dir, then run 'sbt package'
    8. store procedure call with pyspark and scala:
        1. pyspark
            a. issue retrieving out parameter
        2. scala
            b. use java native sql classes
