# Logging module
# ---------------
#  |->Event - recording information about what is happening inside an application
#  ------
import logging

#logging.info("Processing data")
#logging.error("Error occurred")
'''
def f1(a,b):
    return a/b
print("Statring")
result = f1(10,0)
print("result=",result)
'''
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s %(message)s")

logging.info("App started")
logging.warning("This is warning")
logging.error("Something went wrong")
try:
    result = 10 / 0
except Exception:
    logging.exception("Error while performing division")
