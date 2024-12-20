#!/bin/bash

# Prompt for the Django app name
read -p "Enter the Django app name: " app_name

# Check if the app name is empty
if [ -z "$app_name" ]; then
  echo "App name cannot be empty. Please provide a valid Django app name."
  exit 1
fi

# Run makemigrations for the specified app
echo "Running makemigrations for app '$app_name'..."
python manage.py makemigrations "$app_name"

# Check if makemigrations was successful
if [ $? -ne 0 ]; then
  echo "makemigrations failed. Please check your app name and try again."
  exit 1
fi

# Run migrate
echo "Running migrate..."
python manage.py migrate "$app_name"

# Check if migrate was successful
if [ $? -ne 0 ]; then
  echo "migrate failed. Please check your configuration and try again."
  exit 1
fi

echo "Migrations completed successfully for app '$app_name'."
