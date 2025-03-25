# ===========================
# Commit #2: Concurrency Logic
# ===========================

import threading
import random
import time
from collections import deque

NUM_TELLERS = 3
NUM_CUSTOMERS = 50

door_sem = threading.Semaphore(2)
safe_sem = threading.Semaphore(2)
manager_sem = threading.Semaphore(1)
queue_lock = threading.Lock()
queue_cv = threading.Condition(queue_lock)
customer_queue = deque()

served_lock = threading.Lock()
customers_served = 0
simulation_done = False

tellers_ready_count = 0
tellers_ready_lock = threading.Lock()
bank_open_event = threading.Event()

sem_teller = []
sem_customer = []
transactions = []
assigned_teller = [-1]*NUM_CUSTOMERS

def random_sleep(ms_min, ms_max):
    ms = random.randint(ms_min, ms_max)
    time.sleep(ms / 1000.0)

def teller_thread(tid):
    global tellers_ready_count, simulation_done, customers_served

    print(f"Teller {tid} []: ready to serve")
    print(f"Teller {tid} []: waiting for a customer")

    with tellers_ready_lock:
        tellers_ready_count += 1
        if tellers_ready_count == NUM_TELLERS:
            bank_open_event.set()

    while True:
        with served_lock:
            if customers_served >= NUM_CUSTOMERS:
                simulation_done = True
                with queue_cv:
                    queue_cv.notify_all()
                break

        with queue_cv:
            while not customer_queue and not simulation_done:
                queue_cv.wait()
            if simulation_done:
                with served_lock:
                    if customers_served >= NUM_CUSTOMERS:
                        break
            if customer_queue:
                cust_id = customer_queue.popleft()
            else:
                continue

        assigned_teller[cust_id] = tid
        print(f"Teller {tid} [Customer {cust_id}]: serving a customer")
        sem_customer[cust_id].release()

        sem_teller[cust_id].acquire()
        print(f"Teller {tid} [Customer {cust_id}]: asks for transaction")
        sem_customer[cust_id].release()

        sem_teller[cust_id].acquire()
        txn_type = transactions[cust_id]
        if txn_type == "Withdraw":
            print(f"Teller {tid} [Customer {cust_id}]: handling withdrawal transaction")
            print(f"Teller {tid} [Customer {cust_id}]: going to the manager")
            print(f"Teller {tid} [Customer {cust_id}]: getting manager's permission")
            manager_sem.acquire()
            random_sleep(5, 30)
            manager_sem.release()
            print(f"Teller {tid} [Customer {cust_id}]: got manager's permission")
        else:
            print(f"Teller {tid} [Customer {cust_id}]: handling deposit transaction")

        print(f"Teller {tid} [Customer {cust_id}]: going to safe")
        print(f"Teller {tid} [Customer {cust_id}]: enter safe")
        safe_sem.acquire()
        random_sleep(10, 50)
        print(f"Teller {tid} [Customer {cust_id}]: leaving safe")
        safe_sem.release()

        if txn_type == "Withdraw":
            print(f"Teller {tid} [Customer {cust_id}]: finishes withdrawal transaction.")
        else:
            print(f"Teller {tid} [Customer {cust_id}]: finishes deposit transaction.")

        print(f"Teller {tid} [Customer {cust_id}]: wait for customer to leave.")
        sem_customer[cust_id].release()

        sem_teller[cust_id].acquire()

        with served_lock:
            customers_served += 1
            if customers_served >= NUM_CUSTOMERS:
                simulation_done = True
                with queue_cv:
                    queue_cv.notify_all()
                break

        print(f"Teller {tid} []: ready to serve")
        print(f"Teller {tid} []: waiting for a customer")

    print(f"Teller {tid} []: leaving for the day")

def customer_thread(cid):
    txn_type = random.choice(["Deposit", "Withdraw"])
    transactions[cid] = txn_type

    if txn_type == "Deposit":
        print(f"Customer {cid} []: wants to perform a deposit transaction")
    else:
        print(f"Customer {cid} []: wants to perform a withdrawal transaction")

    random_sleep(0, 100)

    print(f"Customer {cid} []: going to bank.")
    bank_open_event.wait()
    print(f"Customer {cid} []: entering bank.")
    door_sem.acquire()

    print(f"Customer {cid} []: getting in line.")
    with queue_cv:
        customer_queue.append(cid)
        queue_cv.notify()

    sem_customer[cid].acquire()
    teller_id = assigned_teller[cid]
    print(f"Customer {cid} []: selecting a teller.")
    print(f"Customer {cid} [Teller {teller_id}]: selects teller")

    print(f"Customer {cid} [Teller {teller_id}] introduces itself")
    sem_teller[cid].release()

    sem_customer[cid].acquire()
    if txn_type == "Withdraw":
        print(f"Customer {cid} [Teller {teller_id}]: asks for withdrawal transaction")
    else:
        print(f"Customer {cid} [Teller {teller_id}]: asks for deposit transaction")
    sem_teller[cid].release()

    sem_customer[cid].acquire()
    print(f"Customer {cid} [Teller {teller_id}]: leaves teller")
    print(f"Customer {cid} []: goes to door")
    print(f"Customer {cid} []: leaves the bank")

    sem_teller[cid].release()
    door_sem.release()

def main():
    random.seed(42)

    for _ in range(NUM_CUSTOMERS):
        sem_teller.append(threading.Semaphore(0))
        sem_customer.append(threading.Semaphore(0))
        transactions.append("")

    t_threads = []
    for t in range(NUM_TELLERS):
        th = threading.Thread(target=teller_thread, args=(t,))
        t_threads.append(th)
        th.start()

    c_threads = []
    for c in range(NUM_CUSTOMERS):
        ch = threading.Thread(target=customer_thread, args=(c,))
        c_threads.append(ch)
        ch.start()

    for ch in c_threads:
        ch.join()

    with queue_cv:
        queue_cv.notify_all()

    for th in t_threads:
        th.join()

    print("The bank closes for the day.")

if __name__ == "__main__":
    main()