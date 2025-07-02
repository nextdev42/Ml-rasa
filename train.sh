#!/bin/bash

# Run rasa train inside the container


# Fix permissions (makes models editable by Gitpod)
sudo chown -R gitpod:gitpod /workspace/ml-rasa
