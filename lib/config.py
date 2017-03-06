DEBUGGER = True
LOG_DIRECTORY = "/home/rohan/parser_files/YearlyLogFiles/"
OUTPUT_DIRECTORY = "/home/rohan/Desktop/"
STARTING_DATE = "2013-1-1"
ENDING_DATE = "2013-1-31"
MINIMUM_NICK_LENGTH = 3


# change to ["ALL"] if want to perform analysis over all channels
CHANNEL_NAME = ["#kubuntu-devel"]
# CHANNEL_NAME = ["ALL"]

# increase if using channel_user_presence
MAX_EXPECTED_DIFF_NICKS = 5000

# MAX_EXPECTED_DIFF_NICKS = 100000

# message_number_graph
THRESHOLD_MESSAGE_NUMBER_GRAPH = 0

#number of entries in log plot
NUMBER_OF_ENTRIES_IN_LOG_PLOTS = 20

#use pyplot
USE_PYPLOT = True

#Message Number CSV
BIN_LENGTH_MINS = 30

# channel_user_presence
STARTING_HASH_CHANNEL = 1000000
FILTER_FOR_CHANNEL_USER_GRAPH = 0
FILTER_FOR_CHANNEL_CHANNEL_GRAPH = 0
FILTER_FOR_USER_USER_GRAPH = 0
CHANNEL_USER_MAX_DEG = 1000
FILTER_TOP_USERS = 100
FILTER_TOP_CHANNELS = 30
GENERATE_DEGREE_ANAL = False
PRINT_CHANNEL_USER_HASH = False


# ConvL_ConvRT constants
MAX_CONVERSATIONS = 10000
HOURS_PER_DAY = 24
MINS_PER_HOUR = 60

# Response Time constants
RESPONSE_TIME_RANGE = 1000
MAX_RESPONSE_CONVERSATIONS = 200

# keyworkds
KEYWORDS_THRESHOLD = 0.01
KEYWORDS_MIN_WORDS = 100

# key_word_cluster
ENABLE_SVD = False
SHOW_N_WORDS_PER_CLUSTER = 10
ENABLE_ELBOW_METHOD_FOR_K = False
# NON ELBOW
NUMBER_OF_CLUSTERS = 11
# ELBOW SETTINGS
CHECK_K_TILL = 20
