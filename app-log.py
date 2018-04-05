import logging
logging.basicConfig(level=logging.WARN,
    filename="log.txt",
    format="%(asctime)s=>%(levelname)s==>%(message)s")
logging.info("program strted")
a=raw_input("Enter a value:")
logging.info("a value give by user")
b=raw_input("Enter b value:")
logging.info("b value give by user")
print "a=%s, b=%s"%(a,b)
logging.debug("a=%s, b=%s"%(a,b))
try:
    a=float(a)
    logging.info("conversion a completed")
    b=float(b)
    logging.info("conversion b completed")
    logging.debug("After conversion: a=%s, b=%s"%(a,b))
    logging.info("calculating the result")
    res=a/b
    print "result=%s"%res
    logging.debug("result=%s"%res)

except ZeroDivisionError as err:
    logging.error("error:%s"%err)
    print "b value sould not be zero"
except ValueError as err:
    logging.error("error:%s"%err)
    print "Should enter only digits"
except Exception as err:
    logging.error("error:%s"%err)
    print "something went wrong"
finally:
    print "THIS IS FINALLY BLOCK"
logging.info("continuing the main block statements")
print "some main blcok statements"
print "other statements in program"
logging.info("program ended")
