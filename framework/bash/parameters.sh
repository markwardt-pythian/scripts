#!/bin/bash

function usage {
    echo " "
    echo "This is the bash parameters script usage"
    echo " "
    echo "Arguments:"
    echo "    -s            Description : Specify a parmater that you want to set to true"
    echo "    -a value      Desciprtion : Set parameter a and set it's value"
    echo "    -b value      Desciprtion : Set parameter a and set it's value"
    echo "    -c value      Desciprtion : Set parameter a and set it's value"
    echo " "
}

echo "OPTIND starts at $OPTIND"

# For getopts if the argument is expecting a value, follow it with a semicolon.  Otherwise do not follow it with a colon, like p
while getopts "a:b:c:sq:" optname
do
    case "$optname" in
        "s")
            echo "Option $optname is specified"
            ;;
        "a"|"b"|"c")
            echo "Option $optname has value $OPTARG"
            ;;
        "?")
            echo "Unknown option $OPTARG"
            ;;
        ":")
            echo "No argument value for option $OPTARG"
            ;;
        *)
        # Should not occur
        echo "Unknown error while processing options"
        ;;
    esac
    #echo "OPTIND is now $OPTIND"
done

usage
