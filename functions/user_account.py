import sys
import logging

# def entry_point():
#     return render_template('./app.html')

def hello():
    logging.info("premier hello")
    return "Hello Simplon"

if __name__ == "__main__":
    logging.basicConfig(filename="prog.log", level=logging.DEBUG)
    