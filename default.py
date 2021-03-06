######################## FUNCTIONS ##############################

from credentials import credentials
from multithread import multithread_engine
import initialize
import getpass


def default_interface():

	del initialize.credentials[:]
	controller = 'default_interface'
	initialize.credentials = credentials()
	multithread_engine(initialize.ntw_device,controller,initialize.credentials)
