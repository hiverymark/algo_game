import time
import click
import numpy as np
import copy

from reference import reference, gen_data
import contestants

RESULT_FN = 'results.csv'
RESULT_COLS = 'contestant,n,run,time'
DQ_FN = 'dq.csv'
DQ_COLS = 'contestant'


@click.command()
@click.option('--start', default=1)
@click.option('--stop', default=100000)
@click.option('--num', default=100)
@click.option('--samples', default=3)
def main(start, stop, num, samples):
    funcs = {contestant[8:]: eval('contestants.'+contestant)
             for contestant in dir(contestants) if contestant.startswith('contest_')}
    ns = list(np.linspace(start=start, stop=stop, num=num, dtype=int))
    runs = range(samples)
    disqualified = set()
    clear_files()
    # Store references
    datas = dict()
    refs = dict()
    print('Running on funcs: {}'.format(str(funcs.keys())))
    print('with {} samples each'.format(samples))
    print('for ns: {}'.format(str(ns)))
    for contestant_name in funcs:
        for n in ns:
            for run in runs:
                contestant = funcs[contestant_name]
                if contestant_name in disqualified:
                    continue
                if (n, run) not in datas:
                    datas[n, run] = gen_data(n)
                    refs[n, run] = reference(datas[n, run])
                data = copy.copy(datas[n, run])
                ref = refs[n, run]
                if inner(n, run, contestant_name, contestant, data, ref):
                    disqualified.add(contestant_name)


def inner(n, run, contestant_name, contestant, data, ref):
    print('{}: n={} run {}'.format(contestant_name, n, run))
    start_time = time.time()
    res = contestant(data)
    end_time = time.time()
    if res != ref:
        print("{} has been disqualified!".format(contestant_name))
        write_dq(contestant_name)
        return True
    this_time = end_time - start_time
    write_res(contestant_name, n, run, this_time)
    return False


def clear_files():
    with open(RESULT_FN, 'w') as f:
        f.write(RESULT_COLS+'\n')
    with open(DQ_FN, 'w') as f:
        f.write(DQ_COLS+'\n')


def write_dq(contestant_name):
    with open(DQ_FN, 'a') as f:
        f.write(contestant_name+'\n')


def write_res(contestant_name, n, run, this_time):
    with open(RESULT_FN, 'a') as f:
        f.write('{},{},{},{}\n'.format(contestant_name, n, run, this_time))


if __name__ == '__main__':
    main()
