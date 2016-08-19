import sys
import parser
import validation as valid
import errors as err

# Main function
def run(input_parameters):
    try:
        execute()
    except:
        pass


#
def execute(input_parameters):
    try:
        initialize()
        in_data = sys.argv
        parser.parse_data(in_data)
        source = parser.get_source()
        dest = parser.get_dest()
        valid.check_path(source)
        valid.check_path(dest)
        in_rsync_str = create_rsync_string()
        run_rsync()
    except:
        pass

# Reset params, errors, init params, errors
def initialize():
    pass

# Create a string to run rsunc utility
def create_rsync_string():
    out_str = ''
    return out_str

# Run RSYNC
def run_rsync(input_rsync_string):
    pass

