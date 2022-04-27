# Answer to 11 questions

### Question 1. (4 points) What is the default block size on HDFS? What is the default replication factor of HDFS on Dataproc?

The default block size on HDFS is 128MB.
Considering the performance and the reliability of storage inDataproc clusters, the default replication factor is set at 2.

### Question 2. (2 points) Use enwiki_test.xml as input and run the program locally on a Single Node cluster using 4 cores. Include your screenshot of the dataproc job. What is the completion time of the task?

The completion time for this job is 4 minutes and 55 seconds. 
<img width="1185" alt="Task2Q2" src="https://user-images.githubusercontent.com/90704283/165556745-e3cfe0e0-a2b1-466e-914f-cac662c61a1b.png">


### Question 3. (2 points) Use enwiki_test.xml as input and run the program under HDFS inside a 3 node cluster (2 worker nodes). Include your screenshot of the dataproc job. Is the performance getting better or worse in terms of completion time? Briefly explain.

The completion time is now 3 minutes and 13 seconds. the performance is improving in terms of completion time when compared with the single node cluster as now we can take advantage of the two worker nodes. 
<img width="1185" alt="Task2Q3" src="https://user-images.githubusercontent.com/90704283/165556716-16f45680-491b-4b49-8b13-254a38a05272.png">


### Question 4. (2 points) For this question, change the default block size in HDFS to be 64MB and repeat Question 3. Include your screenshot of the dataproc job. Record run time, is the performance getting better or worse in terms of completion time? Briefly explain.

The completion running time for this task was 3 minutes and 7 seconds so it was slightly faster than with the default block size on HDFS. I imagine that is becasue this smaller size allowed the data to be split itno smaller chunks and thus processed slightly faster by the worker nodes. 
<img width="1185" alt="Task2Q4" src="https://user-images.githubusercontent.com/90704283/165556685-afd49be4-6e58-4b23-9d7c-0c21459c2f86.png">
