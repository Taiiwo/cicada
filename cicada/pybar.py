import sys
import time

# Keeps track of an iteration
class Tracker:
    def __init__(self, max=False, index=0):
        self.max = max
        self.index = index
        self.times = []
        self.time = time.time()
        self.start = self.time

    def next(self):
        t = time.time()
        self.times.append(t - self.time)
        self.time = t
        self.index += 1

class PyBar:
    def __init__(self, tracker=None, max=False, poll=1, pad=" "):
        self.pad = pad
        self.poll = poll
        self.last_poll = 0
        self.max = max
        self.default_tracker = tracker if tracker else Tracker(max=max)
        self.args = []
        self.stdout_length = 0
        self.vars = {}

    """
    Begin bar modules
    """

    def progress(self, tracker=False):
        tracker = tracker if tracker else self.default_tracker
        return lambda: "%s/%s" % (tracker.index, tracker.max)

    def bar(self, width=25, progress="▣", empty="▢", tracker=False):
        tracker = tracker if tracker else self.default_tracker
        def a():
            p = int(width * tracker.index / tracker.max)
            return (progress * p) + (empty * (width - p))
        return a

    def avg(self, length=5, places=3, tracker=False):
        tracker = tracker if tracker else self.default_tracker
        def a():
            if len(tracker.times) < 1:
                return "N/A"
            l = len(tracker.times) if len(tracker.times) < length else length
            return str(round(float(sum(tracker.times[-l:]) / l), places))
        return a

    def rate(self, places=3, time=1, length=5, tracker=None):
        tracker = tracker if tracker else self.default_tracker
        def a():
            if len(tracker.times) < 1:
                return "N/A"
            l = len(tracker.times) if len(tracker.times) < length else length
            avg = float(sum(tracker.times[-l:]) / l)
            avg = 0.00000001 if avg == 0 else avg # lol
            return str(round(time / avg, 3)) + "/s" if time == 1 else ""
        return a

    def elapsed(self, tracker=None):
        tracker = tracker if tracker else self.default_tracker
        def a():
            return time.strftime("%H:%M:%S", time.gmtime(tracker.time - tracker.start))
        return a

    def eta(self, length=5, tracker=None):
        tracker = tracker if tracker else self.default_tracker
        def a():
            if len(tracker.times) < 1:
                return "infinity"
            l = len(tracker.times) if len(tracker.times) < length else length
            avg = float(sum(tracker.times[-l:]) / l)
            return time.strftime("%H:%M:%S", time.gmtime(
                (tracker.max - tracker.index) * avg
            ))
        return a


    def percent(self, places=3, tracker=None):
        tracker = tracker if tracker else self.default_tracker
        def a():
            return ("%s%%") % str(round(tracker.index / tracker.max * 100, places))
        return a

    """
    End bar modules
    """

    # prints something above the bar without distrupting it
    def echo(self, *args):
        clear = " " * self.stdout_length
        self.write(clear)
        sys.stdout.write("\r")
        sys.stdout.flush()
        print(" ".join([str(s) for s in args]))
        self.update(*self.args, now=True)

    # writes to the bar
    def write(self, text):
        sys.stdout.write("\r")
        sys.stdout.flush()
        sys.stdout.write(text)
        sys.stdout.flush()
        self.stdout_length = len(text)

    # increments the index of the default tracker
    def next(self):
        self.default_tracker.next()
        self.update()

    # updates the content of the bar with new information
    # if next: also updates the index of the bar
    # if now: bypasses bar polling and writes to the bar immediately
    def update(self, *args, next=False, now=False):
        if len(self.args) < 1: self.args = args
        if len(args) < 1: args = self.args
        if next: self.default_tracker.next()
        t = time.time()
        if not now and t - self.last_poll < self.poll:return
        self.last_poll = t
        bar = ""
        for arg in args:
            if callable(arg):
                bar += arg() + self.pad
            else:
                bar += arg + self.pad
        self.write(bar)

    # artificially completes the bar, and prints a success bar to a new line
    def done(self, *args, trackers=[]):
        bar = ""
        trackers.append(self.default_tracker)
        for tracker in trackers:
            tracker.index = tracker.max
        for arg in self.args:
            if callable(arg):
                bar += arg() + self.pad
            else:
                bar += arg + self.pad
        self.write(bar)
        bar = ""
        for arg in args:
            if callable(arg):
                bar += arg() + self.pad
            else:
                bar += arg + self.pad
        print("\n" + bar)

    # Just like python's range, but automatically sets the max of a tracker
    def range(self, *args, tracker=None):
        tracker = tracker if tracker else self.default_tracker
        low = args[0] if len(args) >= 2 else 0
        high = args[1] if len(args) >= 2 else args[0]
        inc = args[2] if len(args) >= 3 else 1
        i = low
        tracker.max = int((high - low) / inc)
        while i < high:
            yield i
            i += inc

if __name__ == "__main__":
    # make a new bar
    bar = PyBar(max=10, poll=0)
    for i in range(10):
        time.sleep(0.1)
        # tracks another iteration
        track = Tracker(max=10)
        for x in range(10):
            time.sleep(0.1)
            # increment the other iteration
            track.next()
            # update the bar values
            bar.update(bar.progress(), bar.bar(), bar.bar(tracker=track))
        # increment that main iteration
        bar.next()
    # ignore progress and set everything to 100% and write finished
    bar.done("Finished!")
    # make a new bar
    bar = PyBar(poll=0.5)
    # like range, but automatically sets the max
    for i in bar.range(8888901, 8888999, 2):
        is_prime = True
        # track a second iterator
        bar2 = Tracker()
        # note again the max of the iterator is set automatically by using bar.range
        for a in bar.range(3, int(i/2), 2, tracker=bar2):
            # step forward the second iterator
            bar2.next()
            # update the bar information
            bar.update(
                        bar.progress(), bar.bar(), bar.rate(tracker=bar2, time=1),
                        bar.bar(tracker=bar2), bar.progress(tracker=bar2))
            # check for not prime number
            if i % a == 0:
                is_prime = False
                break
        # check for prime number
        if is_prime:
            # print a value above the bar without disrupting it
            bar.echo("[i] Prime number: ", i)
        # step the primary bar forwards
        bar.next()
    # complete all bars and say "Finished!"
    bar.done("Finished!", trackers=[bar2])
