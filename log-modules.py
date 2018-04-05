import logging
#logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.WARN)
logging.basicConfig(level=logging.DEBUG,
	filename="log.txt",
	format="%(asctime)s=>%(levelname)s==>%(message)s")
logging.error("Error message")
logging.info("info message")
logging.debug("Debug message")
logging.warn("Warning message")