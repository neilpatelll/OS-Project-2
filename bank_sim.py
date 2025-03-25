# ===========================
# Commit #1: Skeleton Code
# ===========================

import threading
import random
import time
from collections import deque

NUM_TELLERS = 3
NUM_CUSTOMERS = 50

door_sem = threading.Semaphore(2)      # Limits # of customers entering
safe_sem = threading.Semaphore(2)      # Up to 2 Tellers in safe
manager_sem = threading.Semaphore(1)   # Only 1 Teller at manager
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
assigned_teller = [-1]*NUM_CUSTOMERS  # Track which Teller is serving which Customer

def random_sleep(ms_min, ms_max):
    ms = random.randint(ms_min, ms_max)
    time.sleep(ms / 1000.0)

def teller_thread(tid):
    print(f"[Commit#1] Teller {tid} placeholder")

def customer_thread(cid):
    print(f"[Commit#1] Customer {cid} placeholder")

def main():
    random.seed(42)

    for _ in range(NUM_CUSTOMERS):
        sem_teller.append(threading.Semaphore(0))
        sem_customer.append(threading.Semaphore(0))
        transactions.append("")

    tellers = []
    for t in range(NUM_TELLERS):
        th = threading.Thread(target=teller_thread, args=(t,))
        tellers.append(th)
        th.start()

    customers = []
    for c in range(NUM_CUSTOMERS):
        ch = threading.Thread(target=customer_thread, args=(c,))
        customers.append(ch)
        ch.start()

    for ch in customers:
        ch.join()

    with queue_cv:
        queue_cv.notify_all()

    for th in tellers:
        th.join()

    print("[Commit#1] The bank closes for the day.")

if __name__ == "__main__":
    main()
