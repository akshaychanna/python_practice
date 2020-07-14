import logging
a = 8
b = 0

try:
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.warning('Admin logged out')
    # logging.basicConfig(format='%(asctime)s -%(message)s', level = logging.INFO)
    # logging.info("heyy how are you")
    # # a/b
except Exception as e:
    logging.exception(e)
else:
    print("finally..!!!")