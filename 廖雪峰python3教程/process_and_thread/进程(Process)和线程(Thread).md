# **进程(Process)和线程(Thread)**

## **多进程(multiprocessing)**

### **apply是阻塞式的：**

首先主进程开始运行，碰到子进程，操作系统切换到子进程，等待子进程运行结束后，在切换到另外一个子进程，直到所有子进程运行完毕。然后在切换到主进程，运行剩余的部分 。

### **apply_async是异步非阻塞式的：**

首先主进程开始运行，碰到子进程后，主进程说：让我先运行个够，等到操作系统进行进程切换的时候，在交给子进程运行。以为我们的程序太短，然而还没等到操作系统进行进程切换，主进程就运行完毕了。想要子进程执行，就告诉主进程：你等着所有子进程执行完毕后，在运行剩余部分。

```
pool.close()
pool.join()    
```

 <!---->close()必须在join()前面，Python官方建议：废弃apply，使用apply_async。

[参考自简书](https://www.jianshu.com/p/0a55507f9d9e?open_source=weibo_search)

### **Queue模块：**

import Queue

#### **将一个值放入队列中**

**q.put(10):**  调用队列对象的put()方法在队尾插入一个项目。put()有两个参数，第一个item为必需的，为插入项目的值；第二个block为可选参数，默认为 1。如果队列当前为空且block为1，put()方法就使调用线程暂停,直到空出一个数据单元。如果block为0，put方法将引发Full异常。 

#### **将一个值从队列中取出**

**q.get():**调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。如果队列为空且block为False，队列将引发Empty异常 。

[参考blog](https://blog.linuxeye.cn/334.html)

## 多线程

[多线程核心笔记](https://superxiaoxiong.github.io/2016/07/27/python-threading/#thread%E7%B1%BB%E8%BF%90%E8%A1%8C%E5%87%BD%E6%95%B0)   

[GIL](http://cenalulu.github.io/python/gil-in-python/)















