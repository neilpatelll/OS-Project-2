# CS4348 Project 2 Development Log

**2025-03-23 11:00 AM**

**Session Goal:** Implement basic concurrency structure for Customers and Tellers.

**Thoughts:**
* Skeleton from Session 1 provides a base.
* Thinking about real-world simulation details (wait times, leaving).
* Need to decide on granularity of Teller-Customer interaction

**Plan:**
* Add thread creation for Customers and Tellers.
* Define necessary semaphores and mutexes.
* Implement Customer simulation loop (enter, wait, interact, leave)
* Implement Teller waiting and response logic
* Achieve basic multi-threaded execution for concurrency testing

**Progress:**
* Semaphore initialization issues encountered and resolved.
* Threads spawning, but output is chaotic; need thread IDs for logging.
* Tellers waiting; need a queue or signal mechanism for Customer assignment
* Considering a Manager thread for easier coordination.
* Thread naming for debugging purposes considered.
* Potential bug: Customer exits without service; semaphore signaling needs review.


**2025-03-24 11:55 PM**

**Session Summary:** Basic multi-threaded simulation with Customers and Tellers implemented.

**Reflection:**
* Multi-threaded Customer and Teller interaction achieved.
* Semaphores used for customer limit and Teller assignment
* Implementation is functional but messy.

**Bugs Encountered:**
* Semaphore reuse leading to deadlocks.
* Customer waiting indefinitely due to missing signals.
* Debugging thread-based code is challenging; added extensive logging.

**Remaining Tasks:**
* Manager thread logic is a placeholder.
* Logging needs improvement for readability.
* Implement "bank closing" scenario for proper thread termination.

**Next Session Goals:**
* Implement Manager thread for Teller-Customer oversight.
* Fine-tune semaphore handling to prevent edge cases.
* Implement Customer timeouts or max-wait logic.
* Clean up code and consolidate logic into functions.
