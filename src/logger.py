import logging
import os
from datetime import datetime
LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,
)

'''
Ye code ek professional logging system banata hai jo aapke
ML project me errors, warnings, and events ko automatically files me 
save karta hai — taaki debugging fast aur easy ho jaye.
'''

'''Ye code Python ka logging system setup karta hai, jisse aapki application me hone wale events, errors, warnings ek .log file me save ho jayein.

Logging ka kaam:
✅ Errors ko record karna
✅ Program me kya ho raha hai track karna
✅ Debugging easy banana
✅ Production me system monitoring
'''
'''
filename → log kis file me save ho

format → log ka message kaise dikhe

level → INFO se upar wale saare logs save ho (INFO, WARNING, ERROR)
'''
'''
timestamp = kab log record hua

lineno = kaunsi line se log banaya

name = file ka naam

levelname = INFO / ERROR

message = hum jo likhte hain (logging.info("..."))'''
'''
ek logs directory banayega

uske andar ek timestamp-based folder banayega

usme ek .log file banayega

jitne bhi logs aap likhoge, wo us file me store hote jayenge'''