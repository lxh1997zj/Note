# import collections

# # time 字段是事件发生时的仿真时间，
# # proc 字段是出租车进程实例的编号，
# # action 字段是描述活动的字符串。
# Event = collections.namedtuple('Event', 'time proc action')


# def taxi_process(proc_num, trips_num, start_time=0):
#     """
#     每次改变状态时创建事件，把控制权让给仿真器
#     :param proc_num:
#     :param trips_num:
#     :param start_time:
#     :return:
#     """
#     time = yield Event(start_time, proc_num, 'leave garage')

#     for i in range(trips_num):
#         time = yield Event(time, proc_num, 'pick up people')
#         time = yield Event(time, proc_num, 'drop off people')

#     yield Event(time, proc_num, 'go home')

# # run
# t1 = taxi_process(1, 1)
# a = next(t1)    
# print(a)    # Event(time=0, proc=1, action='leave garage')
# b = t1.send(a.time + 6)
# print(b)    # Event(time=6, proc=1, action='pick up people')
# c = t1.send(b.time + 12)
# print(c)    # Event(time=18, proc=1, action='drop off people')
# d = t1.send(c.time + 1)
# print(d)    # Event(time=19, proc=1, action='go home')





import collections
import queue
import random

# time 字段是事件发生时的仿真时间，
# proc 字段是出租车进程实例的编号，
# action 字段是描述活动的字符串。
Event = collections.namedtuple('Event', 'time proc action')


def taxi_process(proc_num, trips_num, start_time=0):
    """
    每次改变状态时创建事件，把控制权让给仿真器
    :param proc_num:
    :param trips_num:
    :param start_time:
    :return:
    """
    time = yield Event(start_time, proc_num, 'leave garage')

    for i in range(trips_num):
        time = yield Event(time, proc_num, 'pick up people')
        time = yield Event(time, proc_num, 'drop off people')

    yield Event(time, proc_num, 'go home')


class SimulateTaxi(object):
    """
    模拟出租车控制台
    """

    def __init__(self, proc_map):
        # 保存排定事件的 PriorityQueue 对象，
        # 如果进来的是tuple类型，则默认使用tuple[0]做排序
        self.events = queue.PriorityQueue()
        # procs_map 参数是一个字典,使用dict构建本地副本
        self.procs = dict(proc_map)

    def run(self, end_time):
        """
        排定并显示事件，直到时间结束
        :param end_time:
        :return:
        """
        for _, taxi_gen in self.procs.items():
            leave_evt = next(taxi_gen)
            self.events.put(leave_evt)

        # 仿真系统的主循环
        simulate_time = 0
        while simulate_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break

            # 第一个事件的发生
            current_evt = self.events.get()
            simulate_time, proc_num, action = current_evt
            print('taxi:', proc_num, ', at time:', simulate_time, ', ', action)

            # 准备下个事件的发生
            proc_gen = self.procs[proc_num]
            next_simulate_time = simulate_time + self.compute_duration()

            try:
                next_evt = proc_gen.send(next_simulate_time)
            except StopIteration:
                del self.procs[proc_num]
            else:
                self.events.put(next_evt)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))

    @staticmethod
    def compute_duration():
        """
        随机产生下个事件发生的时间
        :return:
        """
        duration_time = random.randint(1, 20)
        return duration_time


# 生成3个出租车，现在全部都没有离开garage
taxis = {i: taxi_process(i, (i + 1) * 2, i * 5)
         for i in range(3)}

# 模拟运行
st = SimulateTaxi(taxis)
st.run(100)
