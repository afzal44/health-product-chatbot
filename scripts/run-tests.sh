#!/bin/bash

# Navigate to the tests directory
cd tests

# Run unit tests
echo "Running unit tests..."
pytest unit/

# Run integration tests
echo "Running integration tests..."
pytest integration/

# Optionally, you can add more commands to run specific tests or generate reports
echo "Tests completed."