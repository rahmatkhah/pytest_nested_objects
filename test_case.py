import pytest


class Worker:
    def __init__(self, name):
        self.name = name
        self.hours = 0

    def work(self):
        self.hours += 1

    def play(self):
        self.hours += 0.5


class Monitor:
    def __init__(self, worker: Worker):
        self.worker = worker

    def spend_a_day(self):
        while True:
            if self.__has_it_been_a_day():
                return
            self.worker.work()
            if self.__has_it_been_a_day():
                return
            self.worker.play()

    def __has_it_been_a_day(self):
        return self.worker.hours >= 24


def test_worker_work():
    worker = Worker('TEST')
    assert worker.hours == 0
    worker.work()
    assert worker.hours == 1


def test_worker_play():
    worker = Worker('TEST')
    assert worker.hours == 0
    worker.play()
    assert worker.hours == 0.5


def test_monitor_spend_a_day(mocker):
    worker = mocker.patch('test_case.Worker', spec=True)
    worker.name = 'TEST'
    worker.hours = 0
    monitor = Monitor(worker)
    monitor.spend_a_day()
    assert worker.hours >= 24
