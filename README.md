# Answer to 11 questions

### Question 1. (4 points) What is the default block size on HDFS? What is the default replication factor of HDFS on Dataproc?

The default block size on HDFS is 128MB.
Considering the performance and the reliability of storage inDataproc clusters, the default replication factor is set at 2.

### Question 2. (2 points) Use enwiki_test.xml as input and run the program locally on a Single Node cluster using 4 cores. Include your screenshot of the dataproc job. What is the completion time of the task?

The completion time for this job is 9 minutes and 21 seconds. 
<img width="796" alt="Q2" src="https://user-images.githubusercontent.com/90704283/165850213-44f923a7-38d7-46f1-9a1d-2c88e10ca87a.png">


### Question 3. (2 points) Use enwiki_test.xml as input and run the program under HDFS inside a 3 node cluster (2 worker nodes). Include your screenshot of the dataproc job. Is the performance getting better or worse in terms of completion time? Briefly explain.

The completion time is now 5 minutes and 13 seconds. The performance is improving in terms of completion time when compared with the single node cluster as now we can take advantage of the two worker nodes. 

<img width="796" alt="Q3" src="https://user-images.githubusercontent.com/90704283/165853515-ed45fd77-a25e-4fb7-a6c9-a94bee28beb4.png">

### Question 4. (2 points) For this question, change the default block size in HDFS to be 64MB and repeat Question 3. Include your screenshot of the dataproc job. Record run time, is the performance getting better or worse in terms of completion time? Briefly explain.

The completion time is now 5 minutes and 38 seconds which is only sloightly slower than the time with the default HDSF block size which makes me think that the block size does not have a large impact on running time. 

<img width="796" alt="Q4" src="https://user-images.githubusercontent.com/90704283/165857441-be9bba58-fcba-42de-99eb-81e0fb32507e.png">


