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

**During Coding Notes (random thoughts + live log):**

* Okay, forgot how annoying semaphores can be—spent 15 minutes realizing I had initialized one with the wrong value.
* Threads are spawning but feels like a chaotic mess. Gonna need to print logs with thread IDs so I know who's doing what.
* Tellers are just chilling… waiting on customers who haven’t been released yet. Think I need a queue or at least a signal mechanism.
* Considering using a manager thread to simulate opening the bank and controlling flow—it might make coordination easier.
* Wondering if I should name my threads for easier debugging—like “Teller-1” or “Customer-3.”
* Possible bug: sometimes it looks like a customer exits without being served. I think the semaphore signaling isn't aligned right. Might have to introduce a waiting room or condition variable.


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


**2025-03-25 8:11 AM**

**Goal:** Add concurrency logic and print statements for Customer and Teller interaction.
* Realized I was getting ahead of myself in session 1 trying to do concurrency logic then. Decided to hold it off till this commit and go for just a simple skeleton code for that commit. 
* Added a simple print statement to see if the teller is working correctly for commit 1. But devlog says otherwise. 

**Initial Goal That I Had in Mind:** Set up the initial structure for the bank simulator project. Got ahead and tried moving too quick, but just did simple.

**Thoughts:**
* Conceptualizing a bank simulation with concurrent Customers and Tellers.
* Planning to utilize semaphores for synchronization and resource management.
* Focusing on establishing the project skeleton, deferring complex behavior and edge cases.
* Considering the inclusion of simulated resources like a safe or vault, and the level of transaction detail.

**Plan:**
* Establish global data structures and include necessary libraries.
* Create placeholder thread functions for Tellers and Customers.
* Define enums, constants, and initial shared variables.
* Outline the high-level program flow for future logic implementation.
* Maintain code organization with comments indicating areas for future development.

**Progress:**
* Created function stubs for Teller and Customer threads.
* Set up the basic main structure with initialization and placeholder thread creation.
* Added initial global variables and outlined the placement of semaphores and mutexes.
* Included comments to guide future steps, particularly regarding concurrency and resource access.

**Session End of First Commit**

**Session Summary:** Project skeleton created with key components outlined and ready for implementation.

**Reflection:**
* Satisfied with the established base, which should facilitate smoother concurrency logic implementation in the next session.
* No bugs or significant roadblocks encountered during setup.
* The next session will involve implementing actual logic, including semaphore initialization, thread communication, and Teller-Customer interaction.
* Thinking about a manager thread for future flow control.

**Next Session Goals:**
* Implement thread logic and concurrency using semaphores and mutexes.
* Simulate basic Customer entry, service, and exit flow.
* Establish a structure for managing limited resources (e.g., safe, teller availability).
* Begin planning logging and output format for thread behavior tracing.

**Actual Session Start 2025-03-25 01:00 PM**

**Thoughts:**
* Ready to move beyond placeholders want Customers and Tellers to actually "do something."
* Thinking about using a queue or signaling system so Tellers can serve Customers in order
* Debating how much to simulate—right now, print-based feedback seems easiest to trace
* Want to make sure I can actually visualize what's happening in the threads—logging is key

**Plan:**
* Set up semaphores to control access and coordination between Customers and Tellers
* Implement thread logic for Tellers to wait for Customers
* Create simulation where Customers can request a service (deposit/withdraw)
* Add logging to reflect entry, service, and exit events.
* Ensure threads are not interfering with each other—introduce mutexes where needed.

**Progress:**
* Implemented semaphores for coordination; adjusted their initial values a few times.
* Basic thread logic works—Customers arrive, Tellers respond.
* Added random sleep durations to simulate realistic service time.
* Ran into a race condition where Tellers helped the same Customer—added mutexes to resolve.
* Created unique logging output so it's easier to follow which Customer is being served by which Teller.

**During Coding Notes (random thoughts + live log):**
* Tellers now wait on a semaphore and respond when a Customer is ready—finally feels like a real simulation
* Thought about adding thread names like "Teller-1" or "Customer-2" and it’s helping a lot with print debugging.
* Mutex helped solve the double-helping issue. Didn’t realize two Tellers could pick the same Customer so easily
* Tempted to rewrite a lot already, but trying to get something functional first.
* The current log output looks like a little story—unexpectedly fun to watch it play out
* Accidentally had a Customer exit before being served—added a "wait-for-service" semaphore for proper sequencing.

**2025-03-25 06:30 PM - Session End**

