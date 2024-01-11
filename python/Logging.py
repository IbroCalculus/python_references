import logging

#Logging is a means of tracking events that happen when some software runs.
#Logging is important for software development, debugging and running.
#If you don't have any logging record and your program crashes, there are very little chances
# that you detect the cause of the problem

#PRINTING / LOGGING
#Printing may be used for logging purpose for simple scripts, but will fail for complex scripts.

#Can log to 5 different log levels. They indicat the severity of the event

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")
