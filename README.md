# Answer to 11 questions

### Question 1. (4 points) What is the default block size on HDFS? What is the default replication factor of HDFS on Dataproc?

The default block size on HDFS is 128MB.
Considering the performance and the reliability of storage inDataproc clusters, the default replication factor is set at 2.

### Question 2. (2 points) Use enwiki_test.xml as input and run the program locally on a Single Node cluster using 4 cores. Include your screenshot of the dataproc job. What is the completion time of the task?

The completion time for this job is 9 minutes and 21 seconds. 
<img width="796" alt="Q2" src="https://user-images.githubusercontent.com/90704283/165857641-f0d3b4ba-d287-4022-ae44-4bc45ba92d48.png">
Q3


### Question 3. (2 points) Use enwiki_test.xml as input and run the program under HDFS inside a 3 node cluster (2 worker nodes). Include your screenshot of the dataproc job. Is the performance getting better or worse in terms of completion time? Briefly explain.

The completion time is now 5 minutes and 13 seconds. The performance is improving in terms of completion time when compared with the single node cluster as now we can take advantage of the two worker nodes. 

<img width="796" alt="Q3" src="https://user-images.githubusercontent.com/90704283/165857750-cd8d4fb8-b59f-4404-99fa-84b4f63c85ce.png">


### Question 4. (2 points) For this question, change the default block size in HDFS to be 64MB and repeat Question 3. Include your screenshot of the dataproc job. Record run time, is the performance getting better or worse in terms of completion time? Briefly explain.

The completion time is now 5 minutes and 38 seconds which is only sloightly slower than the time with the default HDSF block size which makes me think that the block size does not have a large impact on running time. 

<img width="796" alt="Q4" src="https://user-images.githubusercontent.com/90704283/165857441-be9bba58-fcba-42de-99eb-81e0fb32507e.png">

### Question 5 Use enwiki_whole.xml as input and run the program under HDFS inside the Spark cluster you deployed. Record the completion time. Now, kill one of the worker nodes immediately. You could kill one of the worker nodes by go to the VM Instances tab on the Cluster details page and click on the name of one of the workers. Then click on the STOP button. Record the completion time. Does the job still finish? Do you observe any difference in the completion time? Briefly explain your observations. Include your screenshot of the dataproc jobs.

The job with two worker nodes took 1 hr and 13 minutes to complete successfully. 
<img width="796" alt="Q5_1" src="https://user-images.githubusercontent.com/90704283/165866143-cd3c1ee6-9a31-4cbe-854c-ebce777186fd.png">

When i restarted the job and immidiately killed one of the nodes, the job did finish but was much slower. It took 2 hours and 21 minutes whihc is almost double the original running time. This makes sense since we only had one worker node instead of two.
<img width="796" alt="Q2_2" src="https://user-images.githubusercontent.com/90704283/165877615-ecd52922-670d-4511-88dd-0feddc5b22fe.png">


### Question 6 Only for this question, change the replication factor of enwiki_whole.xml to 1 and repeat Question 5 without killing one of the worker nodes. Include your screenshot of the dataproc job. Do you observe any difference in the completion time? Briefly explain.

The completion time was 1 hr and 14 minutes which is almost exactly the same as the original job. This means that the code did not need to access replicated data and was able to finish successfully. 
<img width="796" alt="Q6" src="https://user-images.githubusercontent.com/90704283/166080237-2c7b711a-de4d-40ef-a7bf-6492feaad727.png">

### Question 7. (2 points) Only for this question, change the default block size in HDFS to be 64MB and repeat Question 5 without killing one of the worker nodes. Record run time, include your screenshot of the dataproc job. Is the performance getting better or worse in terms of completion time? Briefly explain.

The run time was 1 hr and 15 minutes which is almost the same as the original running time. This indicates that the block size does not have a significant impact on running time. 

<img width="796" alt="Q7" src="https://user-images.githubusercontent.com/90704283/166084281-ea006c57-1adc-4946-9a66-eef810a91f2d.png">


>>>>>>> d3c7c02209d30935dfc8fc898ee1fff8e2707bee

### **Question 8.** (2 points) Use your output from Task 2 with `enwiki_whole.xml` as input, run Task 3 using a 3 node cluster (2 worker nodes). Include your screenshot of the dataproc job. What is the completion time of the task?

I used 36 minutes to run it.

![image-20220429214307886](/Users/mac/Library/Application Support/typora-user-images/image-20220429214307886.png)




### **Question 9** (2 points) Start a PageRank program you wrote in Part 1 Task 3 whose input is the link graph generated from “enwiki_whole.xml” and store the output to a directory inside HDFS. Set your stream receiver to read the files generated by the PageRank program. Kill the receiver when the PageRank task is finished. How many articles in the database has a rank greater than **0.5**?

1265848 articles in the database has a ranker greater than 0.5.





### **Question 10** (2 points) Spark Streaming can also be used to send data via TCP sockets. The Emitter in this case will wait on a socket connection request from the receiver, and upon accepting the connection request it will start sending data. Do you think such data server design is feasible and efficient? Briefly explain.



The data server design is feasible because data could be transferred through TCP socket. However, it is not efficient because we already get the data on the HDFS, and we could just read the data from HDFS instead of transmitting the data through network.



### **Questions 11** (2 points) How many hours did you spend in this assignment?

I think each of us spent more than 40 hours on it.

