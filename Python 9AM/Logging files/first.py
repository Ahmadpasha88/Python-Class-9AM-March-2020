import logging
logging.basicConfig(filename="myerrorinfo.txt",level=logging.WARNING)
print("Logging module information:")
logging.debug("This is debugg message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.critical("This is critical message")
logging.error("This is error message")
