import ConfigParser
from optparse import OptionParser

config = ConfigParser.SafeConfigParser()

parser = OptionParser()
parser.add_option("-c", "--config", dest="configFile", 
				  default="config.cfg",
				  help="The path to a config file ")
options, args = parser.parse_args()

config.read(options.configFile)

if config.has_option("rabbitmq", "server"):
	rabbitmq_server = config.get("rabbitmq", "server")
	rabbitmq_username = config.get("rabbitmq", "username")
	rabbitmq_password = config.get("rabbitmq", "password")
else:
	rabbitmq_server = "localhost"
	rabbitmq_username = ""
	rabbitmq_password = ""
	
print "rabbitmq_server", rabbitmq_server