**Session Summary:** Basic concurrency flow between Customers and Tellers implemented using semaphores and threads

**Reflection:**
* Tellers now properly wait and serve incoming Customers.
* Print logs show synchronized flow of activity; easy to trace
* Still early, but it’s already highlighting how tricky thread sync can be
* Mutexes and semaphores are working together—though the logic isn’t very clean yet

**Bugs Encountered:**
* Double-service by Tellers due to lack of synchronization—fixed with mutex
* Semaphore misinitialization led to Customers entering but no Teller response.
* Random delays helped visualize the concurrency better but also introduced timing inconsistencies I had to account for.

**Remaining Tasks:**
* Code needs some structural cleanup—too much is in main right now.
* Add a manager or controller thread to handle flow (eg opening/closing the bank)
* Improve handling of corner cases, like no Tellers available or Customer timeout scenarios

**Next Session Goals:**
* Abstract logic into cleaner functions for readability
* Add a Manager thread to better control bank behavior and flow.
* Possibly simulate a maximum wait time for Customers
* Begin thinking about final formatting of output and structure.

**2025-03-26 10:00 AM - Session Start**

**Goal:** Final polish—improve comments and output formatting for clarity and submission readiness.

**Thoughts:**
* Core concurrency logic is stable and functioning correctly.
* Stable runs show proper customer flow: enter, serve, leave.
* Focus on cleanup and formatting, no structural changes required.
* Aim to enhance print statement readability for potential grader expectations.

**Plan:**
* Review and comment each code section, particularly thread logic and synchronization.
* Standardize print messages for clearer thread activity understanding.
* Execute final test cases to ensure consistency and expected behavior.
* Verify output reflects all major steps: arrival, waiting, service, departure.
* Remove unused variables, test code, and debug print statements.

**Progress:**
* Reworded print statements for clarity (e.g., "Customer 1 enters the bank").
* Added concise comments above major code blocks, especially thread functions.
* Verified correct semaphore initialization and destruction.
* Final test runs produced clean, ordered logs without race conditions.
* Retained thread IDs and role names (e.g., "Teller-2") for easy tracking.

**During Coding Notes (random thoughts + live log):**
* Okay, final stretch—just cleaning things up.
* First thing I noticed: some of my print statements feel robotic. Rewriting them to feel more natural/readable.
* “Customer enters the bank” vs “Customer X has entered” — going with the second one, it just flows better
* Saw a couple comments that just say // TODO… yeah, not doing those anymore. Deleting
* Realized I had three different variations of the word “serving” in my print logs—standardizing that
* Should probably add a quick comment before each semaphore declaration just in case someone else reads this.
* This code is surprisingly readable considering it started as chaos lol.
* Every time I test the output, it feels like a little play—Tellers popping up, Customers flowing through
* Tempted to add some extra spacing to make the output look nicer… okay fine, added a few \ns
* Added a small debug log toggle—just commented it out for now, but nice to have in case I want to trace it deeper.
* Code compiles, prints look good, no weird overlaps—nice.
* Removed that random printf("debug\n"); from line 78 that I forgot about
* Okay, pretty sure I’m done now... going to run it one more time just for peace of mind.
* Final test run looks great output is clean, no errors.

**2025-03-27 5:00 PM - Session End**

**Session Summary:** Completed final polishing of code and output formatting. Ready for submission.

**Reflection:**
* Code structure is clear, output is readable, and comments are concise.
* Confident the program demonstrates intended concurrency behavior with semaphores and threads.
* No unexpected issues encountered, focused on quality-of-life improvements.
* Satisfied with the outcome; potential for future enhancements (timeouts, GUI, complex logic).

**Next Steps (Post-Submission Thoughts):**
* Project completion for now.
* Future enhancements could include thread flow visualization with timestamps or customer impatience simulation.

**Final Notes (Post-Final Session Random Thoughts):**
* Feels good seeing Customers and Tellers interacting like a real simulation.
* Still can't believe how tricky semaphores can be when they're just off by one
* Adding thread names made the whole thing so much easier to follow—never skipping that again.
* Mutexes saved the day more than once.
* Output kinda reads like a play: “Teller-2 serves Customer-5". pretty fun to watch.
* Wish I had more time to add features like timeouts or stats.
* Might revisit this later just to add some extras, like tracking wait time or doing a GUI.
* For now, code runs clean, output makes sense, no deadlocks. That’s a win.
* Submitting this and taking a break, my brain’s been in sort of thread land all week