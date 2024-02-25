# AI-Internship-Assignment-
Assignment Title: MultiThreaded Priority Queue Implementation Architecture and Design Documentation

The multi-threaded priority queue system consists of three main components:

Priority Message Queue: A data structure that supports enqueueing, dequeueing, peeking, and empty checking with varying priorities.
Thread Pool: A fixed number of worker threads that execute tasks concurrently.
Message Sending Function: A function that allows threads to send messages to other threads with a specified priority.
Data Structures

Priority Queue: A queue data structure with a priority value associated with each message. The priority queue is implemented using a binary heap to ensure efficient enqueueing and dequeueing operations.
Thread Pool: A fixed number of worker threads that are initialized at startup. Each worker thread has its own task queue to ensure thread safety.
Message: A data structure that contains a message string and a priority value.
Algorithms

Priority Queue: The priority queue is implemented using a binary heap with the following operations:
Enqueue: Add a new message to the binary heap and maintain the heap property.
Dequeue: Remove and return the message with the highest priority.
Peek: Return the message with the highest priority without removing it.
Empty check: Check if the binary heap is empty.
Thread Pool: The thread pool is implemented using a fixed number of worker threads that execute tasks concurrently. The tasks are added to the worker threads' task queues using a lock-free queue data structure to ensure thread safety.
Synchronization Mechanisms

Mutex: Used to protect the priority queue from concurrent access.
Condition Variables: Used to wake up sleeping threads when a message is enqueued.
Source Code and Test Code

The source code and test code can be found in the Git repository provided with the assignment. The source code contains the following files:

priority_queue.py: Header file for the priority queue implementation.
thread_pool.py: Header file for the thread pool implementation.
message_queue.py: Header file for the message queue implementation.
To build and run the program, follow these steps:

Clone the Git repository.
Navigate to the repository directory.
Run make to build the program.
Run ./message_queue to execute the program.
Test Cases and Expected Outcomes

The main program contains test cases that demonstrate the functionality of the message queue system. The expected outcomes are displayed on the console.

Additional Notes and Insights

During the implementation process, the following good design and coding concepts were used:

Lock-free queue: A lock-free queue data structure was used to ensure thread safety when adding tasks to the worker threads' task queues.
Mutex and Condition Variables: Mutex and condition variables were used to protect the priority queue from concurrent access and wake up sleeping threads when a message is enqueued.
Binary Heap: A binary heap was used to implement the priority queue to ensure efficient enqueueing and dequeueing operations.
README for Execution

The README file in the Git repository contains instructions for building and running the program. It also provides an overview of the implemented solution, a description of the data structures and algorithms used, and an explanation of the test cases and their expected outcomes.
