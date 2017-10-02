from multiprocessing import Pool


def part_crack_helper(args):
    solution = do_job(args)
    if solution:
        return True
    else:
        return False


class Worker():
    def __init__(self, workers, initializer, initargs):
        self.pool = Pool(processes=workers, initializer=initializer, initargs=initargs)

    def callback(self, result):
        if result:
            print "Solution found! Yay!"
            self.pool.terminate()

    def do_job(self):
        for args in product(seed_str, repeat=4):
            self.pool.apply_async(part_crack_helper, args=args, callback=self.callback)
        self.pool.close()
        self.pool.join()
        print "good bye"

if __name__ == '__main__':

    userame    = "admin"
    N_CPU = 2
    pool = mp.Pool(N_CPU)
    
    with open("/usr/share/wordlists/rockyou.txt") as passfile:
        w = Worker(N_CPU, init, [total_count])
        w.do_job()