#!/bin/bash


function test27 {
    echo "Starting tests..."
    make test-docker-27
    if [ $? == 0 ]
    then
        echo "Tests finished."
    else
        exit 1
    fi
}


function test35 {
    echo "Starting tests..."
    make test-docker-35
    if [ $? == 0 ]
    then
        echo "Tests finished."
    else
        exit 1
    fi
}


case "$1" in
    test27)
        test27
        exit 0
    ;;
    test35)
        test35
        exit 0
esac

exec "$@"
