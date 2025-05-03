# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Install streamlit (if needed separately)
RUN pip install streamlit

# Copy the rest of your project files into the container
COPY . /app/

# Expose the port that Streamlit will run on
EXPOSE 5000

# Command to run your Streamlit app
# Command to run your Streamlit app on port 5000
CMD ["streamlit", "run", "app.py", "--server.port", "5000"]
